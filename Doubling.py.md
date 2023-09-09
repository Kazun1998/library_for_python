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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.5/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.5/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class Doubling():\n    def __init__(self, A, Max_Level=1):\n        \"\"\"\
    \ N=len(A), X={0,1,...,N-1} \u3068\u3059\u308B. f: X\u2192X \u3092 f(x):=A[x]\
    \ \u3068\u3057\u305F\u3068\u304D, f^k(x) \u3092\u6C42\u3081\u308B.\n\n       \
    \ A: f \u3092\u8868\u3059\u30EA\u30B9\u30C8, \u4EFB\u610F\u306E x in X \u306B\u5BFE\
    \u3057\u3066, f(x) in X \u3067\u306A\u3051\u308C\u3070\u306A\u3089\u306A\u3044\
    .\n        Max_Level: k=2^(Max_Level+1)-1 \u307E\u3067\u5BFE\u5FDC\u53EF\u80FD\
    \u306B\u306A\u308B.\n        \"\"\"\n\n        self.N=len(A)\n        self.D=[[0]*self.N\
    \ for _ in range(Max_Level+1)]\n        self.Level=Max_Level\n\n        E=self.D[0]\n\
    \        for i in range(self.N):\n            assert 0<=A[i]<self.N\n        \
    \    E[i]=A[i]\n\n        for k in range(1,Max_Level+1):\n            E=self.D[k];\
    \ F=self.D[k-1]\n            for i in range(self.N):\n                E[i]=F[F[i]]\n\
    \n    def evaluate(self,x,k):\n        \"\"\" f^k(x) \u3092\u6C42\u3081\u308B\
    .\n\n        \"\"\"\n\n        for i in range(self.Level+1):\n            E=self.D[i]\n\
    \            if k&1:\n                x=E[x]\n            k>>=1\n            if\
    \ k==0:\n                break\n        return x\n\n    def evaluate_list(self,k):\n\
    \        \"\"\" [f^k(0), f^k(1), ..., f^k(N-1)] \u3092\u6C42\u3081\u308B.\n\n\
    \        \"\"\"\n\n        X=list(range(self.N))\n        for i in range(self.Level+1):\n\
    \            E=self.D[i]\n            if k&1:\n                for x in range(self.N):\n\
    \                    X[x]=E[X[x]]\n            k>>=1\n            if k==0:\n \
    \               break\n        return X\n"
  dependsOn: []
  isVerificationFile: false
  path: Doubling.py
  requiredBy: []
  timestamp: '2023-06-17 23:40:34+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Doubling.py
layout: document
redirect_from:
- /library/Doubling.py
- /library/Doubling.py.html
title: Doubling.py
---
