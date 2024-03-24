# verification-helper: PROBLEM https://judge.yosupo.jp/problem/matrix_rank

#==================================================
from Modulo_Matrix.Modulo_Matrix import Modulo_Matrix

import sys
input=sys.stdin.readline
write=sys.stdout.write

#==================================================
def verify():
    global Mod; Mod = 998244353

    N, M = map(int, input().split())

    A = [None] * N
    for i in range(N):
        A[i] = list(map(int, input().split()))

    A = Modulo_Matrix(A)
    print(A.rank())

#==================================================
verify()
