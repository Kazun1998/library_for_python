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
  code: "from Modulo_Matrix import *\nfrom Modulo_Vector import *\n\nclass Modulo_Vector_Space:\n\
    \    def __init__(self, n: int, *vectors: \"Modulo_Vector\"):\n        \"\"\"\
    \ n \u6B21\u5143\u306E F \u4FC2\u6570\u6570\u30D9\u30AF\u30C8\u30EB\u7A7A\u9593\
    \u3092\u751F\u6210\u3059\u308B. \u6700\u521D\u306F\u30BC\u30ED\u7A7A\u9593.\n\n\
    \        Args:\n            n (int): \u6B21\u5143\n        \"\"\"\n\n        self.__n\
    \ = n\n        self.basis: list[Modulo_Vector] = []\n        self.__ind: list[int]\
    \ = []\n\n        self.add_vectors(*vectors)\n\n    @property\n    def n(self):\n\
    \        return self.__n\n\n    def __contains__(self, v: Modulo_Vector) -> bool:\n\
    \        return self.projection(v).is_zero()\n\n    def add_vectors(self, *S:\
    \ Modulo_Vector):\n        for v in S:\n            if (v := self.projection(v)).is_zero():\n\
    \                continue\n\n            for j in range(self.n):\n           \
    \     if v[j]:\n                    self.__ind.append(j)\n                   \
    \ break\n\n            v = pow(v[j], -1, Mod) * v\n            self.basis.append(v)\n\
    \n            for k in range(len(self.basis)-1):\n                self.basis[k]\
    \ -= self.basis[k][j] * v\n\n    def dimension(self) -> int:\n        return len(self.basis)\n\
    \n    def __le__(self, other: \"Modulo_Vector_Space\") -> bool:\n        return\
    \ all(u in other for u in self.basis)\n\n    def __ge__(self, other: \"Modulo_Vector_Space\"\
    ) -> bool:\n        return other <= self\n\n    def __eq__(self, other):\n   \
    \     return (self <= other) and (other <= self)\n\n    def refresh(self):\n \
    \       I = sorted(range(self.dimension()), key = lambda i: self.__ind[i])\n\n\
    \        self.basis = [self.basis[i] for i in I]\n        self.__ind = [self.__ind[i]\
    \ for i in I]\n\n    def projection(self, v: Modulo_Vector) -> Modulo_Vector:\n\
    \        for i, u in zip(self.__ind, self.basis):\n            v -= v[i] * u\n\
    \        return v\n\n    def __str__(self):\n        if self.basis:\n        \
    \    return f\"dimention: {self.n}, basis: {', '.join(map(str, self.basis))}\"\
    \n        else:\n            return f\"dimention: {self.n}, basis: (empty)\"\n\
    \n    def __repr__(self):\n        if self.basis:\n            return f\"{self.__class__.__name__}({self.n},\
    \ {', '.join(map(repr, self.basis))})\"\n        else:\n            return f\"\
    {self.__class__.__name__}({self.n})\"\n\n#====================\ndef Overall(n:\
    \ int) -> Modulo_Vector_Space:\n    \"\"\" n \u6B21\u5143\u306E\u6570\u30D9\u30AF\
    \u30C8\u30EB\u7A7A\u9593 F^n \u3092\u751F\u6210\u3059\u308B.\n\n    Args:\n  \
    \      n (int): \u6B21\u5143\n\n    Returns:\n        Modulo_Vector: F^n\n   \
    \ \"\"\"\n\n    V = Modulo_Vector_Space(n)\n    V.add_vectors(*[Standard_Basis(n,\
    \ k) for k in range(n)])\n    return V\n\ndef Kernel_Space(A: Modulo_Matrix) ->\
    \ Modulo_Vector_Space:\n    \"\"\" \u884C\u5217 A \u306E\u6838\u7A7A\u9593 Ker\
    \ A (Ax=0 \u3068\u306A\u308B x \u306E\u7A7A\u9593) \u3092\u6C42\u3081\u308B.\n\
    \n    Args:\n        A (Modulo_Matrix): \u884C\u5217\n\n    Returns:\n       \
    \ Modulo_Vector_Space: Ker A\n    \"\"\"\n\n    row,col=A.size\n    T=deepcopy(A.ele)\n\
    \n    p=[]; q=[]\n    rnk=0\n    for j in range(col):\n        for i in range(rnk,row):\n\
    \            if T[i][j]!=0:\n                break\n        else:\n          \
    \  q.append(j)\n            continue\n\n        p.append(j)\n        T[rnk],T[i]=T[i],T[rnk]\n\
    \n        inv=pow(T[rnk][j], -1, Mod)\n        for k in range(col):\n        \
    \    T[rnk][k]=(inv*T[rnk][k])%Mod\n\n        for s in range(row):\n         \
    \   if s==rnk:\n                continue\n            c=-T[s][j]\n           \
    \ for t in range(col):\n                T[s][t]=(T[s][t]+c*T[rnk][t])%Mod\n  \
    \      rnk+=1\n\n    x=[0]*col\n    for i in range(rnk):\n        x[p[i]]=T[i][-1]\n\
    \n    ker_dim=col-rnk\n    ker=[[0]*col for _ in range(ker_dim)]\n\n    for i\
    \ in range(ker_dim):\n        ker[i][q[i]]=1\n\n    for i in range(ker_dim):\n\
    \        for j in range(rnk):\n            ker[i][p[j]]=-T[j][q[i]]%Mod\n\n  \
    \  Ker=Modulo_Vector_Space(col)\n    Ker.add_vectors(*[Modulo_Vector(v) for v\
    \ in ker])\n    return Ker\n\ndef Image_Space(A: Modulo_Matrix) -> Modulo_Vector_Space:\n\
    \    \"\"\" A \u306E\u50CF\u7A7A\u9593 Im A \u3092\u6C42\u3081\u308B.\n\n    Args:\n\
    \        A (Modulo_Matrix): \u884C\u5217\n\n    Returns:\n        Modulo_Vector_Space:\
    \ Im A\n    \"\"\"\n\n    V = Modulo_Vector_Space(A.row)\n    V.add_vectors(*Column_Vector(A))\n\
    \    return V\n\ndef Linear_System_Equations(A: Modulo_Matrix, b: Modulo_Vector)\
    \ -> tuple[Modulo_Vector, Modulo_Vector_Space] | None:\n    \"\"\" A x = b \u3092\
    \u6E80\u305F\u3059 x \u306E\u89E3\u7A7A\u9593\u3092\u6C42\u3081\u308B.\n\n   \
    \ Args:\n        A (Modulo_Matrix): \u884C\u5217\n        b (Modulo_Vector): \u30D9\
    \u30AF\u30C8\u30EB\n\n    Returns:\n        tuple[Modulo_Vector, Modulo_Vector_Space]\
    \ | None:\n            \u89E3\u304C\u5B58\u5728\u3057\u306A\u3044\u5834\u5408\u306F\
    \ None\n            \u89E3\u304C\u5B58\u5728\u3059\u308B\u5834\u5408, \u89E3\u7A7A\
    \u9593\u306F\u3042\u308B\u30D9\u30AF\u30C8\u30EB c \u3092\u7528\u3044\u3066, c\
    \ + Ker A \u3068\u306A\u308B\u305F\u3081, (c, Ker A) \u3092\u8FD4\u3059.\n   \
    \ \"\"\"\n\n    row, col = A.size\n    T = deepcopy(A.ele)\n\n    if row != b.size:\n\
    \        raise ValueError(\"A \u306E\u884C\u3068 b \u306E\u6B21\u5143\u304C\u4E00\
    \u81F4\u3057\u307E\u305B\u3093.\")\n\n    for i in range(row):\n        T[i].append(b[i])\n\
    \n    p=[]; q=[]\n    rnk=0\n    for j in range(col+1):\n        for i in range(rnk,row):\n\
    \            if T[i][j]!=0:\n                break\n        else:\n          \
    \  q.append(j)\n            continue\n        if j==col:\n            return None\n\
    \        p.append(j)\n        T[rnk],T[i]=T[i],T[rnk]\n\n        inv=pow(T[rnk][j],\
    \ -1, Mod)\n        for k in range(col+1):\n            T[rnk][k]=(inv*T[rnk][k])%Mod\n\
    \n        for s in range(row):\n            if s==rnk:\n                continue\n\
    \            c=-T[s][j]\n            for t in range(col+1):\n                T[s][t]=(T[s][t]+c*T[rnk][t])%Mod\n\
    \        rnk+=1\n\n    x=[0]*col\n    for i in range(rnk):\n        x[p[i]]=T[i][-1]\n\
    \n    ker_dim=col-rnk\n    ker=[[0]*col for _ in range(ker_dim)]\n\n    for i\
    \ in range(ker_dim):\n        ker[i][q[i]]=1\n\n    for i in range(ker_dim):\n\
    \        for j in range(rnk):\n            ker[i][p[j]]=-T[j][q[i]]%Mod\n    return\
    \ x,ker\n\ndef Intersection(*V: Modulo_Vector_Space) -> Modulo_Vector_Space:\n\
    \    \"\"\" \u5171\u901A\u90E8\u5206\u306E\u30D9\u30AF\u30C8\u30EB\u7A7A\u9593\
    \u3092\u6C42\u3081\u308B.\n\n    Args:\n        V (Modulo_Vector_Space): \u5171\
    \u901A\u90E8\u5206\u3092\u6C42\u3081\u308B\u30D9\u30AF\u30C8\u30EB\u7A7A\u9593\
    \ (\u3059\u3079\u3066\u306E\u30D9\u30AF\u30C8\u30EB\u7A7A\u9593\u304C\u5C5E\u3059\
    \u308B\u30D9\u30AF\u30C8\u30EB\u306E\u30B5\u30A4\u30BA\u304C\u4E00\u81F4\u3057\
    \u3066\u3044\u306A\u304F\u3066\u306F\u306A\u3089\u306A\u3044)\n\n    Returns:\n\
    \        Modulo_Vector_Space: \u5171\u901A\u90E8\u5206\u3092\u6C42\u3081\u308B\
    \u30D9\u30AF\u30C8\u30EB\u7A7A\u9593\n    \"\"\"\n\n    n = V[0].n\n    Y = Overall(n)\n\
    \n    for X in V:\n        s = Y.dimension()\n\n        Z = Modulo_Vector_Space(n)\n\
    \        for b in Kernel_Space(Vectoric_Matrix(Y.basis + X.basis, column = True)).basis:\n\
    \            x = sum((b[i] * Y.basis[i] for i in range(s)), start = Zero_Vector(n))\n\
    \            Z.add_vectors(x)\n\n            if len(Z.basis) >= s:\n         \
    \       break\n\n        Y = Z\n\n    return Y\n"
  dependsOn: []
  isVerificationFile: false
  path: Modulo_Matrix/Modulo_Vector_Space.py
  requiredBy: []
  timestamp: '2025-03-16 13:56:44+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Modulo_Matrix/Modulo_Vector_Space.py
layout: document
redirect_from:
- /library/Modulo_Matrix/Modulo_Vector_Space.py
- /library/Modulo_Matrix/Modulo_Vector_Space.py.html
title: Modulo_Matrix/Modulo_Vector_Space.py
---
