---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Union_Find/Union_Find.py
    title: Union Find (Disjoint Set Union)
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/unionfind
    links:
    - https://judge.yosupo.jp/problem/unionfind
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.1/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.1/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/unionfind\n\
    \n#==================================================\nfrom Union_Find.Union_Find\
    \ import Union_Find\n\nimport sys\ninput=sys.stdin.readline\nwrite=sys.stdout.write\n\
    #==================================================\ndef verify():\n    N,Q=map(int,input().split())\n\
    \    U=Union_Find(N)\n    X=[]\n    for _ in range(Q):\n        t,u,v=map(int,input().split())\n\
    \        if t==0:\n            U.union(u,v)\n        else:\n            X.append(1\
    \ if U.same(u,v) else 0)\n\n    write(\"\\n\".join(map(str,X)))\n#==================================================\n\
    verify()\n"
  dependsOn:
  - Union_Find/Union_Find.py
  isVerificationFile: true
  path: test_verify/yosupo_library_checker/Data_Structure/Union_Find.test.py
  requiredBy: []
  timestamp: '2022-12-04 19:53:09+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test_verify/yosupo_library_checker/Data_Structure/Union_Find.test.py
layout: document
redirect_from:
- /verify/test_verify/yosupo_library_checker/Data_Structure/Union_Find.test.py
- /verify/test_verify/yosupo_library_checker/Data_Structure/Union_Find.test.py.html
title: test_verify/yosupo_library_checker/Data_Structure/Union_Find.test.py
---
