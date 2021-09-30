class Binary_Indexed_Tree_Exception(Exception):
    pass

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
    def __init__(self, L, calc, unit, inv, index=1):
        """ calc を演算とする N 項の Binary Indexed Tree を作成
        calc: 演算 (2変数関数, 可換群)
        unit: 群 calc の単位元 (x+e=e+x=xを満たすe)
        inv : 群 calc の逆元 (1変数関数, x+y(x)=y(x)+x=e をみたす y(x))
        """
        self.calc=calc
        self.unit=unit
        self.inv=inv
        self.index=index

        N=len(L)
        d=max(1,(N-1).bit_length())
        k=2**d

        X=[None]+[unit]*k

        self.num=k
        self.depth=d

        if L:
            for i in range(len(L)):
                p=i+1
                while p<=k:
                    X[p]=self.calc(X[p],L[i])
                    p+=p&(-p)
        self.data=X

    def index_number(self, k, index=1):
        """ 第 k 要素の値を出力する.
        k    : 数列の要素
        index: 先頭の要素の番号
        """
        return self.sum(k,k,index)

    def add(self, k, x, index=1):
        """ 第 k 要素に x を加え, 更新を行う.
        k    : 数列の要素
        x    : 加える値
        index: 先頭の要素の番号
        """
        p=k+(1-index)
        while p<=self.num:
            self.data[p]=self.calc(self.data[p],x)
            p+=p&(-p)

    def update(self, k, x, index=1):
        """ 第 k 要素を x に変え, 更新を行う.
        k: 数列の要素
        x: 更新後の値
        """

        a=self.index_number(k,index)
        y=self.calc(self.inv(a),x)

        self.add(k,y,index)

    def sum(self, From, To, index=1):
        """ 第 From 要素から第 To 要素までの総和を求める.
        ※From!=1を使うならば, 群でなくてはならない.
        From : 始まり
        To   : 終わり
        index: 先頭の要素の番号
        """
        alpha=max(1,From+(1-index))
        beta=min(self.num,To+(1-index))

        if alpha==1:
            return self.__section(beta)
        else:
            return self.calc(self.inv(self.__section(alpha-1)),self.__section(beta))

    def __section(self,x):
        """ B[1]+...+B[x] を求める. """
        S=self.unit
        while x>0:
            S=self.calc(self.data[x],S)
            x-=x&(-x)
        return S

    def all_sum(self):
        return self.data[-1]

    def binary_search(self, cond, index=1):
        """ cond(B[1]+...+B[k]) を満たす最小の k を返す.

        cond: 単調増加

        ※ cond(uint)=True の場合の返り値は index-1
        ※ cond(B[1]+...+B[k]) なる k が存在しない場合の返り値は self.num+index
        """

        if cond(self.unit):
            return index-1

        j=0
        r=self.num
        t=r
        data=self.data
        alpha=self.unit

        for _ in range(self.depth+1):
            if j+t<=self.num:
                beta=self.calc(alpha,data[j+t])
                if not cond(beta):
                    alpha=beta
                    j+=t
            t>>=1

        return j+index

    def __getitem__(self,index):
        if isinstance(index,int):
            return self.index_number(index,self.index)
        else:
            return [self.index_number(t,self.index) for t in index]

    def __setitem__(self,index,val):
        self.update(index,val,self.index)

class Range_Binary_Indexed_Tree():
    def __init__(self, L, calc, unit, inv, index=1):
        """ calc を演算とする N 項の Binary Indexed Tree (区間作用付き) を作成
        calc: 演算 (2変数関数, 可換群)
        unit: 群 calc の単位元 (x+e=e+x=xを満たすe)
        inv : 群 calc の逆元 (1変数関数, x+y(x)=y(x)+x=e をみたす y(x))
        """

        self.bit0=Binary_Indexed_Tree(L, calc, unit, inv, 1)

        self.calc=calc
        self.unit=unit
        self.inv=inv
        self.index=index

        self.num=self.bit0.num
        self.depth=self.bit0.depth

        self.bit1=Binary_Indexed_Tree([unit]*self.num, calc, unit, inv, 1)

    def index_number(self, k, index=1):
        """ 第 k 要素の値を出力する.
        k    : 数列の要素
        index: 先頭の要素の番号
        """
        return self.sum(k,k,index)

    def add(self, k, x, index=1):
        """ 第 k 要素に x を加え, 更新を行う.
        k    : 数列の要素
        x    : 加える値
        index: 先頭の要素の番号
        """

        self.bit0.add(k,x,index)

    def add_range(self, l, r, x, index=1):
        """ 第 l 要素から第 r 要素全てに x を加え, 更新を行う.
        l,r: 更新の範囲
        x: 加算する値
        index: 先頭の要素の番号
        """
        l=max(1,l+(1-index))
        r=min(self.num,r+(1-index))

        self.bit0.add(l, -x*(l-1),index)
        self.bit1.add(l, x, index)

        if r<self.index+self.num-1:
            self.bit0.add(r+1, x*r, index)
            self.bit1.add(r+1, -x, index)

    def update(self, k, x, index=1):
        """ 第 k 要素を x に変え, 更新を行う.
        k: 数列の要素
        x: 更新後の値
        """

        self.bit0.update(k,x,index)

    def sum(self, From, To, index=1):
        """ 第 From 要素から第 To 要素までの総和を求める.
        ※From!=1を使うならば, 群でなくてはならない.
        From : 始まり
        To   : 終わり
        index: 先頭の要素の番号
        """
        alpha=max(1,From+(1-index))
        beta=min(self.num,To+(1-index))

        Y=self.bit0.sum(1,beta,1)+self.bit1.sum(1,beta,1)*beta

        if alpha==1:
            return Y
        else:
            X=self.bit0.sum(1, alpha-1,1)+self.bit1.sum(1, alpha-1,1)*(alpha-1)
            return self.calc(self.inv(X),Y)

    def all_sum(self):
        return self.bit0.data[-1]+self.bit1.data[-1]*self.num

    def binary_search(self, cond, index=1):
        """ cond(B[1]+...+B[k]) を満たす最小の k を返す.

        cond: 単調増加

        ※ cond(uint)=True の場合の返り値は index-1
        ※ cond(B[1]+...+B[k]) なる k が存在しない場合の返り値は self.num+index
        """

        pass

    def __getitem__(self,index):
        if isinstance(index,int):
            return self.index_number(index,self.index)
        else:
            return [self.index_number(t,self.index) for t in index]

    def __setitem__(self,index,val):
        self.update(index,val,self.index)

class Compact_Binary_Indexed_Tree():
    def __init__(self, N, calc, unit, inv, index=1):
        """ calc を演算とする最高の添字が N になるような Compact Binary Indexed Tree を作成
        calc: 演算 (2変数関数, 可換群)
        unit: 群 calc の単位元 (x+e=e+x=xを満たすe)
        inv : 群 calc の逆元 (1変数関数, x+y(x)=y(x)+x=e をみたす y(x))
        """
        self.calc=calc
        self.unit=unit
        self.inv=inv
        self.index=index

        d=max(1,(N+(1-index)-1).bit_length())
        k=2**d

        self.num=k
        self.depth=d
        self.data={}

    def index_number(self, k, index=1):
        """ 第 k 要素の値を出力する.
        k    : 数列の要素
        index: 先頭の要素の番号
        """
        return self.sum(k,k,index)

    def add(self, k, x, index=1):
        """ 第 k 要素に x を加え, 更新を行う.
        k    : 数列の要素
        x    : 加える値
        index: 先頭の要素の番号
        right:「左から」が「右から」になる
        """
        p=k+(1-index)
        while p<=self.num:
            self.data[p]=self.calc(self.data.get(p,self.unit),x)
            p+=p&(-p)

    def update(self, k, x, index=1):
        """ 第 k 要素を x に変え, 更新を行う.
        k: 数列の要素
        x: 更新後の値
        """

        a=self.index_number(k,index)
        y=self.calc(self.inv(a),x)

        self.add(k,y,index)

    def sum(self, From, To, index=1):
        """ 第 From 要素から第 To 要素までの総和を求める.
        ※From!=1を使うならば, 群でなくてはならない.
        From : 始まり
        To   : 終わり
        index: 先頭の要素の番号
        """
        alpha=max(1,From+(1-index))
        beta=min(self.num,To+(1-index))

        if alpha==1:
            return self.__section(beta)
        else:
            return self.calc(self.inv(self.__section(alpha-1)),self.__section(beta))

    def __section(self,x):
        """ B[1]+...+B[x] を求める. """
        S=self.unit
        while x:
            S=self.calc(self.data.get(x,self.unit),S)
            x-=x&(-x)
        return S

    def all_sum(self):
        return self.data.get(self.num,self.unit)

    def binary_search(self, cond, index=1):
        """ cond(B[1]+...+B[k]) を満たす最小の k を返す.

        cond: 単調増加

        ※ cond(uint)=True の場合の返り値は index-1
        ※ cond(B[1]+...+B[k]) なる k が存在しない場合の返り値は self.num+index
        """

        if cond(self.unit):
            return index-1

        j=0
        r=self.num
        t=r
        data=self.data
        alpha=self.unit

        for _ in range(self.depth+1):
            if j+t<=self.num:
                beta=self.calc(alpha,data.get(j+t,self.unit))
                if not cond(beta):
                    alpha=beta
                    j+=t
            t>>=1

        return j+index

    def __getitem__(self,index):
        if isinstance(index,int):
            return self.index_number(index,self.index)
        else:
            return [self.index_number(t,self.index) for t in index]

    def __setitem__(self,index,val):
        self.update(index,val,self.index)
