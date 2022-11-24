# verification-helper: PROBLEM https://judge.yosupo.jp/problem/predecessor_problem

#==================================================
from Ordered_Set.Ordered_Set import *

import sys
input=sys.stdin.readline
write=sys.stdout.write

#==================================================
def verify():
    N,Q=map(int,input().split())
    T=list(map(int,input()[:-1]))

    S=Ordered_Set(N,S=T)

    Ans=[]
    for q in range(Q):
        c,k=map(int,input().split())
        if c==0:
            S.add(k)
        elif c==1:
            S.discard(k)
        elif c==2:
            Ans.append(S.count(k))
        elif c==3:
            Ans.append(S.next(k))
        else:
            Ans.append(S.previous(k))

    write("\n".join(map(str,Ans)))


#==================================================
verify()
