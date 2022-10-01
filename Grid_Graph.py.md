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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.7/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.7/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class Grid:\n    def __init__(self,*F):\n        self.F=tuple(F)\n      \
    \  self.dim=len(self.F)\n\n        R=[1]\n        for a in self.F[::-1]:\n   \
    \         R.append(R[-1]*a)\n\n        self.volume,*self.partition=R[::-1]\n\n\
    \    def number_to_position(self,N):\n        assert 0<=N<self.volume\n\n    \
    \    pos=[0]*self.dim\n        for i in range(self.dim):\n            pos[i],N=divmod(N,self.partition[i])\n\
    \        return pos\n\n    def position_to_number(self,*pos):\n        assert\
    \ len(pos)==self.dim\n\n        N=0\n        for i in range(self.dim):\n     \
    \       assert 0<=pos[i]<self.F[i]\n            N+=self.partition[i]*pos[i]\n\
    \        return N\n\n    def number_neighborhood_yielder(self,N):\n        r=N\n\
    \        for i in range(self.dim):\n            q,r=divmod(r,self.partition[i])\n\
    \n            if 0<q:\n                yield N-self.partition[i]\n\n         \
    \   if q<self.F[i]-1:\n                yield N+self.partition[i]\n\n    def position_neighborhood_yielder(self,*pos):\n\
    \        assert self.dim==len(pos)\n        pos=list(pos)\n\n        for i in\
    \ range(self.dim):\n            if 0<pos[i]:\n                pos[i]-=1\n    \
    \            yield pos\n                pos[i]+=1\n\n            if pos[i]<self.F[i]-1:\n\
    \                pos[i]+=1\n                yield pos\n                pos[i]-=1\n"
  dependsOn: []
  isVerificationFile: false
  path: Grid_Graph.py
  requiredBy: []
  timestamp: '2021-05-19 11:47:56+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Grid_Graph.py
layout: document
redirect_from:
- /library/Grid_Graph.py
- /library/Grid_Graph.py.html
title: Grid_Graph.py
---
