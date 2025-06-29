---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Integer/Prime.py
    title: Integer/Prime.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/factorize
    links:
    - https://judge.yosupo.jp/problem/factorize
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.13.5/x64/lib/python3.13/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.13.5/x64/lib/python3.13/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/factorize\n\
    \n#==================================================\nfrom Integer.Prime import\
    \ *\n\nimport sys\ninput=sys.stdin.readline\nwrite=sys.stdout.write\n\n#==================================================\n\
    def verify():\n    Q = int(input())\n    for _ in range(Q):\n        a = int(input())\n\
    \        prime_factors = Pollard_Rho_Prime_Factorization(a)\n        primes =\
    \ []\n        for p, e in prime_factors:\n            primes.extend([p] * e)\n\
    \n        print(len(primes), *primes)\n\n#==================================================\n\
    verify()\n"
  dependsOn:
  - Integer/Prime.py
  isVerificationFile: true
  path: test_verify/yosupo_library_checker/Math/Factorize.test.py
  requiredBy: []
  timestamp: '2025-06-29 11:20:13+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test_verify/yosupo_library_checker/Math/Factorize.test.py
layout: document
redirect_from:
- /verify/test_verify/yosupo_library_checker/Math/Factorize.test.py
- /verify/test_verify/yosupo_library_checker/Math/Factorize.test.py.html
title: test_verify/yosupo_library_checker/Math/Factorize.test.py
---
