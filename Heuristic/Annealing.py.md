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
  code: "from random import random\nfrom math import exp\n\nclass Annealing:\n   \
    \ def __init__(self, temperature: float, alpha: float, phase: int = 1) -> \"Annealing\"\
    :\n        self.temperature = temperature\n        self.alpha = alpha\n      \
    \  self.phase = phase\n        self.count = 0\n\n    def judge(self, before, after)\
    \ -> bool:\n        self.count += 1\n        if self.count == self.phase:\n  \
    \          self.temperature *= self.alpha\n            self.count = 0\n\n    \
    \    if after == before:\n            return False\n\n        if after > before:\n\
    \            return True\n        else:\n            return random() < exp((after\
    \ - before) / self.temperature)\n"
  dependsOn: []
  isVerificationFile: false
  path: Heuristic/Annealing.py
  requiredBy: []
  timestamp: '2025-02-01 00:09:11+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Heuristic/Annealing.py
layout: document
redirect_from:
- /library/Heuristic/Annealing.py
- /library/Heuristic/Annealing.py.html
title: Heuristic/Annealing.py
---
