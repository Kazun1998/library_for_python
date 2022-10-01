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
  code: "from Modulo_Matrix import *\n\nclass Modulo_Vector_Error(Exception):\n  \
    \  pass\n\nclass Modulo_Vector:\n    def __init__(self,v):\n        self.vec=[x%Mod\
    \ for x in v]\n        self.size=len(v)\n\n        #\u51FA\u529B\n    def __str__(self):\n\
    \        return str(self.vec)\n\n    def __repr__(self):\n        return str(self)\n\
    \n    def __bool__(self):\n        return any(self.vec)\n\n    #+,-\n    def __pos__(self):\n\
    \        return self\n\n    def __neg__(self):\n        return self.__scale__(-1)\n\
    \n    #\u52A0\u6CD5\n    def __add__(self,other):\n        if self.size!=other.size:\n\
    \            raise Modulo_Vector_Error(\"2\u3064\u306E\u30D9\u30AF\u30C8\u30EB\
    \u306E\u30B5\u30A4\u30BA\u304C\u7570\u306A\u308A\u307E\u3059. ({}, {})\".format(self.size,other.size))\n\
    \n        v=self.vec\n        w=other.vec\n        return Modulo_Vector([v[i]+w[i]\
    \ for i in range(self.size)])\n\n    #\u6E1B\u6CD5\n    def __sub__(self, other):\n\
    \        return self+(-other)\n\n    def __rsub__(self, other):\n        return\
    \ (-self)+other\n\n    #\u4E57\u6CD5\n    def __mul__(self,other):\n        pass\n\
    \n    def __rmul__(self,other):\n        return self.__scale__(other)\n\n    #\u30B9\
    \u30AB\u30E9\u30FC\u500D\n    def __scale__(self,r):\n        v=self.vec\n   \
    \     v=[r*x for x in v]\n        return Modulo_Vector(v)\n\n    #\u5185\u7A4D\
    \n    def inner(self,other):\n        if self.size!=other.size:\n            raise\
    \ Modulo_Vector_Error(\"2\u3064\u306E\u30D9\u30AF\u30C8\u30EB\u306E\u30B5\u30A4\
    \u30BA\u304C\u7570\u306A\u308A\u307E\u3059.({},{})\".format(self.size,other.size))\n\
    \n        X=0\n        v=self.vec\n        w=other.vec\n\n        for i in range(self.size):\n\
    \            X+=v[i]*w[i]%Mod\n        return X\n\n    #\u7D2F\u4E57\n    def\
    \ __pow__(self,n):\n        pass\n\n    #\u7B49\u53F7\n    def __eq__(self,other):\n\
    \        return (self.vec==other.vec)\n\n    def __len__(self):\n        return\
    \ self.size\n\n    #\u4E0D\u7B49\u53F7\n    def __neq__(self,other):\n       \
    \ return not(self==other)\n\n    def __getitem__(self,index):\n        assert\
    \ isinstance(index,int)\n        return self.vec[index]\n\n    def __setitem__(self,index,val):\n\
    \        assert isinstance(index,int)\n        self.vec[index]=val\n\n#=================================================\n\
    def Zero_Vector(N):\n    \"\"\"N \u6B21\u5143\u306E\u30BC\u30ED\u30D9\u30AF\u30C8\
    \u30EB\u3092\u51FA\u529B\u3059\u308B.\n\n    \"\"\"\n    return Modulo_Vector([0]*N)\n\
    \ndef Standard_Basis(N, k):\n    \"\"\"N \u6B21\u5143\u30D9\u30AF\u30C8\u30EB\u306E\
    \u7B2C k \u6A19\u6E96\u57FA\u5E95\u3092\u51FA\u529B\u3059\u308B.\n\n    \"\"\"\
    \n    return Modulo_Vector([1 if i==k else 0 for i in range(N)])\n\ndef Vectoric_Matrix(V,\
    \ Mode=True):\n    \"\"\"\n\n    V: \u30D9\u30AF\u30C8\u30EB\u306E\u30EA\u30B9\
    \u30C8\n    Mode: True \u2192 \u884C\u30D9\u30AF\u30C8\u30EB, False \u2192 \u5217\
    \u30D9\u30AF\u30C8\u30EB\n    \"\"\"\n\n    M=[v.vec for v in V]\n    if Mode==True:\n\
    \        M=[list(c) for c in zip(*M)]\n    return Modulo_Matrix(M)\n\ndef Matrix_Action(A,v):\n\
    \    \"\"\" \u884C\u5217 A\u3068\u30D9\u30AF\u30C8\u30EB v \u306E\u7A4D Av \u3092\
    \u6C42\u3081\u308B.\n\n    A: Matrix\n    v: Vector\n    \"\"\"\n\n    assert\
    \ A.col==v.size\n\n    v=v.vec\n    w=[0]*A.row\n    for i in range(A.row):\n\
    \        a=A.ele[i]\n        for j in range(A.col):\n            w[i]+=a[j]*v[j]\n\
    \            w[i]%=Mod\n    return Modulo_Vector(w)\n\ndef Row_Vector(A):\n  \
    \  \"\"\" \u884C\u5217 A \u306E\u884C\u30D9\u30AF\u30C8\u30EB\u3092\u751F\u6210\
    \u3059\u308B.\n\n    A: Modulo_Matrix\n    \"\"\"\n\n    return [Modulo_Vector(v)\
    \ for v in A.ele]\n\ndef Column_Vector(A):\n    \"\"\" \u884C\u5217 A \u306E\u5217\
    \u30D9\u30AF\u30C8\u30EB\u3092\u751F\u6210\u3059\u308B.\n\n    A: Modulo_Matrix\n\
    \    \"\"\"\n\n    return [Modulo_Vector(v) for v in zip(*A.ele)]\n\ndef Tensor_Product(u,v):\n\
    \    \"\"\" u,v \u306E\u30C6\u30F3\u30BD\u30EB\u7A4D u (x) v \u3092\u8868\u3059\
    \u30D9\u30AF\u30C8\u30EB\u3092\u6C42\u3081\u308B.\n\n    u,v: vector\n    \"\"\
    \"\n\n    M=[[0]*len(v) for _ in range(len(u))]\n\n    for i in range(len(u)):\n\
    \        Mi=M[i]\n        for j in range(len(v)):\n            Mi[j]=u[i]*v[j]\n\
    \    return Modulo_Matrix(M)\n\n"
  dependsOn: []
  isVerificationFile: false
  path: Modulo_Matrix/Modulo_Vector.py
  requiredBy: []
  timestamp: '2022-02-01 19:50:52+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Modulo_Matrix/Modulo_Vector.py
layout: document
redirect_from:
- /library/Modulo_Matrix/Modulo_Vector.py
- /library/Modulo_Matrix/Modulo_Vector.py.html
title: Modulo_Matrix/Modulo_Vector.py
---
