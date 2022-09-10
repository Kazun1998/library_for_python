"""
Note:各群演算に関する関数と単位元
[和]
calc=lambda x,y:x+y
unit=0

[積 (群)]
calc=lambda x,y:x*y
unit=1

[Bit Xor]
calc=lambda x,y:x^y
unit=0

[集合の対称差]
calc=lambda x,y:x^y
unit=set()
"""

class Binary_Indexed_Tree():
    def __init__(self, L, calc, unit, inv):
        """ calc を演算とする N 項の Binary Indexed Tree を作成
        calc: 演算 (2変数関数, 可換群)
        unit: 群 calc の単位元 (x+e=e+x=xを満たすe)
        inv : 群 calc の逆元 (1変数関数, x+inv(x)=inv(x)+x=e をみたす inv(x))
        """
        self.calc=calc
        self.unit=unit
        self.inv=inv

        N=len(L)
        d=max(1, (N-1).bit_length())
        k=2**d

        X=[None]+[unit]*k

        self.num=k
        self.depth=d

        for i in range(N):
            p=i+1
            while p<=k:
                X[p]=self.calc(X[p],L[i])
                p+=p&(-p)
        self.data=X

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
        index: 先頭の要素の番号
        """
        data=self.data; calc=self.calc
        p=k+1
        while p<=self.num:
            data[p]=calc(self.data[p],x)
            p+=p&(-p)

    def update(self, k, x):
        """ 第 k 要素を x に変え, 更新を行う.
        k: 数列の要素
        x: 更新後の値
        """

        a=self.get(k)
        y=self.calc(self.inv(a),x)

        self.add(k,y)

    def sum(self, l, r):
        """ 第 l 要素から第 r 要素までの総和を求める.
        ※ l != 0 を使うならば, 群でなくてはならない.
        l: 始まり
        r: 終わり
        """
        l=max(1, l+1)
        r=min(self.num, r+1)

        if l>r:
            return self.unit
        elif l==1:
            return self.__section(r)
        else:
            return self.calc(self.inv(self.__section(l-1)),self.__section(r))

    def __section(self,x):
        """ B[0]+...+B[x] を求める. """
        data=self.data; calc=self.calc
        S=self.unit
        while x>0:
            S=calc(data[x],S)
            x-=x&(-x)
        return S

    def all_sum(self):
        return self.data[-1]

    def binary_search(self, cond):
        """ cond(B[0]+...+B[k]) を満たす最小の k を返す.

        cond: 単調増加

        ※ cond(unit)=True の場合の返り値は -1
        ※ cond(B[1]+...+B[k]) なる k が存在しない場合の返り値は self.num
        """

        if cond(self.unit):
            return -1

        j=0
        r=self.num
        t=r
        data=self.data; calc=self.calc
        alpha=self.unit

        for _ in range(self.depth+1):
            if j+t<=self.num:
                beta=calc(alpha,data[j+t])
                if not cond(beta):
                    alpha=beta
                    j+=t
            t>>=1

        return j

    def __getitem__(self,index):
        if isinstance(index,int):
            return self.get(index)
        else:
            return [self.get(t) for t in index]

    def __setitem__(self,index,val):
        self.update(index,val)

    def __iter__(self):
        for k in range(self.num):
            yield self.sum(k,k)
