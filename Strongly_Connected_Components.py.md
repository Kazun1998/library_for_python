---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test_verify/yosupo_library_checker/Graph/Strongly_Connected_Components-class.test.py
    title: test_verify/yosupo_library_checker/Graph/Strongly_Connected_Components-class.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.3/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.3/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class Strongly_Connected_Components:\n    def __init__(self, N):\n      \
    \  \"\"\" N \u9802\u70B9\u306E\u6709\u5411\u30B0\u30E9\u30D5\u3092\u751F\u6210\
    \u3059\u308B. \"\"\"\n        self.N=N\n        self.arc=[[] for _ in range(N)]\n\
    \        self.rev=[[] for _ in range(N)]\n\n    def add_vertex(self):\n      \
    \  \"\"\" \u9802\u70B9\u3092\u8FFD\u52A0\u3059\u308B.\n\n        \"\"\"\n\n  \
    \      self.N+=1\n        self.arc.append([])\n        self.rev.append([])\n \
    \       return self.N-1\n\n    def add_vertices(self, k=1):\n        \"\"\" \u9802\
    \u70B9\u3092 k \u500B\u8FFD\u52A0\u3059\u308B.\n\n        k: int\n        \"\"\
    \"\n\n        self.N+=k\n        self.arc.extend([[] for _ in range(k)])\n   \
    \     self.rev.extend([[] for _ in range(k)])\n        return list(range(self.N-k,\
    \ self.N))\n\n    def add_arc(self, source, target):\n        \"\"\" source \u304B\
    \u3089 target \u3078\u7D50\u3076\u6709\u5411\u8FBA\u3092\u8FFD\u52A0\u3059\u308B\
    .\n\n        \"\"\"\n\n        self.arc[source].append(target)\n        self.rev[target].append(source)\n\
    \n    def decomposition(self, mode=0):\n        \"\"\"\u6709\u5411\u30B0\u30E9\
    \u30D5\u3092\u5F37\u9023\u7D50\u6210\u5206\u306B\u5206\u89E3\n\n        Mode:\n\
    \        0 (defalt) ---\u5404\u5F37\u9023\u7D50\u6210\u5206\u306E\u9802\u70B9\u306E\
    \u30EA\u30B9\u30C8\n        1        ---\u5404\u9802\u70B9\u304C\u5C5E\u3057\u3066\
    \u3044\u308B\u5F37\u9023\u7D50\u6210\u5206\u306E\u756A\u53F7\n        2      \
    \  ---0, 1 \u306E\u4E21\u65B9\n\n        \u203B 0 or 2\u3067\u5E30\u3063\u3066\
    \u304F\u308B\u30EA\u30B9\u30C8\u306F\u5404\u5F37\u9023\u7D50\u6210\u5206\u306B\
    \u95A2\u3057\u3066\u30C8\u30DD\u30ED\u30B8\u30AB\u30EB\u30BD\u30FC\u30C8\u3067\
    \u3042\u308B.\n        \"\"\"\n\n        G=[0]*self.N\n        D=[0]*self.N\n\
    \        O=[]\n\n        for v in range(self.N):\n            if G[v]:\n     \
    \           continue\n\n            S=[~v, v]\n\n            while S:\n      \
    \          v=S.pop()\n                if v>=0:\n                    if G[v]==-1:\n\
    \                        continue\n\n                    G[v]=-1\n           \
    \         for w in self.arc[v]:\n                        if not G[w]:\n      \
    \                      S.append(~w)\n                            S.append(w)\n\
    \                else:\n                    v=~v\n                    if not D[v]:\n\
    \                        D[v]=1\n                        O.append(v)\n\n     \
    \   K=0\n        for v in reversed(O):\n            if G[v]!=-1:\n           \
    \     continue\n\n            S=[v]\n            G[v]=K\n\n            while S:\n\
    \                w=S.pop()\n                for u in self.rev[w]:\n          \
    \          if G[u]==-1:\n                        G[u]=K\n                    \
    \    S.append(u)\n            K+=1\n\n        if mode==0 or mode==2:\n       \
    \     R=[[] for _ in range(K)]\n            for i in range(self.N):\n        \
    \        R[G[i]].append(i)\n\n        if mode==0:\n            return R\n    \
    \    elif mode==1:\n            return G\n        else:\n            return R,G\n"
  dependsOn: []
  isVerificationFile: false
  path: Strongly_Connected_Components.py
  requiredBy: []
  timestamp: '2023-01-08 21:36:08+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test_verify/yosupo_library_checker/Graph/Strongly_Connected_Components-class.test.py
documentation_of: Strongly_Connected_Components.py
layout: document
title: "Strongly Connected Components (\u5F37\u9023\u7D50\u6210\u5206\u5206\u89E3)"
---

## Outline

有向グラフにおける強連結成分分解を行う.

## Theory

$D=(V,A)$ を有向グラフとする.

$V$ 上の関係 $\sim$ を次のように定義する.

* $u \sim v :\iff$ $u$ から $v$ への有向路, $v$ から $u$ への有向路が共に存在する.

この関係 $\sim$ は同値関係になる. この  $\sim$ に関する連結成分を **強連結成分** という.

そして, $A'$ を

$$A':=\left \{\overrightarrow{[u][v]}\middle| \overrightarrow{uv} \in A , [u] \neq [v] \right \}$$

と定義すると, $D'=(V/\sim, A')$ は DAG になる. よって, $D'$ には Topological Sort $\geq$ が存在する.

このアルゴリズムでは強連結成分をトポロジカルソートの順に求めることができる.
