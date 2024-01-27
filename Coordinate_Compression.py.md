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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.1/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.1/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class Coordinate_compression_1:\n    def __init__(self,X,Mode=False):\n \
    \       \"\"\"1\u6B21\u5143\u306E\u5EA7\u6A19\u5727\u7E2E\u3092\u884C\u3046.\n\
    \        X:\u5206\u5272\u3059\u308B\u5024.\n        Mode:X=[x_0,x_1, ... , x_k]\
    \ (\u91CD\u8907\u306A\u3057, \u6607\u9806) \u306E\u3068\u304D,\n        Mode=False\
    \ -> [-inf, x_0), [x_0, x_1), ..., [x_{k-1}, x_k), [x_k, inf]\n        Mode=True\
    \ -> [-inf, x_0], (x_0, x_1], ..., (x_{k-1}, x_k], (x_k, inf]\n        \"\"\"\n\
    \        self.X=list(set(X))\n        self.X.sort()\n        self.Mode=Mode\n\n\
    \    def __str__(self):\n        X=self.X\n        Mode=self.Mode\n        S=[\"\
    \"]*(len(self)-1)\n        for k in range(len(self)-1):\n            if not Mode:\n\
    \                S[k]=\"[{},{})\".format(X[k],X[k+1])\n            else:\n   \
    \             S[k]=\"({},{}]\".format(X[k],X[k+1])\n\n        if not Mode:\n \
    \           return \"X: [-inf, {}) \".format(X[0])+\" \".join(S)+\" [{}, inf]\"\
    .format(X[-1])\n        else:\n            return \"X: [-inf, {}] \".format(X[0])+\"\
    \ \".join(S)+\" ({}, inf]\".format(X[-1])\n\n    def __repr__(self):\n       \
    \ return str(self)\n\n    def at(self,x):\n        X=self.X\n        Mode=self.Mode\n\
    \n        if x<X[0] or (Mode and x==X[0]):\n            return 0\n\n        L,R=0,len(self)\n\
    \        while R-L>1:\n            C=L+(R-L)//2\n            xc=X[C]\n       \
    \     if x>xc or (not Mode and x==xc):\n                L=C\n            else:\n\
    \                R=C\n        return L+1\n\n    def __len__(self):\n        return\
    \ len(self.X)\n\nclass Coordinate_compression_2(Coordinate_compression_1):\n \
    \   def __init__(self,X,Y,Mode=False):\n        \"\"\"2\u6B21\u5143\u306E\u5EA7\
    \u6A19\u5727\u7E2E\u3092\u884C\u3046.\n        X,Y:\u5206\u5272\u3059\u308B\u5024\
    .\n        Mode:(1\u6B21\u5143\u306E\u6642\u3068\u540C\u69D8, False \u306A\u3089\
    \u3070\u53F3\u534A\u958B\u533A\u9593, True \u306A\u3089\u3070\u534A\u958B\u533A\
    \u9593)\n        \"\"\"\n        self.X=Coordinate_compression_1(X,Mode)\n   \
    \     self.Y=Coordinate_compression_1(Y,Mode)\n        self.Mode=Mode\n\n    def\
    \ __str__(self):\n        return str(self.X)+\"\\nY:\"+str(self.Y)[2:]\n\n   \
    \ def __repr__(self):\n        return str(self)\n\n    def at(self,x,y):\n   \
    \     return (self.X.at(x),self.Y.at(y))\n\n    def __len__(self):\n        pass\n\
    \nclass Coordinate_compression_N(Coordinate_compression_1):\n    def __init__(self,XX,Mode=False):\n\
    \        \"\"\"N\u6B21\u5143\u306E\u5EA7\u6A19\u5727\u7E2E\u3092\u884C\u3046.\n\
    \        XX:\u5206\u5272\u3059\u308B\u5024\u306E\u30EA\u30B9\u30C8.\n        Mode:(1\u6B21\
    \u5143\u306E\u6642\u3068\u540C\u69D8, False \u306A\u3089\u3070\u53F3\u534A\u958B\
    \u533A\u9593, True \u306A\u3089\u3070\u534A\u958B\u533A\u9593)\n        \"\"\"\
    \n        self.XX=[Coordinate_compression_1(X,Mode) for X in XX]\n        self.Mode=Mode\n\
    \n    def __str__(self):\n        T=[\"X{}: {}\".format(i,str(x)[3:]) for i,x\
    \ in enumerate(self.XX,1)]\n        return \"\\n\".join(T)\n\n    def __repr__(self):\n\
    \        return str(self)\n\n    def at(self,*r):\n        assert len(self.XX)==len(r)\n\
    \        return tuple([self.XX[i].at(r[i]) for i in range(len(r))])\n\n    def\
    \ __len__(self):\n        pass\n"
  dependsOn: []
  isVerificationFile: false
  path: Coordinate_Compression.py
  requiredBy: []
  timestamp: '2021-04-27 15:14:50+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Coordinate_Compression.py
layout: document
redirect_from:
- /library/Coordinate_Compression.py
- /library/Coordinate_Compression.py.html
title: Coordinate_Compression.py
---
