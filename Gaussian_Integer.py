class Gaussian_Integer:
    def __new__(cls, real: int = 0, imaginary: int = 0) -> "Gaussian_Integer":
        """ 実部 real, 虚部 imaginary の Gauss 整数を生成する.

        Args:
            real (int, optional): 実部. Defaults to 0.
            imaginary (int, optional): 虚部. Defaults to 0.

        Returns:
            Gaussian_Integer:
        """

        self = super().__new__(cls)
        self.__re = real
        self.__im = imaginary
        return self

    @property
    def re(self) -> int:
        return self.__re

    @property
    def im(self) -> int:
        return self.__im

    #表示定義
    def __str__(self) -> str:
        if self.re == 0:
            if self.im == 0:
                return "0"
            elif self.im == 1:
                return "i"
            elif self.im == -1:
                return "-i"
            else:
                return f"{self.im}i"
        else:
            if self.im == 0:
                return str(self.re)
            elif self.im == 1:
                return f"{self.re}+i"
            elif self.im == -1:
                return f"{self.re}-i"
            else:
                return f"{self.re}{self.im:+}i"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.re}, {self.im})"

    #四則演算定義
    #加法
    def __add__(self, other: "Gaussian_Integer") -> "Gaussian_Integer":
        if isinstance(other, Gaussian_Integer):
            return Gaussian_Integer(self.re + other.re, self.im + other.im)
        elif isinstance(other, int):
            return Gaussian_Integer(self.re + other, self.im)
        else:
            raise NotImplementedError

    def __radd__(self, other: "Gaussian_Integer") -> "Gaussian_Integer":
        return self + other

    #減法
    def __sub__(self, other: "Gaussian_Integer") -> "Gaussian_Integer":
        if isinstance(other, Gaussian_Integer):
            return Gaussian_Integer(self.re - other.re, self.im - other.im)
        elif isinstance(other, int):
            return Gaussian_Integer(self.re - other, self.im)
        else:
            raise NotImplementedError

    def __rsub__(self, other: "Gaussian_Integer") -> "Gaussian_Integer":
        return (-self) + other

    #乗法
    def __mul__(self, other: "Gaussian_Integer") -> "Gaussian_Integer":
        a, b = self.re, self.im
        if isinstance(other, Gaussian_Integer):
            c, d = other.re, other.im
        elif isinstance(other, int):
            c, d = other, 0
        else:
            raise NotImplementedError

        x = a * c - b * d
        y = a * d + b * c
        return Gaussian_Integer(x, y)

    def __rmul__(self, other: "Gaussian_Integer") -> "Gaussian_Integer":
        return self * other

    def __floordiv__(self, other: "Gaussian_Integer") -> "Gaussian_Integer":
        if isinstance(other, int):
            other = Gaussian_Integer(other, 0)

        a, b = self.re, self.im
        c, d = other.re, other.im

        n = other.norm()

        p = (2 * (a * c + b * d) + n) // (2 * n)
        q = (2 * (b * c - a * d) + n) // (2 * n)

        return Gaussian_Integer(p, q)

    def __divmod__(self, other: "Gaussian_Integer") -> "Gaussian_Integer":
        x = self // other
        return (x, self - other * x)

    def __mod__(self, other: "Gaussian_Integer") -> "Gaussian_Integer":
        return  self - other * (self // other)

    #比較演算子
    def __eq__(self, other: "Gaussian_Integer") -> bool:
        if isinstance(other, Gaussian_Integer):
            return (self.re == other.re) and (self.im == other.im)
        elif isinstance(other, int):
            return (self.re == other) and (self.im == 0)
        else:
            return NotImplementedError

    def __bool__(self):
        return not self.is_zero()

    #その他
    def is_zero(self) -> bool:
        """ 0 か?

        Returns:
            bool: 0 なら True, そうでないならば False
        """
        return (self.re == 0) and (self.im == 0)

    def conjugate(self) -> "Gaussian_Integer":
        """ 共役を求める

        Returns:
            Gaussian_Integer: 共役
        """
        return Gaussian_Integer(self.re, -self.im)

    def __abs__(self) -> float:
        import math
        return math.sqrt(self.norm())

    def norm(self) -> int:
        """ Gauss 整数上ノルム (= 絶対値の 2 乗) を求める

        Returns:
            int: Gauss 整数のノルム
        """
        return self.re * self.re + self.im * self.im

    #符号
    def __pos__(self) -> "Gaussian_Integer":
        return self

    def __neg__(self) -> "Gaussian_Integer":
        return Gaussian_Integer(-self.re, -self.im)

    #コピー
    def __copy__(self):
        return self

    #ハッシュ
    def __hash__(self):
        return hash((self.re, self.im))

#最大公約数
def gcd(x: Gaussian_Integer, y: Gaussian_Integer) -> Gaussian_Integer:
    """  Gauss 整数 x, y の最大公約数 gcd(x, y) を求める.

    Args:
        x (Gaussian_Integer):
        y (Gaussian_Integer):

    Returns:
        Gaussian_Integer: 最大公約数 (単数倍の違いによる差が生まれる可能性はある)
    """

    while not y.is_zero():
        x, y = y, x % y
    return x

#拡張Euclidの互除法
def Extended_Euclid(x: Gaussian_Integer, y: Gaussian_Integer) -> tuple[Gaussian_Integer, Gaussian_Integer, Gaussian_Integer]:
    """ Gauss 整数 x, y について, a x + b y = gcd(x, y) となる (a, b, gcd(x, y)) の例を求める.

    Args:
        x (Gaussian_Integer):
        y (Gaussian_Integer):

    Returns:
        tuple[Gaussian_Integer, Gaussian_Integer, Gaussian_Integer]: (a, b, g) のタプルであり, 以下を満たす.
            g = gcd(x, y)
            a x + b y = g
    """

    a0, b0, a1, b1 = 1, 0, 0, 1
    while y:
        q, x, y = x // y, y, x % y
        a0, a1 = a1, a0 - q * a1
        b0, b1 = b1, b0 - q * b1
    return a0, b0, x

#同伴?
def Is_Associate(x: Gaussian_Integer, y: Gaussian_Integer) -> bool:
    """ x, y は同伴?

    Args:
        x (Gaussian_Integer):
        y (Gaussian_Integer):

    Returns:
        bool: 同伴 ?
    """

    e = Gaussian_Integer(0, 1)

    a = (x == y)
    b = (x == -y)
    c = (x == y * e)
    d = (x == y * (-e))

    return a or b or c or d
