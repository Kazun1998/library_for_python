def Knapsack_01_Weight(items, weight):
    """ 非常に軽い 01- ナップサック問題を解く.

    items: (重さ, 価値) の形のタプル
    weight: ナップサックの耐久重量
    """

    dp = [0] * (weight + 1)
    for item in items:
        if item is None:
            continue

        w, v = item
        for a in range(weight, w - 1, -1):
            dp[a] = max(dp[a], dp[a - w] + v)

    packed_value = max(dp)
    packed_weight = dp.index(packed_value)
    knapsack = []
    for i, item in enumerate(items):
        if item is None:
            continue

        w, v = item
        if (w <= packed_weight) and (dp[packed_weight] == dp[packed_weight - w] + v):
            knapsack.append(i)
            packed_weight -= w

    return { 'value': packed_value, 'knapsack': knapsack }

def Knapsack_01_Value(items, weight):
    """ 価値が非常に小さい 01-Knapsack 問題を解く.

    items: (価値, 重さ) の形のタプル
    weight: ナップサックの耐久重量

    [計算量]
    O(N sum(v))
    """

    v_sum = sum(v for _, v in items)

    dp = [weight + 1] * (v_sum + 1)
    dp[0] = 0
    for item in items:
        if item is None:
            continue

        w, v = item
        for a in range(v_sum, v - 1, -1):
            dp[a] = min(dp[a], dp[a - v] + w)

    value = pointer = max(v for v in range(v_sum + 1) if dp[v] <= weight)
    knapsack = []
    for i, item in enumerate(items):
        if item is None:
            continue

        w, v = item
        if dp[pointer] == dp[pointer - v] + w:
            knapsack.append(i)
            pointer -= v

    return { 'value': value, 'knapsack': knapsack }

def Knapsack_01_Middle(List,Weight,Mode=False):
    """個数が非常に少ない01-Knapsack Problemを (半分全列挙で) 解く.

    List:各要素はタプル(v,w) の形で, vは価値, wは重さ
    [計算量]
    O(N 2^(N/2))

    [参考元]
    https://tjkendev.github.io/procon-library/python/dp/knapsack-meet-in-the-middle.html
    """

    def subset_sum(S):
        T={0:0}
        for v,w in S:
            T1=dict(T)
            for key,val in T.items():
                a=key+w
                if a>Weight:
                    continue
                if a in T1:
                    T1[a]=max(T1[a],val + v)
                else:
                    T1[a]=val+v
            T=T1

        v=-1
        R=[]
        for w in sorted(T):
            if T[w]>v:
                v=T[w]
                R.append((v,w))
        return R

    def merge(S,T):
        T=T[::-1]
        it=iter(T)
        v1,w1=next(it)

        t=0

        for v,w in S:
            while w+w1>Weight:
                v1,w1=next(it)

            if t<v+v1:
                t=v+v1
        return t

    N=len(List)
    A=subset_sum(List[:N//2])
    B=subset_sum(List[N//2:])
    return merge(A,B)
