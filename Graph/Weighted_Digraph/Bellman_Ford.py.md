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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.13.1/x64/lib/python3.13/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.13.1/x64/lib/python3.13/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from Weighted_Digraph import *\n\ndef Bellman_Fold(D: Weigthed_Digraph, start,\
    \ goal, default = None):\n    N = D.order()\n\n    arcs = []\n    for u in range(N):\n\
    \        arcs.extend([(u, v, w) for v, w, _ in D.adjacent_out[u]])\n\n    inf\
    \ = float('inf')\n    dist = [inf] * N; dist[start] = 0\n\n    for _ in range(N\
    \ - 1):\n        updated = False\n        for u, v, w in arcs:\n            if\
    \ dist[u] + w < dist[v]:\n                dist[v] = dist[u] + w\n            \
    \    updated = True\n\n        if not updated:\n            break\n\n    # \u8CA0\
    \u9589\u8DEF\u691C\u51FA\n    for _ in range(N):\n        updated = False\n  \
    \      for u, v, w in arcs:\n            if dist[u] + w < dist[v]:\n         \
    \       dist[v] = -inf\n                updated = True\n\n        if not updated:\n\
    \            break\n\n    return dist[goal]\n"
  dependsOn: []
  isVerificationFile: false
  path: Graph/Weighted_Digraph/Bellman_Ford.py
  requiredBy: []
  timestamp: '2024-02-25 11:27:32+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Graph/Weighted_Digraph/Bellman_Ford.py
layout: document
redirect_from:
- /library/Graph/Weighted_Digraph/Bellman_Ford.py
- /library/Graph/Weighted_Digraph/Bellman_Ford.py.html
title: Graph/Weighted_Digraph/Bellman_Ford.py
---
