---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links:
    - https://judge.yosupo.jp/submission/31819
    - https://judge.yosupo.jp/submission/6131
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.13.3/x64/lib/python3.13/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.13.3/x64/lib/python3.13/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class Prime:\n    class Pseudo_Prime_Generator:\n        def __init__(self):\n\
    \            self.prime = 1\n            self.step = None\n\n        def __iter__(self):\n\
    \            return self\n\n        def __next__(self):\n            if self.step:\n\
    \                self.prime += self.step\n                self.step = 6 - self.step\n\
    \            elif self.prime == 1:\n                self.prime = 2\n         \
    \   elif self.prime == 2:\n                self.prime = 3\n            elif self.prime\
    \ == 3:\n                self.prime = 5\n                self.step = 2\n     \
    \       return self.prime\n\n    @staticmethod\n    def exponents(n, p):\n   \
    \     e = 0\n        while n % p == 0:\n            e += 1\n            n //=\
    \ p\n        return e, n\n\n    @classmethod\n    def prime_factorization(cls,\
    \ N):\n        if N == 0:\n            return [[0, 1]]\n\n        factors = []\n\
    \        if N < 0:\n            factors.append([-1, 1])\n            N = abs(N)\n\
    \n        for p in [2, 3]:\n            e, N = cls.exponents(N, p)\n         \
    \   if e:\n                factors.append([p, e])\n\n        offset = 6\n    \
    \    while offset * offset <= N:\n            p = offset - 1\n            e, N\
    \ = cls.exponents(N, p)\n            if e:\n                factors.append([p,\
    \ e])\n\n            q = offset + 1\n            e, N = cls.exponents(N, q)\n\
    \            if e:\n                factors.append([q, e])\n\n            offset\
    \ += 6\n\n        if N > 1:\n            factors.append([N, 1])\n\n        return\
    \ factors\n\n    @staticmethod\n    def is_prime(N: int) -> bool:\n        if\
    \ N <= 3:\n            return N >= 2\n        elif N == 5:\n            return\
    \ True\n        elif (N % 2 == 0) or (N % 3 == 0) or (N % 5 == 0):\n         \
    \   return False\n\n        p = 7\n        while p * p <= N:\n            judge\
    \ = (N % p == 0) or (N % (p + 4) == 0) or (N % (p + 6) == 0) or (N % (p + 10)\
    \ == 0)\n            judge |= (N % (p + 12) == 0) or (N % (p + 16) == 0) or (N\
    \ % (p + 22) == 0) or (N % (p + 24) == 0)\n\n            if judge:\n         \
    \       return False\n\n            p += 30\n        return True\n\n    @classmethod\n\
    \    def radical(cls, N):\n        rad = 1\n        for p, _ in cls.prime_factorization(N):\n\
    \            rad *= p\n        return rad\n\n    @classmethod\n    def next_prime(cls,\
    \ N, K):\n        if K > 0:\n            while K > 0:\n                N += 1\n\
    \                if cls.is_prime(N):\n                    K -= 1\n        else:\n\
    \            while K < 0:\n                N -= 1\n                if cls.is_prime(N):\n\
    \                    K += 1\n        return N\n\n    @classmethod\n    def prime_list(cls,\
    \ N: int) -> list[int]:\n        \"\"\" N \u4EE5\u4E0B\u306E\u7D20\u6570\u5168\
    \u3066\u3092\u6607\u9806\u306B\u5217\u6319\u3057\u305F\u30EA\u30B9\u30C8\u3092\
    \u751F\u6210\u3059\u308B.\n\n        Args:\n            N (int): \u4E0A\u9650\n\
    \n        Returns:\n            list[int]: \u7D20\u6570\u306E\u30EA\u30B9\u30C8\
    \n        \"\"\"\n        # N = 0, 1, 2 \u306E\u6642\u306F\u4F8B\u5916\u51E6\u7406\
    \n        if N == 0 or N == 1:\n            return []\n        elif N == 2:\n\
    \            return [2]\n\n        # N \u304C 4 \u4EE5\u4E0A\u306E\u5076\u6570\
    \u306A\u3089\u3070, N \u3092 (N - 1) \u306B\u7F6E\u304D\u63DB\u3048, N \u3092\u5947\
    \u6570\u3068\u3057\u3066\u3082\u554F\u984C\u306A\u3044.\n        if N % 2 == 0:\n\
    \            N -= 1\n\n        M = (N + 1) // 2\n\n        is_prime = [True] *\
    \ M # is_prime[k] := 2k+1 \u306F\u7D20\u6570\u304B?\n\n        # 9 \u4EE5\u4E0A\
    \u306E 3 \u306E\u500D\u6570\u3092\u6D88\u3059\n        for x in range(4, M, 3):\n\
    \            is_prime[x] = False\n\n        for p in cls.Pseudo_Prime_Generator():\n\
    \            if p <= 3:\n                continue\n            if p * p > N:\n\
    \                break\n\n            if not is_prime[(p - 1) >> 1]:\n       \
    \         continue\n\n            for j in range((p * p - 1) >> 1, M, p):\n  \
    \              is_prime[j] = False\n\n        primes = [(k << 1) | 1 for k in\
    \ range(M) if is_prime[k]]\n        primes[0] = 2\n\n        return primes\n\n\
    \    @classmethod\n    def interval_sieve_of_eratosthenes(cls, L: int, R: int)\
    \ -> list[bool]:\n        \"\"\" L \u4EE5\u4E0A R \u4EE5\u4E0B\u306E\u6574\u6570\
    \u306B\u5BFE\u3057\u3066, \u30A8\u30E9\u30C8\u30B9\u30C6\u30CD\u30B9\u306E\u7BE9\
    \u3092\u5B9F\u884C\u3057, \u7D20\u6570\u304B\u3069\u3046\u304B\u306E\u30EA\u30B9\
    \u30C8\u3092\u4F5C\u6210\u3059\u308B.\n\n        Args:\n            L (int): \u4E0B\
    \u9650\n            R (int): \u4E0A\u9650\n\n        Returns:\n            list[bool]:\
    \ \u7B2C k \u9805\u76EE\u306F (k + L) \u304C\u7D20\u6570\u306A\u3089\u3070 True,\
    \ \u7D20\u6570\u3067\u306A\u3051\u308C\u3070 False\n        \"\"\"\n\n\n     \
    \   M = 1\n        while (M + 1) * (M + 1) <= R:\n            M += 1\n\n     \
    \   X = [True] * (R - L + 1)\n\n        # 0 \u3068 1 \u306E\u4F8B\u5916\n    \
    \    if L <= 0 <= R:\n            X[0 - L] = False\n        if L <= 1 <= R:\n\
    \            X[1 - L] = False\n\n        for p in cls.prime_list(M):\n       \
    \     lower = max((L + p - 1) // p * p, p * p)\n            for x in range(lower,\
    \ R + 1, p):\n                X[x - L] = False\n        return X\n\n    @classmethod\n\
    \    def interval_prime_factorization(cls, L: int, R: int) -> list[tuple[int]]:\n\
    \        \"\"\" L \u4EE5\u4E0A R \u4EE5\u4E0B\u306E\u5168\u3066\u306E\u6574\u6570\
    \u306B\u5BFE\u3057\u3066, \u7D20\u56E0\u6570\u5206\u89E3\u3092\u884C\u3046.\n\n\
    \        Args:\n            L (int): \u4E0B\u9650\n            R (int): \u4E0A\
    \u9650\n\n        Returns:\n            list[tuple[int]]: \u7B2C x \u9805\u304C\
    \ [(p1, e1), (p2, e2), ...] \u3067\u3042\u308B\u3068\u304D, x = p1^e1 * p2^e2\
    \ * ... \u304C\u7D20\u56E0\u6570\u5206\u89E3\u306B\u306A\u308B\n        \"\"\"\
    \n\n        assert 0 <= L <= R\n\n        M = 1\n        while (M + 1) * (M +\
    \ 1) <= R:\n            M += 1\n\n        if L == 0:\n            zero_include_flag\
    \ = 1\n            L = 1\n        else:\n            zero_include_flag = 0\n\n\
    \        A = list(range(L, R + 1))\n        X = [[] for _ in range(R-L+1)]\n\n\
    \        for p in cls.prime_list(M):\n            lower = (L + p - 1) // p * p\n\
    \            for x in range(lower, R + 1, p):\n                e = 0\n       \
    \         while A[x - L] % p == 0:\n                    A[x - L] //= p\n     \
    \               e += 1\n                X[x - L].append((p, e))\n\n        for\
    \ x in range(L, R + 1):\n            if A[x - L] != 1:\n                X[x -\
    \ L].append((A[x - L], 1))\n\n        if zero_include_flag:\n            return\
    \ [(0, 1)] + X\n        else:\n            return  X\n\n#\u7D20\u6570\u5224\u5B9A\
    \ for long long\ndef Is_Prime_for_long_long(N):\n    if N<=1: return False\n \
    \   if N==2 or N==7 or N==61: return True\n    if N%2==0: return False\n\n   \
    \ d=N-1\n    while d%2==0: d//=2\n\n    for a in (2,7,61):\n        t=d\n    \
    \    y=pow(a,t,N)\n        while t!=N-1 and y!=1 and y!=N-1:\n            y=(y*y)%N\n\
    \            t<<=1\n        if y!=N-1 and t%2==0:\n            return False\n\
    \    return True\n\n#Miller-Rabin\u306E\u7D20\u6570\u5224\u5B9A\u6CD5\ndef Miller_Rabin_Primality_Test(N,\
    \ Times=20):\n    \"\"\" Miller-Rabin \u306B\u3088\u308B\u6574\u6570 N \u306E\u7D20\
    \u6570\u5224\u5B9A\u3092\u884C\u3046.\n\n    N: \u6574\u6570\n    \u203B True\
    \ \u306F\u6B63\u78BA\u306B\u306F Probably True \u3067\u3042\u308B ( False \u306F\
    \ \u78BA\u5B9A False ).\n    \"\"\"\n    from random import randint as ri\n\n\
    \    if N==2: return True\n\n    if N==1 or N%2==0: return False\n\n    q=N-1\n\
    \    k=0\n    while q&1==0:\n        k+=1\n        q>>=1\n\n    for _ in range(Times):\n\
    \        m=ri(2,N-1)\n        y=pow(m,q,N)\n        if y==1:\n            continue\n\
    \n        flag=True\n        for i in range(k):\n            if (y+1)%N==0:\n\
    \                flag=False\n                break\n\n            y*=y\n     \
    \       y%=N\n\n        if flag:\n            return False\n    return True\n\n\
    #\u30DD\u30E9\u30FC\u30C9\u30FB\u30ED\u30FC\u30A2\u30EB\u30B4\u30EA\u30BA\u30E0\
    \u306B\u3088\u3063\u3066\u7D20\u56E0\u6570\u3092\u767A\u898B\u3059\u308B\n#\u53C2\
    \u8003\u5143:https://judge.yosupo.jp/submission/6131\ndef Find_Factor_Rho(N):\n\
    \    if N==1:\n        return 1\n    from math import gcd\n    m=1<<(N.bit_length()//8+1)\n\
    \n    for c in range(1,99):\n        f=lambda x:(x*x+c)%N\n        y,r,q,g=2,1,1,1\n\
    \        while g==1:\n            x=y\n            for i in range(r):\n      \
    \          y=f(y)\n            k=0\n            while k<r and g==1:\n        \
    \        for i in range(min(m, r - k)):\n                    y=f(y)\n        \
    \            q=q*abs(x - y)%N\n                g=gcd(q,N)\n                k+=m\n\
    \            r <<=1\n\n        if g<N:\n            if Miller_Rabin_Primality_Test(g):\n\
    \                return g\n            elif Miller_Rabin_Primality_Test(N//g):\n\
    \                return N//g\n    return N\n\n#\u30DD\u30E9\u30FC\u30C9\u30FB\u30ED\
    \u30FC\u30A2\u30EB\u30B4\u30EA\u30BA\u30E0\u306B\u3088\u308B\u7D20\u56E0\u6570\
    \u5206\u89E3\n#\u53C2\u8003\u5143:https://judge.yosupo.jp/submission/6131\ndef\
    \ Pollard_Rho_Prime_Factorization(N):\n    I=2\n    res=[]\n    while I*I<=N:\n\
    \        if N%I==0:\n            k=0\n            while N%I==0:\n            \
    \    k+=1\n                N//=I\n            res.append([I,k])\n\n        I+=1+(I%2)\n\
    \n        if I!=101 or N<2**20:\n            continue\n\n        while N>1:\n\
    \            if Miller_Rabin_Primality_Test(N):\n                res.append([N,1])\n\
    \                N=1\n            else:\n                j=Find_Factor_Rho(N)\n\
    \                k=0\n                while N%j==0:\n                    N//=j\n\
    \                    k+=1\n                res.append([j,k])\n    if N>1:\n  \
    \      res.append([N,1])\n    res.sort(key=lambda x:x[0])\n    return res\n\n\
    class Sieve_of_Eratosthenes:\n    @staticmethod\n    def list(N: int):\n     \
    \   \"\"\" N \u4EE5\u4E0B\u306E\u975E\u8CA0\u6574\u6570\u306B\u5BFE\u3059\u308B\
    \ Eratosthenes \u306E\u7BE9\u3092\u5B9F\u884C\u3059\u308B.\n\n        Args:\n\
    \            N (int): \u4E0A\u9650\n\n        Returns:\n            list[int]:\
    \ \u7B2C k \u9805\u306B\u3064\u3044\u3066, k \u304C\u7D20\u6570\u306A\u3089\u3070\
    , \u7B2C k \u9805\u304C 1, k \u304C\u7D20\u6570\u3067\u306A\u3044\u306A\u3089\u3070\
    , \u7B2C k \u9805\u304C 0 \u3067\u3042\u308B\u5217.\n        \"\"\"\n\n      \
    \  if N == 0:\n            return [0]\n\n        sieve = [1] * (N + 1)\n     \
    \   sieve[0] = sieve[1] = 0\n\n        for x in range(2 * 2, N + 1, 2):\n    \
    \        sieve[x] = 0\n\n        for x in range(3 * 3, N + 1, 6):\n          \
    \  sieve[x] = 0\n\n        p = 5\n        parity = 0\n        while p * p <= N:\n\
    \            if sieve[p]:\n                pointer = p * p\n                while\
    \ pointer <= N:\n                    sieve[pointer] = 0\n                    pointer\
    \ += 2 * p\n\n            p += 4 if parity else 2\n            parity ^= 1\n \
    \       return sieve\n\n    @staticmethod\n    def smallest_prime_factor(N: int):\n\
    \        \"\"\" 0, 1, ..., N \u306B\u3064\u3044\u3066\u6700\u5C0F\u306E\u7D20\u56E0\
    \u6570\u306E\u30EA\u30B9\u30C8\u3092\u6C42\u3081\u308B\n\n        Args:\n    \
    \        N (int): \u4E0A\u9650\n\n        Returns:\n            list[int]: \u7B2C\
    \ k \u9805\u306F k \u306E\u6700\u5C0F\u306E\u7D20\u56E0\u6570\u3067\u3042\u308B\
    \u30EA\u30B9\u30C8 (k = 0, 1 \u306E\u5834\u5408\u306F 1 \u3068\u3059\u308B)\n\
    \        \"\"\"\n\n        if N <= 1:\n            return [1] * (N + 1)\n\n  \
    \      # spf: smallest prime factor\n        spf = [0] * (N + 1); spf[0] = spf[1]\
    \ = 1\n\n        for x in range(2, N + 1, 2):\n            spf[x] = 2\n\n    \
    \    for x in range(3, N + 1, 6):\n            spf[x] = 3\n\n        primes =\
    \ [2, 3]\n        parity = 0\n        x = 5\n        while x <= N:\n         \
    \   if spf[x] == 0:\n                spf[x] = x\n                primes.append(x)\n\
    \n            for p in primes:\n                if x * p <= N:\n             \
    \       spf[x * p] = p\n                else:\n                    break\n\n \
    \               if p == spf[x]:\n                    break\n\n            x +=\
    \ 4 if parity else 2\n            parity ^= 1\n\n        return spf\n\n    @staticmethod\n\
    \    def faster_prime_factorization(N: int, spf: list) -> list:\n        \"\"\"\
    \ smallest_prime_factor \u3067\u6C42\u3081\u305F\u6700\u5C0F\u306E\u7D20\u56E0\
    \u6570\u30EA\u30B9\u30C8\u3092\u5229\u7528\u3057\u3066, N \u3092\u9AD8\u901F\u3067\
    \u7D20\u56E0\u6570\u5206\u89E3\u3059\u308B.\n\n        Args:\n            N (int):\
    \ \u7D20\u56E0\u6570\u5206\u89E3\u306E\u5BFE\u8C61\n            spf (list[int]):\
    \ smallest_prime_factor \u3067\u6C42\u3081\u305F\u6700\u5C0F\u306E\u7D20\u56E0\
    \u6570\u30EA\u30B9\u30C8\n\n        Returns:\n            list[list[int]]: \u7D20\
    \u56E0\u6570\u5206\u89E3\u306E\u7D50\u679C\n        \"\"\"\n\n        if N ==\
    \ 0:\n            return [[0, 1]]\n\n        factors = []\n        if N < 0:\n\
    \            factors.append([-1, 1])\n            N = abs(N)\n\n        while\
    \ N > 1:\n            p = spf[N]\n            e = 0\n            while spf[N]\
    \ == p:\n                e += 1\n                N //= p\n\n            factors.append([p,\
    \ e])\n\n        return factors\n\n#\u7D20\u6570\u306E\u500B\u6570\n#Thanks for\
    \ pyranine\n#URL: https://judge.yosupo.jp/submission/31819\ndef Prime_Pi(N):\n\
    \    \"\"\" N \u4EE5\u4E0B\u306E\u7D20\u6570\u306E\u500B\u6570\n\n    N: int\n\
    \    \"\"\"\n\n    if N<2: return 0\n    v = int(N ** 0.5) + 1\n    smalls = [i\
    \ // 2 for i in range(1, v + 1)]\n    smalls[1] = 0\n    s = v // 2\n    roughs\
    \ = [2 * i + 1 for i in range(s)]\n    larges = [(N // roughs[i] + 1) // 2 for\
    \ i in range(s)]\n    skip = [False] * v\n\n    pc = 0\n    for p in range(3,\
    \ v):\n        if smalls[p] <= smalls[p - 1]:\n            continue\n\n      \
    \  q = p * p\n        pc += 1\n        if q * q > N:\n            break\n    \
    \    skip[p] = True\n        for i in range(q, v, 2 * p):\n            skip[i]\
    \ = True\n\n        ns = 0\n        for k in range(s):\n            i = roughs[k]\n\
    \            if skip[i]:\n                continue\n            d = i * p\n  \
    \          larges[ns] = larges[k] - (larges[smalls[d] - pc] if d < v else smalls[N\
    \ // d]) + pc\n            roughs[ns] = i\n            ns += 1\n        s = ns\n\
    \        for j in range((v - 1) // p, p - 1, -1):\n            c = smalls[j] -\
    \ pc\n            e = min((j + 1) * p, v)\n            for i in range(j * p, e):\n\
    \                smalls[i] -= c\n\n    for k in range(1, s):\n        m = N //\
    \ roughs[k]\n        s = larges[k] - (pc + k - 1)\n        for l in range(1, k):\n\
    \            p = roughs[l]\n            if p * p > m:\n                break\n\
    \            s -= smalls[m // p] - (pc + l - 1)\n        larges[0] -= s\n\n  \
    \  return larges[0]\n\n#K\u4E57\u30EA\u30B9\u30C8\ndef Power_List(N: int, K: int,\
    \ M: int) -> list[int]:\n    \"\"\" x = 0, 1, ..., N \u306B\u5BFE\u3059\u308B\
    \ x^K mod M \u3092\u6C42\u3081\u308B.\n\n    \u8A08\u7B97\u91CF: O(N log log N\
    \ + (log K) pi(N))\n\n    Args:\n        N (int): \u5E95\u306E\u4E0A\u9650\n \
    \       K (int): \u6307\u6570\n        M (int): \u9664\u6570\n\n    Returns:\n\
    \        list[int]: \u7B2C x \u9805\u306F x^K mod M \u306E\u5024\u304C\u8A18\u9332\
    \u3055\u308C\u308B.\n    \"\"\"\n\n    if N == 0:\n        return [pow(0, K, M)]\n\
    \n    spf = Sieve_of_Eratosthenes.smallest_prime_factor(N)\n\n    A = [0] * (N\
    \ + 1)\n    A[0] = pow(0, K, M); A[1] = pow(1, K, M)\n\n    for x in range(2,\
    \ N + 1):\n        if spf[x] == x:\n            A[x] = pow(x, K, M)\n        else:\n\
    \            A[x] = A[spf[x]] * A[x // spf[x]] % M\n\n    return A\n"
  dependsOn: []
  isVerificationFile: false
  path: Integer/Prime.py
  requiredBy: []
  timestamp: '2025-01-12 18:26:36+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Integer/Prime.py
layout: document
redirect_from:
- /library/Integer/Prime.py
- /library/Integer/Prime.py.html
title: Integer/Prime.py
---
