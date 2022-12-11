# verification-helper: PROBLEM https://judge.yosupo.jp/problem/double_ended_priority_queue

#==================================================
from Double_Heap import *

import sys
input=sys.stdin.readline
write=sys.stdout.write

#==================================================
def verify():
    N,Q=map(int,input().split())
    S=map(int,input().split())

    H=Double_Heap()
    for a in S:
        H.push(a)

    Ans=[]
    for _ in range(Q):
        mode,*value=map(int,input().split())
        if mode==0:
            H.push(value[0])
        elif mode==1:
            Ans.append(H.pop_min())
        else:
            Ans.append(H.pop_max())
    write("\n".join(map(str,Ans)))

#==================================================
verify()
