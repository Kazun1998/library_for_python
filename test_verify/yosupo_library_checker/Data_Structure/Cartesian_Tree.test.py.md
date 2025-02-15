---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Sequence/Cartesian_Tree.py
    title: Sequence/Cartesian_Tree.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/cartesian_tree
    links:
    - https://judge.yosupo.jp/problem/cartesian_tree
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.13.2/x64/lib/python3.13/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.13.2/x64/lib/python3.13/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/cartesian_tree\n\
    \n#==================================================\nfrom Sequence.Cartesian_Tree\
    \ import Cartesian_Tree\n\nimport sys\ninput=sys.stdin.readline\nwrite=sys.stdout.write\n\
    #==================================================\ndef verify():\n    N = int(input())\n\
    \    A = list(map(int, input().split()))\n    print(*[t if t != -1 else i for\
    \ i, t in enumerate(Cartesian_Tree(A).parent)])\n\n#==================================================\n\
    verify()\n"
  dependsOn:
  - Sequence/Cartesian_Tree.py
  isVerificationFile: true
  path: test_verify/yosupo_library_checker/Data_Structure/Cartesian_Tree.test.py
  requiredBy: []
  timestamp: '2024-08-02 23:29:24+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test_verify/yosupo_library_checker/Data_Structure/Cartesian_Tree.test.py
layout: document
redirect_from:
- /verify/test_verify/yosupo_library_checker/Data_Structure/Cartesian_Tree.test.py
- /verify/test_verify/yosupo_library_checker/Data_Structure/Cartesian_Tree.test.py.html
title: test_verify/yosupo_library_checker/Data_Structure/Cartesian_Tree.test.py
---
