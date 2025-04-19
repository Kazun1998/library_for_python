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
  code: "#Euler's Totient\u95A2\u6570\ndef Euler_Totient(N, mode=True):\n    \"\"\"\
    \ 1 \u4EE5\u4E0A N \u4EE5\u4E0B\u306E\u6574\u6570\u306E\u3046\u3061, N \u3068\u4E92\
    \u3044\u306B\u7D20\u306A\u6574\u6570\u306E\u500B\u6570 phi (N) \u3092\u6C42\u3081\
    \u308B.\n\n    Args:\n        N (int): \u6B63\u306E\u6574\u6570\n        mode:\
    \ False \u306B\u3059\u308B\u3068, N \"\u4EE5\u4E0B\" \u304C N \"\u672A\u6E80\"\
    \ \u306B\u306A\u308B (phi(1) \u304C True \u3060\u3068 1, False \u3060\u3068 0\
    \ \u306B\u306A\u308B\u3060\u3051\u306E\u9055\u3044\u3067\u3042\u308B) \n\n   \
    \ Returns:\n        int: varphi (N)\n    \"\"\"\n\n    assert N>=0,\"N\u304C\u975E\
    \u8CA0\u6574\u6570\u3067\u306F\u306A\u3044.\"\n\n    if N==1:\n        return\
    \ 1 if mode else 0\n\n    e=(N&(-N)).bit_length()-1\n    if e>0:\n        phi=1<<(e-1)\n\
    \        N>>=e\n    else:\n        phi=1\n\n    e=0\n    while N%3==0:\n     \
    \   e+=1\n        N//=3\n\n    if e>0:\n        phi*=pow(3,e-1)*2\n\n    flag=0\n\
    \    p=5\n    while p*p<=N:\n        if N%p==0:\n            e=0\n           \
    \ while N%p==0:\n                e+=1\n                N//=p\n\n            phi*=pow(p,e-1)*(p-1)\n\
    \n        p+=2\n        flag^=1\n\n    if N>1:\n        phi*=N-1\n\n    return\
    \ phi\n\n#Euler's Totient\u95A2\u6570\ndef Euler_Totient_List(N, mode=True):\n\
    \    \"\"\"k=0,1,...,N \u306B\u5BFE\u3057\u3066, 1\u4EE5\u4E0Ak\u4EE5\u4E0B\u306E\
    \u6574\u6570\u306E\u3046\u3061, k\u3068\u4E92\u3044\u306B\u7D20\u306A\u6574\u6570\
    \u306E\u500B\u6570 \u03C6(k) \u3092\u6C42\u3081\u308B.\n\n    N:\u6B63\u306E\u6574\
    \u6570\n    mode: False \u306B\u3059\u308B\u3068, N \"\u4EE5\u4E0B\" \u304C N\
    \ \"\u672A\u6E80\" \u306B\u306A\u308B (phi(1) \u304C True \u3060\u3068 1, False\
    \ \u3060\u3068 0 \u306B\u306A\u308B\u3060\u3051\u306E\u9055\u3044\u3067\u3042\u308B\
    ) \n    \"\"\"\n\n    assert N>=0,\"N\u304C\u975E\u8CA0\u6574\u6570\u3067\u306F\
    \u306A\u3044.\"\n\n    phi=list(range(N+1))\n    for p in range(2,N+1):\n    \
    \    if phi[p]==p:\n            for j in range(p,N+1,p):\n                phi[j]=phi[j]//p*(p-1)\n\
    \n    if not mode and N>=1:\n        phi[1]=0\n\n    return phi\n"
  dependsOn: []
  isVerificationFile: false
  path: Integer/Totient.py
  requiredBy: []
  timestamp: '2023-03-18 02:55:12+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Integer/Totient.py
layout: document
title: Totient Function
---

## Outline

Euler の Totient 関数 $\varphi$ に関する計算を行う.

正の整数 $N$ に対して, $N$ と互いに素な $1$ 以上 $N$ 未満の整数の個数を $\varphi(N)$ と書く.

## Theory

Euler の Totient 関数 に対して, 以下の性質が成り立つ.

* 素数 $p$ と非負整数 $k$ に対して, $\varphi(p^k) = p^k - p^{k-1} = p^{k-1} (p-1)$.
* 互いに素な正の整数 $m, n$ に対して, $\varphi(mn) = \varphi(m) \varphi(n)$.

このことから, $N$ の素因数分解を

$$ N = p_1^{e_1} \times \dots \times p_r^{e_r} = \prod_{i = 1}^r p_i^{e_i} \quad (i \neq j \Rightarrow p_i \neq p_j)$$

としたとき,

$$ \varphi(N) = \prod_{i=1}^r p_i^{e_i-1} (p_i - 1) = N \prod_{i=1}^r \left(1 - \dfrac{1}{p_i} \right)$$

となる.

$N$ の素因数分解は試し割りを用いると, $O(\sqrt{N})$ 時間, 高速な方法で $O(N^{1/4})$ 時間で求められるので, $\varphi(N)$ もこれらと同程度の時間で求められる.

### $\varphi$ の性質

$\varphi$ について, 以下が成り立つ.

* $N \geq 2$ とする. $\mathbb{Z}/N \mathbb{Z}$ における可逆元の個数は $\varphi(N)$ 個である.
* $d$ を $N$ の約数とする. $\gcd(N,x) = \frac{N}{d}$ となる $N$ 未満の非負整数の数は $\varphi(d)$ 個である. このことから, $\displaystyle \sum_{d \mid N} \varphi(d) = N$ が成り立つ.
