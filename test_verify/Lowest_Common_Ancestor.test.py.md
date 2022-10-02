---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/lca
    links:
    - https://judge.yosupo.jp/problem/lca
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.7/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.7/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/lca\n\n#==================================================\n\
    import sys\nsys.path.append('Tree/')\nfrom  Tree import Tree\n\ninput=sys.stdin.readline\n\
    write=sys.stdout.write\n#==================================================\n\
    def verify():\n    N,Q=map(int,input().split())\n    P=[0]+list(map(int,input().split()))\n\
    \n    T=Tree(N)\n    T.root_set(0)\n    for i in range(1,N):\n        T.parent_set(i,P[i])\n\
    \    T.seal()\n\n    X=[0]*Q\n    for q in range(Q):\n        u,v=map(int,input().split())\n\
    \        X[q]=T.lowest_common_ancestor(u,v)\n\n    write(\"\\n\".join(map(str,X)))\n\
    \n#==================================================\nverify()\n"
  dependsOn: []
  isVerificationFile: true
  path: test_verify/Lowest_Common_Ancestor.test.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test_verify/Lowest_Common_Ancestor.test.py
layout: document
redirect_from:
- /verify/test_verify/Lowest_Common_Ancestor.test.py
- /verify/test_verify/Lowest_Common_Ancestor.test.py.html
title: test_verify/Lowest_Common_Ancestor.test.py
---
