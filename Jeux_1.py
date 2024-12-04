from random import randint

NOMBRE_ALEATOIRE = randint(0, 100)
NOMBRES_D_ESSAI = 5

print(" \tLe jeu du nombre mystère ")
print("Vous avez à deviner un nombre entre 0 et 100 😁")
print("Vous avez 5 essais\n")

while NOMBRES_D_ESSAI > 0:
    print(f"Il vous reste {NOMBRES_D_ESSAI} essai{'s' if NOMBRES_D_ESSAI > 1 else ''}")
    nombre_deviné = input("Deviner le nombre: ")
    if nombre_deviné == "" or nombre_deviné == " ":
        print("Vous n'avez rien saisie.")
    if not nombre_deviné.isdigit():
        print("Veuillez entrer un nombre valide.")
        continue

    nombre_deviné = int(nombre_deviné)
    if nombre_deviné < NOMBRE_ALEATOIRE:
        print(f"Le nombre mystère est plus grand que {nombre_deviné}")
    elif nombre_deviné > NOMBRE_ALEATOIRE:
        print(f"Le nombre mystère est plus petit que {nombre_deviné}")
    else:
        break
    NOMBRES_D_ESSAI -= 1
print("_" *50)

if NOMBRES_D_ESSAI == 0:
    print(f"Dommage 😔 ! Le nombre mystère était {NOMBRE_ALEATOIRE}.")
else :
    print(f"Bravo ! 👍 Le nombre mystère était bien {NOMBRE_ALEATOIRE}.")
    print(f"Tu l'a trouvé en {6 - NOMBRES_D_ESSAI} essai{'s' if NOMBRES_D_ESSAI>1 else ''}.")
print("\tFIN DU JEU")