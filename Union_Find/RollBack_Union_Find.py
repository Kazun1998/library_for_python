class RollBack_Union_Find():
    __slots__=["n", "parents", "__history", "__snap_time", "__group_count"]
    def __init__(self, N):
        """ 0,1,...,N-1 を要素として初期化する.

        N: 要素数
        """
        self.n=N
        self.parents=[-1]*N
        self.__history=[]
        self.__snap_time=[]
        self.__group_count=[]

    def find(self, x):
        """ 要素 x の属している族を調べる.

        x: 要素
        """

        while self.parents[x]>=0:
            x=self.parents[x]

        return x

    def union(self, x, y):
        """ 要素 x,y を同一視する.

        [input]
        x,y: 要素

        [output]
        元々が非連結 → True
        元々が連結 → False
        """
        x=self.find(x); y=self.find(y)

        par=self.parents

        self.__history.append((x, par[x]))
        self.__history.append((y, par[y]))

        if self.__group_count:
            count=self.__group_count[-1]
        else:
            count=self.n

        if x==y:
            self.__group_count.append(count)
            return False

        if par[x]>par[y]:
            x,y=y,x

        par[x]+=par[y]
        par[y]=x

        self.__group_count.append(count-1)

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

    def representative(self):
        """ 代表元のリスト
        """
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        """ 族の個数
        """

        if self.__group_count:
            return self.__group_count[-1]
        else:
            return self.n

    def get_time(self):
        return len(self.__history)>>1

    def undo(self):
        """ 1 回分の union を戻る.

        """

        if self.__history:
            y,b=self.__history.pop()
            self.parents[y]=b

            x,a=self.__history.pop()
            self.parents[x]=a

            self.__group_count.pop()

    def snapshot(self):
        """ スナップショットを撮る

        """

        self.__snap_time.append(self.get_time())

    def rollback(self, time=-1):
        """ 時刻 time 直前まで戻る.

        """

        if time==-1:
            if self.__snap_time:
                time=self.__snap_time[-1]
            else:
                return

        if time>self.get_time():
            return

        T=time<<1
        while T<len(self.__history):
            self.undo()

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

    def __str__(self):
        return str(self.all_group_members().values())[13:-2]

    def __repr__(self):
        return "RollBack Union Find: "+str(self)

    def __getitem__(self,index):
        return self.find(index)

    def __setitem__(self,x,y):
        self.union(x,y)
