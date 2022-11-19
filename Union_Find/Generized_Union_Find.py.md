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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class Generalized_Union_Find():\n    def __init__(self):\n        \"\"\"\u521D\
    \u671F\u5316\u3059\u308B.\n\n        N:\u8981\u7D20\u6570\n        f:2\u5909\u6570\
    \u95A2\u6570\u306E\u5408\u6210\n        e:\u6700\u521D\u306E\u5024\n        \"\
    \"\"\n        self.parent={}\n        self.SIZE={}\n        self.rank={}\n\n \
    \   def vertex_exist(self,x):\n        return x in self.parent\n\n    def vertex_add(self,x):\n\
    \        if x in self.parent:\n            return\n        self.parent[x]=x\n\
    \        self.SIZE[x]=1\n        self.rank[x]=1\n        return\n\n    def find(self,\
    \ x):\n        \"\"\"\u8981\u7D20x\u306E\u5C5E\u3057\u3066\u3044\u308B\u65CF\u3092\
    \u8ABF\u3079\u308B.\n\n        x:\u8981\u7D20\n        \"\"\"\n\n        self.vertex_add(x)\n\
    \n        V=[]\n        while self.parent[x]!=x:\n            V.append(x)\n  \
    \          x=self.parent[x]\n\n        self.parent[x]=x\n        for v in V:\n\
    \            self.parent[x]=x\n        return x\n\n    def union(self, x, y):\n\
    \        \"\"\"\u8981\u7D20x,y\u3092\u540C\u4E00\u8996\u3059\u308B.\n\n      \
    \  x,y:\u8981\u7D20\n        \"\"\"\n        x=self.find(x)\n        y=self.find(y)\n\
    \n        if x==y:\n            return\n\n        if self.rank[x]<self.rank[y]:\n\
    \            x,y=y,x\n\n        self.SIZE[x]+=self.SIZE[y]\n        self.parent[y]=x\n\
    \n        if self.rank[x]==self.rank[y]:\n            self.rank[x]+=1\n\n    def\
    \ size(self, x):\n        \"\"\"\u8981\u7D20x\u306E\u5C5E\u3057\u3066\u3044\u308B\
    \u8981\u7D20\u306E\u6570.\n\n        x:\u8981\u7D20\n        \"\"\"\n        return\
    \ self.SIZE[self.find(x)]\n\n    def same(self, x, y):\n        \"\"\"\u8981\u7D20\
    x,y\u306F\u540C\u4E00\u8996\u3055\u308C\u3066\u3044\u308B\u304B?\n\n        x,y:\u8981\
    \u7D20\n        \"\"\"\n        return self.find(x) == self.find(y)\n\n    def\
    \ members(self, x):\n        \"\"\"\u8981\u7D20x\u304C\u5C5E\u3057\u3066\u3044\
    \u308B\u65CF\u306E\u8981\u7D20.\n        \u203B\u65CF\u306E\u8981\u7D20\u306E\u500B\
    \u6570\u304C\u6B32\u3057\u3044\u3068\u304D\u306Fsize\u3092\u4F7F\u3046\u3053\u3068\
    !!\n\n        x:\u8981\u7D20\n        \"\"\"\n        root = self.find(x)\n  \
    \      return [v for v in self.parent if self.find(v)==root]\n\n    def roots(self):\n\
    \        \"\"\"\u65CF\u306E\u540D\u524D\u306E\u30EA\u30B9\u30C8\n        \"\"\"\
    \n        return [v for v in self.parent if self.find(v)==v]\n\n    def group_count(self):\n\
    \        \"\"\"\u65CF\u306E\u500B\u6570\n        \"\"\"\n        x=0\n       \
    \ for v in self.parent:\n            if self.find(v)==v:\n                x+=1\n\
    \        return x\n\n    def all_group_members(self):\n        \"\"\"\u5168\u3066\
    \u306E\u65CF\u306E\u51FA\u529B\n        \"\"\"\n        X={r:[] for r in self.roots()}\n\
    \        for k in self.parent:\n            X[self.find(k)].append(k)\n      \
    \  return X\n\n    def __str__(self):\n        return '\\n'.join('{}: {}'.format(r,\
    \ self.members(r)) for r in self.roots())\n\n    def __repr__(self):\n       \
    \ return self.__str__()\n"
  dependsOn: []
  isVerificationFile: false
  path: Union_Find/Generized_Union_Find.py
  requiredBy: []
  timestamp: '2021-09-04 16:54:50+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Union_Find/Generized_Union_Find.py
layout: document
redirect_from:
- /library/Union_Find/Generized_Union_Find.py
- /library/Union_Find/Generized_Union_Find.py.html
title: Union_Find/Generized_Union_Find.py
---
