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
  code: "from time import time\n\nclass Timer:\n    def __init__(self, time_limit:\
    \ float, period: int = 1) -> \"Timer\":\n        self.started_at = time()\n  \
    \      self.time_limit = time_limit\n        self.period = period\n        self.counter\
    \ = period\n        self.t = 0\n\n    def __bool__(self) -> bool:\n        self.counter\
    \ -= 1\n        if self.counter:\n            return True\n\n        self.counter\
    \ = self.period\n        return time() - self.started_at <= self.time_limit\n\n\
    \    def time(self) -> float:\n        return time() - self.started_at\n"
  dependsOn: []
  isVerificationFile: false
  path: Heuristic/Timer.py
  requiredBy: []
  timestamp: '2025-02-01 00:09:02+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Heuristic/Timer.py
layout: document
redirect_from:
- /library/Heuristic/Timer.py
- /library/Heuristic/Timer.py.html
title: Heuristic/Timer.py
---
