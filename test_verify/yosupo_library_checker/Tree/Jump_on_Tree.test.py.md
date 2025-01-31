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
    PROBLEM: https://judge.yosupo.jp/problem/jump_on_tree
    links:
    - https://judge.yosupo.jp/problem/jump_on_tree
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.13.1/x64/lib/python3.13/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.13.1/x64/lib/python3.13/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/jump_on_tree\n\
    \n#==================================================\nimport sys\nfrom Tree.Tree\
    \ import Making_Tree_from_Edges\n\ninput=sys.stdin.readline\nwrite=sys.stdout.write\n\
    #==================================================\ndef verify():\n    N,Q=map(int,input().split())\n\
    \n    E=[]\n    for j in range(N-1):\n        a,b=map(int,input().split())\n \
    \       E.append((a,b))\n\n    T=Making_Tree_from_Edges(N, E, 0, 0)\n\n    X=[0]*Q\n\
    \    for q in range(Q):\n        s,t,i=map(int,input().split())\n        X[q]=T.jump(s,t,i)\n\
    \n    write(\"\\n\".join(map(str,X)))\n\n\n#==================================================\n\
    verify()\n"
  dependsOn:
  - Tree/Tree.py
  isVerificationFile: true
  path: test_verify/yosupo_library_checker/Tree/Jump_on_Tree.test.py
  requiredBy: []
  timestamp: '2024-05-25 23:55:04+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test_verify/yosupo_library_checker/Tree/Jump_on_Tree.test.py
layout: document
redirect_from:
- /verify/test_verify/yosupo_library_checker/Tree/Jump_on_Tree.test.py
- /verify/test_verify/yosupo_library_checker/Tree/Jump_on_Tree.test.py.html
title: test_verify/yosupo_library_checker/Tree/Jump_on_Tree.test.py
---
