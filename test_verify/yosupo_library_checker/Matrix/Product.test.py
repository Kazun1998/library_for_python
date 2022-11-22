# verification-helper: PROBLEM https://judge.yosupo.jp/problem/matrix_product

#==================================================
from Modulo_Matrix.Modulo_Matrix import Modulo_Matrix

import sys
input=sys.stdin.readline
write=sys.stdout.write

#==================================================
def verify():
    N,M,K=map(int,input().split())

    A=[]
    for i in range(N):
        A.append(list(map(int,input().split())))

    B=[]
    for i in range(M):
        B.append(list(map(int,input().split())))

    C=Modulo_Matrix(A)*Modulo_Matrix(B)

    string=lambda x:" ".join(map(str,x))
    write("\n".join(map(string,C.ele)))

#==================================================
verify()