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
  code: "#\u6700\u9577\u90E8\u5206\u5217\ndef Longest_Common_Subsequence(S, T, example=False):\n\
    \    \"\"\" \u5217 S,T \u306B\u304A\u3051\u308B\u6700\u9577\u90E8\u5206\u5217\u306E\
    \u9577\u3055\u3092\u6C42\u3081\u308B.\n\n    example: True \u3067\u3042\u308B\u3068\
    \u304D, LCS \u3092\u6E80\u305F\u3059\u4F8B\u30921\u3064\u8FD4\u3059.\n    \"\"\
    \"\n\n    M=len(S); N=len(T)\n    DP=[[0]*(N+1) for _ in range(M+1)]\n\n    for\
    \ i in range(1,M+1):\n        D=DP[i]\n        E=DP[i-1]\n        for j in range(1,N+1):\n\
    \            if S[i-1]==T[j-1]:\n                D[j]=E[j-1]+1\n            else:\n\
    \                if E[j]>=D[j-1]:\n                    D[j]=E[j]\n           \
    \     else:\n                    D[j]=D[j-1]\n\n    if not example:\n        return\
    \ D[-1]\n\n    X=[]\n    I,J=M,N\n    D=DP[I]; E=DP[I-1]\n    while D[J]:\n  \
    \      if S[I-1]==T[J-1]:\n            X.append(S[I-1])\n            I-=1; J-=1\n\
    \            D=DP[I]\n            E=DP[I-1]\n        else:\n            if D[J]==D[J-1]:\n\
    \                J-=1\n            else:\n                I-=1\n             \
    \   D=DP[I]\n                E=DP[I-1]\n\n    return DP[-1][-1], X[::-1]\n"
  dependsOn: []
  isVerificationFile: false
  path: Sequence/Longest_Common_Subsequence.py
  requiredBy: []
  timestamp: '2022-11-26 03:55:08+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Sequence/Longest_Common_Subsequence.py
layout: document
title: "Longest Common Subsequence (\u6700\u9577\u5171\u901A\u90E8\u5206\u5217)"
---

## Outline

2つの列 $S,T$ に対する最長共通部分や, その長さを求める.

## Theory

$\mathcal{A}$ をアルファベットとする. $S \in W(\mathcal{A})$ に対して, 以下を満たすような正の整数列 $\rho$ が存在するとき, $T \in W(\mathcal{A})$ は $S$ の部分列であるという.

* $\rho$ は長さ $\lvert T \rvert$ の列.
* $1 \leq \rho(1) \lt \rho(2) \lt \dots \lt \rho(\lvert T \rvert) \leq \lvert S \rvert$.
* $i=1,2, \dots, \lvert T \rvert$ に対して, $S_{\rho(i)}=T_i$ が成り立つ.

2つの列 $S,T \in W(\mathcal{A})$ に対して, $S,T$ 両方の部分列であるような列のことを $S,T$ の共通部分列という.

$S,T$ の共通部分列のうち, 長さが最大であるようなものを最長共通部分列という (存在はするが, 一意とは限らない).

$S,T$ の最長共通部分列の長さは以下のようにして動的計画法で求めることができる.

${\rm DP}[i,j]$ を $S[1:i], T[1:j]$ の最長共通部分列の長さとする. 自明なケースとして,

$${\rm DP}[0,j]=0 \quad (0 \leq j \leq \lvert T \rvert), \quad {\rm DP}[i,0]=0 \quad (0 \leq i \leq \lvert S \rvert)$$

である.

また, 更新式は次のようになる.

$${\rm DP}[i,j]=\begin{cases} {\rm DP}[i-1, j-1]+1 & (S_i=T_j) \\ \max ({\rm DP}[i-1,j], {\rm DP}[i, j-1]) & (S_i \neq T_j) \end{cases}$$

この動的計画法によって, ${\rm DP}[\lvert S \rvert, \lvert T \rvert]$ が $S,T$ の最長共通部分列の長さになる.
