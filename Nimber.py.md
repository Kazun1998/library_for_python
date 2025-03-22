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
  code: "class Nimber:\n    def __init__(self, x: int = 0):\n        if type(x) is\
    \ str:\n            x = int(x)\n\n        self.__x = x\n\n    def __eq__(self,\
    \ other: \"Nimber\") -> bool:\n        return self.__x == other.__x\n\n    def\
    \ __str__(self) -> str:\n        return str(self.__x)\n\n    def __repr__(self)\
    \ -> str:\n        return f\"{self.__class__.__name__}({self.__x})\"\n\n    def\
    \ __pos__(self) -> \"Nimber\":\n        return Nimber(self.__x)\n\n    def __neg__(self)\
    \ -> \"Nimber\":\n        return Nimber(self.__x)\n\n    def __add__(self, other:\
    \ \"Nimber\") -> \"Nimber\":\n        return Nimber(self.__x ^ other.__x)\n\n\
    \    def __sub__(self, other: \"Nimber\") -> \"Nimber\":\n        return Nimber(self.__x\
    \ ^ other.__x)\n\n    def __mul__(self, other: \"Nimber\") -> \"Nimber\":\n  \
    \      lv = max(self.level(self.__x), self.level(other.__x))\n        return Nimber(self.__mul_calc(self.__x,\
    \ other.__x, lv))\n\n    __SMALL_NIM_PRODUCT_MEMO = [[-1] * 256 for _ in range(256)]\n\
    \    __SMALL_NIM_PRODUCT_MEMO[0][0] = __SMALL_NIM_PRODUCT_MEMO[0][1] = __SMALL_NIM_PRODUCT_MEMO[1][0]\
    \ = 0\n    __SMALL_NIM_PRODUCT_MEMO[1][1] = 1\n\n    @classmethod\n    def __mul_calc(cls,\
    \ x: int, y: int, lv: int) -> int:\n        if lv <= 3 and cls.__SMALL_NIM_PRODUCT_MEMO[x][y]\
    \ != -1:\n            return cls.__SMALL_NIM_PRODUCT_MEMO[x][y]\n\n        x1,\
    \ x0 = cls.separate(x, lv)\n        y1, y0 = cls.separate(y, lv)\n\n        p\
    \ = cls.__mul_calc(x0, y0, lv - 1)\n        e = 1 << (1 << (lv - 1))\n\n     \
    \   a = p ^ cls.__mul_calc(x0 ^ x1, y0 ^ y1, lv - 1) * e\n        b = cls.__mul_calc(cls.__mul_calc(x1,\
    \ y1, lv - 1), e >> 1, lv - 1)\n\n        res = (p * e) ^ a ^ b\n        if lv\
    \ <= 3:\n            cls.__SMALL_NIM_PRODUCT_MEMO[x][y] = res\n\n        return\
    \ res\n\n    def __truediv__(self, other: \"Nimber\") -> \"Nimber\":\n       \
    \ return self * other.inverse()\n\n    @staticmethod\n    def __floor_log(x: int)\
    \ -> int:\n        return x.bit_length() - 1\n\n    @staticmethod\n    def separate(x:\
    \ int, lv: int):\n        if lv == 0:\n            raise ValueError\n\n      \
    \  upper = x >> (1 << (lv - 1))\n        lower = x ^ (upper << (1 << (lv - 1)))\n\
    \        return upper, lower\n\n    @classmethod\n    def level(cls, x: int) ->\
    \ int:\n        if x == 0:\n            return 0\n        else:\n            return\
    \ cls.__floor_log(cls.__floor_log(x)) + 1\n\n    def __hash__(self) -> int:\n\
    \        return hash(self.__x)\n\n    @classmethod\n    def __square_calc(cls,\
    \ x: int, lv: int) -> int:\n        if lv <= 3 and cls.__SMALL_NIM_PRODUCT_MEMO[x][x]\
    \ != -1:\n            return cls.__SMALL_NIM_PRODUCT_MEMO[x][x]\n\n        x1,\
    \ x0 = cls.separate(x, lv)\n\n        x1_square = cls.__square_calc(x1, lv - 1)\n\
    \        x0_square = cls.__square_calc(x0, lv - 1)\n        e = 1 << (1 << (lv\
    \ - 1))\n\n        res = (x1_square * e) ^ cls.__mul_calc(cls.__mul_calc(x1, x1,\
    \ lv - 1), e >> 1, lv - 1) ^ x0_square\n        if lv <= 3:\n            cls.__SMALL_NIM_PRODUCT_MEMO[x][x]\
    \ = res\n\n        return res\n\n    def square(self) -> \"Nimber\":\n       \
    \ \"\"\" \u81EA\u5206\u81EA\u8EAB\u306E\u81EA\u4E57\u3092\u6C42\u3081\u308B.\n\
    \n        Returns:\n            Nimber: self * self\n        \"\"\"\n        return\
    \ Nimber(self.__square_calc(self.__x, self.level(self.__x)))\n\n    def __pow__(self,\
    \ n: int) -> \"Nimber\":\n        x = self\n        y = Nimber(1)\n        while\
    \ n:\n            if n & 1:\n                y *= x\n            x = x.square()\n\
    \            n >>= 1\n\n        return y\n\n    def inverse(self):\n        return\
    \ pow(self, (1 << (1 << self.level(self.__x))) - 2)\n"
  dependsOn: []
  isVerificationFile: false
  path: Nimber.py
  requiredBy: []
  timestamp: '2025-03-22 22:31:05+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Nimber.py
layout: document
redirect_from:
- /library/Nimber.py
- /library/Nimber.py.html
title: Nimber.py
---
