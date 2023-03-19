class Lazy_Evaluation_Proportion_Tree():
    def __init__(self,L,calc,unit,act,comp,id,prop,index=1):
        """calcを演算,actを作用とするリストLのSegment Treeを作成

        calc:演算
        unit:モノイドcalcの単位元 (xe=ex=xを満たすe)
        act:作用素
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
        self.act=act
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
        return self.act(self.prop(self.lazy[m],self.Left[m],self.Right[m]),self.data[m])

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
    def action(self,From,To,alpha,left_closed=True,right_closed=True):
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
