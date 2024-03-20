# verification-helper: PROBLEM https://judge.yosupo.jp/problem/eulerian_trail_undirected

#==================================================
from Graph.Graph.Eulerian import *

import sys
input=sys.stdin.readline
write=sys.stdout.write

#==================================================
def verify():
    N, M = map(int, input().split())

    G = Graph(N)
    for j in range(M):
        u, v = map(int, input().split())
        G.add_edge(u, v, j)

    euler = Find_Eulerian_Trail(G)
    if euler['vertex'] is None:
        print("No")
    else:
        print('Yes')
        print(*euler['vertex'])
        print(*euler['edge'])

#==================================================
T = int(input())
for _ in range(T):
    verify()
