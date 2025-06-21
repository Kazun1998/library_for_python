from typing import TypeVar, Generic, Callable

S = TypeVar('S')
class Disjoint_Sparse_Table(Generic[S]):
    # 参考: https://ei1333.github.io/library/structure/others/disjoint-sparse-table.cpp.html

    def __init__(self, A: list[S], op: Callable[[S, S], S]):
        """ 半群 S 上の列 A に対する Disjoint Sparse Table を生成する.

        Args:
            A (list[S]): S 上の列
            op (Callable[[S, S], S]): S の演算 (x, y) → xy
        """

        self.__op = op
        self.__size = N = len(A)
        height = max(1, (N - 1).bit_length())

        self.table: list[list[S]] = [[None] * self.size for _ in range(height)]

        row = self.table[0]
        for i in range(self.size):
            row[i] = A[i]

        shift = 1
        for i in range(1, height):
            shift <<= 1
            row = self.table[i]

            for j in range(0, N, 2 * shift):
                t = min(j + shift, N)
                row[t - 1] = A[t-1]

                for k in range(t - 2, j - 1, -1):
                    row[k] = op(A[k], row[k + 1])

                if N <= t:
                    break

                row[t] = A[t]
                r = min(t + shift, N)

                for k in range(t + 1, r):
                    row[k] = op(row[k - 1], A[k])

    @property
    def op(self) -> Callable[[S, S], S]:
        return self.__op

    @property
    def size(self) -> int:
        return self.__size

    def product(self, l: int, r: int, left_close: bool = True, right_close: bool = True, default: bool = None) -> S:
        """ 積 A_l A_{l+1} ... A_r を求める.

        Args:
            l (int): 左端
            r (int): 右端
            left_close (bool, optional): False にすると, 左端が開区間になる. Defaults to True.
            right_close (bool, optional): False にすると, 右端が開区間になる. Defaults to True.
            default (bool, optional): 区間が空の場合の返り値. Defaults to None.

        Returns:
            S: 積 A_l A_{l+1} ... A_r
        """
        if not left_close:
            l += 1

        if not right_close:
            r -= 1

        if l == r:
            return self.table[0][l]
        elif l > r:
            return default

        p = (l ^ r).bit_length()-1
        row = self.table[p]
        return self.op(row[l], row[r])
