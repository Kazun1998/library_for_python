from typing import TypeVar, Generic, Callable

SemiGroup = TypeVar('SemiGroup')
class Disjoint_Sparse_Table(Generic[SemiGroup]):
    # 参考: https://ei1333.github.io/library/structure/others/disjoint-sparse-table.cpp.html

    def __init__(self, A: list[SemiGroup], op: Callable[[SemiGroup, SemiGroup], SemiGroup]):
        """ 半群 (SemiGroup, op) 上の列 A に関する Sparse Table を構築する.

        Args:
            A (list[SemiGroup]): 半群 (SemiGroup, op) 上の列
            op (Callable[[SemiGroup, SemiGroup], SemiGroup]): 半群上の演算 (x, y) -> xy

        Remark:
            半群 (SemiGroup, op) は結合則, 可換則, 冪等則を満たしていることを要求する.
        """

        self.__op = op
        n = len(A)
        height = max(1, (n - 1).bit_length())

        self.table: list[list[SemiGroup]] = [[None] * n for _ in range(height)]

        row = self.table[0]
        for i in range(n):
            row[i] = A[i]

        shift = 1
        for i in range(1, height):
            shift <<= 1
            row = self.table[i]

            for j in range(0, n, 2 * shift):
                t = min(j + shift, n)
                row[t - 1] = A[t-1]

                for k in range(t - 2, j - 1, -1):
                    row[k] = op(A[k], row[k + 1])

                if n <= t:
                    break

                row[t] = A[t]
                r = min(t + shift, n)

                for k in range(t + 1, r):
                    row[k] = op(row[k - 1], A[k])

    @property
    def op(self) -> Callable[[SemiGroup, SemiGroup], SemiGroup]:
        return self.__op

    def __len__(self) -> int:
        return len(self.table[0])

    def product(self, l: int, r: int, left_close: bool = True, right_close: bool = True, default: bool = None) -> SemiGroup:
        """ 総積 A_l A_{l+1} ... A_r を求める. ただし, 空積は default とする.

        Args:
            l (int): 左端
            r (int): 右端
            left_close (bool, optional): False にすると, 左端が開になる. Defaults to True.
            right_close (bool, optional): False にすると, 右端が開になる. Defaults to True.
            default (SemiGroup, optional): 空積のときの返り値. Defaults to None.

        Returns:
            SemiGroup: 総積
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
