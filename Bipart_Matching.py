# 参考 URL
# https://snuke.hatenablog.com/entry/2019/05/07/013609

class Bipartite_Matching:
    def __init__(self,M,N):
        """ サイズが M,N からなる二部空グラフを作成する.
        """
        self.M=M; self.N=N
        self.edge=[[] for _ in range(M)]

    def add_edge(self, a, b):
        """ 辺 Aa Bb を加える.

        """
        assert 0<=a<self.M and 0<=b<self.N
        self.edge[a].append(b)

    def max_matching(self, mode):
        M=self.M; N=self.N; edge=self.edge
        pre=[-1]*M; root=[-1]*M
        p=[-1]*M; q=[-1]*N

        upd=True
        size=0
        while upd:
            upd=False
            S=[]
            Index=0

            for i in range(M):
                if p[i]==-1:
                    root[i]=i
                    S.append(i)

            while Index<len(S):
                v=S[Index]
                Index+=1

                if p[root[v]]!=-1:
                    continue

                for u in edge[v]:
                    if q[u]==-1:
                        while u!=-1:
                            q[u]=v
                            p[v],u=u,p[v]
                            v=pre[v]
                        upd=True
                        size+=1
                        break

                    u=q[u]
                    if pre[u]!=-1:
                        continue

                    pre[u]=v
                    root[u]=root[v]
                    S.append(u)

            if upd:
                pre=[-1]*M
                root=[-1]*M

        if mode==0:
            return size
        else:
            A=[-1]*M; B=[-1]*N
            for i in range(M):
                if p[i]!=-1:
                    A[i]=p[i]
                    B[p[i]]=i
            return size,(A,B)
