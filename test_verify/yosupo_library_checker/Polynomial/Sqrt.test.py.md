---
data:
  _extendedDependsOn:
  - icon: ':question:'
    path: Modulo_Sequence/Modulo_Polynomial.py
    title: Modulo_Sequence/Modulo_Polynomial.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/sqrt_of_formal_power_series
    links:
    - https://judge.yosupo.jp/problem/sqrt_of_formal_power_series
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/sqrt_of_formal_power_series\n\
    \n#==================================================\nimport sys\nsys.path.append(\"\
    ../../../\")\nfrom Modulo_Sequence.Modulo_Polynomial import *\n\nimport sys\n\
    input=sys.stdin.readline\nwrite=sys.stdout.write\n\n#==================================================\n\
    def verify():\n    N=int(input())\n\n    A=list(map(int,input().split()))\n  \
    \  P=Modulo_Polynomial(A,N)\n\n    try:\n        write(\" \".join(map(str, Sqrt(P).resize(N,True))))\n\
    \    except:\n        print(-1)\n\n#==================================================\n\
    verify()\n"
  dependsOn:
  - Modulo_Sequence/Modulo_Polynomial.py
  isVerificationFile: true
  path: test_verify/yosupo_library_checker/Polynomial/Sqrt.test.py
  requiredBy: []
  timestamp: '2022-11-23 04:03:17+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: test_verify/yosupo_library_checker/Polynomial/Sqrt.test.py
layout: document
redirect_from:
- /verify/test_verify/yosupo_library_checker/Polynomial/Sqrt.test.py
- /verify/test_verify/yosupo_library_checker/Polynomial/Sqrt.test.py.html
title: test_verify/yosupo_library_checker/Polynomial/Sqrt.test.py
---
