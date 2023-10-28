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
  code: "#\u7D04\u6570\u306EK\u4E57\u548C\ndef Divisor_Sigma(N, K=1):\n    if N==1:\n\
    \        return 1\n\n    R=1\n    p=2\n    while p*p<=N:\n        if N%p==0:\n\
    \            e=0\n            while N%p==0:\n                N//=p\n         \
    \       e+=1\n\n            if K:\n                s=pow(p,K)\n              \
    \  R*=(pow(s,e+1)-1)//(s-1)\n            else:\n                R*=e+1\n     \
    \   p+=1\n\n    if N>1:\n        R*=pow(N,K)+1\n\n    return R\n"
  dependsOn: []
  isVerificationFile: false
  path: Integer/Summation.py
  requiredBy: []
  timestamp: '2023-03-18 02:55:12+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Integer/Summation.py
layout: document
redirect_from:
- /library/Integer/Summation.py
- /library/Integer/Summation.py.html
title: Integer/Summation.py
---
