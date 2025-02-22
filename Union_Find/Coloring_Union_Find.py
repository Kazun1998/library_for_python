from typing import TypeVar, Callable, Generic

M = TypeVar('M')
class Coloring_Union_Find(Generic[M]):
    __slots__=("n", "parents", "rank", "data", "merge", "__group_number")

    def __init__(self, N: int, merge: Callable[[M, M], M], unit: M):
        """ N 要素で初期状態を unit として初期化する.

        Args:
            N (int): 要素数
            merge (Callable[[M, M], M]): Monoid M の合成の方法
            unit (M): 基底状態
        """

        self.n=N
        self.parents=[-1]*N
        self.data=[unit]*N
        self.rank=[0]*N
        self.merge=merge
        self.__group_number=N

    def find(self, x: int) -> int:
        """ 要素 x の属している族を調べる.

        Args:
            x (int): 要素

        Returns:
            int: 要素 x の属している族の代表元
        """
        V=[]
        while self.parents[x]>=0:
            V.append(x)
            x=self.parents[x]

        for v in V:
            self.parents[v]=x
        return x

    def union(self, x: int, y: int) -> None:
        """ 要素 x,y を同一視し, それぞれが持っている族の色を統合する.

        Args:
            x (int): 要素 1
            y (int): 要素 2
        """

        x=self.find(x)
        y=self.find(y)

        if x==y:
            return

        self.__group_number-=1

        self.data[x]=self.data[y]=self.merge(self.data[x], self.data[y])

        if self.rank[x]<self.rank[y]:
            x,y=y,x

        self.parents[x]+=self.parents[y]
        self.parents[y]=x

        if self.rank[x]==self.rank[y]:
            self.rank[x]+=1

    def size(self, x: int) -> int:
        """ 要素 x の属している族の要素の数.

        Args:
            x (int): 要素

        Returns:
            int: 要素数
        """

        return -self.parents[self.find(x)]

    def same(self, x: int, y: int) -> bool:
        """ 要素 x, y は同一視されているか?

        Args:
            x (int): 要素 1
            y (int): 要素 2

        Returns:
            bool: 同一視されているならば True
        """
        return self.find(x) == self.find(y)

    def update(self, x: int, color: M) -> None:
        """ 要素 x の属する族の色を color に変更する.

        Args:
            x (int): 要素
            color (M): 色
        """

        self.data[self.find(x)]=color

    def get(self, x: int) -> M:
        """ 要素 x の属する族の色を求める.

        Args:
            x (int): 要素

        Returns:
            M: 要素 x の属する族の色
        """
        return self.data[self.find(x)]

    def members(self, x: int) -> list[int]:
        """ 要素 x が属している族の要素.
        ※族の要素の個数が欲しいときは size を使うこと!!

        Args:
            x (int): 要素

        Returns:
            list[int]: 要素 x が属している族
        """

        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self) -> list[int]:
        """ 族の名前のリスト
        """
        return [i for i,x in enumerate(self.parents) if x < 0]

    def group_count(self) -> int:
        """ 族の個数
        """
        return self.__group_number

    def all_group_members(self) -> dict[int, list[int]]:
        """ 全ての族の出力
        """
        X={r:[] for r in self.roots()}
        for k in range(self.n):
            X[self.find(k)].append(k)
        return X

    def list(self) -> list[M]:
        return [self.get(x) for x in range(self.n)]

    def map(self) -> dict[int, M]:
        return { root: self.get(root) for root in self.roots()}

    def __str__(self) -> str:
        segments = [f"({self.get(x)}) {g}" for x, g in self.all_group_members().items()]
        return ", ".join(segments)

    def __repr__(self) -> str:
        return f"Coloring Union Find: {str(self)}"

    def __getitem__(self, index) -> M:
        return self.data[self.find(index)]

    def __setitem__(self, index, value) -> None:
        self.data[self.find(index)]=value
