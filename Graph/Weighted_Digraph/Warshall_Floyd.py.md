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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.13.5/x64/lib/python3.13/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.13.5/x64/lib/python3.13/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from Weighted_Digraph import *\n\ndef Warshall_Floyd(D: Weigthed_Digraph):\n\
    \    \"\"\" Warshall-Floyd \u6CD5\u3092\u7528\u3044\u3066, \u5168\u70B9\u9593\u8DDD\
    \u96E2\u3092\u6C42\u3081\u308B.\n\n    D: \u91CD\u307F\u4ED8\u304D\u6709\u5411\
    \u30B0\u30E9\u30D5\n    \"\"\"\n\n    N = D.order()\n    inf = float('inf')\n\n\
    \    dist = [[0 if u == v else inf for v in range(N)] for u in range(N)]\n\n \
    \   def three_loop():\n        for r in range(N):\n            dist_r = dist[r]\n\
    \            for p in range(N):\n                dist_p = dist[p]\n          \
    \      for q in range(N):\n                    dist_p[q] = min(dist_p[q], dist_p[r]\
    \ + dist_r[q])\n\n    for u in range(N):\n        dist_u = dist[u]\n        for\
    \ v, w, _ in D.adjacent_out[u]:\n            dist_u[v] = min(dist_u[v], w)\n\n\
    \    three_loop()\n\n    if any(dist[u][u] < 0 for u in range(N)):\n        for\
    \ u in [u for u in range(N) if dist[u][u] < 0]:\n            dist[u][u] = -inf\n\
    \        three_loop()\n\n    return dist"
  dependsOn: []
  isVerificationFile: false
  path: Graph/Weighted_Digraph/Warshall_Floyd.py
  requiredBy: []
  timestamp: '2024-02-25 11:56:41+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Graph/Weighted_Digraph/Warshall_Floyd.py
layout: document
redirect_from:
- /library/Graph/Weighted_Digraph/Warshall_Floyd.py
- /library/Graph/Weighted_Digraph/Warshall_Floyd.py.html
title: Graph/Weighted_Digraph/Warshall_Floyd.py
---
