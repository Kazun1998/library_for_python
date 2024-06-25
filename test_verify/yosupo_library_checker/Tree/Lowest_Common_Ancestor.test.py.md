---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Tree/Tree.py
    title: Tree
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/lca
    links:
    - https://judge.yosupo.jp/problem/lca
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.4/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.4/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/lca\n\n#==================================================\n\
    from Tree.Tree import Tree\n\nimport sys\ninput=sys.stdin.readline\nwrite=sys.stdout.write\n\
    #==================================================\ndef verify():\n    N,Q=map(int,input().split())\n\
    \    P=[0]+list(map(int,input().split()))\n\n    T=Tree(N)\n    T.root_set(0)\n\
    \    for i in range(1,N):\n        T.parent_set(i,P[i])\n    T.seal()\n\n    X=[0]*Q\n\
    \    for q in range(Q):\n        u,v=map(int,input().split())\n        X[q]=T.lowest_common_ancestor(u,v)\n\
    \n    write(\"\\n\".join(map(str,X)))\n\n#==================================================\n\
    verify()\n"
  dependsOn:
  - Tree/Tree.py
  isVerificationFile: true
  path: test_verify/yosupo_library_checker/Tree/Lowest_Common_Ancestor.test.py
  requiredBy: []
  timestamp: '2024-05-25 23:55:04+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test_verify/yosupo_library_checker/Tree/Lowest_Common_Ancestor.test.py
layout: document
redirect_from:
- /verify/test_verify/yosupo_library_checker/Tree/Lowest_Common_Ancestor.test.py
- /verify/test_verify/yosupo_library_checker/Tree/Lowest_Common_Ancestor.test.py.html
title: test_verify/yosupo_library_checker/Tree/Lowest_Common_Ancestor.test.py
---
