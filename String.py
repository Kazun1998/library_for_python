def Run_Length_Encoding(S):
    """ランレングス圧縮

    S:文字列
    """
    if not S:
        return []

    T=[]

    b,k=S[0],1
    for s in S[1:]:
        if s==b:
            k+=1
        else:
            T.append((b,k))
            b,k=s,1

    T.append((b,k))
    return T

def Substring_Count(S,Mod=None):
    """文字列Sの異なる部分列の個数を求める.

    Mod:余り
    """

    #前処理
    N=len(S)
    A=list(set(S))
    inv_A={A[i]:i for i in range(len(A))}
    for i in range(len(A)):
        inv_A[A[i]]=i

    B=[[N]*len(A) for _ in range(N+1)]

    for i in range(N-1,-1,-1):
        for j in range(len(A)):
            B[i][j]=B[i+1][j]
        B[i][inv_A[S[i]]]=i

    #DP部
    DP=[0]*(N+1)
    if Mod==None:
        DP[0]=1
    else:
        DP[0]=1%Mod

    for i in range(N):
        for j in range(len(A)):
            if B[i][j]>=N:
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

#接尾辞配列
def Suffix_Array(S,index=0):
    X=[(i+index,S[i:]) for i in range(len(S))]
    X.sort(key=lambda x:x[-1])
    return [x[0] for x in X]

#最長共通接頭辞
def LCP_Array(S):
    pass

#Z-Algorithm
def Z_Algorithm(S):
    N=len(S)
    Z=[0]*N
    i,j=1,0
    Z[0]=N
    while i<N:
        while i+j <N and S[j] == S[i+j]:
            j+=1

        if not j:
            i+=1
            continue

        Z[i] = j
        k = 1
        while N-i>k<j-Z[k]:
            Z[i+k]=Z[k]
            k+=1
        i+=k
        j-=k
    return Z

#ハミング距離
def Hamming_Distance(S:str,T:str) -> int:
    """文字列の長さが等しいS,Tにおけるハミング距離を求める.

    S,T:string (|S|=|T| を満たしていなければならない)
    """

    assert len(S)==len(T)

    x=0
    for i in range(len(S)):
        if S[i]!=T[i]:
            x+=1
    return x

#レーベンシュタイン距離
def Levenshtein_Distance(S:str,T:str,example=False) ->int:
    """文字列S,Tにおけるレーベンシュタイン距離(編集距離) を求める.

    S,T: string
    """
    M=len(S);N=len(T)
    DP=[[0]*(N+1) for _ in range(M+1)]

    for i in range(1,M+1):
        D=DP[i]
        E=DP[i-1]
        for j in range(1,N+1):
            if S[i-1]==T[j-1]:
                D[j]=min(D[j-1]+1,E[j]+1,E[j-1])
            else:
                D[j]=min(D[j-1],E[j],E[j-1])+1

    return D[-1]
                
#最長部分列
def Longest_Common_Subsequence(S:str, T:str, example=False):
    """文字列 S,T における最長部分列の長さを求める.

    S,T: string
    example: Trueであるとき,LCSを満たす例を1つ返す.
    """

    M=len(S);N=len(T)
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

    X=""
    I,J=M,N
    D=DP[I];E=DP[I-1]
    while D[J]:
        if S[I-1]==T[J-1]:
            X+=S[I-1]
            I-=1
            J-=1
            D=DP[I]
            E=DP[I-1]
        else:
            if D[J]==D[J-1]:
                J-=1
            else:
                I-=1
                D=DP[I]
                E=DP[I-1]

    return DP[-1][-1],X[::-1]
