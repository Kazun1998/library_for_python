#商列挙
def Quotient_Range(N):
    """ N で割った商の可能性を全て列挙する.

    [Input]
    N: 正整数

    [Output]
    X: リスト
    Xの各要素 (t, x, y) は x <= k <= y であることと, floor(N/k) = t が同値であることを表す.

    [Note]
    各 (t, x, y) に対して, x <= k <= y の範囲において, N mod k は等差数列になる.
    """
    X = []

    # Step 1: k<=sqrt(N) の範囲について k を全探索する.
    k = 1
    while k * k <= N:
        X.append((N//k, k, k))
        k += 1

    # Step 2: t<=sqrt(N) の範囲において, floor(N/k)=t を満たす k の範囲を求める.
    for t in range(k, 0, -1):
        l = N//(t + 1) + 1
        r = N//t

        if (l <= r) and (X[-1][1] < l):
            X.append((t, l, r))

    return X

def Quotient_Range_Yielder(N):
    """ N で割った商の可能性を全て列挙する.

    [Input]
    N: 正整数

    [Output]
    X: リスト
    Xの各要素 (t, x, y) は x <= k <= y であることと, floor(N/k) = t が同値であることを表す.

    [Note]
    各 (t, x, y) に対して, x <= k <= y の範囲において, N mod k は等差数列になる.
    """

    # Step 1: k<=sqrt(N) の範囲について k を全探索する.
    k = 1
    while k * k <= N:
        yield (N//k, k, k)
        k += 1

    # Step 2: t<=sqrt(N) の範囲において, floor(N/k)=t を満たす k の範囲を求める.
    prev_l = k - 1
    for t in range(k, 0, -1):
        l = N//(t + 1) + 1
        r = N//t

        if (l <= r) and (prev_l < l):
            yield (t, l, r)
            prev_l = l

def Ceiling_Range(N, left = None):
    """ 非負整数 x を全て走るときの ceil(N/x) の可能性を全て列挙する.

    [Input]
    N: 正整数

    [Output]
    X: リスト
    X の各要素 (t, x, y) は x <= k <= y であることと, ceil(N/k) = t が同値であることを表す.

    """

    from math import isqrt

    N_sqrt = isqrt(N)
    ceil = lambda k: (N + k - 1) // k
    X = []

    # Step 1: ceil(N/k) < N_sqrt となる k の範囲で個別に求める.
    k = 1
    while True:
        if ceil(k) == N_sqrt:
            break

        X.append((ceil(k), k, k))
        k += 1

    # Step 2: ceil(N/k) >= N_sqrt となる k の範囲をまとめ上げる.
    for t in range(N_sqrt, 1, -1):
        l = ceil(t)
        r = ceil(t - 1) - 1
        if (l <= r) and (X[-1][1] < l):
            X.append((t, l, r))

    if left == None:
        X.append((1, N, float("inf")))
    else:
        left = max(left, N)
        X.append((1, N, left))

    return X

def Ceiling_Range_Yielder(N, left = None):
    """ 非負整数 x を全て走るときの ceil(N/x) の可能性を全て列挙する.

    [Input]
    N: 正整数

    [Output]
    X: リスト
    X の各要素 (t, x, y) は x <= k <= y であることと, ceil(N/k) = t が同値であることを表す.

    """

    from math import isqrt

    N_sqrt = isqrt(N)
    ceil = lambda k: (N + k - 1) // k

    # Step 1: ceil(N/k) < N_sqrt となる k の範囲で個別に求める.
    k = 1
    while True:
        if ceil(k) == N_sqrt:
            break

        yield (ceil(k), k, k)
        k += 1

    # Step 2: ceil(N/k) >= N_sqrt となる k の範囲をまとめ上げる.
    prev_r = k - 1
    for t in range(N_sqrt, 1, -1):
        l = ceil(t)
        r = ceil(t - 1) - 1
        if (l <= r) and (prev_r < l):
            yield (t, l, r)
            prev_l = r

    if left == None:
        yield (1, N, float("inf"))
    else:
        left = max(left, N)
        yield (1, N, left)

def Reminder_Enumeration(N, r):
    """ N を q 割った余りが r になる q を全て列挙する.

    N: 正整数
    r: 非負整数, N != r
    """

    assert N != r, "無限個あります."

    k = 1
    X = []; Y = []
    N -= r
    while k * k <= N:
        if N % k == 0:
            if k > r:
                X.append(k)
            if k * k != N and N//k > r:
                Y.append(N//k)
        k += 1
    return X + Y[::-1]

def Next_Remainder(x, p, r):
    """ x 以上で p で割って r 余る整数のうち, 最小の整数を求める.

    """

    if x % p <= r:
        return (x//p) * p + r
    else:
        return (x//p + 1) * p + r

def Previous_Remainder(x, p, r):
    """ x 以下で p で割って r 余る整数のうち, 最大の整数を求める.

    """

    if r <= x % p:
        return (x//p) * p + r
    else:
        return (x//p - 1) * p + r
