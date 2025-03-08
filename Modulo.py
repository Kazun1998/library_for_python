class Modulo:
    __slots__ = ("_a", "_n")

    @property
    def a(self):
        return self._a

    @property
    def n(self):
        return self._n

    def __init__(self, a: int, n: int, mode: bool = True):
        if mode:
            a %= n

        self._a = a
        self._n = n

    def __str__(self):
        return f"{self.a} (mod {self.n})"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.a}, {self.n})"

    #+,-
    def __pos__(self):
        return self

    def __neg__(self):
        return Modulo(self.n - self.a, self.n, False) if self.a else Modulo(0, self.n, False)

    #等号,不等号
    def __eq__(self, other):
        if isinstance(other, Modulo):
            return (self.a == other.a) and (self.n == other.n)
        elif isinstance(other, int):
            return (self.a - other) % self.n == 0

    def __neq__(self, other):
        return not(self == other)

    def __le__(self, other):
        a, p = self.a, self.n
        b, q = other.a, other.n
        return (a - b) % q == 0 and p % q == 0

    def __ge__(self, other):
        return other <= self

    def __lt__(self, other):
        return (self <= other) and (self != other)

    def __gt__(self, other):
        return (self >= other) and (self != other)

    def __contains__(self, val):
        return val % self.n == self.a

    #加法
    def __add__(self,other):
        if isinstance(other,Modulo):
            assert self.n==other.n, "異なる法同士の演算です."
            y=other.a
        elif isinstance(other,int):
            y=other%self.n

        b=self.a+y
        if self.n<=b:
            b-=self.n
        return Modulo(b,self.n, False)

    def __radd__(self,other):
        if isinstance(other,int):
            b=self.a+(other%self.n)
            if b>=self.n:
                b-=self.n
            return Modulo(b,self.n, False)

    def __iadd__(self,other):
        if isinstance(other,Modulo):
            assert self.n==other.n, "異なる法同士の演算です."
            y=other.a
        elif isinstance(other,int):
            y=other%self.n

        self.a+=y
        if self.a>=self.n:
            self.a-=self.n
        return self

    #減法
    def __sub__(self,other):
        if isinstance(other,Modulo):
            assert self.n==other.n, "異なる法同士の演算です."
            y=other.a
        elif isinstance(other,int):
            y=other%self.n

        b=self.a-y
        if b<0:
            b+=self.n
        return Modulo(b,self.n, False)

    def __rsub__(self,other):
        if isinstance(other,int):
            b=other%self.n-self.a
            if b<0:
                b+=self.n
            return Modulo(b,self.n, False)

    def __isub__(self,other):
        if isinstance(other,Modulo):
            assert self.n==other.n, "異なる法同士の演算です."
            y=other.a
        elif isinstance(other,int):
            y=other%self.n

        self.a-=y
        if self.a<0:
            self.a+=self.n
        return self

    #乗法
    def __mul__(self,other):
        if isinstance(other,Modulo):
            assert self.n==other.n, "異なる法同士の演算です."
            y=other.a
        elif isinstance(other,int):
            y=other%self.n

        return Modulo((self.a*y)%self.n, self.n, False)

    def __rmul__(self,other):
        if isinstance(other,int):
            return Modulo((self.a*other)%self.n, self.n, False)

    def __imul__(self,other):
        if isinstance(other,Modulo):
            assert self.n==other.n, "異なる法同士の演算です."
            y=other.a
        elif isinstance(other,int):
            y=other%self.n

        self.a*=y
        self.a%=self.n
        return self

    #Modulo逆数
    def inverse(self):
        return self.modulo_inverse()

    def modulo_inverse(self):
        try:
            return Modulo(pow(self.a, -1, self.n), self.n, False)
        except ValueError:
            raise ValueError(f"{self} の逆数が存在しません") from None

    #除法
    def __truediv__(self,other):
        return self*(other.modulo_inverse())

    def __rtruediv__(self,other):
        return other*(self.modulo_inverse())

    #累乗
    def __pow__(self, other):
        if isinstance(other, int):
            return Modulo(pow(self.a, other, self.n), self.n, False)
        else:
            b,n=other.a,other.n
            assert pow(self.a,n,self.n)==1, "矛盾なく定義できません."
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
    """ X をx (mod M) の形に細分化する.

    X.n | Mでなくてはならない.
    """

    assert M%X.n==0,"X.n | M ではありません."

    k=M//X.n
    return [Modulo(X.n*i+X.a,M) for i in range(k)]

#退化
def Degenerate(X:Modulo, M:int):
    """ X の情報を退化させる. X=x (mod N) であるとき, mod M での情報に退化させる.

    M | X.n でなくてはならない.
    """

    assert X.n%M==0,"M | X.n ではありません."
    return Modulo(X.a%M,M)

def Chinese_Remainder(X: Modulo):
    """ 中国剰余定理により, Xを分解する.

    """

    Y=[]

    a,N=X.a,X.n
    e=(N&(-N)).bit_length()-1
    if e>0:
        N>>=e
        Y.append(Modulo(a,1<<e))

    e=0
    while N%3==0:
        e+=1
        N//=3

    if e>0:
        Y.append(Modulo(a,pow(3,e)))

    flag=0
    p=5
    while p*p<=N:
        if N%p==0:
            e=0
            while N%p==0:
                e+=1
                N//=p

            Y.append(Modulo(a,pow(p,e)))

        p+=2+2*flag
        flag^=1

    if N>1:
        Y.append(Modulo(a,N))

    return Y

"""
線形合同方程式関連
"""
#法の合成
def __modulo_composite__(p: Modulo, q: Modulo) -> Modulo | None:
    """ 2つの等式 x ≡ p.a (mod p.n), x ≡ q.a (mod q.n) をともに満たす x を全て求める.

    Args:
        p (Modulo):
        q (Modulo):

    Returns:
        Modulo | None: 条件を満たすことが必要十分になる Modulo. 存在しない場合は None
    """
    from math import gcd

    a, n = p.a, p.n
    b, m = q.a, q.n

    d = b - a
    g = gcd(n, m)

    if d % g:
        return None

    n //= g
    m //= g
    d //= g

    s = pow(n, -1, m)

    return Modulo(a + (n * g) * d * s, n * m *g)

def Modulo_Composite(*X: Modulo) -> Modulo:
    """ N個の方程式 x ≡ a (mod n) を全て満たす x を mod の形で求める.
    """
    x=Modulo(0,1)
    for a in X:
        x=__modulo_composite__(x,a)
    return x

def Is_Included(X: Modulo, Y: Modulo):
    """ X を全て満たす整数は Y を全て満たすか?

    X,Y: Modulo
    """
    a,p=X.a,X.n
    b,q=Y.a,Y.n
    return (a-b)%q==0 and p%q==0

#拡張Euclidの互除法
def Extended_Euclid(a: int, b: int):
    """ax+by=gcd(a, b) を満たす (x, y, gcd(a, b)) を 1 つ求める.

    a,b:整数
    """
    from math import gcd
    g = gcd(a, b)
    if g == 0:
        return (0, 0, 0)

    x = pow(a//g, -1, b//g)
    y = - (a*x-g) // b
    return (x, y, g)

#1次合同方程式を解く
def First_Order_Congruent_Equation(a: int, b: int, m: int) -> Modulo:
    """ 1次合同方程式 a x ≡ b (mod m) を求める.

    Args:
        a (int):
        b (int):
        m (int): m != 0

    Returns:
        Modulo: 条件を満たす X が存在しない場合は None.
    """
    from math import gcd

    if m == 0:
        raise ValueError

    g = gcd(a, m)

    # 存在確認
    if b % g:
        return None

    a, b, m = a // g, b // g, m // g
    c = pow(a, -1, m)
    return Modulo(b * c, m)

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
総和
"""

def Geometric_Sum(X, L, R):
    """ sum_{i=L}^R X^i を求める.

    X: modulo
    0<=L<=R
    """
    assert 0<=L
    if L>R:
        return 0

    a=X.a; m=X.n
    def calc(K):
        """ sum_{i=0}^{K-1} a^i
        """

        if K==0:
            return 0
        elif K%2==0:
            return (1+pow(a, K//2, m))*calc(K//2)%m
        else:
            return (1+a*calc(K-1))%m

    return Modulo(calc(R+1)-calc(L), m)

"""
有限体の操作関連
"""
#ルジャンドル記号
def Legendre(X: Modulo) -> int:
    """ ルジャンドル記号 (a/p) を返す. ※ 法が素数のときのみ成立する.

    Args:
        X (Modulo):

    Returns:
        int:
            X = 0 のときは 0
            X が平方剰余のときは 1
            X が平方非剰余のときは -1
    """
    if 0 in X:
        return 0

    return 1 if pow(X, (X.n - 1) // 2) == 1 else -1

#根号
def Sqrt(X, All=False):
    """ X=a (mod p) のとき, r*r=a (mod p) を満たす r を (存在すれば) 返す.

    [Input]
    All: False ならば一方のみ, True ならば両方
    ※ 法 p が素数のときのみ有効
    ※ 存在しないときは None が返り値
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
def Discrete_Log(A: Modulo, B: Modulo | int, default: int = -1) -> int | None:
    """ A^x ≡ B を満たす最小の非負整数 x を求める.

    Args:
        A (Modulo): 底
        B (Modulo | int): 真数
        default (int, optional): 存在しないときの返り値. Defaults to -1.

    Raises:
        ValueError: A, B 共に Modulo のときは法を一致させなければならない.

    Returns:
        int | None: A^x ≡ B を満たす最小の非負整数 x (存在しない場合は default).
    """

    A, M = A.a, A.n

    if isinstance(B, int):
        B %= M
    elif isinstance(B, Modulo):
        if M != B.n:
            raise ValueError
        B = B.a % M
    else:
        raise NotImplementedError

    m = 0
    while m * m < M:
        m += 1

    E = set()
    y = B
    for _ in range(m):
        y *= A; y %= M
        E.add(y)

    step = pow(A, m, M)
    head = 1 % M
    count = 0
    for k in range(1, m + 1):
        tail = head
        head = step * head % M

        if head not in E:
            continue

        body = tail
        for n in range((k - 1) * m, k * m):
            if body == B:
                return n

            body = (A * body) % M

        count += 1
        if count == 2:
            break

    return default

def Order(X: Modulo, defalut: int = -1) -> int:
    """ X^k = 1 を満たす最小の正の整数 k を求める (存在しない場合は -1)

    Args:
        X (Modulo): 底
        defalut (int, optional): 存在しない場合の値. Defaults to -1.

    Returns:
        int: X^k を満たす最小の k
    """

    phi=1
    N=X.n

    e=(N&(-N)).bit_length()-1
    if e>0:
        phi=1<<(e-1)
        N>>=e
    else:
        phi=1

    e=0
    while N%3==0:
        e+=1
        N//=3

    if e>0:
        phi*=pow(3,e-1)*2

    flag=0
    p=5
    while p*p<=N:
        if N%p==0:
            e=0
            while N%p==0:
                e+=1
                N//=p

            phi*=pow(p,e-1)*(p-1)

        p+=2+2*flag
        flag^=1

    if N>1:
        phi*=N-1

    a=float("inf")
    k=1
    while k*k<=phi:
        if phi%k==0:
            if k<a and pow(X,k)==1:
                a=k
                break

            if phi//k<a and pow(X,phi//k)==1:
                a=phi//k
        k+=1

    return a if a < float("inf") else defalut

def Primitive_Root(p):
    """ Z/pZ 上の原始根を見つける

    p: 素数
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

"""
数え上げ関連
"""
def Factor_Modulo(N, Mod, Mode=0):
    """
    Mode=0: N! (mod Mod) を求める.
    Mode=1: k! (mod Mod) (k=0,1,...,N) のリストも出力する.

    [計算量]
    O(N)
    """

    if Mode==0:
        X=1
        for k in range(1,N+1):
            X*=k; X%=Mod
        return Modulo(X,Mod)
    else:
        L=[Modulo(1,Mod)]*(N+1)
        for k in range(1,N+1):
            L[k]=k*L[k-1]
        return L

def Factor_Modulo_with_Inverse(N, Mod):
    """ k=0,1,...,N に対する k! (mod Mod) と (k!)^(-1) (mod Mod) のリストを出力する.

    [入力]
    N, Mod: 整数
    Mod >0
    [出力]
    長さ N+1 のリストのタプル (F,G): F[k]=k! (mod M), G[k]=(k!)^(-1) (mod M)
    [計算量]
    O(N+log Mod)
    """

    assert Mod>0

    F=Factor_Modulo(N,Mod,Mode=1)
    G=[0]*(N+1)

    G[-1]=F[-1].inverse()
    for k in range(N,0,-1):
        G[k-1]=k*G[k]
    return F,G

def Binomial_Coefficient_Modulo(n: int, r: int, Mod:int):
    """ nCr (mod Mod) を愚直な方法で求める.

    [入力]
    n, r, Mod: 整数
    Mod>0
    [出力]
    nCr (mod Mod)
    [計算量]
    O(r)
    """
    assert Mod>0
    if r<0 or n<r:
        return Modulo(0,Mod)

    X=Y=1

    r=min(r,n-r)
    for i in range(r):
        X*=n-i; X%=Mod
        Y*=r-i; Y%=Mod
    return Modulo(X,Mod)/Modulo(Y,Mod)

def Binomial_Coefficient_Modulo_List(n:int, Mod:int):
    """ n を固定し, r=0,1,...,n としたときの nCr (mod Mod) のリストを出力する.

    [入力]
    n,Mod: 整数
    Mod>0
    [出力]
    [nC0 (mod Mod), nC1 (mod Mod),..., nCn (mod Mod)]
    [計算量]
    O(n)
    """

    assert Mod>0
    L=[Modulo(1,Mod) for _ in range(n+1)]

    I=Modulo_Inverse_List(Mod,n)
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
