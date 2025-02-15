---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Sequence/Longest_Increasing_Subsequence.py
    title: Sequence/Longest_Increasing_Subsequence.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/longest_increasing_subsequence
    links:
    - https://judge.yosupo.jp/problem/longest_increasing_subsequence
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.13.2/x64/lib/python3.13/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.13.2/x64/lib/python3.13/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/longest_increasing_subsequence\n\
    \n#==================================================\nfrom Sequence.Longest_Increasing_Subsequence\
    \ import *\n\nimport sys\ninput = sys.stdin.readline\nwrite = sys.stdout.write\n\
    \n#==================================================\ndef verify():\n    N =\
    \ int(input())\n    A = list(map(int, input().split()))\n\n    res =Longest_Increasing_Subsequence(A,\
    \ equal = False)\n\n    print(res['length'])\n    write(\" \".join(map(str, res['index'])))\n\
    \n#==================================================\nverify()\n"
  dependsOn:
  - Sequence/Longest_Increasing_Subsequence.py
  isVerificationFile: true
  path: test_verify/yosupo_library_checker/Data_Structure/Longest_Increasing_Subsequence.test.py
  requiredBy: []
  timestamp: '2024-12-01 02:14:44+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test_verify/yosupo_library_checker/Data_Structure/Longest_Increasing_Subsequence.test.py
layout: document
redirect_from:
- /verify/test_verify/yosupo_library_checker/Data_Structure/Longest_Increasing_Subsequence.test.py
- /verify/test_verify/yosupo_library_checker/Data_Structure/Longest_Increasing_Subsequence.test.py.html
title: test_verify/yosupo_library_checker/Data_Structure/Longest_Increasing_Subsequence.test.py
---
