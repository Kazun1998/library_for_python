def Divisor_Zeta_Transform(A):
    """ A の約数を走る Zeta 変換を行う.

    ※ A[0] の値は無視される.
    """

    N=len(A)-1
    S=[1]*(N+1)

    for p in range(2,N+1):
        if S[p]:
            for k in range(1,N//p+1):
                S[k*p]=0
                A[k*p]+=A[k]

    for i in range(1,N+1):
        A[i]%=Mod

def Divisor_Mobius_Transform(A):
    """ A の約数を走るにおける Mobius 変換を行う.

    ※ A[0] の値は無視される.
    """

    N=len(A)-1
    S=[1]*(N+1)

    for p in range(2,N+1):
        if S[p]:
            for k in range(N//p,0,-1):
                S[k*p]=0
                A[k*p]-=A[k]

    for i in range(1,N+1):
        A[i]%=Mod

def Convolution_LCM(A,B,L=None):
    """ A,B の lcm における畳み込みを行う.

    L: 結果の長さの最大値 (一般的に, lcm(n,m)<=nm なため)
    ※ A[0], B[0] の値は無視される.
    """

    N=len(A)-1; M=len(B)-1; K=max(N,M)
    if L==None:
        L=K*(K-1)

    A=A+[0]*(L-N)
    B=B+[0]*(L-M)

    Divisor_Zeta_Transform(A)
    Divisor_Zeta_Transform(B)

    for i in range(1,L+1):
        A[i]*=B[i]
        A[i]%=Mod

    Divisor_Mobius_Transform(A)
    return A

def Convolution_Power_LCM(A,k,L):
    """ A の lcm における k 回の畳み込みを行う.
    ただし, 最大でも L までに制限する.

    ※ A[0] の値は無視される.
    """

    A=A+[0]*(L+1-len(A))
    Divisor_Zeta_Transform(A)
    A=[pow(a,k,Mod) for a in A]
    Divisor_Mobius_Transform(A)
    return A

Mod=998244353
