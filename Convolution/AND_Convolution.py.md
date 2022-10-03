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
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Convolution/AND_Convolution.py
layout: document
redirect_from:
- /library/Convolution/AND_Convolution.py
- /library/Convolution/AND_Convolution.py.html
title: Convolution/AND_Convolution.py
---
