class Nimber:
    def __init__(self, x: int = 0):
        if type(x) is str:
            x = int(x)

        self.__x = x

    def __eq__(self, other: "Nimber") -> bool:
        return self.__x == other.__x

    def __str__(self) -> str:
        return str(self.__x)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__x})"

    def __pos__(self) -> "Nimber":
        return Nimber(self.__x)

    def __neg__(self) -> "Nimber":
        return Nimber(self.__x)

    def __add__(self, other: "Nimber") -> "Nimber":
        return Nimber(self.__x ^ other.__x)

    def __sub__(self, other: "Nimber") -> "Nimber":
        return Nimber(self.__x ^ other.__x)

    def __mul__(self, other: "Nimber") -> "Nimber":
        lv = max(self.level(self.__x), self.level(other.__x))
        return Nimber(self.__mul_calc(self.__x, other.__x, lv))

    __SMALL_NIM_PRODUCT_MEMO = [[-1] * 256 for _ in range(256)]
    __SMALL_NIM_PRODUCT_MEMO[0][0] = __SMALL_NIM_PRODUCT_MEMO[0][1] = __SMALL_NIM_PRODUCT_MEMO[1][0] = 0
    __SMALL_NIM_PRODUCT_MEMO[1][1] = 1

    @classmethod
    def __mul_calc(cls, x: int, y: int, lv: int) -> int:
        if lv <= 3 and cls.__SMALL_NIM_PRODUCT_MEMO[x][y] != -1:
            return cls.__SMALL_NIM_PRODUCT_MEMO[x][y]

        x1, x0 = cls.separate(x, lv)
        y1, y0 = cls.separate(y, lv)

        p = cls.__mul_calc(x0, y0, lv - 1)
        e = 1 << (1 << (lv - 1))

        a = p ^ cls.__mul_calc(x0 ^ x1, y0 ^ y1, lv - 1) * e
        b = cls.__mul_calc(cls.__mul_calc(x1, y1, lv - 1), e >> 1, lv - 1)

        res = (p * e) ^ a ^ b
        if lv <= 3:
            cls.__SMALL_NIM_PRODUCT_MEMO[x][y] = res

        return res

    def __truediv__(self, other: "Nimber") -> "Nimber":
        return self * other.inverse()

    @staticmethod
    def __floor_log(x: int) -> int:
        return x.bit_length() - 1

    @staticmethod
    def separate(x: int, lv: int):
        if lv == 0:
            raise ValueError

        upper = x >> (1 << (lv - 1))
        lower = x ^ (upper << (1 << (lv - 1)))
        return upper, lower

    @classmethod
    def level(cls, x: int) -> int:
        if x == 0:
            return 0
        else:
            return cls.__floor_log(cls.__floor_log(x)) + 1

    def __hash__(self) -> int:
        return hash(self.__x)

    @classmethod
    def __square_calc(cls, x: int, lv: int) -> int:
        if lv <= 3 and cls.__SMALL_NIM_PRODUCT_MEMO[x][x] != -1:
            return cls.__SMALL_NIM_PRODUCT_MEMO[x][x]

        x1, x0 = cls.separate(x, lv)

        x1_square = cls.__square_calc(x1, lv - 1)
        x0_square = cls.__square_calc(x0, lv - 1)
        e = 1 << (1 << (lv - 1))

        res = (x1_square * e) ^ cls.__mul_calc(cls.__mul_calc(x1, x1, lv - 1), e >> 1, lv - 1) ^ x0_square
        if lv <= 3:
            cls.__SMALL_NIM_PRODUCT_MEMO[x][x] = res

        return res

    def square(self) -> "Nimber":
        """ 自分自身の自乗を求める.

        Returns:
            Nimber: self * self
        """
        return Nimber(self.__square_calc(self.__x, self.level(self.__x)))

    def __pow__(self, n: int) -> "Nimber":
        x = self
        y = Nimber(1)
        while n:
            if n & 1:
                y *= x
            x = x.square()
            n >>= 1

        return y

    def inverse(self):
        return pow(self, (1 << (1 << self.level(self.__x))) - 2)
