# verification-helper: PROBLEM https://judge.yosupo.jp/problem/jump_on_tree

#==================================================
import sys
from Tree.Tree import Tree

input=sys.stdin.readline
write=sys.stdout.write
#==================================================
def verify():
    N,Q=map(int,input().split())

    E=[]
    for j in range(N-1):
        a,b=map(int,input().split())
        E.append((a,b))

    T=Tree.make_tree_from_adjacent_list(N, E, 0, 0)

    X=[0]*Q
    for q in range(Q):
        s,t,i=map(int,input().split())
        X[q]=T.jump(s,t,i)

    write("\n".join(map(str,X)))


#==================================================
verify()
