#商列挙
def Quotient_Range(N):
    """Nで割った商の可能性を全て列挙する.

    [Input]
    N:正整数

    [Output]
    X:リスト
    Xの各要素(k,x,y) は x<=i<=y であることと, floor(N/i)=k が同値であることを表す.
    """
    X=[]

    M=1
    while M*M<=N:
        X.append((N//M,M,M))
        M+=1

    for i in range(M,0,-1):
        L=N//(i+1)+1
        R=N//i

        if L<=R and X[-1][-1]<L:
            X.append((N//L,L,R))
    return X

def Reminder_Enumeration(N,r):
    """ N を q 割った余りが r になる q を全て列挙する.

    N: 正整数
    r: 非負整数, N!=r
    """

    assert N!=r,"無限個あります."

    k=1
    X=[];Y=[]
    N-=r
    while k*k<=N:
        if N%k==0:
            if k>r:
                X.append(k)
            if k*k!=N and N//k>r:
                Y.append(N//k)
        k+=1
    return X+Y[::-1]

def Next_Remainder(x, p, r):
    """ x 以上で p で割って r 余る整数のうち, 最小の整数を求める.

    """

    if x%p<=r:
        return (x//p)*p+r
    else:
        return (x//p+1)*p+r

def Previous_Remainder(x, p, r):
    """ x 以下で p で割って r 余る整数のうち, 最大の整数を求める.

    """

    if r<=x%p:
        return (x//p)*p+r
    else:
        return (x//p-1)*p+r
