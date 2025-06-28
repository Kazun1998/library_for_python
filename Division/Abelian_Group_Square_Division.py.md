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
  code: "from typing import TypeVar, Generic, Callable\n\nG = TypeVar('G')\nclass\
    \ Abelian_Group_Square_Division(Generic[G]):\n    def __init__(self, data: list[G],\
    \ op: Callable[[G, G], G], zero: G, neg: Callable[[G], G]):\n        \"\"\" \u53EF\
    \u63DB\u7FA4 G \u306E\u5217\u306B\u5BFE\u3059\u308B\u5E73\u65B9\u5206\u5272\u306E\
    \u5834\u3092\u8A2D\u5B9A\u3059\u308B.\n\n        Args:\n            data (list[G]):\
    \ G \u306E\u5217\n            op (Callable[[G, G], G]): G \u4E0A\u306E\u6F14\u7B97\
    \n            zero (G): G \u306E\u5358\u4F4D\u5143\n            neg (Callable[[G],\
    \ G]): G \u4E0A\u306E\u9006\u5143\u95A2\u6570\n        \"\"\"\n\n        self.__op\
    \ = op\n        self.__zero = zero\n        self.__neg = neg\n\n        n = len(data)\n\
    \        self.__bucket_size = int(pow(n, 0.5) + 1)\n        self.__bucket_number\
    \ = (n - 1) // self.bucket_size + 1\n\n        upper = self.__upper = [zero] *\
    \ self.bucket_number\n        lower = self.__lower = [zero] * self.bucket_number\
    \ * self.bucket_size\n\n        for i in range(n):\n            lower[i] = data[i]\n\
    \n            j = i // self.bucket_size\n            upper[j] = op(upper[j], lower[i])\n\
    \n    @property\n    def zero(self) -> G:\n        return self.__zero\n\n    @property\n\
    \    def bucket_number(self) -> int:\n        return self.__bucket_number\n\n\
    \    @property\n    def bucket_size(self) -> int:\n        return self.__bucket_size\n\
    \n    def add(self, k: int, x: G):\n        \"\"\" \u7B2C k \u8981\u7D20\u306B\
    \ x \u3092\u8FFD\u52A0\u3059\u308B.\n\n        Args:\n            k (int): \u8981\
    \u7D20\u306E\u5834\u6240\n            x (G): \u8FFD\u52A0\u3059\u308B\u8981\u7D20\
    \n        \"\"\"\n\n        self.__lower[k] = self.__op(self.__lower[k], x)\n\n\
    \        j = k // self.bucket_size\n        self.__upper[j] = self.__op(self.__upper[j],\
    \ x)\n\n    def update(self, k: int, y: G):\n        \"\"\" \u7B2C k \u8981\u7D20\
    \u3092 y \u306B\u5909\u66F4\u3059\u308B.\n\n        Args:\n            k (int):\
    \ \u8981\u7D20\u306E\u5834\u6240\n            y (G): \u5909\u66F4\u5F8C\u306E\u5024\
    \n        \"\"\"\n\n        diff = self.__op(self.__neg(self.__lower[k]), y)\n\
    \        self.add(k, diff)\n\n    def sum(self, l: int, r: int, left_close: bool\
    \ = True, right_close: bool = True) -> G:\n        \"\"\" \u7B2C l \u8981\u7D20\
    \u304B\u3089\u7B2C r \u8981\u7D20\u306E\u7DCF\u548C\u3092\u6C42\u3081\u308B.\n\
    \n        Args:\n            l (int): \u5DE6\u7AEF\n            r (int): \u53F3\
    \u7AEF\n            left_close (bool, optional): False \u306B\u3059\u308B\u3068\
    , \u5DE6\u7AEF\u304C\u958B\u533A\u9593\u306B\u306A\u308B. Defaults to True.\n\
    \            right_close (bool, optional): False \u306B\u306A\u308B\u3068, \u53F3\
    \u7AEF\u304C\u958B\u533A\u9593\u306B\u306A\u308B. Defaults to True.\n\n      \
    \  Returns:\n            G: \u7DCF\u548C\n        \"\"\"\n\n        if not left_close:\n\
    \            l += 1\n\n        if not right_close:\n            r -= 1\n\n   \
    \     b = self.bucket_size\n        op = self.__op\n        lower = self.__lower\n\
    \        upper = self.__upper\n        res = self.zero\n\n        if l // b ==\
    \ r // b:\n            for i in range(l, r + 1):\n                res = op(res,\
    \ lower[i])\n            return res\n\n        while l % b != 0:\n           \
    \ res = op(res, lower[l])\n            l += 1\n\n        while l + (b - 1) <=\
    \ r:\n            res = op(res, upper[l // b])\n            l += b\n\n       \
    \ while l <= r:\n            res = op(res, lower[l])\n            l += 1\n\n \
    \       return res\n\n    def __getitem__(self, k: int) -> G:\n        return\
    \ self.__lower[k]\n"
  dependsOn: []
  isVerificationFile: false
  path: Division/Abelian_Group_Square_Division.py
  requiredBy: []
  timestamp: '2025-05-11 01:45:00+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Division/Abelian_Group_Square_Division.py
layout: document
redirect_from:
- /library/Division/Abelian_Group_Square_Division.py
- /library/Division/Abelian_Group_Square_Division.py.html
title: Division/Abelian_Group_Square_Division.py
---
