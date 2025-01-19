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
    PROBLEM: https://judge.yosupo.jp/problem/adjugate_matrix
    links:
    - https://judge.yosupo.jp/problem/adjugate_matrix
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.8/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.8/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/adjugate_matrix\n\
    \n#==================================================\nfrom Modulo_Matrix.Modulo_Matrix\
    \ import Modulo_Matrix, Adjugate_Matrix\n\nimport sys\ninput=sys.stdin.readline\n\
    write=sys.stdout.write\n\n#==================================================\n\
    def verify():\n    N = int(input())\n    A = [None] * N\n    for i in range(N):\n\
    \        A[i] = list(map(int, input().split()))\n\n    A = Modulo_Matrix(A)\n\
    \    B = Adjugate_Matrix(A)\n\n    for i in range(N):\n        print(*B[i])\n\n\
    #==================================================\nverify()\n"
  dependsOn:
  - Modulo_Matrix/Modulo_Matrix.py
  isVerificationFile: true
  path: test_verify/yosupo_library_checker/Matrix/Adjugate_Matrix.test.py
  requiredBy: []
  timestamp: '2024-12-06 01:02:56+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test_verify/yosupo_library_checker/Matrix/Adjugate_Matrix.test.py
layout: document
redirect_from:
- /verify/test_verify/yosupo_library_checker/Matrix/Adjugate_Matrix.test.py
- /verify/test_verify/yosupo_library_checker/Matrix/Adjugate_Matrix.test.py.html
title: test_verify/yosupo_library_checker/Matrix/Adjugate_Matrix.test.py
---
