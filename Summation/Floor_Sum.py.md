---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test_verify/yosupo_library_checker/Math/Floor_Sum.test.py
    title: test_verify/yosupo_library_checker/Math/Floor_Sum.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.2/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.2/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def floor_sum(A, B, M, N):\n    \"\"\"sum_{i=0}^{N-1} floor((A*i+B)/M) \u3092\
    \u6C42\u3081\u308B.\n    \"\"\"\n    T=0\n    while True:\n        T+=((N-1)*N//2)*(A//M)\n\
    \        A%=M\n\n        T+=N*(B//M)\n        B%=M\n\n        y=(A*N+B)//M\n \
    \       x=B-y*M\n\n        if y==0:\n            return T\n\n        T+=(N+x//A)*y\n\
    \        A,B,M,N=M,x%A,A,y\n\ndef Floor_Sum(A: int, B: int, M: int, N: int, K=0):\n\
    \    \"\"\"sum_{i=K}^N floor((A*i+B)/M) \u3092\u6C42\u3081\u308B.\n    \"\"\"\n\
    \n    if K==0:\n        return floor_sum(A,B,M,N+1)\n    else:\n        return\
    \ floor_sum(A,B,M,N+1)-floor_sum(A,B,M,K)\n"
  dependsOn: []
  isVerificationFile: false
  path: Summation/Floor_Sum.py
  requiredBy: []
  timestamp: '2022-11-23 04:24:29+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test_verify/yosupo_library_checker/Math/Floor_Sum.test.py
documentation_of: Summation/Floor_Sum.py
layout: document
title: Floor Sum
---

## Outline

$\displaystyle \sum\_{i=K}^N \left \lfloor \dfrac{Ai+B}{M}\right \rfloor$ を高速に求めるアルゴリズム.

## Theory

$\displaystyle S(A,B,M,N):=\sum\_{i=0}^N \left \lfloor \dfrac{Ai+B}{M}\right \rfloor$ とする.

$A$ を $M$ で割った商と余りを $Q_A, R_A$, $B$ を $M$ で割った余りを $Q_B, R_B$ とすると,

$$\begin{align*}
\left \lfloor \dfrac{Ai+B}{M}\right \rfloor
&=\left \lfloor \dfrac{(Q_A M+R_A) i+(Q_B M+R_B)}{M}\right \rfloor \\
&=\left \lfloor \dfrac{(Q_A i+Q_B)M+(R_A i+R_B)}{M}\right \rfloor \\
&=\left \lfloor (Q_A i+Q_B) + \dfrac{R_A i+R_B}{M}\right \rfloor \\
&=(Q_A i+Q_B) \left \lfloor \dfrac{R_A i+R_B}{M}\right \rfloor
\end{align*}$$

であるから,

$$\begin{align*}
S(A,B,M,N)
&=\sum_{i=0}^{N-1} \left(Q_A i+ Q_B+\left \lfloor \dfrac{R_A i+R_B}{M}\right \rfloor \right)\\
&=\dfrac{Q_A}{2} N(N-1)+Q_B N +\sum_{i=0}^{N-1} \left \lfloor \dfrac{R_A i+R_B}{M}\right \rfloor\\
&=\dfrac{Q_A}{2} N(N-1)+Q_B N +S(R_A, R_B, M, N)
\end{align*}$$

となり, $0 \leq A,B \lt M$ の場合のみを考慮すれば十分であることが分かる.

以降では $0 \leq A,B \lt M$ とする.

(途中)

## Contents

---

### floor_sum

```Python
floor_sum(A,B,M,N)
```

* $\displaystyle \sum\_{i=0}^{N-1} \left \lfloor \dfrac{Ai+B}{M}\right \rfloor$ を求める.

### Floor_Sum

```Python
Floor_Sum(A,B,M,N,K=0)
```

* $\displaystyle \sum\_{i=K}^{N} \left \lfloor \dfrac{Ai+B}{M}\right \rfloor$ を求める.
  * 範囲の右端が `floor_sum` だと開だが, `Floor_Sum` だと閉になっていることに注意せよ.
