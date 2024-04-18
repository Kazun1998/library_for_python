---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Double_Heap.py
    title: Double_Heap.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.3/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.3/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from Double_Heap import *\n\nclass Median:\n    def __init__(self):\n   \
    \     self.left=Double_Heap()\n        self.right=Double_Heap()\n\n    def __bool__(self):\n\
    \        return bool(self.left) or bool(self.right)\n\n    def __len__(self):\n\
    \        return len(self.left)+len(self.right)\n\n    def __contains__(self, x):\n\
    \        return (x in self.left) or (x in self.right)\n\n    def push(self, x):\n\
    \        \"\"\" \u8981\u7D20 x \u3092\u8FFD\u52A0\u3059\u308B. \"\"\"\n\n    \
    \    if len(self.left)==len(self.right):\n            u=self.right.get_min() if\
    \ self.right else float(\"inf\")\n            if x>u:\n                v=self.right.pop_min()\n\
    \                self.left.push(v)\n                self.right.push(x)\n     \
    \       else:\n                self.left.push(x)\n        else:\n            u=self.left.get_max()\n\
    \            if x>u:\n                self.right.push(x)\n            else:\n\
    \                v=self.left.pop_max()\n                self.left.push(x)\n  \
    \              self.right.push(v)\n\n    def erase(self,x):\n        \"\"\" \u8981\
    \u7D20 x \u3092\u524A\u9664\u3059\u308B. \"\"\"\n\n        assert x in self\n\
    \        alpha=self.left.get_max() if self.left else -float(\"inf\")\n       \
    \ if len(self.left)==len(self.right):\n            if x<=alpha:\n            \
    \    self.left.discard(x)\n                y=self.right.pop_min()\n          \
    \      self.left.push(y)\n            else:\n                self.right.discard(x)\n\
    \        else:\n            if x<=alpha:\n                self.left.discard(x)\n\
    \            else:\n                self.right.discard(x)\n                y=self.left.pop_max()\n\
    \                self.right.push(y)\n\n    def get_median(self,mode=0,func=None):\n\
    \        \"\"\" \u4E2D\u592E\u5024\u3092\u6C42\u3081\u308B.\n\n        [mode]\
    \ \u9805\u306E\u6570\u304C\u5076\u6570\u306E\u3068\u304D\u306E\u4E2D\u592E\u5024\
    \u306E\u6C42\u3081\u65B9\u3092\u6307\u5B9A\u3059\u308B (\u305D\u306E 2\u5024\u3092\
    \ a,b (a<=b) \u3068\u3059\u308B).\n        mode=-1 \u2192 a\n        mode=0  \u2192\
    \ (a+b)/2\n        mode=1 \u2192 b\n        mode=(\u305D\u306E\u4ED6) \u2192 \u305D\
    \u306E\u4ED6 ( 2\u5909\u6570\u95A2\u6570 func(a,b) \u3067\u6307\u5B9A)\n     \
    \   \"\"\"\n\n        assert self, \"\u30AD\u30E5\u30FC\u304C\u7A7A\u3067\u3059\
    \"\n\n        if len(self)%2==1:\n            return self.left.get_max()\n   \
    \     else:\n            if mode==-1:\n                return self.left.get_max()\n\
    \            elif mode==1:\n                return self.right.get_min()\n    \
    \        else:\n                a=self.left.get_max()\n                b=self.right.get_min()\n\
    \n                if mode==0:\n                    return (a+b)/2\n          \
    \      else:\n                    return func(a,b)\n"
  dependsOn:
  - Double_Heap.py
  isVerificationFile: false
  path: Median.py
  requiredBy: []
  timestamp: '2022-12-11 17:04:31+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Median.py
layout: document
redirect_from:
- /library/Median.py
- /library/Median.py.html
title: Median.py
---
