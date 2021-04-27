def Binary_Search_Find(A,x,sort=True):
    """2分探索によって,Aにxが存在するかどうかを調べる.

    A:リスト
    x:調べる要素
    sort:ソートをする必要があるかどうか(Trueで必要)
    """
    if sort:
        A.sort()

    if x<A[0] or A[-1]<x:
        return False

    L,R=0,len(A)
    while R-L>0:
        C=L+(R-L)//2
        if x<A[C]:
            R=C
        elif x>A[C]:
            L=C+1
        else:
            return True
    return False

def Binary_Search_Index(A,x,sort=True,Offset=0):
    """2分探索によって,Aにxが存在するれば,そのインデックスを返す.
    (xが複数ある時,返ってくるインデックスは不定)

    A:リスト
    x:調べる要素
    sort:ソートをする必要があるかどうか(Trueで必要)
    Offset=0:インデックス+Offsetの値を返す.
    """
    if sort:
        A.sort()

    if x<A[0] or A[-1]<x:
        return None

    L,R=0,len(A)
    while R-L>0:
        C=L+(R-L)//2
        if x<A[C]:
            R=C
        elif x>A[C]:
            L=C+1
        else:
            return C+Offset
    return None

def Binary_Search_Small_Count(A,x,equal=False,sort=False):
    """2分探索によって,x未満の要素の個数を調べる.

    A:リスト
    x:調べる要素
    sort:ソートをする必要があるかどうか(Trueで必要)
    equal:Trueのときはx"未満"がx"以下"になる
    """
    if sort:
        A.sort()

    if A[0]>x or ((not equal) and A[0]==x):
        return 0

    L,R=0,len(A)
    while R-L>1:
        C=L+(R-L)//2
        if A[C]<x or (equal and A[C]==x):
            L=C
        else:
            R=C

    return L+1

def Binary_Search_Big_Count(A,x,equal=False,sort=False):
    """2分探索によって,xを超える要素の個数を調べる.

    A:リスト
    x:調べる要素
    sort:ソートをする必要があるかどうか(Trueで必要)
    equal:Trueのときはx"を超える"がx"以上"になる
    """

    if sort:
        A.sort()

    if A[-1]<x or ((not equal) and A[-1]==x):
        return 0

    L,R=-1,len(A)-1
    while R-L>1:
        C=L+(R-L)//2
        if A[C]>x or (equal and A[C]==x):
            R=C
        else:
            L=C
    return len(A)-R

def Binary_Search_Equal_Count(A,x,sort=False):
    """2分探索によって,xの個数を調べる.

    A:リスト
    x:調べる要素
    sort:ソートをする必要があるかどうか(Trueで必要)
    equal:Trueのときはx"を超える"がx"以上"になる
    """

    if sort:
        A.sort()

    if x<A[0] or A[-1]<x:
        return 0

    X=Binary_Search_Small_Count(A,x,equal=True)
    Y=Binary_Search_Small_Count(A,x,equal=False)
    return X-Y

def Binary_Search_Low_Value(A,x,equal=False,sort=False):
    """Aのx未満の要素の中で最大のものを出力する.

    A:リスト
    x:調べる要素
    sort:ソートをする必要があるかどうか(Trueで必要)
    equal:Trueのときはx"未満"がx"以下"になる
    ※全ての要素がx以上(超える)場合はNoneが返される.
    """

    if sort:
        A.sort()

    if A[0]>x or ((not equal) and A[0]==x):
        return None

    L,R=0,len(A)
    while R-L>1:
        C=L+(R-L)//2
        if A[C]<x or (equal and A[C]==x):
            L=C
        else:
            R=C

    return A[L]

def Binary_Search_High_Value(A,x,equal=False,sort=False):
    """Aのxを超える要素の中で最小のものを出力する.

    A:リスト
    x:調べる要素
    sort:ソートをする必要があるかどうか(Trueで必要)
    equal:Trueのときはx"を超える"がx"以上"になる
    ※全ての要素がx以上(超える)場合はNoneが返される.
    """

    if sort:
        A.sort()

    if A[-1]<x or ((not equal) and A[-1]==x):
        return None

    L,R=-1,len(A)-1
    while R-L>1:
        C=L+(R-L)//2
        if A[C]>x or (equal and A[C]==x):
            R=C
        else:
            L=C
    K=len(A)-R
    return A[-K]

def General_Binary_Increase_Search(L,R,cond,Integer=True,ep=1/(1<<20),Times=50):
    """条件式が単調増加であるとき,一般的な二部探索を行う.
    L:解の下限
    R:解の上限
    cond:条件(1変数関数,広義単調減少 or 広義単調減少を満たす)
    Integer:解を整数に制限するか?
    ep:Integer=Falseのとき,解の許容する誤差
    """
    if not(cond(R)):
        return None

    if cond(L):
        return L

    if Integer:
        R+=1
        while R-L>1:
            C=L+(R-L)//2
            if cond(C):
                R=C
            else:
                L=C
        return R
    else:
        while (R-L)>=ep and Times:
            Times-=1
            C=L+(R-L)/2
            if cond(C):
                R=C
            else:
                L=C
        return R

def General_Binary_Decrease_Search(L,R,cond,Integer=True,ep=1/(1<<20),Times=50):
    """条件式が単調減少であるとき,一般的な二部探索を行う.
    L:解の下限
    R:解の上限
    cond:条件(1変数関数,広義単調減少 or 広義単調減少を満たす)
    Integer:解を整数に制限するか?
    ep:Integer=Falseのとき,解の許容する誤差
    """

    if not(cond(L)):
        return None

    if cond(R):
        return R

    if Integer:
        L-=1
        while R-L>1:
            C=L+(R-L)//2
            if cond(C):
                L=C
            else:
                R=C
        return L
    else:
        while (R-L)>=ep and Times:
            Times-=1
            C=L+(R-L)/2
            if cond(C):
                L=C
            else:
                R=C
        return L

def Ternary_Search_Minimize(L,R,f,Integer=True,arg=False,ep=1/(1<<20),Times=50):
    """3部探索による最小値を求める.

    f:[L,R]内で下に凸または単調減少
    """
    if Integer:
        while (R-L)>3:
            a=(2*L+R)//3
            b=(L+2*R)//3
            p=f(a);q=f(b)
            if p<=q:
                R=b
            else:
                L=a

        a=(2*L+R)//3
        b=(L+2*R)//3
    else:
        while (R-L)>=ep and Times:
            Times-=1
            a=(2*L+R)/3
            b=(L+2*R)/3

            p=f(a);q=f(b)
            if p<=q:
                R=b
            else:
                L=a

        a=(2*L+R)/3
        b=(L+2*R)/3

    if arg:
        y=float("inf")
        argx=-1
        for x in [L,a,b,R]:
            p=f(x)
            if y>p:
                y=p
                argx=x
        return y,argx
    else:
        return min(f(L),f(a),f(b),f(R))

def Ternary_Search_Maximize(L,R,f,Integer=True,arg=False,ep=1/(1<<20),Times=50):
    """3部探索による最大値を求める.

    f:[L,R]内で上に凸または単調増加
    """
    if Integer:
        while (R-L)>3:
            a=(2*L+R)//3
            b=(L+2*R)//3
            p=f(a);q=f(b)
            if p>=q:
                R=b
            else:
                L=a

        a=(2*L+R)//3
        b=(L+2*R)//3
    else:
        while (R-L)>=ep and Times:
            Times-=1
            a=(2*L+R)/3
            b=(L+2*R)/3

            p=f(a);q=f(b)
            if p>=q:
                R=b
            else:
                L=a

        a=(2*L+R)/3
        b=(L+2*R)/3

    if arg:
        y=-float("inf")
        argx=-1
        for x in [L,a,b,R]:
            p=f(x)
            if y<p:
                y=p
                argx=x
        return y,argx
    else:
        return min(f(L),f(a),f(b),f(R))