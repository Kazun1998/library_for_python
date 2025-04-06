# verification-helper: PROBLEM https://judge.yosupo.jp/problem/two_sat

#==================================================
from Two_SAT import *

import sys
input=sys.stdin.readline
write=sys.stdout.write

#==================================================
def verify():
    p, cnf, N, M = input().split()
    N = int(N); M = int(M)

    T = Two_SAT(N)
    for _ in range(M):
        a, b, zero = map(int,input().split())

        if a > 0:
            a = a - 1
        else:
            a = ~(-a - 1)

        if b > 0:
            b = b - 1
        else:
            b = ~(-b - 1)

        T.add_or(a, b)

    T.calculate()

    if not T.is_satisfiable:
        print("s","UNSATISFIABLE")
        return

    print("s","SATISFIABLE")
    ans = T.ans
    V = [i + 1 if ans[i] else -(i + 1) for i in range(N)]
    V.append(0)

    print("v", *V)

#==================================================
verify()
