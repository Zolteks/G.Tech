import sys
sys.setrecursionlimit(2000)

def fiboRecursif(n, suite=[0,1]):
    l = len(suite)
    suite.append(suite[-1] + suite[-2])
    if l == n:
        return suite[l-1]
    return fibo(n, suite)

def fibo(n):
    suite = [0, 1]
    while len(suite) - 1 != n:
        suite.append(suite[-1] + suite[-2])
    return suite[-1]

print(fibo(1000))
