def Find_Directed_Eulerian_Trail(D: Digraph):
    N = D.order()

    remain = [D.out_degree(v) for v in range(N)]

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
        return { 'vertex': None, 'arc': None }

    if start == -1:
        for v in range(N):
            if D.out_degree(v):
                start = goal = v
                break
        else:
            start = goal = 0

    adj_out = [[arc for arc in D.adjacent_out[x]] for x in range(N)]

    def dfs(start):
        path = []

        x = start
        while True:
            if not adj_out[x]:
                break

            y, i = adj_out[x].pop()
            path.append((x, y, i))
            remain[x] -= 1
            x = y
        return path

    stack = dfs(start)
    arc = []
    vertex = [goal]
    while stack:
        u, _, j = stack.pop()
        vertex.append(u)
        arc.append(j)

        if remain[u]:
            stack.extend(dfs(u))

    if len(arc) == D.size():
        vertex.reverse()
        arc.reverse()
        return { 'vertex': vertex, 'arc': arc }
    else:
        return { 'vertex': None, 'arc': None }
