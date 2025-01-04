class BaseException(Exception):
    def __init__(self, error_base):
        self.error_base = error_base

    def __str__(self):
        return f"指定した底 {self.error_base} は不正な底です."

def Integer_Digits(n: int, b: int = 10, l: int = None) -> list[int]:
    """ 整数 n の底を b とした場合の表現を求める.

    Args:
        n (int): N
        b (int, optional): 底 (b >= 2). Defaults to 10.
        l (int): 長さが 0 になるように左側に 0 を埋めたり, 右から l 要素を取得する.

    Returns:
        list[int]: 表示
    """

    assert b >= 2, BaseException(b)

    n = abs(n)
    digits = []

    if l is None:
        while (n > 0) or (not digits):
            n, r = divmod(n, b)
            digits.append(r)
    else:
        for _ in range(l):
            n, r = divmod(n, b)
            digits.append(r)

    return digits[::-1]

def Integer_Length(n: int, b: int = 10) -> int:
    """ 整数 n の底を b とした場合の桁数を求める (0 は 0 桁とする).

    Args:
        n (int): N
        b (int, optional): 底 (b >= 2). Defaults to 10.

    Returns:
        int: 桁数
    """

    assert b >= 2, BaseException(b)
    return len(Integer_Digits(n, b)) if n != 0 else 0

def Digit_Sum(n: int, b: int = 10) -> int:
    """ 整数 n の底を b とした場合の桁和を求める.

    Args:
        n (int): N
        b (int, optional): 底 (b >= 2). Defaults to 10.

    Returns:
        int: 桁和
    """

    return sum(Integer_Digits(n, b))

def Digit_Count(n: int, b: int) -> list[int]:
    """ 整数 n の底を b とした場合における各数の出現回数を求める.

    Args:
        n (int): N
        b (int): 底

    Returns:
        list[int]: 長さ b の配列. 第 k 要素は k の出現回数.
    """

    assert b >= 2, BaseException(b)

    count = [0] * b
    for d in Integer_Digits(n, b):
        count[d] += 1
    return count

def From_Digits(digits: list[int], b: int = 10) -> int:
    """ 底を b とした場合に digit がなす整数を返す (Interger_Digit の逆関数)

    Args:
        digits (list[int]): 数のリスト
        b (int, optional): 底 (b >= 2). Defaults to 10.

    Returns:
        int: 整数
    """

    assert b >= 2, BaseException(b)

    res = 0
    for x in digits:
        res = b * res + x
    return res
