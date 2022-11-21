class Sparse_Binary_Indexed_Tree():
    def __init__(self, N, calc, unit, inv, index=1):
        """ calc を演算とする最高の添字が N になるような Sparse Binary Indexed Tree を作成
        calc: 演算 (2変数関数, 可換群)
        unit: 群 calc の単位元 (x+e=e+x=xを満たすe)
        inv : 群 calc の逆元 (1変数関数, x+inv(x)=inv(x)+x=e をみたす inv(x))
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

        if alpha>beta:
            return self.unit
        elif alpha==1:
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