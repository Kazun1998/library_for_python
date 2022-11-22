class Modulo_Polynomial():
    __slots__=("Poly", "max_degree")

    def __init__(self, Poly=[], max_degree=2*10**5):
        """ 多項式の定義

        P: 係数のリスト
        max_degree

        ※Mod: 法はグローバル変数から指定
        """

        if Poly:
            self.Poly=[p%Mod for p in Poly[:max_degree]]
        else:
            self.Poly=[0]
        self.max_degree=max_degree

    def __str__(self):
        return str(self.Poly)

    def __repr__(self):
        return self.__str__()

    def __iter__(self):
        yield from self.Poly

    #=
    def __eq__(self,other):
        from itertools import zip_longest
        return all([a==b for a,b in zip_longest(self.Poly,other.Poly,fillvalue=0)])

    #+,-
    def __pos__(self):
        return self

    def __neg__(self):
        return self.scale(-1)

    #items
    def __getitem__(self, index):
        if isinstance(index, slice):
            return Modulo_Polynomial(self.Poly[index], self.max_degree)
        else:
            if index<0:
                raise IndexError("index is negative (index: {})".format(index))
            elif index>=len(self.Poly):
                return 0
            else:
                return self.Poly[index]

    def __setitem__(self, index, value):
        if index<0:
            raise IndexError("index is negative (index: {})".format(index))
        elif index>=self.max_degree:
            return

        if index>=len(self.Poly):
            self.Poly+=[0]*(index-len(self.Poly)+1)
        self.Poly[index]=value%Mod

    #Boole
    def __bool__(self):
        return any(self.Poly)

    #簡略化
    def reduce(self):
        """ 高次の 0 を切り捨て

        """

        P=self.Poly
        for d in range(len(P)-1,-1,-1):
            if P[d]:
                break
        self.resize(d+1)
        return

    #シフト
    def __lshift__(self,other):
        if other<0:
            return self>>(-other)

        if other>self.max_degree:
            return Modulo_Polynomial([0],self.max_degree)

        G=[0]*other+self.Poly
        return Modulo_Polynomial(G,self.max_degree)

    def __rshift__(self,other):
        if other<0:
            return  self<<(-other)

        return Modulo_Polynomial(self.Poly[other:],self.max_degree)

    #次数
    def degree(self):
        P=self.Poly
        for d in range(len(self.Poly)-1,-1,-1):
            if P[d]:
                return d
        return -float("inf")

    #加法
    def __add__(self,other):
        P=self; Q=other

        if Q.__class__==Modulo_Polynomial:
            N=min(P.max_degree,Q.max_degree)
            A=P.Poly; B=Q.Poly
        else:
            N=P.max_degree
            A=P.Poly; B=Q
        return Modulo_Polynomial(Calc.Add(A,B),N)

    def __radd__(self,other):
        return self+other

    #減法
    def __sub__(self,other):
        P=self; Q=other
        if Q.__class__==Modulo_Polynomial:
            N=min(P.max_degree,Q.max_degree)
            A=P.Poly; B=Q.Poly
        else:
            N=P.max_degree
            A=P.Poly; B=Q
        return Modulo_Polynomial(Calc.Sub(A,B),N)

    def __rsub__(self,other):
        return (-self)+other

    #乗法
    def __mul__(self,other):
        P=self
        Q=other
        if Q.__class__==Modulo_Polynomial:
            a=b=0
            for x in P.Poly:
                if x:
                    a+=1
            for y in Q.Poly:
                if y:
                    b+=1

            if a>b:
                P,Q=Q,P

            P.reduce();Q.reduce()
            U,V=P.Poly,Q.Poly
            M=min(P.max_degree,Q.max_degree)
            if a<2*P.max_degree.bit_length():
                B=[0]*(len(U)+len(V)-1)
                for i in range(len(U)):
                    if U[i]:
                        for j in range(len(V)):
                            B[i+j]+=U[i]*V[j]
                            if B[i+j]>Mod:
                                B[i+j]-=Mod
            else:
                B=Calc.Convolution(U,V)[:M]
            B=Modulo_Polynomial(B,M)
            B.reduce()
            return B
        else:
            return self.scale(other)

    def __rmul__(self,other):
        return self.scale(other)

    #除法
    def __floordiv__(self,other):
        if not other:
            raise ZeroDivisionError
        if isinstance(other,int):
            return self/other

        self.reduce()
        other.reduce()

        return Modulo_Polynomial(Calc.Floor_Div(self.Poly, other.Poly),
                                max(self.max_degree, other.max_degree))

    def __rfloordiv__(self,other):
        if not self:
            raise ZeroDivisionError

        if isinstance(other,int):
            return Modulo_Polynomial([],self.max_degree)

    #剰余
    def __mod__(self,other):
        if not other:
            return ZeroDivisionError
        self.reduce(); other.reduce()
        r=Modulo_Polynomial(Calc.Mod(self.Poly, other.Poly),
                            min(self.max_degree, other.max_degree))
        r.reduce()
        return r

    def __rmod__(self,other):
        if not self:
            raise ZeroDivisionError
        r=other-(other//self)*self
        r.reduce()
        return r

    def __divmod__(self,other):
        q=self//other
        r=self-q*other; r.reduce()
        return (q,r)

    #累乗
    def __pow__(self,other):
        if other.__class__==int:
            n=other
            m=abs(n)

            Q=self
            A=Modulo_Polynomial([1],self.max_degree)
            while m>0:
                if m&1:
                    A*=Q
                m>>=1
                Q*=Q

            if n>=0:
                return A
            else:
                return A.inverse()
        else:
            P=Log(self)
            return Exp(P*other)

    #逆元
    def inverse(self, deg=None):
        assert self.Poly[0], "定数項が0"

        if deg==None:
            deg=self.max_degree

        return Modulo_Polynomial(Calc.Inverse(self.Poly, deg), self.max_degree)

    #除法
    def __truediv__(self,other):
        if isinstance(other, Modulo_Polynomial):
            if Calc.is_sparse(other.Poly):
                d,f=Calc.coefficients_list(other.Poly)
                K=len(d)
                H=[0]*self.max_degree

                alpha=pow(other[0], Mod-2, Mod)
                H[0]=alpha*self[0]%Mod

                for i in range(1, self.max_degree):
                    c=0
                    for j in range(1, K):
                        if d[j]<=i:
                            c+=f[j]*H[i-d[j]]%Mod
                        else:
                            break
                    c%=Mod
                    H[i]=alpha*(self[i]-c)%Mod
                H=Modulo_Polynomial(H, min(self.max_degree, other.max_degree))
                return H
            else:
                return self*other.inverse()
        else:
            return pow(other,Mod-2,Mod)*self

    def __rtruediv__(self,other):
        return other*self.inverse()

    #スカラー倍
    def scale(self, s):
        return Modulo_Polynomial(Calc.Times(self.Poly,s),self.max_degree)

    #最高次の係数
    def leading_coefficient(self):
        for x in self.Poly[::-1]:
            if x:
                return x
        return 0

    def censor(self, N=-1, Return=False):
        """ N 次以上の係数をカット
        """

        if N==-1:
            N=self.max_degree

        N=min(N, self.max_degree)

        if Return:
            return Modulo_Polynomial(self.Poly[:N],self.max_degree)
        else:
            self.Poly=self.Poly[:N]

    def resize(self, N, Return=False):
        """ 強制的に Poly の配列の長さを N にする.

        """

        N=min(N, self.max_degree)
        P=self
        if Return:
            if len(P.Poly)>N:
                E=P.Poly[:N]
            else:
                E=P.Poly+[0]*(N-len(P.Poly))
            return Modulo_Polynomial(E,P.max_degree)
        else:
            if len(P.Poly)>N:
                del P.Poly[N:]
            else:
                P.Poly+=[0]*(N-len(P.Poly))

    #代入
    def substitution(self, a):
        """ a を (形式的に) 代入した値を求める.

        a: int
        """

        y=0
        t=1
        for p in self.Poly:
            y=(y+p*t)%Mod
            t=(t*a)%Mod
        return y
#=================================================
class Calculator:
    def __init__(self):
        self.primitive=self.__primitive_root()
        self.__build_up()

    def __primitive_root(self):
        p=Mod
        if p==2:
            return 1
        if p==998244353:
            return 3
        if p==10**9+7:
            return 5
        if p==163577857:
            return 23
        if p==167772161:
            return 3
        if  p==469762049:
            return 3

        fac=[]
        q=2
        v=p-1

        while v>=q*q:
            e=0
            while v%q==0:
                e+=1
                v//=q

            if e>0:
                fac.append(q)
            q+=1

        if v>1:
            fac.append(v)

        g=2
        while g<p:
            if pow(g,p-1,p)!=1:
                return None

            flag=True
            for q in fac:
                if pow(g,(p-1)//q,p)==1:
                    flag=False
                    break

            if flag:
                return g

            g+=1

    #参考元: https://judge.yosupo.jp/submission/72676
    def __build_up(self):
        rank2=(~(Mod-1)&(Mod-2)).bit_length()
        root=[0]*(rank2+1); iroot=[0]*(rank2+1)
        rate2=[0]*max(0, rank2-1); irate2=[0]*max(0, rank2-1)
        rate3=[0]*max(0, rank2-2); irate3=[0]*max(0, rank2-2)

        root[-1]=pow(self.primitive, (Mod-1)>>rank2, Mod)
        iroot[-1]=pow(root[-1], Mod-2, Mod)

        for i in range(rank2)[::-1]:
            root[i]=root[i+1]*root[i+1]%Mod
            iroot[i]=iroot[i+1]*iroot[i+1]%Mod

        prod=iprod=1
        for i in range(rank2-1):
            rate2[i]=root[i+2]*prod%Mod
            irate2[i]=iroot[i+2]*prod%Mod
            prod*=iroot[i+2]; prod%=Mod
            iprod*=root[i+2]; iprod%=Mod

        prod=iprod = 1
        for i in range(rank2-2):
            rate3[i]=root[i + 3]*prod%Mod
            irate3[i]=iroot[i + 3]*iprod%Mod
            prod*=iroot[i + 3]; prod%=Mod
            iprod*=root[i + 3]; iprod%=Mod

        self.root=root; self.iroot=iroot
        self.rate2=rate2; self.irate2=irate2
        self.rate3=rate3; self.irate3=irate3

    def Add(self, A, B):
        """ 必要ならば末尾に元を追加して, [A[i]+B[i]] を求める.

        """
        if type(A)==int:
            A=[A]

        if type(B)==int:
            B=[B]

        m=min(len(A), len(B))
        C=[(A[i]+B[i])%Mod for i in range(m)]
        C.extend(A[m:])
        C.extend(B[m:])
        return C

    def Sub(self, A, B):
        """ 必要ならば末尾に元を追加して, [A[i]-B[i]] を求める.

        """
        if type(A)==int:
            A=[A]

        if type(B)==int:
            B=[B]

        m=min(len(A), len(B))
        C=[0]*m
        C=[(A[i]-B[i])%Mod for i in range(m)]
        C.extend(A[m:])
        C.extend([-b%Mod for b in B[m:]])
        return C

    def Times(self,A, k):
        """ [k*A[i]] を求める.

        """
        return [k*a%Mod for a in A]

    #参考元 https://judge.yosupo.jp/submission/72676
    def NTT(self, A):
        """ A に Mod を法とする数論変換を施す

        ※ Mod はグローバル変数から指定

        References:
        https://github.com/atcoder/ac-library/blob/master/atcoder/convolution.hpp
        https://judge.yosupo.jp/submission/72676
        """

        N=len(A)
        H=(N-1).bit_length()
        l=0

        I=self.root[2]
        rate2=self.rate2; rate3=self.rate3

        while l<H:
            if H-l==1:
                p=1<<(H-l-1)
                rot=1
                for s in range(1<<l):
                    offset=s<<(H-l)
                    for i in range(p):
                        x=A[i+offset]; y=A[i+offset+p]*rot%Mod
                        A[i+offset]=(x+y)%Mod
                        A[i+offset+p]=(x-y)%Mod

                    if s+1!=1<<l:
                        rot*=rate2[(~s&-~s).bit_length()-1]
                        rot%=Mod
                l+=1
            else:
                p=1<<(H-l-2)
                rot=1
                for s in range(1<<l):
                    rot2=rot*rot%Mod
                    rot3=rot2*rot%Mod
                    offset=s<<(H-l)
                    for i in range(p):
                        a0=A[i+offset]
                        a1=A[i+offset+p]*rot
                        a2=A[i+offset+2*p]*rot2
                        a3=A[i+offset+3*p]*rot3

                        alpha=(a1-a3)%Mod*I

                        A[i+offset]=(a0+a2+a1+a3)%Mod
                        A[i+offset+p]=(a0+a2-a1-a3)%Mod
                        A[i+offset+2*p]=(a0-a2+alpha)%Mod
                        A[i+offset+3*p]=(a0-a2-alpha)%Mod

                    if s+1!=1<<l:
                        rot*=rate3[(~s&-~s).bit_length()-1]
                        rot%=Mod
                l+=2

    #参考元 https://judge.yosupo.jp/submission/72676
    def Inverse_NTT(self, A):
        """ A を Mod を法とする逆数論変換を施す

        ※ Mod はグローバル変数から指定

        References:
        https://github.com/atcoder/ac-library/blob/master/atcoder/convolution.hpp
        https://judge.yosupo.jp/submission/72676
        """
        N=len(A)
        H=(N-1).bit_length()
        l=H

        J=self.iroot[2]
        irate2=self.rate2; irate3=self.irate3

        while l:
            if l==1:
                p=1<<(H-l)
                irot=1
                for s in range(1<<(l-1)):
                    offset=s<<(H-l+1)
                    for i in range(p):
                        x=A[i+offset]; y=A[i+offset+p]
                        A[i+offset]=(x+y)%Mod
                        A[i+offset+p]=(x-y)*irot%Mod

                    if s+1!=1<<(l-1):
                        irot*=irate2[(~s&-~s).bit_length()-1]
                        irot%=Mod
                l-=1
            else:
                p=1<<(H-l)
                irot=1
                for s in range(1<<(l-2)):
                    irot2=irot*irot%Mod
                    irot3=irot2*irot%Mod
                    offset=s<<(H-l+2)
                    for i in range(p):
                        a0=A[i+offset]
                        a1=A[i+offset+p]
                        a2=A[i+offset+2*p]
                        a3=A[i+offset+3*p]

                        beta=(a2-a3)*J%Mod

                        A[i+offset]=(a0+a1+a2+a3)%Mod
                        A[i+offset+p]=(a0-a1+beta)*irot%Mod
                        A[i+offset+2*p]=(a0+a1-a2-a3)*irot2%Mod
                        A[i+offset+3*p]=(a0-a1-beta)*irot3%Mod

                    if s+1!=1<<(l-2):
                        irot*=irate3[(~s&-~s).bit_length()-1]
                        irot%=Mod
                l-=2
        N_inv=pow(N,Mod-2,Mod)
        for i in range(N):
            A[i]=N_inv*A[i]%Mod

    def non_zero_count(self, A):
        """ A にある非零の数を求める. """
        return len(A)-A.count(0)

    def is_sparse(self, A, K=None):
        """ A が疎かどうかを判定する. """

        if K==None:
            K=25

        return self.non_zero_count(A)<=K

    def coefficients_list(self, A):
        """ A にある非零のリストを求める.


        output: ( [d[0], ..., d[k-1] ], [f[0], ..., f[k-1] ]) : a[d[j]]=f[j] であることを表している.
        """

        f=[]; d=[]
        for i in range(len(A)):
            if A[i]:
                d.append(i)
                f.append(A[i])
        return d,f

    def Convolution(self, A, B):
        """ A, B で Mod を法とする畳み込みを求める.

        ※ Mod はグローバル変数から指定
        """
        if not A or not B:
            return []

        N=len(A)
        M=len(B)
        L=M+N-1

        if min(N,M)<=50:
            if N<M:
                N,M=M,N
                A,B=B,A
            C=[0]*L
            for i in range(N):
                for j in range(M):
                    C[i+j]+=A[i]*B[j]
                    C[i+j]%=Mod
            return C

        H=L.bit_length()
        K=1<<H

        A=A+[0]*(K-N)
        B=B+[0]*(K-M)

        self.NTT(A)
        self.NTT(B)

        for i in range(K):
            A[i]=A[i]*B[i]%Mod

        self.Inverse_NTT(A)

        return A[:L]

    def Autocorrelation(self, A):
        """ A 自身に対して,Mod を法とする畳み込みを求める.

        ※ Mod はグローバル変数から指定
        """
        N=len(A)
        L=2*N-1

        if N<=50:
            C=[0]*L
            for i in range(N):
                for j in range(N):
                    C[i+j]+=A[i]*A[j]
                    C[i+j]%=Mod
            return C

        H=L.bit_length()
        K=1<<H

        A=A+[0]*(K-N)

        self.NTT(A)

        for i in range(K):
            A[i]=A[i]*A[i]%Mod
        self.Inverse_NTT(A)

        return A[:L]

    def Multiple_Convolution(self, *A):
        """ A=(A[0], A[1], ..., A[d-1]) で Mod を法とする畳み込みを行う.

        """
        from heapq import heapify,heappush,heappop
        Q=[(len(a), a) for a in A]
        heapify(Q)
        while len(Q)>1:
            m,a=heappop(Q)
            n,b=heappop(Q)
            heappush(Q, (m+n-1, self.Convolution(a,b)))
        return Q[0][1]

    def Inverse(self, F, length=None):
        if length==None:
            M=len(F)
        else:
            M=length

        if M<=0:
            return []

        if self.is_sparse(F):
            """
            愚直に漸化式を用いて求める.
            計算量: F にある係数が非零の項の個数を K, 求める最大次数を N として, O(NK) 時間
            """
            d,f=self.coefficients_list(F)

            G=[0]*M
            alpha=pow(F[0], Mod-2, Mod)
            G[0]=alpha

            for i in range(1, M):
                for j in range(1, len(d)):
                    if d[j]<=i:
                        G[i]+=f[j]*G[i-d[j]]%Mod
                    else:
                        break

                G[i]%=Mod
                G[i]=(-alpha*G[i])%Mod
            del G[M:]
        else:
            """
            FFTの理論を応用して求める.
            計算量: 求めたい項の個数をNとして, O(N log N)

            Reference: https://judge.yosupo.jp/submission/42413
            """

            N=len(F)
            r=pow(F[0],Mod-2,Mod)

            m=1
            G=[r]
            while m<M:
                A=F[:min(N, 2*m)]; A+=[0]*(2*m-len(A))
                B=G.copy(); B+=[0]*(2*m-len(B))

                Calc.NTT(A); Calc.NTT(B)
                for i in range(2*m):
                    A[i]=A[i]*B[i]%Mod

                Calc.Inverse_NTT(A)
                A=A[m:]+[0]*m
                Calc.NTT(A)
                for i in range(2*m):
                    A[i]=-A[i]*B[i]%Mod
                Calc.Inverse_NTT(A)

                G.extend(A[:m])
                m<<=1
            G=G[:M]
        return G

    def Floor_Div(self, F, G):
        assert F[-1]
        assert G[-1]

        F_deg=len(F)-1
        G_deg=len(G)-1

        if F_deg<G_deg:
            return []

        m=F_deg-G_deg+1
        return self.Convolution(F[::-1], Calc.Inverse(G[::-1],m))[m-1::-1]

    def Mod(self, F, G):
        while F and F[-1]==0:
            F.pop()

        while G and G[-1]==0:
            G.pop()

        if not F:
            return []

        return Calc.Sub(F, Calc.Convolution(Calc.Floor_Div(F,G),G))

#以下 参考元https://judge.yosupo.jp/submission/28304
def Differentiate(P):
    G=[(k*a)%Mod for k,a in enumerate(P.Poly[1:],1)]+[0]
    return Modulo_Polynomial(G,P.max_degree)

def Integrate(P):
    F=P.Poly
    N=len(F)

    Inv=[0]*(N+1)
    if N:
        Inv[1]=1
        for i in range(2,N+1):
            q,r=divmod(Mod,i)
            Inv[i]=(-q*Inv[r])%Mod

    G=[0]+[(Inv[k]*a)%Mod for k,a in enumerate(F,1)]
    return Modulo_Polynomial(G,P.max_degree)

"""
累乗,指数,対数
"""
def Log(P):
    assert P.Poly[0]==1,"定数項が1ではない"
    return Integrate(Differentiate(P)/P)

def Exp(P):
    #参考元1:https://arxiv.org/pdf/1301.5804.pdf
    #参考元2:https://opt-cp.com/fps-fast-algorithms/
    from itertools import zip_longest
    N=P.max_degree

    Inv=[0]*(2*N+1)
    Inv[1]=1
    for i in range(2,2*N+1):
        q,r=divmod(Mod,i)
        Inv[i]=(-q*Inv[r])%Mod

    H=P.Poly; H+=[0]*(N-len(H))
    assert (not H) or H[0]==0,"定数項が0でない"

    if Calc.is_sparse(H):
        # 疎だった場合
        F=[0]*N; F[0]=1
        d,f=Calc.coefficients_list(H)
        K=len(d)

        for t in range(K):
            f[t]=(d[t]*f[t])%Mod
            d[t]-=1

        for i in range(1,N):
            a=0
            for j in range(K):
                if d[j]<=i-1:
                    a+=f[j]*F[(i-1)-d[j]]%Mod
                else:
                    break
            a%=Mod
            F[i]=a*Inv[i]%Mod
    else:
        dH=[(k*a)%Mod for k,a in enumerate(H[1:],1)]
        F,G,m=[1],[1],1

        while m<=N:
            #2.a'
            if m>1:
                E=Calc.Convolution(F,Calc.Autocorrelation(G)[:m])[:m]
                G=[(2*a-b)%Mod for a,b in zip_longest(G,E,fillvalue=0)]
            #2.b', 2.c'
            C=Calc.Convolution(F,dH[:m-1])
            R=[0]*m
            for i,a in enumerate(C):
                R[i%m]+=a
            R=[a%Mod for a in R]
            #2.d'
            dF=[(k*a)%Mod for k,a in enumerate(F[1:],1)]
            D=[0]+[(a-b)%Mod for a,b in zip_longest(dF,R,fillvalue=0)]
            S=[0]*m
            for i,a in enumerate(D):
                S[i%m]+=a
            S=[a%Mod for a in S]
            #2.e'
            T=Calc.Convolution(G,S)[:m]
            #2.f'
            E=[0]*(m-1)+T
            E=[0]+[(Inv[k]*a)%Mod for k,a in enumerate(E,1)]
            U=[(a-b)%Mod for a,b in zip_longest(H[:2*m],E,fillvalue=0)][m:]
            #2.g'
            V=Calc.Convolution(F,U)[:m]
            #2.h'
            F.extend(V)
            #2.i'
            m<<=1
    return Modulo_Polynomial(F[:N],P.max_degree)

def Root(P,k):
    assert P.Poly[0]==1, "定数項が1ではない"
    k%=Mod
    assert k, "kが特異"
    k_inv=pow(k,Mod-2,Mod)
    return Power(P,k_inv)

"""
三角関数
"""
#正弦
def Sin(P):
    I=Tonelli_Shanks(-1)
    B=I*P
    C=Exp(B)-Exp(-B)
    return C*pow(2*I,Mod-2,Mod)

#余弦
def Cos(P):
    I=Tonelli_Shanks(-1)
    B=I*P
    C=Exp(B)+Exp(-B)
    return C*pow(2,Mod-2,Mod)

#正接
def Tan(P):
    return Sin(P)/Cos(P)

#逆正弦
def ArcSin(P):
    #積分版
    return Integrate(Differentiate(P)/Sqrt(1-P*P))

    #三角関数と指数関数の相互関係版
    I=Tonelli_Shanks(-1)
    return -I*Log(Sqrt(1-P*P)+I*P)

#逆余弦
def ArcCos(P):
    #※使用時注意!!! (ArcCos(0)=pi/2 のため)
    #積分版
    return -Integrate(Differentiate(P)/Sqrt(1-P*P))

    #三角関数と指数関数の相互関係版
    I=Tonelli_Shanks(-1)
    return I*Log(Sqrt(1-P*P)+I*P)

#逆正接
def ArcTan(P):
    #積分版
    return Integrate(Differentiate(P)/(1+P*P))

    #三角関数と指数関数の相互関係版
    I=Tonelli_Shanks(-1)
    return I*pow(2,Mod-2,Mod)*Log((I+P)/(I-P))

def Power(P, M):
    """ P の M 乗を求める.

    """

    assert M>=0
    N=P.max_degree
    F=P.Poly
    F+=[0]*((N+1)-len(F))
    for (deg,p) in enumerate(F):
        if p:
            break
    else:
        if M==0:
            return Modulo_Polynomial([1], P.max_degree)
        else:
            return Modulo_Polynomial([0] ,P.max_degree)

    if deg*M>N:
        return Modulo_Polynomial([0], P.max_degree)

    p_inv=pow(p, Mod-2, Mod)
    M_mod=M%Mod

    if Calc.is_sparse(F):
        # P が疎な場合
        H=[(p_inv*a)%Mod for a in F[deg:]]+[0]
        Nh=len(H)-1
        d,h=Calc.coefficients_list(H); K=len(d)

        Inv=[0]*(Nh+1); Inv[1]=1
        for i in range(2, Nh+1):
            q,r=divmod(Mod, i)
            Inv[i]=(-q*Inv[r])%Mod

        G=[0]*Nh; G[0]=1
        for i in range(Nh-1):
            g=(M_mod*(i+1)%Mod)*H[i+1]%Mod
            for j in range(K):
                if 1<=d[j]<=i:
                    alpha=(d[j]*M_mod-(i-d[j]+1))%Mod
                    beta=G[i+1-d[j]]*H[d[j]]%Mod
                    g+=alpha*beta
            g%=Mod
            G[i+1]=g*Inv[i+1]%Mod
    else:
        Q=Modulo_Polynomial([(p_inv*a)%Mod for a in F[deg:]],P.max_degree)
        G=Exp(M_mod*Log(Q)).Poly

    pk=pow(p, M, Mod)
    G=[0]*(deg*M)+[(pk*a)%Mod for a in G]
    return Modulo_Polynomial(G, P.max_degree)

#根号
def Tonelli_Shanks(X, default=-1):
    """ X=a (mod Mod) のとき, r*r=a (mod Mod) を満たす r を返す.

    ※法pが素数のときのみ有効
    ※存在しないときは default が返り値
    """

    #ルジャンドル記号
    def Legendre(X):
        """ルジャンドル記号 (a/Mod) を返す.

        ※法が素数のときのみ成立する.
        """

        if X%Mod==0:
            return 0
        elif pow(X,(Mod-1)//2,Mod)==1:
            return 1
        else:
            return -1

    X%=Mod
    if Legendre(X)==-1:
        return default

    from random import randint as ri
    if X==0:
        return X
    elif Mod==2:
        return X
    elif Mod%4==3:
        return pow(X,(Mod+1)//4,Mod)

    u=2
    s=1
    while (Mod-1)%(2*u)==0:
        u*=2
        s+=1
    q=(Mod-1)//u

    z=0
    while pow(z,(Mod-1)//2,Mod)!=Mod-1:
        z=ri(1,Mod-1)

    m,c,t,r=s,pow(z,q,Mod),pow(X,q,Mod),pow(X,(q+1)//2,Mod)
    while m>1:
        if pow(t,2**(m-2),Mod)==1:
            c=(c*c)%Mod
            m=m-1
        else:
            c,t,r,m=(c*c)%Mod,(c*c*t)%Mod,(c*r)%Mod,m-1
    return r

#多項式の根号
def __sqrt(F, N):
    F+=[0]*(N-len(F))
    s=Tonelli_Shanks(F[0])
    if s==-1:
        return None

    two_inv=pow(2, Mod-2, Mod)

    if not Calc.is_sparse(F):
        # P が疎な場合
        F.append(0)
        d,f=Calc.coefficients_list(F); K=len(d)

        Inv=[0]*(N+1); Inv[1]=1
        for i in range(2, N+1):
            q,r=divmod(Mod, i)
            Inv[i]=(-q*Inv[r])%Mod

        G=[0]*N; G[0]=1
        for i in range(N):
            g=(two_inv*(i+1)%Mod)*F[i+1]%Mod
            for j in range(K):
                if 1<=d[j]<=i:
                    alpha=(d[j]*two_inv-(i-d[j]+1))%Mod
                    beta=G[i+1-d[j]]*F[d[j]]%Mod
                    g+=alpha*beta
            g%=Mod
            G[i+1]=g*Inv[i+1]%Mod
    else:
        m=1
        G=[min(s,Mod-s)]

        while m<N:
            G+=[0]*m
            m<<=1
            H=Calc.Convolution(F[:m], Calc.Inverse(G))
            G=[two_inv*(a+b)%Mod for a,b in zip(G,H)]
    return G[:N]

def Sqrt(P):
    N=P.max_degree
    F=P.Poly
    F+=[0]*(N-len(F))

    for d,p in enumerate(F):
        if p:
            break
    else:
        return Modulo_Polynomial([0],P.max_degree)

    if d%2==1:
        return

    E=__sqrt(F[d:],N-d//2)

    if E==None:
        return

    if d>0:
        E=[0]*(d//2)+E
    return Modulo_Polynomial(E,P.max_degree)

"""
形式的ベキ級数に対する特別な操作
"""
def Composition(P,Q):
    """ P o Q=P(Q) を求める (※ 順番注意) ([X^0]Q=0 でなくてはならない).

    Reference: https://judge.yosupo.jp/submission/42372
    """

    assert Q[0]==0

    deg=min(P.max_degree, Q.max_degree)
    k=int(deg**0.5+1)
    d=(deg+k)//k

    X=[[1]]
    for i in range(k):
        X.append(Calc.Convolution(X[-1],Q.Poly)[:deg+1])

    Y=[[0]*len(X[k]) for _ in range(k)]
    for i,y in enumerate(Y):
        for j,x in enumerate(X[:d]):
            if i*d+j>deg:
                break

            for t in range(deg+1):
                if t>=len(x):
                    break
                if t<len(y):
                    y[t]+=x[t]*P[i*d+j]%Mod

    F=[0]*(deg+1)
    Z=[1]
    x=X[d]
    for i in range(k):
        Y[i]=Calc.Convolution(Y[i],Z)[:deg+1]
        for j in range(len(Y[i])):
            F[j]+=Y[i][j]
        Z=Calc.Convolution(Z,x)[:deg+1]
    return Modulo_Polynomial(F, deg)

def Taylor_Shift(P, a):
    """与えられた多項式 P に対して, P(X+a) を求める.

    P: Polynominal
    a: int
    """

    N=len(P.Poly)-1

    fact=[0]*(N+1)
    fact[0]=1
    for i in range(1,N+1):
        fact[i]=(fact[i-1]*i)%Mod

    fact_inv=[0]*(N+1)
    fact_inv[-1]=pow(fact[-1],Mod-2,Mod)

    for i in range(N-1,-1,-1):
        fact_inv[i]=(fact_inv[i+1]*(i+1))%Mod

    F=P.Poly.copy()
    for i in range(N+1):
        F[i]=(F[i]*fact[i])%Mod

    G=[0]*(N+1)
    c=1
    for i in range(N+1):
        G[i]=(c*fact_inv[i])%Mod
        c=(c*a)%Mod
    G.reverse()

    H=Calc.Convolution(F,G)[N:]
    for i in range(len(H)):
        H[i]=(H[i]*fact_inv[i])%Mod

    return Modulo_Polynomial(H,P.max_degree)

def Polynominal_Coefficient(P,Q,N):
    """ [X^N] P/Q を求める.

    References:
    http://q.c.titech.ac.jp/docs/progs/polynomial_division.html
    https://arxiv.org/abs/2008.08822
    https://arxiv.org/pdf/2008.08822.pdf
    """

    P=P.Poly.copy(); Q=Q.Poly.copy()
    m=1<<((len(Q)-1).bit_length())
    P.extend([0]*(2*m-len(P)))
    Q.extend([0]*(2*m-len(Q)))

    while N:
        R=[Q[i] if i&1==0 else -Q[i] for i in range(2*m)]

        Calc.NTT(P); Calc.NTT(Q); Calc.NTT(R)
        for i in range(2*m):
            P[i]*=R[i]; P[i]%=Mod
            Q[i]*=R[i]; Q[i]%=Mod

        Calc.Inverse_NTT(P); Calc.Inverse_NTT(Q)
        if N&1==0:
            for i in range(m):
                P[i]=P[2*i]
        else:
            for i in range(m):
                P[i]=P[2*i+1]

        for i in range(m):
            Q[i]=Q[2*i]

        for i in range(m,2*m):
            P[i]=Q[i]=0

        N>>=1

    if Q[0]==1:
        return P[0]
    else:
        return P[0]*pow(Q[0],Mod-2,Mod)%Mod

def Multipoint_Evaluation(P, X):
    """ 多項式 P に対して, X=[x[0], ..., x[N-1]] としたとき, [P(x[0]), ..., P(x[N-1])] を求める.
    """

    N=len(X)
    size=1<<(N-1).bit_length()

    G=[[1] for _ in range(2*size)]

    for i in range(N):
        G[i+size]=[-X[i],1]

    for i in range(size-1,0,-1):
        G[i]=Calc.Convolution(G[2*i],G[2*i+1])

    for i in range(1, 2*size):
        A=P.Poly if i==1 else G[i>>1]
        m=len(A)-len(G[i])+1
        v=Calc.Convolution(A[::-1][:m], Calc.Inverse(G[i][::-1],m))[m-1::-1]
        w=Calc.Convolution(v,G[i])

        G[i]=A.copy()
        g=G[i]

        for j in range(len(w)):
            g[j]-=w[j]; g[j]%=Mod

        while len(g)>1 and g[-1]==0:
            g.pop()

    return [G[i+size][0] for i in range(N)]

def Polynominal_Interpolation(X, Y):
    """ N=|X|=|Y| とする. P(x_i)=y_i (0<=i<|X|-1) を満たす高々 (N-1) 次の多項式 P を求める.

    """

    assert len(X)==len(Y)

    N=len(X)
    size=1<<(N-1).bit_length()

    T=[[1] for _ in range(2*size)]

    for i in range(N):
        T[i+size]=[-X[i],1]

    for i in range(size-1,0,-1):
        T[i]=Calc.Convolution(T[2*i], T[2*i+1])

    U=[[] for _ in range(2*size)]
    U[1]=[k*a for k,a in enumerate(T[1][1:],1)]

    for i in range(2,N+size):
        m=len(U[i//2])-len(T[i])+1
        v=Calc.Convolution(U[i//2][::-1][:m],Calc.Inverse(T[i][::-1],m))[m-1::-1]
        w=Calc.Convolution(v,T[i])

        U[i]=U[i//2].copy()
        u=U[i]
        for j in range(len(w)):
            u[j]-=w[j]; u[j]%=Mod

        while len(u)>1 and u[-1]==0:
            u.pop()

    for i in range(N):
        U[i+size]=[(Y[i]*pow(U[i+size][0],Mod-2,Mod))%Mod]

    for i in range(size-1,0,-1):
        A=Calc.Convolution(U[2*i], T[2*i+1])
        B=Calc.Convolution(T[2*i], U[2*i+1])

        m=min(len(A), len(B))

        u=[0]*m
        for j in range(m):
            u[j]=(A[j]+B[j])%Mod
        u.extend(A[m:])
        u.extend(B[m:])
        U[i]=u

    return Modulo_Polynomial(U[1], N)

#多項式同士の最大公約数
def _gcd(F,G):
    while G:
        F,G=G,F%G

    a_inv=pow(F.leading_coefficient(),Mod-2,Mod)
    X=F.Poly
    for i in range(len(X)):
        X[i]=(a_inv*X[i])%Mod
    return F

def gcd(*X):
    from functools import reduce
    return reduce(_gcd,X)

#多項式同士の最小公倍数
def _lcm(F,G):
    return (F//gcd(F,G))*G

def lcm(*X):
    from functools import reduce
    L=reduce(_lcm,X)
    a_inv=pow(L.leading_coefficient(),Mod-2,Mod)
    X=L.Poly
    for i in range(len(X)):
        X[i]=(a_inv*X[i])%Mod
    return L

#=================================================
Mod=998244353
Calc=Calculator()
