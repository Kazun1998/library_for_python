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
  code: "class Dual_Segment_Tree:\n    def __init__(self, L, comp, id):\n        \"\
    \"\"op\u3092\u4F5C\u7528\u3068\u3059\u308B\u30EA\u30B9\u30C8L\u306EDual Segment\
    \ Tree\u3092\u4F5C\u6210\n\n        op:\u4F5C\u7528\u7D20\n        id:\u6052\u7B49\
    \u5199\u50CF\n\n        [\u6761\u4EF6]\n        M:Monoid, F={f: F x M\u2192 M:\
    \ \u4F5C\u7528\u7D20} \u306B\u5BFE\u3057\u3066,\u4EE5\u4E0B\u304C\u6210\u7ACB\u3059\
    \u308B.\n        F \u306F\u6052\u7B49\u5199\u50CF id \u3092\u542B\u3080. \u3064\
    \u307E\u308A, \u4EFB\u610F\u306E x in M \u306B\u5BFE\u3057\u3066 id(x)=x\n   \
    \     F \u306F\u5199\u50CF\u306E\u5408\u6210\u306B\u9589\u3058\u3066\u3044\u308B\
    . \u3064\u307E\u308A,\u4EFB\u610F\u306E f,g in F \u306B\u5BFE\u3057\u3066, comp(f,g)\
    \ in F\n        \u4EFB\u610F\u306E f in F, x,y in M \u306B\u5BFE\u3057\u3066,\
    \ f(xy)=f(x)f(y)\u3067\u3042\u308B.\n\n        [\u6CE8\u8A18]\n        \u66F4\u65B0\
    \u306F\u5DE6\u304B\u3089. \u3064\u307E\u308A, comp(new, old) \u3068\u306A\u308B\
    .\n        \"\"\"\n\n        self.comp=comp\n        self.id=id\n\n        N=len(L)\n\
    \        d=max(1,(N-1).bit_length())\n        k=1<<d\n\n        self.lazy=[self.id]*k+L+[self.id]*(k-N)\n\
    \        self.N=k\n        self.depth=d\n\n    #\u914D\u5217\u306E\u7B2Cm\u8981\
    \u7D20\u3092\u4E0B\u306B\u4F1D\u642C\n    def _propagate_at(self,m):\n       \
    \ lazy=self.lazy\n        if lazy[m]!=self.id:\n            lazy[(m<<1)|0]=self.comp(lazy[m],lazy[(m<<1)|0])\n\
    \            lazy[(m<<1)|1]=self.comp(lazy[m],lazy[(m<<1)|1])\n            lazy[m]=self.id\n\
    \n    #\u914D\u5217\u306E\u7B2Cm\u8981\u7D20\u3088\u308A\u4E0A\u3092\u5168\u3066\
    \u4F1D\u642C\n    def _propagate_above(self,m):\n        H=m.bit_length()\n  \
    \      for h in range(H-1,0,-1):\n            self._propagate_at(m>>h)\n\n   \
    \ #\u4F5C\u7528\n    def operate(self, l, r, alpha, left_closed=True, right_closed=True):\n\
    \        L=l+self.N+(not left_closed)\n        R=r+self.N+(right_closed)\n\n \
    \       L0=R0=-1\n        X,Y=L,R-1\n        while X<Y:\n            if X&1:\n\
    \                L0=max(L0,X)\n                X+=1\n\n            if Y&1==0:\n\
    \                R0=max(R0,Y)\n                Y-=1\n\n            X>>=1\n   \
    \         Y>>=1\n\n        L0=max(L0,X)\n        R0=max(R0,Y)\n\n        self._propagate_above(L0)\n\
    \        self._propagate_above(R0)\n\n        lazy=self.lazy; comp=self.comp\n\
    \        while L<R:\n            if L&1:\n                lazy[L]=comp(alpha,\
    \ lazy[L])\n                L+=1\n\n            if R&1:\n                R-=1\n\
    \                lazy[R]=comp(alpha, lazy[R])\n\n            L>>=1\n         \
    \   R>>=1\n\n    #\u30EA\u30D5\u30EC\u30C3\u30B7\u30E5\n    def refresh(self):\n\
    \        for m in range(1,self.N):\n            self._propagate_at(m)\n\n    #\u53D6\
    \u5F97\n    def get(self,k):\n        m=k+self.N\n        self._propagate_above(m)\n\
    \        return self.lazy[m]\n\n    def __getitem__(self,index):\n        m=index+self.N\n\
    \        self._propagate_above(m)\n        return self.lazy[m]\n\n    def __setitem__(self,index,value):\n\
    \        self.operate(index, index, value)\n"
  dependsOn: []
  isVerificationFile: false
  path: Segment_Tree/Dual_Segment_Tree.py
  requiredBy: []
  timestamp: '2022-09-28 10:55:10+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Segment_Tree/Dual_Segment_Tree.py
layout: document
redirect_from:
- /library/Segment_Tree/Dual_Segment_Tree.py
- /library/Segment_Tree/Dual_Segment_Tree.py.html
title: Segment_Tree/Dual_Segment_Tree.py
---