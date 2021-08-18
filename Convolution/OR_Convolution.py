def Fast_Walsh_Hadamard_Transform_OR(A):
    """ OR に関する Walsh_Hadamard_Transform を行う.

    A: List
    """

    N=len(A)
    K=(N-1).bit_length()
    for i in range(K):
        d=1<<i
        for j in range(d):
            for k in range(0,N,2*d):
                A[j+k+d]+=A[j+k]

        for j in range(N):
            A[j]%=Mod

def Fast_Inverse_Walsh_Hadamard_Transform_OR(A):
    """ OR に関する逆 Walsh_Hadamard_Transform を行う.

    A: List
    """

    N=len(A)
    K=(N-1).bit_length()
    for i in range(K):
        d=1<<i
        for j in range(d):
            for k in range(0,N,2*d):
                A[j+k+d]-=A[j+k]

        for j in range(N):
            A[j]%=Mod

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

    Fast_Walsh_Hadamard_Transform_OR(A)
    Fast_Walsh_Hadamard_Transform_OR(B)

    for i in range(N):
        A[i]*=B[i]
        A[i]%=Mod

    Fast_Inverse_Walsh_Hadamard_Transform_OR(A)
    return A

def Convolution_Power_OR(A,k):
    """ OR 演算に関する k 回の畳込みを行う.

    A: List
    """

    N=len(A)
    L=1<<(N-1).bit_length()

    A=A+[0]*(L-N)

    Fast_Walsh_Hadamard_Transform_OR(A)

    A=[pow(A[i],k,Mod) for i in range(L)]

    Fast_Inverse_Walsh_Hadamard_Transform_OR(A)
    return A
