def Superset_Zeta_Transform(A):
    """ A の上位集合を走る Zeta 変換を求める.

    A の長さはある整数 N を用いて, 2^N でなくてはならない.
    """
    N=(len(A)-1).bit_length()
    assert 1<<N==len(A), "列の要素数は 2^N でなくてはなりません."

    for i in range(N):
        bit=1<<i
        for S in range(1<<N):
            if not(S & bit):
                A[S]+=A[S|bit]
                A[S]%=Mod

def Superset_Mobius_Transform(A):
    """ A の上位集合を走る Mobius 変換を求める.

    A の長さはある整数 N を用いて, 2^N でなくてはならない.
    """

    N=(len(A)-1).bit_length()
    assert 1<<N==len(A), "列の要素数は 2^N でなくてはなりません."

    for i in range(N):
        bit=1<<i
        for S in range(1<<N):
            if not (S & bit):
                A[S]-=A[S|bit]
                A[S]%=Mod

def Convolution_AND(A,B):
    """ AND 演算に関する畳込みを行う.

    A,B: List
    """

    N=len(A); M=len(B)
    L=1<<(max(N,M)-1).bit_length()

    if min(N,M)<64:
        C=[0]*L
        for i in range(N):
            for j in range(M):
                C[i&j]+=A[i]*B[j]
                C[i&j]%=Mod
        return C

    A=A+[0]*(L-N)
    B=B+[0]*(L-M)

    Superset_Zeta_Transform(A)
    Superset_Zeta_Transform(B)

    for i in range(N):
        A[i]*=B[i]
        A[i]%=Mod

    Superset_Mobius_Transform(A)
    return A

def Convolution_Power_AND(A,k):
    """ AND 演算に関する k 回の畳込みを行う.

    A: List
    """

    N=len(A)
    L=1<<(N-1).bit_length()

    A=A+[0]*(L-N)

    Superset_Zeta_Transform(A)

    A=[pow(A[i],k,Mod) for i in range(L)]

    Superset_Mobius_Transform(A)
    return A

Mod=998244353