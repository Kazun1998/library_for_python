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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.13.1/x64/lib/python3.13/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.13.1/x64/lib/python3.13/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class Sum_Count:\n    @staticmethod\n    def box_sum(p: int, q: int, r: int,\
    \ s: int, k: int) -> int:\n        \"\"\" p <= x <= q, r <= y <= s, x + y = k\
    \ \u3092\u6E80\u305F\u3059\u6574\u6570\u306E\u7D44 (x, y) \u306E\u6570\u3092\u6C42\
    \u3081\u308B.\n\n        Args:\n            p (int):\n            q (int):\n \
    \           r (int):\n            s (int):\n            k (int):\n\n        Returns:\n\
    \            int: \u7D44\u306E\u6570\n        \"\"\"\n\n        a = max(0, k -\
    \ (p     + r    ) + 1)\n        b = max(0, k - (q + 1 + r    ) + 1)\n        c\
    \ = max(0, k - (p     + s + 1) + 1)\n        d = max(0, k - (q + 1 + s + 1) +\
    \ 1)\n        return a - b - c + d\n\n    @staticmethod\n    def interval_sum(l:\
    \ int, r: int, a: int, b: int) -> int:\n        \"\"\" l <= x <= y, l <= x <=\
    \ r, a <= x + y <= b \u3092\u6E80\u305F\u3059\u6574\u6570\u306E\u7D44 (x, y) \u306E\
    \u6570\u3092\u6C42\u3081\u308B.\n\n        Args:\n            l (int):\n     \
    \       r (int):\n            a (int):\n            b (int):\n\n        Returns:\n\
    \            int: \u7D44\u306E\u6570\n        \"\"\"\n        if not(l <= r and\
    \ a <= b):\n            return 0\n\n        a = max(a, 2 * l)\n        b = min(b,\
    \ 2 * r)\n\n        if not(2 * l <= b and a <= 2 * r):\n            return 0\n\
    \n        linear_sum = lambda a, b, l, r: (a * (l + r) + 2 *b) * (r - l + 1) //\
    \ 2\n\n        if a <= l + r < b:\n            return linear_sum(1, - 2 * l +\
    \ 1, a, l + r) + linear_sum(-1 ,2 * r + 1, l + r + 1, b)\n        else:\n    \
    \        if b <= l + r:\n                return linear_sum(1, - 2 * l + 1, a,\
    \ b)\n            else:\n                return linear_sum(-1, 2 * r + 1, a, b)\n\
    \n    @staticmethod\n    def range_sum_dp(ranges, S: int, Mod: int = None):\n\
    \        \"\"\" ranges = [(a_0, b_0), (a_1, b_1), ..., (a_{N-1}, b_{N-1})] \u3068\
    \u3057\u305F\u3068\u304D,\n        a_i <= x_i <= b_i, x_0 + x_1 + ... + x_{N-1}\
    \ = y \u3092\u6E80\u305F\u3059\u6574\u6570\u306E\u7D44\u306E\u6570\u3092 y = 0,\
    \ 1, ..., S \u306B\u5BFE\u3057\u3066\u6C42\u3081\u308B.\n        (Mod \u304C None\
    \ \u3067\u306A\u3044\u3068\u304D\u306F, \u7D44\u306E\u6570\u3092 Mod \u3067\u5272\
    \u3063\u305F\u4F59\u308A.)\n\n        Args:\n            ranges: (a, b) \u306E\
    \u5F62\u306E\u30BF\u30D7\u30EB\n            S (int): \u4E0A\u9650\n          \
    \  Mod (int, optional): \u6CD5. Defaults to None.\n        \"\"\"\n\n        dp\
    \ = [0] * (S + 1); dp[0] = 1\n        prev_cum = [0] * (S + 1)\n\n        for\
    \ a, b in ranges:\n            # dp \u306E\u7D2F\u7A4D\u548C\u3092\u53D6\u308B\
    \n            prev_cum[0] = dp[0]\n            for x in range(1, S + 1):\n   \
    \             prev_cum[x] = prev_cum[x - 1] + dp[x]\n\n            if Mod is not\
    \ None:\n                for x in range(S):\n                    prev_cum[x] %=\
    \ Mod\n\n            for x in range(S + 1):\n                if x < a:\n     \
    \               dp[x] = 0\n                elif x <= b:\n                    dp[x]\
    \ = prev_cum[x - a]\n                else:\n                    dp[x] = prev_cum[x\
    \ - a] - prev_cum[x - b - 1]\n\n        if Mod is None:\n            return dp\n\
    \        else:\n            return [y % Mod for y in dp]\n"
  dependsOn: []
  isVerificationFile: false
  path: Summation/Count.py
  requiredBy: []
  timestamp: '2025-01-19 11:40:17+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Summation/Count.py
layout: document
redirect_from:
- /library/Summation/Count.py
- /library/Summation/Count.py.html
title: Summation/Count.py
---
