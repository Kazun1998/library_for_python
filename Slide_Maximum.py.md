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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.2/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.2/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from collections import deque\n\ndef Slide_Maximum_Index(A,k):\n    \"\"\"\
    \u30EA\u30B9\u30C8A \u306E k \u8981\u7D20\u30B9\u30E9\u30A4\u30C9\u6700\u5927\u5024\
    \u3092\u3082\u3064\u30A4\u30F3\u30C7\u30C3\u30AF\u30B9\u3092\u6C42\u3081\u308B\
    .\n\n    [Input]\n    A: List\n    k: Length\n\n    [Output]\n    M: \u9577\u3055\
    \ |A|-k+1 \u306E\u30EA\u30B9\u30C8\u3067, \u7B2C i \u8981\u7D20\u306F max(A[i],\
    \ ..., A[i+k-1])=A[M[i]] \u3068\u306A\u308B\u3088\u3046\u306B\u306A\u308B.\n \
    \   \"\"\"\n\n    N=len(A)\n    index=[0]*N\n    Q=deque()\n\n    for i in range(N):\n\
    \        while Q and Q[0]<=i-k:\n            Q.popleft()\n\n        while Q and\
    \ A[Q[-1]]<A[i]:\n            Q.pop()\n        Q.append(i)\n        index[i]=Q[0]\n\
    \    return index\n\ndef Slide_Maximum_Value(A,k):\n    \"\"\"\u30EA\u30B9\u30C8\
    A \u306E k \u8981\u7D20\u30B9\u30E9\u30A4\u30C9\u6700\u5927\u5024\u3092\u6C42\u3081\
    \u308B.\n\n    [Input]\n    A: List\n    k: Length\n\n    [Output]\n    M: \u9577\
    \u3055 |A|-k+1 \u306E\u30EA\u30B9\u30C8\u3067, \u7B2C i \u8981\u7D20\u306F max(A[i],\
    \ ..., A[i+k-1])=A[M[i]] \u3068\u306A\u308B\u3088\u3046\u306B\u306A\u308B.\n \
    \   \"\"\"\n\n    N=len(A)\n    res=[0]*N\n    Q=deque()\n\n    for i in range(N):\n\
    \        while Q and Q[0]<=i-k:\n            Q.popleft()\n\n        while Q and\
    \ A[Q[-1]]<A[i]:\n            Q.pop()\n        Q.append(i)\n        res[i]=A[Q[0]]\n\
    \    return res\n"
  dependsOn: []
  isVerificationFile: false
  path: Slide_Maximum.py
  requiredBy: []
  timestamp: '2022-01-16 16:40:15+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Slide_Maximum.py
layout: document
redirect_from:
- /library/Slide_Maximum.py
- /library/Slide_Maximum.py.html
title: Slide_Maximum.py
---
