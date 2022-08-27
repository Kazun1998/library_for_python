"""
Note:各演算に関する関数と単位元

[和]
calc=lambda x,y:x+y
unit=0

[積]
calc=lambda x,y:x*y
unit=1

[Bit Or]
calc=lambda x,y:x|y
unit=0

[Bit And]
calc=lambda x,y:x&y
unit=(※任意の要素xでx<2**kが保証されているとき,単位元として2**k-1が取れる.)

[Bit Xor]
calc=lambda x,y:x^y
unit=0

[最小値]
calc=lambda x,y:min(x,y)
unit=float("inf")

[最大値]
calc=lambda x,y:max(x,y)
unit=-float("inf")

[集合の和]
calc=lambda x,y:x|y
unit=set()

[集合の積]
calc=lambda x,y:x&y
unit=(全体の集合(場合による))

[集合の対称差]
calc=lambda x,y:x^y
unit=set()
"""

class Segment_Tree():
    """
    このプログラム内は1-index
    """

    def __init__(self,L,calc,unit,index):
        """calcを演算とするリストLのSegment Treeを作成

        calc:演算(2変数関数,モノイド)
        unit:モノイドcalcの単位元 (xe=ex=xを満たすe)
        index:数列の第1要素のindex
        """
        self.calc=calc
        self.unit=unit
        self.index=index

        N=len(L)
        d=max(1,(N-1).bit_length())
        k=1<<d

        self.data=[unit]*k+L+[unit]*(k-len(L))
        self.N=k
        self.depth=d

        for i in range(k-1,0,-1):
            self.data[i]=self.calc(self.data[i<<1],self.data[i<<1|1])

    def get(self,k,index=1):
        """第k要素を取得
        """
        assert 0<=k-index<self.N,"添字が範囲外"
        return self.data[k-index+self.N]

    def update(self,k,x,index=1):
        """第k要素をxに変え,更新を行う.

        k:数列の要素
        x:更新後の値
        """
        assert 0<=k-index<self.N,"添字が範囲外"
        m=(k-index)+self.N
        self.data[m]=x

        while m>1:
            m>>=1
            self.data[m]=self.calc(self.data[m<<1],self.data[m<<1|1])

    def product(self,From,To,index=1,left_closed=True,right_closed=True):
        L=(From-index)+self.N+(not left_closed)
        R=(To-index)+self.N+(right_closed)

        vL=self.unit
        vR=self.unit

        while L<R:
            if L&1:
                vL=self.calc(vL,self.data[L])
                L+=1

            if R&1:
                R-=1
                vR=self.calc(self.data[R],vR)

            L>>=1
            R>>=1

        return self.calc(vL,vR)

    def all_product(self):
        return self.data[1]

    def max_right(self,left,cond,index=1):
        """以下の2つをともに満たすxの1つを返す.\n
        (1) x=left or cond(data[left]*data[left+1]*...*data[x-1]):True
        (2) x=N+index or cond(data[left]*data[left+1]*...*data[x]):False
        ※condが単調減少の時,cond(data[left]*...*data[x-1])を満たす最大のxとなる.

        cond:関数(引数が同じならば結果も同じ)
        cond(unit):True
        index<=left<=r<n+index
        """
        left-=index

        assert 0<=left<=self.N,"添字が範囲外"
        assert cond(self.unit),"単位元が条件を満たさない."

        if left==self.N:
            return self.N+index

        left+=self.N-(index-1)
        sm=self.unit

        calc=self.calc
        first=True
        while first or (left & (-left))!=left:
            first=False
            while left%2==0:
                left>>=1
            if not cond(calc(sm,self.data[left])):
                while left<self.N:
                    left<<=1
                    if cond(self.calc(sm,self.data[left])):
                        sm=self.calc(sm,self.data[left])
                        left+=1
                return left-self.N+index
            sm=self.calc(sm,self.data[left])
            left+=1
        return self.N+index

    def min_left(self,right,cond,index=1):
        """以下の2つをともに満たすyの1つを返す.\n
        (1) y=right or cond(data[y]*data[y+1]*...*data[right]):True
        (2) y=index or cond(data[y-1]*data[y]*...*data[right]):False
        ※condが単調減少の時,cond(data[y]*...*data[right-1])を満たす最大のyとなる.

        cond:関数(引数が同じならば結果も同じ)
        cond(unit):True
        index<=left<=r<n+index
        """
        right-=index

        assert 0<=right<=self.N,"添字が範囲外"
        assert cond(self.unit),"単位元が条件を満たさない."

        if right==0:
            return index

        right+=self.N
        sm=self.unit

        calc=self.calc
        first=1
        while first or (right & (-right))!=right:
            first=0
            right-=1
            while right>1 and right&1:
                right>>=1

            if not cond(calc(self.data[right],sm)):
                while right<self.N:
                    right=2*right+1
                    if cond(calc(self.data[right],sm)):
                        sm=calc(self.data[right],sm)
                        right-=1
                return right+1-self.N+index
            sm=calc(self.data[right],sm)
        return index

    def __getitem__(self,k):
        return self.get(k,self.index)

    def __setitem__(self,k,x):
        return self.update(k,x,self.index)
