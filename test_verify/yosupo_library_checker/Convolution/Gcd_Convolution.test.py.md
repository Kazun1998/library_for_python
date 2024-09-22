---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Convolution/GCD_Convolution.py
    title: Gcd Convolution
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/gcd_convolution
    links:
    - https://judge.yosupo.jp/problem/gcd_convolution
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.6/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.6/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/gcd_convolution\n\
    \n#==================================================\nfrom Convolution.GCD_Convolution\
    \ import Convolution_GCD\n\nimport sys\ninput=sys.stdin.readline\nwrite=sys.stdout.write\n\
    \n#==================================================\ndef verify():\n    N=int(input())\n\
    \    A=[0]+list(map(int,input().split()))\n    B=[0]+list(map(int,input().split()))\n\
    \n    write(\" \".join(map(str,Convolution_GCD(A,B)[1:])))\n\n#==================================================\n\
    verify()\n"
  dependsOn:
  - Convolution/GCD_Convolution.py
  isVerificationFile: true
  path: test_verify/yosupo_library_checker/Convolution/Gcd_Convolution.test.py
  requiredBy: []
  timestamp: '2022-11-22 23:25:26+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test_verify/yosupo_library_checker/Convolution/Gcd_Convolution.test.py
layout: document
redirect_from:
- /verify/test_verify/yosupo_library_checker/Convolution/Gcd_Convolution.test.py
- /verify/test_verify/yosupo_library_checker/Convolution/Gcd_Convolution.test.py.html
title: test_verify/yosupo_library_checker/Convolution/Gcd_Convolution.test.py
---
