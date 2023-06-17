def Hungarian(A, minimize=False, mode=False):
    """ 行列 A に対してハンガリアン法を適用し, 最大値を求める.

    A: 行列
    minimize: True にすると, 最小値を求める
    mode: True にすると, 最大値 (最小値) を達成する例も出力する.

    Reference: https://judge.yosupo.jp/submission/34963
    """
    if minimize:
        if mode:
            score, x=Hungarian([[-a_ij for a_ij in Ai] for Ai in A], False, True)
            return -score,x
        else:
            return -Hungarian([[-a_ij for a_ij in Ai] for Ai in A], False, False)

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

    score=0
    for i,j in enumerate(x):
        score+=A[i][j]

    return (score,x) if mode else score
