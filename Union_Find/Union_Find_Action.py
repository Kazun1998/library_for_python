from typing import TypeVar, Generic, Callable

M = TypeVar('M')
class Union_Find_Action(Generic[M]):
    def __init__(self, N: int, op: Callable[[M, M], M], unit: M):
        # Union Find で用いる変数
        self.__groups = [[x] for x in range(N)]
        self.__belong = [x for x in range(N)]

        # Monoid に関する値
        self.__op = op
        self.__unit = unit

        # Monoid の積に関する変数
        self.__segments = [[[]] for _ in range(N)]
        self.__provisional = [unit for _ in range(N)]
        self.__time_offset = [0] * N

    def find(self, x: int) -> int:
        return self.__belong[x]

    def union(self, x: int, y: int) -> bool:
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return False

        if self.size(x) < self.size(y):
            x, y = y, x

        self.__groups[x].extend(self.__groups[y])
        memo = [self.get(z) for z in self.__groups[y]]
        for z, b in zip(self.__groups[y], memo):
            self.__belong[z] = x
            self.update(z, b)

        self.__groups[y].clear()

        return True

    def same(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def size(self, x: int) -> int:
        return len(self.__groups[self.find(x)])

    def action(self, x: int, a: M):
        """ x が属する連結成分全てに a を作用させる.

        Args:
            x (int): 頂点番号
            a (M): 作用
        """

        x = self.find(x)
        segment = self.__segments[x]
        op = self.__op

        i = 0
        segment[0].append(a)
        while True:
            if len(segment[i]) % 2 == 1:
                break

            if len(segment[i]) == 2:
                segment.append([])

            i += 1
            segment[i].append(op(segment[i - 1][-1], segment[i - 1][-2]))

    def update(self, x: int, a: M):
        """ 頂点 x のラベルを a に更新する.

        Args:
            x (int): 頂点番号
            a (M): 変更後のラベル
        """
        self.__time_offset[x] = len(self.__segments[self.find(x)][0])
        self.__provisional[x] = a

    def get(self, x: int) -> M:
        root = self.find(x)
        lazy = self.__product(self.__segments[root], self.__time_offset[x])
        return self.__op(lazy, self.__provisional[x])

    def __getitem__(self, x: int):
        return self.get(x)

    def __product(self, segment: list[list[M]], t: int):
        vl = self.__unit
        vr = self.__unit

        l = t; r = len(segment[0])
        op = self.__op
        for seg in segment:
            if not l < r:
                break

            if l & 1:
                vl = op(seg[l], vl)
                l += 1

            if r & 1:
                r -= 1
                vr = op(vr, seg[r])

            l >>= 1
            r >>= 1

        return op(vr, vl)
