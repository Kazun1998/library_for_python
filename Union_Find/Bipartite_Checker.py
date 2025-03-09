from Union_Find import Union_Find

class Bipartite_Check:
    __slots__ = ("_N", "__Union")

    def __init__(self, N: int):
        self._N = N
        self.__Union=Union_Find(2 * N)

    @property
    def N(self) -> int:
        return self._N

    def add_edge(self, u: int, v: int, same: bool = False):
        """ 辺 uv を加える. ただし, same が True のときは, 「u, v は同じ色にしなくてはならない」という条件になる.

        Args:
            u (int): 頂点
            v (int): 頂点
            same (bool, optional): True だと, 「u, v は同じ色にしなくてはならない」になる. Defaults to False.
        """

        if same:
            self.__Union.union(u, v)
            self.__Union.union(u + self.N, v + self.N)
        else:
            self.__Union.union(u, v + self.N)
            self.__Union.union(u + self.N, v)

    def check(self) -> bool:
        """ 条件に合うように分割できる?

        Returns:
            bool:
        """

        U = self.__Union
        N = self.N
        return not any(U.same(x, x + N) for x in range(N))

    def bipartite_example(self) -> list[int] | None:
        """ 分割の一例を求める (存在しない場合は None).

        Returns:
            list[int] | None: 分割の方法を 01 で与えるリスト (存在しない場合は None).
        """

        X = [None] * self.N
        G = self.__Union.all_group_members()

        for x in range(self.N):
            if X[x] is not None:
                continue

            key = self.__Union.find(x)
            for y in G[key]:
                if y < self.N:
                    if X[y] == 1:
                        return None
                    X[y] = 0
                else:
                    if X[y- self.N] == 0:
                        return None
                    X[y - self.N] = 1
        return X

    def bipartite(self) -> list[tuple[list, list]] | None:
        """ 分割に関する情報を求める (存在しない場合は None).
        返り値を [(U0, V0), (U1, V1), ...] としたとき, 次が成り立つ.
            + Ui に属する頂点同士は同じ色でなくてはならない.
            + Ui に属する頂点 u と Vi に属する頂点 v について, u, v は異なる色でなくてはならない.
            + それ以外の組み合わせについては自由.

        Returns:
            list[tuple[list, list]] | None: 分割の情報
        """

        bipartite = []
        seen = [False] * self.N
        G = self.__Union.all_group_members()

        for x in range(self.N):
            if seen[x]:
                continue

            g = self.__Union.find(x)
            red = []; blue = []
            for y in G[g]:
                if seen[y % self.N]:
                    # 不可能確定
                    return None

                seen[y % self.N] = True

                if y < self.N:
                    red.append(y)
                else:
                    blue.append(y - self.N)

            bipartite.append((red, blue))

        return bipartite

    def bipart_cases(self, Mod: int = None) -> int:
        """ 分割の場合の数 (を Mod で割った余り) を求める.

        Args:
            Mod (int, optional): 剰余 (None にするとそのままの値). Defaults to None.

        Returns:
            int: 分割の場合の数 (を Mod で割った余り)
        """

        if (bipartite := self.bipartite()) is None:
            return 0

        return pow(2, len(bipartite), Mod)
