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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.13.1/x64/lib/python3.13/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.13.1/x64/lib/python3.13/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class Sliding_Window_Aggregation_Both_Sides:\n    def __init__(self, op):\n\
    \        \"\"\" \u4E21\u5074\u30B9\u30E9\u30A4\u30C9\u30D7\u30ED\u30C0\u30AF\u30C8\
    \u30AF\u30E9\u30B9\u3092\u751F\u6210\u3059\u308B.\n\n        op: 2\u9805\u6F14\
    \u7B97 (\u534A\u7FA4)\n        \u203Bop\u306B\u3064\u3044\u3066, front \u306F\u5DE6\
    \u304B\u3089, back \u306F\u53F3\u304B\u3089\u884C\u3046.\n        \"\"\"\n\n \
    \       self.op=op\n        self.left_value=[]\n        self.left_prod=[]\n  \
    \      self.right_value=[]\n        self.right_prod=[]\n\n    def __str__(self):\n\
    \        if self.left_value:\n            if self.right_value:\n             \
    \   return str(self.left_value[::-1])[:-1]+\", \"+str(self.right_value)[1:]\n\
    \            else:\n                return str(self.left_value[::-1])\n      \
    \  else:\n            return str(self.right_value)\n\n    def __repr__(self):\n\
    \        return \"Slide Product Both Side: \"+str(self)+\": product: {}\".format(self.product())\n\
    \n    def __len__(self):\n        return len(self.left_value)+len(self.right_value)\n\
    \n    def __bool__(self):\n        return bool(len(self))\n\n    def push_front(self,\
    \ x):\n        self.left_value.append(x)\n        if self.left_prod:\n       \
    \     self.left_prod.append(self.op(x, self.left_prod[-1]))\n        else:\n \
    \           self.left_prod.append(x)\n\n    def push_back(self, x):\n        self.right_value.append(x)\n\
    \        if self.right_prod:\n            self.right_prod.append(self.op(self.right_prod[-1],\
    \ x))\n        else:\n            self.right_prod.append(x)\n\n    def pop_front(self):\n\
    \        if not self.left_prod:\n            rm=len(self.right_prod)//2\n    \
    \        lm=len(self.right_prod)-rm\n\n            self.right_prod.clear()\n \
    \           T=[self.right_value.pop() for _ in range(rm)]\n\n            for _\
    \ in range(lm):\n                y=self.right_value.pop()\n                self.left_value.append(y)\n\
    \                if self.left_prod:\n                    self.left_prod.append(self.op(y,\
    \ self.left_prod[-1]))\n                else:\n                    self.left_prod.append(y)\n\
    \n            for _ in range(rm):\n                y=T.pop()\n               \
    \ self.right_value.append(y)\n                if self.right_prod:\n          \
    \          self.right_prod.append(self.op(self.right_prod[-1], y))\n         \
    \       else:\n                    self.right_prod.append(y)\n\n        self.left_value.pop()\n\
    \        self.left_prod.pop()\n\n    def pop_back(self):\n        if not self.right_prod:\n\
    \            lm=len(self.left_prod)//2\n            rm=len(self.left_prod)-lm\n\
    \n            self.left_prod.clear()\n            T=[self.left_value.pop() for\
    \ _ in range(lm)]\n\n            for _ in range(rm):\n                y=self.left_value.pop()\n\
    \                self.right_value.append(y)\n                if self.right_prod:\n\
    \                    self.right_prod.append(self.op(self.right_prod[-1], y))\n\
    \                else:\n                    self.right_prod.append(y)\n\n    \
    \        for _ in range(lm):\n                y=T.pop()\n                self.left_value.append(y)\n\
    \                if self.left_prod:\n                    self.left_prod.append(self.op(y,\
    \ self.left_prod[-1]))\n                else:\n                    self.left_prod.append(y)\n\
    \n        self.right_value.pop()\n        self.right_prod.pop()\n\n    def product(self,\
    \ default=None):\n        if self.right_prod:\n            if self.left_prod:\n\
    \                return self.op(self.left_prod[-1], self.right_prod[-1])\n   \
    \         else:\n                return self.right_prod[-1]\n        else:\n \
    \           if self.left_prod:\n                return self.left_prod[-1]\n  \
    \          else:\n                return default\n\n    def clear(self):\n   \
    \     \"\"\" \u521D\u671F\u5316\u3059\u308B. \"\"\"\n\n        self.left_value.clear()\n\
    \        self.left_prod.clear()\n        self.right_value.clear()\n        self.right_prod.clear()\n\
    \n"
  dependsOn: []
  isVerificationFile: false
  path: Sliding_Window_Aggregation_Both_Sides.py
  requiredBy: []
  timestamp: '2023-03-20 03:47:37+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Sliding_Window_Aggregation_Both_Sides.py
layout: document
redirect_from:
- /library/Sliding_Window_Aggregation_Both_Sides.py
- /library/Sliding_Window_Aggregation_Both_Sides.py.html
title: Sliding_Window_Aggregation_Both_Sides.py
---
