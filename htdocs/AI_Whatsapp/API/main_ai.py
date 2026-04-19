from playwright.sync_api import sync_playwright
import time
import re
import json
import os
import __init__

from API.AI_Query.main import research_by_gemini_auto, update_request_count
from API.Minigames.manage_game import Manage

# whitelist mémoire
WHITELIST_FILE = "whitelist.json"

if os.path.exists(WHITELIST_FILE):
    with open(WHITELIST_FILE, "r") as f:
        WHITELIST = set(json.load(f))
else:
    WHITELIST = set()

def save_whitelist():
    with open(WHITELIST_FILE, "w") as f:
        json.dump(list(WHITELIST), f)

def send_message(page, text):
    input_box = page.locator("div[contenteditable='true']").last
    input_box.click()
    input_box.fill(text)
    input_box.press("Enter")

def extract_sender(meta):
    # format: [17:21, 16/04/2026] Nom:
    match = re.search(r"\]\s(.*?):", meta)
    return match.group(1) if match else "Inconnu"

def get_last_message(page)->tuple[str|None, str|None]:
    messages = page.locator("div[data-pre-plain-text]").all()
    last_message = None
    last_sender = None

    for msg in messages:
        try:
            meta = msg.get_attribute("data-pre-plain-text") or ""
            text = msg.inner_text().strip()

            if text:
                last_message = text
                last_sender = extract_sender(meta)

        except:
            pass
    return last_message, last_sender

def waiting_for_message(page, choices):
    """ Attente active d'un message spécifique dans la conversation.
    Verifie régulièrement les nouveaux messages et retourne dès qu'un message correspond à l'une des options spécifiées.

    Args:
        page (_type_): _description_
        choices (_type_): _description_

    Returns:
        _type_: _description_
    """
    while True:
        print("Attente d'un nouveau message...")
        time.sleep(1)
        last_message, last_sender = get_last_message(page)
        print(f"Teste si : {last_message} in : {choices}")

        if type(last_message) == str:
            text_lower = last_message.lower()
            if text_lower in choices:
                return last_message, last_sender
            
        if last_message in choices:
            return last_message, last_sender

def refresh_request_count(query=True):
    update_request_count(query)

    with open("API/AI_Query/request_nb.txt", "r") as f:
        number_request = f.read().split(":")[1] # Récupère uniquement le nombre de requêtes, pas le jour
    return number_request

def run():
    
    with sync_playwright() as p:
        context = p.chromium.launch_persistent_context(
            user_data_dir="whatsapp_session",  # dossier local
            headless=False
        )

        page = context.new_page()

        page.goto("https://web.whatsapp.com")        
        print("Ouverture automatique de WhatsApp Web. (Scanne le QR code si nécessaire.)")
        
        time.sleep(5)

        number_request = 0
        last_text = ""
        while True:
            try:
                print("\n--- Vérification ---")

                # attendre que les messages soient chargés
                page.wait_for_selector("header")

                last_message, last_sender = get_last_message(page)  # rafraîchir les messages

                if not last_message:
                    time.sleep(2)
                    continue

                print(f"Dernier message : {last_message}")
                print(f"Envoyé par : {last_sender}")

                # éviter double traitement
                if last_message == last_text:
                    time.sleep(2)
                    continue

                last_text = last_message

                text_lower = last_message.lower()

                # =========================
                # HELP
                # =========================
                if text_lower.startswith("/ia -help"):
                    number_request = refresh_request_count(query=False)  # Rafraîchir le nombre de requêtes sans l'incrémenter
                    response = (
                        "🤖 IA : Commandes disponibles (syntaxe générale /ia -option):\n"
                        "*/ia -login* : S'ajouter à la whitelist\n"
                        "*/ia -logout* : Se retirer de la whitelist\n"
                        "*/ia -play* : Jouer à un mini-jeu\n"
                        f"*/ia -question <Votre question>*: Poser une question (limitée: {number_request}/20)\n"
                        "*/ia -help* : Aide"
                    )
                    send_message(page, response)

                # =========================
                # LOGIN WHITELIST
                # =========================
                elif text_lower.startswith("/ia -login"):
                    username = last_sender  # pseudo automatique

                    if username in WHITELIST:
                        send_message(page, f"ℹ️ IA : {username} est déjà dans la whitelist")
                    else:
                        WHITELIST.add(username)
                        save_whitelist()
                        send_message(page, f"🤖 IA : {username} ajouté à la whitelist ✅")

                    print(f"Whitelist actuelle : {WHITELIST}")

                # =========================
                # LOGOUT WHITELIST
                # =========================
                elif text_lower.startswith("/ia -logout"):
                    username = last_sender  # pseudo automatique

                    if username in WHITELIST:
                        WHITELIST.remove(username)
                        save_whitelist()
                        send_message(page, f"🤖 IA : {username} retiré de la whitelist ✅")
                    else:
                        send_message(page, f"ℹ️ IA : {username} n'est pas dans la whitelist")

                    print(f"Whitelist actuelle : {WHITELIST}")


                #==========================
                # Minigames
                #==========================
                elif text_lower.startswith("/ia -play"):                    
                    Manage(page, get_last_message, send_message, waiting_for_message)


                # =========================
                # IA QUERY
                # =========================
                elif text_lower.startswith("/ia -question"):
                    question = last_message.replace("/ia -question ", "", 1).strip()

                    if last_sender not in WHITELIST:
                        response = f"❌ IA : {last_sender} n’est pas autorisé"
                    else:                        
                        #send_message(page, "🤖 IA : Vérification de la disponibilité du modèle...")
                        answer = research_by_gemini_auto(question, page, waiting_for_message, send_message, get_last_message)
                        response = f"🤖 IA ({last_sender}) : {answer}"

                    send_message(page, response)
                
                elif text_lower.startswith("/ia"):
                    send_message(page, "❌ IA : Commande inconnue. Tapez /ia -help pour la liste des commandes.")

            except Exception as e:
                print("Erreur :", e)

            time.sleep(1)

if __name__ == "__main__":
    run()