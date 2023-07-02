from math import gcd

class Fraction():
    reduction = False
    expand = False

    """
    reduction : 分数を約分した状態で保存するかどうか
    expand : 1/0, -1/0 を認めるかどうか
    """

    ##入力定義
    def __init__(self, Numerator = 0, Denominator = 1):
        """分数のオブジェクトを生成する.

        Numerator : 分子
        Denominator : 分母
        """
        assert Denominator or Fraction.expand, "分母が0"

        if Denominator < 0:
            Numerator *= -1
            Denominator *= -1

        self.__a = Numerator
        self.__b = Denominator
        if Fraction.reduction:
            g=gcd(Numerator, Denominator)
            self.__a = Numerator // g
            self.__b = Denominator // g

    def numerator(self):
        return self.__a

    def denominator(self):
        return  self.__b

    def value(self):
        return self.__a, self.__b

    def __iter__(self):
        yield self.__a
        yield self.__b

    #表示定義
    def __str__(self):
        if self.__b == 1:
            return str(self.__a)
        else:
            return "{}/{}".format(self.__a, self.__b)

    __repr__=__str__

    #四則演算定義
    def __add__(self, other):
        if isinstance(other, Fraction):
            x = self.__a * other.__b + self.__b*other.__a
            y = self.__b * other.__b
        elif isinstance(other, int):
            x = self.__a + self.__b * other
            y = self.__b
        else:
            assert 0, "型が違う"
        return Fraction(x, y)

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        if isinstance(other, Fraction):
            x = self.__a * other.__b - self.__b * other.__a
            y = self.__b * other.__b
        elif isinstance(other, int):
            x = self.__a - self.__b * other
            y = self.__b
        else:
            assert 0, "型が違う"
        return Fraction(x, y)

    def __rsub__(self, other):
        return - self + other

    def __mul__(self, other):
        if isinstance(other, Fraction):
            x = self.__a * other.__a
            y = self.__b * other.__b
        elif isinstance(other, int):
            x = self.__a * other
            y = self.__b
        else:
            assert 0, "型が違う"

        return Fraction(x, y)

    def __rmul__(self, other):
        return self * other

    def __floordiv__(self, other):
        if other == Fraction():
            raise ZeroDivisionError

        H = self / other
        return H.a//H.b

    def __rfloordiv__(self, other):
        if self == Fraction():
            raise ZeroDivisionError

        H = other / self
        return H.a // H.b

    def __truediv__(self, other):
        assert other, "除数が0"

        if isinstance(other, Fraction):
            x = self.__a * other.__b
            y = self.__b * other.__a
        elif other.__class__ == int:
            x = self.__a
            y = self.__b * other
        else:
            assert 0, "型が違う"

        return Fraction(x, y)

    def __rtruediv__(self, other):
        assert self,"除数が0"
        if isinstance(other, Fraction):
            x = other.__a * self.__b
            y = other.__b * self.__a
        elif isinstance(other, int):
            x = other * self.__b
            y = self.__a
        else:
            assert 0, "型が違う"
        return Fraction(x, y)

    def __pow__(self, m):
        alpha, beta = self.__a, self.__b

        if m < 0:
            alpha, beta = beta, alpha
            m = -m

        return Fraction(pow(alpha, m), pow(beta, m))

    #丸め
    def __floor__(self):
        return self.__a // self.__b

    def __ceil__(self):
        return (self.__a + self.__b - 1) // self.__b

    #真偽値
    def __bool__(self):
        return bool(self.__a)

    def __compare(self, other):
        if isinstance(other, Fraction):
            x = self.__a * other.__b
            y = self.__b * other.__a
        else:
            x = self.__a
            y = self.__b*other
        return x, y

    #比較
    def __eq__(self, other):
        x, y = self.__compare(other)
        return x == y

    def __nq__(self, other):
        x, y = self.__compare(other)
        return x != y

    def __lt__(self, other):
        x, y = self.__compare(other)
        return x < y

    def __le__(self, other):
        x, y = self.__compare(other)
        return x <= y

    def __gt__(self, other):
        x, y = self.__compare(other)
        return x > y

    def __ge__(self, other):
        x, y = self.__compare(other)
        return x >= y

    #その他
    def __float__(self):
        return self.__a / self.__b

    def sign(self):
        if self.__a > 0:
            return 1
        elif self.__a == 0:
            return 0
        else:
            return -1

    #符号
    def __pos__(self):
        return self

    def __neg__(self):
        return Fraction(-self.__a, self.__b)

    def __abs__(self):
        if self.__a > 0:
            return self
        else:
            return -self

    #その他
    def is_unit(self):
        return self.__a == 1

    def __hash__(self):
        x = self.__a; y = self.__b
        if not Fraction.reduction:
            g=gcd(x, y)
            x //= g; y //= g
        return hash((x, y))
