def Multiple_Zeta_Transform(A):
    """ A の倍数を走るにおける Zeta 変換を行う.

    ※ A[0] の値は無視される.
    """

    N=len(A)-1
    S=[1]*(N+1)

    for p in range(2,N+1):
        if S[p]:
            for k in range(N//p,0,-1):
                S[k*p]=0
                A[k]+=A[k*p]

    for i in range(1,N+1):
        A[i]%=Mod

def Multiple_Mobius_Transform(A):
    """ A の約数における Mobius 変換を行う.

    ※ A[0] の値は無視される.
    """

    N=len(A)-1
    S=[1]*(N+1)

    for p in range(2,N+1):
        if S[p]:
            for k in range(1,N//p+1):
                S[k*p]=0
                A[k]-=A[k*p]

    for i in range(1,N+1):
        A[i]%=Mod

def Convolution_GCD(A,B):
    """ A,B の gcd における畳み込みを行う.

    ※ A[0], B[0] の値は無視される.
    """

    N=len(A)-1; M=len(B)-1; L=max(N,M)

    A=A+[0]*(L-N)
    B=B+[0]*(L-M)

    Multiple_Zeta_Transform(A)
    Multiple_Zeta_Transform(B)

    for i in range(1,L+1):
        A[i]*=B[i]
        A[i]%=Mod

    Multiple_Mobius_Transform(A)
    return A

def Convolution_Power_GCD(A,k):
    """ A の gcd における k 回の畳み込みを行う.

    ※ A[0] の値は無視される.
    """

    A=A[:]
    Multiple_Zeta_Transform(A)
    A=[pow(a,k,Mod) for a in A]
    Multiple_Mobius_Transform(A)
    return A

Mod=998244353
