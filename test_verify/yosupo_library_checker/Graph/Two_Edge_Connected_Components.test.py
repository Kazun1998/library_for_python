# verification-helper: PROBLEM https://judge.yosupo.jp/problem/two_edge_connected_components

#==================================================
from Graph.Graph.Graph import Graph as Undirected_Graph
from Graph.Graph.Graph import Two_Edge_Connected_Components

import sys
input=sys.stdin.readline
write=sys.stdout.write

#==================================================
def verify():
    N, M = map(int, input().split())

    G = Undirected_Graph(N)
    for j in range(M):
        a, b = map(int, input().split())
        G.add_edge(a, b)

    components = Two_Edge_Connected_Components(G)['components']

    def writer(component):
        return f"{len(component)} {' '.join(map(str, component))}"

    print(len(components))
    write("\n".join(map(writer, components)))

#==================================================
verify()
