---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Sequence/Montmort_Number.py
    title: Montmort Number
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/montmort_number_mod
    links:
    - https://judge.yosupo.jp/problem/montmort_number_mod
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.2/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.2/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/montmort_number_mod\n\
    \n#==================================================\nfrom Sequence.Montmort_Number\
    \ import *\n\nimport sys\ninput=sys.stdin.readline\nwrite=sys.stdout.write\n\n\
    #==================================================\ndef verify():\n    N,M=map(int,input().split())\n\
    \    write(\" \".join(map(str, Montmort_Number(N,M)[1:])))\n\n#==================================================\n\
    verify()\n"
  dependsOn:
  - Sequence/Montmort_Number.py
  isVerificationFile: true
  path: test_verify/yosupo_library_checker/Math/Montmort_Number.test.py
  requiredBy: []
  timestamp: '2022-11-25 11:47:07+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test_verify/yosupo_library_checker/Math/Montmort_Number.test.py
layout: document
redirect_from:
- /verify/test_verify/yosupo_library_checker/Math/Montmort_Number.test.py
- /verify/test_verify/yosupo_library_checker/Math/Montmort_Number.test.py.html
title: test_verify/yosupo_library_checker/Math/Montmort_Number.test.py
---
