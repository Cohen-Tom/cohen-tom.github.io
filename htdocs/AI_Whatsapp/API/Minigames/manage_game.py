import time

def Manage(page, get_last_message, send_message, waiting_for_message):
    print("inside manage")
    from API.Minigames.AI_findNumber.main import find_number
    from API.Minigames.AI_RockPaperScissors.main import rock_paper_scissors
    
    games = ["Guess the number", "Rock paper scissors", "Leave"]
    choices = []
    
    send_message(page, "🤖 IA : Choisissez un jeu (ecrivez '/cancel' pour quitter le jeu):")
    for i, elm in enumerate(games):
        send_message(page, f"({i + 1}) : {elm}")
        choices.append(str(i + 1))
        time.sleep(1)
    
    last_message, last_sender = waiting_for_message(page, choices)
        
    if last_message == "1":
        print(f"Lancement du jeu Guess the number par {last_sender} !")
        send_message(page, "🤖 IA : Guess the number !")
        find_number(page, get_last_message, send_message)
            
    elif last_message == "2":
        print(f"Lancement du jeu Rock paper scissors par {last_sender} !")    
        send_message(page, "🤖 IA : Rock paper scissors !")
        rock_paper_scissors(page, get_last_message, send_message, waiting_for_message)
    
    elif last_message == "3":
        send_message(page, "🤖 IA : Retour au menu principal.")
        return