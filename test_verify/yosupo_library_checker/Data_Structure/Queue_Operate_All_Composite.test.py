# verification-helper: PROBLEM https://judge.yosupo.jp/problem/queue_operate_all_composite

#==================================================
from Sliding_Window_Aggregation import *

import sys
input=sys.stdin.readline
write=sys.stdout.write

#==================================================
def verify():
    Q=int(input())

    Mod=998244353
    def calc(f,g):
        return (f[0]*g[0]%Mod, (f[1]*g[0]+g[1])%Mod)

    S=Sliding_Window_Aggregation(calc)
    X=[]
    for _ in range(Q):
        mode,*query=map(int,input().split())
        if mode==0:
            S.push(query)
        elif mode==1:
            S.pop()
        else:
            a,b=S.product([1,0])
            X.append((a*query[0]+b)%Mod)

    write("\n".join(map(str,X)))


#==================================================
verify()
