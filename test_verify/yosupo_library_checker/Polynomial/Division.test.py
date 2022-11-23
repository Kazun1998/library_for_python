# verification-helper: PROBLEM https://judge.yosupo.jp/problem/division_of_polynomials

#==================================================
from Modulo_Sequence.Modulo_Polynomial import *

import sys
input=sys.stdin.readline
write=sys.stdout.write

#==================================================
def verify():
    N,M=map(int,input().split())
    F=list(map(int,input().split()))
    G=list(map(int,input().split()))

    F=Modulo_Polynomial(F,N)
    G=Modulo_Polynomial(G,M)

    Q,R=divmod(F,G)

    Q.reduce(); R.reduce()
    Q=Q.Poly if Q.Poly!=[0] else []
    R=R.Poly if R.Poly!=[0] else []

    print(len(Q), len(R))
    write(" ".join(map(str,Q))); print()
    write(" ".join(map(str,R)))

#==================================================
verify()
