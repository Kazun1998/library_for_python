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
  code: "from Point import *\nfrom Circle import *\nfrom Triangle import *\n\ndef\
    \ Minimum_Enclosing_Circle(S: list[Point], trial: int = 100) -> Circle:\n    \"\
    \"\" \u70B9\u306E\u30EA\u30B9\u30C8 S \u306B\u95A2\u3059\u308B\u6700\u5C0F\u5185\
    \u5305\u5186\u3092\u6C42\u3081\u308B.\n\n    Args:\n        S (list[Point]): \u5E73\
    \u9762\u4E0A\u306E\u70B9\u306E\u30EA\u30B9\u30C8\n        trial (int, optional):\
    \ \u6C42\u3081\u308B\u969B\u306B\u884C\u3046\u4E09\u5206\u63A2\u7D22\u306B\u304A\
    \u3051\u308B\u5224\u5B9A\u306E\u56DE\u6570. Defaults to 100.\n\n    Returns:\n\
    \        Circle: _description_\n    \"\"\"\n\n    # |S| <= 3 \u306E\u3068\u304D\
    \u306F\u660E\u793A\u7684\u306B\u6C42\u3081\u3089\u308C\u308B.\n    if len(S) ==\
    \ 1:\n        # |S| = 1 \u306E\u5834\u5408\u306F\u305D\u306E\u70B9\u304C\u6700\
    \u5C0F\u5185\u5305\u5186\n        return Circle(S[0], 0)\n    elif len(S) == 2:\n\
    \        # |S| = 2 \u306E\u5834\u5408\u306F\u305D\u306E 2 \u70B9\u3092\u76F4\u5F84\
    \u3068\u3059\u308B\u5186\u304C\u6700\u5C0F\u5185\u5305\u5186\n        M = (S[0]\
    \ + S[1]) / 2\n        return Circle(M, abs(M - S[0]))\n    elif len(S) == 3:\n\
    \        A, B, C = S\n        a, b, c = abs(B - C), abs(C - A), abs(A - B)\n \
    \       a2, b2, c2 = a * a, b * b, c * c\n\n        # \u4E09\u89D2\u5F62 ABC \u304C\
    \u920D\u89D2\u4E09\u89D2\u5F62\u306E\u3068\u304D\u306F, \u4E00\u756A\u9577\u3044\
    \u8FBA\u3092\u76F4\u5F84\u3068\u3059\u308B\u5186\u304C\u6700\u5C0F\u5185\u5305\
    \u5186\u306B\u306A\u308B.\n        if compare(a2, b2 + c2) == 1:\n           \
    \ return Minimum_Enclosing_Circle([B, C])\n        elif compare(b2, c2 + a2) ==\
    \ 1:\n            return Minimum_Enclosing_Circle([C, A])\n        elif compare(c2,\
    \ a2 + b2) == 1:\n            return Minimum_Enclosing_Circle([A, B])\n\n    \
    \    # \u4E09\u89D2\u5F62 ABC \u304C\u92ED\u89D2\u4E09\u89D2\u5F62\u306E\u3068\
    \u304D\u306F, \u305D\u306E\u4E09\u89D2\u5F62\u306E\u5916\u63A5\u5186\u304C\u6700\
    \u5C0F\u5185\u5305\u5186\u306B\u306A\u308B.\n        ta = a2 * (-a2 + b2 + c2)\n\
    \        tb = b2 * (a2 - b2 + c2)\n        tc = c2 * (a2 + b2 - c2)\n        s\
    \ = ta + tb + tc\n\n        K = (ta / s) * A + (tb / s) * B + (tc / s) * C\n \
    \       return Circle(K, abs(K - A))\n\n    def f(x, y):\n        res = 0\n  \
    \      for p in S:\n            dx = x - p.x; dy = y - p.y\n            res =\
    \ max(res, dx * dx + dy * dy)\n        return sqrt(res)\n\n    def g(x):\n   \
    \     L = y_min; R = y_max\n        for _ in range(trial):\n            a = (2\
    \ * L + R) / 3\n            b = (L + 2 * R) / 3\n\n            if f(x, a) > f(x,\
    \ b):\n                L = a\n            else:\n                R = b\n\n   \
    \     c = (L + R) / 2\n        return f(x, c), c\n\n    inf=float(\"inf\")\n \
    \   x_min,x_max=inf,-inf\n    y_min,y_max=inf,-inf\n\n    for p in S:\n      \
    \  x_min=min(x_min,p.x)\n        x_max=max(x_max,p.x)\n        y_min=min(y_min,p.y)\n\
    \        y_max=max(y_max,p.y)\n\n    L, R = x_min, x_max\n    for _ in range(trial):\n\
    \        a = (2 * L + R) / 3\n        b = (L + 2 * R) / 3\n\n        if g(a)[0]\
    \ > g(b)[0]:\n            L = a\n        else:\n            R = b\n\n    X = (L\
    \ + R) / 2\n    r, Y = g(X)\n\n    C = Point(X,Y)\n\n    Q = sorted(\n       \
    \ [(0, abs(C - S[0])), (1, abs(C - S[1])),(2, abs(C - S[2]))],\n        key =\
    \ lambda t: t[1], reverse = True\n        )\n\n    for i in range(3, len(S)):\n\
    \        m = (i, abs(C - S[i]))\n        for k in range(3):\n            if m[1]\
    \ > Q[k][1]:\n                Q[k], m = m, Q[k]\n    return Minimum_Enclosing_Circle([S[j]\
    \ for j,_ in Q])\n"
  dependsOn: []
  isVerificationFile: false
  path: Geometric/Advance.py
  requiredBy: []
  timestamp: '2025-03-01 17:53:41+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Geometric/Advance.py
layout: document
redirect_from:
- /library/Geometric/Advance.py
- /library/Geometric/Advance.py.html
title: Geometric/Advance.py
---
