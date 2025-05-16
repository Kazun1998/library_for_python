# verification-helper: PROBLEM https://judge.yosupo.jp/problem/nim_product_64

#==================================================
from Nimber import *

import sys
input=sys.stdin.readline
write=sys.stdout.write

#==================================================
def verify():
    T = int(input())
    ans = [0] * T
    for t in range(T):
        A, B = map(Nimber, input().split())
        ans[t] = A * B

    write("\n".join(map(str, ans)))

#==================================================
verify()