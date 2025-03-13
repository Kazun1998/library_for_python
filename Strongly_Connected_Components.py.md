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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.13.2/x64/lib/python3.13/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.13.2/x64/lib/python3.13/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class Strongly_Connected_Components:\n    def __init__(self, N: int):\n \
    \       \"\"\" N \u9802\u70B9\u306E\u6709\u5411\u30B0\u30E9\u30D5\u3092\u751F\u6210\
    \u3059\u308B.\n\n        Args:\n            N (int): \u9802\u70B9\u6570\n    \
    \    \"\"\"\n\n        self.arc: list[list[int]] = [[] for _ in range(N)]\n  \
    \      self.rev: list[list[int]] = [[] for _ in range(N)]\n\n    @property\n \
    \   def N(self):\n        return len(self.arc)\n\n    def add_vertex(self) ->\
    \ int:\n        \"\"\" 1 \u9802\u70B9\u3092\u8FFD\u52A0\u3059\u308B.\n\n     \
    \   Returns:\n            int: \u8FFD\u52A0\u3057\u305F\u9802\u70B9\u306E\u756A\
    \u53F7\n        \"\"\"\n\n        self.arc.append([])\n        self.rev.append([])\n\
    \        return self.N - 1\n\n    def add_vertices(self, k: int = 1) -> list[int]:\n\
    \        \"\"\" \u9802\u70B9\u3092 k \u500B\u8FFD\u52A0\u3059\u308B.\n\n     \
    \   Args:\n            k (int, optional): \u8FFD\u52A0\u3059\u308B\u9802\u70B9\
    \u6570. Defaults to 1.\n\n        Returns:\n            list[int]: \u8FFD\u52A0\
    \u3057\u305F k \u500B\u306E\u9802\u70B9\u306E\u756A\u53F7\n        \"\"\"\n\n\
    \        self.arc.extend([[] for _ in range(k)])\n        self.rev.extend([[]\
    \ for _ in range(k)])\n        return list(range(self.N - k, self.N))\n\n    def\
    \ add_arc(self, source: int, target: int):\n        \"\"\" source \u304B\u3089\
    \ target \u3078\u306E\u5F27\u3092\u7D50\u3076.\n\n        Args:\n            source\
    \ (int): \u5F27\u306E\u59CB\u70B9\n            target (int): \u5F27\u306E\u7D42\
    \u70B9\n        \"\"\"\n\n        self.arc[source].append(target)\n        self.rev[target].append(source)\n\
    \n    def decomposition(self):\n        \"\"\"\u6709\u5411\u30B0\u30E9\u30D5\u3092\
    \u5F37\u9023\u7D50\u6210\u5206\u306B\u5206\u89E3\"\"\"\n\n        group = [0]\
    \ * self.N\n        D = [False] * self.N\n        O = []\n\n        # 1st DFS\n\
    \        for v in range(self.N):\n            if group[v] != 0:\n            \
    \    continue\n\n            stack = [~v, v]\n\n            while stack:\n   \
    \             v = stack.pop()\n                if v >= 0:\n                  \
    \  # in\n                    if group[v] == -1:\n                        continue\n\
    \n                    group[v] = -1\n                    for w in self.arc[v]:\n\
    \                        if not group[w]:\n                            stack.append(~w)\n\
    \                            stack.append(w)\n                else:\n        \
    \            # out\n                    v = ~v\n                    if D[v]:\n\
    \                        continue\n\n                    D[v] = True\n       \
    \             O.append(v)\n\n        components = []\n        # 2nd DFS\n    \
    \    for v in reversed(O):\n            if group[v] != -1:\n                continue\n\
    \n            stack = [v]\n            component = [v]\n            group[v] =\
    \ len(components)\n\n            while stack:\n                w = stack.pop()\n\
    \                for u in self.rev[w]:\n                    if group[u] != -1:\n\
    \                        continue\n\n                    group[u] = len(components)\n\
    \                    component.append(u)\n                    stack.append(u)\n\
    \n            components.append(component)\n\n        self.__components = components\n\
    \        self.__group = group\n\n    @property\n    def components(self) -> list[list[int]]:\n\
    \        return self.__components\n\n    @property\n    def group(self) -> list[int]:\n\
    \        return self.__group\n"
  dependsOn: []
  isVerificationFile: false
  path: Strongly_Connected_Components.py
  requiredBy: []
  timestamp: '2025-03-13 23:53:34+09:00'
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
