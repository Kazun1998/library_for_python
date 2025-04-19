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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.13.3/x64/lib/python3.13/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.13.3/x64/lib/python3.13/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "#\u30EC\u30FC\u30D9\u30F3\u30B7\u30E5\u30BF\u30A4\u30F3\u8DDD\u96E2\ndef\
    \ Levenshtein_Distance(S, T):\n    \"\"\" S,T \u306B\u304A\u3051\u308B\u30EC\u30FC\
    \u30D9\u30F3\u30B7\u30E5\u30BF\u30A4\u30F3\u8DDD\u96E2 (\u7DE8\u96C6\u8DDD\u96E2\
    ) \u3092\u6C42\u3081\u308B.\n\n    \"\"\"\n\n    M=len(S); N=len(T)\n    DP=[[0]*(N+1)\
    \ for _ in range(M+1)]\n\n    for i in range(1,M+1):\n        D=DP[i]\n      \
    \  E=DP[i-1]\n        for j in range(1,N+1):\n            if S[i-1]==T[j-1]:\n\
    \                D[j]=min(D[j-1]+1, E[j]+1, E[j-1])\n            else:\n     \
    \           D[j]=min(D[j-1], E[j], E[j-1])+1\n\n    return D[-1]\n"
  dependsOn: []
  isVerificationFile: false
  path: Sequence/Levenshtein_Distance.py
  requiredBy: []
  timestamp: '2022-11-26 03:55:08+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Sequence/Levenshtein_Distance.py
layout: document
redirect_from:
- /library/Sequence/Levenshtein_Distance.py
- /library/Sequence/Levenshtein_Distance.py.html
title: Sequence/Levenshtein_Distance.py
---
