def Less_Zeta_Transform(A):
    """ A の以下を走る Zeta 変換を行う.

    """
    for i in range(1,len(A)):
        A[i]=(A[i-1]+A[i])%Mod

def Less_Mobius_Transform(A):
    """ A の以下を走るにおける Mobius 変換を行う.

    """

    for i in range(len(A)-1,0,-1):
        A[i]=(A[i]-A[i-1])%Mod

def Convolution_MAX(A,B):
    """ A,B の max における畳み込みを行う.
    """

    N=len(A); M=len(B)
    L=max(N,M)

    A=A+[0]*(L-N)
    B=B+[0]*(L-M)

    Less_Zeta_Transform(A)
    Less_Zeta_Transform(B)

    for i in range(L):
        A[i]*=B[i]
        A[i]%=Mod

    Less_Mobius_Transform(A)
    return A

def Convolution_Power_MAX(A,k):
    """ A の max における k 回の畳み込みを行う.

    """

    Less_Zeta_Transform(A)
    A=[pow(a,k,Mod) for a in A]
    Less_Mobius_Transform(A)
    return A

Mod=998244353
