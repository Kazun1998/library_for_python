# verification-helper: PROBLEM https://judge.yosupo.jp/problem/adjugate_matrix

#==================================================
from Modulo_Matrix.Modulo_Matrix import Modulo_Matrix, Adjugate_Matrix

import sys
input=sys.stdin.readline
write=sys.stdout.write

#==================================================
def verify():
    N = int(input())
    A = [None] * N
    for i in range(N):
        A[i] = list(map(int, input().split()))

    A = Modulo_Matrix(A)
    B = Adjugate_Matrix(A)

    for i in range(N):
        print(*B[i])

#==================================================
verify()
