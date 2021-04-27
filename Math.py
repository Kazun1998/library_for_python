def floor_sum(A,B,M,N):
    """sum_{i=0}^{N-1} floor((A*i+B)/M) を求める.
    """
    T=0
    while True:
        if A>=M:
            T+=(N-1)*N*(A//M)//2
            A%=M

        if B>=M:
            T+=N*(B//M)
            B%=M

        y=(A*N+B)//M
        x=B-y*M

        if y==0:
            return T

        T+=(N+x//A)*y
        A,B,M,N=M,(A-x%A)%A,A,y

def Floor_Sum(A:int,B:int,M:int,N:int,K=0):
    """sum_{i=K}^N floor((A*i+B)/M) を求める.
    """

    if K==0:
        return floor_sum(A,B,M,N+1)
    else:
        return floor_sum(A,B,M,N+1)-floor_sum(A,B,M,K)

def Linear_Sum(a,b,L,R):
    """ Sum_{i=L}^R (ai+b) を求める.
    """

    if L<=R:
        return (a*(L+R)+2*b)*(R-L+1)//2
    else:
        return 0

def Box_Sum_Count(P,Q,R,S,K):
    """P<=X<=Q, R<=Y<=S, X+Y=K を満たす整数の組 (X,Y) の個数を出力する.

    P,Q,R,S:int (P<=Q, R<=S)
    """

    if not (P<=Q and R<=S):
        return 0

    Q-=P
    S-=R
    K-=P+R

    if S>Q:
        Q,S=S,Q

    if K<0:
        return 0
    elif 0<=K<Q:
        return K+1
    elif Q<=K<S:
        return Q+1
    elif S<=K<=Q+S:
        return Q+S+1-K
    else:
        return 0

def Interval_Sum_Count(L,R,X):
    """L<=x,y<=R を満たす2つの整数x,yのうち, x+y=X を満たす組(x,y) の個数を出力する.

    L,R:Int (L<=R)
    X:Int
    """

    if L>R:
        return 0

    if 2*L<=X<=L+R:
        return X-2*L+1
    elif L+R<=X<=2*R:
        return 2*R+1-X
    else:
        return 0

def Interval_Sum_Count_Sum(L,R,A,B):
    """L<=x,y<=R を満たす2つの整数x,yのうち, A<=x+y<=B を満たす組(x,y) の個数を出力する.

    L,R:Int (L<=R)
    A,B:Int (A<=B)
    """

    if L>R or A>B:
        return 0

    A=max(A,2*L)
    B=min(B,2*R)
    if B<2*L or 2*R<A:
        return 0

    if A<=L+R<B:
        return Linear_Sum(1,-2*L+1,A,L+R)+Linear_Sum(-1,2*R+1,L+R+1,B)
    else:
        if B<=L+R:
            return Linear_Sum(1,-2*L+1,A,B)
        else:
            return Linear_Sum(-1,2*R+1,A,B)

def Bound_Sum(a,b,D,U,L,R):
    """ p[k]:=max(D,min(ak+b,U)) としたとき, Sum_{k=L}^R p[k] を求める.

    a,b :int
    D,U (D<=U) : int :抑え込む範囲
    L,R (L<=R) : int :和を取る範囲
    """

    assert D<=U and L<=R

    if a==0:
        return max(D,min(b,U))*(R-L+1)

    if a>0:
        alpha=(D-b+a-1)//a
        beta =(U-b)//a

        if R<alpha:
            return D*(R-L+1)
        elif beta<L:
            return U*(R-L+1)

        X=0
        if L<alpha:
            X+=D*(alpha-L)
            L=alpha
        if beta<R:
            X+=U*(R-beta)
            R=beta
    else:
        a_abs=-a
        alpha=(b-U+a_abs-1)//a_abs
        beta =(b-D)//a_abs

        if R<alpha:
            return U*(R-L+1)
        elif beta<L:
            return D*(R-L+1)

        X=0
        if L<alpha:
            X+=U*(alpha-L)
            L=alpha
        if beta<R:
            X+=D*(R-beta)
            R=beta
    X+=Linear_Sum(a,b,L,R)
    return X

def Linear_Max_Sum(a,b,c,d,L,R):
    """ sum_{k=L}^R max(ak+b,ck+d) を求める.

    a,b,c,d:int
    L,R:int (L<=R)
    """

    if L>R:
        return 0

    if a==c:
        return Linear_Sum(a,max(b,d),L,R)
    if c>a:
        a,b,c,d=c,d,a,b

    if a*L+b>c*L+d:
        return Linear_Sum(a,b,L,R)

    if a*R+b<c*R+d:
        return Linear_Sum(c,d,L,R)

    m=(d-b)//(a-c)
    return Linear_Sum(c,d,L,m)+Linear_Sum(a,b,m+1,R)

def Linear_Min_Sum(a,b,c,d,L,R):
    """ sum_{k=L}^R min(ak+b,ck+d) を求める.

    a,b,c,d:int
    L,R:int (L<=R)
    """
    return -Linear_Max_Sum(-a,-b,-c,-d,L,R)
