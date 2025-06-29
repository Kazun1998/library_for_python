# verification-helper: PROBLEM https://judge.yosupo.jp/problem/point_add_range_sum

#==================================================
from Binary_Indexed_Tree.Sparse_Binary_Indexed_Tree import Sparse_Binary_Indexed_Tree

import sys
input=sys.stdin.readline
write=sys.stdout.write
#==================================================
def verify():
    from operator import add, neg

    N, Q = map(int, input().split())
    a = list(map(int, input().split()))
    B = Sparse_Binary_Indexed_Tree[int](N, add, 0, neg)

    for i in range(N):
        B.update(i, a[i])

    ans = []
    for _ in range(Q):
        mode, *query = map(int, input().split())

        if mode == 0:
            p, x = query
            B.add(p, x)
        else:
            l, r = query
            ans.append(B.sum(l, r - 1))

    write("\n".join(map(str, ans)))

#==================================================
verify()
