def Hungarian(A, maximize = True):
    """ 行列 A に対して, Hungarian 法を適用して, 割当問題の最適解を求める.

    Args:
        A: 行列
        maximize (bool, optional): True ならば最大値, False ならば最小値を求める.
        mode (bool, optional): _description_. Defaults to False.

    Reference:
        https://judge.yosupo.jp/submission/34963
    """

    if not maximize:
        pre_sol = Hungarian(A, True)
        return { 'value': -pre_sol['value'], 'assignment': pre_sol['assignment'] }

    inf=1<<31
    N=len(A)
    fx=[inf]*N
    fy=[0]*N
    x=[-1]*N
    y=[-1]*N
    i=0
    while i < N:
        t=[-1]*N
        s=[i]*(N + 1)
        p=q=0
        while p <= q and x[i] < 0:
            k, j = s[p], 0
            while j < N and x[i] < 0:
                if fx[k] + fy[j] == A[k][j] and t[j] < 0:
                    q += 1
                    s[q] = y[j]
                    t[j] = k
                    if s[q] < 0:
                        p = j
                        while p >= 0:
                            y[j] = k = t[j]
                            p = x[k]
                            x[k] = j
                            j = p
                j += 1
            p += 1
        if x[i] < 0:
            d = inf
            for k in range(q + 1):
                for j in range(N):
                    if t[j] < 0:
                        d = min(d, fx[s[k]] + fy[j] - A[s[k]][j])
            for j in range(N):
                if t[j] >= 0:
                    fy[j] += d
            for k in range(q + 1):
                fx[s[k]] -= d
        else:
            i += 1

    return { 'value': sum(A[i][j] for i, j in enumerate(x)), 'assignment': x}
