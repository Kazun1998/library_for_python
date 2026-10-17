""" Bitset 説明書
事前に N (Biset のサイズ) と __bit_size (各ブロックごとに収めるサイズ) を決めなくてはいけない.

[おすすめ]
N=10^5, __bit_size=N//k (4<=k<=10)
N=3000, __bit_size=63?

※ count, len を使いたい場合は __bit_size=63 でないと使えない!!!
"""

class Bitset:
    @classmethod
    def popcount(cls, n: int) -> int:
        n -= ((n >> 1) & 0x5555555555555555)
        n = (n & 0x3333333333333333) + ((n >> 2) & 0x3333333333333333)
        n = (n + (n >> 4)) & 0x0f0f0f0f0f0f0f0f
        n += ((n >> 8) & 0x00ff00ff00ff00ff)
        n += ((n >> 16) & 0x0000ffff0000ffff)
        n += ((n >> 32) & 0x00000000ffffffff)
        return n & 0x7f

    # ※ 事前に設定しておくこと!!!
    N = 3000
    __bit_size = 63 * 1
    # ここまで

    __block = (N + __bit_size - 1) // __bit_size

    __msk_b = (1 << __bit_size) - 1
    __msk_s = (1 << (N % __bit_size)) - 1

    __on = [1 << i for i in range(__bit_size)]
    __off = [0] * __bit_size
    for k in range(__bit_size):
        __off[k] = ((1<<__bit_size) - 1) ^ (1 << k)
    del k

    def __init__(self, A: list[int] = None):
        """ A にある要素からなる Bitset を生成する.

        Args:
            A (list[int], optional): 初期値からなるリスト. Defaults to None.
        """

        self.__bit = [0] * Bitset.__block

        if A is None:
            return

        for a in A:
            self.set(a, 1)

    def __len__(self) -> int:
        res = 0
        for bit in self.__bit:
            res += Bitset.popcount(bit)
        return res

    def __bool__(self) -> bool:
        return self.any()

    def __str__(self) -> str:
        return str([x for x in range(Bitset.N) if self[x]])

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({str(self)})"

    def __contains__(self, index: int) -> bool:
        k, i = divmod(index, Bitset.__bit_size)
        return bool((self.__bit[k] >> i) & 1)

    __getitem__ = __contains__

    def __setitem__(self, index: int, value: int):
        self.set(index, value)

    def set(self, index: int = None, value: int = 1):
        """ 第 index 要素を value (0 or 1) に変更する. ただし, index = None のときは, 全ての要素を変更する.

        Args:
            index (int, optional): 要素番号. Defaults to None.
            value (int, optional): 変更後の値. Defaults to 1.
        """

        if index is None:
            if value:
                self.__bit[-1] = Bitset.__msk_s
                for k in range(Bitset.__block - 1):
                    self.__bit[k] = Bitset.__msk_b
            else:
                for k in range(Bitset.__block):
                    self.__bit[k] = 0
        else:
            k, i = divmod(index, Bitset.__bit_size)
            if value:
                self.__bit[k] |= Bitset.__on[i]
            else:
                self.__bit[k] &= Bitset.__off[i]

    def reset(self, index: int = None):
        """ 第 index 要素を 0 にする. ただし, index = None のときは全ての要素を 0 にする.

        Args:
            index (int, optional): 要素番号. Defaults to None.
        """
        self.set(index, value = 0)

    def flip(self, index: int = None):
        """ 第 index 要素の値を切り替える. ただし, index = None のときは全ての要素を切り替える.

        Args:
            index (int, optional): 要素番号. Defaults to None.
        """

        if index is None:
            for k in range(Bitset.__block - 1):
                self.__bit[k] = self.__bit[k] ^ Bitset.__msk_b

            if self.N % Bitset.__bit_size:
                self.__bit[-1] = self.__bit[-1] ^ Bitset.__msk_s
            else:
                self.__bit[-1] = self.__bit[-1] ^ Bitset.__msk_b
        else:
            k, i = divmod(index, Bitset.__bit_size)
            self.__bit[k] ^= Bitset.__on[i]

    test = __contains__

    def any(self) -> bool:
        return any(bit for bit in self.__bit)

    def all(self) -> bool:
        if not all(self.__bit[k] == Bitset.__msk_b for k in range(Bitset.__block - 1)):
            return False

        if self.N % Bitset.__bit_size:
            return self.__bit[-1] == Bitset.__msk_s
        else:
            return self.__bit[-1] == Bitset.__msk_b

    def __iand__(self, other: "Bitset"):
        for k in range(Bitset.__block):
            self.__bit[k] &= other.__bit[k]
        return self

    def __and__(self, other: "Bitset") -> "Bitset":
        X = self.copy()
        X &= other
        return X

    def __ior__(self, other: "Bitset"):
        for k in range(Bitset.__block):
            self.__bit[k] |= other.__bit[k]
        return self

    def __or__(self, other: "Bitset") -> "Bitset":
        X = self.copy()
        X |= other
        return X

    def __ixor__(self, other):
        for k in range(Bitset.__block):
            self.__bit[k]^=other.__bit[k]
        return self

    def __xor__(self, other: "Bitset") -> "Bitset":
        X = self.copy()
        X ^= other
        return X

    def __eq__(self, other: "Bitset") -> bool:
        for k in range(Bitset.__block):
            if self.__bit[k] != other.__bit[k]:
                return False
        return True

    def __neq__(self, other: "Bitset") -> bool:
        return not(self == other)

    def copy(self):
        X = Bitset()
        X.__bit=self.__bit.copy()
        return X

    count = __len__
