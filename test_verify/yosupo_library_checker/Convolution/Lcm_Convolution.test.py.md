---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Convolution/LCM_Convolution.py
    title: Lcm Convolution
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/lcm_convolution
    links:
    - https://judge.yosupo.jp/problem/lcm_convolution
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/lcm_convolution\n\
    \n#==================================================\nfrom Convolution.LCM_Convolution\
    \ import Convolution_LCM\n\nimport sys\ninput=sys.stdin.readline\nwrite=sys.stdout.write\n\
    \n#==================================================\ndef verify():\n    N=int(input())\n\
    \    A=[0]+list(map(int,input().split()))\n    B=[0]+list(map(int,input().split()))\n\
    \    write(\" \".join(map(str,Convolution_LCM(A,B,N)[1:])))\n\n#==================================================\n\
    verify()"
  dependsOn:
  - Convolution/LCM_Convolution.py
  isVerificationFile: true
  path: test_verify/yosupo_library_checker/Convolution/Lcm_Convolution.test.py
  requiredBy: []
  timestamp: '2022-11-22 23:25:26+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test_verify/yosupo_library_checker/Convolution/Lcm_Convolution.test.py
layout: document
redirect_from:
- /verify/test_verify/yosupo_library_checker/Convolution/Lcm_Convolution.test.py
- /verify/test_verify/yosupo_library_checker/Convolution/Lcm_Convolution.test.py.html
title: test_verify/yosupo_library_checker/Convolution/Lcm_Convolution.test.py
---
