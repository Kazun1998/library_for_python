---
data:
  _extendedDependsOn:
  - icon: ':question:'
    path: Modulo_Sequence/Modulo_Polynomial.py
    title: Modulo Polynomial
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/polynomial_taylor_shift
    links:
    - https://judge.yosupo.jp/problem/polynomial_taylor_shift
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.13.3/x64/lib/python3.13/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.13.3/x64/lib/python3.13/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/polynomial_taylor_shift\n\
    \n#==================================================\nfrom Modulo_Sequence.Modulo_Polynomial\
    \ import *\n\nimport sys\ninput=sys.stdin.readline\nwrite=sys.stdout.write\n\n\
    #==================================================\ndef verify():\n    N,c=map(int,input().split())\n\
    \    A=list(map(int,input().split()))\n    A=Modulo_Polynomial(A,N)\n\n    write(\"\
    \ \".join(map(str,Taylor_Shift(A,c).poly)))\n\n#==================================================\n\
    verify()"
  dependsOn:
  - Modulo_Sequence/Modulo_Polynomial.py
  isVerificationFile: true
  path: test_verify/yosupo_library_checker/Polynomial/Taylor_Shift.test.py
  requiredBy: []
  timestamp: '2025-05-04 10:58:23+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: test_verify/yosupo_library_checker/Polynomial/Taylor_Shift.test.py
layout: document
redirect_from:
- /verify/test_verify/yosupo_library_checker/Polynomial/Taylor_Shift.test.py
- /verify/test_verify/yosupo_library_checker/Polynomial/Taylor_Shift.test.py.html
title: test_verify/yosupo_library_checker/Polynomial/Taylor_Shift.test.py
---
