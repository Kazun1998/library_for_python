from Graph import *

# Cycleが存在する?
def Is_Exist_Cycle(G: Graph):
    return G.order < G.size + Connected_Component_Number(G)

def Find_Cycle(G: Graph) -> list[Edge]:
    """ G におけるサイクルを見つける (存在しない場合は None)

    Args:
        G (Graph): グラフ

    Returns:
        list[int]: サイクル (存在しない場合は None)
    """

    N = G.order

    seen = [False] * N
    upper = [None] * N

    # DFS 木における後退辺があれば, その後退辺を含むサイクルが存在する.
    def find_cycle(start: int) -> list[Edge]:
        seen[start] = True
        stack = [edge for edge in G.adjacent[start]]

        while stack:
            edge = stack.pop()

            u = edge.source
            v = edge.target

            if seen[v]:
                back_edge = edge
                break

            seen[v] = True
            upper[v] = edge

            edge_id = edge.id
            stack.extend([e for e in G.adjacent[v] if e.id != edge_id])
        else:
            return None

        cycle = [back_edge]
        u = back_edge.source
        while u != v:
            edge = upper[u]
            cycle.append(edge)
            u = edge.source
        return cycle

    for x in range(N):
        if seen[x]:
            continue

        cycle = find_cycle(x)
        if cycle is not None:
            cycle.reverse()
            return cycle

    return None
