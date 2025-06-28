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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.13.5/x64/lib/python3.13/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.13.5/x64/lib/python3.13/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from Modulo_Matrix import *\n\nclass Modulo_Vector:\n    def __init__(self,\
    \ vector: list[int]):\n        self.vec = [vi % Mod for vi in vector]\n\n    @property\n\
    \    def size(self) -> int:\n        return len(self.vec)\n\n    #\u51FA\u529B\
    \n    def __str__(self):\n        return str(self.vec)\n\n    def __repr__(self):\n\
    \        return f\"{self.__class__.__name__}({self.vec})\"\n\n    def __bool__(self):\n\
    \        return any(self.vec)\n\n    def __iter__(self):\n        yield from self.vec\n\
    \n    #+,-\n    def __pos__(self):\n        return self\n\n    def __neg__(self):\n\
    \        return self.__scale__(-1)\n\n    #\u52A0\u6CD5\n    def __add__(self,\
    \ other):\n        assert self.size == other.size, f\"2\u3064\u306E\u30D9\u30AF\
    \u30C8\u30EB\u306E\u30B5\u30A4\u30BA\u304C\u7570\u306A\u308A\u307E\u3059. ({self.size},\
    \ {other.size})\"\n        return Modulo_Vector([vi + wi for vi, wi in zip(self,\
    \ other)])\n\n    #\u6E1B\u6CD5\n    def __sub__(self, other):\n        return\
    \ self+(-other)\n\n    def __rsub__(self, other):\n        return (-self)+other\n\
    \n    #\u4E57\u6CD5\n    def __mul__(self,other):\n        pass\n\n    def __rmul__(self,other):\n\
    \        return self.__scale__(other)\n\n    #\u30B9\u30AB\u30E9\u30FC\u500D\n\
    \    def __scale__(self, r):\n        return Modulo_Vector([r * vi for vi in self])\n\
    \n    #\u5185\u7A4D\n    def inner(self, other: \"Modulo_Vector\") -> int:\n \
    \       assert self.size == other.size, f\"2\u3064\u306E\u30D9\u30AF\u30C8\u30EB\
    \u306E\u30B5\u30A4\u30BA\u304C\u7570\u306A\u308A\u307E\u3059. ({self.size}, {other.size})\"\
    \n        return sum(vi * wi % Mod for vi, wi in zip(self, other)) % Mod\n\n \
    \   #\u7D2F\u4E57\n    def __pow__(self,n):\n        pass\n\n    #\u7B49\u53F7\
    \n    def __eq__(self, other):\n        return self.vec == other.vec\n\n    def\
    \ __len__(self):\n        return self.size\n\n    #\u4E0D\u7B49\u53F7\n    def\
    \ __neq__(self, other):\n        return not (self == other)\n\n    def __getitem__(self,index):\n\
    \        assert isinstance(index,int)\n        return self.vec[index]\n\n    def\
    \ __setitem__(self,index,val):\n        assert isinstance(index,int)\n       \
    \ self.vec[index]=val\n\n    def is_zero(self) -> bool:\n        return not any(self.vec)\n\
    \n#=================================================\ndef Zero_Vector(N: int)\
    \ -> Modulo_Vector:\n    \"\"\" N \u6B21\u5143\u306E\u30BC\u30ED\u30D9\u30AF\u30C8\
    \u30EB\u3092\u51FA\u529B\u3059\u308B.\n\n    Args:\n        N (int): \u6B21\u5143\
    \n\n    Returns:\n        Modulo_Vector: N \u6B21\u5143\u30BC\u30ED\u30D9\u30AF\
    \u30C8\u30EB\n    \"\"\"\n\n    return Modulo_Vector([0]*N)\n\ndef Standard_Basis(N:\
    \ int, k: int) -> Modulo_Vector:\n    \"\"\" N \u6B21\u5143\u30D9\u30AF\u30C8\u30EB\
    \u306E\u7B2C k \u6A19\u6E96\u57FA\u5E95\u3092\u51FA\u529B\u3059\u308B.\n\n   \
    \ Args:\n        N (int): \u6B21\u5143\n        k (int): 1 \u3092\u7ACB\u305F\u305B\
    \u308B\u6210\u5206\n\n    Returns:\n        Modulo_Vector: \u7B2C k \u6210\u5206\
    \u306E\u307F 1, \u305D\u308C\u4EE5\u5916\u306F\u3059\u3079\u3066 0 \u3067\u3042\
    \u308B N \u6B21\u5143\u30D9\u30AF\u30C8\u30EB\n    \"\"\"\n\n    return Modulo_Vector([1\
    \ if i == k else 0 for i in range(N)])\n\ndef Vectoric_Matrix(A: list[Modulo_Vector],\
    \ column: bool = False) -> Modulo_Vector:\n    \"\"\" \u30D9\u30AF\u30C8\u30EB\
    \u306E\u30EA\u30B9\u30C8 A \u304B\u3089\u884C\u5217\u3092\u751F\u6210\u3059\u308B\
    . A \u306E\u5404\u8981\u7D20\u304C\u884C\u30D9\u30AF\u30C8\u30EB\u306B\u306A\u308B\
    .\n\n    Args:\n        A (list[Modulo_Vector]): \u30D9\u30AF\u30C8\u30EB\u306E\
    \u30EA\u30B9\u30C8\n        column (bool, optional): True \u306B\u3059\u308B\u3068\
    , A \u306E\u5404\u8981\u7D20\u304C\u5217\u30D9\u30AF\u30C8\u30EB\u306B\u306A\u308B\
    \u884C\u5217\u3092\u51FA\u529B\u3059\u308B. Defaults to False.\n\n    Returns:\n\
    \        Modulo_Vector: \u884C (\u5217) \u30D9\u30AF\u30C8\u30EB\u3068\u3057\u305F\
    \u884C\u5217\n    \"\"\"\n\n    A = [a.vec for a in A]\n    if column:\n     \
    \   A = [list(x) for x in zip(*A)]\n    return Modulo_Matrix(A)\n\ndef Matrix_Action(A:\
    \ Modulo_Matrix, v: Modulo_Vector) -> Modulo_Vector:\n    \"\"\" \u884C\u5217\
    \ A \u3068\u30D9\u30AF\u30C8\u30EB v \u306E\u7A4D Av \u3092\u6C42\u3081\u308B\
    .\n\n    Args:\n        A (Modulo_Matrix): \u884C\u5217\n        v (Modulo_Vector):\
    \ \u30D9\u30AF\u30C8\u30EB\n\n    Returns:\n        Modulo_Vector: Av\n    \"\"\
    \"\n\n    if A.col != v.size:\n        raise ValueError\n\n    v = v.vec\n   \
    \ w = [0] * A.row\n    for i in range(A.row):\n        a = A.ele[i]\n        w[i]\
    \ = sum(a[j] * v[j] % Mod for j in range(A.col))\n    return Modulo_Vector(w)\n\
    \ndef Row_Vector(A: Modulo_Matrix) -> list[Modulo_Vector]:\n    \"\"\" \u884C\u5217\
    \ A \u306E\u884C\u30D9\u30AF\u30C8\u30EB\u304B\u3089\u306A\u308B\u30EA\u30B9\u30C8\
    \u3092\u751F\u6210\u3059\u308B.\n\n    Args:\n        A (Modulo_Matrix): \u884C\
    \u5217\n\n    Returns:\n        list[Modulo_Vector]: \u884C\u30D9\u30AF\u30C8\u30EB\
    \u304B\u3089\u306A\u308B\u30EA\u30B9\u30C8\n    \"\"\"\n\n    return [Modulo_Vector(v)\
    \ for v in A.ele]\n\ndef Column_Vector(A: Modulo_Matrix) -> list[Modulo_Vector]:\n\
    \    \"\"\" \u884C\u5217 A \u306E\u5217\u30D9\u30AF\u30C8\u30EB\u304B\u3089\u306A\
    \u308B\u30EA\u30B9\u30C8\u3092\u751F\u6210\u3059\u308B.\n\n    Args:\n       \
    \ A (Modulo_Matrix): \u884C\u5217\n\n    Returns:\n        list[Modulo_Vector]:\
    \ \u5217\u30D9\u30AF\u30C8\u30EB\u304B\u3089\u306A\u308B\u30EA\u30B9\u30C8\n \
    \   \"\"\"\n\n    return [Modulo_Vector(v) for v in zip(*A.ele)]\n\ndef Tensor_Product(u:\
    \ Modulo_Vector, v: Modulo_Vector) -> Modulo_Matrix:\n    \"\"\" u,v \u306E\u30C6\
    \u30F3\u30BD\u30EB\u7A4D u (x) v \u3092\u8868\u3059\u30D9\u30AF\u30C8\u30EB\u3092\
    \u6C42\u3081\u308B.\n\n    Args:\n        u (Modulo_Vector):\n        v (Modulo_Vector):\n\
    \n    Returns:\n        Modulo_Matrix: \u30C6\u30F3\u30BD\u30EB\u7A4D u (x) v\n\
    \    \"\"\"\n\n    M = [[0] * v.size for _ in range(u.size)]\n\n    for i in range(u.size):\n\
    \        M[i] = [u[i] * v[j] for j in range(v.size)]\n    return Modulo_Matrix(M)\n"
  dependsOn: []
  isVerificationFile: false
  path: Modulo_Matrix/Modulo_Vector.py
  requiredBy: []
  timestamp: '2025-03-16 12:46:40+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Modulo_Matrix/Modulo_Vector.py
layout: document
redirect_from:
- /library/Modulo_Matrix/Modulo_Vector.py
- /library/Modulo_Matrix/Modulo_Vector.py.html
title: Modulo_Matrix/Modulo_Vector.py
---
