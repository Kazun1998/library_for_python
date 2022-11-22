---
data:
  _extendedDependsOn:
  - icon: ':question:'
    path: Modulo_Sequence/Modulo_Polynomial.py
    title: Modulo_Sequence/Modulo_Polynomial.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/pow_of_formal_power_series
    links:
    - https://judge.yosupo.jp/problem/pow_of_formal_power_series
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/pow_of_formal_power_series\n\
    \n#==================================================\nfrom Modulo_Sequence.Modulo_Polynomial\
    \ import *\n\nimport sys\ninput=sys.stdin.readline\nwrite=sys.stdout.write\n\n\
    #==================================================\ndef verify():\n    N,M=map(int,input().split())\n\
    \    A=list(map(int,input().split()))\n    P=Modulo_Polynomial(A,N)\n    B=Power(P,M).Poly\n\
    \    B.extend([0]*(N-len(B)))\n    write(\" \".join(map(str,B)))\n\n#==================================================\n\
    verify()"
  dependsOn:
  - Modulo_Sequence/Modulo_Polynomial.py
  isVerificationFile: true
  path: test_verify/yosupo_library_checker/Polynomial/Power.test.py
  requiredBy: []
  timestamp: '2022-11-23 04:00:21+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test_verify/yosupo_library_checker/Polynomial/Power.test.py
layout: document
redirect_from:
- /verify/test_verify/yosupo_library_checker/Polynomial/Power.test.py
- /verify/test_verify/yosupo_library_checker/Polynomial/Power.test.py.html
title: test_verify/yosupo_library_checker/Polynomial/Power.test.py
---
