def Run_Length_Encoding(S) -> list:
    """ 列 S に対する Run Length Encoding を行う.

    Args:
        S: 列

    Returns:
        list: Run Length Encoding の結果
    """

    if not S:
        return []

    RLE = []
    l = 0
    while l < len(S):
        r = l + 1
        while r < len(S) and S[r] == S[l]:
            r += 1

        RLE.append((S[l], r - l))
        l = r

    return RLE

def Alternating_Length_Encoding(S, first, second, equal = True) -> tuple[list[int], list[int]]:
    x = []
    y = []

    if S[0] == second:
        x.append(0)

    for a, k in Run_Length_Encoding(S):
        if a == first:
            x.append(k)
        else:
            y.append(k)

    if equal and len(x) > len(y):
        y.append(0)

    return x, y
