# verification-helper: PROBLEM https://judge.yosupo.jp/problem/binomial_coefficient_prime_mod

#==================================================
from Enumeration import *

import sys
input=sys.stdin.readline
write=sys.stdout.write

#==================================================
def verify():
    T, m = map(int, input().split())

    global Mod; Mod = m
    global fact, fact_inv
    fact, fact_inv = Factor_with_inverse(min(m, 10 ** 7))

    ans = [0] * T
    for t in range(T):
        n, k = map(int, input().split())
        ans[t] = nCr(n, k)
    return ans

#==================================================
write("\n".join(map(str, verify())))
