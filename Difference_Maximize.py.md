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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.13.3/x64/lib/python3.13/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.13.3/x64/lib/python3.13/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "\"\"\"\nNote\n\u901A\u79F0 \"\u725B\u30B2\u30FC\" \u3068\u547C\u3070\u308C\
    \u308B\u554F\u984C\u3092\u89E3\u304F. \u3053\u306E\u554F\u984C\u306F M \u500B\u306E\
    \u6761\u4EF6\n    x[i[m]]-x[j[m]]<=c[m]\n\u306B\u304A\u3044\u3066, x[p]-x[q] \u3092\
    \u6700\u5927\u5316\u3059\u308B. \u306A\u304A, \u3053\u308C\u306F x[q]=0 \u3068\
    \u3044\u3046\u8FFD\u52A0\u5236\u7D04\u5316\u3067\u306E x[p] \u306E\u6700\u5927\
    \u5316\u306B\u306A\u308B.\n\n\u203B \u6700\u77ED\u8DEF\u554F\u984C\u306B\u5E30\
    \u7740\n\"\"\"\n\nclass Difference_Maximize:\n    def __init__(self, n: int):\n\
    \        self.__n = n\n        self.__arcs = [[] for _ in range(n)]\n        self.__has_negative_arc\
    \ = False\n\n    @property\n    def n(self) -> int:\n        return self.__n\n\
    \n    @property\n    def has_negative_arc(self) -> bool:\n        return self.__has_negative_arc\n\
    \n    def __topological_sort(self) -> list[int]:\n        topological_sort = []\n\
    \        in_deg = [0] * self.n\n\n        for s in range(self.n):\n          \
    \  for t, _ in self.__arcs[s]:\n                in_deg[t] += 1\n\n        stack\
    \ = [v for v in range(self.n) if in_deg[v] == 0]\n        while stack:\n     \
    \       x = stack.pop()\n            topological_sort.append(x)\n\n          \
    \  for y, _ in self.__arcs[x]:\n                in_deg[y] -= 1\n             \
    \   if in_deg[y] == 0:\n                    stack.append(y)\n\n        if len(topological_sort)\
    \ == self.n:\n            return topological_sort\n        else:\n           \
    \ return None\n\n    def inequality_constraint(self, i: int, j: int, c: int):\n\
    \        \"\"\" \u4E0D\u7B49\u5F0F\u6761\u4EF6 X[i] - X[j] <= c \u3092\u8FFD\u52A0\
    \u3059\u308B.\n\n        Args:\n            i (int):\n            j (int):\n \
    \           c (int):\n        \"\"\"\n\n        assert 0 <= i < self.n\n     \
    \   assert 0 <= j < self.n\n\n        if c < 0:\n            self.__has_negative_arc\
    \ = True\n\n        self.__arcs[j].append((i, c))\n\n    def equality_constraint(self,\
    \ i: int, j: int, c: int):\n        \"\"\" \u4E0D\u7B49\u5F0F\u6761\u4EF6 X[i]\
    \ - X[j] = c \u3092\u8FFD\u52A0\u3059\u308B.\n\n        Args:\n            i (int):\n\
    \            j (int):\n            c (int):\n        \"\"\"\n\n        self.inequality_constraint(i,\
    \ j, c)\n        self.inequality_constraint(j, i, -c)\n\n    def solve(self, s:\
    \ int) -> list[int]:\n        if (topological_sort := self.__topological_sort())\
    \ is None:\n            return self.solve_by_dp_on_dag(s, topological_sort)\n\
    \        elif self.has_negative_arc:\n            return self.solve_by_bellman_ford(s)\n\
    \        else:\n            return self.solve_by_dijkstra(s)\n\n    def solve_by_dp_on_dag(self,\
    \ s: int, topological_sort: list[int]) -> list[int]:\n        inf = float(\"inf\"\
    )\n        dist = [inf] * self.n; dist[s] = 0\n        for x in topological_sort:\n\
    \            for y, w in self.__arcs[x]:\n                dist[y] = min(dist[y],\
    \ dist[x] + w)\n        return dist\n\n    def solve_by_bellman_ford(self, s:\
    \ int) -> list[int]:\n        inf = float(\"inf\")\n        dist = [inf] * self.n\n\
    \        dist[s] = 0\n\n        def update(negative_cycle = False):\n        \
    \    updated = False\n            for p in range(self.n):\n                for\
    \ q, c in self.__arcs[p]:\n                    if dist[q] > dist[p] + c:\n   \
    \                     if negative_cycle:\n                            dist[q]\
    \ = -inf\n                        else:\n                            dist[q] =\
    \ dist[p] + c\n                        updated = True\n            return updated\n\
    \n        for _ in range(self.n):\n            if not update():\n            \
    \    return dist\n\n        for _ in range(self.n):\n            if not update(True):\n\
    \                return dist\n\n    def solve_by_dijkstra(self, s: int) -> list[int]:\n\
    \        from heapq import heappush, heappop\n\n        inf = float(\"inf\")\n\
    \        dist = [inf] * self.n\n        dist[s] = 0\n        Q = [(0, s)]\n  \
    \      while Q:\n            d, x = heappop(Q)\n            if d > dist[x]:\n\
    \                continue\n\n            for y, c in self.__arcs[x]:\n       \
    \         if dist[y] > dist[x] + c:\n                    dist[y] = dist[x] + c\n\
    \                    heappush(Q, (dist[y], y))\n        return dist\n"
  dependsOn: []
  isVerificationFile: false
  path: Difference_Maximize.py
  requiredBy: []
  timestamp: '2025-05-04 16:00:50+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Difference_Maximize.py
layout: document
redirect_from:
- /library/Difference_Maximize.py
- /library/Difference_Maximize.py.html
title: Difference_Maximize.py
---
