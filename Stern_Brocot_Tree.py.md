---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test_verify/yosupo_library_checker/Math/Rational_Approximation.test.py
    title: test_verify/yosupo_library_checker/Math/Rational_Approximation.test.py
  - icon: ':heavy_check_mark:'
    path: test_verify/yosupo_library_checker/Math/Stern_Brocot_Tree.test.py
    title: test_verify/yosupo_library_checker/Math/Stern_Brocot_Tree.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.13.3/x64/lib/python3.13/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.13.3/x64/lib/python3.13/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class Stern_Brocot_Tree:\n    @staticmethod\n    def encode(a: int, b: int,\
    \ left = 'L', right = 'R') -> list[tuple]:\n        path = []\n        q, r =\
    \ divmod(a, b)\n        if q > 0:\n            path.append((right, q))\n\n   \
    \     a, b = b, r\n        parity = True\n        while b:\n            q, r =\
    \ divmod(a, b)\n            path.append((left if parity else right, q))\n    \
    \        a, b = b, r\n            parity ^= True\n\n        direction, k = path.pop()\n\
    \        if k > 1:\n            path.append((direction, k - 1))\n        return\
    \ path\n\n    @staticmethod\n    def decode_interval(code, left = 'L', right =\
    \ 'R') -> tuple[int, int, int, int]:\n        p, q, r, s = 0, 1, 1, 0\n      \
    \  for direction, k in code:\n            if direction == left:\n            \
    \    r += k * p\n                s += k * q\n            elif direction == right:\n\
    \                p += k * r\n                q += k * s\n        return (p, q,\
    \ r, s)\n\n\n    @classmethod\n    def decode(cls, code, left = 'L', right = 'R')\
    \ -> tuple[int, int]:\n        p, q, r, s = cls.decode_interval(code, left, right)\n\
    \        return (p + r, q + s)\n\n    @classmethod\n    def lowest_common_ancestor(cls,\
    \ a: int, b: int, c:int, d:int) -> tuple[int, int]:\n        if (a, b) == (1,\
    \ 1) or (c, d) == (1, 1):\n            return (1, 1)\n\n        code_1 = cls.encode(a,\
    \ b)\n        code_2 = cls.encode(c, d)\n        if code_1[0][0] != code_2[0][0]:\n\
    \            return (1, 1)\n\n        lca_code = []\n        for ((t, k), (_,\
    \ l)) in zip(code_1, code_2):\n            lca_code.append((t, min(k, l)))\n \
    \           if k != l:\n                break\n        return cls.decode(lca_code)\n\
    \n    @classmethod\n    def depth(cls, a: int, b: int) -> int:\n        code =\
    \ cls.encode(a, b)\n        return sum(k for _, k in code)\n\n    @classmethod\n\
    \    def ancestor(cls, a: int, b: int, k: int, default = None) -> tuple[int, int]:\n\
    \        code = []\n        for direction, l in cls.encode(a, b):\n          \
    \  l = min(k, l)\n            code.append((direction, l))\n            k -= l\n\
    \            if k == 0:\n                return cls.decode(code)\n        else:\n\
    \            return default\n\n    @classmethod\n    def range(cls, a: int, b:\
    \ int):\n        return cls.decode_interval(cls.encode(a, b))\n\n    @classmethod\n\
    \    def binary_search_range_increase(cls, N: int, cond) -> tuple[int, int, int,\
    \ int]:\n        \"\"\" \u5358\u8ABF\u5897\u52A0\u306A check \u306B\u304A\u3044\
    \u3066, cond(x) = T \u304C\u3068\u306A\u308B\u6700\u5C0F\u306E x \u3092\u631F\u3080\
    \u5206\u5B50\u3068\u5206\u6BCD\u304C N \u4EE5\u4E0B\u306E\u6709\u7406\u6570\u3092\
    \u6C42\u3081\u308B.\n\n        Args:\n            N (int): \u5206\u5B50\u3068\u5206\
    \u6BCD\u306E\u4E0A\u9650\n            cond: 2 \u5909\u6570\u95A2\u6570\u3067,\
    \ cond(a, b) \u306F cond(a / b) \u3092\u610F\u5473\u3059\u308B.\n\n        Returns:\n\
    \            tuple[int, int, int, int]: \u6574\u6570\u306E\u7D44 (p, q, r, s)\
    \ \u306F\u4EE5\u4E0B\u3092\u610F\u5473\u3059\u308B.\n                p, q: cond(x)\
    \ = F \u3092\u6E80\u305F\u3059 x \u3067\u5206\u5B50\u3068\u5206\u6BCD\u304C\u5171\
    \u306B N \u4EE5\u4E0B\u3067\u3042\u308B\u6709\u7406\u6570\u306E\u3046\u3061, \u6700\
    \u5927\u306E\u6709\u7406\u6570\u3092 x \u3068\u3057\u305F\u3068\u304D, x = p /\
    \ q \u3067\u3042\u308B.\n                r, s :cond(x) = T \u3092\u6E80\u305F\u3059\
    \ x \u3067\u5206\u5B50\u3068\u5206\u6BCD\u304C\u5171\u306B N \u4EE5\u4E0B\u3067\
    \u3042\u308B\u6709\u7406\u6570\u306E\u3046\u3061, \u6700\u5C0F\u306E\u6709\u7406\
    \u6570\u3092 x \u3068\u3057\u305F\u3068\u304D, x = r / s \u3067\u3042\u308B.\n\
    \        \"\"\"\n\n        def right_search(p: int, q: int, r: int, s: int) ->\
    \ int:\n            lower = 0\n            upper = (N - p) // r + 1\n\n      \
    \      while upper - lower > 1:\n                d = (lower + upper) // 2\n  \
    \              if (p + d * r <= N) and (q + d * s <= N) and not cond(p + d * r,\
    \ q + d * s):\n                    lower = d\n                else:\n        \
    \            upper = d\n            return lower\n\n        def left_search(p:\
    \ int, q: int, r: int, s: int) -> int:\n            lower = 0\n            upper\
    \ = (N - p) // r + 1\n\n            while upper - lower > 1:\n               \
    \ d = (lower + upper) // 2\n                if (r + d * p <= N) and (s + d * q\
    \ <= N) and cond(r + d * p, s + d * q):\n                    lower = d\n     \
    \           else:\n                    upper = d\n            return lower\n\n\
    \        p, q, r, s = 0, 1, 1, 0\n        while p + r <= N and q + s <= N:\n \
    \           d = right_search(p, q, r, s)\n            p += d * r; q += d * s\n\
    \n            d = left_search(p, q, r, s)\n            r += d * p; s += d * q\n\
    \n        return p, q, r, s\n\nclass Stern_Brocot_Tree_Node:\n    def __init__(self):\n\
    \        pass\n"
  dependsOn: []
  isVerificationFile: false
  path: Stern_Brocot_Tree.py
  requiredBy: []
  timestamp: '2025-06-22 15:19:00+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test_verify/yosupo_library_checker/Math/Stern_Brocot_Tree.test.py
  - test_verify/yosupo_library_checker/Math/Rational_Approximation.test.py
documentation_of: Stern_Brocot_Tree.py
layout: document
redirect_from:
- /library/Stern_Brocot_Tree.py
- /library/Stern_Brocot_Tree.py.html
title: Stern_Brocot_Tree.py
---
