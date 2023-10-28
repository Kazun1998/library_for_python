---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test_verify/yosupo_library_checker/Convolution/Bitwise_And_Convolution.test.py
    title: test_verify/yosupo_library_checker/Convolution/Bitwise_And_Convolution.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.0/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.0/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def Superset_Zeta_Transform(A):\n    \"\"\" A \u306E\u4E0A\u4F4D\u96C6\u5408\
    \u3092\u8D70\u308B Zeta \u5909\u63DB\u3092\u6C42\u3081\u308B.\n\n    A \u306E\u9577\
    \u3055\u306F\u3042\u308B\u6574\u6570 N \u3092\u7528\u3044\u3066, 2^N \u3067\u306A\
    \u304F\u3066\u306F\u306A\u3089\u306A\u3044.\n    \"\"\"\n    N=(len(A)-1).bit_length()\n\
    \    assert 1<<N==len(A), \"\u5217\u306E\u8981\u7D20\u6570\u306F 2^N \u3067\u306A\
    \u304F\u3066\u306F\u306A\u308A\u307E\u305B\u3093.\"\n\n    for i in range(N):\n\
    \        bit=1<<i\n        for S in range(1<<N):\n            if not(S & bit):\n\
    \                A[S]+=A[S|bit]\n                A[S]%=Mod\n\ndef Superset_Mobius_Transform(A):\n\
    \    \"\"\" A \u306E\u4E0A\u4F4D\u96C6\u5408\u3092\u8D70\u308B Mobius \u5909\u63DB\
    \u3092\u6C42\u3081\u308B.\n\n    A \u306E\u9577\u3055\u306F\u3042\u308B\u6574\u6570\
    \ N \u3092\u7528\u3044\u3066, 2^N \u3067\u306A\u304F\u3066\u306F\u306A\u3089\u306A\
    \u3044.\n    \"\"\"\n\n    N=(len(A)-1).bit_length()\n    assert 1<<N==len(A),\
    \ \"\u5217\u306E\u8981\u7D20\u6570\u306F 2^N \u3067\u306A\u304F\u3066\u306F\u306A\
    \u308A\u307E\u305B\u3093.\"\n\n    for i in range(N):\n        bit=1<<i\n    \
    \    for S in range(1<<N):\n            if not (S & bit):\n                A[S]-=A[S|bit]\n\
    \                A[S]%=Mod\n\ndef Convolution_AND(A,B):\n    \"\"\" AND \u6F14\
    \u7B97\u306B\u95A2\u3059\u308B\u7573\u8FBC\u307F\u3092\u884C\u3046.\n\n    A,B:\
    \ List\n    \"\"\"\n\n    N=len(A); M=len(B)\n    L=1<<(max(N,M)-1).bit_length()\n\
    \n    if min(N,M)<64:\n        C=[0]*L\n        for i in range(N):\n         \
    \   for j in range(M):\n                C[i&j]+=A[i]*B[j]\n                C[i&j]%=Mod\n\
    \        return C\n\n    A=A+[0]*(L-N)\n    B=B+[0]*(L-M)\n\n    Superset_Zeta_Transform(A)\n\
    \    Superset_Zeta_Transform(B)\n\n    for i in range(N):\n        A[i]*=B[i]\n\
    \        A[i]%=Mod\n\n    Superset_Mobius_Transform(A)\n    return A\n\ndef Convolution_Power_AND(A,k):\n\
    \    \"\"\" AND \u6F14\u7B97\u306B\u95A2\u3059\u308B k \u56DE\u306E\u7573\u8FBC\
    \u307F\u3092\u884C\u3046.\n\n    A: List\n    \"\"\"\n\n    N=len(A)\n    L=1<<(N-1).bit_length()\n\
    \n    A=A+[0]*(L-N)\n\n    Superset_Zeta_Transform(A)\n\n    A=[pow(A[i],k,Mod)\
    \ for i in range(L)]\n\n    Superset_Mobius_Transform(A)\n    return A\n\nMod=998244353"
  dependsOn: []
  isVerificationFile: false
  path: Convolution/AND_Convolution.py
  requiredBy: []
  timestamp: '2022-10-03 22:52:26+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test_verify/yosupo_library_checker/Convolution/Bitwise_And_Convolution.test.py
documentation_of: Convolution/AND_Convolution.py
layout: document
title: And Convolution
---

## Outline

以降では $N$ を正の整数とし, $(\\!(M)\\!)$ を $N$ 未満の非負整数全体の集合とする. つまり, $(\\!(M)\\!)=\\{0,1,2 \dots, M-1\\}$
である.

長さ $2^N$ の数列 $A=(A_i)\_{0 \leq i \lt 2^N}, B=(B_j)\_{0 \leq j \lt 2^N}$ に対し, $A,B$ の And Convolution $A \oplus B$ を

$$A \oplus B:=\left(\sum_{\substack{0 \leq i,j \lt 2^N \\ i ~\land~ j=k}} A_i B_j \right)_{0 \leq k \lt 2^N}$$

と定義する.

なお, 写像 $\operatorname{bit}: \mathcal{P}((\\!(N)\\!)) \to (\\!(2^N)\\!)$ を

$$\operatorname{bit}(S):=\sum_{a \in S} 2^a$$

と定義すると, $\operatorname{bit}$ はこの2つモノイド $((\\!(2^N)\\!), \land), (\mathcal{P}((\\!(N)\\!)), \cap)$ 間の同型写像になることから, 次のような言い換えができる.

$A,B$ は添字集合が $\mathcal{P}((\\!(N)\\!))$ である列であるとする.
このとき, $A=(A_S)\_{S \in \mathcal{P}((\\!(N)\\!))}, B=(B_T)\_{T \in \mathcal{P}((\\!(N)\\!))}$ の And Convolution $A \oplus B$ を

$$A \oplus B:=\left(\sum_{\substack{S,T \in \mathcal{P}((\!(N)\!)) \\ S \cap T=U}} A_S B_T \right)_{U \in \mathcal{P}((\!(N)\!))}$$

と定義する.
