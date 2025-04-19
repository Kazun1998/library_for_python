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
  code: "\"\"\"\nMod \u306F\u30B0\u30ED\u30FC\u30D0\u30EB\u5909\u6570\u304B\u3089\u306E\
    \u6307\u5B9A\u3068\u3059\u308B.\n\"\"\"\n\n\"\"\"\n\u7A4D\n\"\"\"\ndef product_modulo(*X:\
    \ int) -> int:\n    y = 1\n    for x in X:\n        y = (x * y) % Mod\n    return\
    \ y\n\n\"\"\"\n\u968E\u4E57\n\"\"\"\ndef Factor(N: int) -> list[int]:\n    \"\"\
    \" 0!, 1!, 2!, ..., N! (\u3092 Mod \u3067\u5272\u3063\u305F\u4F59\u308A) \u304B\
    \u3089\u306A\u308B\u30EA\u30B9\u30C8\u3092\u751F\u6210\u3059\u308B.\n\n    Args:\n\
    \        N (int): \u4E0A\u9650\n\n    Returns:\n        list[int]: \u7B2C k \u8981\
    \u7D20\u304C k! (mod Mod) \u304B\u3089\u306A\u308B\u9577\u3055 (N + 1) \u306E\u30EA\
    \u30B9\u30C8\n    \"\"\"\n\n    f = [1] * (N + 1)\n    for k in range(1, N + 1):\n\
    \        f[k] = (k * f[k - 1]) % Mod\n    return f\n\ndef Factor_with_inverse(N:\
    \ int) -> tuple[list[int], list[int]]:\n    \"\"\" [0!, 1!, 2!, ..., N!], [(0!)^-1,\
    \ (1!)^-1, ..., (N!)^-1] \u304B\u3089\u306A\u308B\u30EA\u30B9\u30C8\u3092\u751F\
    \u6210\u3059\u308B.\n\n    Args:\n        N (int): \u4E0A\u9650\n\n    Returns:\n\
    \        tuple[list[int], list[int]]:\n            \u7B2C 1 \u8981\u7D20\u306E\
    \u30EA\u30B9\u30C8\u306F\u7B2C k \u8981\u7D20\u304C k! (mod Mod) \u304B\u3089\u306A\
    \u308B\u9577\u3055 (N + 1) \u306E\u30EA\u30B9\u30C8\n            \u7B2C 2 \u8981\
    \u7D20\u306E\u30EA\u30B9\u30C8\u306F\u7B2C k \u8981\u7D20\u304C (k!)^(-1) (mod\
    \ Mod) \u304B\u3089\u306A\u308B\u9577\u3055 (N + 1) \u306E\u30EA\u30B9\u30C8\n\
    \    \"\"\"\n\n    f = Factor(N)\n    g = [0] * (N + 1)\n\n    N = min(N, Mod\
    \ - 1)\n    g[N] = pow(f[N], -1, Mod)\n\n    for k in range(N - 1, -1, -1):\n\
    \        g[k] = ((k + 1) * g[k + 1]) % Mod\n\n    return f, g\n\ndef Double_Factor(N:\
    \ int) -> list[int]:\n    \"\"\" 0!!, 1!!, 2!!, ..., N!! (\u3092 Mod \u3067\u5272\
    \u3063\u305F\u4F59\u308A) \u304B\u3089\u306A\u308B\u30EA\u30B9\u30C8\u3092\u751F\
    \u6210\u3059\u308B.\n\n    Args:\n        N (int): \u4E0A\u9650\n\n    Returns:\n\
    \        list[int]: \u7B2C k \u8981\u7D20\u304C k!! (mod Mod) \u304B\u3089\u306A\
    \u308B\u9577\u3055 (N + 1) \u306E\u30EA\u30B9\u30C8\n    \"\"\"\n\n    f = [1]\
    \ * (N + 1)\n    for k in range(2, N + 1):\n        f[k] = k * f[k - 2] % Mod\n\
    \    return f\n\ndef Modular_Inverse(N: int) -> list[int]:\n    \"\"\" (mod Mod)\
    \ \u306B\u304A\u3051\u308B 1^(-1), 2^(-1), ..., N^(-1) \u304B\u3089\u306A\u308B\
    \u30EA\u30B9\u30C8\u3092\u751F\u6210\u3059\u308B.\n\n    Args:\n        N (int):\
    \ \u4E0A\u9650\n\n    Returns:\n        list[int]: \u521D\u9805\u306F -1, \u7B2C\
    \ k \u8981\u7D20\u304C k^-1 (mod Mod) \u304B\u3089\u306A\u308B\u9577\u3055 (N\
    \ + 1) \u306E\u30EA\u30B9\u30C8\n    \"\"\"\n\n    inv = [1] * (N + 1)\n    inv[0]\
    \ = -1\n\n    for k in range(2, N + 1):\n        q, r = divmod(Mod, k)\n     \
    \   inv[k] = (-q * inv[r]) % Mod\n    return inv\n\n\"\"\"\n\u7D44\u307F\u5408\
    \u308F\u305B\u306E\u6570\nFactor_with_inverse \u3067 fact, fact_inv \u3092\u65E2\
    \u306B\u6C42\u3081\u3066\u3044\u308B\u3053\u3068\u304C\u524D\u63D0 (\u30B0\u30ED\
    \u30FC\u30D0\u30EB\u5909\u6570)\n\"\"\"\n\ndef nCr(n: int, r: int) -> int:\n \
    \   \"\"\" nCr (1,2,...,n \u304B\u3089\u76F8\u7570\u306A\u308B r \u500B\u306E\u6574\
    \u6570\u3092\u9078\u3076\u65B9\u6CD5) \u3092\u6C42\u3081\u308B.\n\n    Args:\n\
    \        n (int):\n        r (int):\n\n    Returns:\n        int: nCr\n    \"\"\
    \"\n\n    if 0 <= r <= n:\n        return fact[n] * (fact_inv[r] * fact_inv[n\
    \ - r] % Mod) % Mod\n    else:\n        return 0\n\ndef nPr(n: int, r: int) ->\
    \ int:\n    \"\"\" nPr (1,2,...,n \u304B\u3089\u76F8\u7570\u306A\u308B r \u500B\
    \u306E\u6574\u6570\u3092\u9078\u3073, \u4E26\u3079\u308B\u65B9\u6CD5) \u3092\u6C42\
    \u3081\u308B.\n\n    Args:\n        n (int):\n        r (int):\n\n    Returns:\n\
    \        int: nPr\n    \"\"\"\n\n    if 0 <= r <= n:\n        return (fact[n]\
    \ * fact_inv[n - r]) % Mod\n    else:\n        return 0\n\ndef nHr(n: int, r:\
    \ int) -> int:\n    \"\"\" nHr (1,2,...,n \u304B\u3089\u91CD\u8907\u3092\u8A31\
    \u3057\u3066 r \u500B\u306E\u6574\u6570\u3092\u9078\u3076\u65B9\u6CD5) \u3092\u6C42\
    \u3081\u308B.\n    \u203B fact, fact_inv \u306F\u7B2C n+r-1 \u9805\u307E\u3067\
    \u5FC5\u8981\n\n    Args:\n        n (int):\n        r (int):\n\n    Returns:\n\
    \        int: nHr\n    \"\"\"\n\n    if n == r == 0:\n        return 1\n    else:\n\
    \        return nCr(n + r - 1, r)\n\ndef Multinomial_Coefficient(*K: int) -> int:\n\
    \    \"\"\" K = [k_0, ..., k_{r-1}] \u306B\u5BFE\u3057\u3066, k_0, ..., k_{r-1}\
    \ \u306B\u5BFE\u3059\u308B\u591A\u9805\u4FC2\u6570\u3092\u6C42\u3081\u308B.\n\n\
    \    Args:\n        K (int):\n\n    Returns:\n        int: k_0, ..., k_{r-1} \u306B\
    \u5BFE\u3059\u308B\u591A\u9805\u4FC2\u6570. \u3064\u307E\u308A, (sum(K)!)/(k_0!\
    \ k_1! ... k_{r-1}!)\n    \"\"\"\n\n    g_inv = 1\n    for k in K:\n        g_inv\
    \ *= fact_inv[k]\n        g_inv %= Mod\n\n    return fact[sum(K)] * g_inv % Mod\n\
    \ndef Binomial_Coefficient_Modulo_List(n: int) -> list[int]:\n    \"\"\" n \u3092\
    \u56FA\u5B9A\u3057, r = 0, 1, ..., n \u3068\u3057\u305F\u3068\u304D\u306E nCr\
    \ (mod Mod) \u306E\u30EA\u30B9\u30C8\u3092\u51FA\u529B\u3059\u308B.\n\n    Args:\n\
    \        n (int): \u56FA\u5B9A\u3059\u308B nCr \u306E n \u306E\u90E8\u5206\n\n\
    \    Returns:\n        list[int]: \u7B2C r \u8981\u7D20\u304C nCr \u3067\u3042\
    \u308B\u9577\u3055 (n + 1) \u306E\u914D\u5217.\n    \"\"\"\n\n    X = [1] * (n\
    \ + 1)\n    inv = Modular_Inverse(n + 1)\n    for r in range(1, n + 1):\n    \
    \    X[r] = ((n + 1 - r) * inv[r] % Mod) * X[r - 1] % Mod\n    return X\n\ndef\
    \ Pascal_Triangle(N: int, square: bool = False) -> list[int]:\n    \"\"\" 0 <=\
    \ n <= N, 0 <= r <= n \u306B\u5BFE\u3059\u308B nCr \u3092\u6C42\u3081\u308B.\n\
    \n    Args:\n        N (int): \u4E0A\u9650\n        square (bool, optional): True\
    \ \u306B\u3059\u308B\u3068, r \u306E\u7BC4\u56F2\u304C 0 <= r <= N \u306B\u306A\
    \u308B. Defaults to False.\n\n    Returns:\n        list[int]: \u7B2C (n, r) \u8981\
    \u7D20\u304C nCr \u3067\u3042\u308B\u4E8C\u91CD\u6DFB\u5B57\u30EA\u30B9\u30C8\n\
    \    \"\"\"\n\n    if square:\n        X = [[0] * (N + 1) for _ in range(N + 1)]\n\
    \        for n in range(N + 1):\n            X[n][0] = 1\n            for r in\
    \ range(1, (N if square else n) + 1):\n                X[n][r] = (X[n - 1][r]\
    \ + X[n - 1][r - 1]) % Mod\n    else:\n        X = [[0] * (n + 1) for n in range(N\
    \ + 1)]\n        for n in range(N + 1):\n            X[n][0] = X[n][n] = 1\n \
    \           for r in range(1, (N if square else n)):\n                X[n][r]\
    \ = (X[n - 1][r] + X[n - 1][r - 1]) % Mod\n\n    return X\n\ndef Lucas_Combination(n:\
    \ int, r: int) -> int:\n    \"\"\" Lucas \u306E\u5B9A\u7406\u3092\u7528\u3044\u3066\
    \ nCr (mod Mod) \u3092\u6C42\u3081\u308B.\n\n    Args:\n        n (int):\n   \
    \     r (int):\n\n    Returns:\n        int: nCr (mod Mod)\n    \"\"\"\n\n   \
    \ X = 1\n    while n or r:\n        ni = n%Mod; ri = r%Mod\n        n //= Mod;\
    \ r //= Mod\n\n        if ni < ri:\n            return 0\n\n        beta = fact_inv[ri]\
    \ * fact_inv[ni - ri] % Mod\n        X *= (fact[ni] * beta) % Mod\n        X %=\
    \ Mod\n    return X\n\ndef Catalan_Number(N: int) -> int:\n    \"\"\" Catalan\
    \ \u6570 C(N) \u3092\u6C42\u3081\u308B.\n    \u203B C(N) = (2N)!/((N+1)! N!) \u3067\
    \u3042\u308B\u305F\u3081, 2N! \u307E\u3067\u306E\u5024\u304C\u5FC5\u8981\n\n \
    \   Args:\n        N (int):\n\n    Returns:\n        int: Catalan \u6570 C(N)\n\
    \    \"\"\"\n\n    g_inv = fact_inv[N + 1] * fact_inv[N] % Mod\n    return fact[2\
    \ * N] * g_inv % Mod\n\n\"\"\"\n\u7B49\u6BD4\u6570\u5217\n\"\"\"\n\ndef Geometric_Sequence(a:\
    \ int, r: int, N: int) -> list[int]:\n    \"\"\" k = 0, 1, ..., N \u306B\u5BFE\
    \u3059\u308B a*r^k \u3092\u51FA\u529B\u3059\u308B.\n\n    Args:\n        a (int):\
    \ \u521D\u9805\n        r (int): \u516C\u6BD4\n        N (int): k \u306E\u6700\
    \u5927\u5024\n\n    Returns:\n        list[int]: \u7B2C k \u9805\u304C a*r^k \u3067\
    \u3042\u308B\u9577\u3055 (N + 1) \u306E\u30EA\u30B9\u30C8\n    \"\"\"\n\n    a\
    \ %= Mod; r %= Mod\n    X = [0] * (N + 1)\n    X[0] = a\n    for k in range(1,\
    \ N + 1):\n        X[k] = r * X[k - 1] %Mod\n    return X\n\ndef Geometric_Inverse_Sequence(a:\
    \ int, r: int, N: int) -> list[int]:\n    \"\"\" k = 0, 1, ..., N \u306B\u5BFE\
    \u3059\u308B a/r^k \u3092\u51FA\u529B\u3059\u308B.\n\n    Args:\n        a (int):\
    \ \u521D\u9805\n        r (int): \u516C\u6BD4\u306E\u9006\u6570\n        N (int):\
    \ k \u306E\u6700\u5927\u5024\n\n    Returns:\n        list[int]: \u7B2C k \u9805\
    \u304C a/r^k \u3067\u3042\u308B\u9577\u3055 (N + 1) \u306E\u30EA\u30B9\u30C8\n\
    \    \"\"\"\n\n\n    a %= Mod\n    r_inv = pow(r, -1, Mod)\n    X = [0] * (N +\
    \ 1)\n    X[0] = a\n\n    for k in range(1, N + 1):\n        X[k] = r_inv * X[k\
    \ - 1] % Mod\n    return X\n\n\"\"\"\n\u7A4D\u548C\n\"\"\"\ndef Sum_of_Product(*X:\
    \ list[int]) -> int:\n    \"\"\" \u9577\u3055\u304C\u7B49\u3057\u3044\u30EA\u30B9\
    \u30C8 X_0, X_1, ..., X_k \u306B\u5BFE\u3057\u3066, sum(X_0[i] * X_1[i] * ...\
    \ * X_k[i]) \u3092\u6C42\u3081\u308B.\n\n    Returns:\n        int: \u7A4D\u548C\
    \n    \"\"\"\n\n    return sum(product_modulo(*alpha) for alpha in zip(*X))\n\n\
    #==================================================\n\nMod = 998244353\n"
  dependsOn: []
  isVerificationFile: false
  path: Enumeration.py
  requiredBy: []
  timestamp: '2025-04-06 14:34:48+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Enumeration.py
layout: document
title: Enumeration
---

## Outline

組合せ論における基本計算を行う関数

## Theory

### 組み合わせを表す関数

(人は互いに区別がつき, ものは互いに区別がつかないとする.)

||意味合い|計算方法|
|:--:|:--:|:--:|
|$N!$|$N$ 人を1列に並べる方法|$N!=1 \times 2 \times \dots \times N$|
|$\dbinom{N}{r}$|$N$ 人から $r$ 人を選び出す方法 |$\dbinom{N}{r}=\dfrac{N!}{r!(N-r)!}$|
|${}_N P_r$|$N$ 人から $r$ 人を選び出し, その $r$ 人を一列に並べる方法|${}_N P_r=\dfrac{N!}{(N-r)!}$|
|${}_N H_r$|$N$ 個のものを $r$ 人に配る方法|${}_N H_r=\dbinom{N+r-1}{r}$ <br> (ただし, $_0H_0=1$ とする.)|
|$\dbinom{N}{r_1, r_2, \dots, r_m}$ <br> $(N=r_1+\dots+r_m)$|$N$ 人を $r_1$ 人の $1$ 班, $\cdots$, $r_m$ 人の $m$ 班に分ける方法|$\dbinom{N}{r_1,r_2, \dots, r_m}=\dfrac{N!}{r_1!r_2! \dots r_m!}$|
|$C_n$<br>(カタラン数)|$N$ 個の `(` と $N$ 個の `)` からなる文字列が正しい文字列になる文字列の数 (など) |$C_N=\dfrac{(2N)!}{(N+1)!N!}$|

### 組み合わせに関する定理

#### Lucas の定理

$p$ を素数とする. $N,r$ の $p$ 進表記をそれぞれ $(N_i)\_{i=0}^{\infty}, (r_i)\_{i=0}^\infty$ としたとき,

$$\dbinom{N}{r} \equiv \prod_{i=0}^\infty \dbinom{N_i}{r_i} \pmod{p}$$

が成り立つ.
