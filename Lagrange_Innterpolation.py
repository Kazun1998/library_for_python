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

    Fact_inv=[1]*(d+1); Fact_inv[-1]=pow(fact,P-2,P)
    for i in range(d-1,-1,-1):
        Fact_inv[i]=(Fact_inv[i+1]*(i+1))%P

    Y=0
    coef=pow(-a,d*(P-2),P)
    for i in range(d+1):
        V_inv=Fact_inv[i]*Fact_inv[d-i]
        if i==0:
            S=(Right[i+1]*V_inv)%P
        elif i==d:
            S=(Left[i-1]*V_inv)%P
        else:
            u=(Left[i-1]*Right[i+1])%P
            S=(u*V_inv)%P

        Y=(Y+coef*L[i]*S)%P
        coef=-coef
    return Y