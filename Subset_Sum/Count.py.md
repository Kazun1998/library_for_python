---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.3/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.3/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def Subset_Sum_Zero_One_Count(A, S, Mod = None):\n    \"\"\" A \u306E\u591A\
    \u91CD\u90E8\u5206\u96C6\u5408\u3067, \u548C\u304C s (0 <= s <= S) \u306B\u306A\
    \u308B\u6570\u3092\u6C42\u3081\u308B.\n\n    Mod: \u4F59\u308A (None \u306E\u3068\
    \u304D\u306F\u4F59\u308A\u3092\u53D6\u3089\u306A\u3044)\n\n    \u8A08\u7B97\u91CF\
    : O(|A| S)\n    \"\"\"\n\n    DP = [0] * (S + 1); DP[0] = 1\n\n    for a in A:\n\
    \        for x in range(S, a - 1, -1):\n            DP[x] += DP[x - a]\n\n   \
    \     if Mod is not None:\n            for x in range(a, S + 1):\n           \
    \     DP[x] %= Mod\n\n    return DP\n\ndef Subset_Sum_Plus_Minus_One_Count(A,\
    \ K, Mod = None):\n    \"\"\" \u4EE5\u4E0B\u3092\u6E80\u305F\u3059 A \u306E\u5206\
    \u5272 X, Y \u306E\u500B\u6570\u3092\u6C42\u3081\u308B: sum(X) - sum(Y) = K.\n\
    \n    \u8A08\u7B97\u91CF: O(|A|(sum(A)+K))\n    \"\"\"\n\n    A = list(map(abs,\
    \ A))\n\n    L = K + sum(A)\n    if (L < 0) or (L % 2 == 1):\n        return 0\n\
    \n    return Subset_Sum_Zero_One_Count(A, L // 2, Mod)[-1]\n"
  dependsOn: []
  isVerificationFile: false
  path: Subset_Sum/Count.py
  requiredBy: []
  timestamp: '2024-03-16 12:35:18+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Subset_Sum/Count.py
layout: document
redirect_from:
- /library/Subset_Sum/Count.py
- /library/Subset_Sum/Count.py.html
title: Subset_Sum/Count.py
---
