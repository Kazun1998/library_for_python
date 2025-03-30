from Weighted_Digraph import *

def Bellman_Ford(D: Weighted_Digraph, start: int, goal: int, default = None) -> int:
    inf = D.inifinity
    N = D.order

    dist = D.initialize_list(inf)
    dist[start] = 0

    arcs = [(arc.source, arc.target, arc.weight) for arc in D.arcs_generator()]

    def update_dist(negative_cycle: bool) -> bool:
        updated = False
        for source, target, weight in arcs:
            if dist[source] >= inf or not(dist[source] + weight < dist[target]):
                continue

            if negative_cycle:
                dist[target] = -float('inf')
            else:
                dist[target] = dist[source] + weight
            updated = True

        return updated

    for _ in range(N):
        if not update_dist(False):
            return dist[goal] if dist[goal] < inf else default

    for _ in range(N):
        if not update_dist(True):
            break

    return dist[goal] if dist[goal] < inf else default