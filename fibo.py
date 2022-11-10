import sys
sys.setrecursionlimit(2000)

def fibo(n, suite=[0,1]):
    l = len(suite)
    suite.append(suite[l-1] + suite[l-2])
    if l == n:
        return suite[l-1]
    return fibo(n, suite)

print(fibo(1000))