#約数のK乗和
def Divisor_Sigma(N, K=1):
    if N==1:
        return 1

    R=1
    p=2
    while p*p<=N:
        if N%p==0:
            e=0
            while N%p==0:
                N//=p
                e+=1

            if K:
                s=pow(p,K)
                R*=(pow(s,e+1)-1)//(s-1)
            else:
                R*=e+1
        p+=1

    if N>1:
        R*=pow(N,K)+1

    return R
