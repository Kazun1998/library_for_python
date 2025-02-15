class Union_Find():
    __slots__ = ("n", "parents", "rank", "edges", "__group_number")

    def __init__(self, N: int) -> None:
        """ 0, 1, ..., (N - 1) を要素に持つ Union Find を生成する.

        Args:
            N (int): 要素数
        """

        self.n=N
        self.parents=[-1]*N
        self.rank=[0]*N
        self.edges=[0]*N
        self.__group_number=N

    def find(self, x: int) -> int:
        """ 要素 x が属している族を調べる

        Args:
            x (int): 要素

        Returns:
            int: x が属している族
        """

        a=x
        while self.parents[a]>=0:
            a=self.parents[a]

        while self.parents[x]>=0:
            y=self.parents[x]
            self.parents[x]=a
            x=y

        return a

    def union(self, x: int, y: int, force : bool = False) -> bool:
        """ 要素 x と 要素 y を同一視する.

        Args:
            x (int): 要素 x
            y (int): 要素 y
            force (bool, optional): True の場合, 必ず x が代表元になるようにマージする. Defaults to False.

        Returns:
            bool: 元々非連結ならば True, 元々連結ならば False.
        """
        x=self.find(x)
        y=self.find(y)

        if x==y:
            self.edges[x]+=1
            return False

        if (not force) and (self.rank[x] < self.rank[y]):
            x,y=y,x

        self.__group_number-=1

        self.edges[x]+=self.edges[y]+1
        self.edges[y]=0

        self.parents[x]+=self.parents[y]
        self.parents[y]=x

        if self.rank[x]==self.rank[y]:
            self.rank[x]+=1
        return True

    def size(self, x: int) -> int:
        """ 要素 x が属している族のサイズを求める

        Args:
            x (int): 要素

        Returns:
            int: 要素 x が属している族のサイズ
        """
        return -self.parents[self.find(x)]

    def same(self, x: int, y: int) -> int:
        """ 要素 x, y は同一視されているか?

        Args:
            x (int): 要素
            y (int): 要素

        Returns:
            int: x, y が同一視されていれば True, そうでなければ False
        """
        return self.find(x) == self.find(y)

    def members(self, x: int) -> list[int]:
        """ 要素 x と同一視されている要素のリスト

        Args:
            x (int): 要素

        Returns:
            list[int]: 要素 x と同一視されている要素のリスト
        """

        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def edge_count(self, x: int) -> int:
        """ 要素 x が属している族における辺の数を求める.

        Args:
            x (int): 要素

        Returns:
            int: 要素 x が属している族における辺の数を求める
        """

        return self.edges[self.find(x)]

    def is_tree(self, x: int) -> bool:
        """ 要素 x が属する族が木かどうかを判定する.

        Args:
            x (int): 要素

        Returns:
            bool: 木ならば True, そうでなければ False
        """

        return self.size(x)==self.edges[self.find(x)]+1

    def tree_count(self) -> int:
        """ 木になっている族の数を計上する

        Returns:
            int: 木になっている族の数
        """

        return sum(self.is_tree(g) for g in self.representative())

    def representative(self) -> list[int]:
        """ 代表元のリスト

        Returns:
            list[int]: 代表元のリスト
        """
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self) -> int:
        """ 族の個数

        Returns:
            int: 族の個数
        """

        return self.__group_number

    def all_group_members(self) -> dict[int, list[int]]:
        """ 全ての族の出力
        """
        X={r:[] for r in self.representative()}
        for k in range(self.n):
            X[self.find(k)].append(k)
        return X

    def group_list(self) -> list[int]:
        """ 各要素が属している族のリストを出力する.

        """
        return [self.find(x) for x in range(self.n)]

    def refresh(self) -> None:
        for i in range(self.n):
            _=self.find(i)

    def __str__(self) -> str:
        return str(list(self.all_group_members().values()))[1: -1]

    def __repr__(self) -> str:
        return f"Union Find : {str(self)}"

    def __getitem__(self, index: int) -> int:
        return self.find(index)

    def __setitem__(self, x: int, y: int) -> None:
        self.union(x, y)
