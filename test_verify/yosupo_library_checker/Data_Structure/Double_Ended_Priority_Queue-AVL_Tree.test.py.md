---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: AVL_Tree.py
    title: AVL_Tree.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/double_ended_priority_queue
    links:
    - https://judge.yosupo.jp/problem/double_ended_priority_queue
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/double_ended_priority_queue\n\
    \n#==================================================\nfrom AVL_Tree import *\n\
    \nimport sys\ninput=sys.stdin.readline\nwrite=sys.stdout.write\n\n#==================================================\n\
    def verify():\n    N,Q=map(int,input().split())\n    S=map(int,input().split())\n\
    \n    E=Adelson_Velsky_and_Landis_Tree()\n    for a in S:\n        E[a]=E.get(a,0)+1\n\
    \n    Ans=[]\n    for _ in range(Q):\n        mode,*value=map(int,input().split())\n\
    \        if mode==0:\n            x=value[0]\n            E[x]=E.get(x,0)+1\n\
    \        elif mode==1:\n            y=E.get_min()\n            E[y]-=1\n     \
    \       if E[y]==0:\n                E.delete(y)\n            Ans.append(y)\n\
    \        elif mode==2:\n            z=E.get_max()\n            E[z]-=1\n     \
    \       if E[z]==0:\n                E.delete(z)\n            Ans.append(z)\n\
    \    write(\"\\n\".join(map(str,Ans)))\n\n#==================================================\n\
    verify()\n"
  dependsOn:
  - AVL_Tree.py
  isVerificationFile: true
  path: test_verify/yosupo_library_checker/Data_Structure/Double_Ended_Priority_Queue-AVL_Tree.test.py
  requiredBy: []
  timestamp: '2022-12-13 00:25:57+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test_verify/yosupo_library_checker/Data_Structure/Double_Ended_Priority_Queue-AVL_Tree.test.py
layout: document
redirect_from:
- /verify/test_verify/yosupo_library_checker/Data_Structure/Double_Ended_Priority_Queue-AVL_Tree.test.py
- /verify/test_verify/yosupo_library_checker/Data_Structure/Double_Ended_Priority_Queue-AVL_Tree.test.py.html
title: test_verify/yosupo_library_checker/Data_Structure/Double_Ended_Priority_Queue-AVL_Tree.test.py
---
