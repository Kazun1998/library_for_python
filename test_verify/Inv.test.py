# verification-helper: PROBLEM https://judge.yosupo.jp/problem/convolution_mod

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