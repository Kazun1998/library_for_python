# verification-helper: PROBLEM https://judge.yosupo.jp/problem/unionfind

import sys
sys.path.append("..")

from Union_Find import Union_Find

input=sys.stdin.readline
write=sys.stdout.write

N,Q=map(int,input().split())
U=Union_Find(N)
X=[]
for _ in range(Q):
    t,u,v=map(int,input().split())
    if t==0:
        U.union(u,v)
    else:
        X.append(1 if U.same(u,v) else 0)

write("\n".join(map(str,X)))
