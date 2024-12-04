from random import randint
print("\tBataille Aléatoire")

SANTE_JOUEUR = 50
SANTE_ENNEMI = 50
NBRE_DE_POTION = 3

while (SANTE_JOUEUR > 0 and SANTE_ENNEMI > 0):
    choix = ""
    while not choix in ["1", "2"] :
        choix = input("Souhaitez-vous attaquer (1) ou utiliser une potion (2) ? : ")
        if choix == '1':
            mon_attaq = randint(5, 10)
            SANTE_ENNEMI -= mon_attaq
            son_attaq = randint(5, 15)
            SANTE_JOUEUR -= son_attaq
            if (SANTE_ENNEMI > 0 and SANTE_JOUEUR > 0 ) :
                print(f"Vous avez infligé {mon_attaq} points de dégats à l'ennemi ⚔ ")
                print(f"L'ennemi vous a infligé {son_attaq} points de dégats ⚔ ")
                print(f"Il vous reste {SANTE_JOUEUR} points de vie ")
                print(f"Il reste {SANTE_ENNEMI} points de vie à l'ennemi")
                print("-" *50)
            elif(SANTE_ENNEMI <=0 and SANTE_JOUEUR > 0) :
                print(f"Vous avez infligé {mon_attaq} points de dégats à l'ennemi ⚔ ")
                print("Tu as gagné 💪")
            else:
                print("Vous avez perdu 😞")
        elif choix == '2':
            if NBRE_DE_POTION > 0:
                for i in range(1, 3):
                    if i==1 :
                        NBRE_DE_POTION -= 1
                        son_attaq = randint(5, 15)
                        point_potion = randint(15, 50)
                        SANTE_JOUEUR += point_potion
                        SANTE_JOUEUR -= son_attaq
                        if (SANTE_JOUEUR > 0 and SANTE_ENNEMI > 0) :
                            print(f"Vous récupérez {point_potion} points de vie 💖 ({NBRE_DE_POTION} 🧪 restantes)")
                            print(f"L'ennemi vous a infligé {son_attaq} points de dégats ⚔ ")
                            print(f"Il vous reste {SANTE_JOUEUR} points de vie ")
                            print(f"Il reste {SANTE_ENNEMI} points de vie à l'ennemi")
                            print("-" *50)
                        elif(SANTE_ENNEMI <=0 and SANTE_JOUEUR > 0) :
                            print(f"Vous avez infligé {mon_attaq} points de dégats à l'ennemi ⚔ ")
                            print("Tu as gagné 💪👍")
                        else:
                            print("Vous avez perdu 😞")
                    elif i==2 :
                        son_attaq = randint(5, 15)
                        SANTE_JOUEUR -= son_attaq
                        if (SANTE_JOUEUR > 0 and SANTE_ENNEMI > 0) :
                            print("Vous passez votre tour...")
                            print(f"L'ennemi vous a infligé {son_attaq} points de dégats ⚔ ")
                            print(f"Il vous reste {SANTE_JOUEUR} points de vie ")
                            print(f"Il reste {SANTE_ENNEMI} points de vie à l'ennemi")
                            print("-" *50)
                        elif(SANTE_ENNEMI <=0 and SANTE_JOUEUR > 0) :
                            print(f"Vous avez infligé {mon_attaq} points de dégats à l'ennemi ⚔ ")
                            print("Tu as gagné 💪")
                        else:
                            print("Vous avez perdu 😞")
            else:
                print("Vous n'avez plus de potion...")
print("Fin du jeu")