# verification-helper: PROBLEM https://judge.yosupo.jp/problem/lca

#==================================================
from Tree.Tree import Tree

import sys
input=sys.stdin.readline
write=sys.stdout.write
#==================================================
def verify():
    N,Q=map(int,input().split())
    P=[0]+list(map(int,input().split()))

    T=Tree(N)
    T.root_set(0)
    for i in range(1,N):
        T.parent_set(i,P[i])
    T.seal()

    X=[0]*Q
    for q in range(Q):
        u,v=map(int,input().split())
        X[q]=T.lowest_common_ancestor(u,v)

    write("\n".join(map(str,X)))

#==================================================
verify()
