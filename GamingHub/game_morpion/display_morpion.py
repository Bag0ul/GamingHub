

from tkinter import *

root = Tk()
root.title("Working state")

frame = Frame(root)
frame.grid()
# Entry_theme
Entry_theme = Entry(root, width=50, text="inserer le theme souhaite(1,2,3)")
Entry_theme.insert(0, "inserer le theme souhaite(1,2,3)")
Entry_theme.grid(row=0, column=4, sticky=W, padx=10)
Label(root, text="Theme:").grid(row=0, column=0, sticky=W, padx=10)

# Entry_size
Entry_size = Entry(root, width=50, text="inserer la taille de la grille")
Entry_size.insert(0, 'inserer la thaille de la grille')
Entry_size.grid(row=1, column=4, sticky=W, padx=10)
Label(root, text="Theme:").grid(row=0, column=0, sticky=W, padx=10)

ai_choice=IntVar()
Entry_ai = Checkbutton(root, text="IA", variable=ai_choice, offvalue=False, onvalue=True)
Entry_ai.grid(row=2, column=0, sticky=W, padx=10)

Com = StringVar()
Com.set("ATTENTION REGARDEZ ICI EN JOUANT")
Commentaire = Entry(root, text="ATTENTION REGARDEZ ICI EN JOUANT", textvariable=Com, width=50)
Commentaire.grid(row=2, column=4, sticky=W, padx=10)
Label(root, text="Taille:").grid(row=1, column=0, sticky=W, padx=10)

# --Cette partie dessine les boutons de jeu--

def modif_commentaire(text):
    global Commentaire
    Commentaire.delete(0, "end")
    Commentaire.insert(0, text)


command = StringVar()


def display_button(dict):
    global Button_1, command
    for key, value in dict.items():
        Text1 = StringVar()
        Button_1 = Radiobutton(root, indicatoron=0, textvariable=Text1, variable=command, value=value[1])
        Button_1.grid(row=value[0][0], column=value[0][1], padx=2, sticky=E)
        Text1.set(key)


def waiting():
    global command
    Button_1.wait_variable(command)

def display_grid(A, root):
    nb_lignes = len(A)
    nb_colonnes = len(A[0])
    L = []
    H = []
    for i in range(0, nb_lignes):
        for j in range(0, nb_colonnes):
            # adresse_image=Dict[A[i][j]]
            # photo=PhotoImage(file=adresse_image)
            contenu = StringVar()
            contenu.set(A[i][j])
            L.append(contenu)
            label = Label(root, width=10, height=5, borderwidth=3, relief='groove',
                          textvariable=contenu)  # image=photo)
            label.grid(row=i + 6, column=j + 6)
            H.append(label)
    return (H, L)
    
def set_ai_choice():
    return ai_choice.get()
def remplir(coord,signe,grille):#signe correspond a x ou o pour remplir l'élement:
    x,y=int(coord.get()[0]),int(coord.get()[1])
    if grille[x][y]==" ":
        grille[x][y]=signe
        u=0
        return("Vous avez fini votre tour",u)
    u=1
    return("Veuillez choisir une case valide",u)

def fin_de_tour(u):
    if u==0:
        return("Fin de tour, le joueur suivant doit jouer")
    else:
        return("Choissisez à présent une valeur correcte")

def victoire(grille):
    if grille[0][0]==grille[0][1]==grille[0][2]!=" " or grille[1][0]==grille[1][1]==grille[1][2]!=" " or grille[2][0]==grille[2][1]==grille[2][2]!=" " or grille[0][0]==grille[1][0]==grille[2][0]!=" " or grille[0][1]==grille[1][1]==grille[2][1]!=" " or grille[0][2]==grille[1][2]==grille[2][2]!=" " or grille[0][0]==grille[1][1]==grille[2][2]!=" " or grille[0][2]==grille[1][1]==grille[2][0]!=" ":
        return("Victoire")
    cond=True
    for i in range(3):
        for j in range(3):
            if grille[i][j]!=" ":
                cond= False
    if cond==True:
        return("Egalité")
    else:
        return("Le jeu est encore en cours")
def altern(signe):
    if signe=='X':
        return('O')
    else:
        return('X')

def waiting():
    global command
    Button_1.wait_variable(command)

def set_coord():
    global command
    waiting()
    return(command)

