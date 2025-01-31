---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Graph/Graph/Cycle.py
    title: Graph/Graph/Cycle.py
  - icon: ':heavy_check_mark:'
    path: Graph/Graph/Graph.py
    title: Graph
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/cycle_detection_undirected
    links:
    - https://judge.yosupo.jp/problem/cycle_detection_undirected
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.13.1/x64/lib/python3.13/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.13.1/x64/lib/python3.13/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/cycle_detection_undirected\n\
    \n#==================================================\nfrom Graph.Graph.Graph\
    \ import Graph as Undirected_Graph\nfrom Graph.Graph.Cycle import *\n\nimport\
    \ sys\ninput=sys.stdin.readline\nwrite=sys.stdout.write\n\n#==================================================\n\
    def verify():\n    N, M = map(int, input().split())\n\n    G = Undirected_Graph(N)\n\
    \    for j in range(M):\n        a, b = map(int, input().split())\n        G.add_edge(a,\
    \ b, j)\n\n    cycle = Find_Cycle(G)\n\n    if cycle['vertex'] is None:\n    \
    \    print(-1)\n    else:\n        print(len(cycle['edge']))\n        print(*cycle['vertex'][:-1])\n\
    \        print(*cycle['edge'])\n\n#==================================================\n\
    verify()\n"
  dependsOn:
  - Graph/Graph/Graph.py
  - Graph/Graph/Cycle.py
  isVerificationFile: true
  path: test_verify/yosupo_library_checker/Graph/Undirected_Find_Cycle.test.py
  requiredBy: []
  timestamp: '2024-03-20 23:31:16+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test_verify/yosupo_library_checker/Graph/Undirected_Find_Cycle.test.py
layout: document
redirect_from:
- /verify/test_verify/yosupo_library_checker/Graph/Undirected_Find_Cycle.test.py
- /verify/test_verify/yosupo_library_checker/Graph/Undirected_Find_Cycle.test.py.html
title: test_verify/yosupo_library_checker/Graph/Undirected_Find_Cycle.test.py
---
