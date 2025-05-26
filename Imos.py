class Imos_1:
    def __init__(self, N: int):
        """ 区間 0 <= t < N に対する Imos 法のデータ構造を作成する.

        Args:
            N (int): 幅
        """

        self.__lazy = [0] * (N + 1)

    def __len__(self) -> int:
        return len(self.__lazy) - 1

    def add(self, l: int, r: int, x: int = 1):
        """ 閉区間 [l, r] に x を加算する.

        Args:
            l (int): 左端
            r (int): 右端
            x (int, optional): 加算する値. Defaults to 1.
        """

        if l > r:
            return

        if 0 <= l < len(self):
            self.__lazy[l] += x

        if 0 <= r < len(self):
            self.__lazy[r + 1] -= x

    def cumulate(self) -> list[int]:
        """ 累積和を求める.

        Returns:
            list[int]: 累積和
        """

        y = self.__lazy.copy()[:-1]
        for i in range(1, len(self)):
            y[i] += y[i - 1]

        return y

#=================================================
from collections import defaultdict
class Sparse_Imos_1:
    def __init__(self):
        self.dict=defaultdict(int)

    def add(self, l: int, r: int, x: int = 1):
        """ 閉区間 [l,r] に x を加算する.

        Args:
            l (int): 左端
            r (int): 右端
            x (int, optional): 加算する値. Defaults to 1.
        """

        if l > r:
            return

        self.dict[l] += x
        self.dict[r + 1] -= x

    def cumulative_sum(self, since: int, until: int) -> list[tuple[int, int, int]]:
        """ since から until までの累積和を求める.

        Args:
            since (int): 始点
            until (int): 終点

        Returns:
            list[tuple[int, int, int]]: (y, l, r) という形のリスト.
                (y, l, r) は l <= x <= r の範囲においては累積和が y であるということを意味する.
        """

        res: list[tuple[int, int, int]] = []
        S = 0
        t_old = since
        dic = self.dict
        for t in sorted(dic):
            if t > until:
                break

            if dic[t] == 0:
                continue

            if t_old <= t - 1:
                res.append((S, t_old, t - 1))

            S += dic[t]
            t_old = t

        if t_old<=until:
            res.append((S, t_old, until))

        return res

#=================================================
class Linear_Imos_1:
    def __init__(self, N: int):
        """ 長さが N の 1 次式対応 Imos 法クラスのインスタンスを作成する.

        Args:
            N (int): 幅
        """

        # 1 次式を加算する → 累積和は 2 回とる → 遅延配列の長さは (N + 2)
        self.__lazy = [0] * (N + 2)

    def __len__(self) -> int:
        return len(self.__lazy) - 2

    def add(self, l: int, r: int, x: int = 1):
        """ 閉区間 [l, r] に一様に x を加算する.

        Args:
            l (int): 左端
            r (int): 右端
            x (int, optional): 加算する値. Defaults to 1.
        """

        self.add_linear(l, r, x, 0)

    def add_linear(self, l: int, r: int, a: int, b: int):
        """ 閉区間 [l, r] に次のようにして加算する.
        I[l] += a, I[l + 1] += a + b, I[l + 2] += a +2b, ..., I[t] += a + (t - r) b, ...,  I[r] += a + (r - l) b

        Args:
            l (int): 左端
            r (int): 右端
            a (int): 1 次式の定数項
            b (int): 1 次式の傾き
        """

        if l < 0:
            a += b * (-l)
            l = 0

        r = min(r, len(self) - 1)

        if l > r:
            return

        lazy = self.__lazy
        difference = [(l, a), (l + 1, -a + b), (r + 1, -a - (r - l + 1) * b), (r + 2, a + (r - l) * b)]
        for k, x in difference:
            lazy[k] += x

    def add_mountain(self, l: int, m: int, a: int, b: int):
        """ 閉区間 [l, l + 2m] に次のように山型に加算する.
        I[l] += a, I[l + 1] = a + b, I[l + 2] = a + 2b, ..., I[l + m] = a + mb
        I[l + m + 1] += a + (m - 1)b, I[l + m + 2] += a + (m - 2)b, ..., I[l + 2m - 1] += a + b, I[l + 2m] += a

        Args:
            l (int): 左端
            m (int): 山の長さ
            a (int): 定数項
            b (int): 1 次式の傾き
        """
        self.add_linear(l, l + m, a, b)
        self.add_linear(l + m + 1, l + 2 * m, a + (m - 1) * b, -b)

    def add_slide_multiple(self, l: int, k: int, m: int, a: int):
        """ 以下を k 個の整数 t = l, l + 1, ..., l + (k - 1) に対して行う.
        (操作): 長さ m の連続区間 x = t, t + 1, ..., t + (m - 1) に対して, 一様に a を加算する.

        Args:
            l (int): 操作の始点
            k (int): 操作の回数
            m (int): 1 回の操作で加算する項の数
            a (int): 加算する値
        """
        if m <= 0:
            return

        if k >= m:
            self.add_linear(l, l + (m - 2), a, a)
            self.add(l + (m - 1), l + k - 1, a * m)
            self.add_linear(l + k, l + k + m - 1, a * (m - 1), -a)
        else:
            self.add_linear(l, l + (k - 1), a, a)
            self.add(l + k, l + m - 2, a * k)
            self.add_linear(l + m - 1, l + (m - 1) + (k - 1), a * k, -a)

    def cumulate(self) -> list[int]:
        """ 累積和を求める.

        Returns:
            list[int]: 累積和
        """

        y = self.__lazy.copy()[:-2]
        for _ in range(2):
            for i in range(1, len(self)):
                y[i] += y[i - 1]
        return y

#=================================================
class Imos_2:
    def __init__(self, W: int, H: int):
        self.__width = W
        self.__height = H
        self.list=[[0]*(W+1) for _ in range(H+1)]

    @property
    def width(self) -> int:
        return self.__width

    @property
    def height(self) -> int:
        return self.__height

    def add(self, i0: int, j0: int, i1: int, j1: int, x: int = 1):
        """ 閉区間 [i0, j0] x [i1, j1] に x を加算する.

        Args:
            i0 (int): 左端
            j0 (int): 上端
            i1 (int): 右端
            j1 (int): 下端
            x (int, optional): 加算する値. Defaults to 1.
        """

        self.list[i0][j0] += x
        self.list[i0][j1 + 1] -= x
        self.list[i1 + 1][j0] -= x
        self.list[i1 + 1][j1 + 1] += x

    def add_row(self, i: int, x: int):
        """ 第 i 行 (i, *) に x を加える.

        Args:
            i (int): 行番号
            x (int): 加算する値
        """
        self.add(i, 0, i, self.width - 1, x)

    def add_column(self, j: int, x: int):
        """ 第 j 列 (*, j) に x を加える.

        Args:
            j (int): 列番号
            x (int): 加算する値
        """
        self.add(0, j, self.height - 1, j, x)

    def cumulate(self):
        Y=[self.list[i].copy()[:-1] for i in range(self.height)]

        for _ in range(2):
            for i in range(len(Y)):
                y=Y[i]
                for j in range(1,len(y)):
                    y[j]+=y[j-1]
            Y=[list(y) for y in zip(*Y)]
        return Y
