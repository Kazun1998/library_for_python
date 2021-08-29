def More_Zeta_Transform(A):
    """ A の以上を走る Zeta 変換を行う.

    """
    for i in range(len(A)-2,-1,-1):
        A[i]=(A[i]+A[i+1])%Mod

def More_Mobius_Transform(A):
    """ A の以下を走るにおける Mobius 変換を行う.

    """

    for i in range(len(A)-1):
        A[i]=(A[i]-A[i+1])%Mod

def Convolution_MIN(A,B):
    """ A,B の min における畳み込みを行う.
    """

    N=len(A); M=len(B)
    L=max(N,M)

    A=A+[0]*(L-N)
    B=B+[0]*(L-M)

    More_Zeta_Transform(A)
    More_Zeta_Transform(B)

    for i in range(L):
        A[i]*=B[i]
        A[i]%=Mod

    More_Mobius_Transform(A)
    return A

def Convolution_Power_MIN(A,k):
    """ A の min における k 回の畳み込みを行う.

    """
    A=A[:]
    More_Zeta_Transform(A)
    A=[pow(a,k,Mod) for a in A]
    More_Mobius_Transform(A)
    return A

Mod=998244353
