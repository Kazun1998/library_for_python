#平方数?
def Is_Square_Number(N):
    if N<0:
        return False
    elif N==0:
        return True

    for p in [2,3]:
        F=0
        while N%p==0:
            F^=1
            N//=p
        if F:
            return False

    k=5
    Flag=1
    while k*k<=N:
        F=0
        while N%k==0:
            F^=1
            N//=k
        if F:
            return False
        k+=2 if Flag else 4
    return N==1

#立方数?
def Is_Cubic_Number(N):
    if N<0:
        return False
    elif N==0:
        return True

    for p in [2,3]:
        F=0
        while N%p==0:
            F+=1
            N//=p
        if F%3:
            return False

    k=5
    Flag=1
    while k*k<=N:
        F=0
        while N%k==0:
            F+=1
            N//=k
        if F%3:
            return False
        k+=2 if Flag else 4
    return N==1

#完全数?
def Is_Perfect(N):
    n=N
    S=1
    p=2
    while p*p<=n:
        if n%p==0:
            e=0
            while n%p==0:
                n//=p
                e+=1

            S*=(pow(p,e+1)-1)//(p-1)
        p+=1

    if n>1:
        S*=n+1

    return 2*N==S
