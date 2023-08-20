#最小公倍数
def lcm(m,n):
    from math import gcd
    return (m//gcd(m,n))*n

def LCM(*X):
    from functools import reduce
    return reduce(lcm,X)

#floor(a^(1/k)) を求める.
def Floor_Root(a,k):
    """floor(a^(1/k)) を求める.

    a:非負整数
    k:正の整数
    """
    assert 0<=a and 0<k
    if a==0: return 0
    if k==1: return a

    #大体の値を求める.
    x=int(pow(a,1/k))

    #増やす
    while pow(x+1,k)<=a:
        x+=1

    #減らす
    while pow(x,k)>a:
        x-=1
    return x

#ceil(a^(1/k)) を求める.
def Ceil_Root(a,k):
    """ceil(a^(1/k)) を求める.

    a:非負整数
    k:正の整数
    """
    assert 0<=a and 0<k
    if a==0:
        return 0
    if k==1:
        return a

    #大体の値を求める.
    x=int(pow(a,1/k))+1

    #増やす
    while pow(x,k)<a:
        x+=1

    #減らす
    while a<=pow(x-1,k):
        x-=1
    return x

def kth_Power(a,k):
    """ 整数 a が k 乗数かどうかを求め, そうならば, b^k=a を満たす k を返す.

    [Input]
    a: int
    k: int (k>0)

    [Output]
    存在しない  : None
    存在する    : b^k=a を満たす b
    """

    if k%2==0:
        if a<0:
            return None
        b=Floor_Root(a,k)
        return b if pow(b,k)==a else None
    else:
        sgn=1 if a>=0 else -1
        b=Floor_Root(abs(a),k)
        return sgn*b if pow(sgn*b,k)==a else None
