from typing import TypeVar, Generic

S = TypeVar('S')
T = TypeVar('T')
U = TypeVar('U')
class Triple(tuple, Generic[S, T, U]):
    def __new__(cls, first: S, second: T, third: U):
        return super().__new__(cls, (first, second, third))

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.first}, {self.second}, {self.third})"

    @property
    def first(self) -> S:
        return self[0]

    @property
    def second(self) -> T:
        return self[1]

    @property
    def third(self) -> U:
        return self[2]

    def __add__(self, other: "Triple[S, T, U]") -> "Triple[S, T, U]":
        return Triple(self.first + other.first, self.second + other.second, self.third + other.third)

    def __sub__(self, other: "Triple[S, T, U]") -> "Triple[S, T, U]":
        return Triple(self.first - other.first, self.second - other.second, self.third - other.third)

    def __mul__(self, other: "Triple[S, T, U]") -> "Triple[S, T, U]":
        return Triple(self.first * other.first, self.second * other.second, self.third * other.third)

    def __xor__(self, other: "Triple[S, T, U]") -> "Triple[S, T, U]":
        return Triple(self.first ^ other.first, self.second ^ other.second, self.third ^ other.third)
