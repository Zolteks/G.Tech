import copy

def impossibleMorpion():

    tab = [ ["_" for i in range(3)] for i in range(3) ]
    curPlayer = {
        1: "Joueur",
        -1: "IA"
    }
    curPlayerID = 1
    playerSymbole = {
        1: "O",
        -1: "X"
    }

    tab[1][1] = "X"
    action = 0


    while True:

        for i in tab:
            print(i)

        action += 1

        if curPlayerID == 1:
            choix = False
            while not choix:
                print("C'est à toi de jouer !")
                choixX = int(input("coordonné x : "))
                choixY = int(input("coordonné y : "))
                if tab[choixX][choixY] != "_":
                    print("case occupée, fais un autre choix")
                else:
                    tab[choixX][choixY] = playerSymbole[curPlayerID]
                    choix = True
        else:
            print("Au tour de l'IA")

        if action == 2:
            if tab[0][0] == "_":
                tab[0][0] = "X"
            else:
                tab[0][2] = "X"
        
        if action == 4:
            for x in range(3):
                for y in range(3):
                    if tab[x][y] == "_":
                        tempTab = copy.deepcopy(tab)
                        tempTab[x][y] = "O"
                        if (tempTab[0][0] == "O" and tempTab[0][1] == "O" and tempTab[0][2] == "O") or (tempTab[1][0] == "O" and tempTab[1][1] == "O" and tempTab[1][2] == "O") or (tempTab[2][0] == "O" and tempTab[2][1] == "O" and tempTab[2][2] == "O") or (tempTab[0][0] == "O" and tempTab[1][0] == "O" and tempTab[2][0] == "O") or (tempTab[0][1] == "O" and tempTab[1][1] == "O" and tempTab[2][1] == "O") or (tempTab[0][2] == "O" and tempTab[1][2] == "O" and tempTab[2][2] == "O") or (tempTab[0][0] == "O" and tempTab[1][1] == "O" and tempTab[2][2] == "O") or (tempTab[0][2] == "O" and tempTab[1][1] == "O" and tempTab[2][0] == "O"):
                            tab[x][y] = "X"
                            break
        else:
            if tab[2][2] == "_":
                tab[2][2] = "X"
            else:
                tab[2][0] = "X"
        
        if action == 6:
            for x in range(3):
                for y in range(3):
                    if tab[x][y] == "_":
                        tempTab = tab
                        tempTab[x][y] = "X"
                        if (tempTab[0][0] == "X" and tempTab[0][1] == "X" and tempTab[0][2] == "X") or (tempTab[1][0] == "X" and tempTab[1][1] == "X" and tempTab[1][2] == "X") or (tempTab[2][0] == "X" and tempTab[2][1] == "X" and tempTab[2][2] == "X") or (tempTab[0][0] == "X" and tempTab[1][0] == "X" and tempTab[2][0] == "X") or (tempTab[0][1] == "X" and tempTab[1][1] == "X" and tempTab[2][1] == "X") or (tempTab[0][2] == "X" and tempTab[1][2] == "X" and tempTab[2][2] == "X") or (tempTab[0][0] == "X" and tempTab[1][1] == "X" and tempTab[2][2] == "X") or (tempTab[0][2] == "X" and tempTab[1][1] == "X" and tempTab[2][0] == "X"):
                            tab[x][y] = "X"
                            break

        cur = playerSymbole[curPlayerID]
        if (tab[0][0] == cur and tab[0][1] == cur and tab[0][2] == cur) or (tab[1][0] == cur and tab[1][1] == cur and tab[1][2] == cur) or (tab[2][0] == cur and tab[2][1] == cur and tab[2][2] == cur) or (tab[0][0] == cur and tab[1][0] == cur and tab[2][0] == cur) or (tab[0][1] == cur and tab[1][1] == cur and tab[2][1] == cur) or (tab[0][2] == cur and tab[1][2] == cur and tab[2][2] == cur) or (tab[0][0] == cur and tab[1][1] == cur and tab[2][2] == cur) or (tab[0][2] == cur and tab[1][1] == cur and tab[2][0] == cur):
            for i in tab:
                print(i)
            print(f"{curPlayer[curPlayerID]} a gagné")
            break
        
        # if tab[choixX][choixY] == playerSymbole[curPlayerID]:
        #     print("lol")
        curPlayerID = curPlayerID * -1

impossibleMorpion()