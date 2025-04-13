---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Union_Find/Union_Find.py
    title: Union Find (Disjoint Set Union)
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.13.2/x64/lib/python3.13/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.13.2/x64/lib/python3.13/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from Union_Find import Union_Find\n\nclass Bipartite_Check():\n    __slots__=[\"\
    N\",\"__Union\"]\n\n    def __init__(self,N):\n        self.N=N\n        self.__Union=Union_Find(2*N)\n\
    \n    def add_edge(self,u,v):\n        self.__Union.union(u,v+self.N)\n      \
    \  self.__Union.union(u+self.N,v)\n\n    def check(self):\n        U=self.__Union\n\
    \        for x in range(self.N):\n            if U.same(x,x+self.N):\n       \
    \         return False\n        return True\n\n    def bipart_example(self):\n\
    \        X=[-1]*self.N\n        G=self.__Union.all_group_members()\n        for\
    \ x in range(self.N):\n            if X[x]!=-1:\n                continue\n\n\
    \            z=self.__Union.find(x)\n            for y in G[z]:\n            \
    \    if y<self.N:\n                    if X[y]==1: return None,None\n        \
    \            X[y]=0\n                else:\n                    if X[y-self.N]==0:\
    \ return None,None\n                    X[y-self.N]=1\n        return X\n\n  \
    \  def bipart(self):\n        Bip=[]\n        seen=[0]*self.N\n        G=self.__Union.all_group_members()\n\
    \n        for x in range(self.N):\n            if seen[x]:\n                continue\n\
    \n            g=self.__Union.find(x)\n            U=[]; V=[]\n            for\
    \ y in G[g]:\n                if seen[y%self.N]:\n                    return None\n\
    \n                seen[y%self.N]=1\n                if y<self.N:\n           \
    \         U.append(y)\n                else:\n                    V.append(y-self.N)\n\
    \            Bip.append((U,V))\n        return Bip\n\n    def bipart_cases(self,\
    \ Mod=None):\n        \"\"\" 2\u90E8\u30B0\u30E9\u30D5\u3078\u306E\u5206\u5272\
    \u306E\u65B9\u6CD5\u306E\u5834\u5408\u306E\u6570\u3092\u6C42\u3081\u308B.\n\n\
    \        \"\"\"\n\n        Bip=self.bipart()\n        if Bip is None:\n      \
    \      return 0\n        else:\n            return pow(2, len(Bip), Mod)\n\n"
  dependsOn:
  - Union_Find/Union_Find.py
  isVerificationFile: false
  path: Union_Find/Bipartite_Checker.py
  requiredBy: []
  timestamp: '2025-04-13 18:55:26+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Union_Find/Bipartite_Checker.py
layout: document
redirect_from:
- /library/Union_Find/Bipartite_Checker.py
- /library/Union_Find/Bipartite_Checker.py.html
title: Union_Find/Bipartite_Checker.py
---
