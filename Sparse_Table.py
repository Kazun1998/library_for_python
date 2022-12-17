class Sparse_Table:
    """ 参考: https://qiita.com/recuraki/items/0fcbc9e2abbc4fae5f62"""

    def __init__(self, A, op):
        """ A の演算 op に対する Sparse Table を生成する.

        A: list
        op: 二項演算
        (op は結合則, 可換則, 冪等速を満たしていることを要求する)
        """

        self.op=op
        self.N=N=len(A)
        self.depth=max(1,(N-1).bit_length())

        self.table=[[a for a in A]]
        for k in range(1, self.depth):
            tab=self.table[-1]
            m=1<<(k-1)
            B=[op(tab[i], tab[i+m]) for i in range(N-2*m+1)]
            self.table.append(B)

    def product(self, l, r, default=None, left_close=True, right_close=True):
        """ l<=i<=r に対する積を生成する.

        """

        if not left_close:
            l+=1

        if right_close:
            r+=1

        length=r-l
        if length==1:
            return self.table[0][l]
        elif length<=0:
            return default

        lv=(length-1).bit_length()-1
        tab=self.table[lv]
        return self.op(tab[l], tab[r-(2**lv)])
