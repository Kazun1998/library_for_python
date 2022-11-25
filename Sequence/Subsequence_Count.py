def Substring_Count(S, Mod=None):
    """ 列 S の異なる部分列の個数を求める.

    Mod: 余り
    """

    #前処理
    N=len(S)
    A=list(set(S))
    inv_A={A[i]:i for i in range(len(A))}

    B=[[N]*len(A) for _ in range(N+1)]

    for i in range(N-1,-1,-1):
        Bi=B[i]; Bii=B[i+1]
        for j in range(len(A)):
            Bi[j]=Bii[j]
        Bi[inv_A[S[i]]]=i

    #DP部
    DP=[0]*(N+1)
    if Mod==None:
        DP[0]=1
    else:
        DP[0]=1%Mod

    for i in range(N):
        Bi=B[i]
        for j in range(len(A)):
            if Bi[j]>=N:
                continue

            DP[B[i][j]+1]+=DP[i]
            if Mod!=None:
                DP[B[i][j]+1]%=Mod
    #集計
    for i in range(N+1):
        if Mod==None:
            return sum(DP)
        else:
            T=0
            for a in DP:
                T+=a
                T%=Mod
            return T
