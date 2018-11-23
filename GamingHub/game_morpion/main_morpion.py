# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 14:10:25 2018
"""


import display_morpion

def play():
    global grid
    ai = display_morpion.set_ai_choice()
    dic_button={'button_1':((5,0),'00'),'Button_2':((5,1),'01'),'button_3':((5,2),'02'),'button_4':((6,0),'10'),'button_5':((6,1),'11')
              ,'button_6':((6,2),'12'),'button_7':((7,0),'20'),'button_8':((7,1),'21'),'button_9':((7,2),'22')}

    display_morpion.display_button(dic_button)
    grid=[[' ',' ',' '] for i in range(3)]
    signe='X'
    print(display_morpion.victoire(grid))
    while True:
        signe=display_morpion.altern(signe)
        coord=display_morpion.set_coord()
        print(coord)
        k=display_morpion.remplir(coord,signe,grid)
        while k[1]==1:
            print("Veuillez rejouer")
        print(k[0])
        display_morpion.modif_commentaire(k[0])
        print(grid)
        display_morpion.display_grid(grid,display_morpion.root)
        a=display_morpion.victoire(grid)
        print(display_morpion.victoire(grid))
        if display_morpion.victoire(grid)!= "Le jeu est encore en cours":
            break
    if display_morpion.victoire(grid)=="Victoire":
        display_morpion.modif_commentaire(signe+" a gagné")

        
Start_game=display_morpion.Button(display_morpion.root, text="Commencer le jeu",command=play)
Start_game.grid(row= 3,column=0,sticky=display_morpion.W)

display_morpion.root.mainloop()
            
