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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.1/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.1/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def Subset_Zeta_Transform(A):\n    \"\"\" A \u306E\u90E8\u5206\u96C6\u5408\
    \u306B\u95A2\u3059\u308B Zeta \u5909\u63DB\u3092\u6C42\u3081\u308B.\n\n    A \u306E\
    \u9577\u3055\u306F\u3042\u308B\u6574\u6570 N \u3092\u7528\u3044\u3066, 2^N \u3067\
    \u306A\u304F\u3066\u306F\u306A\u3089\u306A\u3044.\n    \"\"\"\n\n    N=(len(A)-1).bit_length()\n\
    \    assert 1<<N==len(A), \"\u5217\u306E\u8981\u7D20\u6570\u306F 2^N \u3067\u306A\
    \u304F\u3066\u306F\u306A\u308A\u307E\u305B\u3093.\"\n\n    for i in range(N):\n\
    \        b=1<<i\n        for S in range(1<<N):\n            if (S & b):\n    \
    \            A[S]+=A[S^b]\n\n        for S in range(1<<N):\n            A[S]%=Mod\n\
    \ndef Subset_Mobius_Transform(A):\n    \"\"\" A \u306E\u90E8\u5206\u96C6\u5408\
    \u306B\u95A2\u3059\u308B Mobius \u5909\u63DB\u3092\u6C42\u3081\u308B.\n\n    A\
    \ \u306E\u9577\u3055\u306F\u3042\u308B\u6574\u6570 N \u3092\u7528\u3044\u3066\
    , 2^N \u3067\u306A\u304F\u3066\u306F\u306A\u3089\u306A\u3044.\n    \"\"\"\n\n\
    \    N=(len(A)-1).bit_length()\n    assert 1<<N==len(A), \"\u5217\u306E\u8981\u7D20\
    \u6570\u306F 2^N \u3067\u306A\u304F\u3066\u306F\u306A\u308A\u307E\u305B\u3093\
    .\"\n\n    for i in range(N):\n        b=1<<i\n        for S in range(1<<N):\n\
    \            if (S & b):\n                A[S]-=A[S^b]\n\n        for S in range(1<<N):\n\
    \            A[S]%=Mod\n\n\ndef Convolution_OR(A,B):\n    \"\"\" OR \u6F14\u7B97\
    \u306B\u95A2\u3059\u308B\u7573\u8FBC\u307F\u3092\u884C\u3046.\n\n    A,B: List\n\
    \    \"\"\"\n\n    N=len(A); M=len(B)\n    L=1<<(max(N,M)-1).bit_length()\n\n\
    \    if min(N,M)<64:\n        C=[0]*L\n        for i in range(N):\n          \
    \  for j in range(M):\n                C[i|j]+=A[i]*B[j]\n                C[i|j]%=Mod\n\
    \        return C\n\n    A=A+[0]*(L-N)\n    B=B+[0]*(L-M)\n\n    Subset_Zeta_Transform(A)\n\
    \    Subset_Zeta_Transform(B)\n\n    for i in range(N):\n        A[i]*=B[i]\n\
    \        A[i]%=Mod\n\n    Subset_Mobius_Transform(A)\n    return A\n\ndef Convolution_Power_OR(A,k):\n\
    \    \"\"\" OR \u6F14\u7B97\u306B\u95A2\u3059\u308B k \u56DE\u306E\u7573\u8FBC\
    \u307F\u3092\u884C\u3046.\n\n    A: List\n    \"\"\"\n\n    N=len(A)\n    L=1<<(N-1).bit_length()\n\
    \n    A=A+[0]*(L-N)\n\n    Subset_Zeta_Transform(A)\n\n    A=[pow(A[i],k,Mod)\
    \ for i in range(L)]\n\n    Subset_Mobius_Transform(A)\n    return A\n\nMod=998244353\n"
  dependsOn: []
  isVerificationFile: false
  path: Convolution/OR_Convolution.py
  requiredBy: []
  timestamp: '2021-08-29 23:22:42+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Convolution/OR_Convolution.py
layout: document
title: Or Convolution
---

## Outline

以降では $N$ を正の整数とし, $(\\!(M)\\!)$ を $N$ 未満の非負整数全体の集合とする. つまり, $(\\!(M)\\!)=\\{0,1,2 \dots, M-1\\}$
である.

長さ $2^N$ の数列 $A=(A_i)\_{0 \leq i \lt 2^N}, B=(B_j)\_{0 \leq j \lt 2^N}$ に対し, $A,B$ の Or Convolution $A \oplus B$ を

$$A \oplus B:=\left(\sum_{\substack{0 \leq i,j \lt 2^N \\ i ~\lor~ j=k}} A_i B_j \right)_{0 \leq k \lt 2^N}$$

と定義する.

なお, 写像 $\operatorname{bit}: \mathcal{P}((\\!(N)\\!)) \to (\\!(2^N)\\!)$ を

$$\operatorname{bit}(S):=\sum_{a \in S} 2^a$$

と定義すると, $\operatorname{bit}$ はこの2つモノイド $((\\!(2^N)\\!), \lor), (\mathcal{P}((\\!(N)\\!)), \cup)$ 間の同型写像になることから, 次のような言い換えができる.

$A,B$ は添字集合が $\mathcal{P}((\\!(N)\\!))$ である列であるとする.
このとき, $A=(A_S)\_{S \in \mathcal{P}((\\!(N)\\!))}, B=(B_T)\_{T \in \mathcal{P}((\\!(N)\\!))}$ の Or Convolution $A \oplus B$ を

$$A \oplus B:=\left(\sum_{\substack{S,T \in \mathcal{P}((\!(N)\!)) \\ S \cup T=U}} A_S B_T \right)_{U \in \mathcal{P}((\!(N)\!))}$$

と定義する.
