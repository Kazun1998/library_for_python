---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Segment_Tree/Segment_Tree.py
    title: Segment Tree
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/point_set_range_composite
    links:
    - https://judge.yosupo.jp/problem/point_set_range_composite
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/point_set_range_composite\n\
    \n#==================================================\nfrom Segment_Tree.Segment_Tree\
    \ import Segment_Tree\n\nimport sys\ninput=sys.stdin.readline\nwrite=sys.stdout.write\n\
    \n#==================================================\ndef verify():\n    N,Q=map(int,input().split())\n\
    \    Mod=998244353\n\n    A=[0]*N\n    for i in range(N):\n        a,b=map(int,input().split())\n\
    \        A[i]=(a,b)\n\n    calc=lambda p,q:((p[0]*q[0])%Mod,(p[1]*q[0]+q[1])%Mod)\n\
    \    S=Segment_Tree(A,calc,(1,0))\n\n    Ans=[]\n    for _ in range(Q):\n    \
    \    m,s,t,u=map(int,input().split())\n        if m==0:\n            S.update(s,(t,u))\n\
    \        else:\n            (alpha,beta)=S.product(s,t-1)\n            Ans.append((alpha*u+beta)%Mod)\n\
    \n    write(\"\\n\".join(map(str,Ans)))\n\n#==================================================\n\
    verify()\n"
  dependsOn:
  - Segment_Tree/Segment_Tree.py
  isVerificationFile: true
  path: test_verify/yosupo_library_checker/Data_Structure/Segment_Tree.test.py
  requiredBy: []
  timestamp: '2022-12-06 20:56:01+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test_verify/yosupo_library_checker/Data_Structure/Segment_Tree.test.py
layout: document
redirect_from:
- /verify/test_verify/yosupo_library_checker/Data_Structure/Segment_Tree.test.py
- /verify/test_verify/yosupo_library_checker/Data_Structure/Segment_Tree.test.py.html
title: test_verify/yosupo_library_checker/Data_Structure/Segment_Tree.test.py
---
