---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test_verify/yosupo_library_checker/Data_Structure/Predecessor_Problem-Ordered_Set.test.py
    title: test_verify/yosupo_library_checker/Data_Structure/Predecessor_Problem-Ordered_Set.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.1/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.1/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class Fenwick_Tree:\n    def __init__(self, N, A=None):\n        self.N=N\n\
    \        if A==None:\n            self.data=[0]*N\n        else:\n           \
    \ assert len(A)==N\n            self.data=A\n            self.__build()\n\n  \
    \  def __build(self):\n        data=self.data\n        for i in range(1, self.N+1):\n\
    \            if i+(i&(-i))<=self.N:\n                data[i+(i&(-i))-1]+=data[i-1]\n\
    \n    def add(self, i, x):\n        i+=1\n        data=self.data\n        while\
    \ i<=self.N:\n            data[i-1]+=x\n            i+=i&(-i)\n\n    def sum(self,\
    \ i):\n        S=0\n        data=self.data\n        while i:\n            S+=data[i-1]\n\
    \            i-=i&(-i)\n        return S\n\n    def range_sum(self,l,r):\n   \
    \     return self.sum(r)-self.sum(l)\n\n    def bisect_left(self, x, default=-1):\n\
    \        i=0\n        k=1<<self.N.bit_length()\n        data=self.data\n\n   \
    \     while k:\n            if i+k<=self.N and data[i+k-1]<x:\n              \
    \  x-=self.data[i+k-1]\n                i+=k\n            k>>=1\n        return\
    \ i if x else default\n\n    def bisect_right(self, x, default=-1):\n        i=0\n\
    \        k=1<<self.N.bit_length()\n        data=self.data\n\n        while k:\n\
    \            if i+k<=self.N and data[i+k-1]<=x:\n                x-=self.data[i+k-1]\n\
    \                i+=k\n            k>>=1\n        return i if i<self.N else default\n\
    \nclass Ordered_Set:\n    def __init__(self, N, multiple=False, S=None):\n   \
    \     self.N=N\n        self.multiple=bool(multiple)\n\n        if (not multiple)\
    \ and S:\n            S=[1 if S[i] else 0 for i in range(N)]\n\n        self.Fenwick=Fenwick_Tree(N,S)\n\
    \        self.__card=self.Fenwick.sum(N)\n\n    def __contains__(self, x):\n \
    \       return bool(self.count(x))\n\n    def count(self, x):\n        return\
    \ self.Fenwick.range_sum(x,x+1)\n\n    def __len__(self):\n        return self.__card\n\
    \n    def __bool__(self):\n        return bool(len(self))\n\n    def add(self,\
    \ x, k=1):\n        \"\"\" x \u3092 k \u500B (\u591A\u91CD\u96C6\u5408\u306E\u3068\
    \u304D) \u52A0\u3048\u308B.\n\n        \"\"\"\n\n        if (not self.multiple)\
    \ and (x in self):\n            return\n\n        if not self.multiple:\n    \
    \        k=1\n\n        self.Fenwick.add(x,k)\n        self.__card+=k\n\n    def\
    \ discard(self, x, k=1):\n        \"\"\" x \u3092 k \u500B (\u591A\u91CD\u96C6\
    \u5408\u306E\u3068\u304D) \u524A\u9664\u3059\u308B.\n\n        x: int\n      \
    \  k: k=-1 \u3068\u3059\u308B\u3068, x \u3092\u5168\u3066\u524A\u9664\u3059\u308B\
    .\n        \"\"\"\n\n        if x not in self:\n            return\n\n       \
    \ if k==-1:\n            k=self.count(x)\n        elif not self.multiple:\n  \
    \          k=1\n\n        self.Fenwick.add(x,-k)\n        self.__card-=k\n\n \
    \   def remove(self, x):\n        \"\"\" x \u3092 k \u500B (\u591A\u91CD\u96C6\
    \u5408\u306E\u3068\u304D) \u524A\u9664\u3059\u308B.\n\n        x: int\n      \
    \  k: k=-1 \u3068\u3059\u308B\u3068, x \u3092\u5168\u3066\u524A\u9664\u3059\u308B\
    .\n        \"\"\"\n\n        if  x not in self:\n            raise KeyError(x)\n\
    \n        if k==-1:\n            k=self.count(x)\n        elif not self.multiple:\n\
    \            k=1\n\n        self.Fenwick.add(x, -k)\n        self.__card-=k\n\n\
    \    def get(self, index, default=-1):\n        size=len(self)\n        if size<=index\
    \ or size+index<0:\n            return default\n\n        if index<0:\n      \
    \      index+=size\n\n        return self.Fenwick.bisect_left(index+1)\n\n   \
    \ def __getitem__(self, index):\n        size=len(self)\n        if size<=index\
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
    \ default)\n\n    def less_count(self, x, mode=False):\n        \"\"\" x \u672A\
    \u6E80\u306E\u5143\u306E\u500B\u6570\u3092\u6C42\u3081\u308B.\n\n        x: int\n\
    \        mode: mode=True \u306A\u3089\u3070, \"\u672A\u6E80\" \u304C \"\u4EE5\u4E0B\
    \" \u306B\u306A\u308B.\n        \"\"\"\n\n        if mode:\n            x+=1\n\
    \        return self.Fenwick.sum(x)\n\n    def more_count(self, x, mode=False):\n\
    \        \"\"\" x \u3088\u308A\u5927\u304D\u3044\u5143\u306E\u500B\u6570\u3092\
    \u6C42\u3081\u308B.\n\n        x: int\n        mode: mode=True \u306A\u3089\u3070\
    , \"\u3088\u308A\u5927\u304D\u3044\" \u304C \"\u4EE5\u4E0A\" \u306B\u306A\u308B\
    .\n        \"\"\"\n\n        return len(self)-self.less_count(x, not mode)\n\n\
    \    def kth_min(self, k, default=-1):\n        \"\"\" k \u756A\u76EE\u306B\u5C0F\
    \u3055\u3044\u5143\u3092\u6C42\u3081\u308B.\n\n        \"\"\"\n\n        if 1<=k<=len(self):\n\
    \            return self[k-1]\n        else:\n            return default\n\n \
    \   def kth_max(self, k, default=-1):\n        \"\"\" k \u756A\u76EE\u306B\u5927\
    \u304D\u3044\u5143\u3092\u6C42\u3081\u308B.\n\n        \"\"\"\n\n        if 1<=k<=len(self):\n\
    \            return self[~(k-1)]\n        else:\n            return default\n\n\
    class Ordered_Set_with_Negative:\n    def __init__(self, N, multiple=False):\n\
    \        \"\"\" -N < x < N \u306E\u7BC4\u56F2\u3067\u306E\u9806\u5E8F\u4ED8\u304D\
    \u96C6\u5408\u3092\u751F\u6210\u3059\u308B.\n\n        \"\"\"\n        self.N=N\n\
    \        self.multiple=bool(multiple)\n        self.positive=Ordered_Set(N, multiple)\n\
    \        self.negative=Ordered_Set(N, multiple)\n\n    def __contains__(self,\
    \ x):\n        return bool(self.count(x))\n\n    def count(self, x):\n       \
    \ if x>=0:\n            return self.positive.count(x)\n        else:\n       \
    \     return self.negative.count(-x)\n\n    def __len__(self):\n        return\
    \ len(self.positive)+len(self.negative)\n\n    def __bool__(self):\n        return\
    \ bool(len(self))\n\n    def add(self, x):\n        if (not self.multiple) and\
    \ (x in self):\n            return\n\n        if x>=0:\n            self.positive.add(x)\n\
    \        else:\n            self.negative.add(-x)\n\n    def discard(self, x):\n\
    \        if x>=0:\n            self.positive.discard(x)\n        else:\n     \
    \       self.negative.discard(-x)\n\n    def remove(self, x):\n        if x>=0:\n\
    \            self.positive.remove(x)\n        else:\n            self.negative.remove(-x)\n\
    \n    def get(self, index, default=None):\n        size=len(self)\n        if\
    \ size<=index or size+index<0:\n            return default\n\n        if index<0:\n\
    \            index+=size\n\n        if index<len(self.negative):\n           \
    \ return -self.negative.get(~index)\n        else:\n            return self.positive.get(index-len(self.negative))\n\
    \n    def __getitem__(self, index):\n        size=len(self)\n        if size<=index\
    \ or size+index<0:\n            raise IndexError\n\n        if index<0:\n    \
    \        index+=size\n\n        if index<len(self.negative):\n            return\
    \ -self.negative.get(~index)\n        else:\n            return self.positive.get(index-len(self.negative))\n\
    \n    def get_min(self, default=None):\n        if self.negative:\n          \
    \  return -self.negative.get_max()\n        else:\n            return self.positive.get_min(default=default)\n\
    \n    def pop_min(self):\n        y=self.get_min()\n        if y==None:\n    \
    \        raise IndexError\n        self.remove(y)\n        return y\n\n    def\
    \ get_max(self, default=None):\n        if self.positive:\n            return\
    \ self.positive.get_max()\n        elif self.negative:\n            return -self.negative.get_min()\n\
    \        else:\n            return default\n\n    def pop_max(self):\n       \
    \ y=self.get_max()\n        if y==None:\n            raise IndexError\n      \
    \  self.remove(y)\n        return y\n\n    def index(self, x, mode=False, default=None):\n\
    \        \"\"\" S[k]=x \u3092\u6E80\u305F\u3059 k \u3092\u6C42\u3081\u308B.\n\n\
    \        x: int\n        mode: False \u306E\u3068\u304D\u306F k \u306E\u6700\u5C0F\
    \u5024, True \u306E\u6642\u306F k \u306E\u6700\u5927\u5024 (\u591A\u91CD\u96C6\
    \u5408\u306E\u3068\u304D\u6709\u7528)\n        \"\"\"\n\n        if x not in self:\n\
    \            return default\n\n        if mode:\n            return self.Fenwick.sum(x+1)-1\n\
    \        else:\n            return self.Fenwick.sum(x)\n\n    def previous(self,\
    \ x, mode=True, default=None):\n        \"\"\" S \u306B\u542B\u307E\u308C\u308B\
    \ x \u4EE5\u4E0B\u306E\u8981\u7D20\u306E\u3046\u3061, \u6700\u5927\u5024\u3092\
    \u6C42\u3081\u308B.\n\n        x: int\n        mode: False \u306E\u3068\u304D\u306F\
    \ \"\u4EE5\u4E0B\" \u304C \"\u672A\u6E80\" \u306B\u306A\u308B.\n        \"\"\"\
    \n\n\n        if x<=0:\n            y=self.negative.next(-x, mode, None)\n   \
    \         if y==None:\n                return default\n            else:\n   \
    \             return -y\n        else:\n            y=self.positive.previous(x,\
    \ mode, None)\n            if y==None:\n                return self.previous(-1,\
    \ True, default)\n            else:\n                return y\n\n    def next(self,\
    \ x, mode=True, default=None):\n        \"\"\" S \u306B\u542B\u307E\u308C\u308B\
    \ x \u4EE5\u4E0A\u306E\u8981\u7D20\u306E\u3046\u3061, \u6700\u5927\u5024\u3092\
    \u6C42\u3081\u308B.\n\n        x: int\n        mode: False \u306E\u3068\u304D\u306F\
    \ \"\u4EE5\u4E0A\" \u304C \"\u3088\u308A\u5927\u304D\u3044\" \u306B\u306A\u308B\
    .\n        \"\"\"\n\n        if x>=0:\n            y=self.positive.next(x, mode,\
    \ None)\n            if y==None:\n                return default\n           \
    \ else:\n                return y\n        else:\n            y=self.negative.previous(-x,\
    \ mode, None)\n            if y==None:\n                return self.next(0, True,\
    \ default)\n            else:\n                return -y\n"
  dependsOn: []
  isVerificationFile: false
  path: Ordered_Set/Ordered_Set.py
  requiredBy: []
  timestamp: '2022-04-26 00:13:12+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test_verify/yosupo_library_checker/Data_Structure/Predecessor_Problem-Ordered_Set.test.py
documentation_of: Ordered_Set/Ordered_Set.py
layout: document
redirect_from:
- /library/Ordered_Set/Ordered_Set.py
- /library/Ordered_Set/Ordered_Set.py.html
title: Ordered_Set/Ordered_Set.py
---
