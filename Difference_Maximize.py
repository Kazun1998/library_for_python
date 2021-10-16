"""
Note
通称 "牛ゲー" と呼ばれる問題を解く. この問題は M 個の条件
    x[i[m]]-x[j[m]]<=c[m]
において, x[p]-x[q] を最大化する. なお, これは x[q]=0 という追加制約化での x[p] の最大化になる.

※ 最短路問題に帰着
"""

class Difference_Maximize:
    def __init__(self,N):
        self.N=N
        self.__arc=[[] for _ in range(N)]
        self.Neg_edge=False
        self.__cost=0
        self.__taught_DAG=None

    def cost(self):
        return self.__cost

    def teaching_DAG(self,mode):
        """ 与えられる状況に対応する有向グラフが DAG 確定かどうかを教える.

        """
        self.__is_DAG=mode

    def is_DAG(self):
        arc=self.__arc

        in_deg=[0]*self.N
        for u in range(self.N):
            for v,_ in arc[u]:
                in_deg[v]+=1

        Q=[x for x in range(self.N) if in_deg[x]==0]

        S=[]
        while Q:
            u=Q.pop()
            S.append(u)

            for v,_ in arc[u]:
                in_deg[v]-=1
                if in_deg[v]==0:
                    Q.append(v)

        return S if len(S)==self.N else None

    def add_constraint(self,i,j,c):
        """ x[i]-x[j] <=c という条件を付け加える.

        """

        assert 0<=i<self.N
        assert 0<=j<self.N

        if c<0:
            self.Neg_edge=True

        self.__arc[j].append((i,c))
        self.__cost+=1

    def solve(self, base_index=0, base_value=0):
        """ x[base]=base_value を基準にして解を求める.

        ※実行可能解が存在しない場合, 返り値はNoneになる.
        """
        inf=float("inf")
        N=self.N
        arc=self.__arc

        if (self.__taught_DAG==None) or (self.__taught_DAG==True):
            K=self.is_DAG()
        else:
            K=None

        if K!=None:
            X=[inf]*N; X[base_index]=base_value
            for p in K:
                for q,c in arc[p]:
                    if X[q]>X[p]+c:
                        X[q]=X[p]+c
            return X
        elif self.Neg_edge:
            X=[inf]*N; X[base_index]=base_value

            for _ in range(N):
                update=0
                for p in range(N):
                    for q,c in arc[p]:
                        if X[q]>X[p]+c:
                            X[q]=X[p]+c
                            update=1

                    if not update:
                        return X
            return None
        else:
            from heapq import heapify, heappush, heappop

            arc=self.__arc
            X=[inf]*self.N

            X[base_index]=base_value
            Q=[(base_value, base_index)]
            while Q:
                x,i=heappop(Q)

                if x>X[i]:
                    continue

                for j,c in arc[i]:
                    if X[i]+c<X[j]:
                        X[j]=X[i]+c
                        heappush(Q,(X[j],j))
            return X

    def solve_add_by_Warshall_Floyd(self):
        """ 全ての p,q に対する x[q]-x[p] の最大化の結果を Warshall Floyd 法で求める.

        [Output]
        解が存在する場合
        2次元リスト X が返される. max x[q]-x[p] の解は x[p]=0 を基準にして X[p][q] に記録される.

        解が存在しない場合
        None
        """

        inf=float("inf")
        arc=self.__arc
        N=self.N

        X=[[inf]*N for _ in range(N)]
        for p in range(N):
            x=X[p]
            x[p]=0
            for q,cond in arc[p]:
                if x[q]>cond:
                    x[q]=cond

        for k in range(N):
            xk=X[k]
            for p in range(N):
                xp=X[p]
                for q in range(N):
                    if xp[q]>xp[k]+xk[q]:
                        xp[q]=xp[k]+xk[q]

        # 解答の存在 Check
        for p in range(N):
            if X[p][p]<0: return None

        return X
