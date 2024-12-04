from tkinter import *

# couleurs
couleurs = ["white", "black", "blue", "green"]

# Paramétrage de la fenêtre
fen = Tk()
fen.geometry("256x311+0+0")
fen.config(background=couleurs[1])
fen.title("Calculatrice")
result = ""
#Fonctions associées
calcul = ""
def affiche(x):
    global calcul
    calcul = str(x)
    ecran_1.insert(END, calcul)

def efface():
    ecran_1.delete(1.0, END)
    ecran_1.insert(1.0, "")
    ecran_2.config(text="")

def  calcule_simple():
    global result
    try:
        result = str(eval(ecran_1.get(1.0, END)))
        ecran_1.delete(1.0, END)
        ecran_1.insert(1.0, result)
        ecran_2.config(text= result)
    except:
        ecran_2.config(text="Erreur de calcul !")
    
def calcule_retirer():
    ecran_1.delete(1.0, END)
    lettre = [ecran_1.get(1.0, END).split()]
    lettre.pop(-1)
    "".join(lettre)
    ecran_1.insert(1.0, lettre)

def calcule_pourcent():
    result = (float(str(eval(ecran_1.get(1.0, END))))/100)
    ecran_1.delete(1.0, END)
    ecran_1.insert(1.0, result)
    ecran_2.config(text= str(result)+"%")

def calcule_inverse():
    result = (1/float(str(eval(ecran_1.get(1.0, END)))))
    ecran_1.delete(1.0, END)
    ecran_1.insert(1.0, result)
    ecran_2.config(text= result)

def calcule_carré():
    result = (float(str(eval(ecran_1.get(1.0, END))))**2)
    ecran_1.delete(1.0, END)
    ecran_1.insert(1.0, result)
    ecran_2.config(text= result)

def calcule_racine_carré():
    if float(str(eval(ecran_1.get(1.0, END))))>0:
        result = (float(str(eval(ecran_1.get(1.0, END))))**0.5)
        ecran_1.delete(1.0, END)
        ecran_1.insert(1.0, result)
        ecran_2.config(text= result)
    else:
        ecran_2.config(text="Opération erronée !")

def negative():
    result = (int(str(eval(ecran_1.get(1.0, END))))*-1)
    ecran_1.delete(1.0, END)
    ecran_1.insert(1.0, result)


#Pavé numériques
touches = ["C", "%", "←", "1/x", "x²", chr(8730), "÷", "7", "8", "9", "*",\
            "4", "5", "6", "-", "1", "2", "3", "+", chr(177), "0", ".", "="]

#ecrans
ecran = Frame(fen, borderwidth=2, width=30, height=4, background=couleurs[0])
ecran.grid(columnspan=4)
ecran_1 = Text(ecran, fg=couleurs[1], background=couleurs[0], width=30, height=2)
ecran_1.grid(row=1, column=1, columnspan=4)
ecran_2 = Label(ecran, background="orange",text=result, font="Bahnschrift 10", fg="green", width=35, height=2)
ecran_2.grid(row=2, column=1, columnspan=4)

# Boutons
ligne = 3
colonne = 1
for i in touches:
    if i == touches[0]:
        boutton = Button(fen, bg=couleurs[2], text=i, borderwidth=2, fg=couleurs[1], \
                    activebackground="gray", bd=0, width=17, height=2, command= lambda :efface())
        boutton.grid(column=0 ,columnspan=2, row=ligne, padx=0, pady=1)
        colonne += 1
    if i in touches[6:-4]:
        boutton = Button(fen, bg=couleurs[0], text=i,borderwidth=2, fg=couleurs[1], \
                    activebackground="gray", width=8, height=2, bd=0, command=lambda e=i:affiche(e))
        boutton.grid(column=colonne, row=ligne, padx=0, pady=1)
        colonne += 1
    if i == touches[1]:
        boutton = Button(fen, bg=couleurs[0], text=i,borderwidth=2, fg=couleurs[1], \
                    activebackground="gray", width=8, height=2, bd=0, command=lambda :calcule_pourcent())
        boutton.grid(column=colonne, row=ligne, padx=0, pady=1)
        colonne += 1
    if i in touches[-3:-1]:
        boutton = Button(fen, bg=couleurs[0], text=i,borderwidth=2, fg=couleurs[1], \
                    activebackground="gray", width=8, height=2, bd=0, command=lambda e=i:affiche(e))
        boutton.grid(column=colonne, row=ligne, padx=0, pady=1)
        colonne += 1
    if i == touches[-4]:
        boutton = Button(fen, bg=couleurs[0], text=i,borderwidth=2, fg=couleurs[1], \
                    activebackground="gray", width=8, height=2, bd=0, command=lambda :negative())
        boutton.grid(column=colonne, row=ligne, padx=0, pady=1)
        colonne += 1
    if i == touches[2]:
        boutton = Button(fen, bg=couleurs[0], text=i,borderwidth=2, fg=couleurs[1], \
                    activebackground="gray", width=8, height=2, bd=0, command=lambda :calcule_retirer())
        boutton.grid(column=colonne, row=ligne, padx=0, pady=1)
        colonne += 1
    if i == touches[3]:
        boutton = Button(fen, bg=couleurs[0], text=i,borderwidth=2, fg=couleurs[1], \
                    activebackground="gray", width=8, height=2, bd=0, command=lambda :calcule_inverse())
        boutton.grid(column=colonne, row=ligne, padx=0, pady=1)
        colonne += 1
    if i == touches[4]:
        boutton = Button(fen, bg=couleurs[0], text=i,borderwidth=2, fg=couleurs[1], \
                    activebackground="gray", width=8, height=2, bd=0, command=lambda :calcule_carré())
        boutton.grid(column=colonne, row=ligne, padx=0, pady=1)
        colonne += 1
    if i == touches[5]:
        boutton = Button(fen, bg=couleurs[0], text=i,borderwidth=2, fg=couleurs[1], \
                    activebackground="gray", width=8, height=2, bd=0, command=lambda :calcule_racine_carré())
        boutton.grid(column=colonne, row=ligne, padx=0, pady=1)
        colonne += 1
    if i == touches[-1]:
        boutton = Button(fen, bg=couleurs[3], text=i,borderwidth=2, fg=couleurs[1], \
                    activebackground="gray", width=8, height=2, bd=0, command=lambda :calcule_simple())
        boutton.grid(column=colonne, row=ligne, padx=0, pady=1)
    if colonne == 4:
        colonne = 0
        ligne +=1

fen.mainloop()