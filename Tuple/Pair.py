from typing import TypeVar, Generic

S = TypeVar('S')
T = TypeVar('T')
class Pair(tuple, Generic[S, T]):
    def __new__(cls, first: S, second: T):
        return super().__new__(cls, (first, second))

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.first}, {self.second})"

    @property
    def first(self) -> S:
        return self[0]

    @property
    def second(self) -> T:
        return self[1]

    def __add__(self, other: "Pair[S, T]") -> "Pair[S, T]":
        return Pair(self.first + other.first, self.second + other.second)

    def __sub__(self, other: "Pair[S, T]") -> "Pair[S, T]":
        return Pair(self.first - other.first, self.second - other.second)

    def __mul__(self, other: "Pair[S, T]") -> "Pair[S, T]":
        return Pair(self.first * other.first, self.second * other.second)

    def __xor__(self, other: "Pair[S, T]") -> "Pair[S, T]":
        return Pair(self.first ^ other.first, self.second ^ other.second)
