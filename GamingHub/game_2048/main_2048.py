import grid_2048
import move_2048
import ai_2048
import display_2048

def play():
    ai = display_2048.set_ai_choice()
    dic_button={'Up':((4,1),'h'),'Down':((5,1),'b'),'Right':((5,2),'d'),'Left':((5,0),'g')}
    display_2048.display_button(dic_button)
    dic_move = {0: "g", 1: "d", 2: "h", 3: "b"}
    size = display_2048.set_size_grid()
    grid = grid_2048.init_game(size)
    dic_values = {"round":1}
    display_2048.display_grid(grid, display_2048.root)
    while not move_2048.is_game_over(grid) and grid_2048.get_grid_tile_max(grid) < 2048:
        moves = move_2048.move_possible(grid)
        dic_values["moves"] = [dic_move[i] for i in range(4) if moves[i]]
        if ai:
            command = ai_2048.set_direction(grid, dic_values)
        else:
            command = display_2048.set_direction()
        while not command in dic_values["moves"]:
            if ai:
                command = ai_2048.set_direction(grid, dic_values)
            else:
                command = display_2048.set_direction()
        grid = move_2048.move_grid(grid, command)
        if not grid_2048.is_full_grid(grid):
            grid = grid_2048.grid_add_new_tile(grid)
        print("Tour {}, deplacement {} :".format(dic_values["round"], command))
        display_2048.display_grid(grid, display_2048.root)
        print(grid_2048.grid_to_string(grid))
        dic_values["round"] += 1
    if grid_2048.get_grid_tile_max(grid) >= 2048:
        return "Victoire !"
    return "Game Over"

Start_game=display_2048.Button(display_2048.root, text="Commencer le jeu",command=play)
Start_game.grid(row= 3,column=0,sticky=display_2048.W)

display_2048.root.mainloop()
