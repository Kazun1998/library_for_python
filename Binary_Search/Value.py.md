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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.13.2/x64/lib/python3.13/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.13.2/x64/lib/python3.13/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from bisect import bisect_left, bisect_right\n\ndef Binary_Search_Low_Value(A:\
    \ list, x, equal = False, default = None, sort = False):\n    \"\"\" \u4E8C\u5206\
    \u63A2\u7D22\u306B\u3088\u3063\u3066, A \u306E\u5143\u306E\u3046\u3061, x \u672A\
    \u6E80\u306E\u8981\u7D20\u306E\u3046\u3061\u6700\u5927\u306E\u8981\u7D20\u3092\
    \u6C42\u3081\u308B.\n\n    Args:\n        A (list): \u63A2\u7D22\u5BFE\u8C61\u306E\
    \u30EA\u30B9\u30C8\n        x : \u95BE\u5024\n        equal (bool, optional):\
    \ True \u306E\u3068\u304D\u306F\u300Cx \u672A\u6E80\u300D\u304C\u300Cx \u4EE5\u4E0B\
    \u300D\u306B\u306A\u308B. Defaults to False.\n        default (optional): A \u306E\
    \u5168\u3066\u306E\u8981\u7D20\u304C x \u4EE5\u4E0A (\u3088\u308A\u5927\u304D\u3044\
    \u3068\u304D) \u306E\u8FD4\u308A\u5024. Defaults to None.\n        sort (bool,\
    \ optional): A \u304C\u6607\u9806\u3067\u3042\u308B\u3053\u3068\u304C\u4FDD\u8A3C\
    \u3055\u308C\u3066\u3044\u306A\u3044\u3068\u304D, True \u306B\u3059\u308B\u3053\
    \u3068\u3067\u5B9F\u884C\u6642\u306B\u30BD\u30FC\u30C8\u3092\u884C\u3046. Defaults\
    \ to False.\n    \"\"\"\n\n    if sort:\n        A.sort()\n\n    if equal:\n \
    \       ind = bisect_right(A, x)\n    else:\n        ind = bisect_left(A, x)\n\
    \n    return A[ind - 1] if ind > 0 else default\n\ndef Binary_Search_High_Value(A,\
    \ x, equal = False, default = None, sort = False):\n    \"\"\" \u4E8C\u5206\u63A2\
    \u7D22\u306B\u3088\u3063\u3066, A \u306E\u5143\u306E\u3046\u3061, x \u3088\u308A\
    \u5927\u304D\u3044\u306E\u8981\u7D20\u306E\u3046\u3061\u6700\u5927\u306E\u8981\
    \u7D20\u3092\u6C42\u3081\u308B.\n\n    Args:\n        A (list): \u63A2\u7D22\u5BFE\
    \u8C61\u306E\u30EA\u30B9\u30C8\n        x : \u95BE\u5024\n        equal (bool,\
    \ optional): True \u306E\u3068\u304D\u306F\u300Cx \u3088\u308A\u5927\u304D\u3044\
    \u300D\u304C\u300Cx \u4EE5\u4E0A\u300D\u306B\u306A\u308B. Defaults to False.\n\
    \        default (optional): A \u306E\u5168\u3066\u306E\u8981\u7D20\u304C x \u4EE5\
    \u4E0B (\u672A\u6E80) \u306E\u8FD4\u308A\u5024. Defaults to None.\n        sort\
    \ (bool, optional): A \u304C\u6607\u9806\u3067\u3042\u308B\u3053\u3068\u304C\u4FDD\
    \u8A3C\u3055\u308C\u3066\u3044\u306A\u3044\u3068\u304D, True \u306B\u3059\u308B\
    \u3053\u3068\u3067\u5B9F\u884C\u6642\u306B\u30BD\u30FC\u30C8\u3092\u884C\u3046\
    . Defaults to False.\n    \"\"\"\n\n    if sort:\n        A.sort()\n\n    if equal:\n\
    \        ind = bisect_left(A, x)\n    else:\n        ind = bisect_right(A, x)\n\
    \n    return A[ind] if ind < len(A) else default\n\ndef Binary_Search_High_Low_Value(A:\
    \ list, x, low_equal = False, high_equal = False, low_default = None, high_default\
    \ = None, sort = False):\n    \"\"\" \u4E8C\u5206\u63A2\u7D22\u306B\u3088\u3063\
    \u3066, A \u306E x \u672A\u6E80\u3067\u6700\u5927\u306E\u8981\u7D20 p \u3068 x\
    \ \u3088\u308A\u5927\u304D\u3044\u6700\u5C0F\u306E\u8981\u7D20 q \u3092\u6C42\u3081\
    , (p, q) \u3092\u51FA\u529B\u3059\u308B.\n\n    Args:\n        A (list): \u635C\
    \u7D22\u5BFE\u8C61\u306E\u30EA\u30B9\u30C8\n        x : \u95BE\u5024\n       \
    \ low_equal (bool, optional): True \u306E\u3068\u304D\u306F\u300Cx \u672A\u6E80\
    \u300D\u304C\u300Cx \u4EE5\u4E0B\u300D\u306B\u306A\u308B. Defaults to False.\n\
    \        high_equal (bool, optional):  True \u306E\u3068\u304D\u306F\u300Cx \u3088\
    \u308A\u5927\u304D\u3044\u300D\u304C\u300Cx \u4EE5\u4E0A\u300D\u306B\u306A\u308B\
    . Defaults to False.\n        low_default (optional): A \u306E\u5168\u3066\u306E\
    \u8981\u7D20\u304C x \u4EE5\u4E0A (\u3088\u308A\u5927\u304D\u3044\u3068\u304D\
    ) \u306E\u8FD4\u308A\u5024. Defaults to None.\n        high_default (optional):\
    \ A \u306E\u5168\u3066\u306E\u8981\u7D20\u304C x \u4EE5\u4E0B (\u672A\u6E80) \u306E\
    \u8FD4\u308A\u5024. Defaults to None.\n        sort (bool, optional): A \u304C\
    \u6607\u9806\u3067\u3042\u308B\u3053\u3068\u304C\u4FDD\u8A3C\u3055\u308C\u3066\
    \u3044\u306A\u3044\u3068\u304D, True \u306B\u3059\u308B\u3053\u3068\u3067\u5B9F\
    \u884C\u6642\u306B\u30BD\u30FC\u30C8\u3092\u884C\u3046. Defaults to False.\n\n\
    \    Returns:\n        (p, q): p: A \u306E x \u672A\u6E80\u3067\u6700\u5927\u306E\
    \u8981\u7D20, q: x \u3088\u308A\u5927\u304D\u3044\u6700\u5C0F\u306E\u8981\u7D20\
    \n    \"\"\"\n\n    if sort:\n        A.sort()\n\n    return (\n        Binary_Search_Low_Value(A,\
    \ x, equal = low_equal, default = low_default),\n        Binary_Search_High_Value(A,\
    \ x, equal = high_equal, default = high_default)\n        )\n"
  dependsOn: []
  isVerificationFile: false
  path: Binary_Search/Value.py
  requiredBy: []
  timestamp: '2024-07-28 11:06:05+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Binary_Search/Value.py
layout: document
redirect_from:
- /library/Binary_Search/Value.py
- /library/Binary_Search/Value.py.html
title: Binary_Search/Value.py
---
