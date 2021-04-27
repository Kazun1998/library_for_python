from heapq import heappush, heappop
class MinCostFlow_by_Dijkstra:
    #Dijkstraによる最小費用流問題
    #(参考元:https://tjkendev.github.io/procon-library/python/min_cost_flow/primal-dual.html)
    INF = float("inf")

    def __init__(self, N):
        self.N = N
        self.G = [[] for i in range(N)]
        self.E=set()

    def add_edge(self, fr, to, cap, cost):
        forward = [to, cap, cost, None]
        backward = forward[3] = [fr, 0, -cost, forward]
        self.G[fr].append(forward)
        self.G[to].append(backward)
        self.E.add((fr,to))

    def flow(self, s, t, f,Mode=False):
        N = self.N; G = self.G
        INF = MinCostFlow_by_Dijkstra.INF

        res = 0
        H = [0]*N
        prv_v = [0]*N
        prv_e = [None]*N

        d0 = [INF]*N
        dist = [INF]*N

        while f:
            dist[:] = d0
            dist[s] = 0
            que = [(0, s)]

            while que:
                c, v = heappop(que)
                if dist[v] < c:
                    continue
                r0 = dist[v] + H[v]
                for e in G[v]:
                    w, cap, cost, _ = e
                    if cap > 0 and r0 + cost - H[w] < dist[w]:
                        dist[w] = r = r0 + cost - H[w]
                        prv_v[w] = v; prv_e[w] = e
                        heappush(que, (r, w))
            if dist[t] == INF:
                return None

            for i in range(N):
                H[i] += dist[i]

            d = f; v = t
            while v != s:
                d = min(d, prv_e[v][1])
                v = prv_v[v]
            f -= d
            res += d * H[t]
            v = t
            while v != s:
                e = prv_e[v]
                e[1] -= d
                e[3][1] += d
                v = prv_v[v]

        if Mode:
            R={}
            for v in range(self.N):
                R[v]={}
                for S in self.G[v]:
                    w=S[0]
                    if (v,w) in self.E:
                        R[v][w]=S[-1][1]

            return res,R
        else:
            return res
