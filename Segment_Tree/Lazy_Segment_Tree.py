"""
Note
[1] RMQ(区間上の最小値:Range Minimum Query)
op=lambda x,y:min(x,y)
unit=float("inf")
act=lambda alpha,x:alpha
comp=lambda alpha,beta:alpha
"""
from typing import TypeVar, Callable, Generic

M = TypeVar('M')
F = TypeVar('F')
class Lazy_Evaluation_Tree(Generic[M, F]):
    def __init__(self, L: list[M], op: Callable[[M, M], M], unit: M, act: Callable[[F, M], M], comp: Callable[[F, F], F], id: F):
        """ op を演算, act を作用とする L を初期状態とする遅延セグメント木を作成する.

        [条件]
        M: Monoid, F={f: F x M→ M: 作用素} に対して, 以下が成立する.
        F は恒等写像 id を含む.つまり, 任意の x in M に対して id(x)=x
        F は写像の合成に閉じている. つまり, 任意の f,g in F に対して, comp(f,g) in F
        任意の f in F, x,y in M に対して, f(xy)=f(x) f(y) である.

        [注意]
        作用素は左から掛ける. 更新も左から.

        Args:
            L (list[M]): 初期状態
            op (Callable[[M, M], M]): M の演算
            unit (M): M の単位元
            act (Callable[[F, M], M]): F から M への作用
            comp (Callable[[F, F], F]): F 同士の合成
            id (F): F の単位元
        """

        self.op = op
        self.unit = unit
        self.act = act
        self.comp = comp
        self.id = id

        N = len(L)
        d = max(1, (N - 1).bit_length())
        k = 1 << d

        self.data = data = [unit] * k + L + [unit] * (k - len(L))
        self.lazy = [id] * (2 * k)
        self.N = k
        self.depth = d

        for i in range(k - 1, 0, -1):
            data[i] = op(data[i << 1], data[i << 1 | 1])

    def _eval_at(self, m: int) -> None:
        return self.data[m] if self.lazy[m] == self.id else self.act(self.lazy[m], self.data[m])

    #配列の第m要素を下に伝搬
    def _propagate_at(self, m: int) -> None:
        self.data[m] = self._eval_at(m)
        lazy = self.lazy; comp = self.comp

        if m < self.N and self.lazy[m] != self.id:
            lazy[m << 1] = comp(lazy[m], lazy[m << 1])
            lazy[m << 1 | 1] = comp(lazy[m], lazy[m << 1 | 1])

        lazy[m] = self.id

    #配列の第m要素より上を全て伝搬
    def _propagate_above(self, m: int) -> None:
        for h in range(m.bit_length() - 1, 0, -1):
            self._propagate_at(m >> h)

    #配列の第m要素より上を全て再計算
    def _recalc_above(self, m: int) -> None:
        data = self.data; op = self.op
        eval_at = self._eval_at
        while m > 1:
            m >>= 1
            data[m] = op(eval_at(m << 1), eval_at(m << 1 | 1))

    def get(self, k: int) -> M:
        """ 第 k 要素を取得する

        Args:
            k (int): 要素の場所

        Returns:
            M: 第 k 要素
        """
        m = k + self.N
        self._propagate_above(m)
        self.data[m] = self._eval_at(m)
        self.lazy[m] = self.id
        return self.data[m]

    #作用
    def action(self, l: int, r: int, alpha: F, left_closed: bool = True, right_closed: bool = True) -> None:
        """ 第 l 要素から第 r 要素まで全てに alpha を作用させる

        Args:
            l (int): 左端
            r (int): 右端
            alpha (F): 作用させる値
            left_closed (bool, optional): False にすると, 左端が開区間になる. Defaults to True.
            right_closed (bool, optional): False にすると, 右端が開区間になる. Defaults to True.
        """

        L = l + self.N + (not left_closed)
        R = r + self.N + right_closed

        L0 = R0 = -1
        X, Y = L, R- 1
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

        lazy = self.lazy; comp = self.comp
        while L < R:
            if L & 1:
                lazy[L] = comp(alpha, lazy[L])
                L += 1

            if R & 1:
                R -= 1
                lazy[R] = comp(alpha, lazy[R])

            L >>= 1
            R >>= 1

        self._recalc_above(L0)
        self._recalc_above(R0)

    def update(self, k: int, x: M) -> None:
        """ 第 k 要素を x に更新する.

        Args:
            k (int): 要素の場所
            x (M): 変更後の第 k 要素
        """

        m = k+self.N
        self._propagate_above(m)
        self.data[m] = x
        self.lazy[m] = self.id
        self._recalc_above(m)

    def product(self, l: int, r: int, left_closed: bool = True, right_closed: bool = True) -> M:
        """ 第 l 要素から第 r 要素までの総積を求める.

        Args:
            l (int): 左端
            r (int): 右端
            left_closed (bool, optional): False にすると, 左端が開区間になる. Defaults to True.
            right_closed (bool, optional): False にすると, 右端が開区間になる. Defaults to True.

        Returns:
            M: 総積
        """

        L = l + self.N + (not left_closed)
        R = r + self.N + right_closed

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

        vL = vR = self.unit
        op = self.op; eval_at = self._eval_at
        while L < R:
            if L & 1:
                vL = op(vL, eval_at(L))
                L += 1

            if R & 1:
                R -= 1
                vR = op(eval_at(R), vR)

            L >>= 1
            R >>= 1

        return self.op(vL, vR)

    def all_product(self) -> M:
        """ この遅延セグメント木が持っている要素に関する総積を求める.

        Returns:
            M: 総積
        """

        return self.product(0, self.N - 1)

    def max_right(self, left: int, cond: Callable[[int], bool]) -> int:
        """ 以下の2つをともに満たす r の1つを返す.\n
        (1) r = left or cond(data[left] * data[left + 1] * ... * data[r - 1]): True
        (2) r = N or cond(data[left] * data[left + 1] * ... * data[r]): False
        ※ cond が単調減少の時, cond(data[left] * ... * data[r - 1]): True を満たす最大の r となる.

        Args:
            left (int): 左端
            cond: 条件式 (cond(unit) = True を要求)

        Returns:
            int: 条件を満たす r.
        """

        assert 0 <= left <= self.N
        assert cond(self.unit)

        if left == self.N:
            return self.N

        left += self.N

    def max_right(self, left: int, cond) -> int:
        """ 以下の (1), (2) を満たす整数 r を求める.
        (1) r=left or cond(data[left] data[left+1] ... data[r-1]): True
        (2) r=N or cond(data[left] data[left+1] ... data[r]): False

        Args:
            left (int): 左端
            cond : 条件

        Returns:
            int: (1), (2) を満たす整数 r
        """

        assert 0 <= left <= self.N, f"添字 ({left = }) が範囲外"
        assert cond(self.unit), "単位元が条件を満たさない"

        if left == self.N:
            return self.N

        left += self.N
        sm = self.unit

        op = self.op; data = self.data
        first = True

        self._propagate_above(left)

        while first or (left & (-left)) != left:
            first = False
            while left % 2 == 0:
                left >>= 1

            if not cond(op(sm, data[left])):
                while left < self.N:
                    self._propagate_at(left)
                    left <<= 1
                    self._propagate_at(left)
                    if cond(op(sm, data[left])):
                        sm = op(sm, data[left])
                        left += 1
                return left - self.N
            sm = op(sm, data[left])
            left += 1

        return self.N

    #リフレッシュ
    def refresh(self) -> None:
        """ 遅延セグメント木の遅延情報をリセットする.
        """

        lazy = self.lazy; comp = self.comp
        for m in range(1, 2 * self.N):
            self.data[m] = self._eval_at(m)

            if m < self.N and self.lazy[m] != self.id:
                lazy[m << 1] = comp(lazy[m], lazy[m << 1])
                lazy[m << 1 | 1] = comp(lazy[m], lazy[m << 1 | 1])
            lazy[m] = self.id

    def __getitem__(self, k: int) -> M:
        return self.get(k)

    def __setitem__(self, k: int, x: M) -> None:
        self.update(k, x)
