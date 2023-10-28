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
  code: "def Substring_Count(S, Mod=None):\n    \"\"\" \u6587\u5B57\u5217 S \u306E\
    \u7570\u306A\u308B\u9023\u7D9A\u3068\u306F\u9650\u3089\u306A\u3044\u90E8\u5206\
    \u5217\u306E\u500B\u6570\u3092\u6C42\u3081\u308B.\n\n    Mod: \u4F59\u308A\n \
    \   \"\"\"\n\n    #\u524D\u51E6\u7406\n    N=len(S)\n    A=list(set(S))\n    inv_A={A[i]:i\
    \ for i in range(len(A))}\n\n    B=[[N]*len(A) for _ in range(N+1)]\n\n    for\
    \ i in range(N-1,-1,-1):\n        Bi=B[i]; Bii=B[i+1]\n        for j in range(len(A)):\n\
    \            Bi[j]=Bii[j]\n        Bi[inv_A[S[i]]]=i\n\n    #DP\u90E8\n    DP=[0]*(N+1)\n\
    \    if Mod==None:\n        DP[0]=1\n    else:\n        DP[0]=1%Mod\n\n    for\
    \ i in range(N):\n        Bi=B[i]\n        for j in range(len(A)):\n         \
    \   if Bi[j]>=N:\n                continue\n\n            DP[B[i][j]+1]+=DP[i]\n\
    \            if Mod!=None:\n                DP[B[i][j]+1]%=Mod\n    #\u96C6\u8A08\
    \n    if Mod==None:\n        return sum(DP)\n    else:\n        return sum(DP)%Mod\n"
  dependsOn: []
  isVerificationFile: false
  path: String/Substring_Count.py
  requiredBy: []
  timestamp: '2022-12-24 17:50:01+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: String/Substring_Count.py
layout: document
redirect_from:
- /library/String/Substring_Count.py
- /library/String/Substring_Count.py.html
title: String/Substring_Count.py
---
