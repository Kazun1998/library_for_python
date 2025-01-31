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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.13.1/x64/lib/python3.13/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.13.1/x64/lib/python3.13/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from Graph import *\n\ndef Chromatic_Number(G: Graph):\n    \"\"\" G \u306E\
    \u5F69\u8272\u6570\u3092\u6C42\u3081\u308B.\n\n    Args:\n        G (Graph): \u7121\
    \u5411\u30B0\u30E9\u30D5\n\n    Returns:\n        G: \u5F69\u8272\u6570\n    \"\
    \"\"\n\n    N = G.order()\n\n    def zeta(X):\n        Y = X.copy()\n        for\
    \ x in range(N):\n            b = (1 << x)\n            for S in range(1 << N):\n\
    \                if bit(S, x):\n                    Y[S] += Y[S ^ b]\n       \
    \ return Y\n\n    def mebious(Y):\n        X = Y.copy()\n        for x in range(N):\n\
    \            b = 1<< x\n            for S in range(1<<N):\n                if\
    \ bit(S, x):\n                    X[S] -= X[S ^ b]\n        return X\n\n    def\
    \ convolution(A, B):\n        return mebious([a * b for a, b in zip(zeta(A), zeta(B))])\n\
    \n    def lowest_bit(x: int):\n        return (x & (-x)).bit_length() - 1\n\n\
    \    bit = lambda x, k: (x >> k) & 1\n\n    def bits(x):\n        return [k for\
    \ k in range(N) if bit(x, k)]\n\n    edge = [[False] * N for _ in range(N)]\n\
    \    for u, v in G.edge_yielder():\n        edge[u][v] = edge[v][u] = True\n\n\
    \    # \u65B9\u91DD: dp[k][S] := \u8A98\u5C0E\u30B0\u30E9\u30D5 G[S] \u306F k\
    \ \u8272\u3067\u5F69\u8272\u53EF\u80FD ?\n\n    # Section I: dp[1][S] \u3092\u6C42\
    \u3081\u308B. (iff S \u306F\u72EC\u7ACB\u96C6\u5408?)\n    dp = [None];\n    dp.append([0]\
    \ * (1 << N)); dp[1][0] = 1\n    dp_1 = dp[1]\n    for S in range(1, 1 << N):\n\
    \        x = lowest_bit(S)\n        if not dp_1[S ^ (1 << x)]:\n            continue\n\
    \n        dp_1[S] = int(not any(edge[x][y] for y in bits(S ^ (1 << x))))\n\n \
    \   # \u7A7A\u30B0\u30E9\u30D5\u306E\u5F69\u8272\u6570\u306F 1\n    if dp_1[-1]:\n\
    \        return 1\n\n    # Section II: dp_k[V] \u304C True \u306B\u306A\u308B\u6700\
    \u5C0F\u306E k \u3092\u6C42\u3081\u308B\n    for k in range(2, N + 1):\n     \
    \   dp.append(convolution(dp_1, dp[-1]))\n        dp[k] = list(map(lambda x: 1\
    \ if x else 0, dp[-1]))\n\n        if dp[k][-1]:\n            return k\n\ndef\
    \ Clique_Cover_Number(G: Graph):\n    \"\"\" G \u3092\u30AF\u30EA\u30FC\u30AF\u3067\
    \u5206\u5272\u3059\u308B\u305F\u3081\u306B\u5FC5\u8981\u306A\u30AF\u30EA\u30FC\
    \u30AF\u306E\u6570\u306E\u6700\u5C0F\u5024\u3092\u6C42\u3081\u308B.\n    \u3053\
    \u306E\u5024\u306F G \u306E\u88DC\u30B0\u30E9\u30D5\u306E\u5F69\u8272\u6570\u3068\
    \u4E00\u81F4\u3059\u308B.\n\n    Args:\n        G (Graph): \u7121\u5411\u30B0\u30E9\
    \u30D5\n\n    Returns:\n        int\n    \"\"\"\n    return Clique_Cover_Number(Complement_Graph(G))"
  dependsOn: []
  isVerificationFile: false
  path: Graph/Graph/Coloring.py
  requiredBy: []
  timestamp: '2024-08-01 00:42:08+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Graph/Graph/Coloring.py
layout: document
redirect_from:
- /library/Graph/Graph/Coloring.py
- /library/Graph/Graph/Coloring.py.html
title: Graph/Graph/Coloring.py
---
