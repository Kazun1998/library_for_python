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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.5/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.5/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def Subset_Sum_Zero_One(A, S, Mod=None, mode=False):\n    \"\"\" A \u306E\
    \u591A\u91CD\u90E8\u5206\u96C6\u5408\u3067, \u548C\u304C S \u306B\u306A\u308B\u6570\
    \u3092\u6C42\u3081\u308B.\n\n    Mod: \u4F59\u308A\n    mode: True \u306A\u3089\
    \u3070 0,1,2,...,S \u306E\u5834\u5408\u5168\u3066, false \u306A\u3089\u3070 S\
    \ \u306E\u307F\n\n    \u8A08\u7B97\u91CF: O(|A| S)\n    \"\"\"\n\n    DP=[0]*(S+1);\
    \ DP[0]=1\n    T=0\n\n    for a in A:\n        T+=a\n        for x in range(min(S,T),a-1,-1):\n\
    \            DP[x]+=DP[x-a]\n\n        if Mod!=None:\n            for i in range(a,min(S,T)+1):\n\
    \                DP[i]%=Mod\n\n    if mode:\n        return DP\n    else:\n  \
    \      return DP[S]\n\ndef Subset_Sum_Plus_Minus_One(A, K, Mod=None):\n    \"\"\
    \" \u4EE5\u4E0B\u3092\u6E80\u305F\u3059 A \u306E\u5206\u5272 X,Y \u306E\u500B\u6570\
    \u3092\u6C42\u3081\u308B: sum(X)-sum(Y)=K.\n\n    \u8A08\u7B97\u91CF: O(N(sum(A)+K))\n\
    \    \"\"\"\n\n    L=K+sum(abs(a) for a in A)\n    if L<0 or L%2==1:\n       \
    \ return 0\n\n    B=[abs(a) for a in A]\n    return Subset_Sum_Zero_One(B, L//2,\
    \ Mod)\n"
  dependsOn: []
  isVerificationFile: false
  path: Subset_Sum.py
  requiredBy: []
  timestamp: '2023-05-20 13:42:48+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Subset_Sum.py
layout: document
redirect_from:
- /library/Subset_Sum.py
- /library/Subset_Sum.py.html
title: Subset_Sum.py
---
