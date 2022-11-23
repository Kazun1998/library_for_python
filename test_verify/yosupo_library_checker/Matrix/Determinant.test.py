# verification-helper: PROBLEM https://judge.yosupo.jp/problem/matrix_det

#==================================================
from Modulo_Matrix.Modulo_Matrix import *

import sys
input=sys.stdin.readline
write=sys.stdout.write

#==================================================
def verify():
    N=int(input())
    A=[None]*N

    for i in range(N):
        A[i]=list(map(int,input().split()))

    A=Modulo_Matrix(A)
    print(Determinant(A))

#==================================================
verify()