def Divisors(N: int) -> list[int]:
    """ N の約数全体

    Args:
        N (int): 0 ではない整数

    Returns:
        list[int]: N の「正の」約数を昇順に並べた列
    """

    assert N != 0

    N = abs(N)

    small, large = [], []
    k = 1
    while k * k <= N:
        if N % k== 0:
            small.append(k)
            large.append(N // k)

        k+=1

    # 平方数のとき, small[-1] と large[-1] が重複する値になるので, 一方から削除する.
    if small[-1] == large[-1]:
        large.pop()

    small.extend(reversed(large))
    return small

def Divisors_from_Prime_Factor(prime_factors: list[tuple[int, int]], sort: bool = False) -> list[int]:
    """prime_factors = [(p0, e0), (p1, e1), ...] に対して, N = p0^e0 * p1^e1 * ... としたときの N の正の約数を求める.

    Args:
        prime_factors (list[tuple[int, int]]): 素因数分解
        sort (bool, optional): True にすると, 出力される約数のリストがソート済みになる. Defaults to False.

    Returns:
        list[int]: N = p0^e0 * p1^e1 * ... の正の約数
    """

    divisors = [1]
    for p, e in prime_factors:
        q = 1
        n = len(divisors)
        for _ in range(e):
            q *= p
            for j in range(n):
                divisors.append(divisors[j] * q)

    if sort:
        divisors.sort()

    return divisors

#高度合成数
#参考元:https://qiita.com/convexineq/items/e3d599cb9f91a73f936d
def Highly_Composite_Number(N):
    """ N 以下の高度合成数を求める.
    """

    from heapq import heappop,heappush
    from math import log
    prime = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263]
    lim = [[2*int(log(p,q)) for q in prime] for p in prime] #枝刈り用配列
    # 初期状態
    q = [(2,2,[1])] # (n,nの約数の個数、nの指数表記)を保存する heapq
    res = [(1,1,[])]

    while q and q[0][0] <= N:
        n,val,lst = heappop(q)
        if val > res[-1][1]: #条件をみたすなら答に追加
            res.append((n,val,lst[:]))
        L = len(lst)
        e0 = lst[0]
        #全部1なら新しい素数で横に伸ばせる
        if e0 == 1:
            heappush(q,(n*prime[L],val*2,[1]*(L+1)))
        #最上段の上を横方向に積む
        for i in range(L):
            if e0 > lst[i]: break #段差があると、もう伸ばせない
            if e0 >= lim[L][i]: break #枝刈り（重要）
            n *= prime[i]
            if n <= N:
                lst[i] += 1
                val = val//(e0+1)*(e0+2)
                heappush(q,(n,val,lst[:]))
    return res
