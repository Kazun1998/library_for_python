---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Modulo_Matrix/Modulo_Matrix.py
    title: Modulo_Matrix
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/inverse_matrix
    links:
    - https://judge.yosupo.jp/problem/inverse_matrix
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.2/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.2/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/inverse_matrix\n\
    \n#==================================================\nimport sys\nsys.path.append(\"\
    ../../../\")\nfrom Modulo_Matrix.Modulo_Matrix import *\n\nimport sys\ninput=sys.stdin.readline\n\
    write=sys.stdout.write\n\n#==================================================\n\
    def verify():\n    N=int(input())\n    A=[None]*N\n\n    for i in range(N):\n\
    \        A[i]=list(map(int,input().split()))\n\n    try:\n        B=Modulo_Matrix(A).inverse()\n\
    \        string=lambda x:\" \".join(map(str,x))\n        write(\"\\n\".join(map(string,B.ele)))\n\
    \    except:\n        print(-1)\n\n#==================================================\n\
    verify()"
  dependsOn:
  - Modulo_Matrix/Modulo_Matrix.py
  isVerificationFile: true
  path: test_verify/yosupo_library_checker/Matrix/Inverse.test.py
  requiredBy: []
  timestamp: '2024-03-24 13:46:48+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test_verify/yosupo_library_checker/Matrix/Inverse.test.py
layout: document
redirect_from:
- /verify/test_verify/yosupo_library_checker/Matrix/Inverse.test.py
- /verify/test_verify/yosupo_library_checker/Matrix/Inverse.test.py.html
title: test_verify/yosupo_library_checker/Matrix/Inverse.test.py
---
