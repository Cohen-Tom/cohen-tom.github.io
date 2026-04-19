def find_number(page, get_last_message, send_message):
    import random
    import time
    
    rand_min, rand_max = random.randint(1, 500), random.randint(501, 1000)
    number = random.randint(rand_min, rand_max)
    
    last_guess = ""
    
    response = ("🤖 IA : Veuillez entrer un nombre valide.")
    send_message(page, response)
    
    find = False
    
    while not find:
        time.sleep(1)  # éviter de spammer
        
        # Récupérer le dernier message et son expéditeur
        last_message, last_sender = get_last_message(page)  # rafraîchir les messages

        if not last_message:
            time.sleep(2)
            continue

        print(f"Dernier message : {last_message}")
        print(f"Envoyé par : {last_sender}")

        # éviter double traitement
        if last_message == last_guess:
            time.sleep(2)
            continue

        last_guess = last_message
        
        print(f"Nombre proposé : {last_guess} par {last_sender}")
        
        try:
            if last_guess == "/cancel":
                find = True
                send_message(page, "🤖 IA : Jeu annulé.")
            guess = int(last_guess)
        except ValueError:
            continue

        if guess < number:
            response = (f"🤖 IA : Trop petit ! ({last_sender}, valeur proposée : {guess})")
            send_message(page, response)
        elif guess > number:
            response = (f"🤖 IA : Trop grand ! ({last_sender}, valeur proposée : {guess})")
            send_message(page, response)
        else:
            response = (f"🤖 IA : Félicitations ! Vous avez trouvé le nombre ({last_sender}, valeur correcte : {number})")
            send_message(page, response)
            find = True