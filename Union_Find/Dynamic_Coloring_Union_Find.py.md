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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.13.3/x64/lib/python3.13/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.13.3/x64/lib/python3.13/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class Dynamic_Coloring_Union_Find():\n    __slots__=(\"n\", \"parents\",\
    \ \"rank\", \"data\", \"merge\", \"__group_number\")\n\n    def __init__(self,\
    \ N, merge, unit):\n        \"\"\" 0,1,...,N-1 \u3092\u8981\u7D20\u3068\u3057\u3066\
    \u521D\u671F\u5316\u3059\u308B.\n\n        N: \u8981\u7D20\u6570\n        merge:\
    \ \u5408\u6210\u306E\u65B9\u6CD5\n        unit: \u6700\u521D\u306E\u5024\n   \
    \     \"\"\"\n        self.n=N\n        self.parents=[-1]*N\n        self.data=[unit]*N\n\
    \        self.rank=[0]*N\n        self.merge=merge\n        self.__group_number=N\n\
    \n    def find(self, x):\n        \"\"\" \u8981\u7D20 x \u306E\u5C5E\u3057\u3066\
    \u3044\u308B\u65CF\u3092\u8ABF\u3079\u308B.\n\n        x: \u8981\u7D20\n     \
    \   \"\"\"\n        V=[]\n        while self.parents[x]>=0:\n            V.append(x)\n\
    \            x=self.parents[x]\n\n        for v in V:\n            self.parents[v]=x\n\
    \        return x\n\n    def union(self, x, y):\n        \"\"\" \u8981\u7D20 x,y\
    \ \u3092\u540C\u4E00\u8996\u3057, \u305D\u308C\u305E\u308C\u304C\u6301\u3063\u3066\
    \u3044\u308B\u65CF\u306E\u8272\u3092\u7D71\u5408\u3059\u308B.\n\n        x,y:\
    \ \u8981\u7D20\n        \"\"\"\n        x=self.find(x)\n        y=self.find(y)\n\
    \n        if x==y:\n            return\n\n        self.__group_number-=1\n\n \
    \       self.data[x]=self.data[y]=self.merge(self.data[x], self.data[y])\n\n \
    \       if self.rank[x]<self.rank[y]:\n            x,y=y,x\n\n        self.parents[x]+=self.parents[y]\n\
    \        self.parents[y]=x\n\n        if self.rank[x]==self.rank[y]:\n       \
    \     self.rank[x]+=1\n\n    def size(self, x):\n        \"\"\" \u8981\u7D20 x\
    \ \u306E\u5C5E\u3057\u3066\u3044\u308B\u65CF\u306E\u8981\u7D20\u306E\u6570.\n\n\
    \        x: \u8981\u7D20\n        \"\"\"\n        return -self.parents[self.find(x)]\n\
    \n    def same(self, x, y):\n        \"\"\" \u8981\u7D20 x,y \u306F\u540C\u4E00\
    \u8996\u3055\u308C\u3066\u3044\u308B\u304B?\n\n        x,y: \u8981\u7D20\n   \
    \     \"\"\"\n        return self.find(x) == self.find(y)\n\n    def update(self,\
    \ x, color):\n        \"\"\" \u8981\u7D20 x \u306E\u5C5E\u3059\u308B\u65CF\u306E\
    \u8272\u3092 color \u306B\u5909\u66F4\u3059\u308B.\n\n        x: \u8981\u7D20\n\
    \        color: \u8272\n        \"\"\"\n        self.data[self.find(x)]=color\n\
    \n    def get(self, x):\n        \"\"\" \u8981\u7D20 x \u306E\u5C5E\u3059\u308B\
    \u5C5E\u306E\u8272\u3092\u6C42\u3081\u308B.\n\n        x: \u8981\u7D20\n     \
    \   \"\"\"\n        return self.data[self.find(x)]\n\n    def members(self, x):\n\
    \        \"\"\" \u8981\u7D20 x \u304C\u5C5E\u3057\u3066\u3044\u308B\u65CF\u306E\
    \u8981\u7D20.\n        \u203B\u65CF\u306E\u8981\u7D20\u306E\u500B\u6570\u304C\u6B32\
    \u3057\u3044\u3068\u304D\u306F size \u3092\u4F7F\u3046\u3053\u3068!!\n\n     \
    \   x: \u8981\u7D20\n        \"\"\"\n        root = self.find(x)\n        return\
    \ [i for i in range(self.n) if self.find(i) == root]\n\n    def roots(self):\n\
    \        \"\"\" \u65CF\u306E\u540D\u524D\u306E\u30EA\u30B9\u30C8\n        \"\"\
    \"\n        return [i for i,x in enumerate(self.parents) if x < 0]\n\n    def\
    \ group_count(self):\n        \"\"\" \u65CF\u306E\u500B\u6570\n        \"\"\"\n\
    \        return self.__group_number\n\n    def all_group_members(self):\n    \
    \    \"\"\" \u5168\u3066\u306E\u65CF\u306E\u51FA\u529B\n        \"\"\"\n     \
    \   X={r:[] for r in self.roots()}\n        for k in range(self.n):\n        \
    \    X[self.find(k)].append(k)\n        return X\n\n    def list(self):\n    \
    \    return [self.get(x) for x in range(self.n)]\n\n    def map(self):\n     \
    \   return {x:self.get(x) for x in self.roots()}\n\n    def __str__(self):\n \
    \       string=[]\n        for x,g in self.all_group_members().items():\n    \
    \        string.append(\" ({}) {}\".format(self.get(x), g))\n        return \"\
    ,\".join(string)\n\n    def __repr__(self):\n        return \"Coloring Union Find:\"\
    +str(U)\n\n    def __getitem__(self,index):\n        return self.data[self.find(index)]\n\
    \n    def __setitem__(self,index,value):\n        self.data[self.find(index)]=value\n"
  dependsOn: []
  isVerificationFile: false
  path: Union_Find/Dynamic_Coloring_Union_Find.py
  requiredBy: []
  timestamp: '2023-08-08 23:46:45+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Union_Find/Dynamic_Coloring_Union_Find.py
layout: document
redirect_from:
- /library/Union_Find/Dynamic_Coloring_Union_Find.py
- /library/Union_Find/Dynamic_Coloring_Union_Find.py.html
title: Union_Find/Dynamic_Coloring_Union_Find.py
---
