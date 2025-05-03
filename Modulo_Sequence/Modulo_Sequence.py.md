---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.13.3/x64/lib/python3.13/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.13.3/x64/lib/python3.13/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from Modulo_Polynomial import *\n\ndef Nth_Term_of_Linearly_Recurrent_Sequence(A:\
    \ list[int], C: list[int], n: int, offset: int = 0) -> int:\n    \"\"\" A[i] =\
    \ C[0] * A[i - 1] + C[1] * A[i - 2] + ... + C[d - 1] * A[i - d] \u3067\u8868\u3055\
    \u308C\u308B\u6570\u5217 (A[i]) \u306E\u7B2C n \u9805\u3092\u6C42\u3081\u308B\
    .\n\n    Args:\n        A (list[int]): A = (A[0], ..., A[d - 1]): \u6700\u521D\
    \u306E d \u9805\n        C (list[int]): C = (C[0], ..., C[d - 1]): \u7DDA\u5F62\
    \u6F38\u5316\u5F0F\u306E\u4FC2\u6570\n        n (int): \u6C42\u3081\u308B\u9805\
    \u6570\n        offset (int, optional): \u305A\u3089\u3059\u9805\u6570 (\u521D\
    \u9805\u3092\u7B2C offset \u9805\u3068\u3059\u308B). Defaults to 0.\n\n    Raises:\n\
    \        ValueError: len(A) != len(C) \u306E\u5834\u5408\u306B\u767A\u751F\n\n\
    \    Returns:\n        int: A[n]\n    \"\"\"\n\n    if not len(A) == len(C):\n\
    \        raise ValueError(\"len(A) == len(C) \u3067\u306A\u304F\u3066\u306F\u306A\
    \u308A\u307E\u305B\u3093\")\n\n    d = len(A)\n    n -= offset\n\n    if n < 0:\n\
    \        return 0\n    elif n < d:\n        return A[n] % Mod\n\n    A = Modulo_Polynomial(A,\
    \ d + 1)\n    Q = Modulo_Polynomial([-C[i - 1] if i else 1  for i in range(d +\
    \ 1)], d + 1)\n\n    P = A * Q\n    P[d] = 0\n    return Polynominal_Coefficient(P,\
    \ Q, n)\n\ndef Find_Linear_Recurrence(A: list[int]) -> list[int]:\n    \"\"\"\
    \ \u6574\u6570\u5217 A \u304B\u3089\u63A8\u5B9A\u3055\u308C\u308B\u6700\u5C0F\u306E\
    \u9577\u3055\u306E\u7DDA\u5F62\u6F38\u5316\u5F0F\u3092\u6C42\u3081\u308B.\n\n\
    \    Args:\n        A (list[int]): A \u306E\u5148\u982D\n\n    Returns:\n    \
    \    list[int]: \u6574\u6570\u5217 A \u304B\u3089\u63A8\u5B9A\u3055\u308C\u308B\
    \u6700\u5C0F\u306E\u9577\u3055\u306E\u7DDA\u5F62\u6F38\u5316\u5F0F\u3067\u3042\
    \u308B. \u3064\u307E\u308A, \u4EE5\u4E0B\u3092\u6E80\u305F\u3059.\n          \
    \  A[i] = C[0] * A[i - 1] + C[1] * A[i - 2] + ... + C[d - 1] * A[i - d] (i >=\
    \ len(A))\n    \"\"\"\n\n    N = len(A)\n    B = [1]\n    C = [1]\n    l, m, p\
    \ = 0, 0, 1\n    for i in range(N):\n        m += 1\n        d = A[i]\n      \
    \  for j in range(1, l + 1):\n            d += C[j] * A[i-j]\n            d %=\
    \ Mod\n\n        if d == 0:\n            continue\n\n        T = C.copy()\n  \
    \      q = pow(p, -1, Mod) * d % Mod\n        C.extend([0] * (len(B) + m - len(C)))\n\
    \n        for j in range(len(B)):\n            C[j + m] -= q * B[j]\n        \
    \    C[j + m] %= Mod\n\n        if 2 * l <= i:\n            B = T\n          \
    \  l, m, p = i+1-l, 0, d\n\n    return [Mod - c if c else 0 for c in C[1:]]\n\n\
    def Fibonacci(n: int) -> int:\n    \"\"\" Fibonacci \u5217\u306E\u7B2C n \u9805\
    \u3092\u6C42\u3081\u308B.\n\n    Args:\n        n (int):\n\n    Returns:\n   \
    \     int: Fibonacci \u5217\u306E\u7B2C N \u9805\n    \"\"\"\n\n    return Nth_Term_of_Linearly_Recurrent_Sequence([0,\
    \ 1], [1, 1], n)\n\ndef Lucas(n: int) -> int:\n    \"\"\" Lucas \u5217\u306E\u7B2C\
    \ n \u9805\u3092\u6C42\u3081\u308B.\n\n    Args:\n        n (int):\n\n    Returns:\n\
    \        int: Lucas \u5217\u306E\u7B2C n \u9805\n    \"\"\"\n\n    return Nth_Term_of_Linearly_Recurrent_Sequence([2,\
    \ 1], [1, 1], n)\n\ndef Cumulative(A: list[int], n: int) -> int:\n    \"\"\" d\
    \ := len(A) \u3068\u3057\u3066, A[i + d] = A[i + d - 1] + ... + A[i] \u3067\u5B9A\
    \u7FA9\u3055\u308C\u308B A \u306B\u5BFE\u3057\u3066, A[n] \u3092\u6C42\u3081\u308B\
    .\n\n    Args:\n        A (list[int]): A \u306E\u5148\u982D\n        n (int):\n\
    \n    Returns:\n        int: A[n]\n    \"\"\"\n\n    return Nth_Term_of_Linearly_Recurrent_Sequence(A,\
    \ [1] * len(A), n)\n\ndef Factorial_Modulo(n: int) -> int:\n    \"\"\" n! \u3092\
    \ Mod \u3067\u5272\u3063\u305F\u4F59\u308A\u3092\u6C42\u3081\u308B.\n\n    Args:\n\
    \        n (int):\n\n    Returns:\n        int: n! \u3092 Mod \u3067\u5272\u3063\
    \u305F\u4F59\u308A\n    \"\"\"\n\n    if n == 0:\n        return 1\n    elif n\
    \ >= Mod:\n        return 0\n\n    n_sqrt = 0\n    while (n_sqrt + 1) * (n_sqrt\
    \ + 1) <= n:\n        n_sqrt += 1\n\n    A = Calc.multiple_convolution(*[[i, 1]\
    \ for i in range(1, n_sqrt + 1)])\n    H = Multipoint_Evaluation(Modulo_Polynomial(A,\
    \ n_sqrt + 1), [i * n_sqrt for i in range(n_sqrt)])\n\n    X = 1\n    for h in\
    \ H:\n        X = (h * X) % Mod\n\n    for i in range(n_sqrt * n_sqrt + 1, n_sqrt\
    \ + 1):\n        X = (i * X) % Mod\n    return X\n\n# \u7279\u5225\u306A\u6570\
    \u5217\ndef Bernoulli(N: int) -> list[int]:\n    \"\"\" Bernoulli \u6570 B[0],\
    \ B[1], ..., B[N + 1] \u3092\u6C42\u3081\u308B.\n\n    Args:\n        N (int):\n\
    \n    Returns:\n        list[int]: \u7B2C d \u9805\u304C B[d] \u306B\u5BFE\u5FDC\
    \u3059\u308B\u9577\u3055 (N L 1) \u306E\u30EA\u30B9\u30C8\n    \"\"\"\n\n    P\
    \ = Exp(Modulo_Polynomial([0, 1], N + 2))[1:]\n    f = P.inverse().poly[:-1]\n\
    \n    fact = 1\n    for i in range(1, N + 1):\n        fact = (fact * i) % Mod\n\
    \        f[i] = (f[i] * fact) % Mod\n\n    return f\n\ndef PartitionsP(n: int)\
    \ -> list[int]:\n    \"\"\" k = 0, 1,..., n \u306B\u5BFE\u3057\u3066, \u4EE5\u4E0B\
    \u3067\u5B9A\u7FA9\u3055\u308C\u308B\u5206\u5272\u6570 p(k) \u3092\u6C42\u3081\
    \u308B.\n        p(k) := k \u3092\u9806\u5E8F\u3092\u533A\u5225\u305B\u305A\u306B\
    \u81EA\u7136\u6570\u306E\u548C\u306B\u5206\u3051\u308B\u5834\u5408\u306E\u6570\
    \n\n    Args:\n        n (int):\n\n    Returns:\n        list[int]: \u7B2C k \u9805\
    \u304C p(k) \u306B\u5BFE\u5FDC\u3059\u308B\u9577\u3055 (n + 1) \u306E\u6574\u6570\
    \u306E\u30EA\u30B9\u30C8\n    \"\"\"\n\n    f = [0] * (n + 1)\n    f[0] = 1\n\
    \    k = 1\n    while k * (3 * k - 1) <= 2 *n:\n        m = -1 if k & 1 else 1\n\
    \        f[k * (3 * k - 1) // 2] += m\n\n        if k * (3 * k + 1) <= 2 *n:\n\
    \            f[k * (3 * k + 1) // 2 ]+= m\n        k += 1\n\n    return Calc.inverse(f)\n\
    \ndef PartitionsQ(n: int) -> list[int]:\n    \"\"\" k = 0, 1,..., n \u306B\u5BFE\
    \u3057\u3066, \u4EE5\u4E0B\u3067\u5B9A\u7FA9\u3055\u308C\u308B q(k) \u3092\u6C42\
    \u3081\u308B.\n        q(k) := k \u3092\u9806\u5E8F\u3092\u533A\u5225\u305B\u305A\
    \u306B, \u306A\u304A\u304B\u3064\u5168\u3066\u306E\u9805\u304C\u7570\u306A\u308B\
    \u81EA\u7136\u6570\u306E\u548C\u306B\u5206\u3051\u308B\u5834\u5408\u306E\u6570\
    \n\n    Args:\n        n (int):\n\n    Returns:\n        list[int]: \u7B2C k \u9805\
    \u304C q(k) \u306B\u5BFE\u5FDC\u3059\u308B\u9577\u3055 (n + 1) \u306E\u6574\u6570\
    \u306E\u30EA\u30B9\u30C8\n    \"\"\"\n\n    inv = [0] * (n+1)\n    inv[1] = 1\n\
    \    for x in range(2, n + 1):\n        q, r = divmod(Mod, x)\n        inv[x]\
    \ = (-q * inv[r]) % Mod\n\n    p = [0] * (n + 1)\n    for i in range(1, n + 1):\n\
    \        j = i\n        k = 1\n        c = 1\n        while j <= n:\n        \
    \    p[j] = (p[j] + c * inv[k]) % Mod\n            c *= -1\n            j += i\n\
    \            k += 1\n    P = Modulo_Polynomial(p, n + 1)\n    return Exp(P).poly\n\
    \ndef Stirling_1st(n: int) -> list[int]:\n    \"\"\" k = 0, 1, ..., n \u306B\u5BFE\
    \u3059\u308B\u7B2C I \u7A2E Stirling \u6570 S_{n, k} \u3092\u6C42\u3081\u308B\
    .\n\n    Args:\n        n (int):\n\n    Returns:\n        list[int]: \u9577\u3055\
    \u304C (n + 1) \u306E\u30EA\u30B9\u30C8. \u7B2C k \u9805\u304C S_{n, k} \u3092\
    \u8868\u3059.\n    \"\"\"\n\n    def g(n):\n        if n==0:\n            return\
    \ Modulo_Polynomial([1], n + 1)\n        elif n==1:\n            return Modulo_Polynomial([0,\
    \ 1], n + 1)\n        elif n % 2 == 1:\n            return Modulo_Polynomial([-n\
    \ + 1, 1], n + 1) * g(n - 1)\n        else:\n            P = g(n // 2)\n     \
    \       return P * Taylor_Shift(P, -n // 2)\n\n    return g(n).poly\n\ndef Stirling_2nd(n:\
    \ int) -> list[int]:\n    \"\"\" k = 0, 1, ..., n \u306B\u5BFE\u3059\u308B\u7B2C\
    \ II \u7A2E Stirling \u6570 S_{n, k} \u3092\u6C42\u3081\u308B.\n\n    Args:\n\
    \        n (int):\n\n    Returns:\n        list[int]: \u9577\u3055\u304C (n +\
    \ 1) \u306E\u30EA\u30B9\u30C8. \u7B2C k \u9805\u304C S_{n, k} \u3092\u8868\u3059\
    .\n    \"\"\"\n\n    fact = [0] * (n + 1); fact[0] = 1\n    for i in range(1,\
    \ n + 1):\n        fact[i] = i * fact[i - 1] % Mod\n\n    fact_inv = [0] * (n\
    \ + 1); fact_inv[-1] = pow(fact[-1], -1, Mod)\n    for i in range(n-1, -1, -1):\n\
    \        fact_inv[i] = (i + 1) * fact_inv[i + 1] % Mod\n\n    f = [pow(i, n, Mod)\
    \ * fact_inv [i] % Mod for i in range(n + 1)]\n    g = [fact_inv[i] if i & 1 ==\
    \ 0 else -fact_inv[i] for i in range(n + 1)]\n    return Calc.convolution(f, g)[:n\
    \ + 1]\n\ndef Bell(n: int) -> list[int]:\n    \"\"\" Bell \u6570 Bell[k] ({1,\
    \ 2, ..., k} \u306E\u5206\u5272\u306E\u6570) \u3092 k = 0, 1, ..., n \u306B\u5BFE\
    \u3057\u3066\u6C42\u3081\u308B.\n\n    Args:\n        n (int):\n\n    Returns:\n\
    \        list[int]: \u7B2C k \u9805\u306F Bell[k] \u306B\u5BFE\u5FDC\u3059\u308B\
    .\n    \"\"\"\n\n    # Note: Bell(X) = exp(exp(X) - 1) \u3067\u3042\u308B.\n\n\
    \    fact = [1] * (n + 1)\n    for k in range(1, n + 1):\n        fact[k] = (k\
    \ * fact[k - 1]) % Mod\n\n    fact_inv = [1] * (n + 1)\n    fact_inv[-1] = pow(fact[-1],\
    \ -1, Mod)\n    for k in range(n - 1, 0, -1):\n        fact_inv[k] = (k + 1) *\
    \ fact_inv[k + 1] % Mod\n\n    # G = exp(X) - 1\n    g = [0] + fact_inv[1:]\n\n\
    \    # F = exp(G) = exp(exp(X) - 1)\n    f = Exp(Modulo_Polynomial(g, n + 1)).poly\n\
    \n    for k in range(1, n + 1):\n        f[k] = fact[k] * f[k] % Mod\n\n    return\
    \ f\n\ndef Motzkin(n: int) -> list[int]:\n    \"\"\" Motzkin \u6570 Mot[k] (\u5186\
    \u5468\u4E0A\u306E\u533A\u5225\u304C\u3064\u304F\u76F8\u7570\u306A\u308B k \u70B9\
    \u3092\u7DDA\u5206\u3092\u3069\u306E2\u3064\u3082\u5171\u901A\u90E8\u5206\u304C\
    \u306A\u3044 (k \u70B9\u5185\u3067\u5171\u6709\u3082\u7981\u6B62) \u3067\u7D50\
    \u3076\u65B9\u6CD5 (\u7D50\u3070\u308C\u306A\u3044\u70B9\u304C\u3042\u3063\u3066\
    \u3082\u3088\u3044) \u306E\u6570) \u3092 k = 0, 1, ..., n \u306B\u5BFE\u3057\u3066\
    \u6C42\u3081\u308B.\n\n    Args:\n        n (int):\n\n    Returns:\n        list[int]:\
    \ \u7B2C k \u9805\u306F Mot[k] \u306B\u5BFE\u5FDC\u3059\u308B.\n    \"\"\"\n\n\
    \    two_inv = pow(2, -1, Mod)\n    F = ((Modulo_Polynomial([1, -1], n + 3) -\
    \ Sqrt(Modulo_Polynomial([1,-2,-3], n + 3))) * two_inv) >> 2\n    return F.poly[:n\
    \ + 1]\n\n#===\ndef Subset_Sum(X: list[int], K: int) -> list[int]:\n    \"\"\"\
    \ k = 0, 1, ..., K \u306B\u5BFE\u3057\u3066, X \u306E\u9023\u7D9A\u3068\u306F\u9650\
    \u3089\u306A\u3044\u90E8\u5206\u5217 Y \u306E\u3046\u3061, sum(Y) = k \u3068\u306A\
    \u308B Y \u306E\u6570 (\u5834\u6240\u304C\u7570\u306A\u308C\u3070\u5225\u3068\u3057\
    \u3066\u30AB\u30A6\u30F3\u30C8) \u3092\u6C42\u3081\u308B.\n\n    Args:\n     \
    \   X (list[int]):\n        K (int):\n\n    Returns:\n        list[int]: \u7B2C\
    \ k \u9805\u306F\u300CX \u306E\u9023\u7D9A\u3068\u306F\u9650\u3089\u306A\u3044\
    \u90E8\u5206\u5217 Y \u306E\u3046\u3061, sum(Y) = k \u3068\u306A\u308B Y \u306E\
    \u6570 (\u5834\u6240\u304C\u7570\u306A\u308C\u3070\u5225\u3068\u3057\u3066\u30AB\
    \u30A6\u30F3\u30C8)\u300D\n    \"\"\"\n\n    chi = [0] * (K + 1)\n    for x in\
    \ X:\n        if x <= K:\n            chi[x] += 1\n\n    inv = [0] * (K+1)\n \
    \   inv[1] = 1\n    for i in range(2,K+1):\n        q, r = divmod(Mod, i)\n  \
    \      inv[i] = (-q * inv[r]) % Mod\n\n    f = [0] * (K + 1)\n    for i in range(1,K+1):\n\
    \        if chi[i] == 0:\n            continue\n\n        c = 1\n        for k\
    \ in range(1, K // i + 1):\n            f[i * k] = (f[i * k] + c * inv[k] * chi[i])\
    \ % Mod\n            c *= -1\n\n    return Exp(Modulo_Polynomial(f, K + 1)).poly\n\
    \n# \u591A\u9805\u5F0F\u548C\ndef Polynominal_Sigma(P: Modulo_Polynomial) -> Modulo_Polynomial:\n\
    \    \"\"\" \u591A\u9805\u5F0F P \u306B\u5BFE\u3057\u3066, Q(n) = P(1) + P(2)\
    \ + ... + P(n) \u3092\u6E80\u305F\u3059\u591A\u9805\u5F0F Q \u3092\u6C42\u3081\
    \u308B.\n\n    Args:\n        P (Modulo_Polynomial):\n\n    Returns:\n       \
    \ Modulo_Polynomial: Q\n    \"\"\"\n\n    from itertools import accumulate\n\n\
    \    n = len(P.poly)\n    y_pre = Multipoint_Evaluation(P, list(range(1, n + 2)))\n\
    \    y = list(accumulate(y_pre, lambda x, y: (x + y) % Mod))\n    return Polynominal_Interpolation(list(range(1,\
    \ n + 2)), y)\n\ndef Differences(P: Modulo_Polynomial, k: int = 1) -> Modulo_Polynomial:\n\
    \    \"\"\" \u4EE5\u4E0B\u3067\u5B9A\u7FA9\u3055\u308C\u308B P \u306E k \u56DE\
    \u5DEE\u5206 D^k(P) \u3092\u6C42\u3081\u308B.\n        D^t(P(n)) = D^{t-1}(P(n+1)-P(n)),\
    \ D^0(P)=P.\n\n    Args:\n        P (Modulo_Polynomial):\n        k (int, optional):\
    \ \u5DEE\u5206\u306E\u968E\u6570. Defaults to 1.\n\n    Returns:\n        Modulo_Polynomial:\
    \ D^k(P)\n    \"\"\"\n\n    n = len(P.poly)\n\n    fact = [1] * (k + 1)\n    for\
    \ i in range(1, k + 1):\n        fact[i] = i * fact[i - 1] % Mod\n\n    fact_inv\
    \ = [1] * (k + 1)\n    fact_inv[-1] = pow(fact[i], -1, Mod)\n    for i in range(k\
    \ - 1, -1, -1):\n        fact_inv[i] = (i + 1) *fact_inv[i + 1] % Mod\n\n    q\
    \ = [0] * (n - k)\n    sgn = 1 if k % 2 == 0 else -1\n\n    for r in range(k +\
    \ 1):\n        alpha = sgn * fact[k] * (fact_inv[r] * fact_inv[k - r] % Mod) %\
    \ Mod\n        for j in range(n - k):\n            q[j] += alpha * P[j] % Mod\n\
    \n        if r == k:\n            break\n\n        sgn *= -1\n        P = Taylor_Shift(P,\
    \ 1)\n\n    return Modulo_Polynomial(q, P.max_degree)\n"
  dependsOn: []
  isVerificationFile: false
  path: Modulo_Sequence/Modulo_Sequence.py
  requiredBy: []
  timestamp: '2025-05-04 00:51:23+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Modulo_Sequence/Modulo_Sequence.py
layout: document
title: Modulo Sequence
---

## Outline

線形漸化式で表された数列に関する計算を行う.

## Theory

### 線形漸化式の第 $N$ 項

数列 $A=(A_n)$ は漸化式

$$A_n=\sum_{k=0}^{d-1} C_k A_{n-k-1} \quad (n \geq d)$$

を満たしているとする.

このとき, 形式的ベキ級数 $Q$, 多項式 $P$ をそれぞれ

- $Q(X)=1-C_0 X-C_1 X^2-\dots-C_{d-1} X^d$
- $P(X)=(A_0+A_1 X+\dots+A_{d-1} X^{d-1}) Q(X) \pmod{X^d}$

とすると, 任意の非負整数 $n$ において,

$$A_n=\left[X^n \right] \dfrac{P(X)}{Q(X)}$$

となる.

### 分割数

非負整数 $N$ に対して, $N$ を $0$ 個以上の正の整数の和で表す方法 (ただし, 順番の違いは同一視する) を分割数といい, $P_N$ と書く.

このとき, $P_N$ は

$$P_N=\left[X^N \right] \prod_{n=1}^\infty \dfrac{1}{1-X^n}$$

である.

なお, 五角数定理 により,

$$\prod_{n=1}^\infty (1-X^n)=\sum_{n=-\infty}^{\infty} (-1)^n X^{n(3n-1)/2}$$

となるから, 高速化できる.

### 相異なる整数への分割

非負整数 $N$ に対して, $N$ を $0$ 個以上相異なる正の整数の和で表す方法 (ただし, 順番の違いは同一視する) を $Q_N$ と書く.

このとき, $Q_N$ は

$$Q_N=\left[X^N \right] \prod_{n=1}^\infty (1+X^n)$$

である.

なお, ベキ級数展開することによって,

$$1+X^n=\exp \left(\log (1+X^n) \right)=\exp \left( \sum_{k=1}^\infty (-1)^{k-1} X^{kn} \right)$$

であるから,

$$Q_N=\left[X^N \right] \exp \left(\sum_{n=1}^\infty \sum_{k=1}^\infty (-1)^{k-1} X^{kn} \right)$$

となる. なお, $Q_N$ を求める際には, $N$ 次まであれば十分でるが, $kn \leq N$ となる非負整数の組の個数は $O(N \log N)$ 個程度になる.

## Contents

---

### Nth_Term_of_Linearly_Recurrent_Sequence

```Pyhon
Nth_Term_of_Linearly_Recurrent_Sequence(A, C, N, offset=0)
```

- $A,C$ の長さを $d$ とする.
- 線形漸化式 $\displaystyle A_n=\sum_{k=0}^{d-1} C_k A_{n-k-1} \quad (n \geq d)$ で表される整数列 $A=(A_i)$ の第 $N$ 項 $A_N$ を求める.
- **制約**
  - $A$ と $C$ の長さは等しい.
- **計算量** : $O(d \log d \log N)$ Time.

---

### Find_Linear_Recurrence

```Python
Find_Linear_Recurrence(A)
```

- 整数列 $A=(A_0, \dots, A_{N-1})$ が見たす最小の次数の漸化式を求める.

---

### Fibonacci

```Python
Fibonacci(N)
```

- 以下で定義される Fibonacci 数列 $F=(F_n)$ の第 $N$ 項を求める.
  - $F_0=0, F_1=1$
  - $F_n=F_{n-1}+F_{n-2} \quad (n \geq 2)$
- **計算量** : $O(\log N)$ Time.

---

### Lucas

```Python
Lucas(N)
```

- 以下で定義される Lucas 数列 $L=(L_n)$ の第 $N$ 項を求める.
  - $L_0=2, L_1=1$
  - $L_n=L_{n-1}+L_{n-2} \quad (n \geq 2)$
- **計算量** : $O(\log N)$ Time.

---

### Cumulative

```Python
Cumulative(A,N)
```

- $A$ の長さを $d$ とする. 以下で定義される数列 $B=(B_n)$ の第 $N$ 項を求める.
  - $B_n=A_n \quad (0 \leq n \leq d-1)$
  - $B_n=B_{n-1}+B_{n-2}+\dots+B_{n-d} \quad (n \geq d)$
- **計算量** : $A$ の長さを $d$ として, $O(d \log d \log N)$ Time.

---

### Factorial_Modulo

```Python
Factorial_Modulo(N)
```

- $N! \pmod{\mathrm{mod}}$ を求める.

- **計算量** : $O(\sqrt{N} (\log N)^2)$ Time.

---

### Bernoulli

```Python
Bernoulli(N, mode=0)
```

- Bernoulli 数を求める.
- ${\rm mode}=0$ ならば, $B_N$ のみ, ${\rm mode}=1$ ならば, $B_0, \dots, B_N$ からなるリスト.
- **計算量** : $O(N \log N)$ TIme.

---

### PartitionsP

```Python
PartitionsP(N, mode=0)
```

- 以下で定義される $P_k$ を求める.
  - 整数 $k$ を順番を考慮せずに自然数の和にわける場合の数
- ${\rm mode}=0$ ならば, $P_N$ のみ, ${\rm mode}=1$ ならば, $P_0, \dots, P_N$ からなるリスト.
- **計算量** : $O(N \log N)$ TIme.

---

### PartitionsQ

```Python
PartitionsQ(N, mode=0)
```

- 以下で定義される $Q_k$ を求める.
  - 整数 $k$ を相異なる自然数の和にわける場合の数
- ${\rm mode}=0$ ならば, $Q_N$ のみ, ${\rm mode}=1$ ならば, $Q_0, \dots, Q_N$ からなるリスト.
- **計算量** : $O(N \log N)$ TIme.

---

### Stirling_1st

``` Python
Stirling_1st(N)
```

- $k=0,1,\dots,N$ に対する第 I 種スターリング数 $\begin{bmatrix} n \\ k \end{bmatrix}$ を求める.
- **計算量** : $O(N (\log N)^2)$ Time ?

### Stirling_2nd

``` Python
Stirling_2nd(N)
```

- $k=0,1,\dots,N$ に対する第 II 種スターリング数 $\begin{Bmatrix} n \\ k \end{Bmatrix}$ を求める.
- **計算量** : $O(N \log N)$ Time.

### Bell

```Pythoon
Bell(N, mode=0)
```

- 次の式で定義される Bell 数 $B_n$ を求める. $\displaystyle \sum_{n=0}^\infty B_n x^n=\exp(\exp(x)-1)$

- ${\rm mode}=0$ ならば, $B_N$ のみ, ${\rm mode}=1$ ならば, $B_0, \dots, B_N$ からなるリスト.
- **計算量** : $O(N \log N)$ TIme.

### Motzkin

```Pythoon
Motzkin(N, mode=0)
```

- 次の式で定義される Motzkin 数 $M_n$ を求める. $\displaystyle \sum_{n=0}^\infty M_n x^n=\dfrac{1-x-\sqrt{1-2x-3x^2}}{2x^2}$

- ${\rm mode}=0$ ならば, $M_N$ のみ, ${\rm mode}=1$ ならば, $M_0, \dots, M_N$ からなるリスト.
- **計算量** : $O(N \log N)$ TIme.
