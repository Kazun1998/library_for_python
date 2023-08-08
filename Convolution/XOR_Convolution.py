def Fast_Walsh_Hadamard_Transform_XOR(A):
    """ XOR に関する Walsh_Hadamard_Transform を行う.

    A: List
    """

    N=len(A)
    h=(N-1).bit_length()
    for k in range(h):
        bit=1<<k
        for i in range(N):
            if i&bit==0:
                x=A[i]
                y=A[i|bit]
                A[i]=(x+y)%Mod
                A[i|bit]=(x-y)%Mod

def Fast_Inverse_Walsh_Hadamard_Transform_XOR(A):
    """ XOR に関する逆 Walsh_Hadamard_Transform を行う.

    A: List
    """

    Fast_Walsh_Hadamard_Transform_XOR(A)
    N_inv=pow(len(A), -1, Mod)
    for i in range(len(A)):
        A[i] = (A[i] * N_inv) % Mod

def Convolution_XOR(A,B):
    """ XOR 演算に関する畳込みを行う.

    A,B: List
    """

    N=len(A); M=len(B)
    L=1<<(max(N,M)-1).bit_length()

    if min(N,M)<64:
        C=[0]*L
        for i in range(N):
            for j in range(M):
                C[i^j]+=A[i]*B[j]
                C[i^j]%=Mod
        return C

    A=A+[0]*(L-N)
    B=B+[0]*(L-M)

    Fast_Walsh_Hadamard_Transform_XOR(A)
    Fast_Walsh_Hadamard_Transform_XOR(B)

    for i in range(N):
        A[i]*=B[i]
        A[i]%=Mod

    Fast_Inverse_Walsh_Hadamard_Transform_XOR(A)
    return A

def Convolution_Power_XOR(A,k):
    """ XOR 演算に関する k 回の畳込みを行う.

    A,B: List
    """

    N=len(A)
    L=1<<(N-1).bit_length()

    A=A+[0]*(L-N)

    Fast_Walsh_Hadamard_Transform_XOR(A)

    A=[pow(A[i],k,Mod) for i in range(L)]

    Fast_Inverse_Walsh_Hadamard_Transform_XOR(A)
    return A

Mod=998244353