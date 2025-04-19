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
  code: "from Digraph import *\n\ndef Find_Directed_Eulerian_Trail(D: Digraph):\n\
    \    N = D.order()\n\n    remain = [D.out_degree(v) for v in range(N)]\n\n   \
    \ start = goal = -1\n    necessary = True\n    # \u5FC5\u8981\u6761\u4EF6\u30C1\
    \u30A7\u30C3\u30AF\n    for v in range(N):\n        out_deg = D.out_degree(v)\n\
    \        in_deg = D.in_degree(v)\n\n        if abs(out_deg - in_deg) >= 2:\n \
    \           necessary = False\n        elif out_deg - in_deg == 1:\n         \
    \   if start == -1:\n                start = v\n            else:\n          \
    \      necessary = False\n        if out_deg - in_deg == -1:\n            goal\
    \ = v\n\n    if not necessary:\n        return { 'vertex': None, 'arc': None }\n\
    \n    if start == -1:\n        for v in range(N):\n            if D.out_degree(v):\n\
    \                start = goal = v\n                break\n        else:\n    \
    \        start = goal = 0\n\n    adj_out = [[arc for arc in D.adjacent_out[x]]\
    \ for x in range(N)]\n\n    def dfs(start):\n        path = []\n\n        x =\
    \ start\n        while True:\n            if not adj_out[x]:\n               \
    \ break\n\n            y, i = adj_out[x].pop()\n            path.append((x, y,\
    \ i))\n            remain[x] -= 1\n            x = y\n        return path\n\n\
    \    stack = dfs(start)\n    arc = []\n    vertex = [goal]\n    while stack:\n\
    \        u, _, j = stack.pop()\n        vertex.append(u)\n        arc.append(j)\n\
    \n        if remain[u]:\n            stack.extend(dfs(u))\n\n    if len(arc) ==\
    \ D.size():\n        vertex.reverse()\n        arc.reverse()\n        return {\
    \ 'vertex': vertex, 'arc': arc }\n    else:\n        return { 'vertex': None,\
    \ 'arc': None }\n"
  dependsOn: []
  isVerificationFile: false
  path: Graph/Digraph/Eulerian.py
  requiredBy: []
  timestamp: '2025-01-04 19:25:49+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Graph/Digraph/Eulerian.py
layout: document
redirect_from:
- /library/Graph/Digraph/Eulerian.py
- /library/Graph/Digraph/Eulerian.py.html
title: Graph/Digraph/Eulerian.py
---
