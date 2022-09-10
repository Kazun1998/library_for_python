from Binary_Indexed_Tree import Binary_Indexed_Tree

class Range_Binary_Indexed_Tree():
    def __init__(self, L, calc, unit, inv, mul, index=1):
        """ calc を演算とする N 項の Binary Indexed Tree (区間作用付き) を作成
        calc: 演算 (2変数関数, 可換群)
        unit: 群 calc の単位元 (x+e=e+x=xを満たすe)
        inv : 群 calc の逆元 (1変数関数, x+inv(x)=inv(x)+x=e をみたす inv(x))
        mul: r を整数, x を可換群の元としたときの mul(r,x):=r*x
        """

        self.bit0=Binary_Indexed_Tree(L, calc, unit, inv, index)

        self.calc=calc
        self.unit=unit
        self.inv=inv
        self.mul=mul
        self.index=index

        self.num=self.bit0.num
        self.depth=self.bit0.depth

        self.bit1=Binary_Indexed_Tree([unit]*self.num, calc, unit, inv, index)

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

        inv=self.inv; mul=self.mul

        self.bit0.add(l, inv(mul(l-1,x)),index)
        self.bit1.add(l, x, index)

        if r<self.index+self.num-1:
            self.bit0.add(r+1, mul(r,x), index)
            self.bit1.add(r+1, inv(x), index)

    def update(self, k, x, index=1):
        """ 第 k 要素を x に変え, 更新を行う.
        k: 数列の要素
        x: 更新後の値
        """

        self.bit0.update(k,x,index)

    def sum(self, l, r, index=1):
        """ 第 l 要素から第 r 要素までの総和を求める.
        ※ l != index ならば, 群でなくてはならない.
        l : 始まり
        r   : 終わり
        index: 先頭の要素の番号
        """
        alpha=max(1, l+(1-index))
        beta=min(self.num, r+(1-index))

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

from operator import add,neg,mul
B=Range_Binary_Indexed_Tree([0]*10, add, 0, neg, mul ,1)

