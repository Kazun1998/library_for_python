class Gaussian_Integer():
    #入力定義
    def __init__(self, real = 0, imaginary = 0):
        self.re = real
        self.im = imaginary

    #表示定義
    def __str__(self):
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

    __repr__=__str__

    #四則演算定義
    #加法
    def __add__(self, other):
        if isinstance(other, Gaussian_Integer):
            return Gaussian_Integer(self.re + other.re, self.im + other.im)
        else:
            return Gaussian_Integer(self.re + other, self.im)

    def __radd__(self, other):
        return self + other

    #減法
    def __sub__(self, other):
        return self + (-other)

    def __rsub__(self, other):
        return (- self) + other

    #乗法
    def __mul__(self, other):
        a, b = self.re, self.im
        if isinstance(other, Gaussian_Integer):
            c, d = other.re, other.im
        else:
            c, d = other, 0

        x = a * c - b * d
        y = a * d + b * c
        return Gaussian_Integer(x, y)

    def __rmul__(self, other):
        return self * other

    def __floordiv__(self, other):
        if isinstance(other, int):
            other = Gaussian_Integer(other, 0)

        a, b = self.re, self.im
        c, d = other.re, other.im

        n = other.norm()

        p = (2 * (a * c + b * d) + n) // (2 * n)
        q = (2 * (b * c - a * d) + n) // (2 * n)

        return Gaussian_Integer(p, q)

    def __divmod__(self, other):
        x = self // other
        return (x, self - other * x)

    def __mod__(self, other):
        return  self - other * (self // other)

    #比較演算子
    def __eq__(self,other):
        if isinstance(other, Gaussian_Integer):
            return (self.re == other.re) and (self.im == other.im)
        else:
            return (self-other)==Gaussian_Integer()

    def __bool__(self):
        return bool(self.re) or bool(self.im)

    #その他
    def conjugate(self):
        return Gaussian_Integer(self.re, -self.im)

    def __abs__(self):
        import math
        return math.sqrt(self.norm())

    def norm(self):
        return self.re * self.re + self.im * self.im

    #実数から複素数に変換
    def Real_to_Complex(self):
        pass

    #符号
    def __pos__(self):
        return self

    def __neg__(self):
        return Gaussian_Integer(-self.re,-self.im)

    #コピー
    def __copy__(self):
        return self

    #ハッシュ
    def __hash__(self):
        return hash((self.re, self.im))

#最大公約数
def gcd(x: Gaussian_Integer, y: Gaussian_Integer):
    """ Gauss 整数 x, y の最大公約数 gcd(x, y) を求める.

    Args:
        x (Gaussian_Integer)
        y (Gaussian_Integer)
    """

    while y:
        x, y = y, x % y
    return x

#拡張Euclidの互除法
def Extended_Euclid(x: Gaussian_Integer, y: Gaussian_Integer):
    """ Gauss 整数 x, y について, a x + b y = gcd(x, y) となる (a, b, gcd(x, y)) の例を求める.

    Args:
        x (Gaussian_Integer)
        y (Gaussian_Integer)
    """

    a0, b0, a1, b1 = 1, 0, 0, 1
    while y:
        q, x, y = x // y, y, x % y
        a0, a1 = a1, a0 - q * a1
        b0, b1 = b1, b0 - q * b1
    return a0, b0, x

#同伴?
def Is_Associate(x,y):
    """ x, y は同伴 ?

    x, y: Gauss整数
    """

    e = Gaussian_Integer(0, 1)

    a = (x == y)
    b = (x == -y)
    c = (x == y*e)
    d = (x == y*(-e))

    return a or b or c or d
