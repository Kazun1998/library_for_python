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
  code: "from typing import TypeVar, Generic\n\nS = TypeVar('S')\nT = TypeVar('T')\n\
    U = TypeVar('U')\nclass Triple(tuple, Generic[S, T, U]):\n    def __new__(cls,\
    \ first: S, second: T, third: U):\n        return super().__new__(cls, (first,\
    \ second, third))\n\n    def __repr__(self) -> str:\n        return f\"{self.__class__.__name__}({self.first},\
    \ {self.second}, {self.third})\"\n\n    @property\n    def first(self) -> S:\n\
    \        return self[0]\n\n    @property\n    def second(self) -> T:\n       \
    \ return self[1]\n\n    @property\n    def third(self) -> U:\n        return self[2]\n\
    \n    def __add__(self, other: \"Triple[S, T, U]\") -> \"Triple[S, T, U]\":\n\
    \        return Triple(self.first + other.first, self.second + other.second, self.third\
    \ + other.third)\n\n    def __sub__(self, other: \"Triple[S, T, U]\") -> \"Triple[S,\
    \ T, U]\":\n        return Triple(self.first - other.first, self.second - other.second,\
    \ self.third - other.third)\n\n    def __mul__(self, other: \"Triple[S, T, U]\"\
    ) -> \"Triple[S, T, U]\":\n        return Triple(self.first * other.first, self.second\
    \ * other.second, self.third * other.third)\n\n    def __xor__(self, other: \"\
    Triple[S, T, U]\") -> \"Triple[S, T, U]\":\n        return Triple(self.first ^\
    \ other.first, self.second ^ other.second, self.third ^ other.third)\n"
  dependsOn: []
  isVerificationFile: false
  path: Tuple/Triple.py
  requiredBy: []
  timestamp: '2025-03-29 18:25:08+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Tuple/Triple.py
layout: document
redirect_from:
- /library/Tuple/Triple.py
- /library/Tuple/Triple.py.html
title: Tuple/Triple.py
---
