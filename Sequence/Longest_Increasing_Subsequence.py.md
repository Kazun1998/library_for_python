---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':x:'
    path: test_verify/yosupo_library_checker/Data_Structure/Longest_Increasing_Subsequence.test.py
    title: test_verify/yosupo_library_checker/Data_Structure/Longest_Increasing_Subsequence.test.py
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.7/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.7/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def Longest_Increasing_Subsequence(A, equal = False):\n    \"\"\" A \u306B\
    \u5BFE\u3059\u308B LIS (\u6700\u5927\u72ED\u7FA9\u5358\u8ABF\u5897\u52A0\u5217\
    ) \u3092\u6C42\u3081\u308B\n\n    Args:\n        A (list): \u5217\n        equal\
    \ (bool, optional): True \u306B\u3059\u308B\u3068, LIS \u306E\u6761\u4EF6\u304C\
    \u6700\u5927\u5E83\u7FA9\u5358\u8ABF\u5897\u52A0\u5217\u306B\u306A\u308B. Defaults\
    \ to False.\n\n    Returns:\n        dict:\n            length: \u6700\u5927\u5358\
    \u8ABF\u5897\u52A0\u5217\u306E\u9577\u3055\n            example: \u6700\u5927\u5358\
    \u8ABF\u5897\u52A0\u5217\u306E\u4F8B\n            index: example \u306B\u304A\u3044\
    \u3066\u305D\u308C\u305E\u308C\u306E\u9805\u3092\u6301\u3063\u3066\u304D\u305F\
    \u30A4\u30F3\u30C7\u30C3\u30AF\u30B9\n    \"\"\"\n    if equal:\n        from\
    \ bisect import bisect_right as bis\n    else:\n        from bisect import bisect_left\
    \ as bis\n\n    L = []\n    ind = [0] * len(A)\n\n    for i, a in enumerate(A):\n\
    \        k = bis(L,a)\n        if k == len(L):\n            L.append(a)\n    \
    \    else:\n            L[k] = a\n\n        ind[i]=k\n\n    X = []\n    I = []\n\
    \    j = len(L)-1\n    for i in range(len(A) - 1, -1, -1):\n        if ind[i]\
    \ == j:\n            j -= 1\n            X.append(A[i])\n            I.append(i)\n\
    \n    X.reverse(); I.reverse()\n    return { 'length': len(X), 'example': X, 'index':\
    \ I }"
  dependsOn: []
  isVerificationFile: false
  path: Sequence/Longest_Increasing_Subsequence.py
  requiredBy: []
  timestamp: '2024-08-31 23:52:58+09:00'
  verificationStatus: LIBRARY_ALL_WA
  verifiedWith:
  - test_verify/yosupo_library_checker/Data_Structure/Longest_Increasing_Subsequence.test.py
documentation_of: Sequence/Longest_Increasing_Subsequence.py
layout: document
redirect_from:
- /library/Sequence/Longest_Increasing_Subsequence.py
- /library/Sequence/Longest_Increasing_Subsequence.py.html
title: Sequence/Longest_Increasing_Subsequence.py
---
