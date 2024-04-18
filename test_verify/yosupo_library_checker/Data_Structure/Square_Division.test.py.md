---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Division/Square_Division.py
    title: Division/Square_Division.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/static_range_sum
    links:
    - https://judge.yosupo.jp/problem/static_range_sum
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.3/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.3/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/static_range_sum\n\
    \n#==================================================\nfrom Division.Square_Division\
    \ import *\n\nimport sys\ninput=sys.stdin.readline\nwrite=sys.stdout.write\n\n\
    #==================================================\ndef verify():\n    from operator\
    \ import add\n\n    N, Q = map(int, input().split())\n    A = list(map(int, input().split()))\n\
    \n    S = Square_Division(A, add, 0)\n    ans = [0] * Q\n\n    for q in range(Q):\n\
    \        l, r = map(int, input().split())\n        ans[q] = S.product(l, r - 1)\n\
    \n    write(\"\\n\".join(map(str, ans)))\n\n#==================================================\n\
    verify()\n"
  dependsOn:
  - Division/Square_Division.py
  isVerificationFile: true
  path: test_verify/yosupo_library_checker/Data_Structure/Square_Division.test.py
  requiredBy: []
  timestamp: '2024-03-21 00:27:42+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test_verify/yosupo_library_checker/Data_Structure/Square_Division.test.py
layout: document
redirect_from:
- /verify/test_verify/yosupo_library_checker/Data_Structure/Square_Division.test.py
- /verify/test_verify/yosupo_library_checker/Data_Structure/Square_Division.test.py.html
title: test_verify/yosupo_library_checker/Data_Structure/Square_Division.test.py
---
