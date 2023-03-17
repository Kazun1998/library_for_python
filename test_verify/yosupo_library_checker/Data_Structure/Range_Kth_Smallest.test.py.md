---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Wavelet_Matrix.py
    title: Wavelet Matrix
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/range_kth_smallest
    links:
    - https://judge.yosupo.jp/problem/range_kth_smallest
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.2/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.2/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/range_kth_smallest\n\
    \n#==================================================\nfrom Wavelet_Matrix import\
    \ *\n\nimport sys\ninput=sys.stdin.readline\nwrite=sys.stdout.write\n\n#==================================================\n\
    def verify():\n    N,Q=map(int,input().split())\n\n    A=list(map(int,input().split()))\n\
    \    W=Wavelet_Matrix(A)\n\n    Ans=[0]*Q\n\n    for q in range(Q):\n        l,r,k=map(int,input().split())\n\
    \        Ans[q]=W.quantile(l,r,k+1)\n\n    write(\"\\n\".join(map(str,Ans)))\n\
    \n\n#==================================================\nverify()\n"
  dependsOn:
  - Wavelet_Matrix.py
  isVerificationFile: true
  path: test_verify/yosupo_library_checker/Data_Structure/Range_Kth_Smallest.test.py
  requiredBy: []
  timestamp: '2022-11-23 16:55:38+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test_verify/yosupo_library_checker/Data_Structure/Range_Kth_Smallest.test.py
layout: document
redirect_from:
- /verify/test_verify/yosupo_library_checker/Data_Structure/Range_Kth_Smallest.test.py
- /verify/test_verify/yosupo_library_checker/Data_Structure/Range_Kth_Smallest.test.py.html
title: test_verify/yosupo_library_checker/Data_Structure/Range_Kth_Smallest.test.py
---
