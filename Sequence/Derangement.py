def Derangement_List(N,Mod=None):
    """ k=0,1,...,N に関して, k 要素撹乱順列の個数を求める.
    """
    if N<0:
        return []
    elif N==0:
        return [0]
    elif N==1:
        return [0,0]
    elif Mod==1:
        return [0]*(N+1)

    X=[0]*(N+1)
    if Mod==None:
        X[2]=1
        for k in range(3,N+1):
            X[k]=(k-1)*(X[k-1]+X[k-2])
    else:
        X[2]=1%Mod
        for k in range(3,N+1):
            X[k]=(k-1)*(X[k-1]+X[k-2])%Mod

    return X

