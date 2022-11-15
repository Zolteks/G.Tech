# on admet la fonction input() qui renvoie la valeur donné par l'utilisateur.

# definir une fonction morpion() qui lance une partie de morpion entre deux joueurs.
def morpion():
    # definir un tableau de 3 x 3 avec des symboles vide.
    tab = [ ["_" for i in range(3)] for i in range(3) ]
    # definir un dictionaire dans lequel on stock le nom des joueurs
    curPlayer = {
        1: "Joueur 1",
        -1: "Joueur 2"
    }
    # definir une variable à laquelle on assigne l'ID du joueur actuel
    curPlayerID = 1
    # definir un dictionaire dans lequel on stock le symbole de chaque joueur en fonction de son ID
    playerSymbole = {
        1: "O",
        -1: "X"
    }

    # tant que True
    while True:
        # ecrire le nom du joueur dont c'est le tour en fonction de l'ID du joueur actuel dans curPlayer 
        print(f"{curPlayer[curPlayerID]}, c'est à toi !")

        # on assigne à la variable choixX le retour de la variable input("coordonné x : ") sous forme d'entier
        choixX = int(input("coordonné x : "))
        # on assigne à la variable choixX le retour de la variable input("coordonné y : ") sous forme d'entier
        choixY = int(input("coordonné y : "))

        # si tab[choixX][choixY] est different de "_".
        if tab[choixX][choixY] != "_":
            # alors on ecrit "case occupée, fais un autre choix".
            print("case occupée, fais un autre choix")
        
        # sinon
        else:
            # assigner le symbole du joueur aux coordonnées choixX, choixY dans tab.
            tab[choixX][choixY] = playerSymbole[curPlayerID]

        # pour chaque element de tab
        for i in tab:
            # on imrpime la ligne du tableau
            print(i)

        # on stock temporairement le symbole du joueur actuel dans la variable cur.
        cur = playerSymbole[curPlayerID]
        # si l'action du joueur est un action qui lui fait gagner la partie.
        if (tab[0][0] == cur and tab[0][1] == cur and tab[0][2] == cur) or (tab[1][0] == cur and tab[1][1] == cur and tab[1][2] == cur) or (tab[2][0] == cur and tab[2][1] == cur and tab[2][2] == cur) or (tab[0][0] == cur and tab[1][0] == cur and tab[2][0] == cur) or (tab[0][1] == cur and tab[1][1] == cur and tab[2][1] == cur) or (tab[0][2] == cur and tab[1][2] == cur and tab[2][2] == cur) or (tab[0][0] == cur and tab[1][1] == cur and tab[2][2] == cur) or (tab[0][2] == cur and tab[1][1] == cur and tab[2][0] == cur):
            # alors on ecrit quel joueur à gagné
            print(f"{curPlayer[curPlayerID]} a gagné")
            # puis on force la sortie de la boucle infinie avec un break
            break
        
        # si tab[choixX][choixY] est égal au symbole du joueur.
        if tab[choixX][choixY] == playerSymbole[curPlayerID]:
            # alors on change l'ID de curPlayerID en multipliant la variable par -1.
            curPlayerID = curPlayerID * -1

morpion()