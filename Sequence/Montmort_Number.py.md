---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test_verify/yosupo_library_checker/Math/Montmort_Number.test.py
    title: test_verify/yosupo_library_checker/Math/Montmort_Number.test.py
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
  code: "def Montmort_Number(N, Mod=None):\n    \"\"\" k=0,1,...,N \u306B\u95A2\u3057\
    \u3066, k \u8981\u7D20\u64B9\u4E71\u9806\u5217\u306E\u500B\u6570\u3092\u6C42\u3081\
    \u308B.\n    \"\"\"\n    if N<0:\n        return []\n    elif N==0:\n        return\
    \ [0]\n    elif N==1:\n        return [0,0]\n    elif Mod==1:\n        return\
    \ [0]*(N+1)\n\n    X=[0]*(N+1)\n    if Mod==None:\n        X[2]=1\n        for\
    \ k in range(3,N+1):\n            X[k]=(k-1)*(X[k-1]+X[k-2])\n    else:\n    \
    \    X[2]=1%Mod\n        for k in range(3,N+1):\n            X[k]=(k-1)*(X[k-1]+X[k-2])%Mod\n\
    \n    return X\n\n"
  dependsOn: []
  isVerificationFile: false
  path: Sequence/Montmort_Number.py
  requiredBy: []
  timestamp: '2022-11-25 04:01:22+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test_verify/yosupo_library_checker/Math/Montmort_Number.test.py
documentation_of: Sequence/Montmort_Number.py
layout: document
redirect_from:
- /library/Sequence/Montmort_Number.py
- /library/Sequence/Montmort_Number.py.html
title: Sequence/Montmort_Number.py
---
