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

        self.lazy=[self.id]*k+L+[self.id]*(k-N)
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
