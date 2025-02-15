---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test_verify/yosupo_library_checker/Convolution/Bitwise_Xor_Convolution.test.py
    title: test_verify/yosupo_library_checker/Convolution/Bitwise_Xor_Convolution.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.13.2/x64/lib/python3.13/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.13.2/x64/lib/python3.13/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def Fast_Walsh_Hadamard_Transform_XOR(A):\n    \"\"\" XOR \u306B\u95A2\u3059\
    \u308B Walsh_Hadamard_Transform \u3092\u884C\u3046.\n\n    A: List\n    \"\"\"\
    \n\n    N=len(A)\n    h=(N-1).bit_length()\n    for k in range(h):\n        bit=1<<k\n\
    \        for i in range(N):\n            if i&bit==0:\n                x=A[i]\n\
    \                y=A[i|bit]\n                A[i]=(x+y)%Mod\n                A[i|bit]=(x-y)%Mod\n\
    \ndef Fast_Inverse_Walsh_Hadamard_Transform_XOR(A):\n    \"\"\" XOR \u306B\u95A2\
    \u3059\u308B\u9006 Walsh_Hadamard_Transform \u3092\u884C\u3046.\n\n    A: List\n\
    \    \"\"\"\n\n    Fast_Walsh_Hadamard_Transform_XOR(A)\n    N_inv=pow(len(A),\
    \ -1, Mod)\n    for i in range(len(A)):\n        A[i] = (A[i] * N_inv) % Mod\n\
    \ndef Convolution_XOR(A,B):\n    \"\"\" XOR \u6F14\u7B97\u306B\u95A2\u3059\u308B\
    \u7573\u8FBC\u307F\u3092\u884C\u3046.\n\n    A,B: List\n    \"\"\"\n\n    N=len(A);\
    \ M=len(B)\n    L=1<<(max(N,M)-1).bit_length()\n\n    if min(N,M)<64:\n      \
    \  C=[0]*L\n        for i in range(N):\n            for j in range(M):\n     \
    \           C[i^j]+=A[i]*B[j]\n                C[i^j]%=Mod\n        return C\n\
    \n    A=A+[0]*(L-N)\n    B=B+[0]*(L-M)\n\n    Fast_Walsh_Hadamard_Transform_XOR(A)\n\
    \    Fast_Walsh_Hadamard_Transform_XOR(B)\n\n    for i in range(N):\n        A[i]*=B[i]\n\
    \        A[i]%=Mod\n\n    Fast_Inverse_Walsh_Hadamard_Transform_XOR(A)\n    return\
    \ A\n\ndef Convolution_Power_XOR(A,k):\n    \"\"\" XOR \u6F14\u7B97\u306B\u95A2\
    \u3059\u308B k \u56DE\u306E\u7573\u8FBC\u307F\u3092\u884C\u3046.\n\n    A,B: List\n\
    \    \"\"\"\n\n    N=len(A)\n    L=1<<(N-1).bit_length()\n\n    A=A+[0]*(L-N)\n\
    \n    Fast_Walsh_Hadamard_Transform_XOR(A)\n\n    A=[pow(A[i],k,Mod) for i in\
    \ range(L)]\n\n    Fast_Inverse_Walsh_Hadamard_Transform_XOR(A)\n    return A\n\
    \nMod=998244353"
  dependsOn: []
  isVerificationFile: false
  path: Convolution/XOR_Convolution.py
  requiredBy: []
  timestamp: '2023-08-06 20:56:34+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test_verify/yosupo_library_checker/Convolution/Bitwise_Xor_Convolution.test.py
documentation_of: Convolution/XOR_Convolution.py
layout: document
title: Xor Convolution
---

## Outline

以降では $N$ を正の整数とし, $(\\!(M)\\!)$ を $N$ 未満の非負整数全体の集合とする. つまり, $(\\!(M)\\!)=\\{0,1,2 \dots, M-1\\}$
である.

長さ $2^N$ の数列 $A=(A_i)\_{0 \leq i \lt 2^N}, B=(B_j)\_{0 \leq j \lt 2^N}$ に対し, $A,B$ の Xor Convolution $A \oplus B$ を

$$A \oplus B:=\left(\sum_{\substack{0 \leq i,j \lt 2^N \\ i ~\oplus~ j=k}} A_i B_j \right)_{0 \leq k \lt 2^N}$$

と定義する.

なお, 写像 $\operatorname{bit}: \mathcal{P}((\\!(N)\\!)) \to (\\!(2^N)\\!)$ を

$$\operatorname{bit}(S):=\sum_{a \in S} 2^a$$

と定義すると, $\operatorname{bit}$ はこの2つモノイド $((\\!(2^N)\\!), \oplus), (\mathcal{P}((\\!(N)\\!)), \triangle)$ 間の同型写像になることから, 次のような言い換えができる.

$A,B$ は添字集合が $\mathcal{P}((\\!(N)\\!))$ である列であるとする.
このとき, $A=(A_S)\_{S \in \mathcal{P}((\\!(N)\\!))}, B=(B_T)\_{T \in \mathcal{P}((\\!(N)\\!))}$ の Xor Convolution $A \oplus B$ を

$$A \oplus B:=\left(\sum_{\substack{S,T \in \mathcal{P}((\!(N)\!)) \\ S \triangle T=U}} A_S B_T \right)_{U \in \mathcal{P}((\!(N)\!))}$$

と定義する.
