from typing import TypeVar, Generic, Callable

G = TypeVar('G')
class Potentilized_Union_Find(Generic[G]):
    def __init__(self, N: int, op: Callable[[G, G], G], zero: G, neg: Callable[[G], G]):
        """ 0, 1, ..., N - 1 を要素としたポテンシャル付き Union_Find を実装する.

        Args:
            N (int): 要素数
            op (Callable[[G, G], G]): 群演算
            zero (G): 群 G 上の単位元
            neg (Callable[[G], G]): 群 G の逆元を求める関数
        """

        self.n = N
        self.parents = [-1] * N
        self.rank = [0] * N
        self.edges = [0] * N
        self.pot = [zero] * N
        self.valid = [True] * N
        self.__group_number = N

        self.op = op
        self.diff : Callable[[int, int], G] = lambda u, v: self.op(u, self.neg(v)) # diff(u, v) = U(u) - U(v)
        self.zero = zero
        self.neg = neg

    def find(self, x: int) -> int:
        """ 要素 x が属している族を調べる

        Args:
            x (int): 要素

        Returns:
            int: x が属している族
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

    def union(self, x: int, y: int, u: G) -> None:
        """ 要素 x, y を同一視し, U(y) - U(x) = u という情報を加える.

        Args:
            x (int): 基準点
            y (int): 対象点
            u (G): ポテンシャルの差
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

    def size(self, x: int) -> int:
        """ 要素 x が属している族のサイズを求める

        Args:
            x (int): 要素

        Returns:
            int: 要素 x が属している族のサイズ
        """

        return -self.parents[self.find(x)]

    def potential_energy(self, x: int, y: int) -> G | None:
        """ x を基準にした y のポテンシャルエネルギー

        Args:
            x (int): 基準点
            y (int): ポテンシャルを求める点

        Returns:
            G | None: 不明な場合や非妥当である場合は None
        """

        if self.same(x,y) and self.is_valid(x):
            return self.diff(self.pot[y], self.pot[x])
        else:
            return None

    def same(self, x: int, y: int) -> bool:
        """ 要素 x, y は同一視されているか?

        Args:
            x (int): 要素
            y (int): 要素

        Returns:
            bool: x, y が同一視されていれば True, そうでなければ False
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

    def is_valid(self, x: int) -> bool:
        """ x が属している族のポテンシャルが妥当かどうかを判定する.

        Args:
            x (int): 点

        Returns:
            bool: 妥当ならば True, そうでなければ False
        """

        return self.valid[self.find(x)]

    def is_well_defined(self) -> bool:
        """ この系全体のポテンシャルが妥当かどうかを判定する.

        Returns:
            bool: 妥当ならば True, そうでなければ False
        """

        return all(self.is_valid(x) for x in range(self.n))

    def is_forest(self, x):
        """ 要素 x が属する族が森かどうかを判定する.

        x: 要素
        """
        return self.size(x)==self.edges[self.find(x)]+1

    def is_tree(self, x: int) -> bool:
        """ 要素 x が属する族が木かどうかを判定する.

        Args:
            x (int): 要素

        Returns:
            bool: 木ならば True, そうでなければ False
        """

        return sum(self.is_tree(g) for g in self.representative())

    def representative(self) -> list[int]:
        """ 代表元のリストを出力する

        Returns:
            list[int]: 代表元のリスト
        """
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self) -> int:
        """ 族の個数を出力する.

        Returns:
            int: 族の個数
        """

        return self.__group_number

    def all_group_members(self) -> dict[int, list[int]]:
        """ 全ての族の出力
        """

        groups: dict[int, list[int]] = { r: [] for r in self.representative() }
        for x in range(self.n):
            groups[self.find(x)].append(x)
        return groups

    def refresh(self):
        """ Union Find の情報を簡潔にする.
        """

        for i in range(self.n):
            self.find(i)

    def __str__(self):
        return ', '.join(f'{r}: {self.members(r)}' for r in self.representative())

    def __repr__(self):
        return f"{self.__class__.__name__}({self.n}, {self.op}, {self.zero}, {self.neg})"
