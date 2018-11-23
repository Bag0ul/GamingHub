# ----- Récupérer les entrées
def set_theme_grid():
    global Entry_theme
    theme = ""
    i = 0
    while not theme in ["0", "1", "2"]:
        theme = Entry_theme.get()
        if i > 0:
            modif_commentaire("le théme doit être 0,1 ou 2")
        i += 1
    return int(theme)


def set_size_grid():
    global Entry_size
    size = ""
    i = 0
    while not size.isdigit():

        size = Entry_size.get()
        if i > 0:
            modif_commentaire("Entrer un entier svp")

        i += 1
    return int(size)

def set_direction():
    global command
    waiting()
    print(command.get())
    return (command.get())
