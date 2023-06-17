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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class Permutation():\n    def __init__(self, n, p=[]):\n        if p==[]:\n\
    \            self.p=[i for i in range(n)]\n            self.ind=[i for i in range(n)]\n\
    \        else:\n            self.p=p\n            self.ind=[0]*n\n\n         \
    \   for i in range(n):\n                self.ind[p[i]]=i\n\n        self.n=n\n\
    \n    def __getitem__(self, k):\n        return self.p[k]\n\n    def __str__(self):\n\
    \        return str(self.p)\n\n    def __repr__(self):\n        return \"[Permutation]\
    \ : \"+str(self)\n\n    def __eq__(self,other):\n        return (self.n==other.n)\
    \ and (self.p==other.p)\n\n    def __iter__(self):\n        return iter(self.p)\n\
    \n    def index(self, x):\n        return self.ind[x]\n\n    def __mul__(self,other):\n\
    \        assert self.n==other.n\n\n        p=self.p; q=other.p\n        return\
    \ Permutation(self.n,  [p[q[i]] for i in range(self.n)])\n\n    def __pow__(self,\
    \ n):\n        if n<0:\n            return pow(self,-n).inverse()\n\n        a=list(range(self.n))\n\
    \        e=self.p[:]\n\n        while n:\n            if n&1:\n              \
    \  a=[a[e[i]] for i in range(self.n)]\n            e=[e[e[i]] for i in range(self.n)]\n\
    \            n>>=1\n\n        return Permutation(self.n, a)\n\n    def __truediv__(self,other):\n\
    \        pass\n\n    def sgn(self):\n        \"\"\" \u7F6E\u63DB\u306E\u7B26\u53F7\
    \u3092\u6C42\u3081\u308B (\u5076\u7F6E\u63DB \u2192 1, \u5947\u7F6E\u63DB \u2192\
    \ -1)\n\n        \"\"\"\n        return -1 if self.minimum_transposition()%2 else\
    \ 1\n\n    def inverse(self):\n        return Permutation(self.n, self.ind)\n\n\
    \    def inversion(self):\n        \"\"\" \u8EE2\u5012\u6570\u3092\u6C42\u3081\
    \u308B.\n        \"\"\"\n\n        BIT=[0]*(self.n+1)\n        Y=(self.n*(self.n-1))//2\n\
    \n        for a in self.p:\n            s=a\n            while 1<=s:\n       \
    \         Y-=BIT[s]\n                s-=s&(-s)\n\n            r=a+1\n        \
    \    while r<=self.n:\n                BIT[r]+=1\n                r+=r&(-r)\n\
    \        return Y\n\n    def swap(self, i, j):\n        \"\"\" i \u756A\u76EE\u3068\
    \ j \u756A\u76EE\u3092\u4EA4\u63DB\u3059\u308B \u203B i \u3068 j \u3092\u4EA4\u63DB\
    \u3067\u306F\u306A\u3044\"\"\"\n\n        u=self.p[i]; v=self.p[j]\n\n       \
    \ self.p[i]=v; self.p[j]=u\n        self.ind[v]=i; self.ind[u]=j\n\n    def transposition(self,\
    \ u, v):\n        \"\"\" u \u3068 v \u3092\u4EA4\u63DB\u3059\u308B \u203B u \u756A\
    \u76EE\u3068v \u756A\u76EE\u3067\u306F\u306A\u3044\"\"\"\n\n        a=self.ind[u];\
    \ b=self.ind[v]\n\n        self.p[a]=v; self.p[b]=u\n        self.ind[u]=b; self.ind[v]=a\n\
    \n    def minimum_transposition(self):\n        \"\"\" \u4E92\u63DB\u306E\u6700\
    \u5C0F\u56DE\u6570\u3092\u6C42\u3081\u308B. \"\"\"\n\n        return self.n-len(self.cycle_division())\n\
    \n    def cycle_division(self, mode=True):\n        \"\"\" \u7F6E\u63DB\u3092\u5DE1\
    \u56DE\u7F6E\u63DB\u306E\u7A4D\u306B\u5206\u89E3\u3059\u308B.\n\n        mode:\
    \ \u81EA\u5DF1\u30EB\u30FC\u30D7\u3092\u5165\u308C\u308B\u304B\u5426\u304B\"\"\
    \"\n\n        p=self.p\n        T=[False]*self.n\n        A=[]\n\n        for\
    \ k in range(self.n):\n            if not T[k]:\n                a=[k]\n\n   \
    \             T[k]=True\n                v=p[k]\n                while v!=k:\n\
    \                    T[v]=True\n                    a.append(v)\n            \
    \        v=p[v]\n\n                if mode or len(a)>=2:\n                   \
    \ A.append(a)\n        return A\n\n    def operate_list(self, list):\n       \
    \ assert self.n==len(list),\"\u7F6E\u63DB\u306E\u9577\u3055\u3068\u30EA\u30B9\u30C8\
    \u306E\u9577\u3055\u304C\u9055\u3044\u307E\u3059.\"\n\n        return [list[self.ind[i]]\
    \ for i in range(self.n)]\n\n\n    def order(self, mod=None):\n        \"\"\"\
    \ \u4F4D\u6570\u3092\u6C42\u3081\u308B (mod \u3092\u6307\u5B9A\u3059\u308B\u3068\
    , mod \u3067\u5272\u3063\u305F\u4F59\u308A\u306B\u306A\u308B).\n\n        \"\"\
    \"\n\n        from math import gcd\n\n        if mod==None:\n            x=1\n\
    \            for m in self.cycle_division():\n                g=gcd(x,len(m))\n\
    \                x=(x//g)*len(m)\n            return x\n        else:\n      \
    \      def factor(n):\n                e=(n&(-n)).bit_length()-1\n           \
    \     yield 2,e\n\n                n>>=e\n\n                p=3\n            \
    \    while p*p<=n:\n                    if n%p==0:\n                        e=0\n\
    \                        while n%p==0:\n                            n//=p\n  \
    \                          e+=1\n                        yield p,e\n         \
    \           p+=2\n\n                if n>1:\n                    yield n,1\n \
    \               return\n\n            T={}\n            for m in self.cycle_division():\n\
    \                for p,e in factor(len(m)):\n                    T[p]=max(T.get(p,0),\
    \ e)\n\n            x=1\n            for p in T:\n                x*=pow(p, T[p],\
    \ mod)\n                x%=mod\n            return x\n\n    def conjugate(self):\n\
    \        return Permutation(self.n, [self.n-1-x for x in self.p])\n\n    def next(self):\n\
    \        y=[]\n        for i in range(self.n-1,0,-1):\n            y.append(self.p[i])\n\
    \            if self.p[i-1]<self.p[i]:\n                y.append(self.p[i-1])\n\
    \                a=self.p[i-1]\n                break\n\n        x=self.p[:i-1]\n\
    \        y.sort()\n        for j,b in enumerate(y):\n            if a<b:\n   \
    \             x.append(b)\n                del y[j]\n                break\n \
    \       return Permutation(self.n, x+y)\n\n#=================================================\n\
    def Permutation_Inversion(P, Q):\n    \"\"\" P \u304B\u3089 Q \u3078\u96A3\u63A5\
    \u9805\u540C\u58EB\u306E\u5165\u308C\u66FF\u3048\u306E\u307F\u306E\u6700\u5C0F\
    \u56DE\u6570\u3092\u6C42\u3081\u308B.\n    \"\"\"\n    R=Q*(P.inverse())\n   \
    \ return R.inversion()\n\ndef List_Inversion(A, B, default=-1):\n    \"\"\"\u9577\
    \u3055\u304C\u7B49\u3057\u3044\u30EA\u30B9\u30C8 A,B \u306B\u5BFE\u3057\u3066\
    , \u4EE5\u4E0B\u306E\u64CD\u4F5C\u306E\u6700\u5C0F\u56DE\u6570\u3092\u6C42\u3081\
    \u308B.\n    \u5217 A[i] \u3068 A[i+1] \u3092\u5165\u308C\u66FF\u3048, B \u3068\
    \u4E00\u81F4\u3055\u305B\u308B.\n    \"\"\"\n\n    from collections import defaultdict\n\
    \n    if len(A)!=len(B):\n        return default\n\n    N=len(A)\n    D=defaultdict(list)\n\
    \n    for i in range(N):\n        D[A[i]].append(i)\n\n    for lis in D:\n   \
    \     D[lis].reverse()\n\n    try:\n        return Permutation(N,[D[B[i]].pop()\
    \ for i in range(N)]).inversion()\n    except:\n        return default\n\n#=================================================\n\
    #\u30E9\u30F3\u30C0\u30E0\u306B\u7F6E\u63DB\u3092\u751F\u6210\u3059\u308B.\ndef\
    \ Random_Permutation(N):\n    from random import shuffle\n    L=list(range(N))\n\
    \    shuffle(L)\n    return Permutation(N,L)\n\ndef Is_Identity(P):\n    for k,a\
    \ in enumerate(P.p):\n        if k!=a:\n            return False\n    return True\n\
    \ndef Generate_Permutation(P, Q):\n    \"\"\" P \u3092 Q \u306B\u3059\u308B\u5909\
    \u63DB\u3092\u8868\u3059\u7F6E\u63DB\u3092\u751F\u6210\u3059\u308B.\n\n    \"\"\
    \"\n    assert len(P)==len(Q)\n    N=len(P)\n    X=[-1]*N\n    for i in range(N):\n\
    \        X[P[i]]=Q[i]\n    return Permutation(N, X)\n"
  dependsOn: []
  isVerificationFile: false
  path: Permutation.py
  requiredBy: []
  timestamp: '2022-12-24 17:45:24+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Permutation.py
layout: document
redirect_from:
- /library/Permutation.py
- /library/Permutation.py.html
title: Permutation.py
---
