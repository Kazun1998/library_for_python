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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "#\u62E1\u5F35\u30E6\u30FC\u30AF\u30EA\u30C3\u30C9\u306E\u4E92\u9664\u6CD5\
    \ndef Find_Extend_Euclid(a: int, b: int):\n    \"\"\"ax+by=gcd(a, b) \u3092\u6E80\
    \u305F\u3059 (x, y, gcd(a, b)) \u3092 1 \u3064\u6C42\u3081\u308B.\n\n    a,b:\u6574\
    \u6570\n    \"\"\"\n    from math import gcd\n    g = gcd(a, b)\n    if g == 0:\n\
    \        return (1, 0, 0)\n\n    x = pow(a//g, -1, b//g)\n    y = - (a*x-g) //\
    \ b\n    return (x, y, g)\n\ndef Solve_Bezout_Identity(a, b, c, lx, rx, ly, ry,\
    \ extgcd = None):\n    \"\"\" a x + b y = c, lx <= x <=rx, ly <= y <= ry \u3092\
    \u6E80\u305F\u3059\u6574\u6570 (x,y) \u306B\u3064\u3044\u3066\u6C42\u3081\u308B\
    .\n\n    [Input]\n    a != 0, b != 0 \u3067\u306A\u304F\u3066\u306F\u306A\u3089\
    \u306A\u3044.\n    extgcd : (s, t) \u306E\u5F62\u306E\u30BF\u30D7\u30EB\u3067\
    , a s + b t = gcd(a, b) \u3092\u6E80\u305F\u3057\u3066\u3044\u306A\u3051\u308C\
    \u3070\u306A\u3089\u306A\u3044.\n\n    [Output]\n    \u7B54\u3048\u304C\u5B58\u5728\
    \u3059\u308B\u5834\u5408:\n    (p0, p1, q0, q1, l, r) \u306E\u5F62\u306E\u30BF\
    \u30D7\u30EB\u3067, \u4EE5\u4E0B\u3092\u610F\u5473\u3059\u308B\n    x = p0 + p1\
    \ k, y = q0 + q1 k, l <= k <= r\n\n    \u7B54\u3048\u304C\u5B58\u5728\u3057\u306A\
    \u3044\u5834\u5408: None\n    \"\"\"\n\n    assert a != 0 and b != 0\n\n    sgn_a\
    \ = 1 if a > 0 else -1; a = abs(a)\n    sgn_b = 1 if b > 0 else -1; b = abs(b)\n\
    \n    if extgcd is None:\n        s, t, g = Find_Extend_Euclid(a, b)\n    else:\n\
    \        s, t = extgcd\n        g = a * s + b * t\n\n    if c % g != 0:\n    \
    \    return None\n"
  dependsOn: []
  isVerificationFile: false
  path: Integer/Equation.py
  requiredBy: []
  timestamp: '2023-08-20 01:06:32+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Integer/Equation.py
layout: document
redirect_from:
- /library/Integer/Equation.py
- /library/Integer/Equation.py.html
title: Integer/Equation.py
---
