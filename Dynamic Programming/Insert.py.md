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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.8/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.8/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def Increase_Decrease_Permutation(N,T,Mod):\n    \"\"\" \u9577\u3055\u304C\
    \ N \u306E\u9806\u5217\u306E\u3046\u3061, \u4EE5\u4E0B\u3092\u6E80\u305F\u3059\
    \u3088\u3046\u306A\u9806\u5217 P \u306E\u7DCF\u6570\u3092 Mod \u3067\u5272\u3063\
    \u305F\u4F59\u308A\u3092\u51FA\u529B\u3059\u308B:\n    T[i]=1 -> P[i]<P[i+1],\
    \ T[i]=-1 -> P[i]>P[i+1], T[i]=0 -> (\u7279\u306B\u306A\u3057)\n\n    N: int\n\
    \    T: list (|T|=N-1)\n    Mod: int\n    \"\"\"\n\n    assert len(T)==N-1\n \
    \   from itertools import accumulate\n\n    DP=[1]*N\n\n    for i in range(1,N):\n\
    \        if Mod!=None:\n            Cum=list(accumulate(DP,lambda x,y:(x+y)%Mod))\n\
    \        else:\n            Cum=list(accumulate(DP))\n\n        if T[i-1]==1:\n\
    \            for m in range(N-i):\n                DP[m]=Cum[m]\n        elif\
    \ T[i-1]==0:\n            for m in range(N-i):\n                DP[m]=Cum[N-i]\n\
    \        else:\n            for m in range(N-i-1,-1,-1):\n                DP[m]=Cum[N-i]-Cum[m]\n\
    \        for m in range(N-i,N):\n            DP[m]=0\n\n    return DP[0]%Mod\n"
  dependsOn: []
  isVerificationFile: false
  path: Dynamic Programming/Insert.py
  requiredBy: []
  timestamp: '2021-09-12 03:07:51+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Dynamic Programming/Insert.py
layout: document
redirect_from:
- /library/Dynamic Programming/Insert.py
- /library/Dynamic Programming/Insert.py.html
title: Dynamic Programming/Insert.py
---
