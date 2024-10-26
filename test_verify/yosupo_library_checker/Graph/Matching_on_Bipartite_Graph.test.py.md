---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Bipart_Matching.py
    title: Bipart_Matching.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/bipartitematching
    links:
    - https://judge.yosupo.jp/problem/bipartitematching
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.7/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.7/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/bipartitematching\n\
    \n#==================================================\nfrom Bipart_Matching import\
    \ *\n\nimport sys\ninput=sys.stdin.readline\nwrite=sys.stdout.write\n\n#==================================================\n\
    def verify():\n    L,R,M=map(int,input().split())\n    G=Bipartite_Matching(L,R)\n\
    \n    for _ in range(M):\n        a,b=map(int,input().split())\n        G.add_edge(a,b)\n\
    \n    K,(A,B)=G.max_matching(1)\n\n    H=[]\n    for i in range(L):\n        if\
    \ A[i]!=-1:\n            H.append((i,A[i]))\n\n    print(K)\n    def string(x):\n\
    \        return \"{} {}\".format(x[0],x[1])\n\n    write(\"\\n\".join(map(string,H)))\n\
    \    print()\n\n#==================================================\nverify()\n"
  dependsOn:
  - Bipart_Matching.py
  isVerificationFile: true
  path: test_verify/yosupo_library_checker/Graph/Matching_on_Bipartite_Graph.test.py
  requiredBy: []
  timestamp: '2022-11-23 15:56:15+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test_verify/yosupo_library_checker/Graph/Matching_on_Bipartite_Graph.test.py
layout: document
redirect_from:
- /verify/test_verify/yosupo_library_checker/Graph/Matching_on_Bipartite_Graph.test.py
- /verify/test_verify/yosupo_library_checker/Graph/Matching_on_Bipartite_Graph.test.py.html
title: test_verify/yosupo_library_checker/Graph/Matching_on_Bipartite_Graph.test.py
---
