class Modulo_Error(Exception):
    pass

class Modulo():
    __slots__=["a","n"]

    def __init__(self,a,n):
        self.a=a%n
        self.n=n

    def __str__(self):
        return "{} (mod {})".format(self.a,self.n)

    def __repr__(self):
        return self.__str__()

    #+,-
    def __pos__(self):
        return self

    def __neg__(self):
        return  Modulo(-self.a,self.n)

    #等号,不等号
    def __eq__(self,other):
        if isinstance(other,Modulo):
            return (self.a==other.a) and (self.n==other.n)
        elif isinstance(other,int):
            return (self-other).a==0

    def __neq__(self,other):
        return not(self==other)

    def __le__(self,other):
        a,p=self.a,self.n
        b,q=other.a,other.n
        return (a-b)%q==0 and p%q==0

    def __ge__(self,other):
        return other<=self

    def __lt__(self,other):
        return (self<=other) and (self!=other)

    def __gt__(self,other):
        return (self>=other) and (self!=other)

    def __contains__(self,val):
        return val%self.n==self.a

    #加法
    def __add__(self,other):
        if isinstance(other,Modulo):
            if self.n!=other.n:
                raise Modulo_Error("異なる法同士の演算です.")
            return Modulo(self.a+other.a,self.n)
        elif isinstance(other,int):
            return Modulo(self.a+other,self.n)

    def __radd__(self,other):
        if isinstance(other,int):
            return Modulo(self.a+other,self.n)

    def __iadd__(self,other):
        if isinstance(other,Modulo):
            if self.n!=other.n: raise Modulo_Error("異なる法同士の演算です.")
            self.a+=other.a
            if self.a>=self.n: self.a-=self.n
        elif isinstance(other,int):
            self.a+=other
            if self.a>=self.n: self.a-=self.n
        return self

    #減法
    def __sub__(self,other):
        return self+(-other)

    def __rsub__(self,other):
        if isinstance(other,int):
            return -self+other

    def __isub__(self,other):
        if isinstance(other,Modulo):
            if self.n!=other.n: raise Modulo_Error("異なる法同士の演算です.")
            self.a-=other.a
            if self.a<0: self.a+=self.n
        elif isinstance(other,int):
            self.a-=other
            if self.a<0: self.a+=self.n
        return self

    #乗法
    def __mul__(self,other):
        if isinstance(other,Modulo):
            if self.n!=other.n:
                raise Modulo_Error("異なる法同士の演算です.")
            return Modulo(self.a*other.a,self.n)
        elif isinstance(other,int):
            return Modulo(self.a*other,self.n)

    def __rmul__(self,other):
        if isinstance(other,int):
            return Modulo(self.a*other,self.n)

    def __imul__(self,other):
        if isinstance(other,Modulo):
            if self.n!=other.n: raise Modulo_Error("異なる法同士の演算です.")
            self.a*=other.a
        elif isinstance(other,int):
            self.a*=other
        self.a%=self.n
        return self

    #Modulo逆数
    def inverse(self):
        return self.Modulo_Inverse()

    def Modulo_Inverse(self):
        s,t=1,0
        a,b=self.a,self.n
        while b:
            q,a,b=a//b,b,a%b
            s,t=t,s-q*t

        if a!=1:
            raise Modulo_Error("{}の逆数が存在しません".format(self))
        else:
            return Modulo(s,self.n)

    #除法
    def __truediv__(self,other):
        return self*(other.Modulo_Inverse())

    def __rtruediv__(self,other):
        return other*(self.Modulo_Inverse())

    #累乗
    def __pow__(self,other):
        if isinstance(other,int):
            u=abs(other)

            r=Modulo(pow(self.a,u,self.n),self.n)
            if other>=0:
                return r
            else:
                return r.Modulo_Inverse()
        else:
            b,n=other.a,other.n
            if pow(self.a,n,self.n)!=1:
                raise Modulo_Error("矛盾なく定義できません.")
            else:
                return self**b

"""
初等的
"""
def Modulo_Inverse_List(M:int,K:int):
    """
    1^(-1), 2^(-1), ... , K^(-1) (mod N) のリストを出力する.

    [入力]
    M,K:整数
    M>0, K>=1
    K=min(M-1,K) に変換される.

    [出力]
    長さ K+1 のリスト F
    k=1,2,...,K に対して, F[k]=k^(-1) mod M
    また, k^(-1) mod M が存在しない場合, F[k]=None
    """

    assert M>0 and K>=1

    if K==None:
        K=M-1
    K=min(K,M-1)

    F=[None,Modulo(1,M)]
    for k in range(2,K+1):
        q,r=divmod(M,k)
        if F[r]!=None:
            F.append(-q*F[r])
        else:
            F.append(None)
    return F

#細分化
def Subdivision(X:Modulo,M:int):
    """Xをx (mod M) の形に細分化する.

    X.n|Mでなくてはならない.
    """

    assert M%X.n==0,"X.n|Mではありません."

    k=M//X.n
    return [Modulo(X.n*i+X.a,M) for i in range(k)]

#退化
def Degenerate(X:Modulo, M:int):
    """ X の情報を退化させる. X=x (mod N) であるとき, mod M での情報に退化させる.

    M|X.n でなくてはならない.
    """

    assert X.n%M==0,"M|X.n ではありません."
    return Modulo(X.a%M,M)

"""
線形合同方程式関連
"""
#法の合成
def __modulo_composite__(p:Modulo,q:Modulo):
    """2つの等式 x ≡ p.a (mod p.n), x ≡ q.a (mod q.n) をともに満たす x を全て求める.
    """
    from math import gcd

    a,n=p.a,p.n
    b,m=q.a,q.n

    d=b-a

    g,h=n,m
    while h:
        g,h=h,g%h

    if d%g:
        return None
        #raise Modulo_Error("{}と{}は両立しません.".format(p,q))

    n//=g;m//=g;d//=g

    s=(1/Modulo(n,m)).a

    return Modulo(a+(n*g)*d*s,n*m*g)

def Modulo_Composite(*X:Modulo):
    """ N個の方程式 x ≡ a (mod n) を全て満たす x を mod の形で求める.
    """
    x=Modulo(0,1)
    for a in X:
        x=__modulo_composite__(x,a)
    return x

def Is_Included(X:Modulo,Y:Modulo):
    """Xを全て満たす整数はYを全て満たすか?

    X,Y:Modulo
    """
    a,p=X.a,X.n
    b,q=Y.a,Y.n
    return (a-b)%q==0 and p%q==0

#拡張Euclidの互除法
def Extended_Euclid(a:int,b:int):
    """ax+by=gcd(a,b) を満たす(x,y,gcd(a,b))を1つ求める.

    a,b:整数
    """
    s,t,u,v=1,0,0,1
    while b:
        q,a,b=a//b,b,a%b
        s,t=t,s-q*t
        u,v=v,u-q*v
    return s,u,a

#1次合同方程式を解く
def First_Order_Congruent_Equation(a:int,b:int,m:int):
    """1次合同方程式 ax≡b (mod m) を求める.

    a,b,m:整数
    m!=0
    """
    assert m
    g=a;h=m
    while h:
        g,h=h,g%h

    if b%g:
        return None

    a,b,m=a//g,b//g,m//g
    c,_,_=Extended_Euclid(a,m)
    return Modulo(b*c,m)

#1次連立合同方程式を解く
def First_Order_Simultaneous_Congruent_Equation(*X):
    """1次合同方程式 a_i x≡b_i (mod m_i) を求める.

    [Input]
    X:(a,b,m) という形のタプル
    """
    R=Modulo(0,1)
    for (a,b,m) in X:
        T=First_Order_Congruent_Equation(a,b,m)
        if T==None:
            return None
        R=__modulo_composite__(R,T)
    return R

"""
有限体の操作関連
"""
#ルジャンドル記号
def Legendre(X):
    """ルジャンドル記号(a/p)を返す.

    ※法が素数のときのみ成立する.
    """

    if X==0:
        return 0
    elif pow(X,(X.n-1)//2)==1:
        return 1
    else:
        return -1

#根号
def sqrt(X,All=False):
    """X=a (mod p)のとき,r*r=a (mod p)を満たすrを返す.

    ※法pが素数のときのみ有効
    ※存在しないときはNoneが返り値
    """
    if Legendre(X)==-1:
        return None

    a,p=X.a,X.n

    if X==0:
        return X
    elif p==2:
        return X
    elif p%8==3 or p%8==7:
        r=pow(X,(p+1)//4)
        if All:
            return (r,-r)
        else:
            return r
    elif p%8==5:
        if pow(X,(p-1)//4)==1:
            r=pow(X,(p+3)//8)
        else:
            r=pow(2,(p-1)//4,p)*pow(X,(p+3)//8)

        if All:
            return (r,-r)
        else:
            return r

    from random import randint as ri
    u=2
    s=1
    while (p-1)%(2*u)==0:
        u*=2
        s+=1
    q=(p-1)//u

    z=Modulo(0,p)
    while pow(z,(p-1)//2)!=-1:
        z=Modulo(ri(1,p-1),p)

    m,c,t,r=s,z**q,X**q,pow(X,(q+1)//2)
    while m>1:
        if pow(t,2**(m-2))==1:
            c=c*c
            m=m-1
        else:
            c,t,r,m=c*c,c*c*t,c*r,m-1

    if All:
        return (r,-r)
    else:
        return r

#離散対数
def Discrete_Log(A,B):
    """A^X=B (mod M)を満たす最小の非負整数Xを求める.

    [入力]
    A:底
    B:
    [出力]
    A^X=B (mod M)を満たす非負整数Xが存在すればその中で最小のもの
    存在しなければ-1
    """
    if isinstance(B,int):
        B%=A.n
    elif isinstance(B,Modulo):
        assert A.n==B.n,"A,Bの法が違います."
        B=B.a
    else:
        raise TypeError

    A,M=A.a,A.n

    #A=0の時を処理
    if M==1:
        return 0
    if B==1:
        return 0
    if A==B==0:
        return 1

    D={1:0}
    S=int(M**0.5)+2

    #Baby-Step
    Baby=1
    for i in range(S):
        if Baby==B:
            return i
        D[(Baby*B)%M]=i
        Baby=(Baby*A)%M

    #Giant-Step
    Giant=1
    H=pow(A,S,M)
    for i in range(1,S+1):
        Giant=(Giant*H)%M
        if Giant in D:
            j=D[Giant]
            X=i*S-j
            return X if pow(A,X,M)==B else None
    return None

def Order(X):
    """Xの位数を求める. つまり, X^k=[1] を満たす最小の正整数 k を求める.
    """
    R=X.n
    N=X.n
    k=2
    while k*k<=N:
        if N%k==0:
            R-=R//k
            while N%k==0:
                N//=k
        k+=1

    if N>1:
        R-=R//N

    D=[]
    k=1
    while k*k<=R:
        if R%k==0:
            D.append(k)
            D.append(R//k)
        k+=1

    a=float("inf")
    for k in D:
        if pow(X,k)==1:
            a=min(a,k)
    return a

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
    if p==469762049:
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

Mod=10**9+7
X=Modulo(3,Mod)
Y=Modulo(193,Mod)

"""
数え上げ関連
"""
def Factor_Modulo(N,M,Mode=0):
    """
    Mode=0のとき:N! (mod M) を求める.
    Mode=1のとき:k! (mod M) (k=0,1,...,N) のリストも出力する.

    [計算量]
    O(N)
    """

    if Mode==0:
        X=Modulo(1,M)
        for k in range(1,N+1):
            X*=k
        return X
    else:
        L=[Modulo(1,M)]*(N+1)
        for k in range(1,N+1):
            L[k]=k*L[k-1]
        return L

def Factor_Modulo_with_Inverse(N,M):
    """
    k=0,1,...,N に対する k! (mod M) と (k!)^(-1) (mod M) のリストを出力する.

    [入力]
    N,M:整数
    M>0
    [出力]
    長さ N+1 のリストのタプル (F,G):F[k]=k! (mod M), G[k]=(k!)^(-1) (mod M)
    [計算量]
    O(N)
    """

    assert M>0

    F=Factor_Modulo(N,M,Mode=1)
    G=[0]*(N+1)

    G[-1]=F[-1].inverse()
    for k in range(N,0,-1):
        G[k-1]=k*G[k]
    return F,G

def Binomial_Coefficient_Modulo(n,r,M):
    """
    nCr (mod M) を求める.

    [入力]
    n,r,M:整数
    M>0
    [出力]
    nCr (mod M)
    [計算量]
    O(r)
    """
    assert M>0
    if r<0 or n<r:
        return Modulo(0,M)

    X=Modulo(1,M)
    Y=Modulo(1,M)

    r=min(r,n-r)
    for i in range(r):
        X*=n-i
        Y*=r-i
    return X/Y

def Binomial_Coefficient_Modulo_List(n,M):
    """
    nを固定し, r=0,1,...,n としたときの nCr (mod M) のリストを出力する.

    [入力]
    N,M:整数
    M>0
    [出力]
    [nC0 (mod M), nC1 (mod M),..., nCn (mod M)]
    [計算量]
    O(n)
    """

    assert M>0
    L=[Modulo(1,M) for _ in range(n+1)]

    I=Modulo_Inverse_List(M,n)
    for r in range(1,n+1):
        L[r]=(n+1-r)*I[r]*L[r-1]
    return L

def Pascal_Triangle(N,M):
    """
    0<=n<=N, 0<=r<=n の全てに対して nCr (mod M) のリストを出力する.

    [入力]
    N,M:整数
    M>0
    [出力] (mod M) を省略.
    [[0C0], [1C0, 1C1], ... , [nC0, ... , nCn], ..., [NC0, ..., NCN]]
    [計算量]
    O(N^2)
    """

    X=[Modulo(1,M)]
    L=[[Modulo(1,M)]]
    for n in range(N):
        Y=[Modulo(1,M)]
        for k in range(1,n+1):
            Y.append(X[k]+X[k-1])
        Y.append(Modulo(1,M))
        X=Y
        L.append(Y)
    return L
