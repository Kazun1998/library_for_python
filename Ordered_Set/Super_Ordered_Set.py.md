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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.5/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.5/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class Super_Fenwick_Tree:\n    def __init__(self, N):\n        self.N=N\n\
    \        self.data={}\n\n    def add(self, i, x):\n        i+=1\n        data=self.data\n\
    \        while i<=self.N:\n            data[i-1]=data.get(i-1,0)+x\n         \
    \   i+=i&(-i)\n\n    def sum(self, i):\n        S=0\n        data=self.data\n\
    \        while i:\n            S+=data.get(i-1,0)\n            i-=i&(-i)\n   \
    \     return S\n\n    def range_sum(self,l,r):\n        return self.sum(r)-self.sum(l)\n\
    \n    def bisect_left(self, x, default=-1):\n        i=0\n        k=1<<self.N.bit_length()\n\
    \        data=self.data\n\n        while k:\n            if i+k<=self.N and data.get(i+k-1,0)<x:\n\
    \                x-=data.get(i+k-1,0)\n                i+=k\n            k>>=1\n\
    \        return i if x else default\n\n    def bisect_right(self, x, default=-1):\n\
    \        i=0\n        k=1<<self.N.bit_length()\n        data=self.data\n\n   \
    \     while k:\n            if i+k<=self.N and data.get(i+k-1,0)<=x:\n       \
    \         x-=data.get(i+k-1,0)\n                i+=k\n            k>>=1\n    \
    \    return i if i<self.N else default\n\nclass Super_Ordered_Set:\n    def __init__(self,\
    \ N, multiple=False):\n        self.N=N\n        self.multiple=bool(multiple)\n\
    \n        self.Fenwick=Super_Fenwick_Tree(N)\n        self.__card=self.Fenwick.sum(N)\n\
    \n    def __contains__(self, x):\n        return bool(self.count(x))\n\n    def\
    \ count(self, x):\n        return self.Fenwick.range_sum(x,x+1)\n\n    def __len__(self):\n\
    \        return self.__card\n\n    def __bool__(self):\n        return bool(len(self))\n\
    \n    def add(self, x):\n        if (not self.multiple) and (x in self):\n   \
    \         return\n\n        self.Fenwick.add(x,1)\n        self.__card+=1\n\n\
    \    def discard(self, x):\n        if x not in self:\n            return\n\n\
    \        self.Fenwick.add(x,-1)\n        self.__card-=1\n\n    def remove(self,\
    \ x):\n        if  x not in self:\n            raise KeyError(x)\n\n        self.Fenwick.add(x,\
    \ -1)\n        self.__card-=1\n\n    def get(self, index, default=-1):\n     \
    \   size=len(self)\n        if size<=index or size+index<0:\n            return\
    \ default\n\n        if index<0:\n            index+=size\n\n        return self.Fenwick.bisect_left(index+1)\n\
    \n    def __getitem__(self, index):\n        size=len(self)\n        if size<=index\
    \ or size+index<0:\n            raise IndexError\n\n        if index<0:\n    \
    \        index+=size\n\n        return self.Fenwick.bisect_left(index+1)\n\n \
    \   def get_min(self, default=-1):\n        return self.get(0, default)\n\n  \
    \  def pop_min(self):\n        y=self.get_min()\n        if y==-1:\n         \
    \   raise IndexError\n        self.remove(y)\n        return y\n\n    def get_max(self,\
    \ default=-1):\n        return self.get(-1, default)\n\n    def pop_max(self):\n\
    \        y=self.get_max()\n        if y==-1:\n            raise IndexError\n \
    \       self.remove(y)\n        return y\n\n    def index(self, x, mode=False,\
    \ default=-1):\n        \"\"\" S[k]=x \u3092\u6E80\u305F\u3059 k \u3092\u6C42\u3081\
    \u308B.\n\n        x: int\n        mode: False \u306E\u3068\u304D\u306F k \u306E\
    \u6700\u5C0F\u5024, True \u306E\u6642\u306F k \u306E\u6700\u5927\u5024 (\u591A\
    \u91CD\u96C6\u5408\u306E\u3068\u304D\u6709\u7528)\n        \"\"\"\n\n        if\
    \ x not in self:\n            return default\n\n        if mode:\n           \
    \ return self.Fenwick.sum(x+1)-1\n        else:\n            return self.Fenwick.sum(x)\n\
    \n    def previous(self, x, mode=True, default=-1):\n        \"\"\" S \u306B\u542B\
    \u307E\u308C\u308B x \u4EE5\u4E0B\u306E\u8981\u7D20\u306E\u3046\u3061, \u6700\u5927\
    \u5024\u3092\u6C42\u3081\u308B.\n\n        x: int\n        mode: False \u306E\u3068\
    \u304D\u306F \"\u4EE5\u4E0B\" \u304C \"\u672A\u6E80\" \u306B\u306A\u308B.\n  \
    \      \"\"\"\n\n        if mode:\n            x+=1\n\n        if x>=0:\n    \
    \        return self.Fenwick.bisect_left(self.Fenwick.sum(x), default)\n     \
    \   else:\n            return default\n\n    def next(self, x, mode=True, default=-1):\n\
    \        \"\"\" S \u306B\u542B\u307E\u308C\u308B x \u4EE5\u4E0A\u306E\u8981\u7D20\
    \u306E\u3046\u3061, \u6700\u5927\u5024\u3092\u6C42\u3081\u308B.\n\n        x:\
    \ int\n        mode: False \u306E\u3068\u304D\u306F \"\u4EE5\u4E0A\" \u304C \"\
    \u3088\u308A\u5927\u304D\u3044\" \u306B\u306A\u308B.\n        \"\"\"\n\n     \
    \   if not mode:\n            x+=1\n        return self.Fenwick.bisect_right(self.Fenwick.sum(x),\
    \ default)\n"
  dependsOn: []
  isVerificationFile: false
  path: Ordered_Set/Super_Ordered_Set.py
  requiredBy: []
  timestamp: '2023-08-08 23:43:42+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Ordered_Set/Super_Ordered_Set.py
layout: document
redirect_from:
- /library/Ordered_Set/Super_Ordered_Set.py
- /library/Ordered_Set/Super_Ordered_Set.py.html
title: Ordered_Set/Super_Ordered_Set.py
---
