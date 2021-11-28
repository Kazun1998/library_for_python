def Integer_Partition(N,M):
    """ 各項が M 以下の N の分割を求める. """

    Q=[[k] for k in range(1,M+1)]
    X=[]

    while Q:
        x=Q.pop()
        alpha=sum(x)

        if alpha==N:
            X.append(x)
            continue

        for k in range(1, min(M, N-alpha, x[-1])+1):
            Q.append(x+[k])

    return X

def Integer_Partition_yielder(N,M):
    """ 各項が M 以下の N の分割を求める. (yielder)"""

    Q=[[k] for k in range(1,M+1)]

    while Q:
        x=Q.pop()
        alpha=sum(x)

        if alpha==N:
            yield x
            continue

        for k in range(1, min(M, N-alpha, x[-1])+1):
            Q.append(x+[k])

from math import gcd
def lcm(A):
    x=1
    for a in A:
        x*=a//gcd(a,x)
    return x

