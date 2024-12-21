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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.8/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.8/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from heapq import heappush, heappop\n\nclass Best_Sum:\n    def __init__(self,\
    \ K, reversal = 1):\n\n        self.K = max(0, K)\n        self.reversal = reversal\n\
    \n        self.more = []\n        self.more_count = {}\n        self.more_sum\
    \ = 0\n        self.more_length = 0\n\n        self.less = []\n        self.less_count\
    \ = {}\n        self.less_sum = 0\n        self.less_length  = 0\n\n    def _more_insert(self,\
    \ x):\n        self.more_sum += x\n        self.more_length += 1\n\n        if\
    \ x in self.more_count:\n            self.more_count[x] += 1\n        else:\n\
    \            self.more_count[x] = 1\n            heappush(self.more, x)\n\n  \
    \  def _less_insert(self, x):\n        self.less_sum += x\n        self.less_length\
    \ += 1\n\n        if x in self.less_count:\n            self.less_count[x] +=\
    \ 1\n        else:\n            self.less_count[x] = 1\n            heappush(self.less,\
    \ -x)\n\n    def _more_discard(self, x):\n        self.more_sum -= x\n       \
    \ self.more_length -= 1\n        self.more_count[x] -= 1\n\n        if self.more_count[x]\
    \ == 0:\n            del self.more_count[x]\n\n        while self.more and (self.more[0]\
    \ not in self.more_count):\n            heappop(self.more)\n\n    def _less_discard(self,\
    \ x):\n        self.less_sum -= x\n        self.less_length -= 1\n        self.less_count[x]\
    \ -= 1\n\n        if self.less_count[x] == 0:\n            del self.less_count[x]\n\
    \n        while self.less and (-self.less[0] not in self.less_count):\n      \
    \      heappop(self.less)\n\n    def _more_to_less(self):\n        x = self.more[0]\n\
    \        self._more_discard(x)\n        self._less_insert(x)\n\n    def _less_to_more(self):\n\
    \        x = -self.less[0]\n        self._less_discard(x)\n        self._more_insert(x)\n\
    \n    def _validation(self):\n        if self.more_length > self.K:\n        \
    \    while self.more_length > self.K:\n                self._more_to_less()\n\
    \        elif self.more_length < self.K:\n            while self.less_length >\
    \ 0 and self.more_length < self.K:\n                self._less_to_more()\n\n \
    \   def __len__(self):\n        return self.more_length + self.less_length\n\n\
    \    def __contains__(self, value):\n        return (value in self.more_count)\
    \ or (value in self.less_count)\n\n    def count(self, value):\n        return\
    \ self.more_count(value, 0) + self.less_count(value, 0)\n\n    def insert(self,\
    \ x):\n        x *= self.reversal\n        self._more_insert(x)\n        self._validation()\n\
    \n    def discard(self, x):\n        x *= self.reversal\n\n        if x not in\
    \ self:\n            return\n\n        if x >= self.more[0]:\n            self._more_discard(x)\n\
    \        else:\n            self._less_discard(x)\n        self._validation()\n\
    \n    def best_sum(self):\n        assert self.reversal == 1\n        return self.more_sum\n\
    \n    def worst_sum(self):\n        assert self.reversal == -1\n        return\
    \ -self.more_sum\n\n    def all_sum(self):\n        return self.reversal * (self.more_sum\
    \ + self.less_sum)\n\n    def change_K(self, K):\n        self.K = max(0, K)\n\
    \        self._validation()\n\nclass Worst_Sum(Best_Sum):\n    def __init__(self,\
    \ K, reversal = 1):\n        Best_Sum.__init__(self, K, - reversal)\n"
  dependsOn: []
  isVerificationFile: false
  path: Best_Sum.py
  requiredBy: []
  timestamp: '2023-08-26 10:47:28+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Best_Sum.py
layout: document
redirect_from:
- /library/Best_Sum.py
- /library/Best_Sum.py.html
title: Best_Sum.py
---
