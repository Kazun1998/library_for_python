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
  code: "from typing import TypeVar, Generic, Callable\nfrom heapq import heappush,\
    \ heappop\n\nOrderedGroup = TypeVar('OrderedGroup')\nclass Best_Sum(Generic[OrderedGroup]):\n\
    \    def __init__(self, K: int, add: Callable[[OrderedGroup, OrderedGroup], OrderedGroup],\
    \ neg: Callable[[OrderedGroup], OrderedGroup], zero: OrderedGroup, reversal: bool\
    \ = False):\n\n        self.K = max(0, K)\n        self.__reversal = reversal\n\
    \n        self.more: list[OrderedGroup] = []\n        self.more_count: dict[OrderedGroup,\
    \ int] = {}\n        self.more_sum = zero\n        self.more_length = 0\n\n  \
    \      self.less: list[OrderedGroup] = []\n        self.less_count: dict[OrderedGroup,\
    \ int] = {}\n        self.less_sum = zero\n        self.less_length  = 0\n\n \
    \       self.__add = add\n        self.__neg = neg\n        self.__sub: Callable[[OrderedGroup,\
    \ OrderedGroup], OrderedGroup] = lambda x, y: add(x, neg(y))\n\n    @property\n\
    \    def reversal(self) -> int:\n        return self.__reversal\n\n    def _more_insert(self,\
    \ x: OrderedGroup):\n        self.more_sum = self.__add(self.more_sum, x)\n  \
    \      self.more_length += 1\n\n        if x in self.more_count:\n           \
    \ self.more_count[x] += 1\n        else:\n            self.more_count[x] = 1\n\
    \            heappush(self.more, x)\n\n    def _less_insert(self, x: OrderedGroup):\n\
    \        self.less_sum = self.__add(self.less_sum, x)\n        self.less_length\
    \ += 1\n\n        if x in self.less_count:\n            self.less_count[x] +=\
    \ 1\n        else:\n            self.less_count[x] = 1\n            heappush(self.less,\
    \ -x)\n\n    def _more_discard(self, x: OrderedGroup):\n        self.more_sum\
    \ = self.__sub(self.more_sum, x)\n        self.more_length -= 1\n        self.more_count[x]\
    \ -= 1\n\n        if self.more_count[x] == 0:\n            del self.more_count[x]\n\
    \n        while self.more and (self.more[0] not in self.more_count):\n       \
    \     heappop(self.more)\n\n    def _less_discard(self, x: OrderedGroup):\n  \
    \      self.less_sum = self.__sub(self.less_sum, x)\n        self.less_length\
    \ -= 1\n        self.less_count[x] -= 1\n\n        if self.less_count[x] == 0:\n\
    \            del self.less_count[x]\n\n        while self.less and (-self.less[0]\
    \ not in self.less_count):\n            heappop(self.less)\n\n    def _more_to_less(self):\n\
    \        x = self.more[0]\n        self._more_discard(x)\n        self._less_insert(x)\n\
    \n    def _less_to_more(self):\n        x = -self.less[0]\n        self._less_discard(x)\n\
    \        self._more_insert(x)\n\n    def _validation(self):\n        if self.more_length\
    \ > self.K:\n            while self.more_length > self.K:\n                self._more_to_less()\n\
    \        elif self.more_length < self.K:\n            while self.less_length >\
    \ 0 and self.more_length < self.K:\n                self._less_to_more()\n\n \
    \   def __len__(self) -> int:\n        return self.more_length + self.less_length\n\
    \n    def __contains__(self, value: OrderedGroup) -> bool:\n        return (value\
    \ in self.more_count) or (value in self.less_count)\n\n    def count(self, value:\
    \ OrderedGroup) -> int:\n        return self.more_count(value, 0) + self.less_count(value,\
    \ 0)\n\n    def insert(self, x: OrderedGroup):\n        if self.reversal:\n  \
    \          x = self.__neg(x)\n\n        self._more_insert(x)\n        self._validation()\n\
    \n    def discard(self, x: OrderedGroup):\n        if self.reversal:\n       \
    \     x = self.__neg(x)\n\n        if x not in self:\n            return\n\n \
    \       if x >= self.more[0]:\n            self._more_discard(x)\n        else:\n\
    \            self._less_discard(x)\n        self._validation()\n\n    def best_sum(self)\
    \ -> OrderedGroup:\n        assert not self.reversal\n        return self.more_sum\n\
    \n    def worst_sum(self) -> OrderedGroup:\n        assert self.reversal\n   \
    \     return self.__neg(self.more_sum)\n\n    def all_sum(self) -> OrderedGroup:\n\
    \        return self.sign * self.__add(self.more_sum, self.less_sum)\n\n    def\
    \ change_K(self, K: int):\n        self.K = max(0, K)\n        self._validation()\n\
    \nclass Worst_Sum(Best_Sum[OrderedGroup]):\n    def __init__(self, K: int, add:\
    \ Callable[[OrderedGroup, OrderedGroup], OrderedGroup], neg: Callable[[OrderedGroup],\
    \ OrderedGroup], zero: OrderedGroup, reversal: bool = False):\n        Best_Sum.__init__(self,\
    \ K, add, neg, zero, not reversal)\n"
  dependsOn: []
  isVerificationFile: false
  path: Best_Sum.py
  requiredBy: []
  timestamp: '2025-06-22 12:24:47+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Best_Sum.py
layout: document
redirect_from:
- /library/Best_Sum.py
- /library/Best_Sum.py.html
title: Best_Sum.py
---
