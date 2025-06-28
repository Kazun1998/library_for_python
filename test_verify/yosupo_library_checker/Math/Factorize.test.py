# verification-helper: PROBLEM https://judge.yosupo.jp/problem/factorize

#==================================================
from Integer.Prime import *

import sys
input=sys.stdin.readline
write=sys.stdout.write

#==================================================
def verify():
    Q = int(input())
    for _ in range(Q):
        a = int(input())
        prime_factors = Pollard_Rho_Prime_Factorization(a)
        primes = []
        for p, e in prime_factors:
            primes.extend([p] * e)

        print(len(primes), *primes)

#==================================================
verify()
