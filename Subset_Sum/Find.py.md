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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.6/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.6/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def Subset_Sum_Zero_One_Find(A, S):\n    \"\"\" A \u306E\u591A\u91CD\u90E8\
    \u5206\u96C6\u5408\u3067, \u548C\u304C S \u306B\u306A\u308B (0, 1) \u5217\u306E\
    \u4F8B\u3092\u6C42\u3081\u308B.\n\n    \u8A08\u7B97\u91CF: O(|A| S)\n    \"\"\"\
    \n\n    N = len(A)\n    DP = [[False]* (S + 1) for _ in range(N + 1)]; DP[0][0]\
    \ = True\n\n    for i, a in enumerate(A, 1):\n        DP_i = DP[i]; DP_prev =\
    \ DP[i - 1]\n        for x in range(S, a - 1, -1):\n            DP_i[x] = DP_prev[x]\
    \ | DP_prev[x - a]\n        for x in range(a - 1, -1, -1):\n            DP_i[x]\
    \ = DP_prev[x]\n\n    if not DP[N][S]:\n        return None\n\n    signs = []\n\
    \    pointer = S\n    for i, a in reversed(list(enumerate(A, 1))):\n        DP_prev\
    \ = DP[i - 1]\n        if (pointer >= a) and DP_prev[pointer - a]:\n         \
    \   signs.append(1)\n            pointer -= a\n        else:\n            signs.append(0)\n\
    \n    signs.reverse()\n    return signs\n\ndef Subset_Sum_Plus_Minus_One_Find(A,\
    \ K):\n    \"\"\" \u4EE5\u4E0B\u3092\u6E80\u305F\u3059 A \u306E\u5206\u5272 X,\
    \ Y \u306E\u500B\u6570\u3092\u6C42\u3081\u308B: sum(X) - sum(Y) = K.\n\n    \u8A08\
    \u7B97\u91CF: O(|A|(sum(A)+K))\n    \"\"\"\n\n    p = [1 if a >= 0 else -1 for\
    \ a in A]\n    B = list(map(abs, A))\n\n    L = K + sum(B)\n    if (L < 0) or\
    \ (L % 2 == 1):\n        return None\n\n    signs = Subset_Sum_Zero_One_Find(B,\
    \ L // 2)\n    if signs is not None:\n        return [p[i] * (2 * s - 1) for i,\
    \ s in enumerate(signs)]\n    else:\n        return None\n"
  dependsOn: []
  isVerificationFile: false
  path: Subset_Sum/Find.py
  requiredBy: []
  timestamp: '2024-03-16 12:35:35+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Subset_Sum/Find.py
layout: document
redirect_from:
- /library/Subset_Sum/Find.py
- /library/Subset_Sum/Find.py.html
title: Subset_Sum/Find.py
---
