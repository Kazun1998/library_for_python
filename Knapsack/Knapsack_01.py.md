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
    - https://tjkendev.github.io/procon-library/python/dp/knapsack-meet-in-the-middle.html
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.13.1/x64/lib/python3.13/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.13.1/x64/lib/python3.13/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class Knapsack_item:\n    def __init__(self, value, weight):\n        self.value\
    \ = value\n        self.weight = weight\n\n    def __repr__(self):\n        return\
    \ f\"value: {self.value}, weight: {self.weight}\"\n\n    __str__ = __repr__\n\n\
    class Knapsack_01:\n    @classmethod\n    def solve(cls, items, capacity):\n \
    \       \"\"\" 01-Knapsack \u554F\u984C\u3092\u89E3\u304F\n        \"\"\"\n\n\
    \        from math import log2\n\n        n = max(len(items), 1)\n        cost_by_middle\
    \ = n * log2(n)\n        cost_by_weight = log2(n * max(capacity, 1))\n       \
    \ cost_by_value = log2(n * max(sum(item.value for item in items), 1))\n      \
    \  min_cost = min(cost_by_middle, cost_by_value, cost_by_weight)\n\n        if\
    \ min_cost == cost_by_middle:\n            return cls.solve_small(items, capacity)\n\
    \        elif min_cost == cost_by_weight:\n            return cls.solve_weight(items,\
    \ capacity)\n        else:\n            return cls.solve_value(items, capacity)\n\
    \n    @classmethod\n    def solve_weight(_, items: list[Knapsack_item], capacity:\
    \ int):\n        \"\"\" \u5404\u30A2\u30A4\u30C6\u30E0\u306E\u91CD\u3055\u304C\
    \u8EFD\u3044\u5834\u5408\u306E 01-Knapsack \u554F\u984C\u3092\u89E3\u304F.\n\n\
    \        Args:\n            items (list[Knapsack_item]): \u30A2\u30A4\u30C6\u30E0\
    \u306E\u30EA\u30B9\u30C8\n            weight (int): \u30CA\u30C3\u30D7\u30B5\u30C3\
    \u30AF\u306E\u5BB9\u91CF\n        \"\"\"\n\n        dp = [0] * (capacity + 1)\n\
    \        for item in items:\n            if item is None:\n                continue\n\
    \n            for a in range(capacity, item.weight - 1, -1):\n               \
    \ dp[a] = max(dp[a], dp[a - item.weight] + item.value)\n\n        packed_value\
    \ = max(dp)\n        packed_weight = dp.index(packed_value)\n        knapsack\
    \ = []\n        for i, item in enumerate(items):\n            if item is None:\n\
    \                continue\n\n            if (item.weight <= packed_weight) and\
    \ (dp[packed_weight] == dp[packed_weight - item.weight] + item.value):\n     \
    \           knapsack.append(i)\n                packed_weight -= item.weight\n\
    \n        return { 'value': packed_value, 'packed': knapsack }\n\n    @classmethod\n\
    \    def solve_value(_, items: list[Knapsack_item], capacity: int):\n        \"\
    \"\" \u5404\u30A2\u30A4\u30C6\u30E0\u306E\u4FA1\u5024\u304C\u5C0F\u3055\u3044\
    \ 01-Knapsack \u554F\u984C\u3092\u89E3\u304F.\n\n        Args:\n            items\
    \ (list[Knapsack_item]): \u30A2\u30A4\u30C6\u30E0\u306E\u30EA\u30B9\u30C8\n  \
    \          weight (int): \u30CA\u30C3\u30D7\u30B5\u30C3\u30AF\u306E\u5BB9\u91CF\
    \n        \"\"\"\n\n        value_sum = sum(item.value for item in items)\n  \
    \      dp = [capacity + 1] * (value_sum + 1)\n        dp[0] = 0\n\n        for\
    \ item in items:\n            if item is None:\n                continue\n\n \
    \           for a in range(value_sum, item.value - 1, -1):\n                dp[a]\
    \ = min(dp[a], dp[a - item.value] + item.weight)\n\n        value = pointer =\
    \ max(v for v in range(value_sum+ 1) if dp[v] <= capacity)\n        knapsack =\
    \ []\n        for i, item in enumerate(items):\n            if item is None:\n\
    \                continue\n\n            if dp[pointer] == dp[pointer - item.value]\
    \ + item.weight:\n                knapsack.append(i)\n                pointer\
    \ -= item.value\n\n        return { 'value': value, 'packed': knapsack }\n\n \
    \   @classmethod\n    def __subset_sum(_, items: list[Knapsack_item], capacity:\
    \ int):\n        def bit(x, k):\n            return (x >> k) & 1\n\n        memo\
    \ = { }\n        n = len(items)\n        for E in range(1 << n):\n           \
    \ partial_value = 0\n            partial_weight = 0\n\n            for i in range(n):\n\
    \                if bit(E, i) == 0:\n                    continue\n\n        \
    \        partial_value += items[i].value\n                partial_weight += items[i].weight\n\
    \n            if partial_weight > capacity:\n                continue\n\n    \
    \        if partial_weight in memo:\n                memoed_value, F = memo[partial_weight]\n\
    \                if memoed_value <= partial_value:\n                    memo[partial_weight]\
    \ = (partial_value, F)\n            else:\n                memo[partial_weight]\
    \ = (partial_value, E)\n\n        champion_value = -1\n        res = []\n    \
    \    for key in sorted(memo):\n            value, E = memo[key]\n            if\
    \ value <= champion_value:\n                continue\n\n            res.append((value,\
    \ key, E))\n            champion_value = value\n        return res\n\n    @classmethod\n\
    \    def __merge(cls, S, T, capacity):\n        T.reverse()\n        it = iter(T)\n\
    \        v1, w1, F = next(it)\n\n        t = 0\n        E0 = 0\n        F0 = 0\n\
    \n        for v, w, E in S:\n            while w + w1 > capacity:\n          \
    \      v1, w1, F = next(it)\n\n            if t < v + v1:\n                t =\
    \ v + v1\n                E0 = E\n                F0 = F\n\n        return t,\
    \ E0, F0\n\n    @classmethod\n    def solve_small(cls, items: list[Knapsack_item],\
    \ capacity: int):\n        \"\"\" \u30A2\u30A4\u30C6\u30E0\u306E\u500B\u6570\u304C\
    \u5C0F\u3055\u3044 01-Knapsack \u554F\u984C\u3092\u89E3\u304F.\n\n        Args:\n\
    \            items (list[Knapsack_item]): \u30A2\u30A4\u30C6\u30E0\u306E\u30EA\
    \u30B9\u30C8\n            capacity (int): \u30CA\u30C3\u30D7\u30B5\u30C3\u30AF\
    \u306E\u5BB9\u91CF\n\n        Reference:\n            https://tjkendev.github.io/procon-library/python/dp/knapsack-meet-in-the-middle.html\n\
    \        \"\"\"\n\n        n = len(items)\n        A = cls.__subset_sum(items[:n//2],\
    \ capacity)\n        B = cls.__subset_sum(items[n//2:], capacity)\n\n        value,\
    \ E, F  = cls.__merge(A, B, capacity)\n        E_bit = [i for i in range(n //\
    \ 2) if (E >> i) & 1 ]\n        F_bit = [j for j in range(n // 2, n) if (F >>\
    \ j) & 1]\n\n        return { 'value': value, 'packed': E_bit + [f + n // 2 for\
    \ f in F_bit] }\n"
  dependsOn: []
  isVerificationFile: false
  path: Knapsack/Knapsack_01.py
  requiredBy: []
  timestamp: '2024-12-01 01:34:56+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Knapsack/Knapsack_01.py
layout: document
redirect_from:
- /library/Knapsack/Knapsack_01.py
- /library/Knapsack/Knapsack_01.py.html
title: Knapsack/Knapsack_01.py
---
