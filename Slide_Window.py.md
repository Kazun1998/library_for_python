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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.7/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.7/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class Slide_Window():\n    \"\"\" \u7A4D\u3092\u30B9\u30E9\u30A4\u30C9\u3055\
    \u305B\u306A\u304C\u3089\u3082\u3068\u3081\u308B.\n    \"\"\"\n\n    __slots__=(\"\
    calc\", \"__front\", \"__back\", \"__left\", \"__right\", \"__cnt\")\n\n    def\
    \ __init__(self,calc,X=[]):\n        \"\"\"\u30B9\u30E9\u30A4\u30C9\u30D7\u30ED\
    \u30C0\u30AF\u30C8\u30AF\u30E9\u30B9\u3092\u751F\u6210\u3059\u308B.\n\n      \
    \  calc: 2\u9805\u6F14\u7B97 (\u534A\u7FA4)\n        \u203Bcalc\u306B\u3064\u3044\
    \u3066, \u53F3\u304B\u3089\u65B0\u3057\u3044\u9805\u3092\u52A0\u3048\u308B\u3053\
    \u3068.\n        \"\"\"\n        from collections import deque\n        self.calc=calc\n\
    \        self.__front=deque()\n        self.__left=deque()\n        self.__back=deque()\n\
    \        self.__right=deque()\n        self.__cnt=0\n\n        for x in X:\n \
    \           if self.__right:\n                self.__right.append(self.calc(self.__right[-1],\
    \ x))\n            else:\n                self.__right.append(x)\n\n         \
    \   self.__cnt+=1\n            self.__back.append(x)\n\n    def __str__(self):\n\
    \        if self.__front:\n            if self.__back:\n                return\
    \ str(self.__front)[6:-2]+\", \"+str(self.__back)[7:-1]\n            else:\n \
    \               return str(self.__front)[6:-1]\n        else:\n            return\
    \ str(self.__back)[6:-1]\n\n    __repr__=__str__\n\n    def __len__(self):\n \
    \       return self.__cnt\n\n    def __bool__(self):\n        return self.__cnt>0\n\
    \n    def push(self, x, k=1):\n        \"\"\" x \u3092 k \u56DE push \u3059\u308B\
    .\n\n        x: value\n        k: \u56DE\u6570\n        \"\"\"\n\n        for\
    \ _ in range(k):\n            self.__cnt+=1\n\n            self.__back.append(x)\n\
    \n            if self.__right:\n                self.__right.append(self.calc(self.__right[-1],x))\n\
    \            else:\n                self.__right.append(x)\n\n    def pop(self,\
    \ k=1):\n        \"\"\" k \u56DE push \u3059\u308B.\n\n        k: \u56DE\u6570\
    \n        \"\"\"\n\n        for _ in range(min(k,self.__cnt)):\n            if\
    \ not self.__front:\n                self.__right.clear()\n                while\
    \ self.__back:\n                    x=self.__back.pop()\n\n                  \
    \  if self.__front:\n                        self.__left.appendleft(self.calc(x,self.__left[0]))\n\
    \                    else:\n                        self.__left.appendleft(x)\n\
    \                    self.__front.appendleft(x)\n\n            self.__front.popleft()\n\
    \            self.__left.popleft()\n\n        self.__cnt-=min(k,self.__cnt)\n\n\
    \    def product(self, default=None):\n        \"\"\" \u7A4D\u3092\u6C42\u3081\
    \u308B.\n\n        default: \u7A7A\u306E\u3068\u304D\u306E\u8FD4\u308A\u5024\u3092\
    \u8A2D\u5B9A\u3059\u308B.\n        \"\"\"\n\n        if self.__front:\n      \
    \      if self.__back:\n                return self.calc(self.__left[0],self.__right[-1])\n\
    \            else:\n                return self.__left[0]\n        else:\n   \
    \         if self.__back:\n                return self.__right[-1]\n         \
    \   else:\n                return default\n\n    def clear(self):\n        \"\"\
    \" \u521D\u671F\u5316\u3059\u308B. \"\"\"\n\n        self.__front.clear()\n  \
    \      self.__back.clear()\n        self.__left.clear()\n        self.__right.clear()\n\
    \        self.__cnt=0\n"
  dependsOn: []
  isVerificationFile: false
  path: Slide_Window.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Slide_Window.py
layout: document
redirect_from:
- /library/Slide_Window.py
- /library/Slide_Window.py.html
title: Slide_Window.py
---