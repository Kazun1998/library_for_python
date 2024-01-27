---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Sorted_Set/Sorted_Multiset.py
    title: Sorted_Set/Sorted_Multiset.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/double_ended_priority_queue
    links:
    - https://judge.yosupo.jp/problem/double_ended_priority_queue
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.1/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.1/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/double_ended_priority_queue\n\
    \n#==================================================\nfrom Sorted_Set.Sorted_Multiset\
    \ import *\n\nimport sys\ninput=sys.stdin.readline\nwrite=sys.stdout.write\n\n\
    #==================================================\ndef verify():\n    N,Q=map(int,input().split())\n\
    \    S=list(map(int,input().split()))\n\n    S=Sorted_Multiset(S)\n    Ans=[]\n\
    \    for _ in range(Q):\n        mode,*value=map(int,input().split())\n      \
    \  if mode==0:\n            S.add(value[0])\n        elif mode==1:\n         \
    \   Ans.append(S.pop_min())\n        else:\n            Ans.append(S.pop_max())\n\
    \    write(\"\\n\".join(map(str,Ans)))\n\n#==================================================\n\
    verify()\n"
  dependsOn:
  - Sorted_Set/Sorted_Multiset.py
  isVerificationFile: true
  path: test_verify/yosupo_library_checker/Data_Structure/Double_Ended_Priority_Queue-Sorted_Multiset.test.py
  requiredBy: []
  timestamp: '2023-06-18 16:03:57+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test_verify/yosupo_library_checker/Data_Structure/Double_Ended_Priority_Queue-Sorted_Multiset.test.py
layout: document
redirect_from:
- /verify/test_verify/yosupo_library_checker/Data_Structure/Double_Ended_Priority_Queue-Sorted_Multiset.test.py
- /verify/test_verify/yosupo_library_checker/Data_Structure/Double_Ended_Priority_Queue-Sorted_Multiset.test.py.html
title: test_verify/yosupo_library_checker/Data_Structure/Double_Ended_Priority_Queue-Sorted_Multiset.test.py
---
