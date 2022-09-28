def Run_Length_Encoding(S):
    """ Run Length 圧縮

    S: 列
    """
    if not S:
        return []

    R=[[S[0],1]]

    for i in range(1,len(S)):
        if R[-1][0]==S[i]:
            R[-1][1]+=1
        else:
            R.append([S[i],1])

    return R

def Substring_Count(S, Mod=None):
    """文字列 S の異なる部分列の個数を求める.

    Mod: 余り
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

def Suffix_Array(S, encoder=lambda x:x):
    """ S の Suffix Array (接尾辞配列) (S[0...], S[1...],... を辞書式に並べた時の開始インデックスの列) を SA-IS によって求める.

    S: 列
    encoder: 正の整数への順序埋め込み (※ max encoder(S) が小さいほど計算量がよい)
    """

    A=[encoder(x) for x in S]+[0]
    assert min(A[:-1])>0,"encoder の値域が正から外れています"
    k=max(A)+1
    n=len(A)

    def induce_l(sa, a, n, k, stype):
        bucket = get_buckets(a, k, 1)
        for i in range(n):
            j = sa[i] - 1
            if j >= 0 and (not stype[j]):
                sa[bucket[a[j]]] = j
                bucket[a[j]] += 1

    def induce_s(sa, a, n, k, stype):
        bucket = get_buckets(a, k, 0)
        for i in range(n)[::-1]:
            j = sa[i] - 1
            if j >= 0 and stype[j]:
                bucket[a[j]] -= 1
                sa[bucket[a[j]]] = j

    def get_buckets(a, k, start = 0):
        bucket = [0] * k
        for item in a:
            bucket[item] += 1
        s = 0
        for i in range(k):
            s += bucket[i]
            bucket[i] = s - (bucket[i] if start else 0)
        return bucket

    def set_lms(a, n, k, default_order):
        bucket = get_buckets(a, k)
        sa = [-1] * n
        for i in default_order[::-1]:
            bucket[a[i]] -= 1
            sa[bucket[a[i]]] = i
        return sa

    def induce(a, n, k, stype, default_order):
        sa = set_lms(a, n, k, default_order)
        induce_l(sa, a, n, k, stype)
        induce_s(sa, a, n, k, stype)
        return sa

    def rename_LMS_substring(sa, a, n, stype, LMS, l):
        sa = [_s for _s in sa if LMS[_s]]
        tmp = [-1] * (n//2) + [0]
        dupl = 0
        for _ in range(1, l):
            i, j = sa[_-1], sa[_]
            for ii in range(n):
                if a[i+ii] != a[j+ii] or stype[i+ii] != stype[j+ii]:
                    break
                if ii and (LMS[i+ii] or LMS[j+ii]):
                    dupl += 1
                    break
            tmp[j//2] = _ - dupl
        tmp = [t for t in tmp if t >= 0]
        return tmp, dupl

    def calc(a, n, k):
        stype = [1] * n
        for i in range(n-1)[::-1]:
            if a[i] > a[i+1] or (a[i] == a[i+1] and stype[i+1] == 0):
                stype[i] = 0

        LMS = [1 if stype[i] and not stype[i-1] else 0 for i in range(n-1)] + [1]
        l = sum(LMS)
        lms = [i for i in range(n) if LMS[i]]
        sa = induce(a, n, k, stype, lms)
        renamed_LMS, dupl = rename_LMS_substring(sa, a, n, stype, LMS, l)

        if dupl:
            sub_sa = calc(renamed_LMS, l, l - dupl)
        else:
            sub_sa = [0] * l
            for i in range(l):
                sub_sa[renamed_LMS[i]] = i

        lms = [lms[sub_sa[i]] for i in range(l)]
        sa = induce(a, n, k, stype, lms)
        return sa

    return calc(A,n,k)[1:]

def Longest_Commom_Prefix(S, encoder=lambda x:x,with_SA=False):
    SA=Suffix_Array(S,encoder)
    N=len(S)
    rank=[0]*N

    for i in range(N):
        rank[SA[i]] = i

    LCP=[0]*(N - 1)
    h=0
    for i in range(N):
        if h: h -= 1
        if rank[i] == 0: continue
        j = SA[rank[i] - 1]
        while j + h < N and i + h < N:
            if S[j+h] != S[i+h]: break
            h += 1
        LCP[rank[i] - 1] = h

    if with_SA:
        return SA,LCP
    else:
        return LCP

#Z-Algorithm
def Z_Algorithm(S):
    """ i=0,1,...,|S|-1 に対して, S[i...] と S の先頭何文字が一致しているかを表すリストを返す.

    S: string
    """
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
def Hamming_Distance(S: str, T: str):
    """文字列の長さが等しい S, T におけるハミング距離を求める.

    S,T:string (|S|=|T| を満たしていなければならない)
    """

    assert len(S)==len(T)

    x=0
    for i in range(len(S)):
        if S[i]!=T[i]:
            x+=1
    return x

#レーベンシュタイン距離
def Levenshtein_Distance(S: str, T: str):
    """文字列 S,T におけるレーベンシュタイン距離 (編集距離) を求める.

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
    example: True であるとき, LCS を満たす例を1つ返す.
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

    X=[]
    I,J=M,N
    D=DP[I];E=DP[I-1]
    while D[J]:
        if S[I-1]==T[J-1]:
            X.append(S[I-1])
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

    return DP[-1][-1]," ".join(X[::-1])
