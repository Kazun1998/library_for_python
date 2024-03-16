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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.2/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.2/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def Subset_Sum_Zero_One_Decision(A, S):\n    \"\"\" A \u306E\u591A\u91CD\u90E8\
    \u5206\u96C6\u5408\u3067, \u548C\u304C S \u306B\u306A\u308B (0, 1) \u5217\u306E\
    \u4F8B\u3092\u6C42\u3081\u308B.\n\n    \u8A08\u7B97\u91CF: O(|A| S)\n    \"\"\"\
    \n\n    DP = [False] * (S + 1); DP[0] = True\n    DP_prev = [False] * (S + 1)\n\
    \n    for a in A:\n        DP_prev, DP = DP, DP_prev\n        for x in range(S\
    \ + 1):\n            DP[x] = DP_prev[x]\n\n        for y in range(S, a - 1, -1):\n\
    \            DP[y] |= DP_prev[y - a]\n\n    return DP[S]\n\ndef Subset_Sum_Plus_Minus_One_Decision(A,\
    \ K):\n    \"\"\" \u4EE5\u4E0B\u3092\u6E80\u305F\u3059 A \u306E\u5206\u5272 X,\
    \ Y \u306E\u500B\u6570\u3092\u6C42\u3081\u308B: sum(X) - sum(Y) = K.\n\n    \u8A08\
    \u7B97\u91CF: O(|A|(sum(A)+K))\n    \"\"\"\n\n    B = list(map(abs, A))\n\n  \
    \  L = K + sum(B)\n    return (L >= 0) and (L % 2 == 0) and Subset_Sum_Zero_One_Decision(B,\
    \ L // 2)\n"
  dependsOn: []
  isVerificationFile: false
  path: Subset_Sum/Decision.py
  requiredBy: []
  timestamp: '2024-03-16 13:19:13+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Subset_Sum/Decision.py
layout: document
redirect_from:
- /library/Subset_Sum/Decision.py
- /library/Subset_Sum/Decision.py.html
title: Subset_Sum/Decision.py
---
