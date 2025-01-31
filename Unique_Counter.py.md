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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.13.1/x64/lib/python3.13/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.13.1/x64/lib/python3.13/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class Unique_Counter:\n    def __init__(self):\n        self.list = []\n\n\
    \    def add(self, x):\n        self.list.append(x)\n\n    def count(self):\n\
    \        if not self.list:\n            return 0\n\n        self.list.sort()\n\
    \        res = 1\n        for i in range(1, len(self.list)):\n            if self.list[i]\
    \ != self.list[i - 1]:\n                res += 1\n        return res\n"
  dependsOn: []
  isVerificationFile: false
  path: Unique_Counter.py
  requiredBy: []
  timestamp: '2025-01-26 00:03:14+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Unique_Counter.py
layout: document
redirect_from:
- /library/Unique_Counter.py
- /library/Unique_Counter.py.html
title: Unique_Counter.py
---
