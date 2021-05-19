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
        A,B,M,N=M,x%A,A,y

def Floor_Sum(A:int,B:int,M:int,N:int,K=0):
    """sum_{i=K}^N floor((A*i+B)/M) を求める.
    """

    if K==0:
        return floor_sum(A,B,M,N+1)
    else:
        return floor_sum(A,B,M,N+1)-floor_sum(A,B,M,K)

#==================================================
#Sum系
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
    A=max(0,K-(P  +R  )+1)
    B=max(0,K-(Q+1+R  )+1)
    C=max(0,K-(P  +S+1)+1)
    D=max(0,K-(Q+1+S+1)+1)
    return A-B-C+D

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

#==================================================
#Sum_Count系
def Range_Sum_DP(Range,S,Mod=None,Mode=0):
    """Range=[(A_0,B_0),...,(A_{N-1}, B_{N-1})] としとたき,
    A_i<=X_i<=B_i, X_0+...+X_{n-1}=S を満たす組の個数を動的計画法で求める.

    0<=A_i<=B_i
    0<=S
    計算量: O(NS)
    """

    D=[0]*(S+1); D[0]=1
    E=[1]*(S+1)

    for a,b in Range:
        assert 0<=a<=b

        for i in range(S+1):
            if i<a:
                D[i]=0
            elif i<=b:
                D[i]=E[i-a]
            else:
                D[i]=E[i-a]-E[i-b-1]

        E[0]=D[0]
        for i in range(1,S+1):
            E[i]=D[i]+E[i-1]

        if Mod!=None:
            E[i]%=Mod

    if Mode:
        return D
    else:
        return D[S]

def Range_Sum_Inclusion(Range,S,Mod=None):
    """Range=[(A_0,B_0),...,(A_{N-1}, B_{N-1})] としとたき,
    A_i<=X_i<=B_i, X_0+...+X_{n-1}=S を満たす組の個数を包除原理で求める.

    0<=A_i<=B_i
    0<=S
    計算量: O(N2^N)
    """
    from itertools import product

    def nCr(n,r):
        if n<0: return 0
        if r<0 or n<r: return 0

        a=b=1
        r=min(r,n-r)

        while r:
            a*=n; b*=r

            if Mod!=None:
                a%=Mod; b%=Mod

            n-=1; r-=1

        if Mod!=None:
            return (a*pow(b,Mod-2,Mod))%Mod
        else:
            return a//b

    def nHr(n,r):
        return nCr(n+r-1,n-1)

    N=len(Range)
    X=0
    for p in product((0,1),repeat=N):
        T=S
        for i in range(N):
            a,b=Range[i]
            if p[i]:
                T-=b+1
            else:
                T-=a

        X+=pow(-1,sum(p))*nHr(N,T)

    if Mod==None:
        return X
    else:
        return X%Mod

#==================================================
#Find_Sum系
def Find_Range_Sum(Range,S):
    """Range=[(A_0,B_0),...,(A_{N-1}, B_{N-1})] としとたき,
    A_i<=X_i<=B_i, X_0+...+X_{n-1}=S を満たす組の例を1つ求める.

    A_i<=B_i
    """

    alpha=beta=0
    for a,b in Range:
        alpha+=a
        beta +=b

    if not (alpha<=S<=beta): return None

    N=len(Range)
    X=[a for a,_ in Range]
    remain=S-sum(X)
    for i in range(N):
        y=min(Range[i][1],X[i]+remain)
        remain-=y-X[i]
        X[i]=y
    return X
#==================================================
#幾何級数系

def Geometric_Sequence_Sum(r,n,Mod=None):
    """ sum_{i=0}^{n-1} r^i [(mod Mod)] """

    if Mod==None:
        if r==1: return n
        else: return (pow(r,n)-1)/(r-1)
    else:
        if r==1: return n%Mod
        else: return (pow(r,n,(r-1)*Mod)//(r-1))%Mod
