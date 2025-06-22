# verification-helper: PROBLEM https://judge.yosupo.jp/problem/rational_approximation

#==================================================
from Stern_Brocot_Tree import *

import sys
input=sys.stdin.readline
write=sys.stdout.write

#==================================================
def verify():
    T = int(input())

    for _ in range(T):
        N, x, y = map(int, input().split())
        _, _, c, d = Stern_Brocot_Tree.binary_search_range_increase(N, lambda a, b: a * y >= b * x)
        a, b, _, _ = Stern_Brocot_Tree.binary_search_range_increase(N, lambda a, b: a * y > b * x)
        yield f"{a} {b} {c} {d}"

#==================================================

write("\n".join(map(str, verify())))
