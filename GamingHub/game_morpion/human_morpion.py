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

