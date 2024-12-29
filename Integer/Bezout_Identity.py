class Bezout_Identity:
    inf = float('inf')

    @staticmethod
    def __extgcd(a: int, b: int) -> tuple[int, int, int]:
        s, t, u, v = 1, 0, 0, 1
        while b:
            q, a, b = a // b, b, a % b
            s, t, u, v = u, v, s - q * u, t - q * v
        return s, t, a

    @classmethod
    def __inequality_geq(cls, a: int, b: int):
        """ 不等式 a x >= b を解く.

        Args:
            a (int)
            b (int)
        """

        if a > 0:
            left = (b - 1) // a + 1 if abs(b) < cls.inf else b
            return (left, cls.inf)
        elif a < 0:
            return cls.__inequality_leq(-a, -b)
        else:
            if 0 >= b:
                return (-cls.inf, cls.inf)
            else:
                return (cls.inf, -cls.inf)

    @classmethod
    def __inequality_leq(cls, a: int, b: int):
        """ 不等式 a x <= b を解く.

        Args:
            a (int)
            b (int)
        """

        if a > 0:
            right = b // a if abs(b) < cls.inf else b
            return (-cls.inf, right)
        elif a < 0:
            return cls.__inequality_geq(-a, -b)
        else:
            if 0 <= b:
                return (-cls.inf, cls.inf)
            else:
                return (cls.inf, -cls.inf)

    @classmethod
    def __inequality_interval(cls, a: int, l: int, r: int):
        """ 不等式 l <= ax <= r, x in Z であることと, L <= x <= R が同値になる (L, R) を求める.

        Args:
            a (int)
            l (int)
            r (int)
        """

        # ax >= l
        sl, sr = cls.__inequality_geq(a, l)

        # ax <= r
        tl, tr = cls.__inequality_leq(a, r)

        return max(sl, tl), min(sr, tr)

    @classmethod
    def __is_finite(cls, x):
        return abs(x) < cls.inf

    @classmethod
    def __fetch_example(cls, l, r):
        """ l <= k <= r を満たす k の例を求める

        Args:
            l (int): 下端
            r (int): 上端
        """

        assert l <= r
        if cls.__is_finite(l):
            return l
        elif cls.__is_finite(r):
            return r
        elif l == -cls.inf and r == cls.inf:
            return 0
        else:
            return l

    def __init__(self, a: int, b: int):
        """ a x + b y 型の Bezout 式を生成する.

        Args:
            a (int): x 側係数
            b (int): y 側係数
        """

        self.a = a; self.b = b

        # a s + b t = gcd(a, b) を満たす s, t を求める.
        self.hint_s, self.hint_t, self.gcd = self.__extgcd(a, b)

    def solve(self, c: int, lx: int, rx: int, ly: int, ry: int):
        """ a x + b y = c , lx <= x <= rx, ly <= y <= ry を満たすような整数の組 (x,y) を求める.

        [Input]
        a != 0, b != 0
        lx <= rx, ly <= ry

        [Output]
        存在しない場合, (None, None, None, None, None, None)
        存在する場合, (p0, p1, q0, q1, lk, rk) の形のタプルである. 以下を意味する.
        x = p0 + p1 k, y = q0 + q1 k, lk <= k <= rk
        """

        # a = 0 または b = 0 の場合は縮退してしまう
        assert self.a != 0 and self.b != 0

        # x, y の範囲が異常な場合を除く
        if not(lx <= rx and ly <= ry):
            return (None, None, None, None, None, None)

        # c が gcd(a, b) の倍数でないならば, 存在しない確定
        if c % self.gcd != 0:
            return (None, None, None, None, None, None)

        s = self.hint_s; t = self.hint_t
        g = self.gcd
        a = self.a; b = self.b

        # 両辺を g で割る (Bezout 係数が満たす式が as+bt=1 になる).
        a //= g; b //= g; c //= g

        p0, p1 = c * s, -b
        q0, q1 = c * t, a

        Lx, Rx = self.__inequality_interval(p1, lx - p0, rx - p0)
        Ly, Ry = self.__inequality_interval(q1, ly - q0, ry - q0)

        L = max(Lx, Ly); R = min(Rx, Ry)
        if L <= R:
            return p0, p1, q0, q1, L, R
        else:
            return None, None, None, None, None, None

    def find(self, c: int, lx: int, rx: int, ly: int, ry: int):
        """ a x + b y = c, lx <= x <= ry, ly <= y <= ry を満たす整数の組 (x, y) を存在するならば 1 組求める

        Args:
            c (int):
            lx (int): x 下限
            rx (int): x 上限
            ly (int): y 下限
            ry (int): y 上限
        """

        # x, y の範囲が異常な場合を除く
        if not(lx <= rx and ly <= ry):
            return (None, None)

        a = self.a; b = self.b
        # a = b = 0 のときは c = 0 しか解にならない.
        if a == b == 0:
            if c == 0:
                return (self.__fetch_example(lx, rx), self.__fetch_example(rx, ry))
            else:
                return (None, None)

        # a != 0, b = 0 の場合
        if b == 0:
            # 方程式は a x = c になる.
            if c % a == 0:
                return (c // a, self.__fetch_example(ly, ry))
            else:
                return (None, None)

        # a = 0, b != 0 の場合
        if a == 0:
            # 方程式は b y = c になる.
            if c % b == 0:
                return (self.__fetch_example(lx, rx), c // b)
            else:
                return (None, None)

        # ここまで来たら, a != 0, b != 0 が確定なため, solve が使える.
        p0, p1, q0, q1, lk, rk = self.solve(c, lx, ry, ly, ry)

        if p0 is None:
            return None, None

        # lk <= k <= rk を満たす k の例を求める.
        k = self.__fetch_example(lk, rk)

        # 解あり
        return p0 + p1 * k, q0 + q1 * k

    def count(self, c: int, lx: int, rx: int, ly: int, ry: int):
        _, _, _, _, lk, rk = self.solve(c, lx, rx, ly, ry)
        if lk is None:
            return 0
        else:
            return rk - lk + 1
