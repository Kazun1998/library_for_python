---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':warning:'
    path: Union_Find/Bipartite_Checker.py
    title: Union_Find/Bipartite_Checker.py
  _extendedVerifiedWith:
  - icon: ':x:'
    path: test_verify/Union_Find.test.py
    title: test_verify/Union_Find.test.py
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.7/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.7/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class Union_Find():\n    __slots__=[\"n\",\"parents\",\"rank\",\"edges\"\
    ,\"__group_number\"]\n    def __init__(self,N):\n        \"\"\" 0,1,...,N-1 \u3092\
    \u8981\u7D20\u3068\u3057\u3066\u521D\u671F\u5316\u3059\u308B.\n\n        N: \u8981\
    \u7D20\u6570\n        \"\"\"\n        self.n=N\n        self.parents=[-1]*N\n\
    \        self.rank=[0]*N\n        self.edges=[0]*N\n        self.__group_number=N\n\
    \n    def find(self, x):\n        \"\"\" \u8981\u7D20 x \u306E\u5C5E\u3057\u3066\
    \u3044\u308B\u65CF\u3092\u8ABF\u3079\u308B.\n\n        x: \u8981\u7D20\n     \
    \   \"\"\"\n\n        a=x\n        while self.parents[a]>=0:\n            a=self.parents[a]\n\
    \n        while self.parents[x]>=0:\n            self.parents[x]=a\n         \
    \   x=self.parents[x]\n\n        return a\n\n    def union(self, x, y):\n    \
    \    \"\"\" \u8981\u7D20 x,y \u3092\u540C\u4E00\u8996\u3059\u308B.\n\n       \
    \ [input]\n        x,y: \u8981\u7D20\n\n        [output]\n        \u5143\u3005\
    \u304C\u975E\u9023\u7D50 \u2192 True\n        \u5143\u3005\u304C\u9023\u7D50 \u2192\
    \ False\n        \"\"\"\n        x=self.find(x)\n        y=self.find(y)\n\n  \
    \      if x==y:\n            self.edges[x]+=1\n            return False\n\n  \
    \      if self.rank[x]<self.rank[y]:\n            x,y=y,x\n\n        self.__group_number-=1\n\
    \n        self.edges[x]+=self.edges[y]+1\n        self.edges[y]=0\n\n        self.parents[x]+=self.parents[y]\n\
    \        self.parents[y]=x\n\n        if self.rank[x]==self.rank[y]:\n       \
    \     self.rank[x]+=1\n        return True\n\n    def size(self, x):\n       \
    \ \"\"\" \u8981\u7D20 x \u306E\u5C5E\u3057\u3066\u3044\u308B\u65CF\u306E\u8981\
    \u7D20\u306E\u6570.\n\n        x: \u8981\u7D20\n        \"\"\"\n        return\
    \ -self.parents[self.find(x)]\n\n    def same(self, x, y):\n        \"\"\" \u8981\
    \u7D20 x,y \u306F\u540C\u4E00\u8996\u3055\u308C\u3066\u3044\u308B\u304B?\n\n \
    \       x,y: \u8981\u7D20\n        \"\"\"\n        return self.find(x) == self.find(y)\n\
    \n    def members(self, x):\n        \"\"\" \u8981\u7D20 x \u304C\u5C5E\u3057\u3066\
    \u3044\u308B\u65CF\u306E\u8981\u7D20.\n        \u203B\u65CF\u306E\u8981\u7D20\u306E\
    \u500B\u6570\u304C\u6B32\u3057\u3044\u3068\u304D\u306F size \u3092\u4F7F\u3046\
    \u3053\u3068!!\n\n        x: \u8981\u7D20\n        \"\"\"\n        root = self.find(x)\n\
    \        return [i for i in range(self.n) if self.find(i) == root]\n\n    def\
    \ edge_count(self, x):\n        \"\"\" \u8981\u7D20 x \u304C\u5C5E\u3059\u308B\
    \u65CF\u306E\u8FBA\u306E\u672C\u6570\u3092\u6C42\u3081\u308B.\n\n        x: \u8981\
    \u7D20\n        \"\"\"\n        return self.edges[self.find(x)]\n\n    def is_tree(self,\
    \ x):\n        \"\"\" \u8981\u7D20 x \u304C\u5C5E\u3059\u308B\u65CF\u304C\u6728\
    \u304B\u3069\u3046\u304B\u3092\u5224\u5B9A\u3059\u308B.\n\n        x: \u8981\u7D20\
    \n        \"\"\"\n        return self.size(x)==self.edges[self.find(x)]+1\n\n\
    \    def tree_count(self):\n        \"\"\" \u6728\u306B\u306A\u3063\u3066\u3044\
    \u308B\u5C5E\u306E\u500B\u6570\u3092\u6C42\u3081\u308B.\n        \"\"\"\n\n  \
    \      X=0\n        for g in self.representative():\n            if self.is_tree(g):\n\
    \                X+=1\n        return X\n\n    def representative(self):\n   \
    \     \"\"\" \u4EE3\u8868\u5143\u306E\u30EA\u30B9\u30C8\n        \"\"\"\n    \
    \    return [i for i, x in enumerate(self.parents) if x < 0]\n\n    def group_count(self):\n\
    \        \"\"\" \u65CF\u306E\u500B\u6570\n        \"\"\"\n\n        return self.__group_number\n\
    \n    def all_group_members(self):\n        \"\"\" \u5168\u3066\u306E\u65CF\u306E\
    \u51FA\u529B\n        \"\"\"\n        X={r:[] for r in self.representative()}\n\
    \        for k in range(self.n):\n            X[self.find(k)].append(k)\n    \
    \    return X\n\n    def group_list(self):\n        \"\"\" \u5404\u8981\u7D20\u304C\
    \u5C5E\u3057\u3066\u3044\u308B\u65CF\u306E\u30EA\u30B9\u30C8\u3092\u51FA\u529B\
    \u3059\u308B.\n\n        \"\"\"\n        return [self.find(x) for x in range(self.n)]\n\
    \n    def refresh(self):\n        for i in range(self.n):\n            _=self.find(i)\n\
    \n    def __str__(self):\n        return '\\n'.join('{}: {}'.format(r, self.members(r))\
    \ for r in self.representative())\n\n    def __repr__(self):\n        return self.__str__()\n\
    \n    def __getitem__(self,index):\n        return self.find(index)\n\n    def\
    \ __setitem__(self,x,y):\n        self.union(x,y)\n"
  dependsOn: []
  isVerificationFile: false
  path: Union_Find/Union_Find.py
  requiredBy:
  - Union_Find/Bipartite_Checker.py
  timestamp: '2022-04-16 12:03:37+09:00'
  verificationStatus: LIBRARY_ALL_WA
  verifiedWith:
  - test_verify/Union_Find.test.py
documentation_of: Union_Find/Union_Find.py
layout: document
redirect_from:
- /library/Union_Find/Union_Find.py
- /library/Union_Find/Union_Find.py.html
title: Union_Find/Union_Find.py
---

#### 概要
無向グラフにおける辺の追加と2頂点が連結であるかどうかの判定を得意とするデータ構造

#### 使用方法
- `Union_Find(N)`: $N$ 個の頂点 $0,1, \dots, N-1$ からなる空グラフ (辺なしグラフ) を生成する.
- `find(x)`: $x$ が属している連結成分の代表元を求める.
- `union(x,y)`: 無向辺 $xy$ を追加する (単純にならなくてもよい)
- `size(x)`: 頂点 $x$ が属している連結成分の頂点数を求める.
- `same(x,y)`: 2頂点 $x,y$ が連結かどうかを判定する.
- `members(x)`: 頂点 $x$ が属している連結成分にある頂点を返す.
- `edge_count(x)`: 頂点 $x$ が属している連結成分にある辺の数を求める.
- `is_tree(x)`: 頂点 $x$ が属している連結成分が木かどうか (サイクルを含まないか) どうかを判定する.
- `tree_count()`: 木になっている連結成分の数を求める.
- `representative()`: 代表元のリストを求める.
- `group_count()`: 連結成分の数を求める.
- `all_group_members()`: 各連結成分における頂点のリストからなるリストを求める.
- `group_list()`: 各頂点が属している連結成分の代表元からなるリストを求める.
- `refresh()`: 情報を整理し, Union Find を単純化する.
