class Potentilized_Union_Find():
    def __init__(self, N, op, zero, neg):
        """ 0,1,...,N-1 を要素として初期化する.

        N: 要素数
        """
        self.n=N
        self.parents=[-1]*N
        self.rank=[0]*N
        self.edges=[0]*N
        self.pot=[zero]*N
        self.valid=[True]*N
        self.__group_number=N

        self.op=op
        self.diff=lambda u,v:self.op(u, self.neg(v)) # diff(u,v)=U(u)-U(v)
        self.zero=zero
        self.neg=neg


    def find(self, x):
        """ 要素 x の属している族を調べる.

        x: 要素
        """


        if self.parents[x]<0:
            return x

        par=self.parents; pot=self.pot; op=self.op

        r=x
        data=[]
        while par[r]>=0:
            data.append(r)
            r=par[r]

        for x in data[::-1]:
            pot[x]=self.op(pot[x], pot[par[x]])
            par[x]=r

        return r

    def union(self, x, y, u):
        """ 要素 x,y を同一視し, U(y)-U(x)=u という情報を加える.

        x,y: 要素
        """

        a=self.find(x); b=self.find(y)
        u=self.op(u, self.diff(self.pot[x],self.pot[y]))
        x=a; y=b

        if x==y:
            self.valid[x]&=self.diff(self.pot[y],self.pot[x])==u
            self.edges[x]+=1
            return

        if self.rank[x]<self.rank[y]:
            x,y=y,x
            u=self.neg(u)
        elif self.rank[x]==self.rank[y]:
            self.rank[x]+=1

        self.parents[x]+=self.parents[y]
        self.parents[y]=x

        self.edges[x]+=self.edges[y]+1
        self.edges[y]=0

        self.valid[x]&=self.valid[y]

        self.pot[y]=u

        self.__group_number-=1

        return

    def size(self, x):
        """ 要素 x の属している族の要素の数.

        x: 要素
        """
        return -self.parents[self.find(x)]

    def potential_energy(self, x, y):
        """ x を基準にした y のポテンシャルエネルギー"""

        if self.same(x,y) and self.is_valid(x):
            return self.diff(self.pot[y], self.pot[x])
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

    def is_valid(self, x):
        """ x が属している族のポテンシャルが妥当かどうかを判定する. """

        return self.valid[self.find(x)]

    def is_well_defined(self):
        """ この系全体のポテンシャルが妥当かどうかを判定する. """

        return all(self.is_valid(x) for x in range(self.n))

    def is_tree(self, x):
        """ 要素 x が属する族が森かどうかを判定する.

        x: 要素
        """
        return self.size(x)==self.edges[self.find(x)]+1

    def tree_count(self):
        """ 森になっている属の個数を求める.
        """

        return sum(self.is_tree(g) for g in self.representative())

    def representative(self):
        """ 代表元の名前のリスト
        """
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        """ 族の個数
        """
        return self.__group_number

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
