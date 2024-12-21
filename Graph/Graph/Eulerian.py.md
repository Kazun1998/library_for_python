---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test_verify/yosupo_library_checker/Graph/Undirected_Eulerian_Trail.test.py
    title: test_verify/yosupo_library_checker/Graph/Undirected_Eulerian_Trail.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.8/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.8/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from Graph import *\n\n#\u30AA\u30A4\u30E9\u30FC\u30B0\u30E9\u30D5?\ndef\
    \ Is_Eulerian_Graph(G: Graph):\n    \"\"\" \u30B0\u30E9\u30D5 G \u304C\u30AA\u30A4\
    \u30E9\u30FC\u30B0\u30E9\u30D5\u304B\u3069\u3046\u304B\u3092\u5224\u5B9A\u3059\
    \u308B. \"\"\"\n    return all(G.degree(v) % 2 == 0 for v in range(G.order()))\
    \ and Is_Connected(G)\n\n#\u6E96\u30AA\u30A4\u30E9\u30FC\u30B0\u30E9\u30D5?\n\
    def Is_Semi_Eulerian_Graph(G: Graph):\n    \"\"\" \u30B0\u30E9\u30D5 G \u304C\u6E96\
    \u30AA\u30A4\u30E9\u30FC\u30B0\u30E9\u30D5\u304B\u3069\u3046\u304B\u3092\u5224\
    \u5B9A\u3059\u308B. \"\"\"\n    return len([v for v in range(G.order()) if G.degree(v)\
    \ % 2 == 0]) == 2 and Is_Connected(G)\n\n#Euler (\u9589) \u8DEF\u3092\u898B\u3064\
    \u3051\u308B\ndef Find_Eulerian_Trail(G: Graph):\n    N = G.order()\n\n    remain\
    \ = [G.degree(v) for v in range(N)]\n\n    odd_vertex = [v for v in range(N) if\
    \ remain[v] % 2 == 1]\n    if len(odd_vertex) > 2:\n        return { 'vertex':\
    \ None, 'edge': None }\n    elif len(odd_vertex) == 2:\n        start, goal =\
    \ odd_vertex\n    else:\n        for v in range(N):\n            if remain[v]:\n\
    \                start = goal = v\n                break\n        else:\n    \
    \        start = goal = 0\n\n    adj = [[edge for edge in G.adjacent[x]] for x\
    \ in range(N)]\n    seen = set()\n\n    def dfs(start):\n        path = []\n\n\
    \        x = start\n        while True:\n            if not adj[x]:\n        \
    \        break\n\n            y, i = adj[x].pop()\n            if i in seen:\n\
    \                continue\n\n            seen.add(i)\n            path.append((x,\
    \ y, i))\n            remain[x] -= 1; remain[y] -= 1\n            x = y\n    \
    \    return path\n\n    stack = dfs(start)\n    edge = []\n    vertex = [goal]\n\
    \    while stack:\n        u, _, j = stack.pop()\n        vertex.append(u)\n \
    \       edge.append(j)\n\n        if remain[u]:\n            stack.extend(dfs(u))\n\
    \n    if len(edge) == G.size():\n        return { 'vertex': vertex, 'edge': edge\
    \ }\n    else:\n        return { 'vertex': None, 'edge': None }\n"
  dependsOn: []
  isVerificationFile: false
  path: Graph/Graph/Eulerian.py
  requiredBy: []
  timestamp: '2024-03-20 23:15:33+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test_verify/yosupo_library_checker/Graph/Undirected_Eulerian_Trail.test.py
documentation_of: Graph/Graph/Eulerian.py
layout: document
redirect_from:
- /library/Graph/Graph/Eulerian.py
- /library/Graph/Graph/Eulerian.py.html
title: Graph/Graph/Eulerian.py
---
