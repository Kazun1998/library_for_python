class Strongly_Connected_Components:
    def __init__(self, N):
        """ N 頂点の有向グラフを生成する. """
        self.N=N
        self.arc=[[] for _ in range(N)]
        self.rev=[[] for _ in range(N)]

    def add_vertex(self):
        """ 頂点を追加する.

        """

        self.N+=1
        self.arc.append([])
        self.rev.append([])
        return self.N-1

    def add_vertices(self, k=1):
        """ 頂点を k 個追加する.

        k: int
        """

        self.N+=k
        self.arc.extend([[] for _ in range(k)])
        self.rev.extend([[] for _ in range(k)])
        return list(range(self.N-k, self.N))

    def add_arc(self, source, target):
        """ source から target へ結ぶ有向辺を追加する.

        """

        self.arc[source].append(target)
        self.rev[target].append(source)

    def decomposition(self, mode=0):
        """有向グラフを強連結成分に分解

        Mode:
        0 (defalt) ---各強連結成分の頂点のリスト
        1        ---各頂点が属している強連結成分の番号
        2        ---0, 1 の両方

        ※ 0 or 2で帰ってくるリストは各強連結成分に関してトポロジカルソートである.
        """

        G=[0]*self.N
        D=[0]*self.N
        O=[]

        for v in range(self.N):
            if G[v]:
                continue

            S=[~v, v]

            while S:
                v=S.pop()
                if v>=0:
                    if G[v]==-1:
                        continue

                    G[v]=-1
                    for w in self.arc[v]:
                        if not G[w]:
                            S.append(~w)
                            S.append(w)
                else:
                    v=~v
                    if not D[v]:
                        D[v]=1
                        O.append(v)

        K=0
        for v in reversed(O):
            if G[v]!=-1:
                continue

            S=[v]
            G[v]=K

            while S:
                w=S.pop()
                for u in self.rev[w]:
                    if G[u]==-1:
                        G[u]=K
                        S.append(u)
            K+=1

        if mode==0 or mode==2:
            R=[[] for _ in range(K)]
            for i in range(self.N):
                R[G[i]].append(i)

        if mode==0:
            return R
        elif mode==1:
            return G
        else:
            return R,G
