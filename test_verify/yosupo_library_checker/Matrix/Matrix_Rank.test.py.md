---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Modulo_Matrix/Modulo_Matrix.py
    title: Modulo_Matrix
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/matrix_rank
    links:
    - https://judge.yosupo.jp/problem/matrix_rank
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.8/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.8/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/matrix_rank\n\
    \n#==================================================\nfrom Modulo_Matrix.Modulo_Matrix\
    \ import Modulo_Matrix\n\nimport sys\ninput=sys.stdin.readline\nwrite=sys.stdout.write\n\
    \n#==================================================\ndef verify():\n    global\
    \ Mod; Mod = 998244353\n\n    N, M = map(int, input().split())\n\n    A = [None]\
    \ * N\n    for i in range(N):\n        A[i] = list(map(int, input().split()))\n\
    \n    A = Modulo_Matrix(A)\n    print(A.rank())\n\n#==================================================\n\
    verify()\n"
  dependsOn:
  - Modulo_Matrix/Modulo_Matrix.py
  isVerificationFile: true
  path: test_verify/yosupo_library_checker/Matrix/Matrix_Rank.test.py
  requiredBy: []
  timestamp: '2024-12-06 01:02:56+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test_verify/yosupo_library_checker/Matrix/Matrix_Rank.test.py
layout: document
redirect_from:
- /verify/test_verify/yosupo_library_checker/Matrix/Matrix_Rank.test.py
- /verify/test_verify/yosupo_library_checker/Matrix/Matrix_Rank.test.py.html
title: test_verify/yosupo_library_checker/Matrix/Matrix_Rank.test.py
---
