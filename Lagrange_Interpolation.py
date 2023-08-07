def Lagrange_Interpolation_Point(L,X,P):
    """ 法が P の下でのLagrange 補間を行い, x=X での値を返す.

    [Input]
    L: [(x_0,y_0), ..., (x_N, y_N)]: F(x_i)=y_i (mod P)
    X: F(X) を返す.
    P: 法

    [Output]
    F(X)

    [Complexity]
    O(N^2+log P)
    """

    N=len(L)-1

    x=[p[0] for p in L]
    y=[p[1] for p in L]

    X%=P
    Y=0
    for i in range(N+1):
        a=b=1
        for j in range(N+1):
            if i==j: continue
            a*=X-x[j]; a%=P
            b*=x[i]-x[j]; b%=P
        c = (a * pow(b, -1 ,P)) % P
        Y+=y[i]*c; Y%=P
    return Y

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

def Lagrange_Interpolation_Point_Arithmetic(L,a,b,X,P):
    """ 法が P の下でのLagrange 補間を行い, x=X での値を返す. ただし, x_i=ai+b

    [Input]
    L: [y_0, ..., y_n]: F(x_i)=y_i (mod P)
    X: F(X) を返す.
    P: 法

    [Output]
    F(X)

    [Complexity]
    O(N+log P)
    """

    d=len(L)-1

    X%=P
    Left=[1]*(d+1)
    for i in range(d+1):
        if i:
            Left[i]=(Left[i-1]*(X-(a*i+b)))%P
        else:
            Left[i]=(X-(a*i+b))%P

    Right=[1]*(d+1)
    for i in range(d,-1,-1):
        if i<d:
            Right[i]=(Right[i+1]*(X-(a*i+b)))%P
        else:
            Right[i]=(X-(a*i+b))%P

    fact=1
    for i in range(1,d+1): fact=(fact*i)%P

    Fact_inv=[1]*(d+1); Fact_inv[-1]=pow(fact, -1, P)
    for i in range(d-1,-1,-1):
        Fact_inv[i]=(Fact_inv[i+1]*(i+1))%P

    Y=0
    coef=pow(-a, -d, P)

    for i in range(d+1):
        V_inv=(Fact_inv[i]*Fact_inv[d-i])%P
        if i==0:
            S=(Right[i+1]*V_inv)%P
        elif i==d:
            S=(Left[i-1]*V_inv)%P
        else:
            u=(Left[i-1]*Right[i+1])%P
            S=(u*V_inv)%P

        M=L[i]*S%P
        Y=(Y+coef*M)%P
        coef=-coef
    return Y
