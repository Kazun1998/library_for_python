# verification-helper: PROBLEM https://judge.yosupo.jp/problem/exp_of_formal_power_series

#==================================================
from Modulo_Sequence.Modulo_Polynomial import *

import sys
input=sys.stdin.readline
write=sys.stdout.write

#==================================================
def verify():
    N=int(input())
    A=list(map(int,input().split()))
    P=Modulo_Polynomial(A,N)
    write(" ".join(map(str,Exp(P))))

#==================================================
verify()