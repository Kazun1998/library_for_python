# verification-helper: PROBLEM https://judge.yosupo.jp/problem/cycle_detection_undirected

#==================================================
from Graph.Graph.Graph import Graph as Undirected_Graph
from Graph.Graph.Cycle import *

import sys
input=sys.stdin.readline
write=sys.stdout.write

#==================================================
def verify():
    N, M = map(int, input().split())

    G = Undirected_Graph(N)
    for j in range(M):
        a, b = map(int, input().split())
        G.add_edge(a, b, j)

    cycle = Find_Cycle(G)

    if cycle['vertex'] is None:
        print(-1)
    else:
        print(len(cycle['edge']))
        print(*cycle['vertex'][:-1])
        print(*cycle['edge'])

#==================================================
verify()
