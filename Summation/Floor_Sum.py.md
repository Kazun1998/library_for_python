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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.2/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.2/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
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
