---
data:
  _extendedDependsOn:
  - icon: ':x:'
    path: Disjoint_Sparse_Table.py
    title: Disjoint Sparse Table
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/staticrmq
    links:
    - https://judge.yosupo.jp/problem/staticrmq
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/staticrmq\n\
    \n#==================================================\nimport sys\n#sys.path.append('../')\n\
    from Disjoint_Sparse_Table import Disjoint_Sparse_Table\n\nimport sys\ninput=sys.stdin.readline\n\
    write=sys.stdout.write\n#==================================================\n\
    def verify():\n    N,Q=map(int,input().split())\n    A=list(map(int,input().split()))\n\
    \n    D=Disjoint_Sparse_Table(A,min)\n    Ans=[0]*Q\n    for q in range(Q):\n\
    \        l,r=map(int,input().split())\n        Ans[q]=D.product(l,r,None,True,False)\n\
    \n    write(\"\\n\".join(map(str,Ans)))\n\n#==================================================\n\
    verify()\n"
  dependsOn:
  - Disjoint_Sparse_Table.py
  isVerificationFile: true
  path: test_verify/Disjoint_Sparse_Table.test.py
  requiredBy: []
  timestamp: '2022-11-22 04:31:41+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: test_verify/Disjoint_Sparse_Table.test.py
layout: document
redirect_from:
- /verify/test_verify/Disjoint_Sparse_Table.test.py
- /verify/test_verify/Disjoint_Sparse_Table.test.py.html
title: test_verify/Disjoint_Sparse_Table.test.py
---
