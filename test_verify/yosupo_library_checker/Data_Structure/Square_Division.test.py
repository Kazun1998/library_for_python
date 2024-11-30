# verification-helper: PROBLEM https://judge.yosupo.jp/problem/static_range_sum

#==================================================
from Division.Square_Division import *

import sys
input=sys.stdin.readline
write=sys.stdout.write

#==================================================
def verify():
    from operator import add

    N, Q = map(int, input().split())
    A = list(map(int, input().split()))

    S = Square_Division(A, add, 0)
    ans = [0] * Q

    for q in range(Q):
        l, r = map(int, input().split())
        ans[q] = S.product(l, r - 1)

    write("\n".join(map(str, ans)))

#==================================================
verify()
