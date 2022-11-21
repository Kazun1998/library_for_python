---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Segment_Tree/Dual_Segment_Tree.py
    title: Dual Segment Tree
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/range_affine_point_get
    links:
    - https://judge.yosupo.jp/problem/range_affine_point_get
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/range_affine_point_get\n\
    \n#==================================================\nimport sys\nfrom  Segment_Tree.Dual_Segment_Tree\
    \ import Dual_Segment_Tree\n\ninput=sys.stdin.readline\nwrite=sys.stdout.write\n\
    \n#==================================================\ndef verify():\n    def\
    \ comp(g,f):\n        f0=f>>bit; f1=f&msk\n        g0=g>>bit; g1=g&msk\n\n   \
    \     h0=(g0+g1*f0)%Mod\n        h1=(f1*g1)%Mod\n        return (h0<<bit)+h1\n\
    \n    N,Q=map(int,input().split())\n    A=list(map(int,input().split()))\n\n \
    \   Mod=998244353\n    bit=32; msk=(1<<bit)-1\n    D=Dual_Segment_Tree([a<<bit\
    \ for a in A],comp,1)\n\n    Ans=[]\n    for q in range(Q):\n        mode,*query=map(int,input().split())\n\
    \        if mode==0:\n            l,r,b,c=query\n            D.operate(l,r,(c<<bit)+b,True,False)\n\
    \        else:\n            Ans.append(D[query[0]]>>bit)\n\n    write(\"\\n\"\
    .join(map(str,Ans)))\n\n#==================================================\n\
    verify()\n"
  dependsOn:
  - Segment_Tree/Dual_Segment_Tree.py
  isVerificationFile: true
  path: test_verify/Dual_Segment_Tree.test.py
  requiredBy: []
  timestamp: '2022-11-22 04:43:14+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test_verify/Dual_Segment_Tree.test.py
layout: document
redirect_from:
- /verify/test_verify/Dual_Segment_Tree.test.py
- /verify/test_verify/Dual_Segment_Tree.test.py.html
title: test_verify/Dual_Segment_Tree.test.py
---
