class Dynamic_Union_Find():
    def __init__(self):
        """初期化する.

        N:要素数
        """
        self.parent={}
        self.SIZE={}
        self.rank={}

    def vertex_exist(self,x):
        return x in self.parent

    def vertex_add(self,x):
        if x in self.parent:
            return
        self.parent[x]=x
        self.SIZE[x]=1
        self.rank[x]=1
        return

    def find(self, x):
        """要素xの属している族を調べる.

        x:要素
        """

        self.vertex_add(x)

        V=[]
        while self.parent[x]!=x:
            V.append(x)
            x=self.parent[x]

        self.parent[x]=x
        for v in V:
            self.parent[v]=x
        return x

    def union(self, x, y):
        """要素x,yを同一視する.

        x,y:要素
        """
        x=self.find(x)
        y=self.find(y)

        if x==y:
            return

        if self.rank[x]<self.rank[y]:
            x,y=y,x

        self.SIZE[x]+=self.SIZE[y]
        self.parent[y]=x

        if self.rank[x]==self.rank[y]:
            self.rank[x]+=1

    def size(self, x):
        """要素xの属している要素の数.

        x:要素
        """
        return self.SIZE[self.find(x)]

    def same(self, x, y):
        """要素x,yは同一視されているか?

        x,y:要素
        """
        return self.find(x) == self.find(y)

    def members(self, x):
        """要素xが属している族の要素.
        ※族の要素の個数が欲しいときはsizeを使うこと!!

        x:要素
        """
        root = self.find(x)
        return [v for v in self.parent if self.find(v)==root]

    def roots(self):
        """族の名前のリスト
        """
        return [v for v in self.parent if self.find(v)==v]

    def group_count(self):
        """族の個数
        """
        x=0
        for v in self.parent:
            if self.find(v)==v:
                x+=1
        return x

    def all_group_members(self):
        """全ての族の出力
        """
        X={r:[] for r in self.roots()}
        for k in self.parent:
            X[self.find(k)].append(k)
        return X

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

    def __repr__(self):
        return self.__str__()
