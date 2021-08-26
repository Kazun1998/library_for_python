class Topological_Sort:
    def __init__(self, N: int):
        """ N 頂点からなる空グラフを用意する.

        N: int
        """
        self.N=N
        self.arc=[[] for _ in  range(N)]
        self.rev=[[] for _ in range(N)]

    def add_arc(self, source: int, target: int):
        """ 有向辺 source → taeget を追加する.

        """
        self.arc[source].append(target)
        self.rev[target].append(source)

    def sort(self):
        """ トポロジカルソートを求める.

        [Ouput]
        存在する → トポロジカルソート
        存在しない → None
        """

        in_deg=[len(self.rev[x]) for x in range(self.N)]
        Q=[x for x in range(self.N) if in_deg[x]==0]

        S=[]
        while Q:
            u=Q.pop()
            S.append(u)

            for v in self.arc[u]:
                in_deg[v]-=1
                if in_deg[v]==0:
                    Q.append(v)

        return S if len(S)==self.N else None

    def is_DAG(self):
        """ DAG かどうかを判定する.
        """
        return self.sort()!=None
