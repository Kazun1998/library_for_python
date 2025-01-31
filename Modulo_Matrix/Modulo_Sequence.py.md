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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.13.1/x64/lib/python3.13/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.13.1/x64/lib/python3.13/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from Modulo_Matrix import *\n\n#\u6F38\u5316\u5F0F\u3068\u884C\u5217\ndef\
    \ Linear_Recurrence_Sequence_Value(p,x,N):\n    \"\"\"\u7DDA\u5F62\u6F38\u5316\
    \u5F0F\u306E\u7B2CN\u9805\u3092\u6C42\u3081\u308B.\n\n    p:\u6F38\u5316\u5F0F\
    \ (d=|p| \u3068\u3059\u308B.)\n    x:\u7B2C0\u9805\u304B\u3089\u7B2C(d-1)\u9805\
    \u307E\u3067\u306E\u5024\n    N:\u7B2CN\u9805\n\n    \u7DDA\u5F62\u6F38\u5316\u5F0F\
    \u306F x[n+d]=p[0]x[n]+p[1]x[n+1]+...+p[d-1]x[n+d-1] \u3068\u3059\u308B.\n   \
    \ \"\"\"\n\n    assert len(p)==len(x)\n    d=len(p)\n\n    if N<d:\n        return\
    \ x[N]\n\n    A=[p[::-1]]\n    for i in range(d-1):\n        A.append([1 if j==i\
    \ else 0 for j in range(d)])\n    A=Modulo_Matrix(A)\n    v=Modulo_Matrix([[y]\
    \ for y in x])\n\n    X=0\n    aa=pow(A,N-d+1).ele[0][::-1]\n\n    for i in range(d):\n\
    \        X+=aa[i]*x[i]\n\n    return X%Mod\n\ndef Linear_Recurrence_Sequence_Matrix(p):\n\
    \    \"\"\"\u7DDA\u5F62\u6F38\u5316\u5F0F\u304B\u3089\u884C\u5217\u3092\u4F5C\u308B\
    .\n\n    p:\u6F38\u5316\u5F0F (d=|p|)\n    Mod:\u6CD5\n\n    \u7DDA\u5F62\u6F38\
    \u5316\u5F0F\u306F x[n+d]=p[0]x[0]+p[1]x[1]+...+p[d-1] x[d-1] \u3068\u3059\u308B\
    .\n    \"\"\"\n\n    A=[p[::-1]]\n    d=len(p)\n    for i in range(d-1):\n   \
    \     A.append([1 if j==i else 0 for j in range(d)])\n    return Modulo_Matrix(A)\n"
  dependsOn: []
  isVerificationFile: false
  path: Modulo_Matrix/Modulo_Sequence.py
  requiredBy: []
  timestamp: '2022-01-16 16:36:55+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Modulo_Matrix/Modulo_Sequence.py
layout: document
redirect_from:
- /library/Modulo_Matrix/Modulo_Sequence.py
- /library/Modulo_Matrix/Modulo_Sequence.py.html
title: Modulo_Matrix/Modulo_Sequence.py
---
