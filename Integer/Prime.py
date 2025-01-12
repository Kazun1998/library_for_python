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

    @staticmethod
    def is_prime(N: int) -> bool:
        if N <= 3:
            return N >= 2
        elif N == 5:
            return True
        elif (N % 2 == 0) or (N % 3 == 0) or (N % 5 == 0):
            return False

        p = 7
        while p * p <= N:
            judge = (N % p == 0) or (N % (p + 4) == 0) or (N % (p + 6) == 0) or (N % (p + 10) == 0)
            judge |= (N % (p + 12) == 0) or (N % (p + 16) == 0) or (N % (p + 22) == 0) or (N % (p + 24) == 0)

            if judge:
                return False

            p += 30
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

    @classmethod
    def prime_list(cls, N: int) -> list[int]:
        """ N 以下の素数全てを昇順に列挙したリストを生成する.

        Args:
            N (int): 上限

        Returns:
            list[int]: 素数のリスト
        """
        # N = 0, 1, 2 の時は例外処理
        if N == 0 or N == 1:
            return []
        elif N == 2:
            return [2]

        # N が 4 以上の偶数ならば, N を (N - 1) に置き換え, N を奇数としても問題ない.
        if N % 2 == 0:
            N -= 1

        M = (N + 1) // 2

        is_prime = [True] * M # is_prime[k] := 2k+1 は素数か?

        # 9 以上の 3 の倍数を消す
        for x in range(4, M, 3):
            is_prime[x] = False

        for p in cls.Pseudo_Prime_Generator():
            if p <= 3:
                continue
            if p * p > N:
                break

            if not is_prime[(p - 1) >> 1]:
                continue

            for j in range((p * p - 1) >> 1, M, p):
                is_prime[j] = False

        primes = [(k << 1) | 1 for k in range(M) if is_prime[k]]
        primes[0] = 2

        return primes

    @classmethod
    def interval_sieve_of_eratosthenes(cls, L: int, R: int) -> list[bool]:
        """ L 以上 R 以下の整数に対して, エラトステネスの篩を実行し, 素数かどうかのリストを作成する.

        Args:
            L (int): 下限
            R (int): 上限

        Returns:
            list[bool]: 第 k 項目は (k + L) が素数ならば True, 素数でなければ False
        """


        M = 1
        while (M + 1) * (M + 1) <= R:
            M += 1

        X = [True] * (R - L + 1)

        # 0 と 1 の例外
        if L <= 0 <= R:
            X[0 - L] = False
        if L <= 1 <= R:
            X[1 - L] = False

        for p in cls.prime_list(M):
            lower = max((L + p - 1) // p * p, p * p)
            for x in range(lower, R + 1, p):
                X[x - L] = False
        return X

    @classmethod
    def interval_prime_factorization(cls, L: int, R: int) -> list[tuple[int]]:
        """ L 以上 R 以下の全ての整数に対して, 素因数分解を行う.

        Args:
            L (int): 下限
            R (int): 上限

        Returns:
            list[tuple[int]]: 第 x 項が [(p1, e1), (p2, e2), ...] であるとき, x = p1^e1 * p2^e2 * ... が素因数分解になる
        """

        assert 0 <= L <= R

        M = 1
        while (M + 1) * (M + 1) <= R:
            M += 1

        if L == 0:
            zero_include_flag = 1
            L = 1
        else:
            zero_include_flag = 0

        A = list(range(L, R + 1))
        X = [[] for _ in range(R-L+1)]

        for p in cls.prime_list(M):
            lower = (L + p - 1) // p * p
            for x in range(lower, R + 1, p):
                e = 0
                while A[x - L] % p == 0:
                    A[x - L] //= p
                    e += 1
                X[x - L].append((p, e))

        for x in range(L, R + 1):
            if A[x - L] != 1:
                X[x - L].append((A[x - L], 1))

        if zero_include_flag:
            return [(0, 1)] + X
        else:
            return  X

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
def Miller_Rabin_Primality_Test(N, Times=20):
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

class Sieve_of_Eratosthenes:
    @staticmethod
    def list(N: int):
        """ N 以下の非負整数に対する Eratosthenes の篩を実行する.

        Args:
            N (int): 上限

        Returns:
            list[int]: 第 k 項について, k が素数ならば, 第 k 項が 1, k が素数でないならば, 第 k 項が 0 である列.
        """

        if N == 0:
            return [0]

        sieve = [1] * (N + 1)
        sieve[0] = sieve[1] = 0

        for x in range(2 * 2, N + 1, 2):
            sieve[x] = 0

        for x in range(3 * 3, N + 1, 6):
            sieve[x] = 0

        p = 5
        parity = 0
        while p * p <= N:
            if sieve[p]:
                pointer = p * p
                while pointer <= N:
                    sieve[pointer] = 0
                    pointer += 2 * p

            p += 4 if parity else 2
            parity ^= 1
        return sieve

    @staticmethod
    def smallest_prime_factor(N: int):
        """ 0, 1, ..., N について最小の素因数のリストを求める

        Args:
            N (int): 上限

        Returns:
            list[int]: 第 k 項は k の最小の素因数であるリスト (k = 0, 1 の場合は 1 とする)
        """

        if N <= 1:
            return [1] * (N + 1)

        # spf: smallest prime factor
        spf = [0] * (N + 1); spf[0] = spf[1] = 1

        for x in range(2, N + 1, 2):
            spf[x] = 2

        for x in range(3, N + 1, 6):
            spf[x] = 3

        primes = [2, 3]
        parity = 0
        x = 5
        while x <= N:
            if spf[x] == 0:
                spf[x] = x
                primes.append(x)

            for p in primes:
                if x * p <= N:
                    spf[x * p] = p
                else:
                    break

                if p == spf[x]:
                    break

            x += 4 if parity else 2
            parity ^= 1

        return spf

    @staticmethod
    def faster_prime_factorization(N: int, spf: list) -> list:
        """ smallest_prime_factor で求めた最小の素因数リストを利用して, N を高速で素因数分解する.

        Args:
            N (int): 素因数分解の対象
            spf (list[int]): smallest_prime_factor で求めた最小の素因数リスト

        Returns:
            list[list[int]]: 素因数分解の結果
        """

        if N == 0:
            return [[0, 1]]

        factors = []
        if N < 0:
            factors.append([-1, 1])
            N = abs(N)

        while N > 1:
            p = spf[N]
            e = 0
            while spf[N] == p:
                e += 1
                N //= p

            factors.append([p, e])

        return factors

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
def Power_List(N: int, K: int, M: int) -> list[int]:
    """ x = 0, 1, ..., N に対する x^K mod M を求める.

    計算量: O(N log log N + (log K) pi(N))

    Args:
        N (int): 底の上限
        K (int): 指数
        M (int): 除数

    Returns:
        list[int]: 第 x 項は x^K mod M の値が記録される.
    """

    if N == 0:
        return [0]

    spf = Sieve_of_Eratosthenes.smallest_prime_factor(N)

    A = [0] * (N + 1)
    A[1] = pow(1, K, M)

    for x in range(2, N + 1):
        if spf[x] == x:
            A[x] = pow(x, K, M)
        else:
            A[x] = A[spf[x]] * A[x // spf[x]] % M

    return A
