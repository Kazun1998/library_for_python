---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Stern_Brocot_Tree.py
    title: Stern_Brocot_Tree.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/rational_approximation
    links:
    - https://judge.yosupo.jp/problem/rational_approximation
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.13.5/x64/lib/python3.13/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.13.5/x64/lib/python3.13/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/rational_approximation\n\
    \n#==================================================\nfrom Stern_Brocot_Tree\
    \ import *\n\nimport sys\ninput=sys.stdin.readline\nwrite=sys.stdout.write\n\n\
    #==================================================\ndef verify():\n    T = int(input())\n\
    \n    for _ in range(T):\n        N, x, y = map(int, input().split())\n      \
    \  _, _, c, d = Stern_Brocot_Tree.binary_search_range_increase(N, lambda a, b:\
    \ a * y >= b * x)\n        a, b, _, _ = Stern_Brocot_Tree.binary_search_range_increase(N,\
    \ lambda a, b: a * y > b * x)\n        yield f\"{a} {b} {c} {d}\"\n\n#==================================================\n\
    \nwrite(\"\\n\".join(map(str, verify())))\n"
  dependsOn:
  - Stern_Brocot_Tree.py
  isVerificationFile: true
  path: test_verify/yosupo_library_checker/Math/Rational_Approximation.test.py
  requiredBy: []
  timestamp: '2025-06-22 15:22:29+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test_verify/yosupo_library_checker/Math/Rational_Approximation.test.py
layout: document
redirect_from:
- /verify/test_verify/yosupo_library_checker/Math/Rational_Approximation.test.py
- /verify/test_verify/yosupo_library_checker/Math/Rational_Approximation.test.py.html
title: test_verify/yosupo_library_checker/Math/Rational_Approximation.test.py
---
