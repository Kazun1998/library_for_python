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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.13.5/x64/lib/python3.13/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.13.5/x64/lib/python3.13/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def Monotone_Minima(N: int, M: int, eval) -> list[int]:\n    \"\"\" N \u884C\
    \ M \u5217\u306E\u884C\u5217 A \u306E\u7B2C (i, j) \u8981\u7D20\u304C eval(i,\
    \ j) \u3067\u3042\u308A, \u4EE5\u4E0B\u306E\u5358\u8ABF\u6027\u3092\u6E80\u305F\
    \u3059\u3068\u3059\u308B.\n        f(i) := min argmin_{j} A(i, j) \u3068\u3057\
    \u305F\u3068\u304D, f(0) <= f(1) <= ... <= f(M - 1) \u304C\u6210\u308A\u7ACB\u3064\
    .\n    \u3053\u306E\u3068\u304D, 0 <= i < N \u306B\u5BFE\u3057\u3066, f(i) \u3092\
    \u6C42\u3081\u308B.\n\n    Args:\n        N (int): \u884C\u306E\u6570\n      \
    \  M (int): \u5217\u306E\u6570\n        eval (Callable[[int, int], int]): \u7B2C\
    \ (i, j) \u8981\u7D20\u304C eval(i, j) \u306B\u306A\u308B.\n\n    Returns:\n \
    \       list[int]: \u7B2C i \u8981\u7D20\u304C f(i) \u3067\u3042\u308B\u9577\u3055\
    \ N \u306E\u30EA\u30B9\u30C8\n    \"\"\"\n    res = [-1] * N\n    stack = [(0,\
    \ N, 0, M)]\n\n    while stack:\n        u, d, l, r = stack.pop()\n\n        if\
    \ d - u < 1:\n            continue\n\n        i = (u + d) // 2\n        j = min(range(l,\
    \ r), key = lambda j: eval(i, j))\n\n        res[i] = j\n\n        stack.append((u,\
    \ i, l, j + 1))\n        stack.append((i + 1, d, j, r))\n\n    return res\n"
  dependsOn: []
  isVerificationFile: false
  path: Monotone/Monotone_Minima.py
  requiredBy: []
  timestamp: '2025-06-01 12:50:15+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Monotone/Monotone_Minima.py
layout: document
title: Monotone Minima
---

## Outline

$N$ 行 $M$ 列の行列 $A = (a_{i,j})$ が Monotone であるとは,

$$ \min \left(\operatorname*{argmin}_{0 \leq j < M} a_{0,j} \right) \leq \min \left(\operatorname*{argmin}_{0 \leq j < M} a_{1,j} \right) \leq \dots \leq \min \left(\operatorname*{argmin}_{0 \leq j < M} a_{N-1,j} \right)$$

を満たすことである.

このとき, $0 \leq i < N$ それぞれに対する

$$ \min \left(\operatorname*{argmin}_{0 \leq j < M} a_{i,j} \right) $$

を合計で $O(N + M \log N)$ 時間で求める.

## Contents

```Python
Monotone_Minima(N: int, M: int, eval: Callable[[int, int], int]) -> list[int]
```

* Monotone な行列 $A = (a_{i,j})$ に対して, 各 $0 \leq i < N$ に対する $\displaystyle \min \left(\operatorname*{argmin}\_{0 \leq j < M} a_{i,j} \right)$ を求める.
* **引数**
  * $N$: 行数
  * $M$: 列数
  * $\textrm{eval}$: $a_{i,j} = \textrm{eval}(i,j)$ を満たす $2$ 変数関数
* **計算量**
  * $O(N + M \log N)$ 時間
