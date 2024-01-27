---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links:
    - https://judge.yosupo.jp/submission/34963
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.1/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.1/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def Hungarian(A, minimize=False, mode=False):\n    \"\"\" \u884C\u5217 A\
    \ \u306B\u5BFE\u3057\u3066\u30CF\u30F3\u30AC\u30EA\u30A2\u30F3\u6CD5\u3092\u9069\
    \u7528\u3057, \u6700\u5927\u5024\u3092\u6C42\u3081\u308B.\n\n    A: \u884C\u5217\
    \n    minimize: True \u306B\u3059\u308B\u3068, \u6700\u5C0F\u5024\u3092\u6C42\u3081\
    \u308B\n    mode: True \u306B\u3059\u308B\u3068, \u6700\u5927\u5024 (\u6700\u5C0F\
    \u5024) \u3092\u9054\u6210\u3059\u308B\u4F8B\u3082\u51FA\u529B\u3059\u308B.\n\n\
    \    Reference: https://judge.yosupo.jp/submission/34963\n    \"\"\"\n    if minimize:\n\
    \        if mode:\n            score, x=Hungarian([[-a_ij for a_ij in Ai] for\
    \ Ai in A], False, True)\n            return -score,x\n        else:\n       \
    \     return -Hungarian([[-a_ij for a_ij in Ai] for Ai in A], False, False)\n\n\
    \    inf=1<<31\n    N=len(A)\n    fx=[inf]*N\n    fy=[0]*N\n    x=[-1]*N\n   \
    \ y=[-1]*N\n    i=0\n    while i < N:\n        t=[-1]*N\n        s=[i]*(N + 1)\n\
    \        p=q=0\n        while p <= q and x[i] < 0:\n            k, j = s[p], 0\n\
    \            while j < N and x[i] < 0:\n                if fx[k] + fy[j] == A[k][j]\
    \ and t[j] < 0:\n                    q += 1\n                    s[q] = y[j]\n\
    \                    t[j] = k\n                    if s[q] < 0:\n            \
    \            p = j\n                        while p >= 0:\n                  \
    \          y[j] = k = t[j]\n                            p = x[k]\n           \
    \                 x[k] = j\n                            j = p\n              \
    \  j += 1\n            p += 1\n        if x[i] < 0:\n            d = inf\n   \
    \         for k in range(q + 1):\n                for j in range(N):\n       \
    \             if t[j] < 0:\n                        d = min(d, fx[s[k]] + fy[j]\
    \ - A[s[k]][j])\n            for j in range(N):\n                if t[j] >= 0:\n\
    \                    fy[j] += d\n            for k in range(q + 1):\n        \
    \        fx[s[k]] -= d\n        else:\n            i += 1\n\n    score=0\n   \
    \ for i,j in enumerate(x):\n        score+=A[i][j]\n\n    return (score,x) if\
    \ mode else score\n"
  dependsOn: []
  isVerificationFile: false
  path: Hungarian.py
  requiredBy: []
  timestamp: '2023-06-17 23:41:30+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Hungarian.py
layout: document
redirect_from:
- /library/Hungarian.py
- /library/Hungarian.py.html
title: Hungarian.py
---
