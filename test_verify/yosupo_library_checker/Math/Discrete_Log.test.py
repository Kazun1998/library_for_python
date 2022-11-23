# verification-helper: PROBLEM https://judge.yosupo.jp/problem/discrete_logarithm_mod

#==================================================
from Modulo import *

import sys
input=sys.stdin.readline
write=sys.stdout.write

#==================================================
def verify():
    T=int(input())
    Ans=[-1]*T

    for t in range(T):
        X,Y,M=map(int,input().split())
        X=Modulo(X,M)
        K=Discrete_Log(X,Y)

        if K is not None:
            Ans[t]=K

    write("\n".join(map(str,Ans)))

#==================================================
verify()
