---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Segment_Tree/Lazy_Segment_Tree.py
    title: Lazy Segment Tree
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/range_affine_range_sum
    links:
    - https://judge.yosupo.jp/problem/range_affine_range_sum
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/range_affine_range_sum\n\
    \n#==================================================\nfrom Segment_Tree.Lazy_Segment_Tree\
    \ import Lazy_Evaluation_Tree\n\nimport sys\ninput=sys.stdin.readline\nwrite=sys.stdout.write\n\
    \n#==================================================\ndef verify():\n    def\
    \ calc(p,q):\n        a,x=p>>32,p&msk\n        b,y=q>>32,q&msk\n        return\
    \ ((a+b)%Mod<<32)+(x+y)\n\n    def op(u,p):\n        b,c=u>>32,u&msk\n       \
    \ a,x=p>>32,p&msk\n        return (((a*b+c*x)%Mod)<<32)+x\n\n    def comp(u,v):\n\
    \        b1,c1=u>>32,u&msk\n        b2,c2=v>>32,v&msk\n        return (((b1*b2)%Mod)<<32)+(b1*c2+c1)%Mod\n\
    \n    N,Q=map(int,input().split())\n    A=[(a<<32)+1 for a in map(int,input().split())]\n\
    \n    Mod=998244353\n    msk=(1<<32)-1\n    S=Lazy_Evaluation_Tree(A,calc,0,op,comp,1<<32)\n\
    \n    Ans=[]\n    for q in range(Q):\n        t,*query=map(int,input().split())\n\
    \        if t==0:\n            l,r,b,c=query\n            S.operate(l,r-1,(b<<32)+c)\n\
    \        else:\n            l,r=query\n            Ans.append(S.product(l,r-1)>>32)\n\
    \n    write(\"\\n\".join(map(str,Ans)))\n\n#==================================================\n\
    verify()\n"
  dependsOn:
  - Segment_Tree/Lazy_Segment_Tree.py
  isVerificationFile: true
  path: test_verify/yosupo_library_checker/Data_Structure/Lazy_Segment_Tree.test.py
  requiredBy: []
  timestamp: '2022-11-23 02:07:00+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test_verify/yosupo_library_checker/Data_Structure/Lazy_Segment_Tree.test.py
layout: document
redirect_from:
- /verify/test_verify/yosupo_library_checker/Data_Structure/Lazy_Segment_Tree.test.py
- /verify/test_verify/yosupo_library_checker/Data_Structure/Lazy_Segment_Tree.test.py.html
title: test_verify/yosupo_library_checker/Data_Structure/Lazy_Segment_Tree.test.py
---
