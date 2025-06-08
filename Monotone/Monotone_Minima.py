def Monotone_Minima(N: int, M: int, eval) -> list[int]:
    """ N 行 M 列の行列 A の第 (i, j) 要素が eval(i, j) であり, 以下の単調性を満たすとする.
        f(i) := min argmin_{j} A(i, j) としたとき, f(0) <= f(1) <= ... <= f(M - 1) が成り立つ.
    このとき, 0 <= i < N に対して, f(i) を求める.

    Args:
        N (int): 行の数
        M (int): 列の数
        eval (Callable[[int, int], int]): 第 (i, j) 要素が eval(i, j) になる.

    Returns:
        list[int]: 第 i 要素が f(i) である長さ N のリスト
    """
    res = [-1] * N
    stack = [(0, N, 0, M)]

    while stack:
        u, d, l, r = stack.pop()

        if d - u < 1:
            continue

        i = (u + d) // 2
        j = min(range(l, r), key = lambda j: eval(i, j))

        res[i] = j

        stack.append((u, i, l, j + 1))
        stack.append((i + 1, d, j, r))

    return res
