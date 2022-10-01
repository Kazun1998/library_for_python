# verification-helper: PROBLEM https://judge.yosupo.jp/problem/point_add_range_sum

#==================================================
import sys
sys.path.append('Binary_Indexed_Tree/')
from Binary_Indexed_Tree import Binary_Indexed_Tree

input=sys.stdin.readline
write=sys.stdout.write

#==================================================
def verify():
    from operator import add,neg

    N,Q=map(int,input().split())
    A=list(map(int,input().split()))
    B=Binary_Indexed_Tree(A,add,0,neg)

    Ans=[]
    for q in range(Q):
        mode,*query=map(int,input().split())

        if mode==0:
            B.add(query[0],query[1])
        else:
            Ans.append(B.sum(query[0],query[1]-1))

    write("\n".join(map(str,Ans)))

#==================================================
verify()
