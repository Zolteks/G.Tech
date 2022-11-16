import copy

def impossibleMorpion():

    tab = [ ["_" for i in range(3)] for i in range(3) ]
    curPlayer = {
        1: "Joueur",
        -1: "Cortana"
    }
    curPlayerID = 1
    playerSymbole = {
        1: "O",
        -1: "X"
    }

    tab[1][1] = "X"
    action = 1


    while True:

        for i in tab:
            print(i)

        action += 1

        if curPlayerID == 1:
            choix = False
            while not choix:
                print("C'est à toi de jouer !")
                choixX = int(input("Ligne : "))
                choixY = int(input("Colonne : "))
                if tab[choixX][choixY] != "_":
                    print("case occupée, fais un autre choix")
                else:
                    tab[choixX][choixY] = playerSymbole[curPlayerID]
                    choix = True
        else:
            print("Au tour de Cortana")

        print("")
        if action == 3 and curPlayerID == -1:
            if tab[0][0] == "_":
                tab[0][0] = "X"
            else:
                tab[0][2] = "X"
        
        if action == 5 and curPlayerID == -1:
            check = False
            for x in range(3):
                if not check:
                    for y in range(3):
                        if tab[x][y] == "_":
                            tempTab = copy.deepcopy(tab)
                            tempTab[x][y] = "O"
                            if (tempTab[0][0] == "O" and tempTab[0][1] == "O" and tempTab[0][2] == "O") or (tempTab[1][0] == "O" and tempTab[1][1] == "O" and tempTab[1][2] == "O") or (tempTab[2][0] == "O" and tempTab[2][1] == "O" and tempTab[2][2] == "O") or (tempTab[0][0] == "O" and tempTab[1][0] == "O" and tempTab[2][0] == "O") or (tempTab[0][1] == "O" and tempTab[1][1] == "O" and tempTab[2][1] == "O") or (tempTab[0][2] == "O" and tempTab[1][2] == "O" and tempTab[2][2] == "O") or (tempTab[0][0] == "O" and tempTab[1][1] == "O" and tempTab[2][2] == "O") or (tempTab[0][2] == "O" and tempTab[1][1] == "O" and tempTab[2][0] == "O"):
                                tab[x][y] = "X"
                                check = True
                                break
            if not check and tab[2][2] == "_":
                tab[2][2] = "X"
            elif not check:
                tab[2][0] = "X"
        
        if action == 7:
            check = False
            for x in range(3):
                if not check:
                    for y in range(3):
                        if tab[x][y] == "_":
                            tempTab = copy.deepcopy(tab)
                            tempTab[x][y] = "X"
                            if (tempTab[0][0] == "X" and tempTab[0][1] == "X" and tempTab[0][2] == "X") or (tempTab[1][0] == "X" and tempTab[1][1] == "X" and tempTab[1][2] == "X") or (tempTab[2][0] == "X" and tempTab[2][1] == "X" and tempTab[2][2] == "X") or (tempTab[0][0] == "X" and tempTab[1][0] == "X" and tempTab[2][0] == "X") or (tempTab[0][1] == "X" and tempTab[1][1] == "X" and tempTab[2][1] == "X") or (tempTab[0][2] == "X" and tempTab[1][2] == "X" and tempTab[2][2] == "X") or (tempTab[0][0] == "X" and tempTab[1][1] == "X" and tempTab[2][2] == "X") or (tempTab[0][2] == "X" and tempTab[1][1] == "X" and tempTab[2][0] == "X"):
                                tab[x][y] = "X"
                                check = True
                                break
            if not check:
                check = False
                for x in range(3):
                    if not check:
                        for y in range(3):
                            if tab[x][y] == "_":
                                tab[x][y] = "X"
                                check = True
                                break
        
        if action == 9:
            check = False
            for x in range(3):
                if not check:
                    for y in range(3):
                        if tab[x][y] == "_":
                            tab[x][y] = "X"
                            check = True
                            break

        cur = playerSymbole[curPlayerID]
        if (tab[0][0] == cur and tab[0][1] == cur and tab[0][2] == cur) or (tab[1][0] == cur and tab[1][1] == cur and tab[1][2] == cur) or (tab[2][0] == cur and tab[2][1] == cur and tab[2][2] == cur) or (tab[0][0] == cur and tab[1][0] == cur and tab[2][0] == cur) or (tab[0][1] == cur and tab[1][1] == cur and tab[2][1] == cur) or (tab[0][2] == cur and tab[1][2] == cur and tab[2][2] == cur) or (tab[0][0] == cur and tab[1][1] == cur and tab[2][2] == cur) or (tab[0][2] == cur and tab[1][1] == cur and tab[2][0] == cur):
            for i in tab:
                print(i)
            print(f"{curPlayer[curPlayerID]} a gagné")
            break
        elif action == 9:
            print("égalité...")
            break
        
        curPlayerID = curPlayerID * -1


impossibleMorpion()