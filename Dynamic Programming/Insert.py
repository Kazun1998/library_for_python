def Increase_Decrease_Permutation(N,T,Mod):
    """ 長さが N の順列のうち, 以下を満たすような順列 P の総数を Mod で割った余りを出力する:
    T[i]=1 -> P[i]<P[i+1], T[i]=-1 -> P[i]>P[i+1], T[i]=0 -> (特になし)

    N: int
    T: list (|T|=N-1)
    Mod: int
    """

    assert len(T)==N-1
    from itertools import accumulate

    DP=[1]*N

    for i in range(1,N):
        if Mod!=None:
            Cum=list(accumulate(DP,lambda x,y:(x+y)%Mod))
        else:
            Cum=list(accumulate(DP))

        if T[i-1]==1:
            for m in range(N-i):
                DP[m]=Cum[m]
        elif T[i-1]==0:
            for m in range(N-i):
                DP[m]=Cum[N-i]
        else:
            for m in range(N-i-1,-1,-1):
                DP[m]=Cum[N-i]-Cum[m]
        for m in range(N-i,N):
            DP[m]=0

    return DP[0]%Mod
