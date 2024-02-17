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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.2/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.2/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from heapq import heapify,heappushpop,heappush\nclass Slope_Trick:\n    def\
    \ __init__(self):\n        self.__L=[float(\"inf\")]\n        self.__R=[float(\"\
    inf\")]\n        self.__y_min=0\n        self.__add_L=self.__add_R=0\n\n    def\
    \ get_min(self):\n        return self.__y_min\n\n    def add(self,a):\n      \
    \  self.__y_min+=a\n\n    def add_right(self,a):\n        \"\"\" (x-a)^+:=max(0,x-a)\
    \ \u3092\u52A0\u7B97\u3059\u308B.\n\n        \"\"\"\n        l0=-self.__L[0]\n\
    \        b=-heappushpop(self.__L,-a)\n        heappush(self.__R,b)\n        self.__y_min+=max(0,l0-a)\n\
    \n    def add_left(self,a):\n        \"\"\" (x-a)^-:=max(0,-(x-a)) \u3092\u52A0\
    \u7B97\u3059\u308B.\n\n        \"\"\"\n        r0=self.__R[0]\n        b=heappushpop(self.__R,a)\n\
    \        heappush(self.__L,-b)\n        self.__y_min+=max(0,a-r0)\n\n    def add_both_side(self,a):\n\
    \        \"\"\" abs(x-a) \u3092\u52A0\u7B97\u3059\u308B.\n\n        \"\"\"\n \
    \       self.add_right(a)\n        self.add_left(a)\n\n    def argmin(self):\n\
    \        \"\"\" f(x)=min f \u3092\u6E80\u305F\u3059 x \u306E\u7BC4\u56F2\u3092\
    \u6C42\u3081\u308B.\n        \"\"\"\n        return (-self.__L[0]+self.__add_L,self.__R[0]+self.__add_R)\n\
    \n    def cumulative_left_min(self):\n        \"\"\" min_{y<=x} f(y) \u306B\u5909\
    \u66F4\u3059\u308B.\n\n        \"\"\"\n\n        self.__R=[float(\"inf\")]\n\n\
    \    def cumulative_right_min(self):\n        \"\"\" min_{y>=x} f(x) \u3092\u6C42\
    \u3081\u308B.\n\n        \"\"\"\n\n        self.__L=[float(\"inf\")]\n\n    def\
    \ slide(self,a):\n        \"\"\" f(x-a) \u306B\u5909\u66F4\u3059\u308B.\n\n  \
    \      \"\"\"\n        self.__add_L+=a\n        self.__add_R+=a\n\n    def sliding_window_minimum(self,a,b):\n\
    \        \"\"\" min_{x-b<=y<=x-a} f(y) \u306B\u5909\u66F4\u3059\u308B.\n     \
    \   \"\"\"\n\n        assert a<=b\n\n        self.__add_L+=a\n        self.__add_R+=b\n\
    \n    def copy(self):\n        G=Slope_Trick()\n        G.__L=self.__L.copy()\n\
    \        G.__R=self.__R.copy()\n        G.__add_L=self.__add_L\n        G.__add_R=self.__add_R\n\
    \        G.__y_min=self.__y_min\n        return G"
  dependsOn: []
  isVerificationFile: false
  path: Slope_Trick.py
  requiredBy: []
  timestamp: '2021-08-12 04:24:06+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Slope_Trick.py
layout: document
redirect_from:
- /library/Slope_Trick.py
- /library/Slope_Trick.py.html
title: Slope_Trick.py
---
