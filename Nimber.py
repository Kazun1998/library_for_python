class Nimber:
    def __init__(self, x: int = 0):
        self.__x = x

    def __str__(self):
        return str(self.__x)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__x})"

    def __add__(self, other: "Nimber") -> "Nimber":
        return Nimber(self.__x ^ other.__x)

    def __mul__(self, other: "Nimber") -> "Nimber":
        pass

    @classmethod
    def __mul_calc(cls, x: int, y: int) -> int:
        pass

    @staticmethod
    def __floor_log(x: int) -> int:
        return x.bit_length() - 1

    @staticmethod
    def __separate(x: int, lv: int):
        upper = x >> (1 << (lv - 1))
        lower = x ^ (upper << (1 << (lv - 1)))
        return upper, lower

    @classmethod
    def level(cls, x: int) -> int:
        if x == 0:
            return 0
        else:
            return cls.__floor_log(cls.__floor_log(cls.__x)) + 1

    def __hash__(self) -> int:
        return hash(self.__x)