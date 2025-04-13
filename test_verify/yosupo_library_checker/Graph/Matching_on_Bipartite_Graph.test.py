# verification-helper: PROBLEM https://judge.yosupo.jp/problem/bipartitematching

#==================================================
from Bipart_Matching import *

import sys
input=sys.stdin.readline
write=sys.stdout.write

#==================================================
def verify():
    L, R, M = map(int,input().split())
    G = Bipartite_Matching(L,R)

    for _ in range(M):
        a, b=map(int,input().split())
        G.add_edge(a, b)

    G.calculate(True)

    K = G.max_matching_size
    A, B = G.max_matching_size
    H = []
    for i in range(L):
        if A[i] != -1:
            H.append((i, A[i]))

    print(K)
    def string(x):
        return "{} {}".format(x[0], x[1])

    write("\n".join(map(string, H)))
    print()

#==================================================
verify()
