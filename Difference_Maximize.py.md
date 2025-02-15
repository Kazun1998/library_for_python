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
  code: "\"\"\"\nNote\n\u901A\u79F0 \"\u725B\u30B2\u30FC\" \u3068\u547C\u3070\u308C\
    \u308B\u554F\u984C\u3092\u89E3\u304F. \u3053\u306E\u554F\u984C\u306F M \u500B\u306E\
    \u6761\u4EF6\n    x[i[m]]-x[j[m]]<=c[m]\n\u306B\u304A\u3044\u3066, x[p]-x[q] \u3092\
    \u6700\u5927\u5316\u3059\u308B. \u306A\u304A, \u3053\u308C\u306F x[q]=0 \u3068\
    \u3044\u3046\u8FFD\u52A0\u5236\u7D04\u5316\u3067\u306E x[p] \u306E\u6700\u5927\
    \u5316\u306B\u306A\u308B.\n\n\u203B \u6700\u77ED\u8DEF\u554F\u984C\u306B\u5E30\
    \u7740\n\"\"\"\n\nclass Difference_Maximize:\n    def __init__(self,N):\n    \
    \    self.N=N\n        self.__arc=[[] for _ in range(N)]\n        self.Neg_edge=False\n\
    \        self.__cost=0\n        self.__taught_DAG=None\n\n    def cost(self):\n\
    \        return self.__cost\n\n    def teaching_DAG(self,mode):\n        \"\"\"\
    \ \u4E0E\u3048\u3089\u308C\u308B\u72B6\u6CC1\u306B\u5BFE\u5FDC\u3059\u308B\u6709\
    \u5411\u30B0\u30E9\u30D5\u304C DAG \u78BA\u5B9A\u304B\u3069\u3046\u304B\u3092\u6559\
    \u3048\u308B.\n\n        \"\"\"\n        self.__is_DAG=mode\n\n    def is_DAG(self):\n\
    \        arc=self.__arc\n\n        in_deg=[0]*self.N\n        for u in range(self.N):\n\
    \            for v,_ in arc[u]:\n                in_deg[v]+=1\n\n        Q=[x\
    \ for x in range(self.N) if in_deg[x]==0]\n\n        S=[]\n        while Q:\n\
    \            u=Q.pop()\n            S.append(u)\n\n            for v,_ in arc[u]:\n\
    \                in_deg[v]-=1\n                if in_deg[v]==0:\n            \
    \        Q.append(v)\n\n        return S if len(S)==self.N else None\n\n    def\
    \ add_constraint(self,i,j,c):\n        \"\"\" x[i]-x[j] <=c \u3068\u3044\u3046\
    \u6761\u4EF6\u3092\u4ED8\u3051\u52A0\u3048\u308B.\n\n        \"\"\"\n\n      \
    \  assert 0<=i<self.N\n        assert 0<=j<self.N\n\n        if c<0:\n       \
    \     self.Neg_edge=True\n\n        self.__arc[j].append((i,c))\n        self.__cost+=1\n\
    \n    def solve(self, base_index=0, base_value=0):\n        \"\"\" x[base]=base_value\
    \ \u3092\u57FA\u6E96\u306B\u3057\u3066\u89E3\u3092\u6C42\u3081\u308B.\n\n    \
    \    \u203B\u5B9F\u884C\u53EF\u80FD\u89E3\u304C\u5B58\u5728\u3057\u306A\u3044\u5834\
    \u5408, \u8FD4\u308A\u5024\u306FNone\u306B\u306A\u308B.\n        \"\"\"\n    \
    \    inf=float(\"inf\")\n        N=self.N\n        arc=self.__arc\n\n        if\
    \ (self.__taught_DAG==None) or (self.__taught_DAG==True):\n            K=self.is_DAG()\n\
    \        else:\n            K=None\n\n        if K!=None:\n            X=[inf]*N;\
    \ X[base_index]=base_value\n            for p in K:\n                for q,c in\
    \ arc[p]:\n                    if X[q]>X[p]+c:\n                        X[q]=X[p]+c\n\
    \            return X\n        elif self.Neg_edge:\n            X=[inf]*N; X[base_index]=base_value\n\
    \n            for _ in range(N):\n                update=0\n                for\
    \ p in range(N):\n                    for q,c in arc[p]:\n                   \
    \     if X[q]>X[p]+c:\n                            X[q]=X[p]+c\n             \
    \               update=1\n\n                    if not update:\n             \
    \           return X\n            return None\n        else:\n            from\
    \ heapq import heapify, heappush, heappop\n\n            arc=self.__arc\n    \
    \        X=[inf]*self.N\n\n            X[base_index]=base_value\n            Q=[(base_value,\
    \ base_index)]\n            while Q:\n                x,i=heappop(Q)\n\n     \
    \           if x>X[i]:\n                    continue\n\n                for j,c\
    \ in arc[i]:\n                    if X[i]+c<X[j]:\n                        X[j]=X[i]+c\n\
    \                        heappush(Q,(X[j],j))\n            return X\n\n    def\
    \ solve_add_by_Warshall_Floyd(self):\n        \"\"\" \u5168\u3066\u306E p,q \u306B\
    \u5BFE\u3059\u308B x[q]-x[p] \u306E\u6700\u5927\u5316\u306E\u7D50\u679C\u3092\
    \ Warshall Floyd \u6CD5\u3067\u6C42\u3081\u308B.\n\n        [Output]\n       \
    \ \u89E3\u304C\u5B58\u5728\u3059\u308B\u5834\u5408\n        2\u6B21\u5143\u30EA\
    \u30B9\u30C8 X \u304C\u8FD4\u3055\u308C\u308B. max x[q]-x[p] \u306E\u89E3\u306F\
    \ x[p]=0 \u3092\u57FA\u6E96\u306B\u3057\u3066 X[p][q] \u306B\u8A18\u9332\u3055\
    \u308C\u308B.\n\n        \u89E3\u304C\u5B58\u5728\u3057\u306A\u3044\u5834\u5408\
    \n        None\n        \"\"\"\n\n        inf=float(\"inf\")\n        arc=self.__arc\n\
    \        N=self.N\n\n        X=[[inf]*N for _ in range(N)]\n        for p in range(N):\n\
    \            x=X[p]\n            x[p]=0\n            for q,cond in arc[p]:\n \
    \               if x[q]>cond:\n                    x[q]=cond\n\n        for k\
    \ in range(N):\n            xk=X[k]\n            for p in range(N):\n        \
    \        xp=X[p]\n                for q in range(N):\n                    if xp[q]>xp[k]+xk[q]:\n\
    \                        xp[q]=xp[k]+xk[q]\n\n        # \u89E3\u7B54\u306E\u5B58\
    \u5728 Check\n        for p in range(N):\n            if X[p][p]<0: return None\n\
    \n        return X\n"
  dependsOn: []
  isVerificationFile: false
  path: Difference_Maximize.py
  requiredBy: []
  timestamp: '2021-10-17 04:54:27+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Difference_Maximize.py
layout: document
redirect_from:
- /library/Difference_Maximize.py
- /library/Difference_Maximize.py.html
title: Difference_Maximize.py
---
