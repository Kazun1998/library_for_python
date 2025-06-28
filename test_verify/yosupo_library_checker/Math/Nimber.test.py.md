---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Nimber.py
    title: Nimber
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/nim_product_64
    links:
    - https://judge.yosupo.jp/problem/nim_product_64
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.13.5/x64/lib/python3.13/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.13.5/x64/lib/python3.13/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/nim_product_64\n\
    \n#==================================================\nfrom Nimber import *\n\n\
    import sys\ninput=sys.stdin.readline\nwrite=sys.stdout.write\n\n#==================================================\n\
    def verify():\n    T = int(input())\n    ans = [0] * T\n    for t in range(T):\n\
    \        A, B = map(Nimber, input().split())\n        ans[t] = A * B\n\n    write(\"\
    \\n\".join(map(str, ans)))\n\n#==================================================\n\
    verify()"
  dependsOn:
  - Nimber.py
  isVerificationFile: true
  path: test_verify/yosupo_library_checker/Math/Nimber.test.py
  requiredBy: []
  timestamp: '2025-03-25 23:53:58+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test_verify/yosupo_library_checker/Math/Nimber.test.py
layout: document
redirect_from:
- /verify/test_verify/yosupo_library_checker/Math/Nimber.test.py
- /verify/test_verify/yosupo_library_checker/Math/Nimber.test.py.html
title: test_verify/yosupo_library_checker/Math/Nimber.test.py
---
