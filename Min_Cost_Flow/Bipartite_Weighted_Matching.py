from Min_Cost_Flow import *

class Bipartite_Weighted_Matching:
    inf=float("inf")
    def __init__(self, M: int, N: int):
        """ 位数が M (A 側) と N (B 側) の部集合からなる二部グラフの最大重み付きマッチングの場を作成する.

        Args:
            M (int): A 側の頂点数
            N (int): B 側の頂点数
        """

        self.M=M; self.N=N
        self.__max_weight=-Bipartite_Weighted_Matching.inf
        self.edge: list[list[tuple[int, int]]] =[ [] for _ in range(M)]

    def add_vertex(self, side: int, k: int = 1) -> list[int]:
        """ side 側に k 個の頂点を追加する.

        Args:
            side (int): 0 だと A 側, 1 だと B 側
            k (int, optional): 追加する頂点数. Defaults to 1.

        Returns:
            list[int]: 追加した頂点の追加した側での頂点番号
        """

        if side==0:
            self.M+=k
            self.edge.extend([[] for _ in range(k)])
            return list(range(self.M-k, self.M))
        else:
            self.N+=k
            return list(range(self.N-k, self.N))

    def add_edge(self, a: int, b: int, w: int):
        """ 重さ w の辺 Aa Bb を追加する.

        Args:
            a (int): A 側の頂点番号
            b (int): B 側の頂点番号
            w (int): 辺の重み
        """

        assert 0<=a<self.M and 0<=b<self.N

        self.__max_weight=max(self.__max_weight, w)
        self.edge[a].append((b,w))

    def matching(self, mode=False):
        """ 普通の最大重みマッチングを求める.

        """

        if mode==0:
            return self.matching_vertex_duplicate([1]*self.M, [1]*self.N)
        else:
            weight,(X,Y)=self.matching_vertex_duplicate([1]*self.M, [1]*self.N,1)
            X=[x[0] if x else -1 for x in X]
            Y=[y[0] if y else -1 for y in Y]
            return weight,(X,Y)

    def matching_specify_size(self, size, default=None):
        return self.matching_vertex_duplicate([1]*self.M, [1]*self.N, size, default)

    def matching_each_size(self):
        """ 普通の最大重みマッチングを求める.

        """

        M=self.M; N=self.N
        G=Max_Gain_Flow(M+N+2)
        source=M+N; target=M+N+1

        for a in range(M):
            G.add_arc(source, a, 1, 0)

        for b in range(N):
            G.add_arc(b+M, target, 1, 0)

        for a in range(M):
            for b,w in self.edge[a]:
                G.add_arc(a, b+M, 1, w)

        return G.slope(source, target, min(M,N))

    def matching_vertex_duplicate(self, k, l, mode=0):
        """ 頂点 Aa の選択を k[a] 回, 頂点 Bb の選択を l[b] 回まで許す最大マッチングを選ぶ.

        """

        M=self.M; N=self.N
        G=Max_Gain_Flow(M+N+2)
        source=M+N; target=M+N+1

        flow=min(sum(k), sum(l))

        G.add_arc(source, target, flow, 0)
        for a in range(M):
            G.add_arc(source, a, k[a], 0)

        for b in range(N):
            G.add_arc(b+M, target, l[b], 0)

        for a in range(M):
            for b,w in self.edge[a]:
                G.add_arc(a, b+M, 1, w)

        gain=G.flow(source, target, flow)

        if not mode:
            return gain

        X=[[] for _ in range(M)]; Y=[[] for _ in range(N)]
        for i in range(G.arc_count):
            arc=G.get_arc(i)
            if arc.source!=source and arc.target!=target:
                if arc.cap==0:
                    a=arc.source; b=arc.target-M
                    X[a].append(b)
                    Y[b].append(a)
        return gain,(X,Y)

    def matching_vertex_duplicate_specify_size(self, k, l, size, default=None):
        try:
            return self.matching_vertex_duplicate_each_size(k,l)[size]
        except:
            return default

    def matching_vertex_duplicate_each_size(self, k, l):
        """ 頂点 Aa の選択を k[a] 回, 頂点 Bb の選択を l[b] 回まで許す最大マッチングを選ぶ.

        """

        M=self.M; N=self.N
        G=Max_Gain_Flow(M+N+2)
        source=M+N; target=M+N+1

        flow=min(sum(k), sum(l))

        for a in range(M):
            G.add_arc(source, a, k[a], 0)

        for b in range(N):
            G.add_arc(b+M, target, l[b], 0)

        for a in range(M):
            for b,w in self.edge[a]:
                G.add_arc(a, b+M, 1, w)

        return G.slope(source, target)
