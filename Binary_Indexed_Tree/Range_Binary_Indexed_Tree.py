from Binary_Indexed_Tree import Binary_Indexed_Tree

class Range_Binary_Indexed_Tree():
    def __init__(self, L, op, zero, neg, mul):

        self.op = op
        self.zero = zero
        self.neg = neg
        self.mul = mul
        self.N = len(L)

        self.bit0 = Binary_Indexed_Tree(L, op, zero, neg)
        self.bit1 = Binary_Indexed_Tree([zero]*len(L), op, zero, neg)

    def get(self, k):
        """ 第 k 要素の値を出力する.

        k    : 数列の要素
        """
        return self.sum(k, k)

    def add(self, k, x):
        """ 第 k 要素に x を加え, 更新を行う.
        k    : 数列の要素
        x    : 加える値
        index: 先頭の要素の番号
        """
        self.bit0.add(k, x)

    def update(self, k, x):
        self.bit0.update(k, x)

    def add_range(self, l, r, x):
        """ 第 l 要素から第 r 要素までに一様に x を加える.

        Args:
            l (int): 左端
            r (int): 右端
            x:
        """

        self.bit0.add(l, self.neg(self.mul(l, x)))
        self.bit1.add(l, x)
        if r < self.N - 1:
            self.bit0.add(r + 1, self.mul(r + 1, x))
            self.bit1.add(r + 1, self.neg(x))

    def sum(self, l, r):
        """ 第 l 要素から第 r 要素までの総和を求める.
        ※ l != index ならば, 群でなくてはならない.
        l : 始まり
        r   : 終わり
        index: 先頭の要素の番号
        """
        if l > 0:
            return self.__section(r) - self.__section(l - 1)
        else:
            return self.__section(r)

    def __section(self, k):
        return self.bit0.sum(0, k) + self.mul(k + 1, self.bit1.sum(0, k))

    def all_sum(self):
        return self.sum(0, self.N - 1)

    def __getitem__(self, index):
        if isinstance(index, int):
            return self.get(index)
        else:
            return [self.get(t) for t in index]

    def __setitem__(self, index, value):
        self.update(index, value)

    def __iter__(self):
        for ind in range(self.N):
            yield self.sum(ind, ind)
