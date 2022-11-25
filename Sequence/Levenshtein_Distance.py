#レーベンシュタイン距離
def Levenshtein_Distance(S, T):
    """ S,T におけるレーベンシュタイン距離 (編集距離) を求める.

    """

    M=len(S); N=len(T)
    DP=[[0]*(N+1) for _ in range(M+1)]

    for i in range(1,M+1):
        D=DP[i]
        E=DP[i-1]
        for j in range(1,N+1):
            if S[i-1]==T[j-1]:
                D[j]=min(D[j-1]+1, E[j]+1, E[j-1])
            else:
                D[j]=min(D[j-1], E[j], E[j-1])+1

    return D[-1]
