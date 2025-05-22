from typing import TypeVar, Generic, Callable

F = TypeVar('F')
class Dual_Segment_Tree(Generic[F]):
    def __init__(self, A: list[F], comp: Callable[[F, F], F], id: F):
        """ comp を演算とするリスト L の Dual Segment Tree を作成

        comp : 作用素
        id : 単位元

        [注記]
        更新は左から. つまり, comp(new, old) となる.
        """

        self.__comp = comp
        self.__id = id

        N = len(A)
        d = max(1, (N - 1).bit_length())
        k = 1 << d

        self.lazy = [self.id] * k + A + [self.id] * (k - N)
        self.__size = k

    @property
    def comp(self) -> Callable[[F, F], F]:
        return self.__comp

    @property
    def id(self) -> F:
        return self.__id

    @property
    def size(self) -> int:
        """ Dual Segment Tree の大きさ (扱える要素番号の最大値)

        Returns:
            int: Dual Segment Tree の大きさ
        """
        return self.__size

    #配列の第 m 要素を下に伝搬
    def _propagate_at(self, m: int):
        """ 遅延伝搬配列の第 m 要素を 1 個下の子に伝搬させる.

        Args:
            m (int): 要素番号
        """

        lazy = self.lazy
        if lazy[m] == self.id:
            return

        lazy[(m << 1) | 0] = self.comp(lazy[m], lazy[(m << 1) | 0])
        lazy[(m << 1) | 1] = self.comp(lazy[m], lazy[(m << 1) | 1])
        lazy[m] = self.id

    #配列の第 m 要素より上を全て伝搬
    def _propagate_above(self, m: int):
        """ 遅延伝搬配列の第 m 要素の先祖 (自分自身除く) を根から順に伝搬させる.

        Args:
            m (int): 配列の番号
        """

        for h in range(m.bit_length() - 1, 0, -1):
            self._propagate_at(m >> h)

    #作用
    def action(self, l: int, r: int, alpha: F, left_closed: bool = True, right_closed: bool = True):
        """ 第 l 要素から第 r 要素までの各要素に alpha を作用させる.

        Args:
            l (int): 左端
            r (int): 右端
            alpha (F): 作用させる値
            left_closed (bool, optional): False にすると, 左端が開区間になる. Defaults to True.
            right_closed (bool, optional): False にすると, 右端が開区間になる. Defaults to True.
        """
        L = l + self.size + (not left_closed)
        R = r + self.size + (right_closed)

        L0 = R0 = -1
        X, Y = L, R - 1
        while X < Y:
            if X & 1:
                L0 = max(L0, X)
                X += 1

            if Y & 1 == 0:
                R0 = max(R0, Y)
                Y -= 1

            X >>= 1
            Y >>= 1

        L0 = max(L0, X)
        R0 = max(R0, Y)

        self._propagate_above(L0)
        self._propagate_above(R0)

        lazy = self.lazy
        comp = self.comp
        while L < R:
            if L & 1:
                lazy[L] = comp(alpha, lazy[L])
                L += 1

            if R & 1:
                R -= 1
                lazy[R] = comp(alpha, lazy[R])

            L >>= 1
            R >>= 1

    #リフレッシュ
    def refresh(self):
        """ 全ての遅延している伝搬を解除する.
        """

        for m in range(1, self.size):
            self._propagate_at(m)

    #取得
    def get(self, k: int) -> F:
        """ 第 k 要素を取得する.

        Args:
            k (int): 要素の番号

        Returns:
            F: 第 k 要素
        """

        m = k + self.size
        self._propagate_above(m)
        return self.lazy[m]

    def __getitem__(self, index: int) -> F:
        m = index + self.size
        self._propagate_above(m)
        return self.lazy[m]
