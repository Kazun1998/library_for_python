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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.7/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.7/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def More_Zeta_Transform(A):\n    \"\"\" A \u306E\u4EE5\u4E0A\u3092\u8D70\u308B\
    \ Zeta \u5909\u63DB\u3092\u884C\u3046.\n\n    \"\"\"\n    for i in range(len(A)-2,-1,-1):\n\
    \        A[i]=(A[i]+A[i+1])%Mod\n\ndef More_Mobius_Transform(A):\n    \"\"\" A\
    \ \u306E\u4EE5\u4E0B\u3092\u8D70\u308B\u306B\u304A\u3051\u308B Mobius \u5909\u63DB\
    \u3092\u884C\u3046.\n\n    \"\"\"\n\n    for i in range(len(A)-1):\n        A[i]=(A[i]-A[i+1])%Mod\n\
    \ndef Convolution_MIN(A,B):\n    \"\"\" A,B \u306E min \u306B\u304A\u3051\u308B\
    \u7573\u307F\u8FBC\u307F\u3092\u884C\u3046.\n    \"\"\"\n\n    N=len(A); M=len(B)\n\
    \    L=max(N,M)\n\n    A=A+[0]*(L-N)\n    B=B+[0]*(L-M)\n\n    More_Zeta_Transform(A)\n\
    \    More_Zeta_Transform(B)\n\n    for i in range(L):\n        A[i]*=B[i]\n  \
    \      A[i]%=Mod\n\n    More_Mobius_Transform(A)\n    return A\n\ndef Convolution_Power_MIN(A,k):\n\
    \    \"\"\" A \u306E min \u306B\u304A\u3051\u308B k \u56DE\u306E\u7573\u307F\u8FBC\
    \u307F\u3092\u884C\u3046.\n\n    \"\"\"\n    A=A[:]\n    More_Zeta_Transform(A)\n\
    \    A=[pow(a,k,Mod) for a in A]\n    More_Mobius_Transform(A)\n    return A\n\
    \nMod=998244353\n"
  dependsOn: []
  isVerificationFile: false
  path: Convolution/MIN_Convolution.py
  requiredBy: []
  timestamp: '2021-08-29 23:22:42+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Convolution/MIN_Convolution.py
layout: document
title: Min Convolution
---

## Outline

数列 $A=(A_i)_i, B=(B_j)_j$ に対し, $A,B$ の Min Convolution $A \oplus B$ を

$$A \oplus B:=\left(\sum_{\min(i,j)=k} A_i B_j \right)_k$$

と定義する.
