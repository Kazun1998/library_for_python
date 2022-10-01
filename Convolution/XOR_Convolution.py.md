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
  code: "def Fast_Walsh_Hadamard_Transform_XOR(A):\n    \"\"\" XOR \u306B\u95A2\u3059\
    \u308B Walsh_Hadamard_Transform \u3092\u884C\u3046.\n\n    A: List\n    \"\"\"\
    \n\n    N=len(A)\n    h=(N-1).bit_length()\n    for k in range(h):\n        bit=1<<k\n\
    \        for i in range(N):\n            if i&bit==0:\n                x=A[i]\n\
    \                y=A[i|bit]\n                A[i]=x+y\n                A[i|bit]=x-y\n\
    \        for i in range(N):\n            A[i]%=Mod\n\ndef Fast_Inverse_Walsh_Hadamard_Transform_XOR(A):\n\
    \    \"\"\" XOR \u306B\u95A2\u3059\u308B\u9006 Walsh_Hadamard_Transform \u3092\
    \u884C\u3046.\n\n    A: List\n    \"\"\"\n\n    Fast_Walsh_Hadamard_Transform_XOR(A)\n\
    \    N_inv=pow(len(A),Mod-2,Mod)\n    for i in range(len(A)):\n        A[i]=(A[i]*N_inv)%Mod\n\
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
    \ range(L)]\n\n    Fast_Inverse_Walsh_Hadamard_Transform_XOR(A)\n    return A\n"
  dependsOn: []
  isVerificationFile: false
  path: Convolution/XOR_Convolution.py
  requiredBy: []
  timestamp: '2021-08-18 16:28:38+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Convolution/XOR_Convolution.py
layout: document
redirect_from:
- /library/Convolution/XOR_Convolution.py
- /library/Convolution/XOR_Convolution.py.html
title: Convolution/XOR_Convolution.py
---
