#ハミング距離
def Hamming_Distance(S, T):
    """ 列の長さが等しい S, T におけるハミング距離を求める.

    S,T: (|S|=|T| を満たしていなければならない)
    """

    assert len(S)==len(T)
    return sum(int(S[i]!=T[i]) for i in range(len(S)))
