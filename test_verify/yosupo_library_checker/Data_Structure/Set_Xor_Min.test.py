# verification-helper: PROBLEM https://judge.yosupo.jp/problem/set_xor_min

#==================================================
from Binary_Trie import *

import sys
input=sys.stdin.readline
write=sys.stdout.write

#================================================
def verify():
    Q=int(input())
    B=Binary_Trie((1<<30)-1, query_number=Q)
    X=[]
    for _ in range(Q):
        c,x=map(int,input().split())
        if c==0:
            B.insert(x)
        elif c==1:
            B.discard(x)
        else:
            B^=x
            X.append(B.get_min())
            B^=x

    write("\n".join(map(str,X)))
#==================================================
verify()
