# verification-helper: PROBLEM https://judge.yosupo.jp/problem/pow_of_matrix

#==================================================
from Modulo_Matrix.Modulo_Matrix import *

import sys
input=sys.stdin.readline
write=sys.stdout.write

#==================================================
def verify():
    N, K = map(int, input().split())
    A = [None] * N

    for i in range(N):
        A[i] = list(map(int,input().split()))

    A = Modulo_Matrix(A)
    B = A ** K

    for i in range(N):
        print(*B.ele[i])

#==================================================
verify()
