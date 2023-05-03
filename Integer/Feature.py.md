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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.3/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.3/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "#\u5E73\u65B9\u6570?\ndef Is_Square_Number(N):\n    if N<0:\n        return\
    \ False\n    elif N==0:\n        return True\n\n    for p in [2,3]:\n        F=0\n\
    \        while N%p==0:\n            F^=1\n            N//=p\n        if F:\n \
    \           return False\n\n    k=5\n    Flag=1\n    while k*k<=N:\n        F=0\n\
    \        while N%k==0:\n            F^=1\n            N//=k\n        if F:\n \
    \           return False\n        k+=2 if Flag else 4\n    return N==1\n\n#\u7ACB\
    \u65B9\u6570?\ndef Is_Cubic_Number(N):\n    if N<0:\n        return False\n  \
    \  elif N==0:\n        return True\n\n    for p in [2,3]:\n        F=0\n     \
    \   while N%p==0:\n            F+=1\n            N//=p\n        if F%3:\n    \
    \        return False\n\n    k=5\n    Flag=1\n    while k*k<=N:\n        F=0\n\
    \        while N%k==0:\n            F+=1\n            N//=k\n        if F%3:\n\
    \            return False\n        k+=2 if Flag else 4\n    return N==1\n\n#\u5B8C\
    \u5168\u6570?\ndef Is_Perfect(N):\n    n=N\n    S=1\n    p=2\n    while p*p<=n:\n\
    \        if n%p==0:\n            e=0\n            while n%p==0:\n            \
    \    n//=p\n                e+=1\n\n            S*=(pow(p,e+1)-1)//(p-1)\n   \
    \     p+=1\n\n    if n>1:\n        S*=n+1\n\n    return 2*N==S\n"
  dependsOn: []
  isVerificationFile: false
  path: Integer/Feature.py
  requiredBy: []
  timestamp: '2023-03-18 02:55:12+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Integer/Feature.py
layout: document
redirect_from:
- /library/Integer/Feature.py
- /library/Integer/Feature.py.html
title: Integer/Feature.py
---
