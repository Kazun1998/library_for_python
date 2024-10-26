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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.7/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.7/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def Knapsack_01_Weight(items, weight):\n    \"\"\" \u975E\u5E38\u306B\u8EFD\
    \u3044 01- \u30CA\u30C3\u30D7\u30B5\u30C3\u30AF\u554F\u984C\u3092\u89E3\u304F\
    .\n\n    items: (\u91CD\u3055, \u4FA1\u5024) \u306E\u5F62\u306E\u30BF\u30D7\u30EB\
    \n    weight: \u30CA\u30C3\u30D7\u30B5\u30C3\u30AF\u306E\u8010\u4E45\u91CD\u91CF\
    \n    \"\"\"\n\n    dp = [0] * (weight + 1)\n    for item in items:\n        if\
    \ item is None:\n            continue\n\n        w, v = item\n        for a in\
    \ range(weight, w - 1, -1):\n            dp[a] = max(dp[a], dp[a - w] + v)\n\n\
    \    packed_value = max(dp)\n    packed_weight = dp.index(packed_value)\n    knapsack\
    \ = []\n    for i, item in enumerate(items):\n        if item is None:\n     \
    \       continue\n\n        w, v = item\n        if (w <= packed_weight) and (dp[packed_weight]\
    \ == dp[packed_weight - w] + v):\n            knapsack.append(i)\n           \
    \ packed_weight -= w\n\n    return { 'value': packed_value, 'knapsack': knapsack\
    \ }\n\ndef Knapsack_01_Value(items, weight):\n    \"\"\" \u4FA1\u5024\u304C\u975E\
    \u5E38\u306B\u5C0F\u3055\u3044 01-Knapsack \u554F\u984C\u3092\u89E3\u304F.\n\n\
    \    items: (\u4FA1\u5024, \u91CD\u3055) \u306E\u5F62\u306E\u30BF\u30D7\u30EB\n\
    \    weight: \u30CA\u30C3\u30D7\u30B5\u30C3\u30AF\u306E\u8010\u4E45\u91CD\u91CF\
    \n\n    [\u8A08\u7B97\u91CF]\n    O(N sum(v))\n    \"\"\"\n\n    v_sum = sum(v\
    \ for _, v in items)\n\n    dp = [weight + 1] * (v_sum + 1)\n    dp[0] = 0\n \
    \   for item in items:\n        if item is None:\n            continue\n\n   \
    \     w, v = item\n        for a in range(v_sum, v - 1, -1):\n            dp[a]\
    \ = min(dp[a], dp[a - v] + w)\n\n    value = pointer = max(v for v in range(v_sum\
    \ + 1) if dp[v] <= weight)\n    knapsack = []\n    for i, item in enumerate(items):\n\
    \        if item is None:\n            continue\n\n        w, v = item\n     \
    \   if dp[pointer] == dp[pointer - v] + w:\n            knapsack.append(i)\n \
    \           pointer -= v\n\n    return { 'value': value, 'knapsack': knapsack\
    \ }\n\ndef Knapsack_01_Middle(List,Weight,Mode=False):\n    \"\"\"\u500B\u6570\
    \u304C\u975E\u5E38\u306B\u5C11\u306A\u304401-Knapsack Problem\u3092 (\u534A\u5206\
    \u5168\u5217\u6319\u3067) \u89E3\u304F.\n\n    List:\u5404\u8981\u7D20\u306F\u30BF\
    \u30D7\u30EB(v,w) \u306E\u5F62\u3067, v\u306F\u4FA1\u5024, w\u306F\u91CD\u3055\
    \n    [\u8A08\u7B97\u91CF]\n    O(N 2^(N/2))\n\n    [\u53C2\u8003\u5143]\n   \
    \ https://tjkendev.github.io/procon-library/python/dp/knapsack-meet-in-the-middle.html\n\
    \    \"\"\"\n\n    def subset_sum(S):\n        T={0:0}\n        for v,w in S:\n\
    \            T1=dict(T)\n            for key,val in T.items():\n             \
    \   a=key+w\n                if a>Weight:\n                    continue\n    \
    \            if a in T1:\n                    T1[a]=max(T1[a],val + v)\n     \
    \           else:\n                    T1[a]=val+v\n            T=T1\n\n     \
    \   v=-1\n        R=[]\n        for w in sorted(T):\n            if T[w]>v:\n\
    \                v=T[w]\n                R.append((v,w))\n        return R\n\n\
    \    def merge(S,T):\n        T=T[::-1]\n        it=iter(T)\n        v1,w1=next(it)\n\
    \n        t=0\n\n        for v,w in S:\n            while w+w1>Weight:\n     \
    \           v1,w1=next(it)\n\n            if t<v+v1:\n                t=v+v1\n\
    \        return t\n\n    N=len(List)\n    A=subset_sum(List[:N//2])\n    B=subset_sum(List[N//2:])\n\
    \    return merge(A,B)\n"
  dependsOn: []
  isVerificationFile: false
  path: Knapsack.py
  requiredBy: []
  timestamp: '2024-02-18 00:28:05+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Knapsack.py
layout: document
redirect_from:
- /library/Knapsack.py
- /library/Knapsack.py.html
title: Knapsack.py
---
