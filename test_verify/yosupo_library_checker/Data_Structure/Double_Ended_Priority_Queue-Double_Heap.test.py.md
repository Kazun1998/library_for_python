---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Double_Heap.py
    title: Double_Heap.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/double_ended_priority_queue
    links:
    - https://judge.yosupo.jp/problem/double_ended_priority_queue
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.6/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.6/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/double_ended_priority_queue\n\
    \n#==================================================\nfrom Double_Heap import\
    \ *\n\nimport sys\ninput=sys.stdin.readline\nwrite=sys.stdout.write\n\n#==================================================\n\
    def verify():\n    N,Q=map(int,input().split())\n    S=map(int,input().split())\n\
    \n    H=Double_Heap()\n    for a in S:\n        H.push(a)\n\n    Ans=[]\n    for\
    \ _ in range(Q):\n        mode,*value=map(int,input().split())\n        if mode==0:\n\
    \            H.push(value[0])\n        elif mode==1:\n            Ans.append(H.pop_min())\n\
    \        else:\n            Ans.append(H.pop_max())\n    write(\"\\n\".join(map(str,Ans)))\n\
    \n#==================================================\nverify()\n"
  dependsOn:
  - Double_Heap.py
  isVerificationFile: true
  path: test_verify/yosupo_library_checker/Data_Structure/Double_Ended_Priority_Queue-Double_Heap.test.py
  requiredBy: []
  timestamp: '2022-12-11 17:04:31+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test_verify/yosupo_library_checker/Data_Structure/Double_Ended_Priority_Queue-Double_Heap.test.py
layout: document
redirect_from:
- /verify/test_verify/yosupo_library_checker/Data_Structure/Double_Ended_Priority_Queue-Double_Heap.test.py
- /verify/test_verify/yosupo_library_checker/Data_Structure/Double_Ended_Priority_Queue-Double_Heap.test.py.html
title: test_verify/yosupo_library_checker/Data_Structure/Double_Ended_Priority_Queue-Double_Heap.test.py
---
