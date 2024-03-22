# verification-helper: PROBLEM https://judge.yosupo.jp/problem/eulerian_trail_directed

#==================================================
from Graph.Digraph.Digraph import Digraph as Directed_Graph
from Graph.Digraph.Eulerian import *

import sys
input=sys.stdin.readline
write=sys.stdout.write

#==================================================
def verify():
    N, M = map(int, input().split())

    D = Directed_Graph(N)
    for j in range(M):
        u, v = map(int, input().split())
        D.add_arc(u, v, j)

    euler = Find_Directed_Eulerian_Trail(D)

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
