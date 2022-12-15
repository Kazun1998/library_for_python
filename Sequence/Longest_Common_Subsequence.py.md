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
  code: "#\u6700\u9577\u90E8\u5206\u5217\ndef Longest_Common_Subsequence(S, T, example=False):\n\
    \    \"\"\" \u5217 S,T \u306B\u304A\u3051\u308B\u6700\u9577\u90E8\u5206\u5217\u306E\
    \u9577\u3055\u3092\u6C42\u3081\u308B.\n\n    example: True \u3067\u3042\u308B\u3068\
    \u304D, LCS \u3092\u6E80\u305F\u3059\u4F8B\u30921\u3064\u8FD4\u3059.\n    \"\"\
    \"\n\n    M=len(S); N=len(T)\n    DP=[[0]*(N+1) for _ in range(M+1)]\n\n    for\
    \ i in range(1,M+1):\n        D=DP[i]\n        E=DP[i-1]\n        for j in range(1,N+1):\n\
    \            if S[i-1]==T[j-1]:\n                D[j]=E[j-1]+1\n            else:\n\
    \                if E[j]>=D[j-1]:\n                    D[j]=E[j]\n           \
    \     else:\n                    D[j]=D[j-1]\n\n    if not example:\n        return\
    \ D[-1]\n\n    X=[]\n    I,J=M,N\n    D=DP[I]; E=DP[I-1]\n    while D[J]:\n  \
    \      if S[I-1]==T[J-1]:\n            X.append(S[I-1])\n            I-=1; J-=1\n\
    \            D=DP[I]\n            E=DP[I-1]\n        else:\n            if D[J]==D[J-1]:\n\
    \                J-=1\n            else:\n                I-=1\n             \
    \   D=DP[I]\n                E=DP[I-1]\n\n    return DP[-1][-1], X[::-1]\n"
  dependsOn: []
  isVerificationFile: false
  path: Sequence/Longest_Common_Subsequence.py
  requiredBy: []
  timestamp: '2022-11-26 03:55:08+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Sequence/Longest_Common_Subsequence.py
layout: document
redirect_from:
- /library/Sequence/Longest_Common_Subsequence.py
- /library/Sequence/Longest_Common_Subsequence.py.html
title: Sequence/Longest_Common_Subsequence.py
---
