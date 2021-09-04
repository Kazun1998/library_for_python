class Potentilized_Union_Find():
    __slots__=["n","parents","rank","edges","pot"]
    def __init__(self,N):
        """ 0,1,...,N-1 を要素として初期化する.

        N: 要素数
        """
        self.n=N
        self.parents=[-1]*N
        self.rank=[0]*N
        self.edges=[0]*N
        self.pot=[0]*N

    def find(self, x):
        """ 要素 x の属している族を調べる.

        x: 要素
        """
        V=[]
        while self.parents[x]>=0:
            V.append(x)
            x=self.parents[x]

        for v in V:
            self.pot[v]+=self.pot[self.parents[v]]
            self.parents[v]=x
        return x

    def union(self, x, y, u):
        """ 要素 x,y を同一視し, U(x)-U(y)=u という情報を加える.

        x,y: 要素
        """

        u+=self.pot[x]-self.pot[y]
        x=self.find(x)
        y=self.find(y)

        if x==y:
            self.edges[x]+=1
            assert self.potential(x,y)==u
            return

        if self.rank[x]>self.rank[y]:
            x,y,u=y,x,-u

        self.edges[x]+=self.edges[y]+1
        self.edges[y]=0

        self.parents[x]+=self.parents[y]
        self.parents[y]=x

        if self.rank[x]==self.rank[y]:
            self.rank[x]+=1
        self.pot[x]=u

    def size(self, x):
        """ 要素 x の属している族の要素の数.

        x: 要素
        """
        return -self.parents[self.find(x)]

    def potential(self, x, y):
        """ y を基準にした x のポテンシャル"""

        if self.same(x,y):
            return self.pot[x]-self.pot[y]
        else:
            return None

    def same(self, x, y):
        """ 要素 x,y は同一視されているか?

        x,y: 要素
        """
        return self.find(x) == self.find(y)

    def members(self, x):
        """ 要素 x が属している族の要素.
        ※族の要素の個数が欲しいときは size を使うこと!!

        x: 要素
        """
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def edge_count(self, x):
        """ 要素 x が属する族の辺の本数を求める.

        x: 要素
        """
        return self.edges[self.find(x)]

    def is_forest(self, x):
        """ 要素 x が属する族が森かどうかを判定する.

        x: 要素
        """
        return self.size(x)==self.edges[self.find(x)]+1

    def forest_count(self):
        """ 森になっている属の個数を求める.
        """

        X=0
        for g in self.roots():
            if self.is_forest(g):
                X+=1
        return X

    def roots(self):
        """ 族の名前のリスト
        """
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        """ 族の個数
        """
        return len(self.roots())

    def all_group_members(self):
        """ 全ての族の出力
        """
        X={r:[] for r in self.roots()}
        for k in range(self.n):
            X[self.find(k)].append(k)
        return X

    def refresh(self):
        for i in range(self.n):
            _=self.find(i)

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

    __repr__=__str__
