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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.13.2/x64/lib/python3.13/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.13.2/x64/lib/python3.13/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "#\u6CD5 p \u306E\u539F\u59CB\u6839\ndef Primitive_Root(p):\n    \"\"\"Z/pZ\u4E0A\
    \u306E\u539F\u59CB\u6839\u3092\u898B\u3064\u3051\u308B\n    p:\u7D20\u6570\n \
    \   \"\"\"\n    if p==2:\n        return 1\n    if p==998244353:\n        return\
    \ 3\n    if p==10**9+7:\n        return 5\n    fac=[]\n    q=2\n    v=p-1\n  \
    \  while v>=q*q:\n        e=0\n        while v%q==0:\n            e+=1\n     \
    \       v//=q\n        if e>0:\n            fac.append(q)\n        q+=1\n    if\
    \ v>1:\n        fac.append(v)\n    g=2\n    while g<p:\n        if pow(g,p-1,p)!=1:\n\
    \            return None\n        flag=True\n        for q in fac:\n         \
    \   if pow(g,(p-1)//q,p)==1:\n                flag=False\n                break\n\
    \        if flag:\n            return g\n\n        g+=1\n\n\ndef Modulo_Inverse(a,\
    \ m):\n    \"\"\" (mod m) \u306B\u304A\u3051\u308B\u9006\u5143\u3092\u6C42\u3081\
    \u308B.\n    Args:\n        a (int): mod m \u306E\u5143\n        m (int): \u6CD5\
    \n    Returns:\n        int: \u53EF\u9006\u5143\u304C\u5B58\u5728\u3059\u308B\u306A\
    \u3089\u3070\u305D\u306E\u5024, \u5B58\u5728\u3057\u306A\u3044\u306E\u3067\u3042\
    \u308C\u3070 -1\n    \"\"\"\n    try:\n        return pow(a, -1, m)\n    except\
    \ ValueError:\n        return -1"
  dependsOn: []
  isVerificationFile: false
  path: Integer/Modulo.py
  requiredBy: []
  timestamp: '2023-08-20 10:06:28+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Integer/Modulo.py
layout: document
redirect_from:
- /library/Integer/Modulo.py
- /library/Integer/Modulo.py.html
title: Integer/Modulo.py
---
