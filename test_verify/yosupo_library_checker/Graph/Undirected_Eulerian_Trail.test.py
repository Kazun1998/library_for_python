# verification-helper: PROBLEM https://judge.yosupo.jp/problem/eulerian_trail_undirected

#==================================================
import sys
sys.path.append('~/Graph/Digraph')

from Graph.Graph.Graph import Graph as Undirected_Graph
from Graph.Graph.Eulerian import *


input=sys.stdin.readline
write=sys.stdout.write

#==================================================
def verify():
    N, M = map(int, input().split())

    G = Undirected_Graph(N)
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
