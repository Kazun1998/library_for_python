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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.3/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.3/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def Binary_Search_Low_Value(A, x, equal=False, sort=False, default=None):\n\
    \    \"\"\" A \u306E x \u672A\u6E80\u306E\u8981\u7D20\u306E\u4E2D\u3067\u6700\u5927\
    \u306E\u3082\u306E\u3092\u51FA\u529B\u3059\u308B.\n\n    A: \u30EA\u30B9\u30C8\
    \n    x: \u8ABF\u3079\u308B\u8981\u7D20\n    sort: \u30BD\u30FC\u30C8\u3092\u3059\
    \u308B\u5FC5\u8981\u304C\u3042\u308B\u304B\u3069\u3046\u304B (True \u3067\u5FC5\
    \u8981)\n    equal: True \u306E\u3068\u304D\u306F x \"\u672A\u6E80\" \u304C x\
    \ \"\u4EE5\u4E0B\" \u306B\u306A\u308B\n    \u203B \u5168\u3066\u306E\u8981\u7D20\
    \u304C x \u4EE5\u4E0A (\u8D85\u3048\u308B) \u5834\u5408\u306F default \u304C\u8FD4\
    \u3055\u308C\u308B.\n    \"\"\"\n\n    if sort:\n        A.sort()\n\n    if len(A)==0\
    \ or A[0]>x or ((not equal) and A[0]==x):\n        return default\n\n    L,R=0,len(A)\n\
    \    while R-L>1:\n        C=L+(R-L)//2\n        if A[C]<x or (equal and A[C]==x):\n\
    \            L=C\n        else:\n            R=C\n\n    return A[L]\n\ndef Binary_Search_High_Value(A,\
    \ x, equal=False, sort=False, default=None):\n    \"\"\" A \u306E x \u3092\u8D85\
    \u3048\u308B\u8981\u7D20\u306E\u4E2D\u3067\u6700\u5C0F\u306E\u3082\u306E\u3092\
    \u51FA\u529B\u3059\u308B.\n\n    A: \u30EA\u30B9\u30C8\n    x: \u8ABF\u3079\u308B\
    \u8981\u7D20\n    sort: \u30BD\u30FC\u30C8\u3092\u3059\u308B\u5FC5\u8981\u304C\
    \u3042\u308B\u304B\u3069\u3046\u304B (True \u3067\u5FC5\u8981)\n    equal: True\
    \ \u306E\u3068\u304D\u306F x \"\u3092\u8D85\u3048\u308B\" \u304C x \"\u4EE5\u4E0A\
    \" \u306B\u306A\u308B\n    \u203B \u5168\u3066\u306E\u8981\u7D20\u304C x \u4EE5\
    \u4E0A (\u3092\u8D85\u3048\u308B) \u5834\u5408\u306F default \u304C\u8FD4\u3055\
    \u308C\u308B.\n    \"\"\"\n\n    if sort:\n        A.sort()\n\n    if len(A)==0\
    \ or A[-1]<x or ((not equal) and A[-1]==x):\n        return default\n\n    L,R=-1,len(A)-1\n\
    \    while R-L>1:\n        C=L+(R-L)//2\n        if A[C]>x or (equal and A[C]==x):\n\
    \            R=C\n        else:\n            L=C\n    K=len(A)-R\n    return A[-K]\n\
    \ndef Binary_Search_High_Low_Value(A, x, low_equal=False, high_equal=False, sort=False,\
    \ low_default=None, high_default=None):\n    \"\"\" A\u306E x \u672A\u6E80\u3067\
    \u6700\u5927\u306E\u8981\u7D20 p \u3068 x \u3092\u8D85\u3048\u308B\u6700\u5C0F\
    \u306E\u8981\u7D20 q \u3092\u898B\u3064\u3051, (p,q) \u3092\u51FA\u529B\u3059\u308B\
    .\n\n    A: \u30EA\u30B9\u30C8\n    x: \u8ABF\u3079\u308B\u8981\u7D20\n    sort:\
    \ \u30BD\u30FC\u30C8\u3092\u3059\u308B\u5FC5\u8981\u304C\u3042\u308B\u304B\u3069\
    \u3046\u304B (True \u3067\u5FC5\u8981)\n    low_equal: True \u306E\u3068\u304D\
    \u306F x \"\u672A\u6E80\" \u304C x \"\u4EE5\u4E0B\" \u306B\u306A\u308B\n    high_equal:\
    \ True \u306E\u3068\u304D\u306F x \"\u3092\u8D85\u3048\u308B\" \u304C \"\u4EE5\
    \u4E0A\" \u306B\u306A\u308B\n    \"\"\"\n\n    if sort:\n        A.sort()\n\n\
    \    return (\n        Binary_Search_Low_Value(A,x,equal=low_equal,default=low_default),\n\
    \        Binary_Search_High_Value(A,x,equal=high_equal,default=high_default)\n\
    \        )\n"
  dependsOn: []
  isVerificationFile: false
  path: Binary_Search/Value.py
  requiredBy: []
  timestamp: '2022-09-10 17:07:59+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Binary_Search/Value.py
layout: document
redirect_from:
- /library/Binary_Search/Value.py
- /library/Binary_Search/Value.py.html
title: Binary_Search/Value.py
---
