# verification-helper: PROBLEM https://judge.yosupo.jp/problem/product_of_polynomial_sequence

#==================================================
from Modulo_Sequence.Modulo_Polynomial import *

import sys
input=sys.stdin.readline
write=sys.stdout.write

#==================================================
def verify():
    N=int(input())
    A=[None]*N

    global Mod; Mod=998244353
    global Calc; Calc=Calculator()

    D=0
    for i in range(N):
        d,*A[i]=map(int,input().split())
        D+=d

    write(" ".join(map(str, Calc.multiple_convolution(*A))))

#==================================================
verify()
