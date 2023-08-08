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
  code: "from Min_Cost_Flow import *\n\nclass Bipartite_Weighted_Matching:\n    inf=float(\"\
    inf\")\n    def __init__(self, M, N):\n        \"\"\"\n\n        \"\"\"\n    \
    \    self.M=M; self.N=N\n        self.__max_weight=-Bipartite_Weighted_Matching.inf\n\
    \        self.edge=[[] for _ in range(M)]\n\n    def add_vertex(self, side, k=1):\n\
    \        \"\"\" side \u5074\u306B k \u500B\u306E\u9802\u70B9\u3092\u8FFD\u52A0\
    \u3059\u308B.\n\n        side: 0 or 1, 0 \u306E\u3068\u304D\u306F A \u5074, 1\
    \ \u306E\u6642\u306F B \u5074\n        \"\"\"\n\n        if side==0:\n       \
    \     self.M+=k\n            self.edge.extend([[] for _ in range(k)])\n      \
    \      return list(range(self.M-k, self.M))\n        else:\n            self.N+=k\n\
    \            return list(range(self.N-k, self.N))\n\n    def add_edge(self, a,\
    \ b, w):\n        \"\"\" \u91CD\u3055 w \u306E \u8FBA Aa Bb \u3092\u52A0\u3048\
    \u308B.\n\n        \"\"\"\n\n        assert 0<=a<self.M and 0<=b<self.N\n\n  \
    \      self.__max_weight=max(self.__max_weight, w)\n        self.edge[a].append((b,w))\n\
    \n    def matching(self, mode=False):\n        \"\"\" \u666E\u901A\u306E\u6700\
    \u5927\u91CD\u307F\u30DE\u30C3\u30C1\u30F3\u30B0\u3092\u6C42\u3081\u308B.\n\n\
    \        \"\"\"\n\n        if mode==0:\n            return self.matching_vertex_duplicate([1]*self.M,\
    \ [1]*self.N)\n        else:\n            weight,(X,Y)=self.matching_vertex_duplicate([1]*self.M,\
    \ [1]*self.N,1)\n            X=[x[0] if x else -1 for x in X]\n            Y=[y[0]\
    \ if y else -1 for y in Y]\n            return weight,(X,Y)\n\n    def matching_specify_size(self,\
    \ size, default=None):\n        return self.matching_vertex_duplicate([1]*self.M,\
    \ [1]*self.N, size, default)\n\n    def matching_each_size(self):\n        \"\"\
    \" \u666E\u901A\u306E\u6700\u5927\u91CD\u307F\u30DE\u30C3\u30C1\u30F3\u30B0\u3092\
    \u6C42\u3081\u308B.\n\n        \"\"\"\n\n        M=self.M; N=self.N\n        G=Max_Gain_Flow(M+N+2)\n\
    \        source=M+N; target=M+N+1\n\n        for a in range(M):\n            G.add_arc(source,\
    \ a, 1, 0)\n\n        for b in range(N):\n            G.add_arc(b+M, target, 1,\
    \ 0)\n\n        for a in range(M):\n            for b,w in self.edge[a]:\n   \
    \             G.add_arc(a, b+M, 1, w)\n\n        return G.slope(source, target,\
    \ min(M,N))\n\n    def matching_vertex_duplicate(self, k, l, mode=0):\n      \
    \  \"\"\" \u9802\u70B9 Aa \u306E\u9078\u629E\u3092 k[a] \u56DE, \u9802\u70B9 Bb\
    \ \u306E\u9078\u629E\u3092 l[b] \u56DE\u307E\u3067\u8A31\u3059\u6700\u5927\u30DE\
    \u30C3\u30C1\u30F3\u30B0\u3092\u9078\u3076.\n\n        \"\"\"\n\n        M=self.M;\
    \ N=self.N\n        G=Max_Gain_Flow(M+N+2)\n        source=M+N; target=M+N+1\n\
    \n        flow=min(sum(k), sum(l))\n\n        G.add_arc(source, target, flow,\
    \ 0)\n        for a in range(M):\n            G.add_arc(source, a, k[a], 0)\n\n\
    \        for b in range(N):\n            G.add_arc(b+M, target, l[b], 0)\n\n \
    \       for a in range(M):\n            for b,w in self.edge[a]:\n           \
    \     G.add_arc(a, b+M, 1, w)\n\n        gain=G.flow(source, target, flow)\n\n\
    \        if not mode:\n            return gain\n\n        X=[[] for _ in range(M)];\
    \ Y=[[] for _ in range(N)]\n        for i in range(G.arc_count()):\n         \
    \   arc=G.get_arc(i)\n            if arc.source!=source and arc.target!=target:\n\
    \                if arc.cap==0:\n                    a=arc.source; b=arc.target-M\n\
    \                    X[a].append(b)\n                    Y[b].append(a)\n    \
    \    return gain,(X,Y)\n\n    def matching_vertex_duplicate_specify_size(self,\
    \ k, l, size, default=None):\n        try:\n            return self.matching_vertex_duplicate_each_size(k,l)[size]\n\
    \        except:\n            return default\n\n    def matching_vertex_duplicate_each_size(self,\
    \ k, l):\n        \"\"\" \u9802\u70B9 Aa \u306E\u9078\u629E\u3092 k[a] \u56DE\
    , \u9802\u70B9 Bb \u306E\u9078\u629E\u3092 l[b] \u56DE\u307E\u3067\u8A31\u3059\
    \u6700\u5927\u30DE\u30C3\u30C1\u30F3\u30B0\u3092\u9078\u3076.\n\n        \"\"\"\
    \n\n        M=self.M; N=self.N\n        G=Max_Gain_Flow(M+N+2)\n        source=M+N;\
    \ target=M+N+1\n\n        flow=min(sum(k), sum(l))\n\n        for a in range(M):\n\
    \            G.add_arc(source, a, k[a], 0)\n\n        for b in range(N):\n   \
    \         G.add_arc(b+M, target, l[b], 0)\n\n        for a in range(M):\n    \
    \        for b,w in self.edge[a]:\n                G.add_arc(a, b+M, 1, w)\n\n\
    \        return G.slope(source, target)\n"
  dependsOn: []
  isVerificationFile: false
  path: Min_Cost_Flow/Bipartite_Weighted_Matching.py
  requiredBy: []
  timestamp: '2022-04-20 14:59:12+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Min_Cost_Flow/Bipartite_Weighted_Matching.py
layout: document
title: Bipartite Weighted Matching
---

## Outline

二部グラフ $G=(X,Y,E)$ における最大重みマッチング問題 (及びそれらの派生問題) を解く.

## Theory

二部グラフ $G=(X,Y,E)$ における最大重みマッチング問題は次のようにして多項式時間で解くことが出来る.

* $G$ に対して, 次のような有向グラフを $H=(V,A)$ 作成する.
  * $V=X \coprod Y \coprod \\{s,t\\}$
  * $A=\\{\overrightarrow{xy} \mid xy \in E\\} \coprod \\{\overrightarrow{sx} \mid x \in X\\} \coprod \\{\overrightarrow{yt} \mid x \in X\\}$
  * 各孤の容量は全て $1$ とし,　単位あたりの費用 $c(a)$ は次のようにする.
    * $xy \in E$ のとき, $c(\overrightarrow{xy})$ は辺 $xy$ の重みとする.
    * $c(\overrightarrow{sx})=c(\overrightarrow{yt})=0$
