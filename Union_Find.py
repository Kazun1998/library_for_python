class Union_Find():
    __slots__=["n","parents","rank","edges"]
    def __init__(self,N):
        """ 0,1,...,N-1 を要素として初期化する.

        N: 要素数
        """
        self.n=N
        self.parents=[-1]*N
        self.rank=[0]*N
        self.edges=[0]*N

    def find(self, x):
        """ 要素 x の属している族を調べる.

        x: 要素
        """
        V=[]
        while self.parents[x]>=0:
            V.append(x)
            x=self.parents[x]

        for v in V:
            self.parents[v]=x
        return x

    def union(self, x, y):
        """ 要素 x,y を同一視する.

        x,y: 要素
        """
        x=self.find(x)
        y=self.find(y)

        if x==y:
            self.edges[x]+=1
            return

        if self.rank[x]<self.rank[y]:
            x,y=y,x

        self.edges[x]+=self.edges[y]+1
        self.edges[y]=0

        self.parents[x]+=self.parents[y]
        self.parents[y]=x

        if self.rank[x]==self.rank[y]:
            self.rank[x]+=1

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

    def __repr__(self):
        return self.__str__()

    def __getitem__(self,index):
        return self.find(index)

    def __setitem__(self,x,y):
        self.union(x,y)
#=================================================
class Coloring_Union_Find():
    __slots__=["n","parents","rank","data","merge"]
    def __init__(self,N,merge,e):
        """ 0,1,...,N-1 を要素として初期化する.

        N: 要素数
        merge: 合成の方法
        e: 最初の値
        """
        self.n=N
        self.parents=[-1]*N
        self.data=[e]*N
        self.rank=[0]*N
        self.merge=merge

    def find(self, x):
        """ 要素 x の属している族を調べる.

        x: 要素
        """
        V=[]
        while self.parents[x]>=0:
            V.append(x)
            x=self.parents[x]

        for v in V:
            self.parents[v]=x
        return x

    def union(self, x, y):
        """ 要素 x,y を同一視し, それぞれが持っている族の色を統合する.

        x,y: 要素
        """
        x=self.find(x)
        y=self.find(y)

        if x==y:
            return

        self.data[x]=self.data[y]=self.merge(self.data[x],self.data[y])

        if self.rank[x]<self.rank[y]:
            x,y=y,x

        self.parents[x]+=self.parents[y]
        self.parents[y]=x

        if self.rank[x]==self.rank[y]:
            self.rank[x]+=1

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

    def set(self,x,c):
        """ 要素 x の属する族の色を c に変更する.

        x: 要素
        c: 色
        """
        self.data[self.find(x)]=c

    def look(self,x):
        """ 要素 x の属する成分の色

        x: 要素
        """
        return self.data[self.find(x)]

    def members(self, x):
        """ 要素 x が属している族の要素.
        ※族の要素の個数が欲しいときは size を使うこと!!

        x: 要素
        """
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        """ 族の名前のリスト
        """
        return [i for i,x in enumerate(self.parents) if x < 0]

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

    def color_list(self):
        return [self.look(x) for x in range(self.n)]

    def color_map(self):
        return {x:self.look(x) for x in self.roots()}

    def __str__(self):
        return '\n'.join('{} [color:{}]: {}'.format(r,self.look(r),self.members(r)) for r in self.roots())

    def __repr__(self):
        return self.__str__()

    def __getitem__(self,index):
        return self.data[self.find(index)]

    def __setitem__(self,index,value):
        self.data[self.find(index)]=value
#=================================================
class Generalized_Union_Find():
    def __init__(self):
        """初期化する.

        N:要素数
        f:2変数関数の合成
        e:最初の値
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
            self.parent[x]=x
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
