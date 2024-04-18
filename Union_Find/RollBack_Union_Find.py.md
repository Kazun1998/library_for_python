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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.3/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.3/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class RollBack_Union_Find():\n    __slots__=[\"n\", \"parents\", \"__history\"\
    , \"__snap_time\", \"__group_count\"]\n    def __init__(self, N):\n        \"\"\
    \" 0,1,...,N-1 \u3092\u8981\u7D20\u3068\u3057\u3066\u521D\u671F\u5316\u3059\u308B\
    .\n\n        N: \u8981\u7D20\u6570\n        \"\"\"\n        self.n=N\n       \
    \ self.parents=[-1]*N\n        self.__history=[]\n        self.__snap_time=[]\n\
    \        self.__group_count=[]\n\n    def find(self, x):\n        \"\"\" \u8981\
    \u7D20 x \u306E\u5C5E\u3057\u3066\u3044\u308B\u65CF\u3092\u8ABF\u3079\u308B.\n\
    \n        x: \u8981\u7D20\n        \"\"\"\n\n        while self.parents[x]>=0:\n\
    \            x=self.parents[x]\n\n        return x\n\n    def union(self, x, y):\n\
    \        \"\"\" \u8981\u7D20 x,y \u3092\u540C\u4E00\u8996\u3059\u308B.\n\n   \
    \     [input]\n        x,y: \u8981\u7D20\n\n        [output]\n        \u5143\u3005\
    \u304C\u975E\u9023\u7D50 \u2192 True\n        \u5143\u3005\u304C\u9023\u7D50 \u2192\
    \ False\n        \"\"\"\n        x=self.find(x); y=self.find(y)\n\n        par=self.parents\n\
    \n        self.__history.append((x, par[x]))\n        self.__history.append((y,\
    \ par[y]))\n\n        if self.__group_count:\n            count=self.__group_count[-1]\n\
    \        else:\n            count=self.n\n\n        if x==y:\n            self.__group_count.append(count)\n\
    \            return False\n\n        if par[x]>par[y]:\n            x,y=y,x\n\n\
    \        par[x]+=par[y]\n        par[y]=x\n\n        self.__group_count.append(count-1)\n\
    \n        return True\n\n    def size(self, x):\n        \"\"\" \u8981\u7D20 x\
    \ \u306E\u5C5E\u3057\u3066\u3044\u308B\u65CF\u306E\u8981\u7D20\u306E\u6570.\n\n\
    \        x: \u8981\u7D20\n        \"\"\"\n        return -self.parents[self.find(x)]\n\
    \n    def same(self, x, y):\n        \"\"\" \u8981\u7D20 x,y \u306F\u540C\u4E00\
    \u8996\u3055\u308C\u3066\u3044\u308B\u304B?\n\n        x,y: \u8981\u7D20\n   \
    \     \"\"\"\n        return self.find(x) == self.find(y)\n\n    def members(self,\
    \ x):\n        \"\"\" \u8981\u7D20 x \u304C\u5C5E\u3057\u3066\u3044\u308B\u65CF\
    \u306E\u8981\u7D20.\n        \u203B\u65CF\u306E\u8981\u7D20\u306E\u500B\u6570\u304C\
    \u6B32\u3057\u3044\u3068\u304D\u306F size \u3092\u4F7F\u3046\u3053\u3068!!\n\n\
    \        x: \u8981\u7D20\n        \"\"\"\n        root = self.find(x)\n      \
    \  return [i for i in range(self.n) if self.find(i) == root]\n\n    def representative(self):\n\
    \        \"\"\" \u4EE3\u8868\u5143\u306E\u30EA\u30B9\u30C8\n        \"\"\"\n \
    \       return [i for i, x in enumerate(self.parents) if x < 0]\n\n    def group_count(self):\n\
    \        \"\"\" \u65CF\u306E\u500B\u6570\n        \"\"\"\n\n        if self.__group_count:\n\
    \            return self.__group_count[-1]\n        else:\n            return\
    \ self.n\n\n    def get_time(self):\n        return len(self.__history)>>1\n\n\
    \    def undo(self):\n        \"\"\" 1 \u56DE\u5206\u306E union \u3092\u623B\u308B\
    .\n\n        \"\"\"\n\n        if self.__history:\n            y,b=self.__history.pop()\n\
    \            self.parents[y]=b\n\n            x,a=self.__history.pop()\n     \
    \       self.parents[x]=a\n\n            self.__group_count.pop()\n\n    def snapshot(self):\n\
    \        \"\"\" \u30B9\u30CA\u30C3\u30D7\u30B7\u30E7\u30C3\u30C8\u3092\u64AE\u308B\
    \n\n        \"\"\"\n\n        self.__snap_time.append(self.get_time())\n\n   \
    \ def rollback(self, time=-1):\n        \"\"\" \u6642\u523B time \u76F4\u524D\u307E\
    \u3067\u623B\u308B.\n\n        \"\"\"\n\n        if time==-1:\n            if\
    \ self.__snap_time:\n                time=self.__snap_time[-1]\n            else:\n\
    \                return\n\n        if time>self.get_time():\n            return\n\
    \n        T=time<<1\n        while T<len(self.__history):\n            self.undo()\n\
    \n    def all_group_members(self):\n        \"\"\" \u5168\u3066\u306E\u65CF\u306E\
    \u51FA\u529B\n        \"\"\"\n        X={r:[] for r in self.representative()}\n\
    \        for k in range(self.n):\n            X[self.find(k)].append(k)\n    \
    \    return X\n\n    def group_list(self):\n        \"\"\" \u5404\u8981\u7D20\u304C\
    \u5C5E\u3057\u3066\u3044\u308B\u65CF\u306E\u30EA\u30B9\u30C8\u3092\u51FA\u529B\
    \u3059\u308B.\n\n        \"\"\"\n        return [self.find(x) for x in range(self.n)]\n\
    \n    def __str__(self):\n        return str(self.all_group_members().values())[13:-2]\n\
    \n    def __repr__(self):\n        return \"RollBack Union Find: \"+str(self)\n\
    \n    def __getitem__(self,index):\n        return self.find(index)\n\n    def\
    \ __setitem__(self,x,y):\n        self.union(x,y)\n"
  dependsOn: []
  isVerificationFile: false
  path: Union_Find/RollBack_Union_Find.py
  requiredBy: []
  timestamp: '2023-05-20 13:23:07+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Union_Find/RollBack_Union_Find.py
layout: document
redirect_from:
- /library/Union_Find/RollBack_Union_Find.py
- /library/Union_Find/RollBack_Union_Find.py.html
title: Union_Find/RollBack_Union_Find.py
---
