# verification-helper: PROBLEM https://judge.yosupo.jp/problem/polynomial_taylor_shift

#==================================================
from Modulo_Sequence.Modulo_Polynomial import *

import sys
input=sys.stdin.readline
write=sys.stdout.write

#==================================================
def verify():
    N,c=map(int,input().split())
    A=list(map(int,input().split()))
    A=Modulo_Polynomial(A,N)

    write(" ".join(map(str,Taylor_Shift(A,c).Poly)))

#==================================================
verify()