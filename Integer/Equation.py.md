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
  code: "#\u62E1\u5F35\u30E6\u30FC\u30AF\u30EA\u30C3\u30C9\u306E\u4E92\u9664\u6CD5\
    \ndef Find_Extend_Euclid(a: int, b: int, new = True):\n    \"\"\"ax+by=gcd(a,\
    \ b) \u3092\u6E80\u305F\u3059 (x, y, gcd(a, b)) \u3092 1 \u3064\u6C42\u3081\u308B\
    .\n    a,b:\u6574\u6570\n    \"\"\"\n\n    if new:\n        from math import gcd\n\
    \        g = gcd(a, b)\n        if g == 0:\n            return (1, 0, 0)\n\n \
    \       x = pow(a//g, -1, b//g)\n        y = - (a*x-g) // b\n        return (x,\
    \ y, g)\n    else:\n        s,t,u,v=1,0,0,1\n        while b:\n            q,a,b=a//b,b,a%b\n\
    \            s,t=t,s-q*t\n            u,v=v,u-q*v\n        return s,u,a\n\ndef\
    \ Solve_Bezout_Identity(a, b, c, lx, rx, ly, ry, extgcd = None):\n    \"\"\" a\
    \ x + b y = c , lx <= x <= rx, ly <= y <= ry \u3092\u6E80\u305F\u3059\u3088\u3046\
    \u306A\u6574\u6570\u306E\u7D44 (x,y) \u3092\u6C42\u3081\u308B.\n\n    [Input]\n\
    \    a != 0, b != 0\n    lx <= rx, ly <= ry\n    extgcd: (s,t) \u306E\u5F62\u306E\
    \u30BF\u30D7\u30EB\u3067\u3042\u308A, a s + b t = gcd(a, b) \u3067\u306A\u304F\
    \u3066\u306F\u306A\u3089\u306A\u3044.\n\n    [Output]\n    \u5B58\u5728\u3057\u306A\
    \u3044\u5834\u5408, (None, None, None, None, None, None)\n    \u5B58\u5728\u3059\
    \u308B\u5834\u5408, (p0, p1, q0, q1, lk, rk) \u306E\u5F62\u306E\u30BF\u30D7\u30EB\
    \u3067\u3042\u308B. \u4EE5\u4E0B\u3092\u610F\u5473\u3059\u308B.\n    x = p0 +\
    \ p1 k, y = q0 + q1 k, lk <= k <= rk\n    \"\"\"\n\n    assert a != 0 and b !=\
    \ 0\n    assert lx <= rx and ly <= ry\n\n    if extgcd is None:\n        s, t,\
    \ g = Find_Extend_Euclid(a, b)\n    else:\n        s, t = extgcd\n        g =\
    \ a * s + b * t\n\n    if c % g != 0:\n        return (None, None, None, None,\
    \ None, None)\n\n    a //= g; b //= g; c //=g\n\n    if b > 0:\n        tmp_l\
    \ = lx - c * s\n        tmp_r = rx - c * s\n    else:\n        tmp_l = -(rx -\
    \ c * s)\n        tmp_r = -(lx - c * s)\n\n    klx = (tmp_l + abs(b) - 1) // abs(b)\n\
    \    krx = tmp_r // abs(b)\n\n    if a > 0:\n        tmp_l = -ry + c * t\n   \
    \     tmp_r = -ly + c * t\n    else:\n        tmp_l = -(-ly + c * t)\n       \
    \ tmp_r = -(-ry + c * t)\n\n    kly = (tmp_l + abs(a) - 1) // abs(a)\n    kry\
    \ = tmp_r // abs(a)\n\n\n    kl = max(klx, kly); kr = min(krx, kry)\n    if kl\
    \ > kr:\n        return (None, None, None, None, None, None)\n\n    return (c\
    \ * s, b, c * t, -a, kl, kr)\n\ndef Integer_Equation(P, Y, L=0, default=None):\n\
    \    \"\"\" P[0]+P[1]x+...+P[n-1]x^(n-1)=Y \u3092\u6E80\u305F\u3059\u6574\u6570\
    \ x \u3092\u6C42\u3081\u308B.\n\n    P: \u591A\u9805\u5F0F (1\u6B21\u4EE5\u4E0A\
    , \u975E\u96F6\u3067\u3042\u308A, L<=x \u306E\u7BC4\u56F2\u3067 P \u306F\u5358\
    \u8ABF\u5897\u52A0\u3067\u306A\u304F\u3066\u306F\u306A\u3089\u306A\u3044).\n \
    \   Y: int\n    L: int (x \u3068\u3057\u3066\u3042\u308A\u3046\u308B\u4E0B\u754C\
    \u3092\u6C42\u3081\u308B).\n    default: \u5B58\u5728\u3057\u306A\u3044\u5834\u5408\
    \u306E\u8FD4\u308A\u5024\n    \"\"\"\n\n    P=list(P)\n    while P and P[-1]==0:\n\
    \        P.pop()\n    assert len(P)>=2\n\n    def calc(x):\n        y=0\n    \
    \    for p in reversed(P):\n            y=(y*x+p)\n        return y\n\n    if\
    \ calc(L)>Y:\n        return default\n\n    # \u4E0A\u754C\u3092\u6C42\u3081\u308B\
    \n    d=1\n    while calc(L+d)<=Y:\n        d*=2\n    R=L+d\n\n    # \u89E3\u3092\
    \u6C42\u3081\u308B\n    while R-L>1:\n        C=L+(R-L)//2\n        if calc(C)<=Y:\n\
    \            L=C\n        else:\n            R=C\n    return L if calc(L)==Y else\
    \ default\n\ndef Integer_Inequality(P, Y, L=0, mode=True, default=None):\n   \
    \ \"\"\" P[0]+P[1]x+...+P[n-1]x^(n-1) <= Y \u3092\u6E80\u305F\u3059\u6700\u5927\
    \u306E\u6574\u6570 x \u3092\u6C42\u3081\u308B.\n\n    P: \u591A\u9805\u5F0F (1\u6B21\
    \u4EE5\u4E0A, \u975E\u96F6\u3067\u3042\u308A, L<=x \u306E\u7BC4\u56F2\u3067 P\
    \ \u306F\u5358\u8ABF\u5897\u52A0\u3067\u306A\u304F\u3066\u306F\u306A\u3089\u306A\
    \u3044).\n    Y: int\n    L: int (x \u3068\u3057\u3066\u3042\u308A\u3046\u308B\
    \u4E0B\u754C\u3092\u6C42\u3081\u308B).\n    mode: True \u306E\u5834\u5408\u306F\
    \ <=, False \u306E\u5834\u5408\u306F < \u306B\u306A\u308B.\n    default: \u5B58\
    \u5728\u3057\u306A\u3044\u5834\u5408\u306E\u8FD4\u308A\u5024\n    \"\"\"\n\n \
    \   P=list(P)\n    while P and P[-1]==0:\n        P.pop()\n    assert len(P)>=2\n\
    \n    def calc(x):\n        y=0\n        for p in reversed(P):\n            y=(y*x+p)\n\
    \        return y\n\n    if calc(L)>Y or (not mode and calc(L)==Y):\n        return\
    \ default\n\n    # \u4E0A\u754C\u3092\u6C42\u3081\u308B\n    d=1\n    if mode:\n\
    \        while calc(L+d)<=Y:\n            d*=2\n    else:\n        while calc(L+d)<Y:\n\
    \            d*=2\n    R=L+d\n\n    # \u89E3\u3092\u6C42\u3081\u308B\n    while\
    \ R-L>1:\n        C=L+(R-L)//2\n        y0=calc(C)\n        if y0<Y or (mode and\
    \ y0==Y):\n            L=C\n        else:\n            R=C\n    return L\n"
  dependsOn: []
  isVerificationFile: false
  path: Integer/Equation.py
  requiredBy: []
  timestamp: '2023-08-20 11:29:25+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Integer/Equation.py
layout: document
redirect_from:
- /library/Integer/Equation.py
- /library/Integer/Equation.py.html
title: Integer/Equation.py
---
