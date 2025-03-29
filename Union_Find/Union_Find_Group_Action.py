from typing import TypeVar, Generic, Callable

G = TypeVar('G')
class Union_Find_Group_Action(Generic[G]):
    def __init__(self, N: int, add: Callable[[G, G], G], zero: G, neg: Callable[[G], G]):
        # Union Find で用いる変数
        self.__groups = [[x] for x in range(N)]
        self.__belong = [x for x in range(N)]

        # Group に関する値
        self.__add = add
        self.__neg = neg

        # Group の積に関する変数
        self.__lazy = [zero for _ in range(N)]
        self.__provisional = [zero for _ in range(N)]

    def find(self, x: int) -> int:
        """ 頂点 x が属する連結成分の代表元を求める.

        Args:
            x (int): 頂点番号

        Returns:
            int: 頂点 x が属する連結成分の代表元
        """
        return self.__belong[x]

    def union(self, x: int, y: int) -> bool:
        """ 頂点 x と頂点 y を結ぶ辺を追加する.

        Args:
            x (int): 頂点番号
            y (int): 頂点番号

        Returns:
            bool: 元々頂点 x と頂点 y が非連結ならば True, 連結ならば False
        """
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return False

        if self.size(x) < self.size(y):
            x, y = y, x

        self.__groups[x].extend(self.__groups[y])

        for z in self.__groups[y]:
            self.__belong[z] = x
            self.__provisional[z] = self.__add(self.__neg(self.__lazy[x]), self.__provisional[z])

        return True

    def same(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def size(self, x: int) -> int:
        return len(self.__groups[self.find(x)])

    def action(self, x: int, a: G):
        """ x が属する連結成分全てに a を作用させる.

        Args:
            x (int): 頂点番号
            a (G): 作用
        """

        x = self.find(x)
        self.__lazy[x] = self.__add(a, self.__lazy[x])

    def update(self, x: int, a: G):
        """ 頂点 x のラベルを a に更新する.

        Args:
            x (int): 頂点番号
            a (G): 変更後のラベル
        """

        self.__provisional[x] = self.__add(self.__neg(self.__lazy[self.find(x)]), a)

    def get(self, x: int) -> G:
        """ 頂点 x のラベルを取得する.

        Args:
            x (int): 頂点番号

        Returns:
            G: 頂点 x のラベル
        """

        return self.__add(self.__lazy[self.find(x)], self.__provisional[x])

    def __getitem__(self, x: int) -> G:
        return self.get(x)

    def __len__(self) -> int:
        return len(self.__belong)

    def __iter__(self):
        yield from [self.get(x) for x in range(len(self))]
