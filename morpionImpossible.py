import copy

# lance une partie de morpion ou l'IA gagne tout le temps ou fait une égalité.
def impossibleMorpion():

    # initialise le tableau de jeu au format 3 x 3.
    tab = [ ["_" for i in range(3)] for i in range(3) ]
    
    # definir le dictionaire qui contient les noms des joueurs en fonction de leur ID.
    curPlayer = {
        1: "Joueur",
        -1: "Cortana"
    }

    # initialise l'ID du joueur actuel à 1.
    curPlayerID = 1

    # définir le dictionaire qui contient le symbole d'un joueur en fonction de son ID.
    playerSymbole = {
        1: "O",
        -1: "X"
    }

    # modifie le tableau d'après la première action de l'IA
    tab[1][1] = "X"

    # initialise la variable du nombre d'action de la partie à 1.
    action = 1

    # tant que True
    while True:
        # pour i dans tab
        for i in tab:
            # écrire i
            print(i)

        # incrémenter action de 1
        action += 1

        # si curPlayerID égal
        if curPlayerID == 1:
            # définir une variable booléenne à False
            choix = False
            # tant que choix n'est pas égal à True.
            while not choix:
                # écrire "c'est à toi de jouer"
                print("C'est à toi de jouer !")
                # définir choixX avec le retour de la fonction input("Ligne (1 à 3): ")
                choixX = int(input("Ligne (1 à 3): ")) - 1
                # définir choixX avec le retour de la fonction input("Colonne (1 à 3): ")
                choixY = int(input("Colonne (1 à 3): ")) - 1
                # si tab[choixX][choixY] est égal à "_".
                if tab[choixX][choixY] != "_":
                    # alors, écrire "case occupée, fais un autre choix"
                    print("case occupée, fais un autre choix")
                # sinon
                else:
                    # assigner à tab[choixX][choixY] la valeur de playerSymbole[curPlayerID]
                    tab[choixX][choixY] = playerSymbole[curPlayerID]
                    # assigner à choix la valeur True
                    choix = True
        # sinon
        else:
            # écrire "Au tour de Cortana"
            print("Au tour de Cortana")

        # écrire un ligne vide afin de créer un espace.
        print("")
        # si action est égal à 3 et curPlayerID est égal à -1.
        if action == 3 and curPlayerID == -1:
            # alors, si tab[0][0] est égal à "_"
            if tab[0][0] == "_":
                # alors modifier tab[0][0] par "X"
                tab[0][0] = "X"
            # sinon
            else:
                # modifier tab[0][2] par "X"
                tab[0][2] = "X"
        
        # si action est égal à 5 et curPlayerID est égal à -1
        if action == 5 and curPlayerID == -1:
            # définir check avec la valeur False
            check = False
            # pour x allant de 0 à 2.
            for x in range(3):
                # si check n'est pas égal à True
                if not check:
                    # pour y allant de 0 à 2.
                    for y in range(3):
                        # si tab[x][y] est égal à "_".
                        if tab[x][y] == "_":
                            # alors définir tempTab avec une copie de tab
                            tempTab = copy.deepcopy(tab)
                            # modifier tempTab[x][y] par "O"
                            tempTab[x][y] = "O"
                            # si une des condition de victoire du joueur est vraie dans tempTab.
                            if (tempTab[0][0] == "O" and tempTab[0][1] == "O" and tempTab[0][2] == "O") or (tempTab[1][0] == "O" and tempTab[1][1] == "O" and tempTab[1][2] == "O") or (tempTab[2][0] == "O" and tempTab[2][1] == "O" and tempTab[2][2] == "O") or (tempTab[0][0] == "O" and tempTab[1][0] == "O" and tempTab[2][0] == "O") or (tempTab[0][1] == "O" and tempTab[1][1] == "O" and tempTab[2][1] == "O") or (tempTab[0][2] == "O" and tempTab[1][2] == "O" and tempTab[2][2] == "O") or (tempTab[0][0] == "O" and tempTab[1][1] == "O" and tempTab[2][2] == "O") or (tempTab[0][2] == "O" and tempTab[1][1] == "O" and tempTab[2][0] == "O"):
                                # modifier tab[x][y] par "X"
                                tab[x][y] = "X"
                                # modifier check par True
                                check = True
                                # casser la boucle actuelle
                                break
            # si check n'est pas True et tab[2][2] égal "_".
            if not check and tab[2][2] == "_":
                # modifier tab[2][2] par "X"
                tab[2][2] = "X"
            # sinon si check n'est pas True
            elif not check:
                # modifier tab[2][0] par "X"
                tab[2][0] = "X"
        
        # si action égal 7
        if action == 7:
            # définir check par False
            check = False
            # pour x allant de 0 à 2
            for x in range(3):
                # si check n'est pas True
                if not check:
                    # pour y allant de 0 à 2
                    for y in range(3):
                        # si  tab[x][y] égal "_"
                        if tab[x][y] == "_":
                            # définir tempTab avec une copie de tab
                            tempTab = copy.deepcopy(tab)
                            # modifier tempTab[x][y] par "X"
                            tempTab[x][y] = "X"
                            # si une des conditions de victoire de l'IA est vraie dans tempTab
                            if (tempTab[0][0] == "X" and tempTab[0][1] == "X" and tempTab[0][2] == "X") or (tempTab[1][0] == "X" and tempTab[1][1] == "X" and tempTab[1][2] == "X") or (tempTab[2][0] == "X" and tempTab[2][1] == "X" and tempTab[2][2] == "X") or (tempTab[0][0] == "X" and tempTab[1][0] == "X" and tempTab[2][0] == "X") or (tempTab[0][1] == "X" and tempTab[1][1] == "X" and tempTab[2][1] == "X") or (tempTab[0][2] == "X" and tempTab[1][2] == "X" and tempTab[2][2] == "X") or (tempTab[0][0] == "X" and tempTab[1][1] == "X" and tempTab[2][2] == "X") or (tempTab[0][2] == "X" and tempTab[1][1] == "X" and tempTab[2][0] == "X"):
                                # modifier tab[x][y] par "X"
                                tab[x][y] = "X"
                                # modifier check par True
                                check = True
                                # casser la boucle actuelle
                                break
            # si check n'est pas True
            if not check:
                # modifier check par False
                check = False
                # pour x allant de 0 à 2
                for x in range(3):
                    # si check n'est pas vrai
                    if not check:
                        # pour y allant de 0 à 2
                        for y in range(3):
                            # si tab[x][y] égal "_"
                            if tab[x][y] == "_":
                                # modifier tab[x][y] par "X"
                                tab[x][y] = "X"
                                # modifier check par True
                                check = True
                                # casser la boucle actuelle
                                break
        
        # si action égal 9
        if action == 9:
            # modifier check par False
            check = False
            # pour x allant de 0 à 2
            for x in range(3):
                # si check n'est pas vrai
                if not check:
                    # pour y allant de 0 à 2
                    for y in range(3):
                        # si tab[x][y] égal "_"
                        if tab[x][y] == "_":
                            # modifier tab[x][y] par "X"
                            tab[x][y] = "X"
                            # modifier check par True
                            check = True
                            # casser la boucle actuelle
                            break
        
        # définir cur avec playerSymbole[curPlayerID], le symbole du joueur actuel
        cur = playerSymbole[curPlayerID]
        # si une des conditions de victoire du joueur actuel est vraie dans tab
        if (tab[0][0] == cur and tab[0][1] == cur and tab[0][2] == cur) or (tab[1][0] == cur and tab[1][1] == cur and tab[1][2] == cur) or (tab[2][0] == cur and tab[2][1] == cur and tab[2][2] == cur) or (tab[0][0] == cur and tab[1][0] == cur and tab[2][0] == cur) or (tab[0][1] == cur and tab[1][1] == cur and tab[2][1] == cur) or (tab[0][2] == cur and tab[1][2] == cur and tab[2][2] == cur) or (tab[0][0] == cur and tab[1][1] == cur and tab[2][2] == cur) or (tab[0][2] == cur and tab[1][1] == cur and tab[2][0] == cur):
            # pour i dans tab
            for i in tab:
                # écrire i
                print(i)
            # écrire quel joueur a gagné
            print(f"{curPlayer[curPlayerID]} a gagné")
            # casser la boucle principale
            break
        # sinon si action égal 9
        elif action == 9:
            # alors écrire "égalité..."
            print("égalité...")
            # casser la boucle principale
            break
        
        # multiplier la valeur de curPlayerID par -1
        curPlayerID = curPlayerID * -1

# exécuter la fonction impossibleMorpion()
impossibleMorpion()