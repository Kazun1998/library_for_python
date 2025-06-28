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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.13.5/x64/lib/python3.13/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.13.5/x64/lib/python3.13/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from itertools import zip_longest\n\nclass Set_Polynomial:\n    __slots__\
    \ = ('poly', )\n\n    def __init__(self, poly = []):\n        n = max(len(poly),\
    \ 1)\n        if n & (-n) == n: # n \u304C 2 \u30D9\u30AD\n            N = n.bit_length()\
    \ - 1\n        else:\n            N = n.bit_length()\n\n        self.poly = [a\
    \ % Mod for a in poly] + [0] * ((1<<N) - n)\n\n    def __len__(self):\n      \
    \  return len(self.poly)\n\n    def cardinality(self):\n        return len(self.poly).bit_length()\
    \ - 1\n\n    def __str__(self):\n        return str(self.poly)\n\n    __repr__\
    \ = __str__\n\n    def __getitem__(self, index):\n        if 0 <= index < len(self):\n\
    \            return self.poly[index]\n        else:\n            return 0\n\n\
    \    def __iter__(self):\n        yield from self.poly\n\n    def __eq__(self,\
    \ other):\n        return all(a == b for a,b in zip_longest(self, other, fillvalue\
    \ = 0))\n\n    def __add__(self, other):\n        return Set_Polynomial([a + b\
    \ for a,b in zip_longest(self, other, fillvalue = 0)])\n\n    def __radd__(self,\
    \ other):\n        return self + other\n\n    def __sub__(self, other):\n    \
    \    return Set_Polynomial([a - b for a,b in zip_longest(self, other, fillvalue\
    \ = 0)])\n\n    def __rsub__(self, other):\n        return (- self) + other\n\n\
    \    def __mul__(self, other):\n        if other.__class__ == Set_Polynomial:\n\
    \            N = self.cardinality(); M = other.cardinality()\n            L =\
    \ max(N, M)\n\n            a = Set_Polynomial.__zeta_transform(self.poly + [0]\
    \ * ((1 << M) - (1 << N)) )\n            b = Set_Polynomial.__zeta_transform(other.poly\
    \ + [0] * ((1 << N) - (1 << M)) )\n\n            c = [0] * ((L + 1)  << L)\n \
    \           popcount = Set_Polynomial.__popcount\n            for S in range(1\
    \ << L):\n                S_pop = popcount(S)\n                for i in range(S_pop\
    \ + 1):\n                    for j in range(min(S_pop, L - i) + 1):\n        \
    \                alpha = a[S * (L + 1) + i] * b[S * (L + 1) + j]\n           \
    \             c[S * (L + 1) + (i + j)] = (c[S * (L + 1) + (i + j)] + alpha) %\
    \ Mod\n            return Set_Polynomial(Set_Polynomial.__mobius_transform(c))\n\
    \        else:\n            return self.scale(other)\n\n    def __rmul__(self,\
    \ other):\n        return self * other\n\n    @staticmethod\n    def __popcount(n):\n\
    \        c = (n & 0x5555555555555555) + ((n >> 1 ) & 0x5555555555555555)\n   \
    \     c = (c & 0x3333333333333333) + ((c >> 2 ) & 0x3333333333333333)\n      \
    \  c = (c & 0x0f0f0f0f0f0f0f0f) + ((c >> 4 ) & 0x0f0f0f0f0f0f0f0f)\n        c\
    \ = (c & 0x00ff00ff00ff00ff) + ((c >> 8 ) & 0x00ff00ff00ff00ff)\n        c = (c\
    \ & 0x0000ffff0000ffff) + ((c >> 16) & 0x0000ffff0000ffff)\n        c = (c & 0x00000000ffffffff)\
    \ + ((c >> 32) & 0x00000000ffffffff)\n        return c\n\n    @staticmethod\n\
    \    def __zeta_transform(p):\n        N = len(p).bit_length() - 1\n        q\
    \ = [0] * ((N + 1) * (1 << N))\n        popcount = Set_Polynomial.__popcount\n\
    \        for S in range(len(p)):\n            q[S * (N + 1) + popcount(S)] = p[S]\n\
    \n        L = 1 << N\n        for i in range(N):\n            bit = 1 << i\n \
    \           S = 0\n            for _ in range(L >> 1):\n                S |= bit\n\
    \                T = S ^ bit\n                for k in range(N + 1):\n       \
    \             q[S * (N + 1) + k] += q[T * (N + 1) + k]\n                S += 1\n\
    \        return [qS % Mod for qS in q]\n\n    @staticmethod\n    def __mobius_transform(q):\n\
    \        N = 0\n        while ((N + 1) << N) < len(q):\n            N += 1\n \
    \       assert ((N + 1) << N) == len(q)\n\n        L = 1 << N\n        for i in\
    \ range(N):\n            bit = 1 << i\n            S = 0\n            for _ in\
    \ range(L >> 1):\n                S |= bit\n                T = S ^ bit\n    \
    \            for k in range(N + 1):\n                    q[S * (N + 1) + k] -=\
    \ q[T * (N + 1) + k]\n                S += 1\n\n        popcount = Set_Polynomial.__popcount\n\
    \        return [q[S * (N + 1) + popcount(S)] % Mod for S in range(1 << N)]\n\n\
    \    def scale(self, r):\n        return Set_Polynomial([(r * a) % Mod for a in\
    \ self])\n\n#==================================================\nMod = 998244353\n"
  dependsOn: []
  isVerificationFile: false
  path: Set_Polynomial/Set_Polynomial.py
  requiredBy: []
  timestamp: '2023-09-30 17:03:54+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Set_Polynomial/Set_Polynomial.py
layout: document
redirect_from:
- /library/Set_Polynomial/Set_Polynomial.py
- /library/Set_Polynomial/Set_Polynomial.py.html
title: Set_Polynomial/Set_Polynomial.py
---
