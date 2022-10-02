# verification-helper: PROBLEM https://judge.yosupo.jp/problem/point_set_range_composite

#==================================================
import sys
sys.path.append('../Segment_Tree/')
from Segment_Tree import Segment_Tree

input=sys.stdin.readline
write=sys.stdout.write

#==================================================
def verify():
    N,Q=map(int,input().split())
    Mod=998244353

    A=[0]*N
    for i in range(N):
        a,b=map(int,input().split())
        A[i]=(a,b)

    calc=lambda p,q:((p[0]*q[0])%Mod,(p[1]*q[0]+q[1])%Mod)
    S=Segment_Tree(A,calc,(1,0))

    Ans=[]
    for _ in range(Q):
        m,s,t,u=map(int,input().split())
        if m==0:
            S.update(s,(t,u))
        else:
            (alpha,beta)=S.product(s,t-1)
            Ans.append((alpha*u+beta)%Mod)

    write("\n".join(map(str,Ans)))

#==================================================
verify()
