"""
Mod はグローバル変数からの指定とする.
"""

"""
積
"""
def product_modulo(*X):
    y=1
    for x in X:
        y=(x*y)%Mod
    return y

"""
階乗
"""
def Factor(N):
    """ 0!, 1!, ..., N! (mod Mod) を出力する.

    N: int
    """
    f=[1]*(N+1)
    for k in range(1,N+1):
        f[k]=(k*f[k-1])%Mod
    return f

def Factor_with_inverse(N):
    """ 0!, 1!, ..., N!, (0!)^-1, (1!)^-1, ..., (N!)^-1 を出力する.

    N: int
    """

    f=Factor(N)
    g=[1]*(N+1); g[-1]=pow(f[-1],Mod-2,Mod)

    for k in range(N-1,-1,-1):
        g[k]=((k+1)*g[k+1])%Mod
    return f,g

def Double_Factor(N):
    """ 0!!, 1!!, ..., N!! (mod Mod) を出力する.

    N: int
    """
    f=[1]*(N+1)
    for i in range(2,N+1):
        f[i]=i*f[i-2]%Mod
    return f

def Modular_Inverse(N):
    """ 1^(-1), 2^(-1), ..., N^(-1) (mod Mod) を出力する.

    [Input]
    N:int

    [Output]
    [-1, 1^(-1), 2^(-1), ..., N^(-1)] (第 0 要素に注意!!)
    """

    inv=[1]*(N+1); inv[0]=-1
    for k in range(2, N+1):
        q,r=divmod(Mod,k)
        inv[k]=(-q*inv[r])%Mod
    return inv    
    
"""
組み合わせの数
Factor_with_inverse で fact, fact_inv を既に求めていることが前提 (グローバル変数)
"""

def nCr(n,r):
    """ nCr (1,2,...,n から相異なる r 個の整数を選ぶ方法) を求める.

    n,r: int
    """

    if 0<=r<=n:
        return fact[n]*(fact_inv[r]*fact_inv[n-r]%Mod)%Mod
    else:
        return 0

def nPr(n,r):
    """ nPr (1,2,...,n から相異なる r 個の整数を選び, 並べる方法) を求める.

    n,r: int
    """

    if 0<=r<=n:
        return (fact[n]*fact_inv[n-r])%Mod
    else:
        return 0

def nHr(n,r):
    """ nHr (1,2,...,n から重複を許して r 個の整数を選ぶ方法) を求める.

    n,r: int
    ※ fact, fact_inv は第 n+r-1 項まで必要
    """

    if n==r==0:
        return 1
    else:
        return nCr(n+r-1,r)

def Multinomial_Coefficient(*K):
    """ K=[k_0,...,k_{r-1}] に対して, k_0, ..., k_{r-1} に対する多項係数を求める.

    k_i: int
    """

    N=0
    g_inv=1
    for k in K:
        N+=k
        g_inv*=fact_inv[k]; g_inv%=Mod
    return (fact[N]*g_inv)%Mod

def Binomial_Coefficient_Modulo_List(n: int):
    """ n を固定し, r=0,1,...,n としたときの nCr (mod Mod) のリストを出力する.

    n: int

    [出力]
    [nC0 , nC1 ,..., nCn]
    """

    L=[1]*(n+1)
    inv=Modular_Inverse(n+1)
    for r in range(1, n+1):
        L[r]=((n+1-r)*inv[r]%Mod)*L[r-1]%Mod
    return L

def Pascal_Triangle(N: int):
    """
    0<=n<=N, 0<=r<=n の全てに対して nCr (mod M) のリストを出力する.

    N: int

    [出力]
    [[0C0], [1C0, 1C1], ... , [nC0, ... , nCn], ..., [NC0, ..., NCN]]
    """

    X=[1]
    L=[[1]]
    for n in range(N):
        Y=[1]
        for k in range(1,n+1):
            Y.append((X[k]+X[k-1])%Mod)
        Y.append(1)
        X=Y
        L.append(Y)
    return L

"""
等比数列
"""

def Geometric_Sequence(a, r, N):
    """ k=0,1,...,N に対する a*r^k を出力する.

    a,r,N: int
    """

    a%=Mod; r%=Mod
    X=[0]*(N+1); X[0]=a
    for k in range(1,N+1):
        X[k]=r*X[k-1]%Mod
    return X

def Geometric_Inverse_Sequence(a, r, N):
    """ k=0,1,...,N に対する a/r^k を出力する.

    a,r,N: int
    """

    a%=Mod; r_inv=pow(r, Mod-2, Mod)
    X=[0]*(N+1); X[0]=a
    for k in range(1,N+1):
        X[k]=r_inv*X[k-1]%Mod
    return X

"""
積和
"""
def Sum_of_Product(*X):
    """ 長さが等しいリスト X_1, X_2, ..., X_k に対して, sum(X_1[i]*X_2[i]*...*X_k[i]) を求める.
    """

    S=0
    for alpha in zip(*X):
        S+=product_modulo(*alpha)
    return S%Mod

def Sum_of_Product_Yielder(N,*Y):
    S=0
    M=len(Y)
    for _ in range(N+1):
        x=1
        for j in range(M):
            x*=next(Y[j]); x%=Mod
        S+=x
    return S%Mod
#==================================================
Mod=998244353
fact, fact_inv=Factor_with_inverse(100)