from Modulo_Polynomial import *

def Nth_Term_of_Linearly_Recurrent_Sequence(A: list[int], C: list[int], n: int, offset: int = 0) -> int:
    """ A[i] = C[0] * A[i - 1] + C[1] * A[i - 2] + ... + C[d - 1] * A[i - d] で表される数列 (A[i]) の第 n 項を求める.

    Args:
        A (list[int]): A = (A[0], ..., A[d - 1]): 最初の d 項
        C (list[int]): C = (C[0], ..., C[d - 1]): 線形漸化式の係数
        n (int): 求める項数
        offset (int, optional): ずらす項数 (初項を第 offset 項とする). Defaults to 0.

    Raises:
        ValueError: len(A) != len(C) の場合に発生

    Returns:
        int: A[n]
    """

    if not len(A) == len(C):
        raise ValueError("len(A) == len(C) でなくてはなりません")

    d = len(A)
    n -= offset

    if n < 0:
        return 0
    elif n < d:
        return A[n] % Mod

    A = Modulo_Polynomial(A, d + 1)
    Q = Modulo_Polynomial([-C[i - 1] if i else 1  for i in range(d + 1)], d + 1)

    P = A * Q
    P[d] = 0
    return Polynominal_Coefficient(P, Q, n)

def Find_Linear_Recurrence(A: list[int]) -> list[int]:
    """ 整数列 A から推定される最小の長さの線形漸化式を求める.

    Args:
        A (list[int]): A の先頭

    Returns:
        list[int]: 整数列 A から推定される最小の長さの線形漸化式である. つまり, 以下を満たす.
            A[i] = C[0] * A[i - 1] + C[1] * A[i - 2] + ... + C[d - 1] * A[i - d] (i >= len(A))
    """

    N = len(A)
    B = [1]
    C = [1]
    l, m, p = 0, 0, 1
    for i in range(N):
        m += 1
        d = A[i]
        for j in range(1, l + 1):
            d += C[j] * A[i-j]
            d %= Mod

        if d == 0:
            continue

        T = C.copy()
        q = pow(p, -1, Mod) * d % Mod
        C.extend([0] * (len(B) + m - len(C)))

        for j in range(len(B)):
            C[j + m] -= q * B[j]
            C[j + m] %= Mod

        if 2 * l <= i:
            B = T
            l, m, p = i+1-l, 0, d

    return [Mod - c if c else 0 for c in C[1:]]

def Fibonacci(N):
    """ Fibonacci 列の第 N 項を求める.

    """
    return Nth_Term_of_Linearly_Recurrent_Sequence([0,1],[1,1],N)

def Lucas(N):
    """ Lucas 列の第 N 項を求める.

    """

    return Nth_Term_of_Linearly_Recurrent_Sequence([2,1],[1,1],N)

def Cumulative(A,N):
    """ d:=|A| として, 漸化式 A[i]=A[i-1]+...+A[i-d] で表される列 A の第 N 項を求める.

    """

    return Nth_Term_of_Linearly_Recurrent_Sequence(A, [1]*len(A), N)

def Factorial_Modulo(N):
    """ N! mod Mod を求める.

    """
    from collections import deque

    if N==0:
        return 1

    if N>=Mod:
        return 0

    M=0
    while (M+1)*(M+1)<=N:
        M+=1

    A=Calc.multiple_convolution(*[[i,1] for i in range(1,M+1)])
    H=Multipoint_Evaluation(Modulo_Polynomial(A,M+1),
                            [i*M for i in range(M)])

    X=1
    for h in H:
        X*=h; X%=Mod

    for i in range(M*M+1, N+1):
        X*=i; X%=Mod
    return X

#=== 特別な数列
def Bernoulli(N, mode=0):
    """ベルヌーイ数 B_0,B_1,...,B_N の (mod Mod) での値を求める.
    """

    P=Exp(Modulo_Polynomial([0,1],N+2))[1:]
    F=P.inverse().poly[:-1]

    if mode==0:
        fact=1
        for i in range(2,N+1):
            fact=(fact*i)%Mod
        return F[-1]*fact%Mod
    else:
        fact=1
        for i in range(N+1):
            F[i]=(F[i]*fact)%Mod
            fact=(fact*(i+1))%Mod
        return F

def PartitionsP(N, mode=0):
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

    if mode==0:
        return Calc.inverse(F)[-1]
    else:
        return Calc.inverse(F)

def PartitionsQ(N, mode=0):
    """ 各項が相異なる N の分割の数を求める.

    """

    Inv=[0]*(N+1)
    Inv[1]=1
    for i in range(2,N+1):
        Inv[i]=(-(Mod//i)*Inv[Mod%i])%Mod

    F=[0]*(N+1)
    for i in range(1,N+1):
        j=i
        k=1
        c=1
        while j<=N:
            F[j]=(F[j]+c*Inv[k])%Mod
            c*=-1
            j+=i
            k+=1
    P=Modulo_Polynomial(F,N+1)

    if mode==0:
        return Exp(P)[N]
    else:
        return Exp(P).poly

def Stirling_1st(N):
    """ k=0,1, ..., N に対する第 I 種 Stirling 数を求める.

    """

    def g(n):
        if n==0:
            return Modulo_Polynomial([1],N+1)
        elif n==1:
            return Modulo_Polynomial([0,1], N+1)
        elif n&1:
            return Modulo_Polynomial([-n+1, 1],N+1)*g(n-1)
        else:
            P=g(n//2)
            return P*Taylor_Shift(P, -n//2)

    return g(N).poly

def Stirling_2nd(N):
    """ k=0,1, ..., N に対する第 II 種 Stirling 数 (区別のできる N 個のものを区別できない K 個のグループ (空グループ禁止) に分割する方法) を求める.

    """

    fact=[0]*(N+1); fact[0]=1
    for i in range(1,N+1):
        fact[i]=i*fact[i-1]%Mod

    fact_inv=[0]*(N+1); fact_inv[-1]=pow(fact[-1], -1, Mod)
    for i in range(N-1,-1,-1):
        fact_inv[i]=(i+1)*fact_inv[i+1]%Mod

    A=[pow(i,N,Mod)*fact_inv[i]%Mod for i in range(N+1)]
    B=[fact_inv[i] if i&1==0 else -fact_inv[i] for i in range(N+1)]
    return Calc.convolution(A,B)[:N+1]

def Bell(N, mode = False):
    """ Bell 数 (集合 {1,2,...,N} の分割の方法) B[N] を求める.

    """
    # Bell(X) = exp(exp(X) - 1)

    fact = [1] * (N + 1)
    for k in range(1, N + 1):
        fact[k] = (k * fact[k - 1]) % Mod

    fact_inv = [1] * (N + 1)
    fact_inv[-1] = pow(fact[-1], -1, Mod)
    for k in range(N - 1, 0, -1):
        fact_inv[k] = (k + 1) * fact_inv[k + 1] % Mod

    # G = exp(X) - 1
    G = [0] + fact_inv[1:]

    # F = exp(G) = exp(exp(X) - 1)
    F = Exp(Modulo_Polynomial(G, N + 1)).poly

    for k in range(1, N + 1):
        F[k] = fact[k] * F[k] % Mod

    if mode:
        return F
    else:
        return F[N]

def Motzkin(N, mode=0):
    """ Motzkin 数 (円周上の区別がつく相異なる N 点を線分をどの2つも共通部分がない (N 点で共有も禁止) で結ぶ方法 (結ばれない点があってもよい) の数.

    """

    two_inv=pow(2, -1, Mod)
    F=((Modulo_Polynomial([1,-1], N+3)-Sqrt(Modulo_Polynomial([1,-2,-3], N+3)))*two_inv)>>2

    if mode:
        return F.poly[:N+1]
    else:
        return F[N]

#===
def Subset_Sum(X, K):
    """ X の要素のうち, 任意個を用いて, 和が k=0,1,...,K になる組み合わせの総数を Mod で割った余りを求める.

    X: リスト
    K: 非負整数
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
        if A[i]:
            j=i
            k=1
            c=1
            while j<=K:
                F[j]=(F[j]+c*Inv[k]*A[i])%Mod
                c*=-1
                j+=i
                k+=1
    P=Modulo_Polynomial(F,K+1)
    return Exp(P).poly

#===
#多項式和
def Polynominal_Sigma(P):
    """ Q(n)=P(1)+P(2)+...+P(n) を満たす多項式 Q を求める.

    """

    from itertools import accumulate

    N=len(P.poly)
    A=Multipoint_Evaluation(P, list(range(1,N+2)))
    A=list(accumulate(A,lambda x,y:(x+y)%Mod))
    return Polynominal_Interpolation(list(range(1,N+2)), A)

def Differences(P, k=1):
    """ P の k- 差分 D[k](P(n))=D[k-1](P(n+1)-P(n)), D[0](P)=P を求める. """

    N=len(P.poly)

    fact=[1]*(k+1)
    for i in range(1,k+1):
        fact[i]=i*fact[i-1]%Mod

    fact_inv=[1]*(k+1); fact_inv[-1]=pow(fact[i], -1, Mod)
    for i in range(k-1,-1,-1):
        fact_inv[i]=(i+1)*fact_inv[i+1]%Mod

    Q=[0]*(N-k)
    sgn=1 if k%2==0 else -1

    for r in range(k+1):
        alpha=sgn*fact[k]*(fact_inv[r]*fact_inv[k-r]%Mod)%Mod
        for j in range(N-k):
            Q[j]+=alpha*P[j]%Mod

        if r!=k:
            sgn*=-1
            P=Taylor_Shift(P,1)

    return Modulo_Polynomial(Q,P.max_degree)
