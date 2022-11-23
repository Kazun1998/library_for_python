# verification-helper: PROBLEM https://judge.yosupo.jp/problem/two_sat

#==================================================
from Two_SAT import *

import sys
input=sys.stdin.readline
write=sys.stdout.write

#==================================================
def verify():
    p,cnf,N,M=input().split()
    N=int(N); M=int(M)

    T=Two_SAT(N)
    for _ in range(M):
        a,b,zero=map(int,input().split())

        if a>0:
            a=a-1
        else:
            a=~(-a-1)

        if b>0:
            b=b-1
        else:
            b=~(-b-1)

        T.add_or(a,b)

    X=T.is_satisfy(1)
    if X:
        print("s","SATISFIABLE")
        V=[]
        for i in range(N):
            if X[i]:
                V.append(i+1)
            else:
                V.append(-(i+1))
        V.append(0)
        print("v",*V)
    else:
        print("s","UNSATISFIABLE")

#==================================================
verify()