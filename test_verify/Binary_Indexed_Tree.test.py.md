---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/point_add_range_sum
    links:
    - https://judge.yosupo.jp/problem/point_add_range_sum
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.8/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.8/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/point_add_range_sum\n\
    \nfrom Binary_Indexed_Tree.Binary_Indexed_Tree import Binary_Indexed_Tree\n\n\
    import sys\ninput=sys.stdin.readline\nwrite=sys.stdout.write\n\n#==================================================\n\
    def verify():\n    from operator import add,neg\n\n    N,Q=map(int,input().split())\n\
    \    A=list(map(int,input().split()))\n    B=Binary_Indexed_Tree(A,add,0,neg)\n\
    \n    Ans=[]\n    for q in range(Q):\n        mode,*query=map(int,input().split())\n\
    \n        if mode==0:\n            p,x=query\n            B.add(p,x)\n       \
    \ else:\n            l,r=query\n            Ans.append(B.sum(l,r-1))\n\n    write(\"\
    \\n\".join(map(str,Ans)))\n\n#==================================================\n\
    verify()\n"
  dependsOn: []
  isVerificationFile: true
  path: test_verify/Binary_Indexed_Tree.test.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test_verify/Binary_Indexed_Tree.test.py
layout: document
redirect_from:
- /verify/test_verify/Binary_Indexed_Tree.test.py
- /verify/test_verify/Binary_Indexed_Tree.test.py.html
title: test_verify/Binary_Indexed_Tree.test.py
---
