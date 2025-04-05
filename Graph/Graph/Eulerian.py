from Graph import *

#オイラーグラフ?
def Is_Eulerian_Graph(G: Graph):
    """ グラフ G がオイラーグラフかどうかを判定する. """
    return all(G.degree(v) % 2 == 0 for v in range(G.order)) and Is_Connected(G)

#準オイラーグラフ?
def Is_Semi_Eulerian_Graph(G: Graph):
    """ グラフ G が準オイラーグラフかどうかを判定する. """
    return len([v for v in range(G.order) if G.degree(v) % 2 == 0]) == 2 and Is_Connected(G)

#Euler (閉) 路を見つける
def Find_Eulerian_Trail(G: Graph) -> list[Edge]:
    """ Euler (閉) 路を求める.

    Args:
        G (Graph):

    Returns:
        list[Edge]: Euler (閉)路
    """

    N = G.order

    remain = [G.degree(v) for v in range(N)]

    odd_vertex = [v for v in range(N) if remain[v] % 2 == 1]

    if len(odd_vertex) > 2:
        # 奇頂点の頂点数が 2 より大きい (iff 4 以上) ならば 存在しない.
        return None

    # Euler (閉) 路を求めるための始点を終点を求める.
    if odd_vertex:
        # 奇頂点の個数が 2 のとき
        start, goal = odd_vertex
    else:
        # 奇頂点が存在しないとき
        for v in range(N):
            if remain[v]:
                start = goal = v
                break
        else:
            start = goal = 0

    adj = [[edge.id for edge in G.adjacent[x]] for x in range(N)]
    seen = set()

    def dfs(start):
        path = []

        x = start
        while True:
            if not adj[x]:
                break

            edge_id = adj[x].pop()
            if edge_id in seen:
                continue

            seen.add(edge_id)
            edge = G.get_edge(edge_id, x)
            y = edge.target
            path.append((x, y, edge_id))
            remain[x] -= 1; remain[y] -= 1
            x = y
        return path

    stack = dfs(start)
    euler_trail: list[Edge] = []
    while stack:
        u, _, j = stack.pop()
        euler_trail.append(G.get_edge(j, u))

        if remain[u]:
            stack.extend(dfs(u))

    if len(euler_trail) == G.size:
        euler_trail.reverse()
        return euler_trail
    else:
        return None
