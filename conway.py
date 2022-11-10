from random import randint
import os

def willLive(tab, x, y):
    for i in range():
        


def gameOfLife(size):
    univers = [ [0 for i in range(size)] for i in range(size) ]
    life = 0
    for i in range(size):
        for j in range(size):
            if randint(1,4) == 1:
                univers[i][j] = 1
    while life < 1000:
        life += 1



        os.system('cls')
        for i in univers:
            print(i)
        print("")


gameOfLife(10)