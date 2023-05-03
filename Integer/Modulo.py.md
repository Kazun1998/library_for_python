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
  code: "#\u6CD5 p \u306E\u539F\u59CB\u6839\ndef Primitive_Root(p):\n    \"\"\"Z/pZ\u4E0A\
    \u306E\u539F\u59CB\u6839\u3092\u898B\u3064\u3051\u308B\n\n    p:\u7D20\u6570\n\
    \    \"\"\"\n    if p==2:\n        return 1\n    if p==998244353:\n        return\
    \ 3\n    if p==10**9+7:\n        return 5\n\n    fac=[]\n    q=2\n    v=p-1\n\n\
    \    while v>=q*q:\n        e=0\n        while v%q==0:\n            e+=1\n   \
    \         v//=q\n\n        if e>0:\n            fac.append(q)\n        q+=1\n\n\
    \    if v>1:\n        fac.append(v)\n\n    g=2\n    while g<p:\n        if pow(g,p-1,p)!=1:\n\
    \            return None\n\n        flag=True\n        for q in fac:\n       \
    \     if pow(g,(p-1)//q,p)==1:\n                flag=False\n                break\n\
    \n        if flag:\n            return g\n\n        g+=1\n\n#\u62E1\u5F35\u30E6\
    \u30FC\u30AF\u30EA\u30C3\u30C9\u306E\u4E92\u9664\u6CD5\ndef Extend_Euclid(a: int,\
    \ b: int):\n    \"\"\" gcd(a,b) \u3068 ax+by=gcd(a,b) \u3092\u6E80\u305F\u3059\
    \u6574\u6570 x,y \u306E\u4F8B\u3092\u6319\u3052\u308B.\n\n    [Input]\n    a,b:\
    \ \u6574\u6570\n\n    [Output]\n    (x,y,gcd(a,b))\n    \"\"\"\n    s,t,u,v=1,0,0,1\n\
    \    while b:\n        q,a,b=a//b,b,a%b\n        s,t=t,s-q*t\n        u,v=v,u-q*v\n\
    \    return s,u,a\n\n\ndef Modulo_Inverse(a, m):\n    \"\"\" (mod m) \u306B\u304A\
    \u3051\u308B\u9006\u5143\u3092\u6C42\u3081\u308B.\n\n    Args:\n        a (int):\
    \ mod m \u306E\u5143\n        m (int): \u6CD5\n\n    Returns:\n        int: \u53EF\
    \u9006\u5143\u304C\u5B58\u5728\u3059\u308B\u306A\u3089\u3070\u305D\u306E\u5024\
    , \u5B58\u5728\u3057\u306A\u3044\u306E\u3067\u3042\u308C\u3070 -1\n    \"\"\"\n\
    \n    h=Extend_Euclid(a,m)\n    return h[0]%m if h[2]==1 else -1\n\n"
  dependsOn: []
  isVerificationFile: false
  path: Integer/Modulo.py
  requiredBy: []
  timestamp: '2023-03-18 02:55:12+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Integer/Modulo.py
layout: document
redirect_from:
- /library/Integer/Modulo.py
- /library/Integer/Modulo.py.html
title: Integer/Modulo.py
---
