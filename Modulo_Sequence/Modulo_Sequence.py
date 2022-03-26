from Modulo_Polynominal import *

#===漸化式
def Nth_Term_of_Linearly_Recurrent_Sequence(A,C,N,offset=0):
    """ A[i]=C[0]*A[i-1]+C[1]*A[i-2]+...+C[d-1]*A[i-d] で表される数列 (A[i]) の第 N 項を求める.

    A=(A[0], ..., A[d-1]): 最初の d 項
    C=(C[0], ..., C[d-1]): 線形漸化式
    N: 求める項数
    offset: ずらす項数
    """

    assert len(A)==len(C)
    d=len(A)

    if N<d:
        return A[N]%Mod

    A=Modulo_Polynominal(A,d+1)
    Q=Modulo_Polynominal([-C[i-1] if i else 1  for i in range(d+1)], d+1)

    P=A*Q; P[d]=0
    return Polynominal_Coefficient(P,Q,N-offset)

def Find_Linear_Recurrence(A):
    """ A から推定される最小の長さの関係式を求める.

    Reference: https://judge.yosupo.jp/submission/28692
    """

    N=len(A)
    B=[1]; C=[1]
    l=0; m=0; p=1
    for i in range(N):
        m+=1
        d=A[i]
        for j in range(1,l+1):
            d+=C[j]*A[i-j]
            d%=Mod
        if d==0:
            continue

        T=C.copy()
        q=pow(p,Mod-2,Mod)*d%Mod
        C=C+[0]*(len(B)+m-len(C))

        for j in range(len(B)):
            C[j+m]-=q*B[j]
            C[j+m]%=Mod
        if 2*l<=i:
            B=T
            l,m,p=i+1-l,0,d

    return [Mod-c if c else 0 for c in C[1:]]

def Fibonacci(N):
    """ Fibonacci 列の第 N 項を求める.

    """
    return Nth_Term_of_Linearly_Recurrent_Sequence([0,1],[1,1],N)

def Lucas(N):
    """ Lucas 列の第 N 項を求める.

    """

    return Nth_Term_of_Linearly_Recurrent_Sequence([2,1],[1,1],N)

def Cumulative(A,N):
    """ d:=|A| として, 漸化式 A[i]=A[i-1]+...+A[i-d] で表される列 T の第 N 項を求める.

    """

    return Nth_Term_of_Linearly_Recurrent_Sequence(A, [1]*len(A), N)

def Factorial_Modulo(N):
    """ N! mod Mod を求める.

    """
    from collections import deque

    if N==0:
        return 1

    M=0
    while (M+1)*(M+1)<=N:
        M+=1

    Q=deque([[i,1] for i in range(1,M+1)])
    while len(Q)>1:
        A=Q.popleft()
        B=Q.popleft()
        Q.append(Calc.Convolution(A,B))

    H=Multipoint_Evaluation(Modulo_Polynominal(Q[0],M+1),
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

    P=Exp(Modulo_Polynominal([0,1],N+2))[1:]
    F=P.inverse().Poly[:-1]

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
        return Calc.Inverse(F)[-1]
    else:
        return Calc.Inverse(F)

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
    P=Modulo_Polynominal(F,N+1)

    if mode==0:
        return Exp(P).Poly[N]
    else:
        return Exp(P)

def Stirling_1st(N):
    """ k=0,1, ..., N に対する第 I 種 Stirling 数を求める.

    """

    def g(n):
        if n==0:
            return Modulo_Polynominal([1],N+1)
        elif n==1:
            return Modulo_Polynominal([0,1], N+1)
        elif n&1:
            return Modulo_Polynominal([-n+1, 1],N+1)*g(n-1)
        else:
            P=g(n//2)
            return P*Taylor_Shift(P, -n//2)

    return g(N).Poly

def Stirling_2nd(N):
    """ k=0,1, ..., N に対する第 II 種 Stirling 数を求める.

    """

    fact=[0]*(N+1); fact[0]=1
    for i in range(1,N+1):
        fact[i]=i*fact[i-1]%Mod

    fact_inv=[0]*(N+1); fact_inv[-1]=pow(fact[-1],Mod-2,Mod)
    for i in range(N-1,-1,-1):
        fact_inv[i]=(i+1)*fact_inv[i+1]%Mod

    A=[pow(i,N,Mod)*fact_inv[i]%Mod for i in range(N+1)]
    B=[fact_inv[i] if i&1==0 else -fact_inv[i] for i in range(N+1)]
    return Calc.Convolution(A,B)[:N+1]

#===
def Subset_Sum(X,K):
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

#===
#多項式和
def Polynominal_Sigma(P):
    """ Q(n)=P(1)+P(2)+...+P(n) を満たす多項式 Q を求める.

    """

    from itertools import accumulate

    N=len(P.Poly)
    A=Multipoint_Evaluation(P, list(range(1,N+2)))
    A=list(accumulate(A,lambda x,y:(x+y)%Mod))
    return Polynominal_Interpolation(list(range(1,N+2)), A)

def Differences(P, k=1):
    """ P の k- 差分 D[k](P(n))=D[k-1](P(n+1)-P(n)), D[0](P)=P を求める. """

    N=len(P.Poly)

    fact=[1]*(k+1)
    for i in range(1,k+1):
        fact[i]=i*fact[i-1]%Mod

    fact_inv=[1]*(k+1); fact_inv[-1]=pow(fact[i],Mod-2,Mod)
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

    return Modulo_Polynominal(Q,P.max_degree)
