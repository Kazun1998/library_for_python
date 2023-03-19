class Binary_Indexed_Tree():
    def __init__(self, L, op, zero, neg):
        """ op を演算とする N 項の Binary Indexed Tree を作成
        op: 演算 (2変数関数, 可換群)
        zero: 群 op の単位元 (x+e=e+x=x を満たす e)
        neg : 群 op の逆元 (1変数関数, x+neg(x)=neg(x)+x=e をみたす neg(x))
        """
        self.op=op
        self.zero=zero
        self.neg=neg
        self.N=N=len(L)
        self.log=N.bit_length()-1

        X=[zero]*(N+1)

        for i in range(N):
            p=i+1
            X[p]=op(X[p],L[i])
            q=p+(p&(-p))
            if q<=N:
                X[q]=op(X[q], X[p])
        self.data=X

    def get(self, k):
        """ 第 k 要素の値を出力する.

        k    : 数列の要素
        index: 先頭の要素の番号
        """
        return self.sum(k, k)

    def add(self, k, x):
        """ 第 k 要素に x を加え, 更新を行う.

        k    : 数列の要素
        x    : 加える値
        """
        data=self.data; op=self.op
        p=k+1
        while p<=self.N:
            data[p]=op(self.data[p], x)
            p+=p&(-p)

    def update(self, k, x):
        """ 第 k 要素を x に変え, 更新を行う.

        k: 数列の要素
        x: 更新後の値
        """

        a=self.get(k)
        y=self.op(self.neg(a), x)

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
            return self.zero
        elif l==1:
            return self.__section(r)
        else:
            return self.op(self.neg(self.__section(l-1)), self.__section(r))

    def __section(self, x):
        """ B[0]+...+B[x] を求める. """
        data=self.data; op=self.op
        S=self.zero
        while x>0:
            S=op(data[x], S)
            x-=x&(-x)
        return S

    def all_sum(self):
        return self.sum(0, self.N-1)

    def binary_search(self, cond):
        """ cond(B[0]+...+B[k]) が True となるような最小の k を返す.

        cond: 単調増加

        ※ cond(zero)=True の場合の返り値は -1 とする.
        ※ cond(B[0]+...+B[k]) なる k が (0<=k<N に) 存在しない場合の返り値は N とする.
        """

        if cond(self.zero):
            return -1

        j=0
        r=self.N
        t=1<<self.log
        data=self.data; op=self.op
        alpha=self.zero

        while t>0:
            if j+t<=self.N:
                beta=op(alpha, data[j+t])
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
