---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Two_SAT.py
    title: 2-SAT
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/two_sat
    links:
    - https://judge.yosupo.jp/problem/two_sat
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.2/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.2/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/two_sat\n\n\
    #==================================================\nfrom Two_SAT import *\n\n\
    import sys\ninput=sys.stdin.readline\nwrite=sys.stdout.write\n\n#==================================================\n\
    def verify():\n    p,cnf,N,M=input().split()\n    N=int(N); M=int(M)\n\n    T=Two_SAT(N)\n\
    \    for _ in range(M):\n        a,b,zero=map(int,input().split())\n\n       \
    \ if a>0:\n            a=a-1\n        else:\n            a=~(-a-1)\n\n       \
    \ if b>0:\n            b=b-1\n        else:\n            b=~(-b-1)\n\n       \
    \ T.add_or(a,b)\n\n    X=T.is_satisfy(1)\n    if X:\n        print(\"s\",\"SATISFIABLE\"\
    )\n        V=[]\n        for i in range(N):\n            if X[i]:\n          \
    \      V.append(i+1)\n            else:\n                V.append(-(i+1))\n  \
    \      V.append(0)\n        print(\"v\",*V)\n    else:\n        print(\"s\",\"\
    UNSATISFIABLE\")\n\n#==================================================\nverify()"
  dependsOn:
  - Two_SAT.py
  isVerificationFile: true
  path: test_verify/yosupo_library_checker/Math/Two_Sat.test.py
  requiredBy: []
  timestamp: '2022-11-23 16:35:46+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test_verify/yosupo_library_checker/Math/Two_Sat.test.py
layout: document
redirect_from:
- /verify/test_verify/yosupo_library_checker/Math/Two_Sat.test.py
- /verify/test_verify/yosupo_library_checker/Math/Two_Sat.test.py.html
title: test_verify/yosupo_library_checker/Math/Two_Sat.test.py
---
