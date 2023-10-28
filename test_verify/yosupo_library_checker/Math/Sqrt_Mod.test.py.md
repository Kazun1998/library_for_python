---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Modulo.py
    title: Modulo
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/sqrt_mod
    links:
    - https://judge.yosupo.jp/problem/sqrt_mod
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.0/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.0/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/sqrt_mod\n\
    \n#==================================================\nfrom Modulo import *\n\n\
    import sys\ninput=sys.stdin.readline\nwrite=sys.stdout.write\n\n#==================================================\n\
    def verify():\n    T=int(input())\n    Ans=[-1]*T\n\n    for t in range(T):\n\
    \        Y,P=map(int,input().split())\n        X=Sqrt(Modulo(Y,P))\n\n       \
    \ if X is not None:\n            Ans[t]=X.a\n\n    write(\"\\n\".join(map(str,Ans)))\n\
    \n#==================================================\nverify()\n"
  dependsOn:
  - Modulo.py
  isVerificationFile: true
  path: test_verify/yosupo_library_checker/Math/Sqrt_Mod.test.py
  requiredBy: []
  timestamp: '2023-08-08 01:23:05+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test_verify/yosupo_library_checker/Math/Sqrt_Mod.test.py
layout: document
redirect_from:
- /verify/test_verify/yosupo_library_checker/Math/Sqrt_Mod.test.py
- /verify/test_verify/yosupo_library_checker/Math/Sqrt_Mod.test.py.html
title: test_verify/yosupo_library_checker/Math/Sqrt_Mod.test.py
---
