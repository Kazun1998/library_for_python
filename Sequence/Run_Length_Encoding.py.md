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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.14.2/x64/lib/python3.14/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.14.2/x64/lib/python3.14/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def Run_Length_Encoding(S):\n    \"\"\" Run Length \u5727\u7E2E\n\n    S:\
    \ \u5217\n    \"\"\"\n    if not S:\n        return []\n\n    R=[[S[0],1]]\n\n\
    \    for i in range(1,len(S)):\n        if R[-1][0]==S[i]:\n            R[-1][1]+=1\n\
    \        else:\n            R.append([S[i],1])\n\n    return R\n\ndef Alternating_Length_Encoding(S,\
    \ first, second, equal = True) -> tuple[list[int], list[int]]:\n    \"\"\" \u30A2\
    \u30EB\u30D5\u30A1\u30D9\u30C3\u30C8\u30B5\u30A4\u30BA\u304C 2 \u3067\u3042\u308B\
    \u5217 S \u306B\u5BFE\u3057\u3066, \u6700\u521D\u306B\u73FE\u308C\u308B first\
    \ \u3068\u6B8B\u308A\u306E second \u306B\u3064\u3044\u3066, \u305D\u308C\u305E\
    \u308C\u304C\u9023\u7D9A\u3057\u3066\u73FE\u308C\u308B\u56DE\u6570\u306E\u30EA\
    \u30B9\u30C8\u3092\u6C42\u3081\u308B.\n\n    Args:\n        S: \u5217\n      \
    \  first: \u6700\u521D\u306B\u73FE\u308C\u308B\u6587\u5B57\n        second: \u6B21\
    \u306B\u73FE\u308C\u308B\u6587\u5B57\n        equal (bool, optional): True \u306B\
    \u3059\u308B\u3068, \u8FD4\u308A\u5024\u306B\u304A\u3051\u308B 2 \u3064\u306E\u914D\
    \u5217\u306E\u9577\u3055\u304C\u7B49\u3057\u304F\u306A\u308B. Defaults to True.\n\
    \n    Returns:\n        tuple[list[int], list[int]]: X, Y \u3092\u6574\u6570\u306E\
    \u30EA\u30B9\u30C8\u3068\u3057\u305F\u30BF\u30D7\u30EB (X, Y). \u3053\u308C\u306F\
    \u4EE5\u4E0B\u3092\u610F\u5473\u3059\u308B.\n            * S = (first \u304C\u9023\
    \u7D9A\u3057\u3066 X[0] \u500B)(second \u304C\u9023\u7D9A\u3057\u3066 Y[0] \u500B\
    )(first \u304C\u9023\u7D9A\u3057\u3066 X[1] \u500B)(second \u304C\u9023\u7D9A\u3057\
    \u3066 Y[1] \u500B)...\n    \"\"\"\n    x: list[int] = []\n    y: list[int] =\
    \ []\n\n    if S[0] == second:\n        x.append(0)\n\n    for a, k in Run_Length_Encoding(S):\n\
    \        if a == first:\n            x.append(k)\n        else:\n            y.append(k)\n\
    \n    if equal and len(x) > len(y):\n        y.append(0)\n\n    return x, y\n"
  dependsOn: []
  isVerificationFile: false
  path: Sequence/Run_Length_Encoding.py
  requiredBy: []
  timestamp: '2025-07-27 21:16:37+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Sequence/Run_Length_Encoding.py
layout: document
title: Run Length Encoding
---

## Outline

$\mathcal{A}$ をアルファベットする. 長さ $N$ の $\mathcal{A}$ の列 $S=(S\_i)\_{i=1}^N$ に対して, 以下を満たすような列 $T=((\alpha\_j, k\_j))\_{j=1}^M$ を求める.

* $\forall j=1,2, \dots, M;~\alpha \in \mathcal{A}, k_j \geq 0$.
* $\forall j=1,2, \dots, M-1;~\alpha_j \neq \alpha_{j+1}$
* $S=(\underbrace{\alpha_1, \dots, \alpha_1}\_{k_1}, \dots, \underbrace{\alpha_M, \dots, \alpha_M}\_{k_M})$

このような $T$ を $S$ の Run Length Encoding (連長圧縮) という. なお, RLE は一意に定まる.
