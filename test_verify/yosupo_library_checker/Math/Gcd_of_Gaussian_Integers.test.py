# verification-helper: PROBLEM https://judge.yosupo.jp/problem/gcd_of_gaussian_integers

#==================================================
from Gaussian_Integers import *

import sys
input=sys.stdin.readline
write=sys.stdout.write

#==================================================
def verify():
    a, b, c, d = map(int, input().split())
    g = gcd(Gaussian_Integer(a, b), Gaussian_Integer(c, d))
    return f'{g.re} {g.im}'

#==================================================
T = int(input())
write("\n".join(verify()))
