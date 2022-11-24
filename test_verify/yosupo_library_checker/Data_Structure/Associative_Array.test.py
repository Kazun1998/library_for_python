# verification-helper: PROBLEM https://judge.yosupo.jp/problem/associative_array

#==================================================
from Hash_Table import *

import sys
input=sys.stdin.readline
write=sys.stdout.write

#==================================================
def verify():
    Q=int(input())

    H=Hash_Table()
    ans=[]
    for q in range(Q):
        mode,*query=map(int,input().split())

        if mode==0:
            H[query[0]]=query[1]
        else:
            ans.append(H.get(query[0],0))

    write("\n".join(map(str,ans)))


#==================================================
verify()
