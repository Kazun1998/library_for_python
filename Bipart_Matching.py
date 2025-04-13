# 参考 URL
# https://snuke.hatenablog.com/entry/2019/05/07/013609

class Bipartite_Matching:
    __slots__ = ("__M", "__N", "__edges", "__size", "__matching")

    def __init__(self, M: int, N: int):
        """ 部集合の大きさが M, N である二部グラフを生成する.

        Args:
            M (int): 部集合 1 の大きさ
            N (int): 部集合 2 の大きさ
        """

        self.__M = M
        self.__N = N
        self.__edges: list[list[int]] = [[] for _ in range(M)]

    @property
    def M(self) -> int:
        """ 部集合 1 の大きさを返す.

        Returns:
            int: 部集合 1 の大きさ
        """

        return self.__M

    @property
    def N(self) -> int:
        """ 部集合 2 の大きさを返す.

        Returns:
            int: 部集合 2 の大きさ
        """

        return self.__N

    def add_edge(self, a: int, b: int):
        """ 辺 Aa と辺 Bb を結ぶ無向辺を追加する.

        Args:
            a (int): 部集合 1 側の頂点番号
            b (int): 部集合 2 側の頂点番号
        """

        assert 0 <= a < self.M
        assert 0 <= b < self.N

        self.__edges[a].append(b)

    def calculate(self, matching = False):
        """ 最大マッチングを計算する (結果は property メソッドで参照する).

        Args:
            matching (bool, optional): True にすると, 最大マッチングの一例も一緒に求める. Defaults to False.
        """

        edge = self.__edges
        pre = [-1] * self.M
        root = [-1]* self.M
        p = [-1] * self.M
        q = [-1] * self.N

        updated = True
        size = 0
        while updated:
            updated = False
            S = []
            index = 0

            for i in range(self.M):
                if p[i] == -1:
                    root[i] = i
                    S.append(i)

            while index < len(S):
                v = S[index]
                index += 1

                if p[root[v]] != -1:
                    continue

                for u in edge[v]:
                    if q[u] == -1:
                        while u != -1:
                            q[u] = v
                            p[v], u = u, p[v]
                            v = pre[v]
                        updated = True
                        size += 1
                        break

                    u = q[u]
                    if pre[u] != -1:
                        continue

                    pre[u] = v
                    root[u] = root[v]
                    S.append(u)

            if updated:
                pre = [-1] * self.M
                root = [-1] * self.M

        self.__size = size

        if not matching:
            self.__matching = None

        A = [-1] * self.M
        B = [-1] * self.N

        for i in range(self.M):
            if p[i] != -1:
                A[i] = p[i]
                B[p[i]] = i

        self.__matching = (A, B)

    @property
    def max_matching_size(self) -> int:
        """ calculate で求めた最大マッチングのサイズを求める.

        Returns:
            int: 最大マッチングのサイズ
        """

        return self.__size

    @property
    def max_matching(self) -> tuple[list[int], list[int]]:
        """ calculate で求めた最大マッチングの一例を求める.

        Returns:
            tuple[list[int], list[int]]: (A, B)
                A[i] が -1 ではないとき, 辺 (i, A[i]) がマッチングとして採用されている. A[i] = -1 のときはマッチングの頂点として採用されていない.
                B[j] が -1 ではないとき, 辺 (B[j], j) がマッチングとして採用されている. B[j] = -1 のときはマッチングの頂点として採用されていない.
        """

        return self.__matching
