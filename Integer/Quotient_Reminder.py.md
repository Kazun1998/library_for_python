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
  code: "#\u5546\u5217\u6319\ndef Quotient_Range(N):\n    \"\"\" N \u3067\u5272\u3063\
    \u305F\u5546\u306E\u53EF\u80FD\u6027\u3092\u5168\u3066\u5217\u6319\u3059\u308B\
    .\n\n    [Input]\n    N: \u6B63\u6574\u6570\n\n    [Output]\n    X: \u30EA\u30B9\
    \u30C8\n    X\u306E\u5404\u8981\u7D20 (t, x, y) \u306F x <= k <= y \u3067\u3042\
    \u308B\u3053\u3068\u3068, floor(N/k) = t \u304C\u540C\u5024\u3067\u3042\u308B\u3053\
    \u3068\u3092\u8868\u3059.\n\n    [Note]\n    \u5404 (t, x, y) \u306B\u5BFE\u3057\
    \u3066, x <= k <= y \u306E\u7BC4\u56F2\u306B\u304A\u3044\u3066, N mod k \u306F\
    \u7B49\u5DEE\u6570\u5217\u306B\u306A\u308B.\n    \"\"\"\n    X = []\n\n    # Step\
    \ 1: k<=sqrt(N) \u306E\u7BC4\u56F2\u306B\u3064\u3044\u3066 k \u3092\u5168\u63A2\
    \u7D22\u3059\u308B.\n    k = 1\n    while k * k <= N:\n        X.append((N//k,\
    \ k, k))\n        k += 1\n\n    # Step 2: t<=sqrt(N) \u306E\u7BC4\u56F2\u306B\u304A\
    \u3044\u3066, floor(N/k)=t \u3092\u6E80\u305F\u3059 k \u306E\u7BC4\u56F2\u3092\
    \u6C42\u3081\u308B.\n    for t in range(k, 0, -1):\n        l = N//(t + 1) + 1\n\
    \        r = N//t\n\n        if (l <= r) and (X[-1][1] < l):\n            X.append((t,\
    \ l, r))\n\n    return X\n\ndef Quotient_Range_Yielder(N):\n    \"\"\" N \u3067\
    \u5272\u3063\u305F\u5546\u306E\u53EF\u80FD\u6027\u3092\u5168\u3066\u5217\u6319\
    \u3059\u308B.\n\n    [Input]\n    N: \u6B63\u6574\u6570\n\n    [Output]\n    X:\
    \ \u30EA\u30B9\u30C8\n    X\u306E\u5404\u8981\u7D20 (t, x, y) \u306F x <= k <=\
    \ y \u3067\u3042\u308B\u3053\u3068\u3068, floor(N/k) = t \u304C\u540C\u5024\u3067\
    \u3042\u308B\u3053\u3068\u3092\u8868\u3059.\n\n    [Note]\n    \u5404 (t, x, y)\
    \ \u306B\u5BFE\u3057\u3066, x <= k <= y \u306E\u7BC4\u56F2\u306B\u304A\u3044\u3066\
    , N mod k \u306F\u7B49\u5DEE\u6570\u5217\u306B\u306A\u308B.\n    \"\"\"\n\n  \
    \  # Step 1: k<=sqrt(N) \u306E\u7BC4\u56F2\u306B\u3064\u3044\u3066 k \u3092\u5168\
    \u63A2\u7D22\u3059\u308B.\n    k = 1\n    while k * k <= N:\n        yield (N//k,\
    \ k, k)\n        k += 1\n\n    # Step 2: t<=sqrt(N) \u306E\u7BC4\u56F2\u306B\u304A\
    \u3044\u3066, floor(N/k)=t \u3092\u6E80\u305F\u3059 k \u306E\u7BC4\u56F2\u3092\
    \u6C42\u3081\u308B.\n    prev_l = k - 1\n    for t in range(k, 0, -1):\n     \
    \   l = N//(t + 1) + 1\n        r = N//t\n\n        if (l <= r) and (prev_l <\
    \ l):\n            yield (t, l, r)\n            prev_l = l\n\ndef Ceiling_Range(N,\
    \ left = None):\n    \"\"\" \u975E\u8CA0\u6574\u6570 x \u3092\u5168\u3066\u8D70\
    \u308B\u3068\u304D\u306E ceil(N/x) \u306E\u53EF\u80FD\u6027\u3092\u5168\u3066\u5217\
    \u6319\u3059\u308B.\n\n    [Input]\n    N: \u6B63\u6574\u6570\n\n    [Output]\n\
    \    X: \u30EA\u30B9\u30C8\n    X \u306E\u5404\u8981\u7D20 (t, x, y) \u306F x\
    \ <= k <= y \u3067\u3042\u308B\u3053\u3068\u3068, ceil(N/k) = t \u304C\u540C\u5024\
    \u3067\u3042\u308B\u3053\u3068\u3092\u8868\u3059.\n\n    \"\"\"\n\n    from math\
    \ import isqrt\n\n    N_sqrt = isqrt(N)\n    ceil = lambda k: (N + k - 1) // k\n\
    \    X = []\n\n    # Step 1: ceil(N/k) < N_sqrt \u3068\u306A\u308B k \u306E\u7BC4\
    \u56F2\u3067\u500B\u5225\u306B\u6C42\u3081\u308B.\n    k = 1\n    while True:\n\
    \        if ceil(k) == N_sqrt:\n            break\n\n        X.append((ceil(k),\
    \ k, k))\n        k += 1\n\n    # Step 2: ceil(N/k) >= N_sqrt \u3068\u306A\u308B\
    \ k \u306E\u7BC4\u56F2\u3092\u307E\u3068\u3081\u4E0A\u3052\u308B.\n    for t in\
    \ range(N_sqrt, 1, -1):\n        l = ceil(t)\n        r = ceil(t - 1) - 1\n  \
    \      if (l <= r) and (X[-1][1] < l):\n            X.append((t, l, r))\n\n  \
    \  if left == None:\n        X.append((1, N, float(\"inf\")))\n    else:\n   \
    \     left = max(left, N)\n        X.append((1, N, left))\n\n    return X\n\n\
    def Ceiling_Range_Yielder(N, left = None):\n    \"\"\" \u975E\u8CA0\u6574\u6570\
    \ x \u3092\u5168\u3066\u8D70\u308B\u3068\u304D\u306E ceil(N/x) \u306E\u53EF\u80FD\
    \u6027\u3092\u5168\u3066\u5217\u6319\u3059\u308B.\n\n    [Input]\n    N: \u6B63\
    \u6574\u6570\n\n    [Output]\n    X: \u30EA\u30B9\u30C8\n    X \u306E\u5404\u8981\
    \u7D20 (t, x, y) \u306F x <= k <= y \u3067\u3042\u308B\u3053\u3068\u3068, ceil(N/k)\
    \ = t \u304C\u540C\u5024\u3067\u3042\u308B\u3053\u3068\u3092\u8868\u3059.\n\n\
    \    \"\"\"\n\n    from math import isqrt\n\n    N_sqrt = isqrt(N)\n    ceil =\
    \ lambda k: (N + k - 1) // k\n\n    # Step 1: ceil(N/k) < N_sqrt \u3068\u306A\u308B\
    \ k \u306E\u7BC4\u56F2\u3067\u500B\u5225\u306B\u6C42\u3081\u308B.\n    k = 1\n\
    \    while True:\n        if ceil(k) == N_sqrt:\n            break\n\n       \
    \ yield (ceil(k), k, k)\n        k += 1\n\n    # Step 2: ceil(N/k) >= N_sqrt \u3068\
    \u306A\u308B k \u306E\u7BC4\u56F2\u3092\u307E\u3068\u3081\u4E0A\u3052\u308B.\n\
    \    prev_r = k - 1\n    for t in range(N_sqrt, 1, -1):\n        l = ceil(t)\n\
    \        r = ceil(t - 1) - 1\n        if (l <= r) and (prev_r < l):\n        \
    \    yield (t, l, r)\n            prev_l = r\n\n    if left == None:\n       \
    \ yield (1, N, float(\"inf\"))\n    else:\n        left = max(left, N)\n     \
    \   yield (1, N, left)\n\ndef Reminder_Enumeration(N, r):\n    \"\"\" N \u3092\
    \ q \u5272\u3063\u305F\u4F59\u308A\u304C r \u306B\u306A\u308B q \u3092\u5168\u3066\
    \u5217\u6319\u3059\u308B.\n\n    N: \u6B63\u6574\u6570\n    r: \u975E\u8CA0\u6574\
    \u6570, N != r\n    \"\"\"\n\n    assert N != r, \"\u7121\u9650\u500B\u3042\u308A\
    \u307E\u3059.\"\n\n    k = 1\n    X = []; Y = []\n    N -= r\n    while k * k\
    \ <= N:\n        if N % k == 0:\n            if k > r:\n                X.append(k)\n\
    \            if k * k != N and N//k > r:\n                Y.append(N//k)\n   \
    \     k += 1\n    return X + Y[::-1]\n\ndef Next_Remainder(x, p, r):\n    \"\"\
    \" x \u4EE5\u4E0A\u3067 p \u3067\u5272\u3063\u3066 r \u4F59\u308B\u6574\u6570\u306E\
    \u3046\u3061, \u6700\u5C0F\u306E\u6574\u6570\u3092\u6C42\u3081\u308B.\n\n    \"\
    \"\"\n\n    if x % p <= r:\n        return (x//p) * p + r\n    else:\n       \
    \ return (x//p + 1) * p + r\n\ndef Previous_Remainder(x, p, r):\n    \"\"\" x\
    \ \u4EE5\u4E0B\u3067 p \u3067\u5272\u3063\u3066 r \u4F59\u308B\u6574\u6570\u306E\
    \u3046\u3061, \u6700\u5927\u306E\u6574\u6570\u3092\u6C42\u3081\u308B.\n\n    \"\
    \"\"\n\n    if r <= x % p:\n        return (x//p) * p + r\n    else:\n       \
    \ return (x//p - 1) * p + r\n"
  dependsOn: []
  isVerificationFile: false
  path: Integer/Quotient_Reminder.py
  requiredBy: []
  timestamp: '2023-09-16 20:08:08+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Integer/Quotient_Reminder.py
layout: document
redirect_from:
- /library/Integer/Quotient_Reminder.py
- /library/Integer/Quotient_Reminder.py.html
title: Integer/Quotient_Reminder.py
---
