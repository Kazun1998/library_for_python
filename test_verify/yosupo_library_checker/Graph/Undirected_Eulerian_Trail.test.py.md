---
data:
  _extendedDependsOn:
  - icon: ':x:'
    path: Graph/Graph/Eulerian.py
    title: Graph/Graph/Eulerian.py
  - icon: ':x:'
    path: Graph/Graph/Graph.py
    title: Graph
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/eulerian_trail_undirected
    links:
    - https://judge.yosupo.jp/problem/eulerian_trail_undirected
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.2/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.2/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/eulerian_trail_undirected\n\
    \n#==================================================\nfrom Graph.Graph.Graph\
    \ import Graph as Undirected_Graph\nfrom Graph.Graph.Eulerian import *\n\nimport\
    \ sys\ninput=sys.stdin.readline\nwrite=sys.stdout.write\n\n#==================================================\n\
    def verify():\n    N, M = map(int, input().split())\n\n    G = Undirected_Graph(N)\n\
    \    for j in range(M):\n        u, v = map(int, input().split())\n        G.add_edge(u,\
    \ v, j)\n\n    euler = Find_Eulerian_Trail(G)\n    if euler['vertex'] is None:\n\
    \        print(\"No\")\n    else:\n        print('Yes')\n        print(*euler['vertex'])\n\
    \        print(*euler['edge'])\n\n#==================================================\n\
    T = int(input())\nfor _ in range(T):\n    verify()\n"
  dependsOn:
  - Graph/Graph/Graph.py
  - Graph/Graph/Eulerian.py
  isVerificationFile: true
  path: test_verify/yosupo_library_checker/Graph/Undirected_Eulerian_Trail.test.py
  requiredBy: []
  timestamp: '2024-03-20 22:23:03+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: test_verify/yosupo_library_checker/Graph/Undirected_Eulerian_Trail.test.py
layout: document
redirect_from:
- /verify/test_verify/yosupo_library_checker/Graph/Undirected_Eulerian_Trail.test.py
- /verify/test_verify/yosupo_library_checker/Graph/Undirected_Eulerian_Trail.test.py.html
title: test_verify/yosupo_library_checker/Graph/Undirected_Eulerian_Trail.test.py
---
