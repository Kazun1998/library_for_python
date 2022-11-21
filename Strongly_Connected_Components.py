"""Thanks to toyuzuko
https://atcoder.jp/contests/typical90/submissions/21969418
"""

class Strongly_Connected_Components:
    def __init__(self,N):
        self.N=N
        self.arc=[[] for _ in range(N)]
        self.rev=[[] for _ in range(N)]

    def add_arc(self,source,target):
        self.arc[source].append(target)
        self.rev[target].append(source)

    def decomposition(self,Mode=0):
        """有向グラフを強連結成分に分解

        Mode:
        0(Defalt)---各強連結成分の頂点のリスト
        1        ---各頂点が属している強連結成分の番号
        2        ---0,1の両方

        ※0 or 2で帰ってくるリストは各強連結成分に関してトポロジカルソートである.
        """

        G=[0]*self.N
        D=[0]*self.N
        O=[]

        for v in range(self.N):
            if G[v]: continue
            S=[~v,v]

            while S:
                v=S.pop()
                if v>=0:
                    if G[v]: continue
                    G[v]=-1
                    for u in self.arc[v]:
                        if G[u]: continue
                        S.append(~u)
                        S.append(u)
                else:
                    if D[~v]: continue
                    D[~v]=1
                    O.append(~v)

        K=0
        for v in O[::-1]:
            if G[v]!=-1: continue

            S=[v]
            G[v]=K

            while S:
                w=S.pop()
                for u in self.rev[w]:
                    if G[u]!=-1: continue
                    G[u]=K
                    S.append(u)
            K+=1

        if Mode==0 or Mode==2:
            R=[[] for _ in range(K)]
            for i in range(self.N):
                R[G[i]].append(i)

        if Mode==0:
            return R
        elif Mode==1:
            return G
        else:
            return R,G
