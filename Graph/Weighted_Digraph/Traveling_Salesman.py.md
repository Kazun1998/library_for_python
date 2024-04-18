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
  code: "from Weighted_Digraph import *\n\ndef Traveling_Salesman(D: Weigthed_Digraph,\
    \ default = -1):\n    \"\"\" \u5DE1\u56DE\u30BB\u30FC\u30EB\u30B9\u30DE\u30F3\u554F\
    \u984C\u3092\u89E3\u304F\n\n    Args:\n        D (Weigthed_Digraph)\n    \"\"\"\
    \n\n    N = D.order()\n\n    dp = [[default] * N for _ in range(1 << N)]\n   \
    \ dp[0][0] = 0\n\n    bit = lambda S, k: (S >> k) & 1\n\n    for S in range(1\
    \ << N):\n        dp_S = dp[S]\n        for x in range(N):\n            if bit(S,\
    \ x):\n                continue\n\n            dp_T = dp[S | (1 << x)]\n     \
    \       for y, w, _ in D.adjacent_in[x]:\n                if dp_S[y] == default:\n\
    \                    continue\n                elif dp_T[x] == default:\n    \
    \                dp_T[x] = dp_S[y] + w\n                else:\n              \
    \      dp_T[x] = min(dp_T[x], dp_S[y] + w)\n    return dp[-1][0]\n"
  dependsOn: []
  isVerificationFile: false
  path: Graph/Weighted_Digraph/Traveling_Salesman.py
  requiredBy: []
  timestamp: '2024-02-25 12:52:08+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Graph/Weighted_Digraph/Traveling_Salesman.py
layout: document
redirect_from:
- /library/Graph/Weighted_Digraph/Traveling_Salesman.py
- /library/Graph/Weighted_Digraph/Traveling_Salesman.py.html
title: Graph/Weighted_Digraph/Traveling_Salesman.py
---
