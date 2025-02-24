from Graph import *

# Cycleが存在する?
def Is_Exist_Cycle(G: Graph):
    return G.order < G.size + Connected_Component_Number(G)

def Find_Cycle(G: Graph):
    N = G.order

    seen = [False] * N
    parent = [-1] * N
    upper = [-1] * N
    def dfs(start):
        seen[start] = True
        stack = [(start, v, j) for v, j in G.partner_with_label_yield(start)]
        while stack:
            u, v, j = stack.pop()

            if seen[v]:
                vertex = [v, u]
                edge = [j]
                while u != v:
                    edge.append(upper[u])
                    u = parent[u]
                    vertex.append(u)
                return vertex, edge

            seen[v] = True
            parent[v] = u
            upper[v] = j

            stack.extend([(v, w, k) for w, k in G.partner_with_label_yield(v) if k != j])
        return None, None

    for x in range(N):
        if not seen[x]:
            vertex, edge = dfs(x)
            if vertex is not None:
                return { 'vertex': vertex, 'edge': edge }
    else:
        return { 'vertex': None, 'edge': None }
