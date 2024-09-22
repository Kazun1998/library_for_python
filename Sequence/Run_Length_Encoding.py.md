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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.6/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.6/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def Run_Length_Encoding(S):\n    \"\"\" Run Length \u5727\u7E2E\n\n    S:\
    \ \u5217\n    \"\"\"\n    if not S:\n        return []\n\n    R=[[S[0],1]]\n\n\
    \    for i in range(1,len(S)):\n        if R[-1][0]==S[i]:\n            R[-1][1]+=1\n\
    \        else:\n            R.append([S[i],1])\n\n    return R\n"
  dependsOn: []
  isVerificationFile: false
  path: Sequence/Run_Length_Encoding.py
  requiredBy: []
  timestamp: '2022-11-26 03:55:08+09:00'
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
