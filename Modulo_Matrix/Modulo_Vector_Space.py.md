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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.6/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.6/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from Modulo_Matrix import *\nfrom Modulo_Vector import *\n\nclass Modulo_Vector_Space:\n\
    \    def __init__(self, dim):\n        \"\"\" \u6B21\u5143\u304C dim \u306E\u30D9\
    \u30AF\u30C8\u30EB\u7A7A\u9593\u306E\u90E8\u5206\u7A7A\u9593\u3092\u751F\u6210\
    \u3059\u308B.\n\n        \"\"\"\n\n        self.dim=dim\n        self.basis=[]\n\
    \        self.__ind=[]\n\n    def __contains__(self, v):\n        for i,u in zip(self.__ind,\
    \ self.basis):\n            v-=v[i]*u\n        return not bool(v)\n\n    def add_vectors(self,\
    \ *S):\n        for v in S:\n            assert len(v)==self.dim\n           \
    \ for i,u in zip(self.__ind, self.basis):\n                v-=v[i]*u\n\n     \
    \       if bool(v):\n                for j in range(self.dim):\n             \
    \       if v[j]:\n                        self.__ind.append(j)\n             \
    \           break\n                v=pow(v[j], -1, Mod) * v\n                self.basis.append(v)\n\
    \n                for k in range(len(self.basis)-1):\n                    self.basis[k]-=self.basis[k][j]*v\n\
    \n    def dimension(self):\n        return len(self.basis)\n\n    def __le__(self,\
    \ other):\n        for u in self.basis:\n            if u not in other:\n    \
    \            return False\n        return True\n\n    def __ge__(self, other):\n\
    \        return other<=self\n\n    def __eq__(self, other):\n        return (self<=other)\
    \ and (other<=self)\n\n    def refresh(self):\n        I=sorted(range(len(self.__ind)),\
    \ key=lambda i:self.__ind[i])\n        self.basis=[self.basis[i] for i in I]\n\
    \        self.__ind=[self.__ind[i] for i in I]\n\n    def projection(self, v):\n\
    \        for i,u in zip(self.__ind, self.basis):\n            v-=v[i]*u\n    \
    \    return v\n\n#====================\ndef Overall(dim):\n    V=Modulo_Vector_Space(dim)\n\
    \    V.add_vectors(*[Standard_Basis(dim,k) for k in range(dim)])\n    return V\n\
    \ndef Kernel_Space(A):\n    \"\"\" \u884C\u5217 A \u306E\u6838\u7A7A\u9593 Ker\
    \ A (Ax=0 \u3068\u306A\u308B x \u306E\u7A7A\u9593) \u3092\u6C42\u3081\u308B.\n\
    \n    \"\"\"\n\n    row,col=A.size\n    T=deepcopy(A.ele)\n\n    p=[]; q=[]\n\
    \    rnk=0\n    for j in range(col):\n        for i in range(rnk,row):\n     \
    \       if T[i][j]!=0:\n                break\n        else:\n            q.append(j)\n\
    \            continue\n\n        p.append(j)\n        T[rnk],T[i]=T[i],T[rnk]\n\
    \n        inv=pow(T[rnk][j], -1, Mod)\n        for k in range(col):\n        \
    \    T[rnk][k]=(inv*T[rnk][k])%Mod\n\n        for s in range(row):\n         \
    \   if s==rnk:\n                continue\n            c=-T[s][j]\n           \
    \ for t in range(col):\n                T[s][t]=(T[s][t]+c*T[rnk][t])%Mod\n  \
    \      rnk+=1\n\n    x=[0]*col\n    for i in range(rnk):\n        x[p[i]]=T[i][-1]\n\
    \n    ker_dim=col-rnk\n    ker=[[0]*col for _ in range(ker_dim)]\n\n    for i\
    \ in range(ker_dim):\n        ker[i][q[i]]=1\n\n    for i in range(ker_dim):\n\
    \        for j in range(rnk):\n            ker[i][p[j]]=-T[j][q[i]]%Mod\n\n  \
    \  Ker=Modulo_Vector_Space(col)\n    Ker.add_vectors(*[Modulo_Vector(v) for v\
    \ in ker])\n    return Ker\n\ndef Image_Space(A):\n    \"\"\" A \u306E\u50CF\u7A7A\
    \u9593 Im A \u3092\u6C42\u3081\u308B.\n\n    \"\"\"\n\n    V=Modulo_Vector_Space(A.row)\n\
    \    V.add_vectors(*Column_Vector(A))\n    return V\n\ndef Linear_System_Equations(A,b):\n\
    \    if type(A) is Modulo_Matrix:\n        row,col=A.size\n        T=deepcopy(A.ele)\n\
    \    else:\n        row,col=len(A),len(A[0])\n        T=deepcopy(A)\n\n    assert\
    \ row==len(b), \"A \u306E\u884C\u3068 b \u306E\u6B21\u5143\u304C\u4E00\u81F4\u3057\
    \u307E\u305B\u3093.\"\n\n    for i in range(row):\n        T[i].append(b[i])\n\
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
    \ x,ker\n"
  dependsOn: []
  isVerificationFile: false
  path: Modulo_Matrix/Modulo_Vector_Space.py
  requiredBy: []
  timestamp: '2023-08-26 01:58:57+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Modulo_Matrix/Modulo_Vector_Space.py
layout: document
redirect_from:
- /library/Modulo_Matrix/Modulo_Vector_Space.py
- /library/Modulo_Matrix/Modulo_Vector_Space.py.html
title: Modulo_Matrix/Modulo_Vector_Space.py
---
