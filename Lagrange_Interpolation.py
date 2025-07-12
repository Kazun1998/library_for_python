def Lagrange_Interpolation_Point(F: list[tuple[int, int]], X: int, P: int) -> int:
    """ F の情報から, 多項式 f に関する P を法とする Lagrange 補完を行い, f(X) を求める.

    Args:
        F (list[tuple[int, int]]): [(x0, y0), ..., (xN,yN)] の形のリスト, i 番目の要素は, f が f(x[i]) = y[i] であることを意味する.
        X (int): 求める X の値
        P (int): 法

    Returns:
        int: f(X) mod P

    Complexity:
        O(N^2 + log P)
    """

    N = len(F) - 1

    x = [p[0] for p in F]
    y = [p[1] for p in F]

    X %= P
    z = 0
    for i in range(N + 1):
        a = b = 1
        for j in range(N + 1):
            if i == j:
                continue

            a *= X - x[j]; a %= P
            b *= x[i] - x[j]; b %= P

        c = a * pow(b, -1, P) % P
        z += y[i] * c % P

    return z % P

def Lagrange_Interpolation_Polynomial(T,P):
    """ 法が P の下でのLagrange 補間を行い, 多項式の係数リストを返す.

    [Input]
    T: [(x_0,y_0), ..., (x_N, y_N)]: F(x_n)=y_n  (i !=j => x_i != x_j (mod P))
    P: 法

    [Output]
    [[X^0]F, [X^1]F, ..., [X^{N-1}]F ]

    [Complexity]
    O(N^2)

    [Thanks]
    hamayanhamayan
    """

    N=len(T)
    X=[0]*N; Y=[0]*N
    for i in range(N):
        X[i]=T[i][0]
        Y[i]=T[i][1]

    Poly=[0]*(N+1); Poly[0]=1
    for x,y in zip(X,Y):
        tmp=[0]*(N+1)
        for i in range(N):
            tmp[i+1]=Poly[i]
        for i in range(N):
            tmp[i]=(tmp[i]-x*Poly[i])%P
        Poly=tmp

    res=[0]*N
    for i,(x,y) in enumerate(zip(X,Y)):
        if y==0:
            continue

        Q=1
        for j in range(N):
            if j!=i:
                Q=Q*(x-X[j])%P
        Q=pow(Q, -1, P)

        tmp=Poly.copy()

        for j in  range(N,0,-1):
            res[j-1]=(res[j-1]+(tmp[j]*Q)%P*y)%P
            tmp[j-1]=(tmp[j-1]+tmp[j]*x)%P
    return res

def Lagrange_Interpolation_Point_Arithmetic(a: int, b: int, Y: list[int], X: int, P: int) -> int:
    """ 法が P の下での Lagrange 補間を行い, x = X での値を返す. ただし, x_i = a i + b

    Args:
        a (int): x の値の傾き
        b (int): x の値の切片
        Y (list[int]): f(a * i + b) = Y[i] となる Y
        X (int): 求める X の値
        P (int): 剰余

    Returns:
        int: f(X) mod P

    Complexity:
        O(N + log P)
    """

    d = len(Y) - 1

    X %= P
    left = [1] * (d + 1)
    for i in range(d + 1):
        alpha = X - a * i + b
        if i > 0:
            left[i] = left[i - 1] * alpha % P
        else:
            left[i] = alpha % P

    right = [1] * (d + 1)
    for i in range(d, -1, -1):
        alpha = X - a * i + b
        if i < d:
            right[i] = right[i + 1] * alpha % P
        else:
            right[i] = alpha % P

    fact = 1
    for i in range(1, d + 1):
        fact = (fact * i) % P

    fact_inv = [1] * (d + 1)
    fact_inv[-1] = pow(fact, -1, P)
    for i in range(d - 1, -1, -1):
        fact_inv[i] = fact_inv[i + 1] * (i + 1) % P

    y = 0
    coef = pow(-a, -d, P)

    for i in range(d + 1):
        alpha = fact_inv[i] * fact_inv[d - i] % P
        if i == 0:
            eta = right[i + 1]
        elif i == d:
            eta = left[i - 1]
        else:
            eta = left[i - 1] * right[i + 1] % P

        beta = eta * alpha % P
        gamma = Y[i] * beta % P
        y += coef * gamma % P
        coef = -coef

    return y % P
