---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/gcd_of_gaussian_integers
    links:
    - https://judge.yosupo.jp/problem/gcd_of_gaussian_integers
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.1/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.1/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/gcd_of_gaussian_integers\n\
    \n#==================================================\nfrom Gaussian_Integers\
    \ import *\n\nimport sys\ninput=sys.stdin.readline\nwrite=sys.stdout.write\n\n\
    #==================================================\ndef verify():\n    a, b,\
    \ c, d = map(int, input().split())\n    return gcd(Gaussian_Integer(a, b), Gaussian_Integer(c,\
    \ d))\n\n#==================================================\nT = int(input())\n\
    write(\"\\n\".join(verify()))\n"
  dependsOn: []
  isVerificationFile: false
  path: test_verify/yosupo_library_checker/Math/Gcd_of_Gaussian_Integers.py
  requiredBy: []
  timestamp: '2024-02-04 00:58:43+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: test_verify/yosupo_library_checker/Math/Gcd_of_Gaussian_Integers.py
layout: document
redirect_from:
- /library/test_verify/yosupo_library_checker/Math/Gcd_of_Gaussian_Integers.py
- /library/test_verify/yosupo_library_checker/Math/Gcd_of_Gaussian_Integers.py.html
title: test_verify/yosupo_library_checker/Math/Gcd_of_Gaussian_Integers.py
---
