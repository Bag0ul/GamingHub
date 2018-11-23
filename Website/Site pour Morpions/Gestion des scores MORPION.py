

dict={"zamel":78}#supposons que l'on dispose d'un dictionnaire
pseudo="zamel"
###On Suppose que pseudo à gagner à ce stade et son score augmente alors de 1
if pseudo in dict:
    lines = []
    with open('scores_Morpions.txt', 'r') as score_Morpion:
        tot=score_Morpion.readlines()
        for i in range(len(tot)):
            if pseudo not in tot[i]:
                lines.append(tot[i])
        with open('scores_Morpions.txt', 'w')as score_Morpion :
            score_Morpion.write("\r".join(lines))
    dict[pseudo]+=1
else:
        dict[pseudo]=1
with open('scores_Morpions.txt', 'a') as score_Morpion:
    score_Morpion.write('\n{}   {}'.format(pseudo,dict[pseudo]))
    

######Gestion des scores sur Morpion
    