def Subset_Zeta_Transform(A):
    """ A の部分集合に関する Zeta 変換を求める.

    A の長さはある整数 N を用いて, 2^N でなくてはならない.
    """

    N=(len(A)-1).bit_length()
    assert 1<<N==len(A), "列の要素数は 2^N でなくてはなりません."

    for i in range(N):
        b=1<<i
        for S in range(1<<N):
            if (S & b):
                A[S]+=A[S^b]

        for S in range(1<<N):
            A[S]%=Mod

def Subset_Mobius_Transform(A):
    """ A の部分集合に関する Mobius 変換を求める.

    A の長さはある整数 N を用いて, 2^N でなくてはならない.
    """

    N=(len(A)-1).bit_length()
    assert 1<<N==len(A), "列の要素数は 2^N でなくてはなりません."

    for i in range(N):
        b=1<<i
        for S in range(1<<N):
            if (S & b):
                A[S]-=A[S^b]

        for S in range(1<<N):
            A[S]%=Mod


def Convolution_OR(A,B):
    """ OR 演算に関する畳込みを行う.

    A,B: List
    """

    N=len(A); M=len(B)
    L=1<<(max(N,M)-1).bit_length()

    if min(N,M)<64:
        C=[0]*L
        for i in range(N):
            for j in range(M):
                C[i|j]+=A[i]*B[j]
                C[i|j]%=Mod
        return C

    A=A+[0]*(L-N)
    B=B+[0]*(L-M)

    Subset_Zeta_Transform(A)
    Subset_Zeta_Transform(B)

    for i in range(N):
        A[i]*=B[i]
        A[i]%=Mod

    Subset_Mobius_Transform(A)
    return A

def Convolution_Power_OR(A,k):
    """ OR 演算に関する k 回の畳込みを行う.

    A: List
    """

    N=len(A)
    L=1<<(N-1).bit_length()

    A=A+[0]*(L-N)

    Subset_Zeta_Transform(A)

    A=[pow(A[i],k,Mod) for i in range(L)]

    Subset_Mobius_Transform(A)
    return A

Mod=998244353
