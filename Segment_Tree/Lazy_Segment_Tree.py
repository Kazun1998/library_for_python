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
        """ calc を演算, op を作用とするリスト L の Segment Tree を作成

        calc: 演算
        unit: Monoid calc の単位元 ( xe=ex=x を満たす e )
        op: 作用素
        comp: 作用素の合成
        id: 恒等写像

        [条件] M: Monoid, F={f: F x M→ M: 作用素} に対して, 以下が成立する.
        F は恒等写像 id を含む.つまり, 任意の x in M に対して id(x)=x
        F は写像の合成に閉じている. つまり, 任意の f,g in F に対して, comp(f,g) in F
        任意の f in F, x,y in M に対して, f(xy)=f(x) f(y) である.

        [注記]
        作用素は左から掛ける. 更新も左から.
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
        lazy=self.lazy; comp=self.comp

        if m<self.N and self.lazy[m]!=self.id:
            lazy[m<<1]=comp(lazy[m],lazy[m<<1])
            lazy[m<<1|1]=comp(lazy[m],lazy[m<<1|1])
        lazy[m]=self.id

    #配列の第m要素より上を全て伝搬
    def _propagate_above(self,m):
        H=m.bit_length()
        for h in range(H-1,0,-1):
            self._propagate_at(m>>h)
            print(m>>h)

    #配列の第m要素より上を全て再計算
    def _recalc_above(self,m):
        data=self.data; calc=self.calc
        eval_at=self._eval_at
        while m>1:
            m>>=1
            data[m]=calc(eval_at(m<<1),eval_at(m<<1|1))

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

        lazy=self.lazy; comp=self.comp
        while L<R:
            if L&1:
                lazy[L]=comp(alpha,lazy[L])
                L+=1

            if R&1:
                R-=1
                lazy[R]=comp(alpha,lazy[R])

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
        calc=self.calc; eval_at=self._eval_at
        while L<R:
            if L&1:
                vL=calc(vL,eval_at(L))
                L+=1

            if R&1:
                R-=1
                vR=calc(eval_at(R),vR)

            L>>=1
            R>>=1

        return self.calc(vL,vR)

    def all_product(self):
        return self.product(self.index,self.index+self.N-1)

    #リフレッシュ
    def refresh(self):
        lazy=self.lazy; comp=self.comp
        for m in range(1,2*self.N):
            self.data[m]=self._eval_at(m)

            if m<self.N and self.lazy[m]!=self.id:
                lazy[m<<1]=comp(lazy[m], lazy[m<<1])
                lazy[m<<1|1]=comp(lazy[m],lazy[m<<1|1])
            lazy[m]=self.id

    def __getitem__(self,k):
        return self.get(k)

    def __setitem__(self,k,x):
        self.update(k,x)
