# verification-helper: PROBLEM https://judge.yosupo.jp/problem/staticrmq

#==================================================
import sys
#sys.path.append('../')
from Disjoint_Sparse_Table import Disjoint_Sparse_Table

import sys
input=sys.stdin.readline
write=sys.stdout.write
#==================================================
def verify():
    N,Q=map(int,input().split())
    A=list(map(int,input().split()))

    D=Disjoint_Sparse_Table(A,min)
    Ans=[0]*Q
    for q in range(Q):
        l,r=map(int,input().split())
        Ans[q]=D.product(l,r,None,True,False)

    write("\n".join(map(str,Ans)))

#==================================================
verify()
