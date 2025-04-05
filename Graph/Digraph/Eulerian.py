from Digraph import *

def Find_Directed_Eulerian_Trail(D: Digraph) -> list[Arc]:
    """ Euler (閉) 路を生成する.

    Args:
        D (Digraph): 有向グラフ

    Returns:
        list[Arc]: Euler (閉) 路
    """
    N = D.order

    remain_out = [D.out_degree(v) for v in range(N)]

    start = goal = -1
    necessary = True
    # 必要条件チェック
    for v in range(N):
        out_deg = D.out_degree(v)
        in_deg = D.in_degree(v)

        if abs(out_deg - in_deg) >= 2:
            necessary = False
        elif out_deg - in_deg == 1:
            if start == -1:
                start = v
            else:
                necessary = False
        if out_deg - in_deg == -1:
            goal = v

    if not necessary:
        return None

    if start == -1:
        for v in range(N):
            if D.out_degree(v):
                start = goal = v
                break
        else:
            start = goal = 0

    adj_out = [[arc.id for arc in D.adjacent_out[x]] for x in range(N)]

    def dfs(start):
        path: list[int] = []

        x = start
        while True:
            if not adj_out[x]:
                break

            arc_id = adj_out[x].pop()
            arc = D.get_arc(arc_id)

            path.append(arc_id)
            remain_out[x] -= 1
            x = arc.target
        return path

    stack = dfs(start)
    eulerian_trail: list[Arc] = []
    while stack:
        arc_id = stack.pop()
        arc = D.get_arc(arc_id)
        eulerian_trail.append(arc)

        if remain_out[arc.source]:
            stack.extend(dfs(arc.source))

    if len(eulerian_trail) == D.size:
        eulerian_trail.reverse()
        return eulerian_trail
    else:
        return None
