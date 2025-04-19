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
  code: "def Power_Tower(tower: list[int], m: int) -> int:\n    def mod(a, m):\n \
    \       return a if a < 2 * m else a % m + m\n\n    def mul(a, b, m):\n      \
    \  return mod(a * b, m)\n\n    def power(a, k, m):\n        res = 1\n        while\
    \ k:\n            if k & 1:\n                res = mul(res, a, m)\n          \
    \  a = mul(a, a, m)\n            k >>= 1\n        return res\n\n    def totient(x):\n\
    \        if x == 1:\n            return 1\n\n        phi = 1\n        def calc(p):\n\
    \            nonlocal x, phi\n\n            if not(x % p == 0 and p != 1):\n \
    \               return\n\n            e = 0\n            while x % p == 0:\n \
    \               e += 1\n                x //= p\n\n            phi *= (p - 1)\
    \ * pow(p, e - 1)\n\n        calc(2); calc(3)\n\n        parity = 0; p = 5\n \
    \       while p * p <= x:\n            calc(p)\n            p += 4 if parity else\
    \ 2\n            parity ^= 1\n        calc(x)\n        return phi\n\n    nest_totients\
    \ = [m]\n    for _ in range(len(tower) - 1):\n        nest_totients.append(totient(nest_totients[-1]))\n\
    \n    while len(tower) > 1:\n        k = mod(tower.pop(), nest_totients.pop())\n\
    \        tower[-1] = power(tower[-1], k, nest_totients[-1])\n\n    return tower[0]\
    \ % m\n\ndef Tetoration(a: int, k: int, m: int) -> int:\n    \"\"\" a^(a^(a^(...^a)))\
    \ (k \u500B\u306E\u7D2F\u4E57\u30BF\u30EF\u30FC) \u3092 m \u3067\u5272\u3063\u305F\
    \u4F59\u308A\u3092\u6C42\u3081\u308B\n\n    Args:\n        a (int): \u5E95 (a\
    \ >= 0)\n        k (int): a \u3092\u91CD\u306D\u308B\u6570 (k >= 0)\n        m\
    \ (int): \u5270\u4F59 (m >= 1)\n\n    Returns:\n        int: \u30C6\u30C8\u30EC\
    \u30FC\u30B7\u30E7\u30F3\u3092 m \u3067\u5272\u3063\u305F\u4F59\u308A\n    \"\"\
    \"\n\n    assert a >= 0\n    assert k >= 0\n    assert m >= 1\n\n    # \u4F8B\u5916\
    \u30B1\u30FC\u30B9\u306E\u51E6\u7406\n    if k == 0:\n        return 1 % m\n \
    \   elif a == 0:\n        return 1 % m if k % 2 == 0 else 0\n\n    k = min(k,\
    \ (m - 1).bit_length() + 1)\n    return Power_Tower([a] * k, m)\n"
  dependsOn: []
  isVerificationFile: false
  path: Integer/Tower.py
  requiredBy: []
  timestamp: '2024-12-22 01:32:36+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Integer/Tower.py
layout: document
redirect_from:
- /library/Integer/Tower.py
- /library/Integer/Tower.py.html
title: Integer/Tower.py
---
