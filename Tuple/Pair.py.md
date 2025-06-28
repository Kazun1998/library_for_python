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
  code: "from typing import TypeVar, Generic\n\nS = TypeVar('S')\nT = TypeVar('T')\n\
    class Pair(tuple, Generic[S, T]):\n    def __new__(cls, first: S, second: T):\n\
    \        return super().__new__(cls, (first, second))\n\n    def __repr__(self)\
    \ -> str:\n        return f\"{self.__class__.__name__}({self.first}, {self.second})\"\
    \n\n    @property\n    def first(self) -> S:\n        return self[0]\n\n    @property\n\
    \    def second(self) -> T:\n        return self[1]\n\n    def __add__(self, other:\
    \ \"Pair[S, T]\") -> \"Pair[S, T]\":\n        return Pair(self.first + other.first,\
    \ self.second + other.second)\n\n    def __sub__(self, other: \"Pair[S, T]\")\
    \ -> \"Pair[S, T]\":\n        return Pair(self.first - other.first, self.second\
    \ - other.second)\n\n    def __mul__(self, other: \"Pair[S, T]\") -> \"Pair[S,\
    \ T]\":\n        return Pair(self.first * other.first, self.second * other.second)\n\
    \n    def __xor__(self, other: \"Pair[S, T]\") -> \"Pair[S, T]\":\n        return\
    \ Pair(self.first ^ other.first, self.second ^ other.second)\n"
  dependsOn: []
  isVerificationFile: false
  path: Tuple/Pair.py
  requiredBy: []
  timestamp: '2025-03-29 18:25:00+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Tuple/Pair.py
layout: document
redirect_from:
- /library/Tuple/Pair.py
- /library/Tuple/Pair.py.html
title: Tuple/Pair.py
---
