#素因数分解
def Prime_Factorization(N):
    if N==0:
        return [[0,1]]

    if N<0:
        R=[[-1,1]]
    else:
        R=[]

    N=abs(N)

    if N&1==0:
        C=0
        while N&1==0:
            N>>=1
            C+=1
        R.append([2,C])

    if N%3==0:
        C=0
        while N%3==0:
            N//=3
            C+=1
        R.append([3,C])

    k=5
    Flag=0
    while k*k<=N:
        if N%k==0:
            C=0
            while N%k==0:
                C+=1
                N//=k
            R.append([k,C])
        k+=2+2*Flag
        Flag^=1

    if N!=1:
        R.append([N,1])

    return R

#根基
def Radical(N):
    """Nが素因数分解 N=p^a*q^b*r^c ...となるとき, pqr...を返す.

    N:非負整数
    """

    assert N>=0,"Nは非負整数ではない."
    a=1

    if N&1==0:
        a*=2
        while N&1==0:
            N>>=1

    if N%3==0:
        a*=3
        while N%3==0:
            N//=3

    k=5
    Flag=0
    while k*k<=N:
        if N%k==0:
            a*=k
            while N%k==0:
                N//=k
        k+=2+2*Flag
        Flag^=1

    if N>1:
        a*=N
    return a

#素因数の種類
def Prime_Factor_List(N):
    """Nが素因数分解 N=p^a*q^b*r^c ...となるとき,リスト[p,q,r,...]を返す.
    """
    N=abs(N)
    X=[]
    if N%2==0:
        X.append(2)
        while N&1==0:
            N>>=1

    if N%3==0:
        X.append(3)
        while N%3==0:
            N//=3

    p=5
    Flag=1
    while p*p<=N:
        if N%p==0:
            X.append(p)
            while N%p==0:
                N//=p
        p+=2 if Flag else 4
        Flag^=1

    if N!=1:
        X.append(N)
    return X

#約数全部
def Divisors(N):
    N=abs(N)
    L,U=[],[]
    k=1
    while k*k <=N:
        if N%k== 0:
            L.append(k)
            if k*k!=N:
                U.append(N//k)
        k+=1
    return L+U[::-1]

#素因数分解の結果から, 約数を全て求める.
def Divisors_from_Prime_Factor(P,sorting=False):
    X=[1]
    for p,e in P:
        q=1
        n=len(X)
        for _ in range(e):
            q*=p
            for j in range(n):
                X.append(X[j]*q)

    if sorting:
        X.sort()

    return X

#高度合成数
#参考元:https://qiita.com/convexineq/items/e3d599cb9f91a73f936d
def Highly_Composite_Number(N):
    """N以下の高度合成数を求める.
    """

    from heapq import heappop,heappush
    from math import log
    prime = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263]
    lim = [[2*int(log(p,q)) for q in prime] for p in prime] #枝刈り用配列
    # 初期状態
    q = [(2,2,[1])] # (n,nの約数の個数、nの指数表記)を保存する heapq
    res = [(1,1,[])]

    while q and q[0][0] <= N:
        n,val,lst = heappop(q)
        if val > res[-1][1]: #条件をみたすなら答に追加
            res.append((n,val,lst[:]))
        L = len(lst)
        e0 = lst[0]
        #全部１なら新しい素数で横に伸ばせる
        if e0 == 1:
            heappush(q,(n*prime[L],val*2,[1]*(L+1)))
        #最上段の上を横方向に積む
        for i in range(L):
            if e0 > lst[i]: break #段差があると、もう伸ばせない
            if e0 >= lim[L][i]: break #枝刈り（重要）
            n *= prime[i]
            if n <= N:
                lst[i] += 1
                val = val//(e0+1)*(e0+2)
                heappush(q,(n,val,lst[:]))
    return res

#素数判定
def Is_Prime(N):
    N=abs(N)
    if N<=1: return False

    if (N==2) or (N==3) or (N==5): return True

    r=N%6
    if not(r==1 or r==5): return False

    k=5
    Flag=0
    while k*k<=N:
        if N%k==0: return False

        k+=2+2*Flag
        Flag^=1
    return True

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
def Miller_Rabin_Primality_Test(N,Times=20):
    """ Miller-Rabin による整数 N の素数判定を行う.

    N: 整数
    ※ True は正確には Probably True である ( False は 確定 False ).
    """
    from random import randint as ri

    if N==2: return True

    if N==1 or N%2==0: return False

    q=N-1
    k=0
    while q&1==0:
        k+=1
        q>>=1

    for _ in range(Times):
        m=ri(2,N-1)
        y=pow(m,q,N)
        if y==1:
            continue

        flag=True
        for i in range(k):
            if (y+1)%N==0:
                flag=False
                break

            y*=y
            y%=N

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

#次の素数
def Next_Prime(N,K=1):
    """
    Nを上回る自然数のうち,K番目に小さい素数

    N:自然数
    """
    if K>0:
        while K>0:
            N+=1
            if Is_Prime(N):
                K-=1
    else:
        while K<0:
            N-=1
            if Is_Prime(N):
                K+=1
    return N

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

    for x in range(4,N+1,2): T[x]=0
    for x in range(9,N+1,3): T[x]=0

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
    素数かどうかのリスト ([0,0,1,1,0,1,...])
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

    if N==0:
        return [1]

    N=abs(N)
    L=list(range(N+1))
    L[0]=L[1]=1

    x=4
    while x<=N:
        L[x]=2
        x+=2

    x=9
    while x<=N:
        if L[x]==x:
            L[x]=3
        x+=6

    x=5
    Flag=0
    while x*x<=N:
        if L[x]==x:
            y=x*x
            while y<=N:
                if L[y]==y:
                    L[y]=x
                y+=x<<1
        x+=2+2*Flag
        Flag^=1

    return L

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

#Euler's Totient関数
def Euler_Totient(N):
    """1以上N以下の整数のうち, Nと互いに素な整数の個数 φ(N) を求める.

    N:正の整数
    """

    assert N>=0,"Nが非負整数ではない."

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
def Euler_Totient_List(N):
    """k=0,1,...,N に対して, 1以上k以下の整数のうち, kと互いに素な整数の個数 φ(k) を求める.

    N:正の整数
    """

    assert N>=0,"Nが非負整数ではない."

    phi=list(range(N+1))
    for p in range(2,N+1):
        if phi[p]==p:
            for j in range(p,N+1,p):
                phi[j]=phi[j]//p*(p-1)
    return phi

#約数のK乗和
def Divisor_Sigma(N,K=1):
    if N==1:
        return 1

    H=Prime_Factorization(N)

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

#完全数?
def Is_Perfect(N):
    return 2*N==Divisor_Sigma(N,1)

#商列挙
def Quotient_Range(N):
    """Nで割った商の可能性を全て列挙する.

    [Input]
    N:正整数

    [Output]
    X:リスト
    Xの各要素(k,x,y) は x<=i<=y であることと, floor(N/i)=k が同値であることを表す.
    """
    X=[]

    M=1
    while M*M<=N:
        X.append((N//M,M,M))
        M+=1

    for i in range(M,0,-1):
        L=N//(i+1)+1
        R=N//i

        if L<=R and X[-1][-1]<L:
            X.append((N//L,L,R))
    return X

def Reminder_Enumeration(N,r):
    """ N を q 割った余りが r になる q を全て列挙する.

    N: 正整数
    r: 非負整数, N!=r
    """

    assert N!=r,"無限個あります."

    k=1
    X=[];Y=[]
    N-=r
    while k*k<=N:
        if N%k==0:
            if k>r:
                X.append(k)
            if k*k!=N and N//k>r:
                Y.append(N//k)
        k+=1
    return X+Y[::-1]

#法pの原始根
def Primitive_Root(p):
    """Z/pZ上の原始根を見つける

    p:素数
    """
    if p==2:
        return 1
    if p==998244353:
        return 3
    if p==10**9+7:
        return 5

    fac=[]
    q=2
    v=p-1

    while v>=q*q:
        e=0
        while v%q==0:
            e+=1
            v//=q

        if e>0:
            fac.append(q)
        q+=1

    if v>1:
        fac.append(v)

    g=2
    while g<p:
        if pow(g,p-1,p)!=1:
            return None

        flag=True
        for q in fac:
            if pow(g,(p-1)//q,p)==1:
                flag=False
                break

        if flag:
            return g

        g+=1

#最大公約数
def gcd(m,n):
    m=abs(m)
    n=abs(n)

    while n:
        m,n=n,m%n
    return m

def GCD(*X):
    from functools import reduce
    return reduce(gcd,X)

#拡張ユークリッドの互除法
def Extend_Euclid(a:int,b:int):
    """gcd(a,b) と ax+by=gcd(a,b) を満たす整数 x,y の例を挙げる.

    a,b:整数
    """
    s,t,u,v=1,0,0,1
    while b:
        q,a,b=a//b,b,a%b
        s,t=t,s-q*t
        u,v=v,u-q*v
    return s,u,a

#最小公倍数
def lcm(m,n):
    return (m//gcd(m,n))*n

def LCM(*X):
    from functools import reduce
    return reduce(lcm,X)

#floor(a^(1/k)) を求める.
def Floor_Root(a,k):
    """floor(a^(1/k)) を求める.

    a:非負整数
    k:正の整数
    """
    assert 0<=a and 0<k
    if a==0: return 0
    if k==1: return a

    #大体の値を求める.
    x=int(pow(a,1/k))

    #増やす
    while pow(x+1,k)<=a:
        x+=1

    #減らす
    while pow(x,k)>a:
        x-=1
    return x

#ceil(a^(1/k)) を求める.
def Ceil_Root(a,k):
    """ceil(a^(1/k)) を求める.

    a:非負整数
    k:正の整数
    """
    assert 0<=a and 0<k
    if a==0:
        return 0
    if k==1:
        return a

    #大体の値を求める.
    x=int(pow(a,1/k))+1

    #増やす
    while pow(x,k)<a:
        x+=1

    #減らす
    while a<=pow(x-1,k):
        x-=1
    return x

def kth_Power(a,k):
    """ 整数 a が k 乗数かどうかを求め, そうならば, b^k=a を満たす k を返す.

    [Input]
    a: int
    k: int (k>0)

    [Output]
    存在しない  : None
    存在する    : b^k=a を満たす b
    """

    b=Floor_Root(a,k)
    if pow(b,k)==a:
        return b
    else:
        return None
