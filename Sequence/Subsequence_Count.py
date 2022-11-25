def Subsequence_Count(S, Mod=None, empty=True):
    """ 列 S の異なる (連続とは限らない) 部分列の個数を求める.

    Mod: 余り
    empty: 空部分列を認めるならば True, 認めないならば False.
    """

    X=0
    dp={}
    for a in S:
        Y=2*X+1-dp.get(a, 0)
        dp[a]=X+1

        if Mod is None:
            X=Y
        else:
            X=Y%Mod

    if Mod is not None:
        return (X+empty)%Mod
    else:
        return X+empty
