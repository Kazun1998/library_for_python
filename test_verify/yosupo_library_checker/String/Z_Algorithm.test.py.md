---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Sequence/Z_Algorithm.py
    title: Sequence/Z_Algorithm.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/zalgorithm
    links:
    - https://judge.yosupo.jp/problem/zalgorithm
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.13.3/x64/lib/python3.13/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.13.3/x64/lib/python3.13/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/zalgorithm\n\
    \n#==================================================\nfrom Sequence.Z_Algorithm\
    \ import *\n\nimport sys\ninput=sys.stdin.readline\nwrite=sys.stdout.write\n\n\
    #==================================================\ndef verify():\n    S=input()[:-1]\n\
    \    write(\" \".join(map(str,Z_Algorithm(S))))\n\n#==================================================\n\
    verify()\n"
  dependsOn:
  - Sequence/Z_Algorithm.py
  isVerificationFile: true
  path: test_verify/yosupo_library_checker/String/Z_Algorithm.test.py
  requiredBy: []
  timestamp: '2022-11-26 04:03:20+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test_verify/yosupo_library_checker/String/Z_Algorithm.test.py
layout: document
redirect_from:
- /verify/test_verify/yosupo_library_checker/String/Z_Algorithm.test.py
- /verify/test_verify/yosupo_library_checker/String/Z_Algorithm.test.py.html
title: test_verify/yosupo_library_checker/String/Z_Algorithm.test.py
---
