
def morpion():
    tab = [ ["_" for i in range(3)] for i in range(3) ]
    game = True
    curPlayer = {
        1: "Joueur 1",
        -1: "Joueur 2"
    }
    curPlayerID = 1
    playerSymbole = {
        1: "O",
        -1: "X"
    }

    while game:
        if curPlayerID == 1:
            print(f"{curPlayer[curPlayerID]}, c'est à toi !")

        choixX = int(input("coordonné x : "))
        choixY = int(input("coordonné y : "))

        if tab[choixX][choixY] != "_":
            print("case occupée, fais un autre choix")
            pass
        
        else:
            tab[choixX][choixY] = playerSymbole[curPlayerID]

        for i in tab:
            print(i)

        cur = playerSymbole[curPlayerID]
        if (tab[0][0] == cur and tab[0][1] == cur and tab[0][2] == cur) or (tab[1][0] == cur and tab[1][1] == cur and tab[1][2] == cur) or (tab[2][0] == cur and tab[2][1] == cur and tab[2][2] == cur) or (tab[0][0] == cur and tab[1][0] == cur and tab[2][0] == cur) or (tab[0][1] == cur and tab[1][1] == cur and tab[2][1] == cur) or (tab[0][2] == cur and tab[1][2] == cur and tab[2][2] == cur) or (tab[0][0] == cur and tab[1][1] == cur and tab[2][2] == cur) or (tab[0][2] == cur and tab[1][1] == cur and tab[2][0] == cur):
            print(f"{curPlayer[curPlayerID]} a gagné")
            break
            
        curPlayerID = curPlayerID * -1

morpion()