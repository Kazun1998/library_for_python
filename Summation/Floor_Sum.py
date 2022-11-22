def floor_sum(A, B, M, N):
    """sum_{i=0}^{N-1} floor((A*i+B)/M) を求める.
    """
    T=0
    while True:
        T+=((N-1)*N//2)*(A//M)
        A%=M

        T+=N*(B//M)
        B%=M

        y=(A*N+B)//M
        x=B-y*M

        if y==0:
            return T

        T+=(N+x//A)*y
        A,B,M,N=M,x%A,A,y

def Floor_Sum(A: int, B: int, M: int, N: int, K=0):
    """sum_{i=K}^N floor((A*i+B)/M) を求める.
    """

    if K==0:
        return floor_sum(A,B,M,N+1)
    else:
        return floor_sum(A,B,M,N+1)-floor_sum(A,B,M,K)
