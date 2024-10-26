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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.7/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.7/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class Stern_Brocot_Tree:\n    @staticmethod\n    def encode(a: int, b: int,\
    \ left = 'L', right = 'R'):\n        path = []\n        q, r = divmod(a, b)\n\
    \        if q > 0:\n            path.append((right, q))\n\n        a, b = b, r\n\
    \        parity = True\n        while b:\n            q, r = divmod(a, b)\n  \
    \          path.append((left if parity else right, q))\n            a, b = b,\
    \ r\n            parity ^= True\n\n        direction, k = path.pop()\n       \
    \ if k > 1:\n            path.append((direction, k - 1))\n        return path\n\
    \n    @staticmethod\n    def decode_interval(code, left = 'L', right = 'R'):\n\
    \        p, q, r, s = 0, 1, 1, 0\n        for direction, k in code:\n        \
    \    if direction == left:\n                r += k * p\n                s += k\
    \ * q\n            elif direction == right:\n                p += k * r\n    \
    \            q += k * s\n        return (p, q, r, s)\n\n\n    @classmethod\n \
    \   def decode(cls, code, left = 'L', right = 'R'):\n        p, q, r, s = cls.decode_interval(code,\
    \ left, right)\n        return (p + r, q + s)\n\n    @classmethod\n    def lowest_common_ancestor(cls,\
    \ a: int, b: int, c:int, d:int):\n        if (a, b) == (1, 1) or (c, d) == (1,\
    \ 1):\n            return (1, 1)\n\n        code_1 = cls.encode(a, b)\n      \
    \  code_2 = cls.encode(c, d)\n        if code_1[0][0] != code_2[0][0]:\n     \
    \       return (1, 1)\n\n        lca_code = []\n        for ((t, k), (_, l)) in\
    \ zip(code_1, code_2):\n            lca_code.append((t, min(k, l)))\n        \
    \    if k != l:\n                break\n        return cls.decode(lca_code)\n\n\
    \    @classmethod\n    def depth(cls, a: int, b: int):\n        code = cls.encode(a,\
    \ b)\n        return sum(k for _, k in code)\n\n    @classmethod\n    def ancestor(cls,\
    \ a: int, b: int, k: int, default = None):\n        code = []\n        for direction,\
    \ l in cls.encode(a, b):\n            l = min(k, l)\n            code.append((direction,\
    \ l))\n            k -= l\n            if k == 0:\n                return cls.decode(code)\n\
    \        else:\n            return default\n\n    @classmethod\n    def range(cls,\
    \ a: int, b: int):\n        return cls.decode_interval(cls.encode(a, b))\n\nclass\
    \ Stern_Brocot_Tree_Node:\n    def __init__(self):\n        pass\n"
  dependsOn: []
  isVerificationFile: false
  path: Stern_Brocot_Tree.py
  requiredBy: []
  timestamp: '2024-02-24 22:48:21+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Stern_Brocot_Tree.py
layout: document
redirect_from:
- /library/Stern_Brocot_Tree.py
- /library/Stern_Brocot_Tree.py.html
title: Stern_Brocot_Tree.py
---
