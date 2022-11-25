def Montmort_Number(N, Mod=None):
    """ k=0,1,...,N に関して, k 要素撹乱順列の個数を求める.
    """
    if N<0:
        return []
    elif N==0:
        return [0]

    X=[0]*(N+1)
    if Mod==None:
        for k in range(2, N+1):
            X[k]=k*X[k-1]+(-1 if k%2 else 1)
    else:
        for k in range(2, N+1):
            X[k]=(k*X[k-1]+(-1 if k%2 else 1))%Mod

    return X

