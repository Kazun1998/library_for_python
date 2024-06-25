---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Ordered_Set/Ordered_Set.py
    title: Ordered_Set/Ordered_Set.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/predecessor_problem
    links:
    - https://judge.yosupo.jp/problem/predecessor_problem
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.4/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.4/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/predecessor_problem\n\
    \n#==================================================\nfrom Ordered_Set.Ordered_Set\
    \ import *\n\nimport sys\ninput=sys.stdin.readline\nwrite=sys.stdout.write\n\n\
    #==================================================\ndef verify():\n    N,Q=map(int,input().split())\n\
    \    T=list(map(int,input()[:-1]))\n\n    S=Ordered_Set(N,S=T)\n\n    Ans=[]\n\
    \    for q in range(Q):\n        c,k=map(int,input().split())\n        if c==0:\n\
    \            S.add(k)\n        elif c==1:\n            S.discard(k)\n        elif\
    \ c==2:\n            Ans.append(S.count(k))\n        elif c==3:\n            Ans.append(S.next(k))\n\
    \        else:\n            Ans.append(S.previous(k))\n\n    write(\"\\n\".join(map(str,Ans)))\n\
    \n\n#==================================================\nverify()\n"
  dependsOn:
  - Ordered_Set/Ordered_Set.py
  isVerificationFile: true
  path: test_verify/yosupo_library_checker/Data_Structure/Predecessor_Problem-Ordered_Set.test.py
  requiredBy: []
  timestamp: '2022-11-24 22:57:20+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test_verify/yosupo_library_checker/Data_Structure/Predecessor_Problem-Ordered_Set.test.py
layout: document
redirect_from:
- /verify/test_verify/yosupo_library_checker/Data_Structure/Predecessor_Problem-Ordered_Set.test.py
- /verify/test_verify/yosupo_library_checker/Data_Structure/Predecessor_Problem-Ordered_Set.test.py.html
title: test_verify/yosupo_library_checker/Data_Structure/Predecessor_Problem-Ordered_Set.test.py
---
