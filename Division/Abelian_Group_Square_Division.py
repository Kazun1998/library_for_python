from typing import TypeVar, Generic, Callable

G = TypeVar('G')
class Abelian_Group_Square_Division(Generic[G]):
    def __init__(self, data: list[G], op: Callable[[G, G], G], zero: G, neg: Callable[[G], G]):
        """ 可換群 G の列に対する平方分割の場を設定する.

        Args:
            data (list[G]): G の列
            op (Callable[[G, G], G]): G 上の演算
            zero (G): G の単位元
            neg (Callable[[G], G]): G 上の逆元関数
        """

        self.__op = op
        self.__zero = zero
        self.__neg = neg

        n = len(data)
        self.__bucket_size = int(pow(n, 0.5) + 1)
        self.__bucket_number = (n - 1) // self.bucket_size + 1

        upper = self.__upper = [zero] * self.bucket_number
        lower = self.__lower = [zero] * self.bucket_number * self.bucket_size

        for i in range(n):
            lower[i] = data[i]

            j = i // self.bucket_size
            upper[j] = op(upper[j], lower[i])

    @property
    def zero(self) -> G:
        return self.__zero

    @property
    def bucket_number(self) -> int:
        return self.__bucket_number

    @property
    def bucket_size(self) -> int:
        return self.__bucket_size

    def add(self, k: int, x: G):
        """ 第 k 要素に x を追加する.

        Args:
            k (int): 要素の場所
            x (G): 追加する要素
        """

        self.__lower[k] = self.__op(self.__lower[k], x)

        j = k // self.bucket_size
        self.__upper[j] = self.__op(self.__upper[j], x)

    def update(self, k: int, y: G):
        """ 第 k 要素を y に変更する.

        Args:
            k (int): 要素の場所
            y (G): 変更後の値
        """

        diff = self.__op(self.__neg(self.__lower[k]), y)
        self.add(k, diff)

    def sum(self, l: int, r: int, left_close: bool = True, right_close: bool = True) -> G:
        """ 第 l 要素から第 r 要素の総和を求める.

        Args:
            l (int): 左端
            r (int): 右端
            left_close (bool, optional): False にすると, 左端が開区間になる. Defaults to True.
            right_close (bool, optional): False になると, 右端が開区間になる. Defaults to True.

        Returns:
            G: 総和
        """

        if not left_close:
            l += 1

        if not right_close:
            r -= 1

        b = self.bucket_size
        op = self.__op
        lower = self.__lower
        upper = self.__upper
        res = self.zero

        if l // b == r // b:
            for i in range(l, r + 1):
                res = op(res, lower[i])
            return res

        while l % b != 0:
            res = op(res, lower[l])
            l += 1

        while l + (b - 1) <= r:
            res = op(res, upper[l // b])
            l += b

        while l <= r:
            res = op(res, lower[l])
            l += 1

        return res

    def __getitem__(self, k: int) -> G:
        return self.__lower[k]
