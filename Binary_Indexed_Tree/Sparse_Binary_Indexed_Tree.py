from typing import TypeVar, Generic, Callable

G = TypeVar('G')
class Sparse_Binary_Indexed_Tree(Generic[G]):
    def __init__(self, N: int, op: Callable[[G, G], G], zero: G, neg: Callable[[G], G]):
        """ op を群 G の演算とつする N 要素を持つ疎 Binary Indexed Tree を生成する.

        Args:
            N (int): 要素数
            op (Callable[[G, G], G]): 群演算
            zero (G): 群 G における単位元 (任意の x in G に対して, x + e = e + x = x となる e in G)
            neg (Callable[[G], G]): x in G における逆元 (x + y = y + x = e となる y) を求める関数
        """

        self.op = op
        self.zero = zero
        self.neg = neg
        self.__N = N
        self.__log = max(N.bit_length() - 1, 1)
        self.data: dict[int, G] = {}

    @property
    def N(self) -> int:
        return self.__N

    @property
    def log(self) -> int:
        return self.__log

    def get(self, k: int) -> G:
        """ 第 k 要素の値を出力する.

        Args:
            k (int): 要素番号

        Returns:
            G: 第 k 要素
        """
        return self.sum(k, k)

    def add(self, k: int, x: G):
        """ 第 k 要素に x を加え, 更新を行う.

        Args:
            k (int): 要素番号
            x (G): 加算する要素
        """

        data = self.data
        op = self.op

        p = k + 1
        while p <= self.N:
            data[p] = op(data.get(p, self.zero), x)
            p += p & (-p)

    def update(self, k: int, x: G):
        """ 第 k 要素を x に変え, 更新を行う.

        Args:
            k (int): 要素番号
            x (G): 変更後の値
        """

        a = self.get(k)
        y = self.op(self.neg(a), x)

        self.add(k, y)

    def sum(self, l: int, r: int) -> G:
        """ 第 l 項から第 r 項までの総和を求める (ただし, l != 0 のときは G が群でなくてはならない).

        Args:
            l (int): 左端
            r (int): 右端

        Returns:
            G: 総和
        """

        l = l + 1 if 0 <= l else 1
        r = r + 1 if r < self.N else self.N

        if l > r:
            return self.zero
        elif l == 1:
            return self.__section(r)
        else:
            return self.op(self.neg(self.__section(l - 1)), self.__section(r))

    def __section(self, x: int) -> G:
        """ B[0] + B[1] + ... + B[x] を求める.

        Args:
            x (int): 右端

        Returns:
            G: 総和
        """

        data = self.data
        op = self.op

        total = self.zero
        while x > 0:
            total = op(data.get(x, self.zero), total)
            x -= x & (-x)
        return total

    def all_sum(self) -> G:
        """ B[0] + B[1] + ... + B[len(B) - 1] を求める.

        Returns:
            G: 総和
        """

        return self.sum(0, self.N - 1)

    def binary_search(self, cond: Callable[[int], bool]) -> int:
        """ cond(B[0] + B[1] + ... + B[k]) が True になる最小の k を止める.

        ※ G は順序群である必要がある.
        ※ cond(zero) = True のとき, 返り値は -1 とする.
        ※ cond(B[0] + ... + B[k]) なる k が (0 <= k < N に) 存在しない場合, 返り値は N とする.

        Args:
            cond (Callable[[int], bool]): 単調増加な条件

        Returns:
            int: cond(B[0] + B[1] + ... + B[k]) が True になる最小の k
        """

        if cond(self.zero):
            return -1

        j = 0
        t = 1 << self.log
        data = self.data
        op = self.op
        alpha = self.zero

        while t > 0:
            if j + t <= self.N:
                beta = op(alpha, data.get(j + t, self.zero))
                if not cond(beta):
                    alpha = beta
                    j += t
            t >>= 1

        return j

    def __getitem__(self, index):
        if isinstance(index, int):
            return self.get(index)
        else:
            return [self.get(t) for t in index]

    def __setitem__(self, index: int, val: G):
        self.update(index, val)

    def __iter__(self):
        for k in range(self.N):
            yield self.sum(k, k)
