class Segment_Tree():
    def __init__(self, L, calc, unit):
        """ calc を演算とするリスト L の Segment Tree を作成

        calc: 演算 (2変数関数, Monoid)
        unit: Monoid calc の単位元 (xe=ex=xを満たすe)
        """
        self.calc=calc
        self.unit=unit

        N=len(L)
        d=max(1,(N-1).bit_length())
        k=1<<d

        self.data=data=[unit]*k+L+[unit]*(k-len(L))
        self.N=k
        self.depth=d

        for i in range(k-1,0,-1):
            data[i]=calc(data[i<<1], data[i<<1|1])

    def get(self, k):
        """ 第 k 要素を取得
        """
        assert 0<=k<self.N,"添字が範囲外"
        return self.data[k+self.N]

    def update(self, k, x):
        """第k要素をxに変え,更新を行う.

        k:数列の要素
        x:更新後の値
        """
        assert 0<=k<self.N,"添字が範囲外"
        m=k+self.N

        data=self.data; calc=self.calc
        data[m]=x

        while m>1:
            m>>=1
            data[m]=calc(data[m<<1], data[m<<1|1])

    def product(self, l, r, left_closed=True,right_closed=True):
        L=l+self.N+(not left_closed)
        R=r+self.N+(right_closed)

        vL=self.unit
        vR=self.unit

        data=self.data; calc=self.calc
        while L<R:
            if L&1:
                vL=calc(vL, data[L])
                L+=1

            if R&1:
                R-=1
                vR=calc(data[R], vR)

            L>>=1
            R>>=1

        return calc(vL,vR)

    def all_product(self):
        return self.data[1]

    def max_right(self, left, cond):
        """ 以下の2つをともに満たす x の1つを返す.\n
        (1) r=left or cond(data[left]*data[left+1]*...*data[r-1]): True
        (2) r=N or cond(data[left]*data[left+1]*...*data[r]): False
        ※ cond が単調減少の時, cond(data[left]*...*data[r-1]) を満たす最大の r となる.

        cond:関数(引数が同じならば結果も同じ)
        cond(unit): True
        0<=left<=N
        """

        assert 0<=left<=self.N,"添字が範囲外"
        assert cond(self.unit),"単位元が条件を満たさない."

        if left==self.N:
            return self.N

        left+=self.N
        sm=self.unit

        calc=self.calc; data=self.data
        first=True

        while first or (left & (-left))!=left:
            first=False
            while left%2==0:
                left>>=1
            if not cond(calc(sm, data[left])):
                while left<self.N:
                    left<<=1
                    if cond(calc(sm, data[left])):
                        sm=calc(sm, data[left])
                        left+=1
                return left-self.N
            sm=calc(sm, data[left])
            left+=1
        return self.N

    def min_left(self, right, cond):
        """ 以下の2つをともに満たす y の1つを返す.\n
        (1) l=right or cond(data[l]*data[l+1]*...*data[right-1]): True
        (2) l=0 or cond(data[l-1]*data[l]*...*data[right-1]): False
        ※ cond が単調増加の時, cond(data[l]*...*data[right-1]) を満たす最小の l となる.

        cond: 関数(引数が同じならば結果も同じ)
        cond(unit): True
        0<=right<=N
        """
        assert 0<=right<=self.N,"添字が範囲外"
        assert cond(self.unit),"単位元が条件を満たさない."

        if right==0:
            return 0

        right+=self.N
        sm=self.unit

        calc=self.calc; data=self.data
        first=1
        while first or (right & (-right))!=right:
            first=0
            right-=1
            while right>1 and right&1:
                right>>=1

            if not cond(calc(data[right], sm)):
                while right<self.N:
                    right=2*right+1
                    if cond(calc(data[right], sm)):
                        sm=calc(data[right], sm)
                        right-=1
                return right+1-self.N
            sm=calc(data[right], sm)
        return 0

    def __getitem__(self,k):
        return self.get(k)

    def __setitem__(self,k,x):
        return self.update(k,x)
