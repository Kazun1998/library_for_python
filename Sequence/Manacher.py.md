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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.13.3/x64/lib/python3.13/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.13.3/x64/lib/python3.13/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def Manacher(S) -> list[int]:\n    \"\"\" S \u306E\u5404\u6587\u5B57\u306B\
    \u5BFE\u3057\u3066, \u305D\u306E\u6587\u5B57\u3092\u4E2D\u5FC3\u3068\u3059\u308B\
    \u6975\u5927\u306A\u56DE\u5206\u306E\u534A\u5F84\u3092\u6C42\u3081\u308B.\n\n\
    \    Args:\n        S:\n\n    Returns:\n        list[int]: \u7B2C i \u8981\u7D20\
    \u306F S \u306E i \u6587\u5B57\u76EE\u3092\u4E2D\u5FC3\u3068\u3059\u308B\u6975\
    \u5927\u306A\u56DE\u5206\u306E\u534A\u5F84 (\u305D\u306E\u6975\u5927\u306A\u56DE\
    \u5206\u306E\u9577\u3055\u3092 y \u3068\u3059\u308B\u3068, \u534A\u5F84\u306F\
    \ (y + 1) / 2).\n    \"\"\"\n\n    i = j = 0\n    res = [0] * len(S)\n    while\
    \ i < len(S):\n        while (i - j >= 0) and (i + j < len(S)) and (S[i - j] ==\
    \ S[i + j]):\n            j += 1\n\n        res[i] = j\n        k = 1\n      \
    \  while (i - k >= 0) and (k + res[i - k] < j):\n            res[i + k] = res[i\
    \ - k]\n            k += 1\n\n        i += k; j -= k\n\n    return res\n\ndef\
    \ Manacher_with_even(S, dummy = None) -> tuple[list[int], list[int]]:\n    \"\"\
    \" S \u306E\u5404\u6587\u5B57\u3068\u6587\u5B57\u3068\u6587\u5B57\u306E\u9593\u306B\
    \u3064\u3044\u3066, \u305D\u3053\u3092\u4E2D\u5FC3\u3068\u3059\u308B\u6975\u5927\
    \u306A\u56DE\u5206\u306E\u534A\u5F84\u3092\u6C42\u3081\u308B.\n\n    Args:\n \
    \       S:\n        dummy (optional): S \u306B\u542B\u307E\u308C\u308B\u3053\u3068\
    \u304C\u306A\u3044\u8981\u7D20. Defaults to None.\n\n    Returns:\n        tuple[list[int],\
    \ list[int]]: (odd, even)\n            odd: Manachar(S) \u306E\u8FD4\u308A\u5024\
    \u3068\u7B49\u3057\u3044.\n            even: \u7B2C i \u8981\u7D20\u306F S \u306E\
    \ i \u6587\u5B57\u76EE\u3068 (i + 1) \u6587\u5B57\u76EE\u306E\u9593\u3092\u4E2D\
    \u5FC3\u3068\u3059\u308B\u6975\u5927\u306A\u56DE\u5206\u306E\u534A\u5F84\n   \
    \ \"\"\"\n    T = [dummy] * (2 * len(S) - 1)\n    for i in range(len(S)):\n  \
    \      T[2 * i] = S[i]\n\n    res = Manacher(T)\n    odd = [(a + 1) // 2 for a\
    \ in res[::2]]\n    even = [b // 2 for b in res[1::2]]\n\n    return odd, even\n"
  dependsOn: []
  isVerificationFile: false
  path: Sequence/Manacher.py
  requiredBy: []
  timestamp: '2025-03-23 22:44:12+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Sequence/Manacher.py
layout: document
redirect_from:
- /library/Sequence/Manacher.py
- /library/Sequence/Manacher.py.html
title: Sequence/Manacher.py
---
