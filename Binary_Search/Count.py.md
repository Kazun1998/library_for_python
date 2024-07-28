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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.4/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.4/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from bisect import bisect_left, bisect_right\n\ndef Binary_Search_Small_Count(A:\
    \ list, x, equal = False, sort = False):\n    \"\"\" \u4E8C\u5206\u63A2\u7D22\u306B\
    \u3088\u3063\u3066, A \u306E\u5143\u306E\u3046\u3061, x \u3088\u308A\u5C0F\u3055\
    \u3044\u5143\u306E\u500B\u6570\u3092\u6C42\u3081\u308B.\n\n    Args:\n       \
    \ A (list): \u63A2\u7D22\u5BFE\u8C61\u306E\u30EA\u30B9\u30C8\n        x : \u95BE\
    \u5024\n        equal (bool, optional): True \u306E\u3068\u304D\u306F\u300Cx \u3088\
    \u308A\u5C0F\u3055\u3044\u300D\u304C\u300Cx \u4EE5\u4E0B\u300D\u306B\u306A\u308B\
    . Defaults to False.\n        sort (bool, optional): A \u304C\u6607\u9806\u3067\
    \u3042\u308B\u3053\u3068\u304C\u4FDD\u8A3C\u3055\u308C\u3066\u3044\u306A\u3044\
    \u3068\u304D, True \u306B\u3059\u308B\u3053\u3068\u3067\u5B9F\u884C\u6642\u306B\
    \u30BD\u30FC\u30C8\u3092\u884C\u3046. Defaults to False.\n\n    Returns:\n   \
    \     int: x \u3088\u308A\u5C0F\u3055\u3044\u5143\u306E\u500B\u6570\n    \"\"\"\
    \n    if sort:\n        A.sort()\n\n    if equal:\n        return bisect_right(A,\
    \ x)\n    else:\n        return bisect_left(A, x)\n\ndef Binary_Search_Big_Count(A,\
    \ x, equal = False, sort = False):\n    \"\"\" \u4E8C\u5206\u63A2\u7D22\u306B\u3088\
    \u3063\u3066, A \u306E\u5143\u306E\u3046\u3061, x \u3088\u308A\u5927\u304D\u3044\
    \u5143\u306E\u500B\u6570\u3092\u6C42\u3081\u308B.\n\n    Args:\n        A (list):\
    \ \u63A2\u7D22\u5BFE\u8C61\u306E\u30EA\u30B9\u30C8\n        x : \u95BE\u5024\n\
    \        equal (bool, optional): True \u306E\u3068\u304D\u306F\u300Cx \u3088\u308A\
    \u5927\u304D\u3044\u300D\u304C\u300Cx \u4EE5\u4E0A\u300D\u306B\u306A\u308B. Defaults\
    \ to False.\n        sort (bool, optional): A \u304C\u6607\u9806\u3067\u3042\u308B\
    \u3053\u3068\u304C\u4FDD\u8A3C\u3055\u308C\u3066\u3044\u306A\u3044\u3068\u304D\
    , True \u306B\u3059\u308B\u3053\u3068\u3067\u5B9F\u884C\u6642\u306B\u30BD\u30FC\
    \u30C8\u3092\u884C\u3046. Defaults to False.\n\n    Returns:\n        int: x \u3088\
    \u308A\u5927\u304D\u3044\u5143\u306E\u500B\u6570\n    \"\"\"\n\n    if sort:\n\
    \        A.sort()\n\n    if equal:\n        return len(A) - bisect_left(A, x)\n\
    \    else:\n        return len(A) - bisect_right(A, x)\n\ndef Binary_Search_Range_Count(A:\
    \ list, x, y, left_equal = True, right_equal = True, sort = False):\n    \"\"\"\
    \ \u4E8C\u5206\u63A2\u7D22\u306B\u3088\u3063\u3066, A \u306B\u542B\u307E\u308C\
    \u308B x \u4EE5\u4E0A y \u4EE5\u4E0B\u306E\u5143\u306E\u500B\u6570\u3092\u6C42\
    \u3081\u308B.\n\n    Args:\n        A (list): \u63A2\u7D22\u5BFE\u8C61\u306E\u30EA\
    \u30B9\u30C8\n        x : \u4E0B\u7AEF\u306E\u95BE\u5024\n        y : \u4E0A\u7AEF\
    \u306E\u95BE\u5024\n        left_equal (bool, optional): False \u306E\u3068\u304D\
    \u306F\u300Cx \u4EE5\u4E0A\u300D\u304C\u300Cx \u3088\u308A\u5927\u304D\u3044\u300D\
    \u306B\u306A\u308B. Defaults to True.\n        right_equal (bool, optional): False\
    \ \u306E\u3068\u304D\u306F\u300Cy \u4EE5\u4E0B\u300D\u304C\u300Cy \u3088\u308A\
    \u5C0F\u3055\u3044\u300D\u306B\u306A\u308B. Defaults to True.\n        sort (bool,\
    \ optional): A \u304C\u6607\u9806\u3067\u3042\u308B\u3053\u3068\u304C\u4FDD\u8A3C\
    \u3055\u308C\u3066\u3044\u306A\u3044\u3068\u304D, True \u306B\u3059\u308B\u3053\
    \u3068\u3067\u5B9F\u884C\u6642\u306B\u30BD\u30FC\u30C8\u3092\u884C\u3046. Defaults\
    \ to False.\n\n    Returns:\n        int: x \u4EE5\u4E0A y \u4EE5\u4E0B\u306E\u5143\
    \u306E\u500B\u6570\n    \"\"\"\n\n    if sort:\n        A.sort()\n\n    alpha\
    \ = Binary_Search_Small_Count(A, y, equal = right_equal)\n    beta = Binary_Search_Small_Count(A,\
    \ x, equal = not left_equal)\n    return max(alpha - beta, 0)\n"
  dependsOn: []
  isVerificationFile: false
  path: Binary_Search/Count.py
  requiredBy: []
  timestamp: '2024-07-28 00:01:28+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Binary_Search/Count.py
layout: document
redirect_from:
- /library/Binary_Search/Count.py
- /library/Binary_Search/Count.py.html
title: Binary_Search/Count.py
---
