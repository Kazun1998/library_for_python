class Segment_Tree_Exception(Exception):
    pass

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
#=================================================
#遅延評価セグメント木

"""
Note
[1] RMQ(区間上の最小値:Range Minimam Query)
calc=lambda x,y:min(x,y)
unit=float("inf")
op=lambda alpha,x:alpha
comp=lambda alpha,beta:alpha
"""
class Lazy_Evaluation_Tree():
    def __init__(self,L,calc,unit,op,comp,id,index):
        """calcを演算,opを作用とするリストLのSegment Treeを作成

        calc:演算
        unit:モノイドcalcの単位元 (xe=ex=xを満たすe)
        op:作用素
        comp:作用素の合成
        id:恒等写像

        [条件] M:Monoid,F={f:F x M→ M:作用素}に対して,以下が成立する.
        Fは恒等写像 id を含む.つまり,任意の x in M に対して id(x)=x
        Fは写像の合成に閉じている.つまり,任意の f,g in F に対して, comp(f,g) in F
        任意の f in F, x,y in M に対して,f(xy)=f(x)f(y)である.

        [注記]
        作用素は左から掛ける.更新も左から.
        """

        self.calc=calc
        self.unit=unit
        self.op=op
        self.comp=comp
        self.id=id
        self.index=index

        N=len(L)
        d=max(1,(N-1).bit_length())
        k=1<<d

        self.data=[unit]*k+L+[unit]*(k-len(L))
        self.lazy=[self.id]*(2*k)
        self.N=k
        self.depth=d

        for i in range(k-1,0,-1):
            self.data[i]=calc(self.data[i<<1],self.data[i<<1|1])

    def _eval_at(self,m):
        if self.lazy[m]==self.id:
            return self.data[m]
        return self.op(self.lazy[m],self.data[m])

    #配列の第m要素を下に伝搬
    def _propagate_at(self,m):
        self.data[m]=self._eval_at(m)

        if m<self.N and self.lazy[m]!=self.id:
            self.lazy[m<<1]=self.comp(
                self.lazy[m],
                self.lazy[m<<1]
                )

            self.lazy[m<<1|1]=self.comp(
                self.lazy[m],
                self.lazy[m<<1|1]
                )

        self.lazy[m]=self.id

    #配列の第m要素より上を全て伝搬
    def _propagate_above(self,m):
        H=m.bit_length()
        for h in range(H-1,0,-1):
            self._propagate_at(m>>h)

    #配列の第m要素より上を全て再計算
    def _recalc_above(self,m):
        while m>1:
            m>>=1
            self.data[m]=self.calc(
                self._eval_at(m<<1),
                self._eval_at(m<<1|1)
            )

    def get(self,k):
        index=self.index
        m=k-index+self.N
        self._propagate_above(m)
        self.data[m]=self._eval_at(m)
        self.lazy[m]=self.id
        return self.data[m]

    #作用
    def operate(self,From,To,alpha,left_closed=True,right_closed=True):
        index=self.index
        L=(From-index)+self.N+(not left_closed)
        R=(To-index)+self.N+(right_closed)

        L0=R0=-1
        X,Y=L,R-1
        while X<Y:
            if X&1:
                L0=max(L0,X)
                X+=1

            if Y&1==0:
                R0=max(R0,Y)
                Y-=1

            X>>=1
            Y>>=1

        L0=max(L0,X)
        R0=max(R0,Y)

        self._propagate_above(L0)
        self._propagate_above(R0)

        while L<R:
            if L&1:
                self.lazy[L]=self.comp(alpha,self.lazy[L])
                L+=1

            if R&1:
                R-=1
                self.lazy[R]=self.comp(alpha,self.lazy[R])

            L>>=1
            R>>=1

        self._recalc_above(L0)
        self._recalc_above(R0)

    def update(self,k,x):
        """ 第k要素をxに変更する.
        """
        index=self.index
        m=k-index+self.N
        self._propagate_above(m)
        self.data[m]=x
        self.lazy[m]=self.id
        self._recalc_above(m)

    def product(self,From,To,left_closed=True,right_closed=True):
        index=self.index
        L=(From-index)+self.N+(not left_closed)
        R=(To-index)+self.N+(right_closed)

        L0=R0=-1
        X,Y=L,R-1
        while X<Y:
            if X&1:
                L0=max(L0,X)
                X+=1

            if Y&1==0:
                R0=max(R0,Y)
                Y-=1

            X>>=1
            Y>>=1

        L0=max(L0,X)
        R0=max(R0,Y)

        self._propagate_above(L0)
        self._propagate_above(R0)

        vL=vR=self.unit

        while L<R:
            if L&1:
                vL=self.calc(vL,self._eval_at(L))
                L+=1

            if R&1:
                R-=1
                vR=self.calc(self._eval_at(R),vR)

            L>>=1
            R>>=1

        return self.calc(vL,vR)

    def all_product(self):
        return self.product(1,self.N,1)

    #リフレッシュ
    def refresh(self):
        for m in range(1,2*self.N):
            self.data[m]=self._eval_at(m)

            if m<self.N and self.lazy[m]!=self.id:
                self.lazy[m<<1]=self.comp(
                    self.lazy[m],
                    self.lazy[m<<1]
                    )

                self.lazy[m<<1|1]=self.comp(
                    self.lazy[m],
                    self.lazy[m<<1|1]
                    )

            self.lazy[m]=self.id

    def __getitem__(self,k):
        return self.get(k)

    def __setitem__(self,k,x):
        self.update(k,x)
#=================================================
#区間に比例する作用付きセグメント木
class Lazy_Evaluation_Proportion_Tree():
    def __init__(self,L,calc,unit,op,comp,id,prop,index=1):
        """calcを演算,opを作用とするリストLのSegment Treeを作成

        calc:演算
        unit:モノイドcalcの単位元 (xe=ex=xを満たすe)
        op:作用素
        comp:作用素の合成
        id:恒等写像
        prop:比例の仕方

        [条件] M:Monoid,F={f:F x M→ M:作用素},prop:F x N →Fに対して,以下が成立する.
        ・Fは恒等写像 id を含む.つまり,任意の x in M に対して id(x)=x
        ・Fは写像の合成に閉じている.つまり,任意の f,g in F に対して, comp(f,g) in F
        ・任意の f in F, x,y in M に対して,f(x*y)=f(x)*f(y)である.
        ・prop(f,2n)(x,y)=prop(f,n)(x)*prop(f,n)(y)

        [注記]
        作用素は左から掛ける.更新も左から.
        calc(a,b,l,r):a,b:計算に用いる値,l,r:a,bが格納されているIndex (lがa,rがb)
        prop(a,l,r):lからrまでのブロックがaであるときの比例の仕方.
        """
        self.calc=calc
        self.unit=unit
        self.op=op
        self.comp=comp
        self.id=id
        self.prop=prop
        self.index=index

        N=len(L)
        d=max(1,(N-1).bit_length())
        k=1<<d

        self.data=[unit]*k+L+[unit]*(k-len(L))
        self.lazy=[self.id]*(2*k)
        self.N=k
        self.depth=d
        self.len=[0]*(2*k)

        for i in range(k-1,0,-1):
            self.data[i]=calc(self.data[i<<1],self.data[i<<1|1],i<<1,i<<1|1)

        self.Left=[0]*k+[x for x in range(1,k+1)]
        self.Right=[0]*k+[x for x in range(1,k+1)]

        for i in range(k-1,0,-1):
            self.Left[i]=self.Left[i<<1]
            self.Right[i]=self.Right[i<<1|1]

    def _eval_at(self,m):
        if self.lazy[m]==self.id:
            return self.data[m]
        return self.op(self.prop(self.lazy[m],self.Left[m],self.Right[m]),self.data[m])

    #配列の第m要素を下に伝搬
    def _propagate_at(self,m):
        self.data[m]=self._eval_at(m)

        if m<self.N and self.lazy[m]!=self.id:
            self.lazy[m<<1]=self.comp(
                self.lazy[m],
                self.lazy[m<<1]
                )

            self.lazy[m<<1|1]=self.comp(
                self.lazy[m],
                self.lazy[m<<1|1]
                )

        self.lazy[m]=self.id

    #配列の第m要素より上を全て伝搬
    def _propagate_above(self,m):
        H=m.bit_length()
        for h in range(H-1,0,-1):
            self._propagate_at(m>>h)

    #配列の第m要素より上を全て再計算
    def _recalc_above(self,m):
        l=1<<(self.depth+1-m.bit_length())
        while m>1:
            m>>=1
            l<<=1

            self.data[m]=self.calc(
                self._eval_at(m<<1),
                self._eval_at(m<<1|1)
            )

    def get(self,k):
        m=k-self.index+self.N
        self._propagate_above(m)

        self.data[m]=self._eval_at(m)

        self.lazy[m]=self.id
        return self.data[m]

    #作用
    def operate(self,From,To,alpha,left_closed=True,right_closed=True):
        L=(From-self.index)+self.N+(not left_closed)
        R=(To-self.index)+self.N+(right_closed)

        L0=R0=-1
        X,Y=L,R-1
        while X<Y:
            if X&1:
                L0=max(L0,X)
                X+=1

            if Y&1==0:
                R0=max(R0,Y)
                Y-=1

            X>>=1
            Y>>=1

        L0=max(L0,X)
        R0=max(R0,Y)

        self._propagate_above(L0)
        self._propagate_above(R0)

        while L<R:
            if L&1:
                self.lazy[L]=self.comp(alpha,self.lazy[L])
                L+=1

            if R&1:
                R-=1
                self.lazy[R]=self.comp(alpha,self.lazy[R])

            L>>=1
            R>>=1

        self._recalc_above(L0)
        self._recalc_above(R0)

    def update(self,k,x):
        """ 第k要素をxに変更する.

        """
        m=k-self.index+self.N
        self._propagate_above(m)
        self.data[m]=x
        self.lazy[m]=self.id
        self._recalc_above(m)

    def product(self,From,To,left_closed=True,right_closed=True):
        L=(From-self.index)+self.N+(not left_closed)
        R=(To-self.index)+self.N+(right_closed)

        L0=R0=-1
        X,Y=L,R-1
        while X<Y:
            if X&1:
                L0=max(L0,X)
                X+=1

            if Y&1==0:
                R0=max(R0,Y)
                Y-=1

            X>>=1
            Y>>=1

        L0=max(L0,X)
        R0=max(R0,Y)

        self._propagate_above(L0)
        self._propagate_above(R0)

        vL=vR=self.unit

        while L<R:
            if L&1:
                #vL=self.calc(vL,self._eval_at(L))
                L+=1

            if R&1:
                R-=1
                #vR=self.calc(self._eval_at(R),vR)

            L>>=1
            R>>=1

            print(L,R)

        return self.calc(vL,vR)

    def all_product(self):
        return self.product(self.index,self.N+(self.index-1))

    #リフレッシュ
    def refresh(self):
        for m in range(1,2*self.N):
            self.data[m]=self._eval_at(m)

            if m<self.N and self.lazy[m]!=self.id:
                self.lazy[m<<1]=self.comp(
                    self.lazy[m],
                    self.lazy[m<<1]
                    )

                self.lazy[m<<1|1]=self.comp(
                    self.lazy[m],
                    self.lazy[m<<1|1]
                    )

            self.lazy[m]=self.id

#=================================================
#遅延評価セグメント木
class Dual_Segment_Tree:
    def __init__(self,L,comp,id,index):
        """opを作用とするリストLのDual Segment Treeを作成

        op:作用素
        id:恒等写像

        [条件] M:Monoid,F={f:F x M→ M:作用素}に対して,以下が成立する.
        Fは恒等写像 id を含む.つまり,任意の x in M に対して id(x)=x
        Fは写像の合成に閉じている.つまり,任意の f,g in F に対して, comp(f,g) in F
        任意の f in F, x,y in M に対して,f(xy)=f(x)f(y)である.

        [注記]
        更新は左から.
        """

        self.comp=comp
        self.id=id
        self.index=index

        N=len(L)
        d=max(1,(N-1).bit_length())
        k=1<<d

        self.lazy=[self.id]*k+X+[self.id]*(k-N)
        self.N=k
        self.depth=d

    #配列の第m要素を下に伝搬
    def _propagate_at(self,m):
        lazy=self.lazy
        if lazy[m]!=self.id:
            lazy[(m<<1)|0]=self.comp(lazy[m],lazy[(m<<1)|0])
            lazy[(m<<1)|1]=self.comp(lazy[m],lazy[(m<<1)|1])
            lazy[m]=self.id

    #配列の第m要素より上を全て伝搬
    def _propagate_above(self,m):
        H=m.bit_length()
        for h in range(H-1,0,-1):
            self._propagate_at(m>>h)

    #作用
    def operate(self,From,To,alpha,left_closed=True,right_closed=True):
        L=(From-self.index)+self.N+(not left_closed)
        R=(To-self.index)+self.N+(right_closed)

        L0=R0=-1
        X,Y=L,R-1
        while X<Y:
            if X&1:
                L0=max(L0,X)
                X+=1

            if Y&1==0:
                R0=max(R0,Y)
                Y-=1

            X>>=1
            Y>>=1

        L0=max(L0,X)
        R0=max(R0,Y)

        self._propagate_above(L0)
        self._propagate_above(R0)

        while L<R:
            if L&1:
                self.lazy[L]=self.comp(alpha,self.lazy[L])
                L+=1

            if R&1:
                R-=1
                self.lazy[R]=self.comp(alpha,self.lazy[R])

            L>>=1
            R>>=1

    #リフレッシュ
    def refresh(self):
        for m in range(1,self.N):
            self._propagate_at(m)

    #取得
    def get(self,k):
        m=k-self.index+self.N
        self._propagate_above(m)
        return self.lazy[m]

    def __getitem__(self,index):
        m=index-self.index+self.N
        self._propagate_above(m)
        return self.lazy[m]

    def __setitem__(self,index,value):
        self.operate(index,index,value)
