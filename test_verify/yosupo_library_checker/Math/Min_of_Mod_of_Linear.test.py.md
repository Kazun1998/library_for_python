---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Summation/Floor_Sum.py
    title: Floor Sum
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/min_of_mod_of_linear
    links:
    - https://judge.yosupo.jp/problem/min_of_mod_of_linear
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.13.5/x64/lib/python3.13/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.13.5/x64/lib/python3.13/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/min_of_mod_of_linear\n\
    \n#==================================================\nfrom Summation.Floor_Sum\
    \ import *\n\nimport sys\ninput=sys.stdin.readline\nwrite=sys.stdout.write\n\n\
    #==================================================\ndef verify():\n    T = int(input())\n\
    \n    ans = [0] * T\n    for t in range(T):\n        N, M, A, B = map(int ,input().split())\n\
    \        ans[t] = Min_of_Mod_of_Linear(A, B, M, N)\n\n    write(\"\\n\".join(map(str,\
    \ ans)))\n\n#==================================================\nverify()"
  dependsOn:
  - Summation/Floor_Sum.py
  isVerificationFile: true
  path: test_verify/yosupo_library_checker/Math/Min_of_Mod_of_Linear.test.py
  requiredBy: []
  timestamp: '2025-04-22 00:58:06+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test_verify/yosupo_library_checker/Math/Min_of_Mod_of_Linear.test.py
layout: document
redirect_from:
- /verify/test_verify/yosupo_library_checker/Math/Min_of_Mod_of_Linear.test.py
- /verify/test_verify/yosupo_library_checker/Math/Min_of_Mod_of_Linear.test.py.html
title: test_verify/yosupo_library_checker/Math/Min_of_Mod_of_Linear.test.py
---
