# verification-helper: PROBLEM https://judge.yosupo.jp/problem/pow_of_formal_power_series

#==================================================
from Modulo_Sequence.Modulo_Polynomial import *

import sys
input=sys.stdin.readline
write=sys.stdout.write

#==================================================
def verify():
    N,M=map(int,input().split())
    A=list(map(int,input().split()))
    P=Modulo_Polynomial(A,N)
    B=Power(P,M).Poly
    B.extend([0]*(N-len(B)))
    write(" ".join(map(str,B)))

#==================================================
verify()