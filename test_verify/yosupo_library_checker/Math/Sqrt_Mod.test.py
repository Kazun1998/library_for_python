# verification-helper: PROBLEM https://judge.yosupo.jp/problem/sqrt_mod

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
        Y,P=map(int,input().split())
        X=Sqrt(Modulo(Y,P))

        if X is not None:
            Ans[t]=X.a

    write("\n".join(map(str,Ans)))

#==================================================
verify()
