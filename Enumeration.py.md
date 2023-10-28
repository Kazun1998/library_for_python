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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.0/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.0/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "\"\"\"\nMod \u306F\u30B0\u30ED\u30FC\u30D0\u30EB\u5909\u6570\u304B\u3089\u306E\
    \u6307\u5B9A\u3068\u3059\u308B.\n\"\"\"\n\n\"\"\"\n\u7A4D\n\"\"\"\ndef product_modulo(*X):\n\
    \    y=1\n    for x in X:\n        y=(x*y)%Mod\n    return y\n\n\"\"\"\n\u968E\
    \u4E57\n\"\"\"\ndef Factor(N):\n    \"\"\" 0!, 1!, ..., N! (mod Mod) \u3092\u51FA\
    \u529B\u3059\u308B.\n\n    N: int\n    \"\"\"\n    f=[1]*(N+1)\n    for k in range(1,N+1):\n\
    \        f[k]=(k*f[k-1])%Mod\n    return f\n\ndef Factor_with_inverse(N):\n  \
    \  \"\"\" 0!, 1!, ..., N!, (0!)^-1, (1!)^-1, ..., (N!)^-1 \u3092\u51FA\u529B\u3059\
    \u308B.\n\n    N: int\n    \"\"\"\n\n    f = Factor(N)\n    g = [0]*(N+1)\n\n\
    \    N = min(N, Mod-1)\n    g[N] = pow(f[N], -1, Mod)\n\n    for k in range(N-1,-1,-1):\n\
    \        g[k] = ((k+1) * g[k+1]) % Mod\n\n    return f, g\n\ndef Double_Factor(N):\n\
    \    \"\"\" 0!!, 1!!, ..., N!! (mod Mod) \u3092\u51FA\u529B\u3059\u308B.\n\n \
    \   N: int\n    \"\"\"\n    f=[1]*(N+1)\n    for i in range(2,N+1):\n        f[i]=i*f[i-2]%Mod\n\
    \    return f\n\ndef Modular_Inverse(N):\n    \"\"\" 1^(-1), 2^(-1), ..., N^(-1)\
    \ (mod Mod) \u3092\u51FA\u529B\u3059\u308B.\n\n    [Input]\n    N:int\n\n    [Output]\n\
    \    [-1, 1^(-1), 2^(-1), ..., N^(-1)] (\u7B2C 0 \u8981\u7D20\u306B\u6CE8\u610F\
    !!)\n    \"\"\"\n\n    inv=[1]*(N+1); inv[0]=-1\n    for k in range(2, N+1):\n\
    \        q,r=divmod(Mod,k)\n        inv[k]=(-q*inv[r])%Mod\n    return inv\n\n\
    \"\"\"\n\u7D44\u307F\u5408\u308F\u305B\u306E\u6570\nFactor_with_inverse \u3067\
    \ fact, fact_inv \u3092\u65E2\u306B\u6C42\u3081\u3066\u3044\u308B\u3053\u3068\u304C\
    \u524D\u63D0 (\u30B0\u30ED\u30FC\u30D0\u30EB\u5909\u6570)\n\"\"\"\n\ndef nCr(n,r):\n\
    \    \"\"\" nCr (1,2,...,n \u304B\u3089\u76F8\u7570\u306A\u308B r \u500B\u306E\
    \u6574\u6570\u3092\u9078\u3076\u65B9\u6CD5) \u3092\u6C42\u3081\u308B.\n\n    n,r:\
    \ int\n    \"\"\"\n\n    if 0<=r<=n:\n        return fact[n]*(fact_inv[r]*fact_inv[n-r]%Mod)%Mod\n\
    \    else:\n        return 0\n\ndef nPr(n,r):\n    \"\"\" nPr (1,2,...,n \u304B\
    \u3089\u76F8\u7570\u306A\u308B r \u500B\u306E\u6574\u6570\u3092\u9078\u3073, \u4E26\
    \u3079\u308B\u65B9\u6CD5) \u3092\u6C42\u3081\u308B.\n\n    n,r: int\n    \"\"\"\
    \n\n    if 0<=r<=n:\n        return (fact[n]*fact_inv[n-r])%Mod\n    else:\n \
    \       return 0\n\ndef nHr(n,r):\n    \"\"\" nHr (1,2,...,n \u304B\u3089\u91CD\
    \u8907\u3092\u8A31\u3057\u3066 r \u500B\u306E\u6574\u6570\u3092\u9078\u3076\u65B9\
    \u6CD5) \u3092\u6C42\u3081\u308B.\n\n    n,r: int\n    \u203B fact, fact_inv \u306F\
    \u7B2C n+r-1 \u9805\u307E\u3067\u5FC5\u8981\n    \"\"\"\n\n    if n==r==0:\n \
    \       return 1\n    else:\n        return nCr(n+r-1,r)\n\ndef Multinomial_Coefficient(*K):\n\
    \    \"\"\" K=[k_0,...,k_{r-1}] \u306B\u5BFE\u3057\u3066, k_0, ..., k_{r-1} \u306B\
    \u5BFE\u3059\u308B\u591A\u9805\u4FC2\u6570\u3092\u6C42\u3081\u308B.\n\n    k_i:\
    \ int\n    \"\"\"\n\n    N=0\n    g_inv=1\n    for k in K:\n        N+=k\n   \
    \     g_inv*=fact_inv[k]; g_inv%=Mod\n    return (fact[N]*g_inv)%Mod\n\ndef Binomial_Coefficient_Modulo_List(n:\
    \ int):\n    \"\"\" n \u3092\u56FA\u5B9A\u3057, r=0,1,...,n \u3068\u3057\u305F\
    \u3068\u304D\u306E nCr (mod Mod) \u306E\u30EA\u30B9\u30C8\u3092\u51FA\u529B\u3059\
    \u308B.\n\n    n: int\n\n    [\u51FA\u529B]\n    [nC0 , nC1 ,..., nCn]\n    \"\
    \"\"\n\n    L=[1]*(n+1)\n    inv=Modular_Inverse(n+1)\n    for r in range(1, n+1):\n\
    \        L[r]=((n+1-r)*inv[r]%Mod)*L[r-1]%Mod\n    return L\n\ndef Pascal_Triangle(N:\
    \ int, mode=False):\n    \"\"\"\n    0<=n<=N, 0<=r<=n \u306E\u5168\u3066\u306B\
    \u5BFE\u3057\u3066 nCr (mod M) \u306E\u30EA\u30B9\u30C8\u3092\u51FA\u529B\u3059\
    \u308B.\n\n    N: int\n\n    [\u51FA\u529B]\n    [[0C0], [1C0, 1C1], ... , [nC0,\
    \ ... , nCn], ..., [NC0, ..., NCN]]\n    \"\"\"\n\n    if mode:\n        L=[[0]*(N+1)\
    \ for _ in range(N+1)]\n        L[0][0]=1\n        for n in range(1,N+1):\n  \
    \          Ln=L[n]; Lnn=L[n-1]\n            Ln[0]=1\n            for r in range(1,N+1):\n\
    \                Ln[r]=(Lnn[r]+Lnn[r-1])%Mod\n        return L\n\n    else:\n\
    \        X=[1]\n        L=[[1]]\n        for n in range(N):\n            Y=[1]\n\
    \            for k in range(1, n+1):\n                Y.append((X[k]+X[k-1])%Mod)\n\
    \            Y.append(1)\n            X=Y\n            L.append(Y)\n    return\
    \ L\n\ndef Lucas_Combination(n, r):\n    \"\"\" Lucas \u306E\u5B9A\u7406\u3092\
    \u7528\u3044\u3066 nCr (mod Mod) \u3092\u6C42\u3081\u308B.\n\n    \"\"\"\n\n \
    \   X=1\n    while n or r:\n        ni=n%Mod; ri=r%Mod\n        n//=Mod; r//=Mod\n\
    \n        if ni<ri:\n            return 0\n\n        beta=fact_inv[ri]*fact_inv[ni-ri]%Mod\n\
    \        X*=(fact[ni]*beta)%Mod\n        X%=Mod\n    return X\n\"\"\"\n\u7279\u5225\
    \u306A\u6570\n\"\"\"\n\ndef Catalan_Number(N):\n    \"\"\" Catalan \u6570 C(N)\
    \ \u3092\u6C42\u3081\u308B.\n\n    \u6CE8\u610F\n    C(N)=(2N)!/((N+1)!N!) \u306A\
    \u306E\u3067, (2N)! \u307E\u3067\u306E\u5024\u304C\u5FC5\u8981.\n    \"\"\"\n\n\
    \    g_inv=fact_inv[N+1]*fact_inv[N]%Mod\n    return fact[2*N]*g_inv%Mod\n\n\"\
    \"\"\n\u7B49\u6BD4\u6570\u5217\n\"\"\"\n\ndef Geometric_Sequence(a, r, N):\n \
    \   \"\"\" k=0,1,...,N \u306B\u5BFE\u3059\u308B a*r^k \u3092\u51FA\u529B\u3059\
    \u308B.\n\n    a,r,N: int\n    \"\"\"\n\n    a%=Mod; r%=Mod\n    X=[0]*(N+1);\
    \ X[0]=a\n    for k in range(1,N+1):\n        X[k]=r*X[k-1]%Mod\n    return X\n\
    \ndef Geometric_Inverse_Sequence(a, r, N):\n    \"\"\" k=0,1,...,N \u306B\u5BFE\
    \u3059\u308B a/r^k \u3092\u51FA\u529B\u3059\u308B.\n\n    a,r,N: int\n    \"\"\
    \"\n\n    a %= Mod; r_inv = pow(r, -1, Mod)\n    X = [0] * (N+1); X[0]=a\n\n \
    \   for k in range(1,N+1):\n        X[k] = r_inv * X[k-1] % Mod\n    return X\n\
    \n\"\"\"\n\u7A4D\u548C\n\"\"\"\ndef Sum_of_Product(*X):\n    \"\"\" \u9577\u3055\
    \u304C\u7B49\u3057\u3044\u30EA\u30B9\u30C8 X_1, X_2, ..., X_k \u306B\u5BFE\u3057\
    \u3066, sum(X_1[i]*X_2[i]*...*X_k[i]) \u3092\u6C42\u3081\u308B.\n    \"\"\"\n\n\
    \    S=0\n    for alpha in zip(*X):\n        S+=product_modulo(*alpha)\n    return\
    \ S%Mod\n\ndef Sum_of_Product_Yielder(N,*Y):\n    S=0\n    M=len(Y)\n    for _\
    \ in range(N+1):\n        x=1\n        for j in range(M):\n            x*=next(Y[j]);\
    \ x%=Mod\n        S+=x\n    return S%Mod\n#==================================================\n"
  dependsOn: []
  isVerificationFile: false
  path: Enumeration.py
  requiredBy: []
  timestamp: '2023-08-06 20:53:14+09:00'
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
