# verification-helper: PROBLEM https://judge.yosupo.jp/problem/inverse_matrix

#==================================================
import sys
sys.path.append("../../../")
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

    try:
        B=Modulo_Matrix(A).inverse()
        string=lambda x:" ".join(map(str,x))
        write("\n".join(map(string,B.ele)))
    except:
        print(-1)

#==================================================
verify()