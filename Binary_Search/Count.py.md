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
  code: "def Binary_Search_Small_Count(A, x, equal=False, sort=False):\n    \"\"\"\
    \u4E8C\u5206\u63A2\u7D22\u306B\u3088\u3063\u3066, x \u672A\u6E80\u306E\u8981\u7D20\
    \u306E\u500B\u6570\u3092\u8ABF\u3079\u308B.\n\n    A: \u30EA\u30B9\u30C8\n   \
    \ x: \u8ABF\u3079\u308B\u8981\u7D20\n    sort: \u30BD\u30FC\u30C8\u3092\u3059\u308B\
    \u5FC5\u8981\u304C\u3042\u308B\u304B\u3069\u3046\u304B (True \u3067\u5FC5\u8981\
    )\n    equal: True \u306E\u3068\u304D\u306F x \"\u672A\u6E80\" \u304C x \"\u4EE5\
    \u4E0B\" \u306B\u306A\u308B\n    \"\"\"\n    if sort:\n        A.sort()\n\n  \
    \  if len(A)==0 or A[0]>x or ((not equal) and A[0]==x):\n        return 0\n\n\
    \    L,R=0,len(A)\n    while R-L>1:\n        C=L+(R-L)//2\n        if A[C]<x or\
    \ (equal and A[C]==x):\n            L=C\n        else:\n            R=C\n\n  \
    \  return L+1\n\ndef Binary_Search_Big_Count(A, x, equal=False, sort=False):\n\
    \    \"\"\"\u4E8C\u5206\u63A2\u7D22\u306B\u3088\u3063\u3066, x \u3092\u8D85\u3048\
    \u308B\u8981\u7D20\u306E\u500B\u6570\u3092\u8ABF\u3079\u308B.\n\n    A: \u30EA\
    \u30B9\u30C8\n    x: \u8ABF\u3079\u308B\u8981\u7D20\n    sort: \u30BD\u30FC\u30C8\
    \u3092\u3059\u308B\u5FC5\u8981\u304C\u3042\u308B\u304B\u3069\u3046\u304B (True\
    \ \u3067\u5FC5\u8981)\n    equal: True \u306E\u3068\u304D\u306F x \"\u3092\u8D85\
    \u3048\u308B\" \u304C x \"\u4EE5\u4E0A\" \u306B\u306A\u308B\n    \"\"\"\n\n  \
    \  if sort:\n        A.sort()\n\n    if len(A)==0 or A[-1]<x or ((not equal) and\
    \ A[-1]==x):\n        return 0\n\n    L,R=-1,len(A)-1\n    while R-L>1:\n    \
    \    C=L+(R-L)//2\n        if A[C]>x or (equal and A[C]==x):\n            R=C\n\
    \        else:\n            L=C\n    return len(A)-R\n\ndef Binary_Search_Range_Count(A,\
    \ x, y, sort=False, left_close=True, right_close=True):\n    \"\"\"\u4E8C\u5206\
    \u63A2\u7D22\u306B\u3088\u3063\u3066, x \u4EE5\u4E0A y \u4EE5\u4E0B \u306E\u500B\
    \u6570\u3092\u8ABF\u3079\u308B.\n\n    A: \u30EA\u30B9\u30C8\n    x, y: \u8ABF\
    \u3079\u308B\u8981\u7D20\n    sort: \u30BD\u30FC\u30C8\u3092\u3059\u308B\u5FC5\
    \u8981\u304C\u3042\u308B\u304B\u3069\u3046\u304B (True \u3067\u5FC5\u8981)\n \
    \   left_equal: True \u306E\u3068\u304D\u306F x<=a, False \u306E\u3068\u304D\u306F\
    \ x<a\n    right_equal: True \u306E\u3068\u304D\u306F y<=a, False \u306E\u3068\
    \u304D\u306F y<a\n    \"\"\"\n\n    if sort:\n        A.sort()\n\n    alpha=Binary_Search_Small_Count(A,\
    \ y, equal=right_close)\n    beta =Binary_Search_Small_Count(A, x, equal=not left_close)\n\
    \    return max(alpha-beta,0)\n"
  dependsOn: []
  isVerificationFile: false
  path: Binary_Search/Count.py
  requiredBy: []
  timestamp: '2022-09-10 17:07:59+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Binary_Search/Count.py
layout: document
redirect_from:
- /library/Binary_Search/Count.py
- /library/Binary_Search/Count.py.html
title: Binary_Search/Count.py
---
