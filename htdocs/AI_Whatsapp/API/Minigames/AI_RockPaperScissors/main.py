from random import choices

def rock_paper_scissors(page, get_last_message, send_message, waiting_for_message):
    import random
    import time
    
    choices = ["pierre", "papier", "ciseaux", "/cancel"]
    
    response = ("🤖 IA : Combien de parties voulez-vous jouer ?(max 10)")
    send_message(page, response)
    
    last_text, last_sender = waiting_for_message(page, [str(i) for i in range(1, 11)])
    
    try:
        rounds = int(last_text)
    except ValueError:
        send_message(page, "🤖 IA : Veuillez entrer un nombre valide.")
        return
    send_message(page, f"🤖 IA : Très bien, nous allons jouer {rounds} parties !")
    
    for round in range(rounds):
        asking = f"🤖 IA : Partie {round + 1} - Choisissez entre pierre, papier ou ciseaux :"
        send_message(page, asking)
        
        user_choice, last_sender = waiting_for_message(page, choices)
        user_choice = user_choice.lower()
        
        ai_choice = random.choice(choices[:-1])
        
        if user_choice == "/cancel":
            send_message(page, "🤖 IA : Jeu annulé.")
            return
        
        elif user_choice == ai_choice:
            send_message(page, f"🤖 IA : Égalité ! Vous avez choisi {user_choice} et l'IA a choisi {ai_choice}.")
            
        elif (user_choice == "pierre" and ai_choice == "ciseaux") or (user_choice == "papier" and ai_choice == "pierre") or (user_choice == "ciseaux" and ai_choice == "papier"):
            send_message(page, f"🤖 IA : Vous gagnez ! Vous avez choisi {user_choice} et l'IA a choisi {ai_choice}.")
            
        else:
            send_message(page, f"🤖 IA : L'IA gagne ! Vous avez choisi {user_choice} et l'IA a choisi {ai_choice}.")