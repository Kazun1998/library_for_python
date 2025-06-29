from typing import TypeVar, Generic, Callable

SemiGroup = TypeVar('SemiGroup')
class Sparse_Table(Generic[SemiGroup]):
    """ 参考: https://qiita.com/recuraki/items/0fcbc9e2abbc4fae5f62"""

    def __init__(self, A: list[SemiGroup], op: Callable[[SemiGroup, SemiGroup], SemiGroup]):
        """ 半群 (SemiGroup, op) 上の列 A に関する Sparse Table を構築する.

        Args:
            A (list[SemiGroup]): 半群 (SemiGroup, op) 上の列
            op (Callable[[SemiGroup, SemiGroup], SemiGroup]): 半群上の演算 (x, y) -> xy

        Remark:
            半群 (SemiGroup, op) は結合則, 可換則, 冪等則を満たしていることを要求する.
        """
        self.op = op
        n = len(A)
        depth = max(1, (n - 1).bit_length())

        self.table = [[a for a in A]]
        for k in range(1, depth):
            prev_row = self.table[-1]
            m = 1 << (k - 1)
            row = [op(prev_row[i], prev_row[i + m]) for i in range(n - 2 * m + 1)]
            self.table.append(row)

    def __len__(self) -> int:
        return len(self.table[0])

    def product(self, l: int, r: int, default: SemiGroup = None, left_close: bool = True, right_close: bool = True) -> SemiGroup:
        """ 総積 A_l A_{l+1} ... A_r を求める. ただし, 空積は default とする.

        Args:
            l (int): 左端
            r (int): 右端
            default (SemiGroup, optional): 空積のときの返り値. Defaults to None.
            left_close (bool, optional): False にすると, 左端が開になる. Defaults to True.
            right_close (bool, optional): False にすると, 右端が開になる. Defaults to True.

        Returns:
            SemiGroup: 総積
        """

        # 区間を左半開区間に変換する.
        if not left_close:
            l += 1

        if right_close:
            r += 1

        length = r - l
        if length == 1:
            # 単項
            return self.table[0][l]
        elif length <= 0:
            # 空積
            return default

        lv = (length - 1).bit_length() - 1
        row = self.table[lv]
        return self.op(row[l], row[r - pow(2, lv)])
