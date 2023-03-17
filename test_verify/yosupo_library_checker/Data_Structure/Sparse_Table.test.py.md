---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Sparse_Table.py
    title: Sparse Table
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/staticrmq
    links:
    - https://judge.yosupo.jp/problem/staticrmq
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.2/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.2/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/staticrmq\n\
    \n#==================================================\nimport sys\nfrom Sparse_Table\
    \ import Sparse_Table\n\nimport sys\ninput=sys.stdin.readline\nwrite=sys.stdout.write\n\
    #==================================================\ndef verify():\n    N,Q=map(int,input().split())\n\
    \    A=list(map(int,input().split()))\n\n    S=Sparse_Table(A,min)\n    Ans=[0]*Q\n\
    \    for q in range(Q):\n        l,r=map(int,input().split())\n        Ans[q]=S.product(l,r,None,True,False)\n\
    \n    write(\"\\n\".join(map(str,Ans)))\n\n#==================================================\n\
    verify()\n"
  dependsOn:
  - Sparse_Table.py
  isVerificationFile: true
  path: test_verify/yosupo_library_checker/Data_Structure/Sparse_Table.test.py
  requiredBy: []
  timestamp: '2022-12-18 03:53:02+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test_verify/yosupo_library_checker/Data_Structure/Sparse_Table.test.py
layout: document
redirect_from:
- /verify/test_verify/yosupo_library_checker/Data_Structure/Sparse_Table.test.py
- /verify/test_verify/yosupo_library_checker/Data_Structure/Sparse_Table.test.py.html
title: test_verify/yosupo_library_checker/Data_Structure/Sparse_Table.test.py
---
