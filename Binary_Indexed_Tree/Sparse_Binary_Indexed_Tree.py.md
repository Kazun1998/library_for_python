---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test_verify/yosupo_library_checker/Data_Structure/Sparse_Binary_Indexed_Tree.test.py
    title: test_verify/yosupo_library_checker/Data_Structure/Sparse_Binary_Indexed_Tree.test.py
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
  code: "from typing import TypeVar, Generic, Callable\n\nG = TypeVar('G')\nclass\
    \ Sparse_Binary_Indexed_Tree(Generic[G]):\n    def __init__(self, N: int, op:\
    \ Callable[[G, G], G], zero: G, neg: Callable[[G], G]):\n        \"\"\" op \u3092\
    \u7FA4 G \u306E\u6F14\u7B97\u3068\u3064\u3059\u308B N \u8981\u7D20\u3092\u6301\
    \u3064\u758E Binary Indexed Tree \u3092\u751F\u6210\u3059\u308B.\n\n        Args:\n\
    \            N (int): \u8981\u7D20\u6570\n            op (Callable[[G, G], G]):\
    \ \u7FA4\u6F14\u7B97\n            zero (G): \u7FA4 G \u306B\u304A\u3051\u308B\u5358\
    \u4F4D\u5143 (\u4EFB\u610F\u306E x in G \u306B\u5BFE\u3057\u3066, x + e = e +\
    \ x = x \u3068\u306A\u308B e in G)\n            neg (Callable[[G], G]): x in G\
    \ \u306B\u304A\u3051\u308B\u9006\u5143 (x + y = y + x = e \u3068\u306A\u308B y)\
    \ \u3092\u6C42\u3081\u308B\u95A2\u6570\n        \"\"\"\n\n        self.op = op\n\
    \        self.zero = zero\n        self.neg = neg\n        self.__N = N\n    \
    \    self.__log = max(N.bit_length() - 1, 1)\n        self.data: dict[int, G]\
    \ = {}\n\n    @property\n    def N(self) -> int:\n        return self.__N\n\n\
    \    @property\n    def log(self) -> int:\n        return self.__log\n\n    def\
    \ get(self, k: int) -> G:\n        \"\"\" \u7B2C k \u8981\u7D20\u306E\u5024\u3092\
    \u51FA\u529B\u3059\u308B.\n\n        Args:\n            k (int): \u8981\u7D20\u756A\
    \u53F7\n\n        Returns:\n            G: \u7B2C k \u8981\u7D20\n        \"\"\
    \"\n        return self.sum(k, k)\n\n    def add(self, k: int, x: G):\n      \
    \  \"\"\" \u7B2C k \u8981\u7D20\u306B x \u3092\u52A0\u3048, \u66F4\u65B0\u3092\
    \u884C\u3046.\n\n        Args:\n            k (int): \u8981\u7D20\u756A\u53F7\n\
    \            x (G): \u52A0\u7B97\u3059\u308B\u8981\u7D20\n        \"\"\"\n\n \
    \       data = self.data\n        op = self.op\n\n        p = k + 1\n        while\
    \ p <= self.N:\n            data[p] = op(data.get(p, self.zero), x)\n        \
    \    p += p & (-p)\n\n    def update(self, k: int, x: G):\n        \"\"\" \u7B2C\
    \ k \u8981\u7D20\u3092 x \u306B\u5909\u3048, \u66F4\u65B0\u3092\u884C\u3046.\n\
    \n        Args:\n            k (int): \u8981\u7D20\u756A\u53F7\n            x\
    \ (G): \u5909\u66F4\u5F8C\u306E\u5024\n        \"\"\"\n\n        a = self.get(k)\n\
    \        y = self.op(self.neg(a), x)\n\n        self.add(k, y)\n\n    def sum(self,\
    \ l: int, r: int) -> G:\n        \"\"\" \u7B2C l \u9805\u304B\u3089\u7B2C r \u9805\
    \u307E\u3067\u306E\u7DCF\u548C\u3092\u6C42\u3081\u308B (\u305F\u3060\u3057, l\
    \ != 0 \u306E\u3068\u304D\u306F G \u304C\u7FA4\u3067\u306A\u304F\u3066\u306F\u306A\
    \u3089\u306A\u3044).\n\n        Args:\n            l (int): \u5DE6\u7AEF\n   \
    \         r (int): \u53F3\u7AEF\n\n        Returns:\n            G: \u7DCF\u548C\
    \n        \"\"\"\n\n        l = l + 1 if 0 <= l else 1\n        r = r + 1 if r\
    \ < self.N else self.N\n\n        if l > r:\n            return self.zero\n  \
    \      elif l == 1:\n            return self.__section(r)\n        else:\n   \
    \         return self.op(self.neg(self.__section(l - 1)), self.__section(r))\n\
    \n    def __section(self, x: int) -> G:\n        \"\"\" B[0] + B[1] + ... + B[x]\
    \ \u3092\u6C42\u3081\u308B.\n\n        Args:\n            x (int): \u53F3\u7AEF\
    \n\n        Returns:\n            G: \u7DCF\u548C\n        \"\"\"\n\n        data\
    \ = self.data\n        op = self.op\n\n        total = self.zero\n        while\
    \ x > 0:\n            total = op(data.get(x, self.zero), total)\n            x\
    \ -= x & (-x)\n        return total\n\n    def all_sum(self) -> G:\n        \"\
    \"\" B[0] + B[1] + ... + B[len(B) - 1] \u3092\u6C42\u3081\u308B.\n\n        Returns:\n\
    \            G: \u7DCF\u548C\n        \"\"\"\n\n        return self.sum(0, self.N\
    \ - 1)\n\n    def binary_search(self, cond: Callable[[int], bool]) -> int:\n \
    \       \"\"\" cond(B[0] + B[1] + ... + B[k]) \u304C True \u306B\u306A\u308B\u6700\
    \u5C0F\u306E k \u3092\u6B62\u3081\u308B.\n\n        \u203B G \u306F\u9806\u5E8F\
    \u7FA4\u3067\u3042\u308B\u5FC5\u8981\u304C\u3042\u308B.\n        \u203B cond(zero)\
    \ = True \u306E\u3068\u304D, \u8FD4\u308A\u5024\u306F -1 \u3068\u3059\u308B.\n\
    \        \u203B cond(B[0] + ... + B[k]) \u306A\u308B k \u304C (0 <= k < N \u306B\
    ) \u5B58\u5728\u3057\u306A\u3044\u5834\u5408, \u8FD4\u308A\u5024\u306F N \u3068\
    \u3059\u308B.\n\n        Args:\n            cond (Callable[[int], bool]): \u5358\
    \u8ABF\u5897\u52A0\u306A\u6761\u4EF6\n\n        Returns:\n            int: cond(B[0]\
    \ + B[1] + ... + B[k]) \u304C True \u306B\u306A\u308B\u6700\u5C0F\u306E k\n  \
    \      \"\"\"\n\n        if cond(self.zero):\n            return -1\n\n      \
    \  j = 0\n        t = 1 << self.log\n        data = self.data\n        op = self.op\n\
    \        alpha = self.zero\n\n        while t > 0:\n            if j + t <= self.N:\n\
    \                beta = op(alpha, data.get(j + t, self.zero))\n              \
    \  if not cond(beta):\n                    alpha = beta\n                    j\
    \ += t\n            t >>= 1\n\n        return j\n\n    def __getitem__(self, index):\n\
    \        if isinstance(index, int):\n            return self.get(index)\n    \
    \    else:\n            return [self.get(t) for t in index]\n\n    def __setitem__(self,\
    \ index: int, val: G):\n        self.update(index, val)\n\n    def __iter__(self):\n\
    \        for k in range(self.N):\n            yield self.sum(k, k)\n"
  dependsOn: []
  isVerificationFile: false
  path: Binary_Indexed_Tree/Sparse_Binary_Indexed_Tree.py
  requiredBy: []
  timestamp: '2025-06-18 00:13:41+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test_verify/yosupo_library_checker/Data_Structure/Sparse_Binary_Indexed_Tree.test.py
documentation_of: Binary_Indexed_Tree/Sparse_Binary_Indexed_Tree.py
layout: document
redirect_from:
- /library/Binary_Indexed_Tree/Sparse_Binary_Indexed_Tree.py
- /library/Binary_Indexed_Tree/Sparse_Binary_Indexed_Tree.py.html
title: Binary_Indexed_Tree/Sparse_Binary_Indexed_Tree.py
---
