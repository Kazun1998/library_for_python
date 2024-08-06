class Prime:
    class Pseudo_Prime_Generator:
        def __init__(self):
            self.prime = 1
            self.step = None

        def __iter__(self):
            return self

        def __next__(self):
            if self.step:
                self.prime += self.step
                self.step = 6 - self.step
            elif self.prime == 1:
                self.prime = 2
            elif self.prime == 2:
                self.prime = 3
            elif self.prime == 3:
                self.prime = 5
                self.step = 2
            return self.prime

    @staticmethod
    def exponents(n, p):
        e = 0
        while n % p == 0:
            e += 1
            n //= p
        return e, n

    @classmethod
    def prime_factorization(cls, N):
        if N == 0:
            return [[0, 1]]

        factors = []
        if N < 0:
            factors.append([-1, 1])
            N = abs(N)

        for p in [2, 3]:
            e, N = cls.exponents(N, p)
            if e:
                factors.append([p, e])

        offset = 6
        while offset * offset <= N:
            p = offset - 1
            e, N = cls.exponents(N, p)
            if e:
                factors.append([p, e])

            q = offset + 1
            e, N = cls.exponents(N, q)
            if e:
                factors.append([q, e])

            offset += 6

        if N > 1:
            factors.append([N, 1])

        return factors

    @classmethod
    def is_prime(cls, N):
        N = abs(N)
        if N <= 1:
            return False

        if (N == 2) or (N == 3) or (N == 5) or (N == 7):
            return True

        if not (N % 6 == 1 or N % 6 == 5):
            return False

        offset = 0
        while offset * offset <= N:
            if (N % (offset + 5) == 0) or (N % (offset + 7) == 0):
                return False
            offset += 6
        return True

    @classmethod
    def radical(cls, N):
        rad = 1
        for p, _ in cls.prime_factorization(N):
            rad *= p
        return rad

    @classmethod
    def next_prime(cls, N, K):
        if K > 0:
            while K > 0:
                N += 1
                if cls.is_prime(N):
                    K -= 1
        else:
            while K < 0:
                N -= 1
                if cls.is_prime(N):
                    K += 1
        return N

#素数判定 for long long
def Is_Prime_for_long_long(N):
    if N<=1: return False
    if N==2 or N==7 or N==61: return True
    if N%2==0: return False

    d=N-1
    while d%2==0: d//=2

    for a in (2,7,61):
        t=d
        y=pow(a,t,N)
        while t!=N-1 and y!=1 and y!=N-1:
            y=(y*y)%N
            t<<=1
        if y!=N-1 and t%2==0:
            return False
    return True

#Miller-Rabinの素数判定法
def Miller_Rabin_Primality_Test(N, trial = 20):
    """ Miller-Rabin の方法によって, N が素数かどうかを判定する.

    Args:
        N (int): 正の整数
        trial (int, optional): N が素数であることを確認するために行う判定回数. Defaults to 20.

    Returns:
        bool: False は確定的 False, True は確率的 True
    """

    from random import randint as ri

    if N == 2:
        return True

    if N == 1 or N % 2 == 0:
        return False

    q = N - 1
    k = 0
    while q & 1 == 0:
        k += 1
        q >>= 1

    for _ in range(trial):
        m = ri(2, N - 1)
        y = pow(m, q, N)
        if y == 1:
            continue

        flag = True
        for _1 in range(k):
            if (y + 1) % N == 0:
                flag=False
                break

            y *= y
            y %= N

        if flag:
            return False

    return True

#ポラード・ローアルゴリズムによって素因数を発見する
#参考元:https://judge.yosupo.jp/submission/6131
def Find_Factor_Rho(N):
    if N==1:
        return 1
    from math import gcd
    m=1<<(N.bit_length()//8+1)

    for c in range(1,99):
        f=lambda x:(x*x+c)%N
        y,r,q,g=2,1,1,1
        while g==1:
            x=y
            for i in range(r):
                y=f(y)
            k=0
            while k<r and g==1:
                for i in range(min(m, r - k)):
                    y=f(y)
                    q=q*abs(x - y)%N
                g=gcd(q,N)
                k+=m
            r <<=1

        if g<N:
            if Miller_Rabin_Primality_Test(g):
                return g
            elif Miller_Rabin_Primality_Test(N//g):
                return N//g
    return N

#ポラード・ローアルゴリズムによる素因数分解
#参考元:https://judge.yosupo.jp/submission/6131
def Pollard_Rho_Prime_Factorization(N):
    I=2
    res=[]
    while I*I<=N:
        if N%I==0:
            k=0
            while N%I==0:
                k+=1
                N//=I
            res.append([I,k])

        I+=1+(I%2)

        if I!=101 or N<2**20:
            continue

        while N>1:
            if Miller_Rabin_Primality_Test(N):
                res.append([N,1])
                N=1
            else:
                j=Find_Factor_Rho(N)
                k=0
                while N%j==0:
                    N//=j
                    k+=1
                res.append([j,k])
    if N>1:
        res.append([N,1])
    res.sort(key=lambda x:x[0])
    return res

#エラトステネスの篩
def Sieve_of_Eratosthenes(N):
    """ N までのエラトステネスの篩を実行

    [Input]
    N:自然数

    [Output]
    素数かどうかのリスト ([0,0,1,1,0,1,...])
    """

    if N==0:
        return [0]

    T=[1]*(N+1)
    T[0]=T[1]=0

    for x in range(4,N+1,2):
        T[x]=0

    for x in range(9,N+1,3):
        T[x]=0

    a=5
    Flag=0
    while a*a<=N:
        if T[a]:
            b=a*a
            c=2*a
            while b<=N:
                T[b]=0
                b+=c
        a+=2+2*Flag
        Flag^=1
    return T

def Prime_List(N):
    """ N 以下の素数を列挙

    [Input]
    N: 自然数

    [Output]
    N 以下の素数を昇順に並べたリスト [2,3,5,...]
    """

    if N==0 or N==1:
        return []
    elif N==2:
        return [2]

    if N%2==0:
        N-=1

    M=(N+1)//2

    prime=[1]*M # prime[k]:=2k+1 は素数?

    for x in range(4,M,3):
        prime[x]=0

    a=5
    Flag=0
    while a*a<=N:
        if prime[(a-1)>>1]:
            ii=(a*a-1)>>1
            for j in range(ii,M,a):
                prime[j]=0
        a+=2+2*Flag
        Flag^=1

    X=[(k<<1)|1 for k in range(M) if prime[k]]
    X[0]=2

    return X

def Interval_Sieve_of_Eratosthenes(L,R):
    """ L 以上 R 以下のエラトステネスの篩を実行

    [Input]
    N:自然数

    [Output]
    素数かどうかのリスト X: X[k]:=k+L が素数なら 1, 素数でないならば 0
    """

    M=1
    while True:
        if (M+1)*(M+1)>R:
            break
        M+=1

    X=[1]*(R-L+1)

    if L<=0<=R:
        X[0-L]=0
    if L<=1<=R:
        X[1-L]=0

    for p in Prime_List(M):
        for x in range(max((L+p-1)//p*p,p*p),R+1,p):
            X[x-L]=0
    return X

def Smallest_Prime_Factor(N):
    """ 0,1,2,...,N の最小の素因数のリスト (0,1 については 1 にしている)
    """

    if N<=1:
        return [1]*(N+1)

    T=[0]*(N+1); T[0]=T[1]=1

    for i in range(2, N+1, 2):
        T[i]=2

    for i in range(3, N+1, 6):
        T[i]=3

    prime=[2,3]
    i=5; d=2
    while i<=N:
        if T[i]==0:
            T[i]=i
            prime.append(i)

        for p in prime:
            if i*p<=N:
                T[i*p]=p
            else:
                break
            if p==T[i]:
                break
        i+=d; d=6-d
    return T

def Faster_Prime_Factorization(N,L):
    """ Smallest_Prime_Factors(N)で求めたリストを利用して, N を高速素因数分解する.

    L: Smallest_Prime_Factors(N)で求めたリスト
    """
    if N==0:
        return [[0,1]]
    elif N>0:
        D=[]
    else:
        D=[[-1,1]]
        N=abs(N)

    while N>1:
        a=L[N]
        k=0
        while L[N]==a:
            k+=1
            N//=a
        D.append([a,k])
    return D

def Interval_Prime_Factorization(L,R):
    """ x=L,L+1,...,R に対して素因数分解を行う.

    """

    assert 0<=L<=R

    M=1
    while True:
        if (M+1)*(M+1)>R:
            break
        M+=1

    if L==0:
        flag=1
        L=1
    else:
        flag=0

    A=list(range(L,R+1))
    X=[[] for _ in range(R-L+1)]

    for p in Prime_List(M):
        for x in range((L+p-1)//p*p,R+1,p):
            k=0
            while A[x-L]%p==0:
                A[x-L]//=p
                k+=1
            X[x-L].append((p,k))

    for x in range(L,R+1):
        if A[x-L]!=1:
            X[x-L].append((A[x-L],1))

    if flag:
        return [(0,1)]+X
    else:
        return  X

#素数の個数
#Thanks for pyranine
#URL: https://judge.yosupo.jp/submission/31819
def Prime_Pi(N):
    """ N 以下の素数の個数

    N: int
    """

    if N<2: return 0
    v = int(N ** 0.5) + 1
    smalls = [i // 2 for i in range(1, v + 1)]
    smalls[1] = 0
    s = v // 2
    roughs = [2 * i + 1 for i in range(s)]
    larges = [(N // roughs[i] + 1) // 2 for i in range(s)]
    skip = [False] * v

    pc = 0
    for p in range(3, v):
        if smalls[p] <= smalls[p - 1]:
            continue

        q = p * p
        pc += 1
        if q * q > N:
            break
        skip[p] = True
        for i in range(q, v, 2 * p):
            skip[i] = True

        ns = 0
        for k in range(s):
            i = roughs[k]
            if skip[i]:
                continue
            d = i * p
            larges[ns] = larges[k] - (larges[smalls[d] - pc] if d < v else smalls[N // d]) + pc
            roughs[ns] = i
            ns += 1
        s = ns
        for j in range((v - 1) // p, p - 1, -1):
            c = smalls[j] - pc
            e = min((j + 1) * p, v)
            for i in range(j * p, e):
                smalls[i] -= c

    for k in range(1, s):
        m = N // roughs[k]
        s = larges[k] - (pc + k - 1)
        for l in range(1, k):
            p = roughs[l]
            if p * p > m:
                break
            s -= smalls[m // p] - (pc + l - 1)
        larges[0] -= s

    return larges[0]

#K乗リスト
def Power_List(N,K,Mod):
    """ i=0,1,...,N における i^K (mod Mod) のリストを求める.
    [計算量] O(N log log N+pi(N) log K)
    N,K,Mod: int
    """

    if N==0:
        return [0]

    S=Smallest_Prime_Factor(N)
    A=[0]*(N+1); A[1]=pow(1,K,Mod)

    for i in range(2,N+1):
        if S[i]<i:
            A[i]=A[S[i]]*A[i//S[i]]%Mod
        else:
            A[i]=pow(i,K,Mod)
    return A
