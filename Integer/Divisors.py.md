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
    - https://qiita.com/convexineq/items/e3d599cb9f91a73f936d
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.13.5/x64/lib/python3.13/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.13.5/x64/lib/python3.13/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def Divisors(N: int) -> list[int]:\n    \"\"\" N \u306E\u7D04\u6570\u5168\
    \u4F53\n\n    Args:\n        N (int): 0 \u3067\u306F\u306A\u3044\u6574\u6570\n\
    \n    Returns:\n        list[int]: N \u306E\u300C\u6B63\u306E\u300D\u7D04\u6570\
    \u3092\u6607\u9806\u306B\u4E26\u3079\u305F\u5217\n    \"\"\"\n\n    assert N !=\
    \ 0\n\n    N = abs(N)\n\n    small, large = [], []\n    k = 1\n    while k * k\
    \ <= N:\n        if N % k== 0:\n            small.append(k)\n            large.append(N\
    \ // k)\n\n        k+=1\n\n    # \u5E73\u65B9\u6570\u306E\u3068\u304D, small[-1]\
    \ \u3068 large[-1] \u304C\u91CD\u8907\u3059\u308B\u5024\u306B\u306A\u308B\u306E\
    \u3067, \u4E00\u65B9\u304B\u3089\u524A\u9664\u3059\u308B.\n    if small[-1] ==\
    \ large[-1]:\n        large.pop()\n\n    small.extend(reversed(large))\n    return\
    \ small\n\ndef Divisors_from_Prime_Factor(prime_factors: list[tuple[int, int]],\
    \ sort: bool = False) -> list[int]:\n    \"\"\"prime_factors = [(p0, e0), (p1,\
    \ e1), ...] \u306B\u5BFE\u3057\u3066, N = p0^e0 * p1^e1 * ... \u3068\u3057\u305F\
    \u3068\u304D\u306E N \u306E\u6B63\u306E\u7D04\u6570\u3092\u6C42\u3081\u308B.\n\
    \n    Args:\n        prime_factors (list[tuple[int, int]]): \u7D20\u56E0\u6570\
    \u5206\u89E3\n        sort (bool, optional): True \u306B\u3059\u308B\u3068, \u51FA\
    \u529B\u3055\u308C\u308B\u7D04\u6570\u306E\u30EA\u30B9\u30C8\u304C\u30BD\u30FC\
    \u30C8\u6E08\u307F\u306B\u306A\u308B. Defaults to False.\n\n    Returns:\n   \
    \     list[int]: N = p0^e0 * p1^e1 * ... \u306E\u6B63\u306E\u7D04\u6570\n    \"\
    \"\"\n\n    divisors = [1]\n    for p, e in prime_factors:\n        q = 1\n  \
    \      n = len(divisors)\n        for _ in range(e):\n            q *= p\n   \
    \         for j in range(n):\n                divisors.append(divisors[j] * q)\n\
    \n    if sort:\n        divisors.sort()\n\n    return divisors\n\n#\u9AD8\u5EA6\
    \u5408\u6210\u6570\n#\u53C2\u8003\u5143:https://qiita.com/convexineq/items/e3d599cb9f91a73f936d\n\
    def Highly_Composite_Number(N):\n    \"\"\" N \u4EE5\u4E0B\u306E\u9AD8\u5EA6\u5408\
    \u6210\u6570\u3092\u6C42\u3081\u308B.\n    \"\"\"\n\n    from heapq import heappop,heappush\n\
    \    from math import log\n    prime = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263]\n\
    \    lim = [[2*int(log(p,q)) for q in prime] for p in prime] #\u679D\u5208\u308A\
    \u7528\u914D\u5217\n    # \u521D\u671F\u72B6\u614B\n    q = [(2,2,[1])] # (n,n\u306E\
    \u7D04\u6570\u306E\u500B\u6570\u3001n\u306E\u6307\u6570\u8868\u8A18)\u3092\u4FDD\
    \u5B58\u3059\u308B heapq\n    res = [(1,1,[])]\n\n    while q and q[0][0] <= N:\n\
    \        n,val,lst = heappop(q)\n        if val > res[-1][1]: #\u6761\u4EF6\u3092\
    \u307F\u305F\u3059\u306A\u3089\u7B54\u306B\u8FFD\u52A0\n            res.append((n,val,lst[:]))\n\
    \        L = len(lst)\n        e0 = lst[0]\n        #\u5168\u90E81\u306A\u3089\
    \u65B0\u3057\u3044\u7D20\u6570\u3067\u6A2A\u306B\u4F38\u3070\u305B\u308B\n   \
    \     if e0 == 1:\n            heappush(q,(n*prime[L],val*2,[1]*(L+1)))\n    \
    \    #\u6700\u4E0A\u6BB5\u306E\u4E0A\u3092\u6A2A\u65B9\u5411\u306B\u7A4D\u3080\
    \n        for i in range(L):\n            if e0 > lst[i]: break #\u6BB5\u5DEE\u304C\
    \u3042\u308B\u3068\u3001\u3082\u3046\u4F38\u3070\u305B\u306A\u3044\n         \
    \   if e0 >= lim[L][i]: break #\u679D\u5208\u308A\uFF08\u91CD\u8981\uFF09\n  \
    \          n *= prime[i]\n            if n <= N:\n                lst[i] += 1\n\
    \                val = val//(e0+1)*(e0+2)\n                heappush(q,(n,val,lst[:]))\n\
    \    return res\n"
  dependsOn: []
  isVerificationFile: false
  path: Integer/Divisors.py
  requiredBy: []
  timestamp: '2025-06-29 13:02:45+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Integer/Divisors.py
layout: document
redirect_from:
- /library/Integer/Divisors.py
- /library/Integer/Divisors.py.html
title: Integer/Divisors.py
---
