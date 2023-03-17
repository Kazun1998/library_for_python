#Euler's Totient関数
def Euler_Totient(N, mode=True):
    """ 1 以上 N 以下の整数のうち, N と互いに素な整数の個数 phi (N) を求める.

    Args:
        N (int): 正の整数
        mode: False にすると, N "以下" が N "未満" になる (phi(1) が True だと 1, False だと 0 になるだけの違いである) 

    Returns:
        int: varphi (N)
    """

    assert N>=0,"Nが非負整数ではない."

    if N==1:
        return 1 if mode else 0

    e=(N&(-N)).bit_length()-1
    if e>0:
        phi=1<<(e-1)
        N>>=e
    else:
        phi=1

    e=0
    while N%3==0:
        e+=1
        N//=3

    if e>0:
        phi*=pow(3,e-1)*2

    flag=0
    p=5
    while p*p<=N:
        if N%p==0:
            e=0
            while N%p==0:
                e+=1
                N//=p

            phi*=pow(p,e-1)*(p-1)

        p+=2
        flag^=1

    if N>1:
        phi*=N-1

    return phi

#Euler's Totient関数
def Euler_Totient_List(N, mode=True):
    """k=0,1,...,N に対して, 1以上k以下の整数のうち, kと互いに素な整数の個数 φ(k) を求める.

    N:正の整数
    mode: False にすると, N "以下" が N "未満" になる (phi(1) が True だと 1, False だと 0 になるだけの違いである) 
    """

    assert N>=0,"Nが非負整数ではない."

    phi=list(range(N+1))
    for p in range(2,N+1):
        if phi[p]==p:
            for j in range(p,N+1,p):
                phi[j]=phi[j]//p*(p-1)

    if not mode and N>=1:
        phi[1]=0

    return phi
