---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Convolution/XOR_Convolution.py
    title: Xor Convolution
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/bitwise_xor_convolution
    links:
    - https://judge.yosupo.jp/problem/bitwise_xor_convolution
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.1/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.1/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/bitwise_xor_convolution\n\
    \n#==================================================\nfrom Convolution.XOR_Convolution\
    \ import *\n\nimport sys\ninput=sys.stdin.readline\nwrite=sys.stdout.write\n\n\
    #==================================================\ndef verify():\n    N=int(input())\n\
    \    A=list(map(int,input().split()))\n    B=list(map(int,input().split()))\n\
    \    write(\" \".join(map(str,Convolution_XOR(A,B))))\n\n#==================================================\n\
    verify()\n"
  dependsOn:
  - Convolution/XOR_Convolution.py
  isVerificationFile: true
  path: test_verify/yosupo_library_checker/Convolution/Bitwise_Xor_Convolution.test.py
  requiredBy: []
  timestamp: '2022-11-23 16:07:50+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test_verify/yosupo_library_checker/Convolution/Bitwise_Xor_Convolution.test.py
layout: document
redirect_from:
- /verify/test_verify/yosupo_library_checker/Convolution/Bitwise_Xor_Convolution.test.py
- /verify/test_verify/yosupo_library_checker/Convolution/Bitwise_Xor_Convolution.test.py.html
title: test_verify/yosupo_library_checker/Convolution/Bitwise_Xor_Convolution.test.py
---
