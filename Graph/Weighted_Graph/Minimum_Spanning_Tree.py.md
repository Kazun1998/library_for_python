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
  code: "from Weighted_Graph import Weigthed_Graph\n\n# \u6700\u5C0F\u5168\u57DF\u6728\
    \u3092\u30AF\u30E9\u30B7\u30AB\u30EB\u6CD5\u3067\u6C42\u3081\u308B.\ndef Minimum_Spanning_Tree_by_Kruskal(G:\
    \ Weigthed_Graph):\n    \"\"\" \u30B0\u30E9\u30D5 G \u306E\u6700\u5C0F\u5168\u57DF\
    \u6728\u3092\u30AF\u30E9\u30B7\u30AB\u30EB\u6CD5\u3067\u6C42\u3081\u308B.\n\n\
    \    G: \u30B0\u30E9\u30D5\n    \"\"\"\n\n    N = G.order()\n\n    #Union-Find\u3092\
    \u5B9A\u7FA9\u3059\u308B.\n    UF = list(range(N))\n    depth = [0] * N\n\n  \
    \  def find(x):\n        y = x\n        while UF[y] != y:\n            y = UF[y]\n\
    \n        while UF[x] != y:\n            x, UF[x] = UF[x], y\n\n        return\
    \ y\n\n    def union(x, y):\n        x = find(x)\n        y = find(y)\n\n    \
    \    if x == y:\n            return False\n\n        if depth[x] > depth[y]:\n\
    \            UF[y] = x\n        else:\n            UF[x] = y\n            if depth[x]\
    \ == depth[y]:\n                depth[y] += 1\n        return True\n\n    k =\
    \ G.edge_offset + G.size()\n\n    u = [0] * k\n    v = [0] * k\n    w = [0] *\
    \ k\n    for x, y, z, id in G.edge_yielder():\n        u[id] = x\n        v[id]\
    \ = y\n        w[id] = z\n\n    edges = []\n    remain = N - 1\n\n    for id in\
    \ sorted(range(G.edge_offset, k), key = lambda id: w[id]):\n        if not union(u[id],\
    \ v[id]):\n            continue\n\n        edges.append(id)\n        remain -=\
    \ 1\n\n        if remain == 0:\n            continue\n\n    return { 'weight':\
    \ sum(w[id] for id in edges), 'edges': edges }\n\n# \u6700\u5C0F\u5168\u57DF\u6728\
    \u3092\u30D7\u30EA\u30E0\u6CD5\u3067\u6C42\u3081\u308B.\ndef Minimum_Spanning_Tree_by_Prim(G:\
    \ Weigthed_Graph):\n    \"\"\" \u30B0\u30E9\u30D5 G \u306E\u6700\u5C0F\u5168\u57DF\
    \u6728\u3092\u30D7\u30EA\u30E0\u6CD5\u3067\u6C42\u3081\u308B.\n    \"\"\"\n  \
    \  from heapq import heapify, heappop, heappush\n    N = G.vertex_count()\n\n\
    \    used = [0] * N; used[0] = 1\n    Q = [(w, 0, y, id) for y, w, id in G.adjacent[0]]\n\
    \    heapify(Q)\n\n    weight = 0\n    remain = N - 1\n    edges = []\n\n    while\
    \ remain:\n        c, _, b, id = heappop(Q)\n\n        if used[b]:\n         \
    \   continue\n\n        remain -= 1\n        weight += c\n        edges.append(id)\n\
    \n        used[b] = 1\n        for v, w, id in G.adjacent[b]:\n            if\
    \ not used[v]:\n                heappush(Q, (w, b, v, id))\n\n    return { 'weight':\
    \ weight, 'edges': edges }\n"
  dependsOn: []
  isVerificationFile: false
  path: Graph/Weighted_Graph/Minimum_Spanning_Tree.py
  requiredBy: []
  timestamp: '2024-03-03 01:24:05+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Graph/Weighted_Graph/Minimum_Spanning_Tree.py
layout: document
redirect_from:
- /library/Graph/Weighted_Graph/Minimum_Spanning_Tree.py
- /library/Graph/Weighted_Graph/Minimum_Spanning_Tree.py.html
title: Graph/Weighted_Graph/Minimum_Spanning_Tree.py
---
