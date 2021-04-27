class Modulo_Polynominal():
    def __init__(self,Poly,Max_Degree=2*10**5,Char="X"):
        from itertools import zip_longest
        """多項式の定義

        P:係数のリスト
        C:文字
        Max_Degree

        ※Mod:法はグローバル変数から指定
        """
        self.Poly=[p%Mod for p in Poly[:Max_Degree]]
        self.Char=Char
        self.Max_Degree=Max_Degree
        self.minus=10**7

    def __str__(self):
        if bool(self):
            M=[(k,a) for k,a in enumerate(self.Poly) if a]
            for i in range(len(M)):
                k,a=M[i]
                if Mod-a<=self.minus:
                    M[i]=(k,a-Mod)


            A=["{} {} ^ {} ".format(a,self.Char,k) for k,a in M]
            S=" "+" + ".join(A)
            S=S.replace(" + -"," - ")
            S=S.replace(" {} ^ 0 ".format(self.Char),"")
            S=S.replace(" {} ^ 1 ".format(self.Char)," "+self.Char+" ")
            S=S.replace(" 1 {} ".format(self.Char),self.Char+" ")
            S=S.replace(" -1 {} ".format(self.Char),"-"+self.Char+" ") 
            S=S.replace(" ","")
        else:
            S="0"

        S+=" (mod (Z/ {0} Z)[{1}]/ ({1}^{2}))".format(Mod,self.Char,self.Max_Degree)
        return S.strip()

    def __repr__(self):
        return self.__str__()

    #=
    def __eq__(self,other):
        if self.Max_Degree!=other.Max_Degree:
            return False

        from itertools import zip_longest
        return all([a==b for a,b in zip_longest(self.Poly,other.Poly,fillvalue=0)])
    #+,-
    def __pos__(self):
        return self

    def __neg__(self):
        return self.scale(-1)

    #Boole
    def __bool__(self):
        return any(self.Poly)

    #簡略化
    def reduce(self):
        P_deg=self.degree()

        if not(P_deg>=0):
            self.Poly=[0]
            self.censor(self.Max_Degree)
            return

        for i in range(self.degree(),-1,-1):
            if self.Poly[i]:
                self.Poly=self.Poly[:i+1]
                self.censor(self.Max_Degree)
                return
        self.Poly=[]
        return

    #シフト
    def __lshift__(self,other):
        if other<0:
            return self>>(-other)

        if other>self.Max_Degree:
            return Modulo_Polynominal([0],self.Max_Degree,self.Char)

        G=[0]*other+self.Poly
        return Modulo_Polynominal(G,self.Max_Degree,self.Char)

    def __rshift__(self,other):
        if other<0:
            return  self<<(-other)

        return Modulo_Polynominal(self.Poly[other:],self.Max_Degree,self.Char)

    #次数
    def degree(self):
        d=len(self.Poly)-1
        for y in self.Poly[::-1]:
            if y:
                return d
            d-=1
        return -float("inf")

    #加法
    def __add__(self,other):
        P=self
        Q=other

        if Q.__class__==Modulo_Polynominal:
            from itertools import zip_longest
            N=min(P.Max_Degree,Q.Max_Degree)
            R=[(a+b)%Mod for (a,b) in zip_longest(P.Poly,Q.Poly,fillvalue=0)]
            return Modulo_Polynominal(R,N,P.Char)
        else:
            P_deg=P.degree()
            if P_deg<0:P_deg=0
            R=[0]*(P_deg+1)

            R=[p for p in P.Poly]
            R[0]=(R[0]+Q)%Mod

            R=Modulo_Polynominal(R,P.Max_Degree,P.Char)
            R.reduce()
            return R

    def __radd__(self,other):
        return self+other

    #減法
    def __sub__(self,other):
        return self+(-other)

    def __rsub__(self,other):
        return (-self)+other

    #乗法
    def __mul__(self,other):
        P=self
        Q=other
        if Q.__class__==Modulo_Polynominal:
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
            M=min(P.Max_Degree,Q.Max_Degree)
            if a<2*P.Max_Degree.bit_length():
                B=[0]*(len(U)+len(V)-1)
                for i in range(len(U)):
                    if U[i]:
                        for j in range(len(V)):
                            B[i+j]+=U[i]*V[j]
                            if B[i+j]>Mod:
                                B[i+j]-=Mod
            else:
                B=Convolution_Mod(U,V)[:M]
            B=Modulo_Polynominal(B,M,self.Char)
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

        F,G=self,other
        N=min(F.Max_Degree,G.Max_Degree)
        F_deg=F.degree()
        G_deg=G.degree()

        if F_deg<G_deg:
            A=Modulo_Polynominal([0],N,self.Char)
            A.reduce()
            return A

        G.reduce()
        F_inv=Modulo_Polynominal(F.Poly[::-1],F.Max_Degree,F.Char)
        G_inv=Modulo_Polynominal(G.Poly[::-1],F.Max_Degree,F.Char)

        H=F_inv/G_inv
        H.censor(F_deg-G_deg+1)
        return Modulo_Polynominal(H.Poly[::-1],N,self.Char)

    def __rfloordiv__(self,other):
        if not self:
            raise ZeroDivisionError

        if isinstance(other,int):
            return Modulo_Polynominal([0],self.Max_Degree,self.Char)

    #剰余
    def __mod__(self,other):
        if not other:
            return ZeroDivisionError
        return self-(self//other)*other

    def __rmod__(self,other):
        if not self:
            raise ZeroDivisionError
        return other-(other//self)*self

    def __divmod__(self,other):
        p=self//other
        return (p,self-other*p)

    #累乗
    def __pow__(self,other):
        if other.__class__==int:
            n=other
            m=abs(n)

            Q=self
            A=Modulo_Polynominal([1],self.Max_Degree,self.Char)
            while m>0:
                if m&1:
                    A*=Q
                m>>=1
                Q*=Q

            if n>=0:
                return A
            else:
                return A.__inv__()
        else:
            P=Log(self)
            return Exp(P*other)

    #逆元
    def __inv__(self,deg=None):
        assert self.Poly[0],"定数項が0"

        P=self
        if len(P.Poly)<=P.Max_Degree.bit_length():
            """
            愚直に漸化式を用いて求める.
            計算量:Pの次数をK, 求めたい項の個数をNとして, O(NK)
            """
            F=P.Poly
            c=F[0]
            c_inv=pow(c,Mod-2,Mod)

            N=len(P.Poly)
            R=[-c_inv*a%Mod for a in F[1:]][::-1]
            G=[0]*P.Max_Degree
            G[0]=1
            Q=[0]*(N-2)+[1]

            for k in range(1,P.Max_Degree):
                a=0
                for x,y in zip(Q,R):
                    a+=x*y
                a%=Mod
                G[k]=a
                Q.append(a)
                Q=Q[1:]

            G=[c_inv*g%Mod for g in G]
            return Modulo_Polynominal(G,P.Max_Degree,P.Char)
        else:
            """
            FFTの理論を応用して求める.
            計算量:求めたい項の個数をNとして, O(N log N)
            """
            if deg==None:
                deg=P.Max_Degree
            else:
                deg=min(deg,P.Max_Degree)

            F=P.Poly
            N=len(F)
            r=pow(F[0],Mod-2,Mod)

            m=1
            G=[r]
            while m<deg:
                T=F[:m<<1]
                H=Convolution_Mod(T,G)[m:m<<1]

                L=Convolution_Mod(H,G)[:m]
                for a in L:
                    G.append(Mod-a)
                m<<=1
            return Modulo_Polynominal(G[:deg],P.Max_Degree,P.Char)

    #除法
    def __truediv__(self,other):
        if isinstance(other,Modulo_Polynominal):
            return self*other.__inv__()
        else:
            return pow(other,Mod-2,Mod)*self

    def __rtruediv__(self,other):
        return other*self.__inv__()

    #スカラー倍
    def scale(self,s):
        P=self
        s%=Mod
        A=[(s*p)%Mod for p in P.Poly]
        A=Modulo_Polynominal(A,P.Max_Degree,P.Char)
        A.reduce()
        return A

    #係数
    def coefficient(self,n):
        try:
            if n<0:
                raise IndexError

            return self.Poly[n]
        except IndexError:
            return  0
        except TypeError:
            return 0

    #最高次の係数
    def leading_coefficient(self):
        for x in self.Poly[::-1]:
            if x:
                return x
        return 0

    def censor(self,n,Return=False):
        """ n次以上の係数をカット
        """
        if Return:
            return Modulo_Polynominal(self.Poly[:n],self.Max_Degree,self.Char)
        else:
            self.Poly=self.Poly[:n]

    def resize(self,n,Return=False):
        P=self
        if Return:
            if len(P.Poly)>n:
                E=P.Poly[:n]
            else:
                E=P.Poly+[0]*(n-P.Poly)
            return Modulo_Polynominal(E,P.Max_Degree,P.Char)
        else:
            if len(P.Poly)>n:
                del P.Poly[n:]
            else:
                P.Poly+=[0]*(n-len(P.Poly))
#=================================================
def Primitive_Root(p):
    """Z/pZ上の原始根を見つける

    p:素数
    """
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

#参考元 https://atcoder.jp/contests/practice2/submissions/16789717
def NTT(A):
    """AをMod を法とする数論変換を施す

    ※Modはグローバル変数から指定
    """
    primitive=Primitive_Root(Mod)

    N=len(A)
    H=(N-1).bit_length()

    if Mod==998_244_353:
        m=998_244_352
        u=119
        e=23
        S=[1,998244352,911660635,372528824,929031873,
        452798380,922799308,781712469,476477967,166035806,
        258648936,584193783,63912897,350007156,666702199,
        968855178,629671588,24514907,996173970,363395222,
        565042129,733596141,267099868,15311432]
    else:
        m=Mod-1
        e=((m&-m)-1).bit_length()
        u=m>>e
        S=[pow(primitive,(Mod-1)>>i,Mod) for i in range(e+1)]

    for l in range(H, 0, -1):
        d = 1 << l - 1
        U = [1]*(d+1)
        u = 1
        for i in range(d):
            u=u*S[l]%Mod
            U[i+1]=u

        for i in range(1 <<H - l):
            s=2*i*d
            for j in range(d):
                A[s],A[s+d]=(A[s]+A[s+d])%Mod, U[j]*(A[s]-A[s+d])%Mod
                s+=1

#参考元 https://atcoder.jp/contests/practice2/submissions/16789717
def Inverse_NTT(A):
    """AをMod を法とする逆数論変換を施す

    ※Modはグローバル変数から指定
    """
    primitive=Primitive_Root(Mod)

    N=len(A)
    H=(N-1).bit_length()

    if Mod==998244353:
        m=998_244_352
        e=23
        u=119
        S=[1,998244352,86583718,509520358,337190230,
        87557064,609441965,135236158,304459705,685443576,
        381598368,335559352,129292727,358024708,814576206,
        708402881,283043518,3707709,121392023,704923114,950391366,
        428961804,382752275,469870224]
    else:
        m=Mod-1
        e=(m&-m).bit_length()-1
        u=m>>e

        inv_primitive=pow(primitive,Mod-2,Mod)
        S=[pow(inv_primitive,(Mod-1)>>i,Mod) for i in range(e+1)]

    for l in range(1, H + 1):
        d = 1 << l - 1
        for i in range(1 << H - l):
            u = 1
            for j in range(2*i*d, (2*i+1)*d):
                A[j+d] *= u
                A[j], A[j+d] = (A[j] + A[j+d]) % Mod, (A[j] - A[j+d]) % Mod
                u = u * S[l] % Mod

    N_inv=pow(N,Mod-2,Mod)
    for i in range(N):
        A[i]=A[i]*N_inv%Mod

#参考元 https://atcoder.jp/contests/practice2/submissions/16789717
def Convolution_Mod(A,B):
    """A,BをMod を法とする畳み込みを求める.

    ※Modはグローバル変数から指定
    """
    if not A or not B:
        return []

    N=len(A)
    M=len(B)
    L=N+M-1
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

    NTT(A)
    NTT(B)

    for i in range(K):
        A[i]=A[i]*B[i]%Mod

    Inverse_NTT(A)
    return A[:L]

def Autocorrelation_Mod(A):
    """A自身に対して,Mod を法とする畳み込みを求める.

    ※Modはグローバル変数から指定
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

    NTT(A)

    for i in range(K):
        A[i]=A[i]*A[i]%Mod
    Inverse_NTT(A)

    return A[:L]

#以下 参考元https://judge.yosupo.jp/submission/28304
def inverse(F):
    G=[pow(F[0],Mod-2,Mod)]
    N=len(F)
    d=1
    while d<N:
        d<<=1
        H=[-v for v in Convolution_Mod(F[:d],G)[:d]]
        H[0]+=2
        G=Convolution_Mod(G,H)[:d]
    return G[:N]

def Differentiate(P):
    F=P.Poly
    G=[(k*a)%Mod for k,a in enumerate(F[1:],1)]+[0]
    return Modulo_Polynominal(G,P.Max_Degree,P.Char)

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
    return Modulo_Polynominal(G,P.Max_Degree,P.Char)

def Add(a, b):
    return [(va + vb) % Mod for va, vb in zip(a, b)]

def Sub(a, b):
    return [(va - vb) % Mod for va, vb in zip(a, b)]

def Times(a, k):
    return [v * k % Mod for v in a]

def Mul(a,b):
    return Convolution_Mod(a,b)

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
    N=P.Max_Degree

    Inv=[0]*(2*N+1)
    Inv[1]=1
    for i in range(2,2*N+1):
        q,r=divmod(Mod,i)
        Inv[i]=(-q*Inv[r])%Mod

    H=P.Poly
    assert (not H) or H[0]==0,"定数項が0でない"

    H+=[0]*(N-len(H))
    dH=[(k*a)%Mod for k,a in enumerate(H[1:],1)]
    F,G,m=[1],[1],1

    while m<=N:
        #2.a'
        if m>1:
            E=Convolution_Mod(F,Autocorrelation_Mod(G)[:m])[:m]
            G=[(2*a-b)%Mod for a,b in zip_longest(G,E,fillvalue=0)]
        #2.b', 2.c'
        C=Convolution_Mod(F,dH[:m-1])
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
        T=Convolution_Mod(G,S)[:m]
        #2.f'
        E=[0]*(m-1)+T
        E=[0]+[(Inv[k]*a)%Mod for k,a in enumerate(E,1)]
        U=[(a-b)%Mod for a,b in zip_longest(H[:2*m],E,fillvalue=0)][m:]
        #2.g'
        V=Convolution_Mod(F,U)[:m]
        #2.h'
        F+=V
        #2.i'
        m<<=1
    return Modulo_Polynominal(F[:N],P.Max_Degree,P.Char)

def Root(P,k):
    assert P.Poly[0]==1,"定数項が1ではない"
    k%=Mod
    assert k,"kが特異"
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

def Power(P,k):
    assert k>=0
    N=P.Max_Degree
    F=P.Poly
    F+=[0]*(N-len(F))
    for (d,p) in enumerate(F):
        if p:
            break
    else:
        return Modulo_Polynominal([0],P.Max_Degree,P.Char)

    if d*k>P.Max_Degree:
        return Modulo_Polynominal([0],P.Max_Degree,P.Char)

    p_inv=pow(p,Mod-2,Mod)
    Q=Modulo_Polynominal([(p_inv*a)%Mod for a in F[d:]],P.Max_Degree,P.Char)

    G=Exp(k*Log(Q)).Poly
    pk=pow(p,k,Mod)
    G=[0]*(d*k)+[(pk*a)%Mod for a in G]
    return Modulo_Polynominal(G,P.Max_Degree,P.Char)

#ルジャンドル記号
def Legendre(X):
    """ルジャンドル記号(a/p)を返す.

    ※法が素数のときのみ成立する.
    """

    if X==0:
        return 0
    elif pow(X,(Mod-1)//2,Mod)==1:
        return 1
    else:
        return -1

#根号
def Tonelli_Shanks(X):
    """X=a (mod p)のとき,r*r=a (mod p)を満たすrを返す.

    ※法pが素数のときのみ有効
    ※存在しないときはNoneが返り値
    """
    X%=Mod
    if Legendre(X)==-1:
        return None

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
def __sqrt(F,N):
    F+=[0]*(N-len(F))
    s=Tonelli_Shanks(F[0])
    if s==None:return None

    m=1
    G=[min(s,Mod-s)]
    two_inv=pow(2,Mod-2,Mod)

    while m<N:
        G+=[0]*m
        m<<=1
        H=Convolution_Mod(F[:m],inverse(G))
        G=[two_inv*(a+b)%Mod for a,b in zip(G,H)]
    return G[:N]

def Sqrt(P):
    N=P.Max_Degree
    F=P.Poly
    F+=[0]*(N-len(F))

    for d,p in enumerate(F):
        if p:break
    else:
        return Modulo_Polynominal([0],P.Max_Degree,P.Char)

    if d&1:return
    E=__sqrt(F[d:],N-d//2)

    if E==None:return
    if d>0:
        E=[0]*(d//2)+E
    return Modulo_Polynominal(E,P.Max_Degree,P.Char)

def Taylor_Shift(P,a):
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

    H=Convolution_Mod(F,G)[N:]
    for i in range(len(H)):
        H[i]=(H[i]*fact_inv[i])%Mod

    return Modulo_Polynominal(H,P.Max_Degree,P.Char)

"""
形式的ベキ級数を用いた応用的な内容
"""
#Bernoulli
def Bernoulli(N):
    """ベルヌーイ数 B_0,B_1,...,B_Nの(mod Mod)での値を求める.
    """

    if N==0:
        return [1]

    X=Modulo_Polynominal([0,1],N+2)
    P=Exp(X)>>1
    F=(1/P).Poly

    fact=1
    for i in range(N+1):
        F[i]=(F[i]*fact)%Mod
        fact=(fact*(i+1))%Mod

    del F[-1]
    return F

def Partition(N):
    """分割数 p(0),...,p(N) (mod Mod) を求める.

    p(k):=kを順序を区別せずに自然数の和に分ける場合の数
    """

    F=[0]*(N+1)
    F[0]=1
    k=1
    while k*(3*k-1)<=2*N:
        m=-1 if k&1 else 1
        F[k*(3*k-1)//2]+=m

        if k*(3*k+1)<=2*N:
            F[k*(3*k+1)//2]+=m
        k+=1

    return (1/Modulo_Polynominal(F,N+1)).Poly

def Subset_Sum(X,K):
    """Xの要素のうち,任意個を用いて, 和がk=0,1,...,Kになる組み合わせの総数をModで割った余りを求める.

    X:リスト
    K:非負整数
    """
    A=[0]*(K+1)
    for x in X:
        if x<=K:
            A[x]+=1

    Inv=[0]*(K+1)
    Inv[1]=1
    for i in range(2,K+1):
        Inv[i]=(-(Mod//i)*Inv[Mod%i])%Mod

    F=[0]*(K+1)
    for i in range(1,K+1):
        j=i
        k=1
        c=1
        while j<=K:
            F[j]=(F[j]+c*Inv[k]*A[i])%Mod
            c*=-1
            j+=i
            k+=1
    P=Modulo_Polynominal(F,K+1)
    return Exp(P).Poly

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

#divmod
def divmod(x,y):
    a=x//y
    return (a,x-a*y)
#=================================================
Mod=998244353
X=Modulo_Polynominal([0,1],15)
F=X+3*X**2
