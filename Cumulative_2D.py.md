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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.13.1/x64/lib/python3.13/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.13.1/x64/lib/python3.13/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class Cumulative_2D:\n    def __init__(self, A):\n        H=self.H=len(A)\n\
    \        W=self.W=len(A[0]) if self.H else 0\n\n        self.cum=cum=[[0]*(W+1)\
    \ for _ in range(H+1)]\n\n        for i in range(H):\n            Ai=A[i]\n  \
    \          ci=cum[i+1]; cii=cum[i]\n            for j in range(W):\n         \
    \       ci[j+1]=ci[j]+Ai[j]\n\n            for j in range(W):\n              \
    \  ci[j+1]+=cii[j+1]\n\n    def sum(self, i0, j0, i1, j1):\n        \"\"\" sum_{i0<=x<=i1,\
    \ j0<=y<=j1} A[x][y] \u3092\u6C42\u3081\u308B.\n\n        \"\"\"\n\n        if\
    \ (i0>i1) or (j0>j1) or (self.H<=i0) or (i1<0) or (self.W<=j0) or (j1<0):\n  \
    \          return 0\n\n        i0=i0 if i0>=0 else 0\n        j0=j0 if j0>=0 else\
    \ 0\n        i1=i1 if i1<self.H else self.H-1\n        j1=j1 if j1<self.W else\
    \ self.W-1\n\n        i0+=1; j0+=1; i1+=1; j1+=1\n        b=self.cum\n       \
    \ return b[i1][j1]-b[i0-1][j1]-b[i1][j0-1]+b[i0-1][j0-1]\n\n    def sum_range(self,\
    \ h, w):\n        \"\"\" 0<=i<=H-h, 0<=j<=W-w \u305D\u308C\u305E\u308C\u306B\u5BFE\
    \u3057\u3066, sum_{i<=x<i+h, j<=y<j+w} A[x][y] \u3092\u6C42\u3081\u308B.\n\n \
    \       \"\"\"\n\n        H=self.H; W=self.W\n        b=self.cum\n\n        T=[[0]*(W-w+1)\
    \ for _ in range(H-h+1)]\n        for i in range(H-h+1):\n            Ti=T[i]\n\
    \            bih=b[i+h]; bi=b[i]\n            for j in range(W-w+1):\n       \
    \         Ti[j]=bih[j+w]-bi[j+w]-bih[j]+bi[j]\n        return T\n"
  dependsOn: []
  isVerificationFile: false
  path: Cumulative_2D.py
  requiredBy: []
  timestamp: '2022-12-24 15:14:41+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Cumulative_2D.py
layout: document
redirect_from:
- /library/Cumulative_2D.py
- /library/Cumulative_2D.py.html
title: Cumulative_2D.py
---
