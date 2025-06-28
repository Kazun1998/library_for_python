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
    PROBLEM: https://judge.yosupo.jp/problem/division_of_polynomials
    links:
    - https://judge.yosupo.jp/problem/division_of_polynomials
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.13.5/x64/lib/python3.13/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.13.5/x64/lib/python3.13/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/division_of_polynomials\n\
    \n#==================================================\nfrom Modulo_Sequence.Modulo_Polynomial\
    \ import *\n\nimport sys\ninput=sys.stdin.readline\nwrite=sys.stdout.write\n\n\
    #==================================================\ndef verify():\n    N,M=map(int,input().split())\n\
    \    F=list(map(int,input().split()))\n    G=list(map(int,input().split()))\n\n\
    \    F=Modulo_Polynomial(F,N)\n    G=Modulo_Polynomial(G,M)\n\n    Q,R=divmod(F,G)\n\
    \n    Q.reduce(); R.reduce()\n    Q=Q.poly if Q.poly!=[0] else []\n    R=R.poly\
    \ if R.poly!=[0] else []\n\n    print(len(Q), len(R))\n    write(\" \".join(map(str,Q)));\
    \ print()\n    write(\" \".join(map(str,R)))\n\n#==================================================\n\
    verify()\n"
  dependsOn:
  - Modulo_Sequence/Modulo_Polynomial.py
  isVerificationFile: true
  path: test_verify/yosupo_library_checker/Polynomial/Division.test.py
  requiredBy: []
  timestamp: '2025-05-04 10:58:23+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test_verify/yosupo_library_checker/Polynomial/Division.test.py
layout: document
redirect_from:
- /verify/test_verify/yosupo_library_checker/Polynomial/Division.test.py
- /verify/test_verify/yosupo_library_checker/Polynomial/Division.test.py.html
title: test_verify/yosupo_library_checker/Polynomial/Division.test.py
---
