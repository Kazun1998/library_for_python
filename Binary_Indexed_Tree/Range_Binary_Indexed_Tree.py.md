---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Binary_Indexed_Tree/Binary_Indexed_Tree.py
    title: Binary Indexed Tree (Fenwick Tree)
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.4/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.4/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from Binary_Indexed_Tree import Binary_Indexed_Tree\n\nclass Range_Binary_Indexed_Tree():\n\
    \    def __init__(self, L, op, zero, neg, mul):\n\n        self.op = op\n    \
    \    self.zero = zero\n        self.neg = neg\n        self.mul = mul\n      \
    \  self.N = len(L)\n\n        self.bit0 = Binary_Indexed_Tree(L, op, zero, neg)\n\
    \        self.bit1 = Binary_Indexed_Tree([zero]*len(L), op, zero, neg)\n\n   \
    \ def get(self, k):\n        \"\"\" \u7B2C k \u8981\u7D20\u306E\u5024\u3092\u51FA\
    \u529B\u3059\u308B.\n\n        k    : \u6570\u5217\u306E\u8981\u7D20\n       \
    \ \"\"\"\n        return self.sum(k, k)\n\n    def add(self, k, x):\n        \"\
    \"\" \u7B2C k \u8981\u7D20\u306B x \u3092\u52A0\u3048, \u66F4\u65B0\u3092\u884C\
    \u3046.\n        k    : \u6570\u5217\u306E\u8981\u7D20\n        x    : \u52A0\u3048\
    \u308B\u5024\n        index: \u5148\u982D\u306E\u8981\u7D20\u306E\u756A\u53F7\n\
    \        \"\"\"\n        self.bit0.add(k, x)\n\n    def update(self, k, x):\n\
    \        self.bit0.add(k, self.op(self.neg(self.get(k)), x))\n\n    def add_range(self,\
    \ l, r, x):\n        \"\"\" \u7B2C l \u8981\u7D20\u304B\u3089\u7B2C r \u8981\u7D20\
    \u307E\u3067\u306B\u4E00\u69D8\u306B x \u3092\u52A0\u3048\u308B.\n\n        Args:\n\
    \            l (int): \u5DE6\u7AEF\n            r (int): \u53F3\u7AEF\n      \
    \      x:\n        \"\"\"\n\n        self.bit0.add(l, self.neg(self.mul(l, x)))\n\
    \        self.bit1.add(l, x)\n        if r < self.N - 1:\n            self.bit0.add(r\
    \ + 1, self.mul(r + 1, x))\n            self.bit1.add(r + 1, self.neg(x))\n\n\
    \    def sum(self, l, r):\n        \"\"\" \u7B2C l \u8981\u7D20\u304B\u3089\u7B2C\
    \ r \u8981\u7D20\u307E\u3067\u306E\u7DCF\u548C\u3092\u6C42\u3081\u308B.\n    \
    \    \u203B l != index \u306A\u3089\u3070, \u7FA4\u3067\u306A\u304F\u3066\u306F\
    \u306A\u3089\u306A\u3044.\n        l : \u59CB\u307E\u308A\n        r   : \u7D42\
    \u308F\u308A\n        index: \u5148\u982D\u306E\u8981\u7D20\u306E\u756A\u53F7\n\
    \        \"\"\"\n        if l > 0:\n            return self.op(self.__section(r),\
    \ self.neg(self.__section(l - 1)))\n        else:\n            return self.__section(r)\n\
    \n    def __section(self, k):\n        return self.op(self.bit0.sum(0, k), self.mul(k\
    \ + 1, self.bit1.sum(0, k)))\n\n    def all_sum(self):\n        return self.sum(0,\
    \ self.N - 1)\n\n    def __getitem__(self, index):\n        if isinstance(index,\
    \ int):\n            return self.get(index)\n        else:\n            return\
    \ [self.get(t) for t in index]\n\n    def __setitem__(self, index, value):\n \
    \       self.update(index, value)\n\n    def __iter__(self):\n        for ind\
    \ in range(self.N):\n            yield self.sum(ind, ind)\n"
  dependsOn:
  - Binary_Indexed_Tree/Binary_Indexed_Tree.py
  isVerificationFile: false
  path: Binary_Indexed_Tree/Range_Binary_Indexed_Tree.py
  requiredBy: []
  timestamp: '2024-04-16 23:39:13+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Binary_Indexed_Tree/Range_Binary_Indexed_Tree.py
layout: document
redirect_from:
- /library/Binary_Indexed_Tree/Range_Binary_Indexed_Tree.py
- /library/Binary_Indexed_Tree/Range_Binary_Indexed_Tree.py.html
title: Binary_Indexed_Tree/Range_Binary_Indexed_Tree.py
---
