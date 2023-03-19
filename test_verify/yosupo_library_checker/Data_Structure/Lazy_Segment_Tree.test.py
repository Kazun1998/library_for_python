# verification-helper: PROBLEM https://judge.yosupo.jp/problem/range_affine_range_sum

#==================================================
from Segment_Tree.Lazy_Segment_Tree import Lazy_Evaluation_Tree

import sys
input=sys.stdin.readline
write=sys.stdout.write

#==================================================
def verify():
    def op(p,q):
        a,x=p>>32,p&msk
        b,y=q>>32,q&msk
        return ((a+b)%Mod<<32)+(x+y)

    def act(u,p):
        b,c=u>>32,u&msk
        a,x=p>>32,p&msk
        return (((a*b+c*x)%Mod)<<32)+x

    def comp(u,v):
        b1,c1=u>>32,u&msk
        b2,c2=v>>32,v&msk
        return (((b1*b2)%Mod)<<32)+(b1*c2+c1)%Mod

    N,Q=map(int,input().split())
    A=[(a<<32)+1 for a in map(int,input().split())]

    Mod=998244353
    msk=(1<<32)-1
    S=Lazy_Evaluation_Tree(A,op,0,act,comp,1<<32)

    Ans=[]
    for q in range(Q):
        t,*query=map(int,input().split())
        if t==0:
            l,r,b,c=query
            S.action(l,r-1,(b<<32)+c)
        else:
            l,r=query
            Ans.append(S.product(l,r-1)>>32)

    write("\n".join(map(str,Ans)))

#==================================================
verify()
