---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Graph/Graph/Graph.py
    title: Graph
  - icon: ':heavy_check_mark:'
    path: Graph/Graph/LowLink.py
    title: Graph/Graph/LowLink.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/two_edge_connected_components
    links:
    - https://judge.yosupo.jp/problem/two_edge_connected_components
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.4/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.4/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/two_edge_connected_components\n\
    \n#==================================================\nfrom Graph.Graph.Graph\
    \ import Graph as Undirected_Graph\nfrom Graph.Graph.LowLink import *\n\nimport\
    \ sys\ninput=sys.stdin.readline\nwrite=sys.stdout.write\n\n#==================================================\n\
    def verify():\n    N, M = map(int, input().split())\n\n    G = Undirected_Graph(N)\n\
    \    for j in range(M):\n        a, b = map(int, input().split())\n        G.add_edge(a,\
    \ b, j)\n\n    comps = Two_Edge_Connected_Components(G)['comps']\n\n    def writer(comp):\n\
    \        return f\"{len(comp)} {' '.join(map(str, comp))}\"\n\n    print(len(comps))\n\
    \    write(\"\\n\".join(map(writer, comps)))\n\n#==================================================\n\
    verify()\n"
  dependsOn:
  - Graph/Graph/LowLink.py
  - Graph/Graph/Graph.py
  isVerificationFile: true
  path: test_verify/yosupo_library_checker/Graph/Two_Edge_Connected_Components.test.py
  requiredBy: []
  timestamp: '2024-03-20 23:42:58+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test_verify/yosupo_library_checker/Graph/Two_Edge_Connected_Components.test.py
layout: document
redirect_from:
- /verify/test_verify/yosupo_library_checker/Graph/Two_Edge_Connected_Components.test.py
- /verify/test_verify/yosupo_library_checker/Graph/Two_Edge_Connected_Components.test.py.html
title: test_verify/yosupo_library_checker/Graph/Two_Edge_Connected_Components.test.py
---
