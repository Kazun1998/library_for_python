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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.7/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.7/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from Tree import *\n\nclass Forest():\n    def __init__(self, N, index=0):\n\
    \        self.N=N\n        self.index=index\n        self.parent=[-1]*(N+index)\n\
    \        self.__mutable=True\n\n    def vertex_exist(self,x):\n        \"\"\"\
    \ \u9802\u70B9 x \u304C\u5B58\u5728\u3059\u308B\u304B\u3069\u3046\u304B\u3092\u5224\
    \u5B9A\u3059\u308B. \"\"\"\n\n        return self.index<=x<self.index+self.N\n\
    \n    def __after_seal_check(self,*vertexes):\n        \"\"\" \u6728\u304C\u78BA\
    \u5B9A\u3057\u3066\u3044\u3066, vertexes \u306E\u9802\u70B9\u304C\u5B58\u5728\u3059\
    \u308B\u304B\u3069\u3046\u304B\u3092\u30C1\u30A7\u30C3\u30AF\u3059\u308B. \"\"\
    \"\n\n        if self.__mutable:\n            return False\n\n        for v in\
    \ vertexes:\n            if not self.vertex_exist(v):\n                return\
    \ False\n        return True\n\n    def is_mutable(self):\n        \"\"\" \u6728\
    \u304C\u78BA\u5B9A\u3057\u3066 [\u3044\u306A\u3044] \u304B\u3069\u3046\u304B\u3092\
    \u8FD4\u3059. \"\"\"\n        return self.__mutable\n\n    #\u8A2D\u5B9A\u30D1\
    \u30FC\u30C8\n    def root_set(self,root):\n        \"\"\" \u9802\u70B9 x \u3092\
    \u6839\u306B\u8A2D\u5B9A\u3059\u308B.\"\"\"\n\n        assert self.vertex_exist(root)\n\
    \        assert self.__mutable\n\n        self.parent[root]=-1\n\n    def parent_set(self,x,y):\n\
    \        \"\"\" \u9802\u70B9 x \u306E\u89AA\u3092 y \u306B\u8A2D\u5B9A\u3059\u308B\
    .\"\"\"\n\n        assert self.vertex_exist(x)\n        assert self.vertex_exist(y)\n\
    \        assert self.__mutable\n\n        self.parent[x]=y\n\n    def child_set(self,x,y):\n\
    \        \"\"\" \u9802\u70B9 x \u306E\u5B50\u306E\u4E00\u3064\u306B y \u3092\u8A2D\
    \u5B9A\u3059\u308B.\"\"\"\n\n        assert self.vertex_exist(x)\n        assert\
    \ self.vertex_exist(y)\n        assert self.__mutable\n\n        self.parent[y]=x\n\
    \n    def seal(self):\n        \"\"\" \u6728\u306E\u60C5\u5831\u3092\u78BA\u5B9A\
    \u3055\u305B\u308B.\"\"\"\n\n        assert self.__mutable\n        from collections\
    \ import deque\n\n        a=self.index\n        b=self.index+self.N\n        C=[[]\
    \ for _ in range(b)]\n\n        self.component_id=[-1]*b\n        self.vertex_number=[0]*b\n\
    \        self.vertex=[]\n        self.root=[]\n        \n        pa=self.parent\n\
    \        ve=self.vertex_exist\n\n        for w in range(a,b):\n            if\
    \ pa[w]!=-1:\n                C[pa[w]].append(w)\n\n        m=0\n        k=0\n\
    \        for v in range(a,b):\n            if pa[v]!=-1:\n                continue\n\
    \n            self.root.append(v)\n            i=0\n\n            self.component_id[v]=k\n\
    \            self.vertex.append([])\n\n            Q=deque([v])\n            while\
    \ Q:\n                w=Q.popleft()\n                m+=1\n                self.vertex_number[w]=i;\
    \ i+=1\n                self.vertex[-1].append(w)\n\n                for u in\
    \ C[w]:\n                    if self.component_id[u]==-1:\n                  \
    \      self.component_id[u]=k\n                        Q.append(u)\n         \
    \   k+=1\n\n        assert m==self.N           \n\n        self.__mutable=False\n\
    \        self.tree=[]\n        for j in range(k):\n            T=Tree(len(self.vertex[j]))\n\
    \n            T.root_set(0)\n            for v in self.vertex[j]:\n          \
    \      for w in C[v]:\n                    T.parent_set(self.vertex_number[w],\
    \ self.vertex_number[v])\n\n            T.seal()\n            self.tree.append(T)\n\
    \n        self.children=C\n        self.component_number=k\n\n    def depth_search(self,\
    \ Mode=True):\n        \"\"\" \u5404\u9802\u70B9\u306E\u6DF1\u3055\u3092\u6C42\
    \u3081\u308B. \"\"\"\n\n        assert self.__after_seal_check()\n        if hasattr(self,\"\
    depth\"):\n            if Mode:\n                return self.depth\n         \
    \   else:\n                return\n\n        for T in self.tree:\n           \
    \ M=T.depth_search(1)\n\n        self.depth=[0]*(self.N+self.index)\n        ve=self.vertex\n\
    \        nu=self.vertex_number\n        for k in range(self.component_number):\n\
    \            T=self.tree[k]\n            for i,v in enumerate(ve[k]):\n      \
    \          self.depth[v]=T.vertex_depth(i)\n\n        if Mode:\n            return\
    \ self.depth\n\n    def vertex_depth(self,x):\n        \"\"\" \u9802\u70B9 x \u306E\
    \u6DF1\u3055\u3092\u6C42\u3081\u308B.\"\"\"\n\n        assert self.__after_seal_check(x)\n\
    \n        if not hasattr(self,\"depth\"):\n            self.depth_search(Mode=False)\n\
    \        return self.depth[x]\n\n    def dfs_yielder(self):\n        \"\"\" DFS\
    \ \u306B\u304A\u3051\u308B\u9802\u70B9\u306E\u51FA\u5165\u308A\u3092 yield \u3059\
    \u308B.\n\n        (v,1): \u9802\u70B9 v \u306B\u5165\u308B\n        (v,0): \u9802\
    \u70B9 v \u3092\u51FA\u308B\n        (-1,-1): \u305D\u306E\u6728\u3067\u306E yield\
    \ \u304C\u7D42\u4E86\n        \"\"\"\n\n        for k,T in enumerate(self.tree):\n\
    \            v=self.vertex[k]\n            for i,c in T.dfs_yielder():\n     \
    \           yield v[i],c\n            yield -1,-1\n\n    def top_down(self):\n\
    \        \"\"\" \u6728\u306E\u9802\u70B9\u304B\u3089 yield \u3059\u308B.\n   \
    \     \u203B -1 \u3067\u305D\u306E\u6728\u3067\u306E yield \u304C\u7D42\u4E86\n\
    \        \"\"\"\n\n        assert self.__after_seal_check()\n        if not hasattr(self,\"\
    depth\"):\n            self.depth_search(False)\n\n        for k,T in enumerate(self.tree):\n\
    \            v=self.vertex[k]\n            for i in T.top_down():\n          \
    \      yield v[i]\n            yield -1\n\n    def bottom_up(self):\n        \"\
    \"\" \u6728\u306E\u6839\u304B\u3089 yield \u3059\u308B. \"\"\"\n\n        assert\
    \ self.__after_seal_check()\n        if not hasattr(self,\"depth\"):\n       \
    \     self.depth_search(False)\n\n        for k,T in enumerate(self.tree):\n \
    \           v=self.vertex[k]\n            for i in T.bottom_up():\n          \
    \      yield v[i]\n            yield -1\n\n    def is_connect(self, x, y):\n \
    \       \"\"\" \u9802\u70B9 x, y \u304C\u540C\u3058\u9023\u7D50\u6210\u5206\u304B\
    \u3069\u3046\u304B\u3092\u5224\u5B9A\u3059\u308B.\"\"\"\n\n        assert self.__after_seal_check(x,y)\n\
    \        return self.component_id[x]==self.component_id[y]\n\n#=================================================\n\
    def Making_Forest(N, E, root_priority=None, index=0):\n    \"\"\" \u68EE\u3092\
    \u4F5C\u308B.\n\n    N: \u9802\u70B9\u6570\n    E: \u8FBA\u306E\u30EA\u30B9\u30C8\
    \n    root_priority: \u5404\u9023\u7D50\u6210\u5206\u306E\u6839\u306B\u306A\u308A\
    \u3046\u308B\u9802\u70B9\u306E\u512A\u5148\u9806\u4F4D\n    \"\"\"\n\n    if root_priority==None:\n\
    \        root_priority=range(index, index+N)\n\n    from collections import deque\n\
    \    G=[[] for _ in range(index+N)]\n    for u,v in E:\n        assert index<=u<index+N\n\
    \        assert index<=v<index+N\n        assert u!=v\n\n        G[u].append(v)\n\
    \        G[v].append(u)\n\n    X=[-1]*(index+N)\n    S=[0]*(index+N)\n\n    for\
    \ root in root_priority:\n        if X[root]!=-1:\n            continue\n\n  \
    \      Q=deque([root]); S[root]=1\n        while Q:\n            x=Q.popleft()\n\
    \            for y in G[x]:\n                if S[y]==0:\n                   \
    \ X[y]=x\n                    S[y]=1\n                    Q.append(y)\n\n    F=Forest(N,index)\n\
    \    for x in range(index, index+N):\n        if X[x]!=-1:\n            F.parent_set(x,X[x])\n\
    \    F.seal()\n    return F\n\ndef Spanning_Forest(N, E, root_priority=None, index=0,\
    \ exclude=0):\n    \"\"\" \u5168\u57DF\u68EE\u3092\u3064\u304F\u308B.\n\n    N:\
    \ \u9802\u70B9\u6570\n    E:  \u8FBA\u306E\u30EA\u30B9\u30C8\n    root_priority:\
    \ \u5404\u9023\u7D50\u6210\u5206\u306E\u6839\u306B\u306A\u308A\u3046\u308B\u9802\
    \u70B9\u306E\u512A\u5148\u9806\u4F4D\n    exclude: \u5168\u57DF\u68EE\u304B\u3089\
    \u5916\u308C\u305F\u8FBA\u306E\u30EA\u30B9\u30C8\u306E\u51FA\u529B\u65B9\u6CD5\
    \n        0 \u2192 \u306A\u3057\n        1 \u2192 \u9664\u5916\u8FBA\u3092\u51FA\
    \u529B\n        2 \u2192 \u9664\u5916\u8FBA\u3092\u9023\u7D50\u6210\u5206\u6BCE\
    \u306B\u308F\u3051\u308B\n    \"\"\"\n\n    from collections import deque,defaultdict\n\
    \    G=[set() for _ in range(index+N)]\n    M=[]\n    EE=[]\n    for u,v in E:\n\
    \        assert index<=u<index+N\n        assert index<=v<index+N\n\n        if\
    \ (u==v) or (u in G[v]):\n            M.append((u,v))\n            continue\n\n\
    \        G[u].add(v)\n        G[v].add(u)\n        EE.append((u,v))\n\n    X=[-1]*(index+N)\n\
    \    S=[0]*(index+N)\n\n    if root_priority==None:\n        root_priority=range(index,\
    \ index+N)\n\n    for root in root_priority:\n        if X[root]!=-1:\n      \
    \      continue\n\n        Q=deque([root]); S[root]=1\n        while Q:\n    \
    \        x=Q.popleft()\n            for y in G[x]:\n                if S[y]==0:\n\
    \                    X[y]=x\n                    S[y]=1\n                    Q.append(y)\n\
    \n    F=Forest(N,index)\n    for x in range(index, index+N):\n        if X[x]!=-1:\n\
    \            F.parent_set(x,X[x])\n    F.seal()\n\n    if exclude==0:\n      \
    \  return F\n    elif exclude==1:\n        for u,v in EE:\n            if not\
    \ (X[v]==u or X[u]==v):\n                M.append((u,v))\n        return F,M\n\
    \    else:\n        comp=F.component_id\n        L=[[] for _ in range(F.component_number)]\n\
    \n        for u,v in M:\n            k=comp[u]\n            L[k].append((u,v))\n\
    \n        for u,v in EE:\n            if not (X[v]==u or X[u]==v):\n         \
    \       k=comp[u]\n                L[k].append((u,v))\n        return F,L\n"
  dependsOn: []
  isVerificationFile: false
  path: Tree/Forest.py
  requiredBy: []
  timestamp: '2021-09-12 03:06:00+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Tree/Forest.py
layout: document
redirect_from:
- /library/Tree/Forest.py
- /library/Tree/Forest.py.html
title: Tree/Forest.py
---
