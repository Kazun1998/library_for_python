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
  code: "\"\"\"\n\u5909\u6570 X_i \u306E\u5426\u5B9A\u306F ~i \u3067\u5BA3\u8A00\u3059\
    \u308B.\n\u4F8B\u3048\u3070, ~0=-1 \u306A\u306E\u3067, X_{-1} \u306F not X_0 \u3092\
    \u610F\u5473\u3059\u308B.\n\"\"\"\n\nclass Two_SAT:\n    def __init__(self,N):\n\
    \        \"\"\" N \u5909\u6570\u306E 2-SAT \u3092\u5B9A\u7FA9\u3059\u308B.\n\n\
    \        N: int\n        \"\"\"\n\n        self.N=N\n        self.var_num=N\n\
    \        self.__cost=2*N\n\n        self.arc=[[] for _ in range(2*N)]\n      \
    \  self.rev=[[] for _ in range(2*N)]\n\n    def cost(self):\n        return self.__cost\n\
    \n    def var_to_index(self,v):\n        if v>=0:\n            return 2*v\n  \
    \      else:\n            return 2*(-v-1)+1\n\n    def index_to_var(self,i):\n\
    \        if i%2:\n            return -(i+1)//2\n        else:\n            return\
    \ i//2\n\n    def add_variable(self,k):\n        \"\"\" \u65B0\u305F\u306B\u5909\
    \u6570 k \u500B\u3092\u52A0\u3048\u308B.\n        \"\"\"\n\n        m=self.var_num\n\
    \        self.var_num+=k\n        self.__cost+=2*k\n\n        self.arc+=[[] for\
    \ _ in range(2*k)]\n        self.rev+=[[] for _ in range(2*k)]\n\n        return\
    \ list(range(m,m+k))\n\n    def __add_clause(self,i,j):\n        self.__cost+=1\n\
    \        self.arc[self.var_to_index(i)].append(self.var_to_index(j))\n       \
    \ self.rev[self.var_to_index(j)].append(self.var_to_index(i))\n\n    def add_imply(self,i,j):\n\
    \        \"\"\" X_i -> X_j \u3092\u52A0\u3048\u308B.\n        \"\"\"\n       \
    \ self.__add_clause(i,j)\n        self.__add_clause(~j,~i)\n\n    def add_or(self,i,j):\n\
    \        \"\"\" X_i or X_j \u3092\u52A0\u3048\u308B.\n        \"\"\"\n\n     \
    \   self.add_imply(~i,j)\n\n    def add_nand(self,i,j):\n        \"\"\" not (X_i\
    \ and X_j) \u3092\u52A0\u3048\u308B.\n        \"\"\"\n\n        self.add_imply(i,~j)\n\
    \n    def add_equivalent(self,*I):\n        \"\"\" I=[i_0, ..., i_{k-1}] \u306B\
    \u5BFE\u3057\u3066, X_{i_0}=...=X_{i_{k-1}} \u3092\u8FFD\u52A0\u3059\u308B.\n\
    \        \"\"\"\n\n        k=len(I)\n\n        if k<=1:\n            return\n\n\
    \        for j in range(k-1):\n            self.add_imply(I[j],I[j+1])\n     \
    \   self.add_imply(I[-1],I[0])\n\n    def add_not_equal(self,i,j):\n        \"\
    \"\" X_i != X_j \u3092\u8FFD\u52A0\u3059\u308B.\n        \"\"\"\n        self.add_equal(i,~j)\n\
    \n    def set_true(self,i):\n        \"\"\" \u5909\u6570 X_i \u3092 True \u306B\
    \u3059\u308B.\n        \"\"\"\n\n        self.__add_clause(~i,i)\n\n    def set_false(self,i):\n\
    \        \"\"\" \u5909\u6570 X_i \u3092 False \u306B\u3059\u308B.\n        \"\"\
    \"\n\n        self.__add_clause(i,~i)\n\n    def at_most_one(self,*I):\n     \
    \   \"\"\" X_i (i in I) \u3092\u6E80\u305F\u3059\u3088\u3046\u306A i \u306F\u9AD8\
    \u30051\u3064\u3060\u3051\u3068\u3044\u3046\u6761\u4EF6\u3092\u8FFD\u52A0\u3059\
    \u308B.\n        \"\"\"\n\n        k=len(I)\n\n        if k<=1:\n            return\n\
    \n        A=self.add_variable(k)\n\n        self.add_imply(I[0],A[0])\n      \
    \  for i in range(1,k):\n            self.add_imply(A[i-1],A[i])\n           \
    \ self.add_imply(I[i],A[i])\n            self.add_nand(A[i-1],I[i])\n\n    def\
    \ is_satisfy(self,Mode=0):\n        \"\"\" Two-SAT \u306F\u5145\u8DB3\u53EF\u80FD\
    ?\n\n        Mode:\n        0 (Defalt): \u5145\u8DB3\u53EF\u80FD?\n        1:\
    \ \u5145\u8DB3\u53EF\u80FD\u306A\u3089\u3070,\u305D\u306E\u5909\u6570\u306E\u5272\
    \u5F53\u3092\u4E0E\u3048\u308B (\u4E0D\u53EF\u80FD\u306A\u3068\u304D\u306FNone).\n\
    \        2: \u5145\u8DB3\u4E0D\u80FD\u306E\u539F\u56E0\u3067\u3042\u308B\u5909\
    \u6570\u3092\u5168\u3066\u6319\u3052\u308B.\n        \"\"\"\n        N=self.var_num\n\
    \        Group=[0]*(2*N)\n        Order=[]\n\n        for s in range(2*N):\n \
    \           if Group[s]:continue\n\n            S=[s]\n            Group[s]=-1\n\
    \n            while S:\n                u=S.pop()\n                for v in self.arc[u]:\n\
    \                    if Group[v]:continue\n                    Group[v]=-1\n \
    \                   S.append(u);S.append(v)\n                    break\n     \
    \           else:\n                    Order.append(u)\n\n        K=0\n      \
    \  for s in Order[::-1]:\n            if Group[s]!=-1:continue\n\n           \
    \ S=[s]\n            Group[s]=K\n\n            while S:\n                u=S.pop()\n\
    \                for v in self.rev[u]:\n                    if Group[v]!=-1:continue\n\
    \n                    Group[v]=K\n                    S.append(v)\n          \
    \  K+=1\n\n        if Mode==0:\n            for i in range(N):\n             \
    \   if Group[2*i]==Group[2*i+1]:\n                    return False\n         \
    \   return True\n        elif Mode==1:\n            T=[0]*N\n            for i\
    \ in range(N):\n                if Group[2*i]>Group[2*i+1]:\n                \
    \    T[i]=1\n                elif Group[2*i]==Group[2*i+1]:\n                \
    \    return None\n            return T[:self.N]\n        elif Mode==2:\n     \
    \       return [i for i in range(self.N) if Group[2*i]==Group[2*i+1]]\n\n    def\
    \ solve(self):\n        return self.is_satisfy(1)\n"
  dependsOn: []
  isVerificationFile: false
  path: Two-SAT.py
  requiredBy: []
  timestamp: '2021-11-28 16:16:29+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Two-SAT.py
layout: document
redirect_from:
- /library/Two-SAT.py
- /library/Two-SAT.py.html
title: Two-SAT.py
---
