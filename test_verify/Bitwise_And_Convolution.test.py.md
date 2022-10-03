---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/bitwise_and_convolution
    links:
    - https://judge.yosupo.jp/problem/bitwise_and_convolution
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.7/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.7/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/bitwise_and_convolution\n\
    \n#==================================================\nimport sys\nsys.path.append('Convolution/')\n\
    from AND_Convolution import *\n\ninput=sys.stdin.readline\nwrite=sys.stdout.write\n\
    \n#==================================================\ndef verify():\n    import\
    \ sys\n    input=sys.stdin.readline\n    write=sys.stdout.write\n\n    N=int(input())\n\
    \    A=list(map(int,input().split()))\n    B=list(map(int,input().split()))\n\
    \    write(\" \".join(map(str,Convolution_AND(A,B))))\n\n#==================================================\n\
    verify()\n"
  dependsOn: []
  isVerificationFile: true
  path: test_verify/Bitwise_And_Convolution.test.py
  requiredBy: []
  timestamp: '2022-10-03 22:55:40+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test_verify/Bitwise_And_Convolution.test.py
layout: document
redirect_from:
- /verify/test_verify/Bitwise_And_Convolution.test.py
- /verify/test_verify/Bitwise_And_Convolution.test.py.html
title: test_verify/Bitwise_And_Convolution.test.py
---
