---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test_verify/yosupo_library_checker/String/Z_Algorithm.test.py
    title: test_verify/yosupo_library_checker/String/Z_Algorithm.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "#Z-Algorithm\ndef Z_Algorithm(S):\n    \"\"\" i=0,1,...,|S|-1 \u306B\u5BFE\
    \u3057\u3066, S[i...] \u3068 S \u306E\u5148\u982D\u4F55\u6587\u5B57\u304C\u4E00\
    \u81F4\u3057\u3066\u3044\u308B\u304B\u3092\u8868\u3059\u30EA\u30B9\u30C8\u3092\
    \u8FD4\u3059.\n\n    S: string\n    \"\"\"\n    N=len(S)\n    Z=[0]*N\n    i,j=1,0\n\
    \    Z[0]=N\n    while i<N:\n        while i+j <N and S[j] == S[i+j]:\n      \
    \      j+=1\n\n        if not j:\n            i+=1\n            continue\n\n \
    \       Z[i] = j\n        k = 1\n        while N-i>k<j-Z[k]:\n            Z[i+k]=Z[k]\n\
    \            k+=1\n        i+=k\n        j-=k\n    return Z\n"
  dependsOn: []
  isVerificationFile: false
  path: Sequence/Z_Algorithm.py
  requiredBy: []
  timestamp: '2022-11-26 03:55:08+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test_verify/yosupo_library_checker/String/Z_Algorithm.test.py
documentation_of: Sequence/Z_Algorithm.py
layout: document
redirect_from:
- /library/Sequence/Z_Algorithm.py
- /library/Sequence/Z_Algorithm.py.html
title: Sequence/Z_Algorithm.py
---
