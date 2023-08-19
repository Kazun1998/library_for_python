#拡張ユークリッドの互除法
def Find_Extend_Euclid(a: int, b: int):
    """ax+by=gcd(a, b) を満たす (x, y, gcd(a, b)) を 1 つ求める.

    a,b:整数
    """
    from math import gcd
    g = gcd(a, b)
    if g == 0:
        return (1, 0, 0)

    x = pow(a//g, -1, b//g)
    y = - (a*x-g) // b
    return (x, y, g)

def Solve_Bezout_Identity(a, b, c, lx, rx, ly, ry, extgcd = None):
    """ a x + b y = c, lx <= x <=rx, ly <= y <= ry を満たす整数 (x,y) について求める.

    [Input]
    a != 0, b != 0 でなくてはならない.
    extgcd : (s, t) の形のタプルで, a s + b t = gcd(a, b) を満たしていなければならない.

    [Output]
    答えが存在する場合:
    (p0, p1, q0, q1, l, r) の形のタプルで, 以下を意味する
    x = p0 + p1 k, y = q0 + q1 k, l <= k <= r

    答えが存在しない場合: None
    """

    assert a != 0 and b != 0

    sgn_a = 1 if a > 0 else -1; a = abs(a)
    sgn_b = 1 if b > 0 else -1; b = abs(b)

    if extgcd is None:
        s, t, g = Find_Extend_Euclid(a, b)
    else:
        s, t = extgcd
        g = a * s + b * t

    if c % g != 0:
        return None
