# verification-helper: PROBLEM https://judge.yosupo.jp/problem/double_ended_priority_queue

#==================================================
from Binary_Tree.Red_and_Black_Tree import *

import sys
input=sys.stdin.readline
write=sys.stdout.write

#==================================================
def verify():
    N,Q=map(int,input().split())
    S=map(int,input().split())

    E=Red_and_Black_Tree()
    for a in S:
        E[a]=E.get(a,0)+1

    Ans=[]
    for _ in range(Q):
        mode,*value=map(int,input().split())
        if mode==0:
            x=value[0]
            E[x]=E.get(x,0)+1
        elif mode==1:
            y=E.get_min()
            E[y]-=1
            if E[y]==0:
                E.delete(y)
            Ans.append(y)
        elif mode==2:
            z=E.get_max()
            E[z]-=1
            if E[z]==0:
                E.delete(z)
            Ans.append(z)
    write("\n".join(map(str,Ans)))

#==================================================
verify()
