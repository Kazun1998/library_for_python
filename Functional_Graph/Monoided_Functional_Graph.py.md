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
  code: "class Monoided_Functional_Graph:\n    def __init__(self, N, K, calc, unit):\n\
    \        self.N=N\n        self.K=K\n        self.calc=calc\n        self.unit=unit\n\
    \n        self.out=[list(range(N))]\n        self.value=[[unit]*N]\n\n    def\
    \ set_arc(self, source, target, x):\n        self.out[0][source]=target\n    \
    \    self.value[0][source]=x\n\n    def build(self):\n        K=self.K>>1\n  \
    \      N=self.N\n        calc=self.calc\n        while K:\n            A=self.out[-1];\
    \ X=[0]*N\n            B=self.value[-1]; Y=[0]*N\n\n            for i in range(N):\n\
    \                p=A[i]; x=B[i]\n                q=A[p]; y=B[p]\n            \
    \    X[i]=q; Y[i]=calc(y,x)\n\n            self.out.append(X)\n            self.value.append(Y)\n\
    \            K>>=1\n\n    def calculate(self, v, t):\n        x=self.unit\n  \
    \      calc=self.calc\n        out=self.out\n        value=self.value\n      \
    \  d=0\n        while t:\n            if t&1:\n                x=calc(value[d][v],\
    \ x)\n                v=out[d][v]\n            t>>=1; d+=1\n        return x\n\
    \n"
  dependsOn: []
  isVerificationFile: false
  path: Functional_Graph/Monoided_Functional_Graph.py
  requiredBy: []
  timestamp: '2022-10-27 18:36:50+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Functional_Graph/Monoided_Functional_Graph.py
layout: document
redirect_from:
- /library/Functional_Graph/Monoided_Functional_Graph.py
- /library/Functional_Graph/Monoided_Functional_Graph.py.html
title: Functional_Graph/Monoided_Functional_Graph.py
---
