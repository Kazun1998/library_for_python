---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Modulo_Sequence/Modulo_Polynomial.py
    title: Modulo Polynomial
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/product_of_polynomial_sequence
    links:
    - https://judge.yosupo.jp/problem/product_of_polynomial_sequence
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.1/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.1/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/product_of_polynomial_sequence\n\
    \n#==================================================\nfrom Modulo_Sequence.Modulo_Polynomial\
    \ import *\n\nimport sys\ninput=sys.stdin.readline\nwrite=sys.stdout.write\n\n\
    #==================================================\ndef verify():\n    N=int(input())\n\
    \    A=[None]*N\n\n    global Mod; Mod=998244353\n    global Calc; Calc=Calculator()\n\
    \n    D=0\n    for i in range(N):\n        d,*A[i]=map(int,input().split())\n\
    \        D+=d\n\n    write(\" \".join(map(str, Calc.Multiple_Convolution(*A))))\n\
    \n#==================================================\nverify()\n"
  dependsOn:
  - Modulo_Sequence/Modulo_Polynomial.py
  isVerificationFile: true
  path: test_verify/yosupo_library_checker/Polynomial/Product_of_Polynomial_Sequence.test.py
  requiredBy: []
  timestamp: '2022-12-02 01:16:54+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test_verify/yosupo_library_checker/Polynomial/Product_of_Polynomial_Sequence.test.py
layout: document
redirect_from:
- /verify/test_verify/yosupo_library_checker/Polynomial/Product_of_Polynomial_Sequence.test.py
- /verify/test_verify/yosupo_library_checker/Polynomial/Product_of_Polynomial_Sequence.test.py.html
title: test_verify/yosupo_library_checker/Polynomial/Product_of_Polynomial_Sequence.test.py
---
