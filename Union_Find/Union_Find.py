class Union_Find():
    __slots__=("n","parents","rank","edges","__group_number")
    def __init__(self,N):
        """ 0,1,...,N-1 を要素として初期化する.

        N: 要素数
        """
        self.n=N
        self.parents=[-1]*N
        self.rank=[0]*N
        self.edges=[0]*N
        self.__group_number=N

    def find(self, x):
        """ 要素 x の属している族を調べる.

        x: 要素
        """

        a=x
        while self.parents[a]>=0:
            a=self.parents[a]

        while self.parents[x]>=0:
            y=self.parents[x]
            self.parents[x]=a
            x=y

        return a

    def union(self, x, y):
        """ 要素 x,y を同一視する.

        [input]
        x,y: 要素

        [output]
        元々が非連結 → True
        元々が連結 → False
        """
        x=self.find(x)
        y=self.find(y)

        if x==y:
            self.edges[x]+=1
            return False

        if self.rank[x]<self.rank[y]:
            x,y=y,x

        self.__group_number-=1

        self.edges[x]+=self.edges[y]+1
        self.edges[y]=0

        self.parents[x]+=self.parents[y]
        self.parents[y]=x

        if self.rank[x]==self.rank[y]:
            self.rank[x]+=1
        return True

    def size(self, x):
        """ 要素 x の属している族の要素の数.

        x: 要素
        """
        return -self.parents[self.find(x)]

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

    def is_tree(self, x):
        """ 要素 x が属する族が木かどうかを判定する.

        x: 要素
        """
        return self.size(x)==self.edges[self.find(x)]+1

    def tree_count(self):
        """ 木になっている属の個数を求める.
        """

        return sum(self.is_tree(g) for g in self.representative())

    def representative(self):
        """ 代表元のリスト
        """
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        """ 族の個数
        """

        return self.__group_number

    def all_group_members(self):
        """ 全ての族の出力
        """
        X={r:[] for r in self.representative()}
        for k in range(self.n):
            X[self.find(k)].append(k)
        return X

    def group_list(self):
        """ 各要素が属している族のリストを出力する.

        """
        return [self.find(x) for x in range(self.n)]

    def refresh(self):
        for i in range(self.n):
            _=self.find(i)

    def __str__(self):
        return str(self.all_group_members().values())[13:-2]

    def __repr__(self):
        return "Union Find : "+str(self)

    def __getitem__(self,index):
        return self.find(index)

    def __setitem__(self,x,y):
        self.union(x,y)
