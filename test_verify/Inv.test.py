# verification-helper: PROBLEM https://judge.yosupo.jp/problem/inv_of_formal_power_series

#==================================================
from Modulo_Sequence.Modulo_Polynominal import *

import sys
input=sys.stdin.readline
write=sys.stdout.write

#==================================================
def verify():
    N=int(input())
    A=list(map(int,input().split()))
    write(" ".join(map(str,Calc.Inverse(A))))

#==================================================
verify()