---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Sequence/Subsequence_Count.py
    title: Sequence/Subsequence_Count.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/number_of_subsequences
    links:
    - https://judge.yosupo.jp/problem/number_of_subsequences
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.8/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.8/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/number_of_subsequences\n\
    \n#==================================================\nfrom Sequence.Subsequence_Count\
    \ import *\n\nimport sys\ninput=sys.stdin.readline\nwrite=sys.stdout.write\n\n\
    #==================================================\ndef verify():\n    N=int(input())\n\
    \    A=list(map(int,input().split()))\n\n    Mod=998244353\n    print(Subsequence_Count(A,\
    \ Mod, False))\n\n#==================================================\nverify()\n"
  dependsOn:
  - Sequence/Subsequence_Count.py
  isVerificationFile: true
  path: test_verify/yosupo_library_checker/Data_Structure/Number_of_Subsequences.test.py
  requiredBy: []
  timestamp: '2022-11-26 05:09:30+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test_verify/yosupo_library_checker/Data_Structure/Number_of_Subsequences.test.py
layout: document
redirect_from:
- /verify/test_verify/yosupo_library_checker/Data_Structure/Number_of_Subsequences.test.py
- /verify/test_verify/yosupo_library_checker/Data_Structure/Number_of_Subsequences.test.py.html
title: test_verify/yosupo_library_checker/Data_Structure/Number_of_Subsequences.test.py
---
