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

