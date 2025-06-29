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
    \ float, period: int = 1) -> \"Timer\":\n        self.__started_at = time()\n\
    \        self.__time_limit = time_limit\n        self.__period = period\n    \
    \    self.__counter = period\n\n    def __repr__(self) -> str:\n        return\
    \ f\"{self.__class__.__name__}(time_limit={self.time_limit}, self.period={self.period})\"\
    \n\n    def __bool__(self) -> bool:\n        self.__counter -= 1\n        if self.__counter:\n\
    \            return True\n\n        self.__counter = self.period\n        return\
    \ time() - self.started_at <= self.time_limit\n\n    @property\n    def started_at(self)\
    \ -> float:\n        return self.__started_at\n\n    @property\n    def period(self)\
    \ -> int:\n        return self.__period\n\n    @property\n    def time_limit(self)\
    \ -> float:\n        return self.__time_limit\n\n    @property\n    def time(self)\
    \ -> float:\n        \"\"\" \u7D4C\u904E\u6642\u9593\u3092\u51FA\u529B\u3059\u308B\
    .\n\n        Returns:\n            float: \u7D4C\u904E\u6642\u9593\n        \"\
    \"\"\n\n        return time() - self.started_at\n"
  dependsOn: []
  isVerificationFile: false
  path: Heuristic/Timer.py
  requiredBy: []
  timestamp: '2025-06-29 13:19:27+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Heuristic/Timer.py
layout: document
redirect_from:
- /library/Heuristic/Timer.py
- /library/Heuristic/Timer.py.html
title: Heuristic/Timer.py
---
