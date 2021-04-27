def Fibonacci(N,M=None):
    """フィボナッチ数列の第N項を求める.

    N:何項目?
    M:剰余
    """

    if N==0:
        return 0

    a,b=0,1
    I=1
    if M==None:
        while I<N:
            a,b=b,a+b
            I+=1
    else:
        while I<N:
            a,b=b,(a+b)%M
            I+=1
    return b

def Lucas(N,M=None):
    """フィボナッチ数列の第N項を求める.

    N:何項目?
    M:剰余
    """

    if N==0:
        return 0

    a,b=2,1
    I=1
    if M==None:
        while I<N:
            a,b=b,a+b
            I+=1
    else:
        while I<N:
            a,b=b,(a+b)%M
            I+=1
    return b

def Cumulative(N,T):
    """漸化式T_n=T_{n-1}+...+T_{n-k}で定められた数列(T_n)の第N項を求める.

    N(Int):第N項
    T(List):[T_0,...,T_{k-1}]最初のk項
    """
    K=len(T)
    if N<K:
        return T[N]

    T=list(T)
    I=K-1
    while I<N:
        U=sum(T)
        T=T[1:]+[U]
        I+=1
    return T[-1]

def Derangement_List(N,Mod=None):
    """k=0,1,...,Nに関して,k要素撹乱順列の個数を求める.
    """
    if N<0:
        return []
    elif N==0:
        return [0]
    elif N==1:
        return [0,0]
    elif Mod==1:
        return [0]*(N+1)

    R=[0]*(N+1)
    R[2]=1
    a,b,c=0,0,1

    for k in range(3,N+1):
        a,b,c=b,c,(k-1)*(b+c)

        if Mod!=None:
            c%=Mod
        R[k]=c

    return R

def Longest_Increase_Subsequence(A,Mode=False,equal=False):
    """列LにおけるLISの長さを求める.

    Mode: Trueのとき, 最長の例を1つ求める.
    equal: Falseのとき...狭義単調増加, Trueのとき...広義単調増加
    """

    if equal:
        from bisect import bisect_right as bis
    else:
        from bisect import bisect_left as bis

    L=[A[0]]
    for a in A[1:]:
        if a>L[-1] or (equal and a==L[-1]):
            L.append(a)
        else:
            L[bis(L,a)]=a
    if Mode:
        return len(L),L
    else:
        return len(L)
