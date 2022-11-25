#最長部分列
def Longest_Common_Subsequence(S, T, example=False):
    """ 列 S,T における最長部分列の長さを求める.

    example: True であるとき, LCS を満たす例を1つ返す.
    """

    M=len(S); N=len(T)
    DP=[[0]*(N+1) for _ in range(M+1)]

    for i in range(1,M+1):
        D=DP[i]
        E=DP[i-1]
        for j in range(1,N+1):
            if S[i-1]==T[j-1]:
                D[j]=E[j-1]+1
            else:
                if E[j]>=D[j-1]:
                    D[j]=E[j]
                else:
                    D[j]=D[j-1]

    if not example:
        return D[-1]

    X=[]
    I,J=M,N
    D=DP[I]; E=DP[I-1]
    while D[J]:
        if S[I-1]==T[J-1]:
            X.append(S[I-1])
            I-=1; J-=1
            D=DP[I]
            E=DP[I-1]
        else:
            if D[J]==D[J-1]:
                J-=1
            else:
                I-=1
                D=DP[I]
                E=DP[I-1]

    return DP[-1][-1], X[::-1]
