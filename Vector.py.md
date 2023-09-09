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
  code: "class VectorException(Exception):\n    pass\n\nclass Vector():\n    def __init__(self,*V):\n\
    \        self.ele=list(V)\n        self.dim=len(V)\n\n    def __str__(self):\n\
    \        if self.dim!=1:\n            return str(tuple(self.ele))\n        else:\n\
    \            return \"({})\".format(self.ele[0])\n\n    #+,-\n    def __pos__(self):\n\
    \        return self\n\n    def __neg__(self):\n        return Vector(*[-x for\
    \ x in self.ele])\n\n    #\u52A0\u6CD5\n    def __add__(self,other):\n       \
    \ if other.__class__==Vector:\n            assert self.dim==other.dim,\"2\u3064\
    \u306E\u30D9\u30AF\u30C8\u30EB\u306E\u6B21\u5143\u304C\u7570\u306A\u308B\"\n \
    \           U=[self.ele[i]+other.ele[i] for i in range(self.dim)]\n        else:\n\
    \            U=[x+other for x in self.ele]\n        return Vector(*U)\n      \
    \  \n    #\u6E1B\u6CD5\n    def __sub__(self,other):\n        if other.__class__==Vector:\n\
    \            assert self.dim==other.dim,\"2\u3064\u306E\u30D9\u30AF\u30C8\u30EB\
    \u306E\u6B21\u5143\u304C\u7570\u306A\u308B\"\n            U=[self.ele[i]-other.ele[i]\
    \ for i in range(self.dim)]\n        else:\n            U=[x-other for x in self.ele]\n\
    \        return Vector(*U)\n\n    #\u4E57\u6CD5\n    def __mul__(self,other):\n\
    \        if other.__class__==Vector:\n            return self.inner(other)\n \
    \       else:\n            return self.scale(k)\n\n    def __rmul__(self,k):\n\
    \        return self.scale(k)\n\n    #\u30B9\u30AB\u30E9\u30FC\u500D\n    def\
    \ scale(self,k):\n        U=[x*k for x in self.ele]\n        return Vector(*U)\n\
    \n    #\u5185\u7A4D\n    def inner(self,other):\n        if self.dim!=other.dim:\n\
    \            raise VectorException(\"\u30D9\u30AF\u30C8\u30EB\u306E\u6B21\u5143\
    \u304C\u7570\u306A\u308A\u307E\u3059({},{}).\".format(self.dim,other.dim))\n \
    \       S=0\n        for i in range(self.dim):\n            S+=self.ele[i]*other.ele[i]\n\
    \        return S\n"
  dependsOn: []
  isVerificationFile: false
  path: Vector.py
  requiredBy: []
  timestamp: '2021-04-27 14:48:27+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Vector.py
layout: document
redirect_from:
- /library/Vector.py
- /library/Vector.py.html
title: Vector.py
---
