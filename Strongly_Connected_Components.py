class Strongly_Connected_Components:
    def __init__(self, N: int):
        """ N 頂点の有向グラフを生成する.

        Args:
            N (int): 頂点数
        """

        self.arc: list[list[int]] = [[] for _ in range(N)]
        self.rev: list[list[int]] = [[] for _ in range(N)]

    @property
    def N(self):
        return len(self.arc)

    def add_vertex(self) -> int:
        """ 1 頂点を追加する.

        Returns:
            int: 追加した頂点の番号
        """

        self.arc.append([])
        self.rev.append([])
        return self.N - 1

    def add_vertices(self, k: int = 1) -> list[int]:
        """ 頂点を k 個追加する.

        Args:
            k (int, optional): 追加する頂点数. Defaults to 1.

        Returns:
            list[int]: 追加した k 個の頂点の番号
        """

        self.arc.extend([[] for _ in range(k)])
        self.rev.extend([[] for _ in range(k)])
        return list(range(self.N - k, self.N))

    def add_arc(self, source: int, target: int):
        """ source から target への弧を結ぶ.

        Args:
            source (int): 弧の始点
            target (int): 弧の終点
        """

        self.arc[source].append(target)
        self.rev[target].append(source)

    def decomposition(self):
        """有向グラフを強連結成分に分解"""

        group = [0] * self.N
        D = [False] * self.N
        O = []

        # 1st DFS
        for v in range(self.N):
            if group[v] != 0:
                continue

            stack = [~v, v]

            while stack:
                v = stack.pop()
                if v >= 0:
                    # in
                    if group[v] == -1:
                        continue

                    group[v] = -1
                    for w in self.arc[v]:
                        if not group[w]:
                            stack.append(~w)
                            stack.append(w)
                else:
                    # out
                    v = ~v
                    if D[v]:
                        continue

                    D[v] = True
                    O.append(v)

        components = []
        # 2nd DFS
        for v in reversed(O):
            if group[v] != -1:
                continue

            stack = [v]
            component = [v]
            group[v] = len(components)

            while stack:
                w = stack.pop()
                for u in self.rev[w]:
                    if group[u] != -1:
                        continue

                    group[u] = len(components)
                    component.append(u)
                    stack.append(u)

            components.append(component)

        self.__components = components
        self.__group = group

    @property
    def components(self) -> list[list[int]]:
        return self.__components

    @property
    def group(self) -> list[int]:
        return self.__group
