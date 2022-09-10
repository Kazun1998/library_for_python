"""
Note

三分探索を用いる際, f は以下のうちのどれかを見たしていなければならない.

* f は下 (上) に "狭義" 凸である
* a<b が存在して, f は [L,a] 上狭義単調減少 (増加), [a,b] 上定数, [b,R] 上狭義単調増加 (減少)
* fは単調減少 (単調増加)
"""

def Ternary_Search_Minimize_Integer(L, R, f, arg=False):
    """ 三分探索によって, 整数を定義域とする関数 f の [L,R] における最小値を求める.

    f: [L,R] 内で下に凸または単調減少
    """
    while (R-L)>3:
        a=(2*L+R)//3
        b=(L+2*R)//3

        p=f(a); q=f(b)
        if p<=q:
            R=b
        else:
            L=a

    a=(2*L+R)//3
    b=(L+2*R)//3

    if arg:
        y,argx=f(L),L
        for x in [a,b,R]:
            p=f(x)
            if y>p:
                y,argx=p,x
        return y,argx
    else:
        return min(f(L),f(a),f(b),f(R))

def Ternary_Search_Minimize_Real(L, R, f, arg=False, ep=1/(1<<20), Times=50):
    """ 三分探索によって, 実数を定義域とする関数 f の [L,R] における最小値を求める.

    f: [L,R] 内で下に凸または単調減少
    """
    while (R-L)>=ep and Times:
        Times-=1
        a=(2*L+R)/3
        b=(L+2*R)/3

        p=f(a); q=f(b)
        if p<=q:
            R=b
        else:
            L=a

    a=(2*L+R)/3
    b=(L+2*R)/3

    if arg:
        y,argx=f(L),L
        for x in [a,b,R]:
            p=f(x)
            if y>p:
                y,argx=p,x
        return y,argx
    else:
        return min(f(L),f(a),f(b),f(R))

def Ternary_Search_Maximize_Integer(L, R, f, arg=False):
    """ 三分探索によって, 整数を定義域とする関数 f の [L,R] における最大値を求める.

    f: [L,R] 内で上に凸または単調増加
    """
    while (R-L)>3:
        a=(2*L+R)//3
        b=(L+2*R)//3

        p=f(a); q=f(b)
        if p>=q:
            R=b
        else:
            L=a

    a=(2*L+R)//3
    b=(L+2*R)//3

    if arg:
        y,argx=f(L),L
        for x in [a,b,R]:
            p=f(x)
            if y<p:
                y,argx=p,x
        return y,argx
    else:
        return max(f(L),f(a),f(b),f(R))

def Ternary_Search_Maximize_Real(L, R, f, arg=False, ep=1/(1<<20), Times=50):
    """ 三分探索によって, 実数を定義域とする関数 f の [L,R] における最大値を求める.

    f: [L,R] 内で上に凸または単調増加
    """

    while (R-L)>=ep and Times:
        Times-=1
        a=(2*L+R)/3
        b=(L+2*R)/3

        p=f(a); q=f(b)
        if p>=q:
            R=b
        else:
            L=a

    a=(2*L+R)/3
    b=(L+2*R)/3

    if arg:
        y,argx=f(L),L
        for x in [a,b,R]:
            p=f(x)
            if y<p:
                y,argx=p,x
        return y,argx
    else:
        return max(f(L),f(a),f(b),f(R))
