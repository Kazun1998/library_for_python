---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test_verify/yosupo_library_checker/Data_Structure/Associative_Array.test.py
    title: test_verify/yosupo_library_checker/Data_Structure/Associative_Array.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.13.5/x64/lib/python3.13/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.13.5/x64/lib/python3.13/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from random import randint\nfrom typing import TypeVar, Generic, Optional,\
    \ Hashable\n\nV = TypeVar('V')\nclass Hash_Table(Generic[V]):\n    __slots__ =\
    \ (\"__table\", \"__seed\")\n\n    def __init__(self):\n        self.__table:\
    \ dict[Hashable, V] = {}\n        self.__seed = randint(-(1 << 63) - 1, (1 <<\
    \ 63) - 1)\n\n    @property\n    def seed(self) -> int:\n        return self.__seed\n\
    \n    def get(self, key: Hashable, default: V = None) -> Optional[V]:\n      \
    \  return self.__table.get(key^self.seed, default)\n\n    def __len__(self) ->\
    \ int:\n        return len(self.__table)\n\n    def __getitem__(self, key: Hashable)\
    \ -> V:\n        k = hash(key) ^ self.seed\n        if k in self.__table:\n  \
    \          return self.__table[k]\n        else:\n            raise KeyError(key)\n\
    \n    def __setitem__(self, key: Hashable, value: V):\n        self.__table[hash(key)\
    \ ^ self.seed] = value\n\n    def __iter__(self):\n        return self.keys()\n\
    \n    def __contains__(self, key: Hashable) -> bool:\n        return hash(key)\
    \ ^ self.seed in self.__table\n\n    def clear(self):\n        self.__table.clear()\n\
    \n    def keys(self):\n        for alpha in self.__table:\n            yield alpha\
    \ ^ self.seed\n\n    def values(self):\n        return self.__table.values()\n\
    \n    def items(self):\n        for alpha in self.__table:\n            yield\
    \ (alpha ^ self.seed, self.__table[alpha])\n\nclass Hash_Set:\n    def __init__(self):\n\
    \        self.__set: set[int] = set()\n        self.__seed = randint(-(1 << 63)\
    \ - 1, (1 << 63) - 1)\n\n    @property\n    def seed(self) -> int:\n        return\
    \ self.__seed\n\n    def add(self, value: Hashable):\n        self.__set.add(hash(value)\
    \ ^ self.seed)\n\n    def __contains__(self, value: Hashable) -> bool:\n     \
    \   return hash(value) ^ self.seed in self.set\n"
  dependsOn: []
  isVerificationFile: false
  path: Hash_Table.py
  requiredBy: []
  timestamp: '2025-06-22 01:08:49+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test_verify/yosupo_library_checker/Data_Structure/Associative_Array.test.py
documentation_of: Hash_Table.py
layout: document
redirect_from:
- /library/Hash_Table.py
- /library/Hash_Table.py.html
title: Hash_Table.py
---
