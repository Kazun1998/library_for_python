---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Gaussian_Integer.py
    title: Gaussian_Integer.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/gcd_of_gaussian_integers
    links:
    - https://judge.yosupo.jp/problem/gcd_of_gaussian_integers
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.13.3/x64/lib/python3.13/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.13.3/x64/lib/python3.13/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/gcd_of_gaussian_integers\n\
    \n#==================================================\nfrom Gaussian_Integer import\
    \ Gaussian_Integer, gcd\n\nimport sys\ninput=sys.stdin.readline\nwrite=sys.stdout.write\n\
    \n#==================================================\ndef verify():\n    a, b,\
    \ c, d = map(int, input().split())\n    g = gcd(Gaussian_Integer(a, b), Gaussian_Integer(c,\
    \ d))\n    return f'{g.re} {g.im}'\n\n#==================================================\n\
    T = int(input())\nwrite(\"\\n\".join([verify() for _ in range(T)]))\n"
  dependsOn:
  - Gaussian_Integer.py
  isVerificationFile: true
  path: test_verify/yosupo_library_checker/Math/Gcd_of_Gaussian_Integers.test.py
  requiredBy: []
  timestamp: '2025-03-27 23:13:02+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test_verify/yosupo_library_checker/Math/Gcd_of_Gaussian_Integers.test.py
layout: document
redirect_from:
- /verify/test_verify/yosupo_library_checker/Math/Gcd_of_Gaussian_Integers.test.py
- /verify/test_verify/yosupo_library_checker/Math/Gcd_of_Gaussian_Integers.test.py.html
title: test_verify/yosupo_library_checker/Math/Gcd_of_Gaussian_Integers.test.py
---
