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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.13.2/x64/lib/python3.13/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.13.2/x64/lib/python3.13/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class Functional_Graph_Single_Source:\n    def __init__(self, N, start):\n\
    \        self.N=N\n        self.start=start\n        self.f=list(range(N))\n\n\
    \    def set_arc(self, source, target):\n        self.f[source]=target\n\n   \
    \ def build(self):\n        self.first=[]\n        used=[0]*self.N\n\n       \
    \ x=self.start\n        while not used[x]:\n            self.first.append(x)\n\
    \            used[x]=1\n\n            x=self.f[x]\n\n        self.second=[x]\n\
    \        y=self.f[x]\n        while y!=x:\n            self.second.append(y)\n\
    \            y=self.f[y]\n\n    def calculate(self, K):\n        if K<len(self.first):\n\
    \            return self.first[K]\n        else:\n            K-=len(self.first)\n\
    \            return self.second[K%len(self.second)]\n"
  dependsOn: []
  isVerificationFile: false
  path: Functional_Graph/Functional_Graph_Single_Source.py
  requiredBy: []
  timestamp: '2022-10-27 18:37:23+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Functional_Graph/Functional_Graph_Single_Source.py
layout: document
redirect_from:
- /library/Functional_Graph/Functional_Graph_Single_Source.py
- /library/Functional_Graph/Functional_Graph_Single_Source.py.html
title: Functional_Graph/Functional_Graph_Single_Source.py
---
