class Functional_Graph:
    def __init__(self, N, F=[]):
        assert (not F) or (len(F)==N)
        self.__N=N

        if F:
            self.__F=F
        else:
            self.__F=list(range(N))

        self.__build()

    def __len__(self):
        return self.__N

    def __getitem__(self, index):
        assert 0<=index<self.__N
        return self.__F[index]

    def __setitem(self, index, value):
        assert 0<=index<self.__N
        self.__F[index]=value

    def __build(self):
        from collections import deque

        N=self.__N
        F=self.__F
        F_inv=[[] for _ in range(len(self))]

        for i in range(self.__N):
            F_inv[F[i]].append(i)

        self.__F_inv=F_inv

        # サイクル検出パート
        in_deg=[len(f_inv) for f_inv in F_inv]

        C=[1]*N
        Q=deque([x for x in range(N) if in_deg[x]==0])
        while Q:
            x=Q.pop()
            C[x]=0
            in_deg[F[x]]-=1
            if in_deg[F[x]]==0:
                Q.append(F[x])

        cycle_vertex=[]
        cycle_id=[-1]*N
        cycle_vertex_id=[-1]*N
        for x in range(N):
            if C[x]:
                c=[x]
                C[x]=0
                y=F[x]
                while y!=x:
                    c.append(y)
                    C[y]=0
                    y=F[y]
                cycle_vertex.append(c)

                i=len(cycle_vertex)-1
                for j in range(len(c)):
                    y=c[j]
                    cycle_id[y]=i
                    cycle_vertex_id[y]=j

        self.__cycle_vertex=cycle_vertex
        self.__cycle_id=cycle_id
        self.__cycle_vertex_id=cycle_vertex_id

        # ブランチパート
        tree_id=[-1]*N # 頂点 i が属している木の id
        tree_vertex_id=[-1]*N # 頂点 i が属している木における頂点の番号
        tree_vertex=[] # tree_vertex[tree_id[v]][tree_vertex_id[v]]=v
        tree_depth=[0]*N # 頂点 v の深さ
        tree_doubling=[]

        i=j=0
        for x in range(N):
            if cycle_id[x]!=-1:
                tree_vertex.append([])

                j=0
                tree_id[x]=i; tree_vertex_id[x]=j

                Q=deque([x])
                tree_vertex[-1].append(x)
                depth_max=0
                while Q:
                    x=Q.popleft()
                    for y in F_inv[x]:
                        if cycle_id[y]==-1:
                            j+=1
                            tree_id[y]=i; tree_vertex_id[y]=j
                            tree_depth[y]=tree_depth[x]+1
                            depth_max=max(depth_max, tree_depth[y])
                            Q.append(y)
                            tree_vertex[-1].append(y)
                i+=1

                m=j+1
                D=[[-1]*m for _ in range(max(1,depth_max.bit_length()))]
                for j in range(m):
                    if j==0:
                        D[0][j]=0
                    else:
                        D[0][j]=tree_vertex_id[F[tree_vertex[-1][j]]]

                for b in range(1, max(1,depth_max.bit_length())):
                    for j in range(m):
                        D[b][j]=D[b-1][D[b-1][j]]
                tree_doubling.append(D)

        self.__tree_id=tree_id
        self.__tree_vertex_id=tree_vertex_id
        self.__tree_vertex=tree_vertex
        self.__tree_depth=tree_depth
        self.__tree_doubling=tree_doubling

    def __upper(self, x, k):
        i=self.__tree_id[x]
        j=self.__tree_vertex_id[x]

        doubling=self.__tree_doubling[i]
        b=0
        while k:
            if k&1:
                j=doubling[b][j]
            k>>=1
            b+=1
        return self.__tree_vertex[i][j]

    def on_cycle(self, x):
        return self.__cycle_id[x]>=0

    def calculate(self, x, k):
        """ f^k(x) を求める.

        """

        if k<self.__tree_depth[x]:
            return self.__upper(x, k)
        else:
            k-=self.__tree_depth[x]
            x=self.__tree_vertex[self.__tree_id[x]][0]

            i=self.__cycle_id[x]
            j=self.__cycle_vertex_id[x]
            m=len(self.__cycle_vertex[i])
            return self.__cycle_vertex[i][(j+k)%m]

    def calculate_list(self, k):
        """ f^k(x) (x=0,1, ..., N-1) を求める.
        """
        return [self.calculate(x,k) for x in range(self.__N)]

    def get_cycle(self):
        return self.__cycle_vertex

    def get_inverse(self):
        return self.__F_inv
