---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test_verify/Gcd_Convolution.test.py
    title: test_verify/Gcd_Convolution.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def Multiple_Zeta_Transform(A):\n    \"\"\" A \u306E\u500D\u6570\u3092\u8D70\
    \u308B\u306B\u304A\u3051\u308B Zeta \u5909\u63DB\u3092\u884C\u3046.\n\n    \u203B\
    \ A[0] \u306E\u5024\u306F\u7121\u8996\u3055\u308C\u308B.\n    \"\"\"\n\n    N=len(A)-1\n\
    \    S=[1]*(N+1)\n\n    for p in range(2,N+1):\n        if S[p]:\n           \
    \ for k in range(N//p,0,-1):\n                S[k*p]=0\n                A[k]+=A[k*p]\n\
    \n    for i in range(1,N+1):\n        A[i]%=Mod\n\ndef Multiple_Mobius_Transform(A):\n\
    \    \"\"\" A \u306E\u7D04\u6570\u306B\u304A\u3051\u308B Mobius \u5909\u63DB\u3092\
    \u884C\u3046.\n\n    \u203B A[0] \u306E\u5024\u306F\u7121\u8996\u3055\u308C\u308B\
    .\n    \"\"\"\n\n    N=len(A)-1\n    S=[1]*(N+1)\n\n    for p in range(2,N+1):\n\
    \        if S[p]:\n            for k in range(1,N//p+1):\n                S[k*p]=0\n\
    \                A[k]-=A[k*p]\n\n    for i in range(1,N+1):\n        A[i]%=Mod\n\
    \ndef Convolution_GCD(A,B):\n    \"\"\" A,B \u306E gcd \u306B\u304A\u3051\u308B\
    \u7573\u307F\u8FBC\u307F\u3092\u884C\u3046.\n\n    \u203B A[0], B[0] \u306E\u5024\
    \u306F\u7121\u8996\u3055\u308C\u308B.\n    \"\"\"\n\n    N=len(A)-1; M=len(B)-1;\
    \ L=max(N,M)\n\n    A=A+[0]*(L-N)\n    B=B+[0]*(L-M)\n\n    Multiple_Zeta_Transform(A)\n\
    \    Multiple_Zeta_Transform(B)\n\n    for i in range(1,L+1):\n        A[i]*=B[i]\n\
    \        A[i]%=Mod\n\n    Multiple_Mobius_Transform(A)\n    return A\n\ndef Convolution_Power_GCD(A,k):\n\
    \    \"\"\" A \u306E gcd \u306B\u304A\u3051\u308B k \u56DE\u306E\u7573\u307F\u8FBC\
    \u307F\u3092\u884C\u3046.\n\n    \u203B A[0] \u306E\u5024\u306F\u7121\u8996\u3055\
    \u308C\u308B.\n    \"\"\"\n\n    A=A[:]\n    Multiple_Zeta_Transform(A)\n    A=[pow(a,k,Mod)\
    \ for a in A]\n    Multiple_Mobius_Transform(A)\n    return A\n\nMod=998244353\n"
  dependsOn: []
  isVerificationFile: false
  path: Convolution/GCD_Convolution.py
  requiredBy: []
  timestamp: '2021-08-29 23:22:42+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test_verify/Gcd_Convolution.test.py
documentation_of: Convolution/GCD_Convolution.py
layout: document
title: Gcd Convolution
---

## Outline

数列 $A=(A_i)\_{1 \leq i}, B=(B_j)\_{1 \leq j}$ に対し, $A,B$ の Gcd Convolution $A \oplus B$ を

$$A \oplus B:=\left(\sum_{\substack{1 \leq i,j \\ \gcd(i,j)=k}} A_i B_j \right)_{1 \leq k}$$

と定義する.

## Remark

実装において, 長さが $N$ の数列を使いたい場合, プログラム言語の仕様上, 初項が第 $0$ 項になるため, 長さ $(N+1)$ のリストを入力しなければならない.

ただし, 第 $0$ 項は無視して計算される.
