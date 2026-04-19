from google import genai
from dotenv import load_dotenv
import os

load_dotenv("API/AI_Query/api.env")
print("Clé API chargée :", os.getenv("GEMINI_API_KEY") is not None)
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def get_model():
    MODELS = [
        "gemini-3.0-flash",
        "gemini-2.5-flash",
        "gemini-2.0-flash",
        "gemini-1.5-flash",
    ]
    for model in MODELS:
        try:
            client.models.generate_content(model=model, contents="Test de disponibilité")
            return model
        except Exception as e:
            print(f"Modèle {model} indisponible : {e}")
            continue
    raise Exception("Aucun modèle disponible")

def check_day():
    from datetime import datetime
    now = datetime.now()
    print(f"Date actuelle : {now.day}")
    return now.day

def update_request_count(query=True):
    day = check_day()
    with open("API/AI_Query/request_nb.txt", "r") as f:
        day_saved, number_request = f.read().split(":")
        
    if day_saved != str(day):
        number_request = 0
    elif query:
        number_request = int(number_request)+1

    with open("API/AI_Query/request_nb.txt", "w") as f:
        f.write(f"{day}:{number_request}")

def research_by_gemini_auto(text, page=None, waiting_for_message=None, send_message=None, get_last_message=None):
    model = "gemini-2.5-flash"  # Vérifie la disponibilité du modèle avant de faire la requête
    print(f"Utilisation du modèle : {model}\n")

    if send_message:
        send_message(page, "🤖 IA : Recherche en cours...")
    try:
        response = client.models.generate_content(
            model=model,
            contents=text
        )


        if send_message:
            send_message(page, "Recherche terminée. Voulez-vous voir la réponse ? (o/n)")
        if waiting_for_message:
            waiting_for_message(page, ["o", "n"])
        
        update_request_count()  # Incrémente le nombre de requêtes après une requête réussie
        print(f"Utilisation du modèle : {model}")
        return response.text

    except Exception as e:
        print(f"Échec avec {model} : {e}")


if __name__ == "__main__":
    check_day()
    