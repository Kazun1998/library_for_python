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
    PROBLEM: https://judge.yosupo.jp/problem/matrix_det
    links:
    - https://judge.yosupo.jp/problem/matrix_det
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.2/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.2/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/matrix_det\n\
    \n#==================================================\nfrom Modulo_Matrix.Modulo_Matrix\
    \ import *\n\nimport sys\ninput=sys.stdin.readline\nwrite=sys.stdout.write\n\n\
    #==================================================\ndef verify():\n    N=int(input())\n\
    \    A=[None]*N\n\n    for i in range(N):\n        A[i]=list(map(int,input().split()))\n\
    \n    A=Modulo_Matrix(A)\n    print(Determinant(A))\n\n#==================================================\n\
    verify()"
  dependsOn:
  - Modulo_Matrix/Modulo_Matrix.py
  isVerificationFile: true
  path: test_verify/yosupo_library_checker/Matrix/Determinant.test.py
  requiredBy: []
  timestamp: '2024-02-25 10:36:05+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test_verify/yosupo_library_checker/Matrix/Determinant.test.py
layout: document
redirect_from:
- /verify/test_verify/yosupo_library_checker/Matrix/Determinant.test.py
- /verify/test_verify/yosupo_library_checker/Matrix/Determinant.test.py.html
title: test_verify/yosupo_library_checker/Matrix/Determinant.test.py
---