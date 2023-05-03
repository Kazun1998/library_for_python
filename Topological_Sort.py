class Topological_Sort:
    __slots__=("N","__arc","__rev", "__reflexive")
    def __init__(self, N: int, reflexive=False):
        """ N 頂点からなる空グラフを生成する.

        N: 頂点数
        reflexive: 自己ループの追加を認めるか? (False の場合は自己ループは自動的に取り除かれる.)
        """

        self.N=N
        self.__arc=[[] for _ in  range(N)]
        self.__rev=[[] for _ in range(N)]
        self.__reflexive=reflexive

    def add_arc(self, source: int, target: int):
        """ 有向辺 source -> target を追加する.

        source: 始点
        target: 終点
        """

        if source==target and (not self.__reflexive):
            return

        self.__arc[source].append(target)
        self.__rev[target].append(source)

    def add_vertex(self):
        res=self.N
        self.N+=1
        self.__arc.append([])
        self.__rev.append([])
        return res

    def add_arc_multiple(self, sources, targets):
        v=self.add_vertex()
        for u in sources:
            self.add_arc(u,v)

        for w in targets:
            self.add_arc(v,w)

        return v

    def sort(self):
        """ トポロジカルソートを求める

        存在するならばトポロジカルソートをしたリスト, 存在しないならば None
        """

        in_deg=[len(self.__rev[x]) for x in range(self.N)]
        Q=[x for x in range(self.N) if in_deg[x]==0]

        S=[]
        while Q:
            u=Q.pop()
            S.append(u)

            for v in self.__arc[u]:
                in_deg[v]-=1
                if in_deg[v]==0:
                    Q.append(v)

        return S if len(S)==self.N else None

    def is_DAG(self):
        """ DAG がどうかを判定する

        DAG ならば True, 非 DAG ならば False
        """

        in_deg=[len(self.__rev[x]) for x in range(self.N)]
        Q=[x for x in range(self.N) if in_deg[x]==0]

        K=0
        while Q:
            u=Q.pop()
            K+=1

            for v in self.__arc[u]:
                in_deg[v]-=1
                if in_deg[v]==0:
                    Q.append(v)

        return K==self.N
