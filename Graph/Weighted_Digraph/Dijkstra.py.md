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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.3/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.3/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from Weighted_Digraph import *\n\ndef Dijkstra(D: Weigthed_Digraph, start,\
    \ goal, default = None):\n    from heapq import heappush, heappop\n\n    inf =\
    \ float('inf')\n    dist = [inf] * D.order(); dist[start] = 0\n    fix = [False]\
    \ * D.order()\n    parent = [None] * D.order()\n    upper = [None] * D.order()\n\
    \n    Q = [(0, start)]\n    while Q:\n        d, x = heappop(Q)\n        if fix[x]:\n\
    \            continue\n\n        fix[x] = True\n        if x == goal:\n      \
    \      break\n\n        for y, w, id in D.adjacent_out[x]:\n            if d +\
    \ w < dist[y]:\n                dist[y] = d + w\n                parent[y] = x\n\
    \                upper[y] = id\n                heappush(Q, (dist[y], y))\n\n\
    \    if dist[goal] == inf:\n        return {'dist': default, 'arc': None, 'vertex':\
    \ None}\n\n    vertex = [goal]\n    arc = []\n    x = goal\n    while x != start:\n\
    \        arc.append(upper[x])\n        x = parent[x]\n        vertex.append(x)\n\
    \n    return {'dist': dist[goal], 'arc': arc[::-1], 'vertex': vertex[::-1]}\n"
  dependsOn: []
  isVerificationFile: false
  path: Graph/Weighted_Digraph/Dijkstra.py
  requiredBy: []
  timestamp: '2024-02-25 11:08:29+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Graph/Weighted_Digraph/Dijkstra.py
layout: document
redirect_from:
- /library/Graph/Weighted_Digraph/Dijkstra.py
- /library/Graph/Weighted_Digraph/Dijkstra.py.html
title: Graph/Weighted_Digraph/Dijkstra.py
---
