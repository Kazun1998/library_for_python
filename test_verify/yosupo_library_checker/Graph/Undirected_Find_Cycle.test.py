# verification-helper: PROBLEM https://judge.yosupo.jp/problem/cycle_detection_undirected

#==================================================
from Graph.Graph.Graph import Graph as Undirected_Graph
from Graph.Graph.Graph import Edge
from Graph.Graph.Cycle import *

import sys
input=sys.stdin.readline
write=sys.stdout.write

#==================================================
def verify():
    N, M = map(int, input().split())
    G = Undirected_Graph(N)
    for _ in range(M):
        a, b = map(int, input().split())
        G.add_edge(a, b)

    cycle = Find_Cycle(G)

    if cycle is not None:
        print(len(cycle))
        print(*[edge.source for edge in cycle])
        print(*[edge.id for edge in cycle])
    else:
        print(-1)

#==================================================
verify()
