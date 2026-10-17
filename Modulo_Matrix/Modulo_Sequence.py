from Modulo_Matrix import *

def Linear_Recurrence_Sequence_Matrix(p: list[int]) -> Modulo_Matrix:
    """ 線形漸化式を表す行列を求める. 線形漸化式は以下の形式である.
        a_{k + d} = p[0] a[k] + p[1] a[k + 1] + ... + p[d - 1] a[n + d - 1]

    Args:
        p (list[int]): 線形漸化式の係数のリスト

    Returns:
        Modulo_Matrix: 線形漸化式を表す行列
    """
    A = [p[::-1]]
    d = len(p)
    for i in range(d - 1):
        A.append([1 if j == i else 0 for j in range(d)])
    return Modulo_Matrix(A)

#漸化式と行列
def Linear_Recurrence_Sequence_Value(p: list[int], x: list[int], N: int) -> int:
    """ 以下の形で表される線形漸化式 (a_n) の第 n 項を求める. ただし, d := len(x) とする.
        a_k = x_k (k = 0, 1, ..., d - 1)
        a_{k + d} = p[0] a[k] + p[1] a[k + 1] + ... + p[d - 1] a[n + d - 1]

    Args:
        p (list[int]): 線形漸化式の係数のリスト
        x (list[int]): 先頭 d 項
        N (int): 求める項の番号

    Returns:
        int: a_N
    """

    assert len(p) == len(x)
    d = len(p)

    if N < d:
        return x[N]

    A = Linear_Recurrence_Sequence_Matrix(p)

    top_row_rev = pow(A, N - d + 1).ele[0][::-1]
    return sum(top_row_rev[i] * x[i] for i in range(d)) %Mod
