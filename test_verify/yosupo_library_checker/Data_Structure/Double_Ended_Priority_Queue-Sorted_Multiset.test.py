# verification-helper: PROBLEM https://judge.yosupo.jp/problem/double_ended_priority_queue

#==================================================
import sys
sys.path.append("../../../")
from Sorted_Set.Sorted_Multiset import *

import sys
input=sys.stdin.readline
write=sys.stdout.write

#==================================================
def verify():
    N,Q=map(int,input().split())
    S=list(map(int,input().split()))

    S=Sorted_Multiset(S)
    Ans=[]
    for _ in range(Q):
        mode,*value=map(int,input().split())
        if mode==0:
            S.add(value[0])
        elif mode==1:
            Ans.append(S.pop_min())
        else:
            Ans.append(S.pop_max())
    write("\n".join(map(str,Ans)))

#==================================================
verify()
