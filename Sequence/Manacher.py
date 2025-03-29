def Manacher(S) -> list[int]:
    """ S の各文字に対して, その文字を中心とする極大な回分の半径を求める.

    Args:
        S:

    Returns:
        list[int]: 第 i 要素は S の i 文字目を中心とする極大な回分の半径 (その極大な回分の長さを y とすると, 半径は (y + 1) / 2).
    """

    i = j = 0
    res = [0] * len(S)
    while i < len(S):
        while (i - j >= 0) and (i + j < len(S)) and (S[i - j] == S[i + j]):
            j += 1

        res[i] = j
        k = 1
        while (i - k >= 0) and (k + res[i - k] < j):
            res[i + k] = res[i - k]
            k += 1

        i += k; j -= k

    return res

def Manacher_with_even(S, dummy = None) -> tuple[list[int], list[int]]:
    """ S の各文字と文字と文字の間について, そこを中心とする極大な回分の半径を求める.

    Args:
        S:
        dummy (optional): S に含まれることがない要素. Defaults to None.

    Returns:
        tuple[list[int], list[int]]: (odd, even)
            odd: Manachar(S) の返り値と等しい.
            even: 第 i 要素は S の i 文字目と (i + 1) 文字目の間を中心とする極大な回分の半径
    """
    T = [dummy] * (2 * len(S) - 1)
    for i in range(len(S)):
        T[2 * i] = S[i]

    res = Manacher(T)
    odd = [(a + 1) // 2 for a in res[::2]]
    even = [b // 2 for b in res[1::2]]

    return odd, even
