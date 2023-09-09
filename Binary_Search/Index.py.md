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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.5/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.5/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def Binary_Search_Index(A, x, sort=False, default=None, offset=0):\n    \"\
    \"\" \u4E8C\u5206\u63A2\u7D22\u306B\u3088\u3063\u3066, A \u306B x \u304C\u5B58\
    \u5728\u3059\u308B\u308C\u3070, \u305D\u306E\u30A4\u30F3\u30C7\u30C3\u30AF\u30B9\
    \u3092\u8FD4\u3059.\n    (x \u304C\u8907\u6570\u3042\u308B\u6642, \u8FD4\u3063\
    \u3066\u304F\u308B\u30A4\u30F3\u30C7\u30C3\u30AF\u30B9\u306F\u4E0D\u5B9A)\n\n\
    \    A: \u30EA\u30B9\u30C8\n    x: \u8ABF\u3079\u308B\u8981\u7D20\n    sort: \u30BD\
    \u30FC\u30C8\u3092\u3059\u308B\u5FC5\u8981\u304C\u3042\u308B\u304B\u3069\u3046\
    \u304B (True \u3067\u5FC5\u8981)\n    default: \u5B58\u5728\u3057\u306A\u304B\u3063\
    \u305F\u5834\u5408\u306E\u8FD4\u308A\u5024\n    offset=0: \u30A4\u30F3\u30C7\u30C3\
    \u30AF\u30B9+ offset \u306E\u5024\u3092\u8FD4\u3059.\n    \"\"\"\n    if sort:\n\
    \        A.sort()\n\n    if len(A)==0 or x<A[0] or A[-1]<x:\n        return default\n\
    \n    L,R=0,len(A)\n    while R-L>0:\n        C=L+(R-L)//2\n        if x<A[C]:\n\
    \            R=C\n        elif x>A[C]:\n            L=C+1\n        else:\n   \
    \         return C+offset\n    return default\n"
  dependsOn: []
  isVerificationFile: false
  path: Binary_Search/Index.py
  requiredBy: []
  timestamp: '2022-09-10 17:07:59+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Binary_Search/Index.py
layout: document
redirect_from:
- /library/Binary_Search/Index.py
- /library/Binary_Search/Index.py.html
title: Binary_Search/Index.py
---
