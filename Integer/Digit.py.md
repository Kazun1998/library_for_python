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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.8/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.8/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class BaseException(Exception):\n    def __init__(self, error_base):\n  \
    \      self.error_base = error_base\n\n    def __str__(self):\n        return\
    \ f\"\u6307\u5B9A\u3057\u305F\u5E95 {self.error_base} \u306F\u4E0D\u6B63\u306A\
    \u5E95\u3067\u3059.\"\n\ndef Integer_Digits(n: int, b: int = 10, l: int = None)\
    \ -> list[int]:\n    \"\"\" \u6574\u6570 n \u306E\u5E95\u3092 b \u3068\u3057\u305F\
    \u5834\u5408\u306E\u8868\u73FE\u3092\u6C42\u3081\u308B.\n\n    Args:\n       \
    \ n (int): N\n        b (int, optional): \u5E95 (b >= 2). Defaults to 10.\n  \
    \      l (int): \u9577\u3055\u304C 0 \u306B\u306A\u308B\u3088\u3046\u306B\u5DE6\
    \u5074\u306B 0 \u3092\u57CB\u3081\u305F\u308A, \u53F3\u304B\u3089 l \u8981\u7D20\
    \u3092\u53D6\u5F97\u3059\u308B.\n\n    Returns:\n        list[int]: \u8868\u793A\
    \n    \"\"\"\n\n    assert b >= 2, BaseException(b)\n\n    n = abs(n)\n    digits\
    \ = []\n\n    if l is None:\n        while (n > 0) or (not digits):\n        \
    \    n, r = divmod(n, b)\n            digits.append(r)\n    else:\n        for\
    \ _ in range(l):\n            n, r = divmod(n, b)\n            digits.append(r)\n\
    \n    return digits[::-1]\n\ndef Integer_Length(n: int, b: int = 10) -> int:\n\
    \    \"\"\" \u6574\u6570 n \u306E\u5E95\u3092 b \u3068\u3057\u305F\u5834\u5408\
    \u306E\u6841\u6570\u3092\u6C42\u3081\u308B (0 \u306F 0 \u6841\u3068\u3059\u308B\
    ).\n\n    Args:\n        n (int): N\n        b (int, optional): \u5E95 (b >= 2).\
    \ Defaults to 10.\n\n    Returns:\n        int: \u6841\u6570\n    \"\"\"\n\n \
    \   assert b >= 2, BaseException(b)\n    return len(Integer_Digits(n, b)) if n\
    \ != 0 else 0\n\ndef Digit_Sum(n: int, b: int = 10) -> int:\n    \"\"\" \u6574\
    \u6570 n \u306E\u5E95\u3092 b \u3068\u3057\u305F\u5834\u5408\u306E\u6841\u548C\
    \u3092\u6C42\u3081\u308B.\n\n    Args:\n        n (int): N\n        b (int, optional):\
    \ \u5E95 (b >= 2). Defaults to 10.\n\n    Returns:\n        int: \u6841\u548C\n\
    \    \"\"\"\n\n    return sum(Integer_Digits(n, b))\n\ndef Digit_Count(n: int,\
    \ b: int) -> list[int]:\n    \"\"\" \u6574\u6570 n \u306E\u5E95\u3092 b \u3068\
    \u3057\u305F\u5834\u5408\u306B\u304A\u3051\u308B\u5404\u6570\u306E\u51FA\u73FE\
    \u56DE\u6570\u3092\u6C42\u3081\u308B.\n\n    Args:\n        n (int): N\n     \
    \   b (int): \u5E95\n\n    Returns:\n        list[int]: \u9577\u3055 b \u306E\u914D\
    \u5217. \u7B2C k \u8981\u7D20\u306F k \u306E\u51FA\u73FE\u56DE\u6570.\n    \"\"\
    \"\n\n    assert b >= 2, BaseException(b)\n\n    count = [0] * b\n    for d in\
    \ Integer_Digits(n, b):\n        count[d] += 1\n    return count\n\ndef From_Digits(digits:\
    \ list[int], b: int = 10) -> int:\n    \"\"\" \u5E95\u3092 b \u3068\u3057\u305F\
    \u5834\u5408\u306B digit \u304C\u306A\u3059\u6574\u6570\u3092\u8FD4\u3059 (Interger_Digit\
    \ \u306E\u9006\u95A2\u6570)\n\n    Args:\n        digits (list[int]): \u6570\u306E\
    \u30EA\u30B9\u30C8\n        b (int, optional): \u5E95 (b >= 2). Defaults to 10.\n\
    \n    Returns:\n        int: \u6574\u6570\n    \"\"\"\n\n    assert b >= 2, BaseException(b)\n\
    \n    res = 0\n    for x in digits:\n        res = b * res + x\n    return res\n"
  dependsOn: []
  isVerificationFile: false
  path: Integer/Digit.py
  requiredBy: []
  timestamp: '2025-01-05 00:53:05+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Integer/Digit.py
layout: document
redirect_from:
- /library/Integer/Digit.py
- /library/Integer/Digit.py.html
title: Integer/Digit.py
---
