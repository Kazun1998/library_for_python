---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test_verify/yosupo_library_checker/Graph/Undirected_Find_Cycle.test.py
    title: test_verify/yosupo_library_checker/Graph/Undirected_Find_Cycle.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.13.3/x64/lib/python3.13/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.13.3/x64/lib/python3.13/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from Graph import *\n\n# Cycle\u304C\u5B58\u5728\u3059\u308B?\ndef Is_Exist_Cycle(G:\
    \ Graph):\n    return G.order() < G.size() + Connected_Component_Number(G)\n\n\
    def Find_Cycle(G: Graph):\n    N = G.order()\n\n    seen = [False] * N\n    parent\
    \ = [-1] * N\n    upper = [-1] * N\n    def dfs(start):\n        seen[start] =\
    \ True\n        stack = [(start, v, j) for v, j in G.partner_with_label_yield(start)]\n\
    \        while stack:\n            u, v, j = stack.pop()\n\n            if seen[v]:\n\
    \                vertex = [v, u]\n                edge = [j]\n               \
    \ while u != v:\n                    edge.append(upper[u])\n                 \
    \   u = parent[u]\n                    vertex.append(u)\n                return\
    \ vertex, edge\n\n            seen[v] = True\n            parent[v] = u\n    \
    \        upper[v] = j\n\n            stack.extend([(v, w, k) for w, k in G.partner_with_label_yield(v)\
    \ if k != j])\n        return None, None\n\n    for x in range(N):\n        if\
    \ not seen[x]:\n            vertex, edge = dfs(x)\n            if vertex is not\
    \ None:\n                return { 'vertex': vertex, 'edge': edge }\n    else:\n\
    \        return { 'vertex': None, 'edge': None }\n"
  dependsOn: []
  isVerificationFile: false
  path: Graph/Graph/Cycle.py
  requiredBy: []
  timestamp: '2024-03-20 20:29:17+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test_verify/yosupo_library_checker/Graph/Undirected_Find_Cycle.test.py
documentation_of: Graph/Graph/Cycle.py
layout: document
redirect_from:
- /library/Graph/Graph/Cycle.py
- /library/Graph/Graph/Cycle.py.html
title: Graph/Graph/Cycle.py
---
