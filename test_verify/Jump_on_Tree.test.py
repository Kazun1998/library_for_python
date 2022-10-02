# verification-helper: PROBLEM https://judge.yosupo.jp/problem/jump_on_tree

#==================================================
import sys
sys.path.append('Tree/')
from  Tree import Tree, Making_Tree_from_Edges

input=sys.stdin.readline
write=sys.stdout.write
#==================================================
def verify():
    N,Q=map(int,input().split())

    E=[]
    for j in range(N-1):
        a,b=map(int,input().split())
        E.append((a,b))

    T=Making_Tree_from_Edges(N, E, 0, 0)

    X=[0]*Q
    for q in range(Q):
        s,t,i=map(int,input().split())
        X[q]=T.jump(s,t,i)

    write("\n".join(map(str,X)))

#==================================================
verify()
