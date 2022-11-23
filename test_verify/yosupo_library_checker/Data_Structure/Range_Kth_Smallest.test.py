# verification-helper: PROBLEM https://judge.yosupo.jp/problem/range_kth_smallest

#==================================================
from Wavelet_Matrix import *

import sys
input=sys.stdin.readline
write=sys.stdout.write

#==================================================
def verify():
    N,Q=map(int,input().split())

    A=list(map(int,input().split()))
    W=Wavelet_Matrix(A)

    Ans=[0]*Q

    for q in range(Q):
        l,r,k=map(int,input().split())
        Ans[q]=W.quantile(l,r,k+1)

    write("\n".join(map(str,Ans)))


#==================================================
verify()
