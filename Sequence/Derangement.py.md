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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def Derangement_List(N,Mod=None):\n    \"\"\" k=0,1,...,N \u306B\u95A2\u3057\
    \u3066, k \u8981\u7D20\u64B9\u4E71\u9806\u5217\u306E\u500B\u6570\u3092\u6C42\u3081\
    \u308B.\n    \"\"\"\n    if N<0:\n        return []\n    elif N==0:\n        return\
    \ [0]\n    elif N==1:\n        return [0,0]\n    elif Mod==1:\n        return\
    \ [0]*(N+1)\n\n    X=[0]*(N+1)\n    if Mod==None:\n        X[2]=1\n        for\
    \ k in range(3,N+1):\n            X[k]=(k-1)*(X[k-1]+X[k-2])\n    else:\n    \
    \    X[2]=1%Mod\n        for k in range(3,N+1):\n            X[k]=(k-1)*(X[k-1]+X[k-2])%Mod\n\
    \n    return X\n\n"
  dependsOn: []
  isVerificationFile: false
  path: Sequence/Derangement.py
  requiredBy: []
  timestamp: '2022-11-25 03:29:15+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Sequence/Derangement.py
layout: document
redirect_from:
- /library/Sequence/Derangement.py
- /library/Sequence/Derangement.py.html
title: Sequence/Derangement.py
---
