"""
Note
通称 "牛ゲー" と呼ばれる問題を解く. この問題は M 個の条件
    x[i[m]]-x[j[m]]<=c[m]
において, x[p]-x[q] を最大化する. なお, これは x[q]=0 という追加制約化での x[p] の最大化になる.

※ 最短路問題に帰着
"""

class Difference_Maximize:
    def __init__(self, n: int):
        self.__n = n
        self.__arcs = [[] for _ in range(n)]
        self.__has_negative_arc = False

    @property
    def n(self) -> int:
        return self.__n

    @property
    def has_negative_arc(self) -> bool:
        return self.__has_negative_arc

    def __topological_sort(self) -> list[int]:
        topological_sort = []
        in_deg = [0] * self.n

        for s in range(self.n):
            for t, _ in self.__arcs[s]:
                in_deg[t] += 1

        stack = [v for v in range(self.n) if in_deg[v] == 0]
        while stack:
            x = stack.pop()
            topological_sort.append(x)

            for y, _ in self.__arcs[x]:
                in_deg[y] -= 1
                if in_deg[y] == 0:
                    stack.append(y)

        if len(topological_sort) == self.n:
            return topological_sort
        else:
            return None

    def inequality_constraint(self, i: int, j: int, c: int):
        """ 不等式条件 X[i] - X[j] <= c を追加する.

        Args:
            i (int):
            j (int):
            c (int):
        """

        assert 0 <= i < self.n
        assert 0 <= j < self.n

        if c < 0:
            self.__has_negative_arc = True

        self.__arcs[j].append((i, c))

    def equality_constraint(self, i: int, j: int, c: int):
        """ 不等式条件 X[i] - X[j] = c を追加する.

        Args:
            i (int):
            j (int):
            c (int):
        """

        self.inequality_constraint(i, j, c)
        self.inequality_constraint(j, i, -c)

    def solve(self, s: int) -> list[int]:
        if (topological_sort := self.__topological_sort()) is None:
            return self.solve_by_dp_on_dag(s, topological_sort)
        elif self.has_negative_arc:
            return self.solve_by_bellman_ford(s)
        else:
            return self.solve_by_dijkstra(s)

    def solve_by_dp_on_dag(self, s: int, topological_sort: list[int]) -> list[int]:
        inf = float("inf")
        dist = [inf] * self.n; dist[s] = 0
        for x in topological_sort:
            for y, w in self.__arcs[x]:
                dist[y] = min(dist[y], dist[x] + w)
        return dist

    def solve_by_bellman_ford(self, s: int) -> list[int]:
        inf = float("inf")
        dist = [inf] * self.n
        dist[s] = 0

        def update(negative_cycle = False):
            updated = False
            for p in range(self.n):
                for q, c in self.__arcs[p]:
                    if dist[q] > dist[p] + c:
                        if negative_cycle:
                            dist[q] = -inf
                        else:
                            dist[q] = dist[p] + c
                        updated = True
            return updated

        for _ in range(self.n):
            if not update():
                return dist

        for _ in range(self.n):
            if not update(True):
                return dist

    def solve_by_dijkstra(self, s: int) -> list[int]:
        from heapq import heappush, heappop

        inf = float("inf")
        dist = [inf] * self.n
        dist[s] = 0
        Q = [(0, s)]
        while Q:
            d, x = heappop(Q)
            if d > dist[x]:
                continue

            for y, c in self.__arcs[x]:
                if dist[y] > dist[x] + c:
                    dist[y] = dist[x] + c
                    heappush(Q, (dist[y], y))
        return dist
