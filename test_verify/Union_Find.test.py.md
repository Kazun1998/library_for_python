---
data:
  _extendedDependsOn:
  - icon: ':x:'
    path: Union_Find/Union_Find.py
    title: Union_Find/Union_Find.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/unionfind
    links:
    - https://judge.yosupo.jp/problem/unionfind
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.7/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.7/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/unionfind\n\
    \nimport sys\n\nfrom Union_Find import Union_Find\n\ninput=sys.stdin.readline\n\
    write=sys.stdout.write\n\nN,Q=map(int,input().split())\nU=Union_Find(N)\nX=[]\n\
    for _ in range(Q):\n    t,u,v=map(int,input().split())\n    if t==0:\n       \
    \ U.union(u,v)\n    else:\n        X.append(1 if U.same(u,v) else 0)\n\nwrite(\"\
    \\n\".join(map(str,X)))\n"
  dependsOn:
  - Union_Find/Union_Find.py
  isVerificationFile: true
  path: test_verify/Union_Find.test.py
  requiredBy: []
  timestamp: '2022-04-16 12:03:37+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: test_verify/Union_Find.test.py
layout: document
redirect_from:
- /verify/test_verify/Union_Find.test.py
- /verify/test_verify/Union_Find.test.py.html
title: test_verify/Union_Find.test.py
---
