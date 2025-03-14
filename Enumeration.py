"""
Mod はグローバル変数からの指定とする.
"""

"""
積
"""
def product_modulo(*X: int) -> int:
    y = 1
    for x in X:
        y = (x * y) % Mod
    return y

"""
階乗
"""
def Factor(N: int) -> list[int]:
    """ 0!, 1!, 2!, ..., N! (を Mod で割った余り) からなるリストを生成する.

    Args:
        N (int): 上限

    Returns:
        list[int]: 第 k 要素が k! (mod Mod) からなる長さ (N + 1) のリスト
    """

    f = [1] * (N + 1)
    for k in range(1, N + 1):
        f[k] = (k * f[k - 1]) % Mod
    return f

def Factor_with_inverse(N: int) -> tuple[list[int], list[int]]:
    """ [0!, 1!, 2!, ..., N!], [(0!)^-1, (1!)^-1, ..., (N!)^-1] からなるリストを生成する.

    Args:
        N (int): 上限

    Returns:
        tuple[list[int], list[int]]:
            第 1 要素のリストは第 k 要素が k! (mod Mod) からなる長さ (N + 1) のリスト
            第 2 要素のリストは第 k 要素が (k!)^(-1) (mod Mod) からなる長さ (N + 1) のリスト
    """

    f = Factor(N)
    g = [0] * (N + 1)

    N = min(N, Mod - 1)
    g[N] = pow(f[N], -1, Mod)

    for k in range(N - 1, -1, -1):
        g[k] = ((k + 1) * g[k + 1]) % Mod

    return f, g

def Double_Factor(N: int) -> list[int]:
    """ 0!!, 1!!, 2!!, ..., N!! (を Mod で割った余り) からなるリストを生成する.

    Args:
        N (int): 上限

    Returns:
        list[int]: 第 k 要素が k!! (mod Mod) からなる長さ (N + 1) のリスト
    """

    f = [1] * (N + 1)
    for k in range(2, N + 1):
        f[k] = k * f[k - 2] % Mod
    return f

def Modular_Inverse(N: int) -> list[int]:
    """ (mod Mod) における 1^(-1), 2^(-1), ..., N^(-1) からなるリストを生成する.

    Args:
        N (int): 上限

    Returns:
        list[int]: 初項は -1, 第 k 要素が k^-1 (mod Mod) からなる長さ (N + 1) のリスト
    """

    inv = [1] * (N + 1)
    inv[0] = -1

    for k in range(2, N + 1):
        q, r = divmod(Mod, k)
        inv[k] = (-q * inv[r]) % Mod
    return inv

"""
組み合わせの数
Factor_with_inverse で fact, fact_inv を既に求めていることが前提 (グローバル変数)
"""

def nCr(n: int, r: int) -> int:
    """ nCr (1,2,...,n から相異なる r 個の整数を選ぶ方法) を求める.

    Args:
        n (int):
        r (int):

    Returns:
        int: nCr
    """

    if 0 <= r <= n:
        return fact[n] * (fact_inv[r] * fact_inv[n - r] % Mod) % Mod
    else:
        return 0

def nPr(n: int, r: int) -> int:
    """ nPr (1,2,...,n から相異なる r 個の整数を選び, 並べる方法) を求める.

    Args:
        n (int):
        r (int):

    Returns:
        int: nPr
    """

    if 0 <= r <= n:
        return (fact[n] * fact_inv[n - r]) % Mod
    else:
        return 0

def nHr(n: int, r: int) -> int:
    """ nHr (1,2,...,n から重複を許して r 個の整数を選ぶ方法) を求める.
    ※ fact, fact_inv は第 n+r-1 項まで必要

    Args:
        n (int):
        r (int):

    Returns:
        int: nHr
    """

    if n == r == 0:
        return 1
    else:
        return nCr(n + r - 1, r)

def Multinomial_Coefficient(*K: int) -> int:
    """ K = [k_0, ..., k_{r-1}] に対して, k_0, ..., k_{r-1} に対する多項係数を求める.

    Args:
        K (int):

    Returns:
        int: k_0, ..., k_{r-1} に対する多項係数. つまり, (sum(K)!)/(k_0! k_1! ... k_{r-1}!)
    """

    g_inv = 1
    for k in K:
        g_inv *= fact_inv[k]
        g_inv %= Mod

    return fact[sum(K)] * g_inv % Mod

def Binomial_Coefficient_Modulo_List(n: int) -> list[int]:
    """ n を固定し, r = 0, 1, ..., n としたときの nCr (mod Mod) のリストを出力する.

    Args:
        n (int): 固定する nCr の n の部分

    Returns:
        list[int]: 第 r 要素が nCr である長さ (n + 1) の配列.
    """

    X = [1] * (n + 1)
    inv = Modular_Inverse(n + 1)
    for r in range(1, n + 1):
        X[r] = ((n + 1 - r) * inv[r] % Mod) * X[r - 1] % Mod
    return X

def Pascal_Triangle(N: int, square: bool = False) -> list[int]:
    """ 0 <= n <= N, 0 <= r <= n に対する nCr を求める.

    Args:
        N (int): 上限
        square (bool, optional): True にすると, r の範囲が 0 <= r <= N になる. Defaults to False.

    Returns:
        list[int]: 第 (n, r) 要素が nCr である二重添字リスト
    """

    if square:
        X = [[0] * (N + 1) for _ in range(N + 1)]
        for n in range(N + 1):
            X[n][0] = 1
            for r in range(1, (N if square else n) + 1):
                X[n][r] = (X[n - 1][r] + X[n - 1][r - 1]) % Mod
    else:
        X = [[0] * (n + 1) for n in range(N + 1)]
        for n in range(N + 1):
            X[n][0] = X[n][n] = 1
            for r in range(1, (N if square else n)):
                X[n][r] = (X[n - 1][r] + X[n - 1][r - 1]) % Mod

    return X

def Lucas_Combination(n: int, r: int) -> int:
    """ Lucas の定理を用いて nCr (mod Mod) を求める.

    Args:
        n (int):
        r (int):

    Returns:
        int: nCr (mod Mod)
    """

    X = 1
    while n or r:
        ni = n%Mod; ri = r%Mod
        n //= Mod; r //= Mod

        if ni < ri:
            return 0

        beta = fact_inv[ri] * fact_inv[ni - ri] % Mod
        X *= (fact[ni] * beta) % Mod
        X %= Mod
    return X

def Catalan_Number(N: int) -> int:
    """ Catalan 数 C(N) を求める.
    ※ C(N) = (2N)!/((N+1)! N!) であるため, 2N! までの値が必要

    Args:
        N (int):

    Returns:
        int: Catalan 数 C(N)
    """

    g_inv = fact_inv[N + 1] * fact_inv[N] % Mod
    return fact[2 * N] * g_inv % Mod

"""
等比数列
"""

def Geometric_Sequence(a: int, r: int, N: int) -> list[int]:
    """ k = 0, 1, ..., N に対する a*r^k を出力する.

    Args:
        a (int): 初項
        r (int): 公比
        N (int): k の最大値

    Returns:
        list[int]: 第 k 項が a*r^k である長さ (N + 1) のリスト
    """

    a %= Mod; r %= Mod
    X = [0] * (N + 1)
    X[0] = a
    for k in range(1, N + 1):
        X[k] = r * X[k - 1] %Mod
    return X

def Geometric_Inverse_Sequence(a: int, r: int, N: int) -> list[int]:
    """ k = 0, 1, ..., N に対する a/r^k を出力する.

    Args:
        a (int): 初項
        r (int): 公比の逆数
        N (int): k の最大値

    Returns:
        list[int]: 第 k 項が a/r^k である長さ (N + 1) のリスト
    """


    a %= Mod
    r_inv = pow(r, -1, Mod)
    X = [0] * (N + 1)
    X[0] = a

    for k in range(1, N + 1):
        X[k] = r_inv * X[k - 1] % Mod
    return X

"""
積和
"""
def Sum_of_Product(*X: list[int]) -> int:
    """ 長さが等しいリスト X_0, X_1, ..., X_k に対して, sum(X_0[i] * X_1[i] * ... * X_k[i]) を求める.

    Returns:
        int: 積和
    """

    return sum(product_modulo(*alpha) for alpha in zip(*X))

#==================================================

Mod = 1019999
