from Point import *
from Circle import *
from Triangle import *

def Minimum_Enclosing_Circle(S: list[Point], trial: int = 100) -> Circle:
    """ 点のリスト S に関する最小内包円を求める.

    Args:
        S (list[Point]): 平面上の点のリスト
        trial (int, optional): 求める際に行う三分探索における判定の回数. Defaults to 100.

    Returns:
        Circle: _description_
    """

    # |S| <= 3 のときは明示的に求められる.
    if len(S) == 1:
        # |S| = 1 の場合はその点が最小内包円
        return Circle(S[0], 0)
    elif len(S) == 2:
        # |S| = 2 の場合はその 2 点を直径とする円が最小内包円
        M = (S[0] + S[1]) / 2
        return Circle(M, abs(M - S[0]))
    elif len(S) == 3:
        A, B, C = S
        a, b, c = abs(B - C), abs(C - A), abs(A - B)
        a2, b2, c2 = a * a, b * b, c * c

        # 三角形 ABC が鈍角三角形のときは, 一番長い辺を直径とする円が最小内包円になる.
        if compare(a2, b2 + c2) == 1:
            return Minimum_Enclosing_Circle([B, C])
        elif compare(b2, c2 + a2) == 1:
            return Minimum_Enclosing_Circle([C, A])
        elif compare(c2, a2 + b2) == 1:
            return Minimum_Enclosing_Circle([A, B])

        # 三角形 ABC が鋭角三角形のときは, その三角形の外接円が最小内包円になる.
        ta = a2 * (-a2 + b2 + c2)
        tb = b2 * (a2 - b2 + c2)
        tc = c2 * (a2 + b2 - c2)
        s = ta + tb + tc

        K = (ta / s) * A + (tb / s) * B + (tc / s) * C
        return Circle(K, abs(K - A))

    def f(x, y):
        res = 0
        for p in S:
            dx = x - p.x; dy = y - p.y
            res = max(res, dx * dx + dy * dy)
        return sqrt(res)

    def g(x):
        L = y_min; R = y_max
        for _ in range(trial):
            a = (2 * L + R) / 3
            b = (L + 2 * R) / 3

            if f(x, a) > f(x, b):
                L = a
            else:
                R = b

        c = (L + R) / 2
        return f(x, c), c

    inf=float("inf")
    x_min,x_max=inf,-inf
    y_min,y_max=inf,-inf

    for p in S:
        x_min=min(x_min,p.x)
        x_max=max(x_max,p.x)
        y_min=min(y_min,p.y)
        y_max=max(y_max,p.y)

    L, R = x_min, x_max
    for _ in range(trial):
        a = (2 * L + R) / 3
        b = (L + 2 * R) / 3

        if g(a)[0] > g(b)[0]:
            L = a
        else:
            R = b

    X = (L + R) / 2
    r, Y = g(X)

    C = Point(X,Y)

    Q = sorted(
        [(0, abs(C - S[0])), (1, abs(C - S[1])),(2, abs(C - S[2]))],
        key = lambda t: t[1], reverse = True
        )

    for i in range(3, len(S)):
        m = (i, abs(C - S[i]))
        for k in range(3):
            if m[1] > Q[k][1]:
                Q[k], m = m, Q[k]
    return Minimum_Enclosing_Circle([S[j] for j,_ in Q])
