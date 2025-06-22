# verification-helper: PROBLEM https://judge.yosupo.jp/problem/staticrmq

#==================================================
import sys
#sys.path.append('../')
from Disjoint_Sparse_Table import Disjoint_Sparse_Table

import sys
input=sys.stdin.readline
write=sys.stdout.write
#==================================================
def verify():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))

    D = Disjoint_Sparse_Table[int](A, min)
    ans = [0] * Q
    for q in range(Q):
        l, r = map(int, input().split())
        ans[q] = D.product(l, r, True, False, None)

    write("\n".join(map(str, ans)))

#==================================================
verify()
