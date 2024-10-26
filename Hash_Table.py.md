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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.7/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.7/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class Hash_Table:\n    __slots__=(\"table\", \"seed\")\n\n    def __init__(self):\n\
    \        from random import randint\n        self.table={}\n        self.seed=randint(-(1<<63)-1,\
    \ (1<<63)-1)\n\n    def get(self, key, default=None):\n        return self.table.get(key^self.seed,\
    \ default)\n\n    def __len__(self):\n        return len(self.table)\n\n    def\
    \ __getitem__(self, key):\n        h=key^self.seed\n        if h in self.table:\n\
    \            return self.table[h]\n        else:\n            raise KeyError(key)\n\
    \n    def __setitem__(self, key, value):\n        self.table[key^self.seed]=value\n\
    \n    def __iter__(self):\n        return self.keys()\n\n    def __contains__(self,\
    \ key):\n        return key^self.seed in self.table\n\n    def clear(self):\n\
    \        self.table.clear()\n\n    def keys(self):\n        for alpha in self.table:\n\
    \            yield alpha^self.seed\n\n    def values(self):\n        return self.table.values()\n\
    \n    def items(self):\n        for alpha in self.table:\n            yield (alpha^self.seed,\
    \ self.table[alpha])\n\nclass Hash_Set:\n    def __init__(self):\n        from\
    \ random import randint\n        self.set=set()\n        self.seed=randint(-(1<<63)-1,\
    \ (1<<63)-1)\n\n    def add(self, value):\n        self.set.add(value^self.seed)\n\
    \n    def __contains__(self, value):\n        return value^self.seed in self.set\n"
  dependsOn: []
  isVerificationFile: false
  path: Hash_Table.py
  requiredBy: []
  timestamp: '2022-11-24 23:18:10+09:00'
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
