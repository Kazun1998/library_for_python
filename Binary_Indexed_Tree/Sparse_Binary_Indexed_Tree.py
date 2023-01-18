class Sparse_Binary_Indexed_Tree():
    def __init__(self, N, op, unit, inv):
        """ calc を演算とする最高の添字が N になるような Sparse Binary Indexed Tree を作成
        calc: 演算 (2変数関数, 可換群)
        unit: 群 calc の単位元 (x+e=e+x=xを満たすe)
        inv : 群 calc の逆元 (1変数関数, x+inv(x)=inv(x)+x=e をみたす inv(x))
        """
        self.op=op
        self.unit=unit
        self.inv=inv
        self.N=N
        self.log=max(N.bit_length()-1, 1)
        self.data={}

    def get(self, k):
        """ 第 k 要素の値を出力する.
        k    : 数列の要素
        index: 先頭の要素の番号
        """
        return self.sum(k,k)

    def add(self, k, x):
        """ 第 k 要素に x を加え, 更新を行う.
        k    : 数列の要素
        x    : 加える値
        """

        data=self.data; op=self.op
        p=k+1
        while p<=self.N:
            data[p]=op(data.get(p, self.unit), x)
            p+=p&(-p)

    def update(self, k, x):
        """ 第 k 要素を x に変え, 更新を行う.
        k: 数列の要素
        x: 更新後の値
        """

        a=self.get(k)
        y=self.op(self.inv(a), x)

        self.add(k,y)

    def sum(self, l, r):
        """ 第 l 要素から第 r 要素までの総和を求める.
        ※ l != 0 を使うならば, 群でなくてはならない.
        l: 始まり
        r: 終わり
        """

        l=l+1 if 0<=l else 1
        r=r+1 if r<self.N else self.N

        if l>r:
            return self.unit
        elif l==1:
            return self.__section(r)
        else:
            return self.op(self.inv(self.__section(l-1)), self.__section(r))

    def __section(self, x):
        """ B[0]+...+B[x] を求める. """
        data=self.data; op=self.op
        S=self.unit
        while x>0:
            S=op(data.get(x, self.unit), S)
            x-=x&(-x)
        return S

    def all_sum(self):
        return self.sum(0, self.N-1)

    def binary_search(self, cond):
        """ cond(B[0]+...+B[k]) が True となるような最小の k を返す.

        cond: 単調増加

        ※ cond(unit)=True の場合の返り値は -1 とする.
        ※ cond(B[0]+...+B[k]) なる k が (0<=k<N に) 存在しない場合の返り値は N とする.
        """

        if cond(self.unit):
            return -1

        j=0
        r=self.N
        t=1<<self.log
        data=self.data; op=self.op
        alpha=self.unit

        while t>0:
            if j+t<=self.N:
                beta=op(alpha, data.get(j+t, self.unit))
                if not cond(beta):
                    alpha=beta
                    j+=t
            t>>=1

        return j

    def __getitem__(self, index):
        if isinstance(index, int):
            return self.get(index)
        else:
            return [self.get(t) for t in index]

    def __setitem__(self, index, val):
        self.update(index, val)

    def __iter__(self):
        for k in range(self.N):
            yield self.sum(k, k)

