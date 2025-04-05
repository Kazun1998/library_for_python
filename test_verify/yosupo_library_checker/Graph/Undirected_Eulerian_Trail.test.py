# verification-helper: PROBLEM https://judge.yosupo.jp/problem/eulerian_trail_undirected

#==================================================
from Graph.Graph.Graph import Graph as Undirected_Graph
from Graph.Graph.Graph import Edge
from Graph.Graph.Eulerian import *

import sys
input=sys.stdin.readline
write=sys.stdout.write

#==================================================
def verify():
    N, M = map(int, input().split())

    G = Undirected_Graph(N)
    for _ in range(M):
        u, v = map(int, input().split())
        G.add_edge(u, v)

    eulerian_trail = Find_Eulerian_Trail(G)

    if eulerian_trail is None:
        print("No")
        return

    print("Yes")
    if eulerian_trail:
        print(eulerian_trail[0].source, *[edge.target for edge in eulerian_trail])
        print(*[edge.id for edge in eulerian_trail])
    else:
        print(0)
        print()

#==================================================
T = int(input())
for _ in range(T):
    verify()
