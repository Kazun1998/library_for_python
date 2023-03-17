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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.2/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.2/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "\"\"\" Note: Projection Selection Problem \u3067\u5BFE\u5FDC\u3067\u304D\u308B\
    \u6761\u4EF6\u306E\u4E00\u89A7\n\nh(x)=0 \u306A\u3089\u3070 a \u70B9\u5F97\u308B\
    \ \u2192 set_zero(x,a)\nh(x)=1 \u306A\u3089\u3070 a \u70B9\u5F97\u308B \u2192\
    \ set_one(x,a)\nh(x)=0 \u304B\u3064 h(y)=1 \u306A\u3089\u3070 a (<=0) \u70B9\u3092\
    \u5F97\u308B \u2192 set_not_equal(x,y,a)\nh(x_0)=...=h(x_{k-1})=0 \u306A\u3089\
    \u3070 a (>=0) \u70B9\u3092\u5F97\u308B \u2192 set_all_zero(X,a)\nh(x_0)=...=h(x_{k-1})=1\
    \ \u306A\u3089\u3070 a (>=0) \u70B9\u3092\u5F97\u308B \u2192 set_all_one(X,a)\n\
    \n\u4E00\u822C\u7684\u306A\u30B0\u30E9\u30D5\u3067\u306F\u5BFE\u5FDC\u3067\u304D\
    \u306A\u3044\u6761\u4EF6\u306E\u4F8B\n[1]\nh(x)=h(y)=0 \u306A\u3089\u3070 a (<=0)\
    \ \u70B9\u3092\u5F97\u308B\nh(x)=h(y)=1 \u306A\u3089\u3070 a (<=0) \u70B9\u3092\
    \u5F97\u308B\n\u2192 \u30B0\u30E9\u30D5\u304C\u4E8C\u90E8\u30B0\u30E9\u30D5 (\u90E8\
    \u96C6\u5408\u3092 X,Y \u3068\u3059\u308B) \u3067\u3042\u308A, x in X,y in Y \u306A\
    \u3089\u3070, \u4EE5\u4E0B\u306E\u3088\u3046\u306B\u3057\u3066\u5909\u63DB\u3059\
    \u308B.\nh'(z)=h(x) (x in X), 1-h(y) (y in Y) \u3068\u3057\u3066, h' \u3067\u306E\
    \u6761\u4EF6 \u300Ch'(x),h'(y) \u304C\u30FB\u30FB\u30FB \u306A\u3089\u3070, a\
    \ (<=0) \u70B9\u3092\u5F97\u308B\u300D\u306B\u7F6E\u304D\u63DB\u3048\u308B.\n\n\
    [2]\nh(x) != h(y) \u306A\u3089\u3070, a (>=0) \u70B9\u3092\u5F97\u308B\n\u2192\
    \u30B0\u30E9\u30D5\u304C\u4E8C\u90E8\u30B0\u30E9\u30D5 (\u90E8\u96C6\u5408\u3092\
    \ X,Y \u3068\u3059\u308B) \u3067\u3042\u308A, x in X,y in Y \u306A\u3089\u3070\
    , \u4EE5\u4E0B\u306E\u3088\u3046\u306B\u3057\u3066\u5909\u63DB\u3059\u308B.\n\
    h'(z)=h(x) (x in X), 1-h(y) (y in Y) \u3068\u3057\u3066\n\u7121\u6761\u4EF6\u306B\
    \ a \u70B9\u3092\u5F97\u3066, h' \u3067\u306E\u6761\u4EF6 \u300Ch'(x)=h'(y) \u306A\
    \u3089\u3070, -a (<=0) \u70B9\u3092\u5F97\u308B (\u3064\u307E\u308A [1])\u300D\
    \u306B\u5E30\u7740\u3059\u308B.\n\u6700\u7D42\u7684\u306B\u306F, \u7121\u6761\u4EF6\
    \u306B a \u70B9\u5F97\u3066, \u300Ch(x)=h(y) \u306A\u3089\u3070 -a (<=0) \u70B9\
    \u3092\u5F97\u308B\u300D\u3068\u3044\u3046\u6761\u4EF6\u306B\u5E30\u7740\u3055\
    \u308C\u308B (h''=h \u306A\u306E\u3067)\n\u203B\u4E0B\u99C4\u3092\u5C65\u304B\u305B\
    \u308B\u3053\u3068\u3068, \u4E0B\u99C4\u3092A, \u5E30\u7740\u554F\u984C\u306E\u7B54\
    \u3048\u3092 X \u3068\u3057\u305F\u3068\u304D, \u5143\u554F\u984C\u306E\u7B54\u3048\
    \u306F A+X \u306B\u306A\u308B\u3053\u3068\u306B\u6CE8\u610F!!\n\"\"\"\n\nfrom\
    \ Flow import *\n\ninf=float(\"inf\")\nclass Project_Selection_Problem:\n    def\
    \ __init__(self,N=0):\n        \"\"\" N \u8981\u7D20\u306E Project Selection Problem\
    \ \u3092\u751F\u6210\u3059\u308B.\n\n        N: int\n        \"\"\"\n\n      \
    \  self.N=N\n        self.ver_num=N+2\n        self.base=0\n        self.source=N\n\
    \        self.target=N+1\n        self.indivi=[[0,0] for _ in range(N+2)]\n  \
    \      self.mutual=[]\n\n    def add_vertex(self):\n        n=self.ver_num\n \
    \       self.indivi.append([0,0])\n        self.ver_num+=1\n        return n\n\
    \n    def __add_vertex_inner(self):\n        n=self.ver_num\n        self.indivi.append([None,None])\n\
    \        self.ver_num+=1\n        return n\n\n    def add_vertices(self, k):\n\
    \        n=self.ver_num\n        self.indivi.extend([[0,0] for _ in range(k)])\n\
    \        self.ver_num+=k\n        return list(range(n,n+k))\n\n    def set_zero_one(self,x,y,a):\n\
    \        \"\"\" h(x)=0,  h(y)=1 \u306E\u3068\u304D, a (<=0) \u70B9\u3092\u5F97\
    \u308B\u3068\u3044\u3046\u6761\u4EF6\u3092\u8FFD\u52A0\u3059\u308B.\n\n      \
    \  0<=x,y<N\n        a<=0\n        \"\"\"\n\n        assert 0<=x<self.N\n    \
    \    assert 0<=y<self.N\n        assert a<=0\n\n        self.mutual.append((x,y,-a))\n\
    \n    def set_zero(self,x,a):\n        \"\"\" h(x)=0 \u306E\u3068\u304D, a \u70B9\
    \u3092\u5F97\u308B\u3068\u3044\u3046\u6761\u4EF6\u3092\u8FFD\u52A0\u3059\u308B\
    .\n\n        0<=x<N\n        \"\"\"\n\n        assert 0<=x<self.N\n        self.indivi[x][0]+=a\n\
    \n    def set_one(self,x,a):\n        \"\"\" h(x)=1 \u306E\u3068\u304D, a \u70B9\
    \u3092\u5F97\u308B\u3068\u3044\u3046\u6761\u4EF6\u3092\u8FFD\u52A0\u3059\u308B\
    .\n\n        0<=x<N\n        \"\"\"\n\n        assert 0<=x<self.N\n        self.indivi[x][1]+=a\n\
    \n    def set_all_zero(self,X,a):\n        \"\"\" h(x)=0 (forall x in X) \u306E\
    \u3068\u304D, a (>=0) \u70B9\u3092\u5F97\u308B\u3068\u3044\u3046\u6761\u4EF6\u3092\
    \u8FFD\u52A0\u3059\u308B.\n\n        0<=x<N\n        a>=0\n        \"\"\"\n\n\
    \        assert a>=0\n\n        k=self.__add_vertex_inner()\n        self.base+=a\n\
    \n        self.indivi[k][0]=-a\n        for x in X:\n            assert 0<=x<self.N\n\
    \            self.mutual.append((k,x,inf))\n\n    def set_all_one(self,X,a):\n\
    \        \"\"\" h(x)=1 (forall x in X) \u306E\u3068\u304D, a (>=0) \u70B9\u3092\
    \u5F97\u308B\u3068\u3044\u3046\u6761\u4EF6\u3092\u8FFD\u52A0\u3059\u308B.\n\n\
    \        0<=x<N\n        a>=0\n        \"\"\"\n\n        assert a>=0\n\n     \
    \   k=self.__add_vertex_inner()\n        self.base+=a\n\n        self.indivi[k][1]=-a\n\
    \        for x in X:\n            assert 0<=x<self.N\n            self.mutual.append((x,k,inf))\n\
    \n    def set_not_equal(self,x,y,a):\n        \"\"\" h(x)!=h(y) \u306A\u3089\u3070\
    , a (<=0) \u70B9\u3092\u5F97\u308B\u3068\u3044\u3046\u6761\u4EF6\u3092\u8FFD\u52A0\
    \u3059\u308B.\n\n        0<=x,y<N\n        a<=0\n        \"\"\"\n\n        assert\
    \ 0<=x<self.N and 0<=y<self.N\n        assert a<=0\n\n        self.set_zero_one(x,y,a)\n\
    \        self.set_zero_one(y,x,a)\n\n    def set_equal(self,x,y,a):\n        \"\
    \"\" h(x)=h(y) \u306A\u3089\u3070, a (>=0) \u70B9\u3092\u5F97\u308B\u3068\u3044\
    \u3046\u6761\u4EF6\u3092\u8FFD\u52A0\u3059\u308B.\n\n        0<=x,y<N\n      \
    \  a>=0\n        \"\"\"\n\n        assert 0<=x<self.N and 0<=y<self.N\n      \
    \  assert a>=0\n\n        self.set_all_zero([x,y],a)\n        self.set_all_one([x,y],a)\n\
    \n    def ban_zero(self,x):\n        \"\"\" h(x)=0 \u3068\u306A\u308B\u3053\u3068\
    \u3092\u7981\u6B62\u3059\u308B. (\u5B9F\u884C\u3057\u305F\u3089 -inf \u70B9\u306B\
    \u306A\u308B)\n\n        0<=x<N\n        \"\"\"\n\n        assert 0<=x<self.N\n\
    \        self.set_zero(x,-inf)\n\n    def ban_one(self,x):\n        \"\"\" h(x)=1\
    \ \u3068\u306A\u308B\u3053\u3068\u3092\u7981\u6B62\u3059\u308B. (\u5B9F\u884C\u3057\
    \u305F\u3089 -inf \u70B9\u306B\u306A\u308B)\n\n        0<=x<N\n        \"\"\"\n\
    \n        assert 0<=x<self.N\n        self.set_one(x,-inf)\n\n    def solve(self,Mode=0):\n\
    \        \"\"\" Project Selection Problem \u3092\u89E3\u304F.\n\n        Mode\n\
    \        0: \u6700\u5927\u5024\u306E\u307F\n        1: \u6700\u5927\u5024\u3068\
    \u305D\u308C\u3092\u9054\u6210\u3059\u308B\u4F8B\n        \"\"\"\n\n        F=MaxFlow(self.ver_num)\n\
    \        base=self.base\n        for i in range(self.N):\n            F.add_arc(self.source,i,0)\n\
    \            F.add_arc(i,self.target,0)\n\n            if self.indivi[i][0]>=0:\n\
    \                base+=self.indivi[i][0]\n                F.add_arc(self.source,i,self.indivi[i][0])\n\
    \            else:\n                F.add_arc(i,self.target,-self.indivi[i][0])\n\
    \n            if self.indivi[i][1]>=0:\n                base+=self.indivi[i][1]\n\
    \                F.add_arc(i,self.target,self.indivi[i][1])\n            else:\n\
    \                F.add_arc(self.source,i,-self.indivi[i][1])\n\n        for i\
    \ in range(self.target+1,self.ver_num):\n            if self.indivi[i][0]!=None:\n\
    \                F.add_arc(self.source,i,-self.indivi[i][0])\n            if self.indivi[i][1]!=None:\n\
    \                F.add_arc(i,self.target,-self.indivi[i][1])\n\n        for x,y,c\
    \ in self.mutual:\n            F.add_arc(x,y,c)\n\n        alpha=F.max_flow(self.source,self.target)\n\
    \        if Mode==0:\n            return base-alpha\n        else:\n         \
    \   return base-alpha, F.min_cut(self.source), self.source, self. target\n"
  dependsOn: []
  isVerificationFile: false
  path: Flow/Projection_Selection_Problem.py
  requiredBy: []
  timestamp: '2022-07-17 14:42:36+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Flow/Projection_Selection_Problem.py
layout: document
redirect_from:
- /library/Flow/Projection_Selection_Problem.py
- /library/Flow/Projection_Selection_Problem.py.html
title: Flow/Projection_Selection_Problem.py
---
