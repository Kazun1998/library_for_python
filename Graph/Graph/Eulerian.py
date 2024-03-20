from Graph import *

#オイラーグラフ?
def Is_Eulerian_Graph(G: Graph):
    """ グラフ G がオイラーグラフかどうかを判定する. """
    return all(G.degree(v) % 2 == 0 for v in range(G.order())) and Is_Connected(G)

#準オイラーグラフ?
def Is_Semi_Eulerian_Graph(G: Graph):
    """ グラフ G が準オイラーグラフかどうかを判定する. """
    return len([v for v in range(G.order()) if G.degree(v) % 2 == 0]) == 2 and Is_Connected(G)

#Euler (閉) 路を見つける
def Find_Eulerian_Trail(G: Graph):
    N = G.order()

    remain = [G.degree(v) for v in range(N)]

    odd_vertex = [v for v in range(N) if remain[v] % 2 == 1]
    if len(odd_vertex) > 2:
        return { 'vertex': None, 'edge': None }
    elif len(odd_vertex) == 2:
        start, goal = odd_vertex
    else:
        start = goal = 0

    adj = [[edge for edge in G.adjacent[x]] for x in range(N)]
    seen = set()

    def dfs(start):
        path = []

        x = start
        while True:
            if not adj[x]:
                break

            y, i = adj[x].pop()
            if i in seen:
                continue

            seen.add(i)
            path.append((x, y, i))
            remain[x] -= 1; remain[y] -= 1
            x = y
        return path

    stack = dfs(start)
    edge = []
    vertex = [goal]
    while stack:
        u, _, j = stack.pop()
        vertex.append(u)
        edge.append(j)

        if remain[u]:
            stack.extend(dfs(u))

    if len(edge) == G.size():
        return { 'vertex': vertex, 'edge': edge }
    else:
        return { 'vertex': None, 'edge': None }
