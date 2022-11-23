---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Slide_Window.py
    title: Slide_Window.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/queue_operate_all_composite
    links:
    - https://judge.yosupo.jp/problem/queue_operate_all_composite
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/queue_operate_all_composite\n\
    \n#==================================================\nfrom Slide_Window import\
    \ *\n\nimport sys\ninput=sys.stdin.readline\nwrite=sys.stdout.write\n\n#==================================================\n\
    def verify():\n    Q=int(input())\n\n    Mod=998244353\n    def calc(f,g):\n \
    \       return (f[0]*g[0]%Mod, (f[1]*g[0]+g[1])%Mod)\n\n    S=Slide_Window(calc)\n\
    \    X=[]\n    for _ in range(Q):\n        mode,*query=map(int,input().split())\n\
    \        if mode==0:\n            S.push(query)\n        elif mode==1:\n     \
    \       S.pop()\n        else:\n            a,b=S.product([1,0])\n           \
    \ X.append((a*query[0]+b)%Mod)\n\n    write(\"\\n\".join(map(str,X)))\n\n\n#==================================================\n\
    verify()\n"
  dependsOn:
  - Slide_Window.py
  isVerificationFile: true
  path: test_verify/yosupo_library_checker/Data_Structure/Queue_Operate_All_Composite.test.py
  requiredBy: []
  timestamp: '2022-11-23 17:03:27+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test_verify/yosupo_library_checker/Data_Structure/Queue_Operate_All_Composite.test.py
layout: document
redirect_from:
- /verify/test_verify/yosupo_library_checker/Data_Structure/Queue_Operate_All_Composite.test.py
- /verify/test_verify/yosupo_library_checker/Data_Structure/Queue_Operate_All_Composite.test.py.html
title: test_verify/yosupo_library_checker/Data_Structure/Queue_Operate_All_Composite.test.py
---
