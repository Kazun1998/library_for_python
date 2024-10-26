---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Sliding_Window_Aggregation.py
    title: Sliding_Window_Aggregation.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/queue_operate_all_composite
    links:
    - https://judge.yosupo.jp/problem/queue_operate_all_composite
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.7/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.7/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/queue_operate_all_composite\n\
    \n#==================================================\nfrom Sliding_Window_Aggregation\
    \ import *\n\nimport sys\ninput=sys.stdin.readline\nwrite=sys.stdout.write\n\n\
    #==================================================\ndef verify():\n    Q=int(input())\n\
    \n    Mod=998244353\n    def calc(f,g):\n        return (f[0]*g[0]%Mod, (f[1]*g[0]+g[1])%Mod)\n\
    \n    S=Sliding_Window_Aggregation(calc)\n    X=[]\n    for _ in range(Q):\n \
    \       mode,*query=map(int,input().split())\n        if mode==0:\n          \
    \  S.push(query)\n        elif mode==1:\n            S.pop()\n        else:\n\
    \            a,b=S.product([1,0])\n            X.append((a*query[0]+b)%Mod)\n\n\
    \    write(\"\\n\".join(map(str,X)))\n\n\n#==================================================\n\
    verify()\n"
  dependsOn:
  - Sliding_Window_Aggregation.py
  isVerificationFile: true
  path: test_verify/yosupo_library_checker/Data_Structure/Queue_Operate_All_Composite.test.py
  requiredBy: []
  timestamp: '2023-08-03 01:41:13+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test_verify/yosupo_library_checker/Data_Structure/Queue_Operate_All_Composite.test.py
layout: document
redirect_from:
- /verify/test_verify/yosupo_library_checker/Data_Structure/Queue_Operate_All_Composite.test.py
- /verify/test_verify/yosupo_library_checker/Data_Structure/Queue_Operate_All_Composite.test.py.html
title: test_verify/yosupo_library_checker/Data_Structure/Queue_Operate_All_Composite.test.py
---
