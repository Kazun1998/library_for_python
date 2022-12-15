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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.1/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.1/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class Potentilized_Union_Find():\n    __slots__=[\"n\",\"parents\",\"rank\"\
    ,\"edges\",\"pot\"]\n    def __init__(self,N):\n        \"\"\" 0,1,...,N-1 \u3092\
    \u8981\u7D20\u3068\u3057\u3066\u521D\u671F\u5316\u3059\u308B.\n\n        N: \u8981\
    \u7D20\u6570\n        \"\"\"\n        self.n=N\n        self.parents=[-1]*N\n\
    \        self.rank=[0]*N\n        self.edges=[0]*N\n        self.pot=[0]*N\n\n\
    \    def find(self, x):\n        \"\"\" \u8981\u7D20 x \u306E\u5C5E\u3057\u3066\
    \u3044\u308B\u65CF\u3092\u8ABF\u3079\u308B.\n\n        x: \u8981\u7D20\n     \
    \   \"\"\"\n        V=[]\n        while self.parents[x]>=0:\n            V.append(x)\n\
    \            x=self.parents[x]\n\n        for v in V:\n            self.pot[v]+=self.pot[self.parents[v]]\n\
    \            self.parents[v]=x\n        return x\n\n    def union(self, x, y,\
    \ u):\n        \"\"\" \u8981\u7D20 x,y \u3092\u540C\u4E00\u8996\u3057, U(x)-U(y)=u\
    \ \u3068\u3044\u3046\u60C5\u5831\u3092\u52A0\u3048\u308B.\n\n        x,y: \u8981\
    \u7D20\n        \"\"\"\n\n        u+=self.pot[x]-self.pot[y]\n        x=self.find(x)\n\
    \        y=self.find(y)\n\n        if x==y:\n            self.edges[x]+=1\n  \
    \          assert self.potential(x,y)==u\n            return\n\n        if self.rank[x]>self.rank[y]:\n\
    \            x,y,u=y,x,-u\n\n        self.edges[x]+=self.edges[y]+1\n        self.edges[y]=0\n\
    \n        self.parents[x]+=self.parents[y]\n        self.parents[y]=x\n\n    \
    \    if self.rank[x]==self.rank[y]:\n            self.rank[x]+=1\n        self.pot[x]=u\n\
    \n    def size(self, x):\n        \"\"\" \u8981\u7D20 x \u306E\u5C5E\u3057\u3066\
    \u3044\u308B\u65CF\u306E\u8981\u7D20\u306E\u6570.\n\n        x: \u8981\u7D20\n\
    \        \"\"\"\n        return -self.parents[self.find(x)]\n\n    def potential(self,\
    \ x, y):\n        \"\"\" y \u3092\u57FA\u6E96\u306B\u3057\u305F x \u306E\u30DD\
    \u30C6\u30F3\u30B7\u30E3\u30EB\"\"\"\n\n        if self.same(x,y):\n         \
    \   return self.pot[x]-self.pot[y]\n        else:\n            return None\n\n\
    \    def same(self, x, y):\n        \"\"\" \u8981\u7D20 x,y \u306F\u540C\u4E00\
    \u8996\u3055\u308C\u3066\u3044\u308B\u304B?\n\n        x,y: \u8981\u7D20\n   \
    \     \"\"\"\n        return self.find(x) == self.find(y)\n\n    def members(self,\
    \ x):\n        \"\"\" \u8981\u7D20 x \u304C\u5C5E\u3057\u3066\u3044\u308B\u65CF\
    \u306E\u8981\u7D20.\n        \u203B\u65CF\u306E\u8981\u7D20\u306E\u500B\u6570\u304C\
    \u6B32\u3057\u3044\u3068\u304D\u306F size \u3092\u4F7F\u3046\u3053\u3068!!\n\n\
    \        x: \u8981\u7D20\n        \"\"\"\n        root = self.find(x)\n      \
    \  return [i for i in range(self.n) if self.find(i) == root]\n\n    def edge_count(self,\
    \ x):\n        \"\"\" \u8981\u7D20 x \u304C\u5C5E\u3059\u308B\u65CF\u306E\u8FBA\
    \u306E\u672C\u6570\u3092\u6C42\u3081\u308B.\n\n        x: \u8981\u7D20\n     \
    \   \"\"\"\n        return self.edges[self.find(x)]\n\n    def is_forest(self,\
    \ x):\n        \"\"\" \u8981\u7D20 x \u304C\u5C5E\u3059\u308B\u65CF\u304C\u68EE\
    \u304B\u3069\u3046\u304B\u3092\u5224\u5B9A\u3059\u308B.\n\n        x: \u8981\u7D20\
    \n        \"\"\"\n        return self.size(x)==self.edges[self.find(x)]+1\n\n\
    \    def forest_count(self):\n        \"\"\" \u68EE\u306B\u306A\u3063\u3066\u3044\
    \u308B\u5C5E\u306E\u500B\u6570\u3092\u6C42\u3081\u308B.\n        \"\"\"\n\n  \
    \      X=0\n        for g in self.roots():\n            if self.is_forest(g):\n\
    \                X+=1\n        return X\n\n    def roots(self):\n        \"\"\"\
    \ \u65CF\u306E\u540D\u524D\u306E\u30EA\u30B9\u30C8\n        \"\"\"\n        return\
    \ [i for i, x in enumerate(self.parents) if x < 0]\n\n    def group_count(self):\n\
    \        \"\"\" \u65CF\u306E\u500B\u6570\n        \"\"\"\n        return len(self.roots())\n\
    \n    def all_group_members(self):\n        \"\"\" \u5168\u3066\u306E\u65CF\u306E\
    \u51FA\u529B\n        \"\"\"\n        X={r:[] for r in self.roots()}\n       \
    \ for k in range(self.n):\n            X[self.find(k)].append(k)\n        return\
    \ X\n\n    def refresh(self):\n        for i in range(self.n):\n            _=self.find(i)\n\
    \n    def __str__(self):\n        return '\\n'.join('{}: {}'.format(r, self.members(r))\
    \ for r in self.roots())\n\n    __repr__=__str__\n"
  dependsOn: []
  isVerificationFile: false
  path: Union_Find/Potentialized_Union_Find.py
  requiredBy: []
  timestamp: '2021-09-04 16:54:50+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Union_Find/Potentialized_Union_Find.py
layout: document
redirect_from:
- /library/Union_Find/Potentialized_Union_Find.py
- /library/Union_Find/Potentialized_Union_Find.py.html
title: Union_Find/Potentialized_Union_Find.py
---
