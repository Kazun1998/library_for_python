---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Modulo_Matrix/Modulo_Matrix.py
    title: Modulo_Matrix/Modulo_Matrix.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/matrix_product
    links:
    - https://judge.yosupo.jp/problem/matrix_product
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/matrix_product\n\
    \n#==================================================\nfrom Modulo_Matrix.Modulo_Matrix\
    \ import Modulo_Matrix\n\nimport sys\ninput=sys.stdin.readline\nwrite=sys.stdout.write\n\
    \n#==================================================\ndef verify():\n    N,M,K=map(int,input().split())\n\
    \n    A=[]\n    for i in range(N):\n        A.append(list(map(int,input().split())))\n\
    \n    B=[]\n    for i in range(M):\n        B.append(list(map(int,input().split())))\n\
    \n    C=Modulo_Matrix(A)*Modulo_Matrix(B)\n\n    string=lambda x:\" \".join(map(str,x))\n\
    \    write(\"\\n\".join(map(string,C.ele)))\n\n#==================================================\n\
    verify()"
  dependsOn:
  - Modulo_Matrix/Modulo_Matrix.py
  isVerificationFile: true
  path: test_verify/yosupo_library_checker/Matrix/Product.test.py
  requiredBy: []
  timestamp: '2022-11-23 02:23:22+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test_verify/yosupo_library_checker/Matrix/Product.test.py
layout: document
redirect_from:
- /verify/test_verify/yosupo_library_checker/Matrix/Product.test.py
- /verify/test_verify/yosupo_library_checker/Matrix/Product.test.py.html
title: test_verify/yosupo_library_checker/Matrix/Product.test.py
---