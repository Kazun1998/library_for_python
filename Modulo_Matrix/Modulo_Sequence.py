from Modulo_Matrix import *

#漸化式と行列
def Linear_Recurrence_Sequence_Value(p,x,N):
    """線形漸化式の第N項を求める.

    p:漸化式 (d=|p| とする.)
    x:第0項から第(d-1)項までの値
    N:第N項

    線形漸化式は x[n+d]=p[0]x[n]+p[1]x[n+1]+...+p[d-1]x[n+d-1] とする.
    """

    assert len(p)==len(x)
    d=len(p)

    if N<d:
        return x[N]

    A=[p[::-1]]
    for i in range(d-1):
        A.append([1 if j==i else 0 for j in range(d)])
    A=Modulo_Matrix(A)
    v=Modulo_Matrix([[y] for y in x])

    X=0
    aa=pow(A,N-d+1).ele[0][::-1]

    for i in range(d):
        X+=aa[i]*x[i]

    return X%Mod

def Linear_Recurrence_Sequence_Matrix(p):
    """線形漸化式から行列を作る.

    p:漸化式 (d=|p|)
    Mod:法

    線形漸化式は x[n+d]=p[0]x[0]+p[1]x[1]+...+p[d-1] x[d-1] とする.
    """

    A=[p[::-1]]
    d=len(p)
    for i in range(d-1):
        A.append([1 if j==i else 0 for j in range(d)])
    return Modulo_Matrix(A)
