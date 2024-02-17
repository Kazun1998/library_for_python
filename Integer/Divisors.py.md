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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.2/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.2/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "#\u7D04\u6570\u5168\u90E8\ndef Divisors(N):\n    N=abs(N)\n    L,U=[],[]\n\
    \    k=1\n    while k*k <=N:\n        if N%k== 0:\n            L.append(k)\n \
    \           if k*k!=N:\n                U.append(N//k)\n        k+=1\n    return\
    \ L+U[::-1]\n\n#\u7D20\u56E0\u6570\u5206\u89E3\u306E\u7D50\u679C\u304B\u3089,\
    \ \u7D04\u6570\u3092\u5168\u3066\u6C42\u3081\u308B.\ndef Divisors_from_Prime_Factor(P,\
    \ sorting=False):\n    X=[1]\n    for p,e in P:\n        q=1\n        n=len(X)\n\
    \        for _ in range(e):\n            q*=p\n            for j in range(n):\n\
    \                X.append(X[j]*q)\n\n    if sorting:\n        X.sort()\n\n   \
    \ return X\n\n#\u9AD8\u5EA6\u5408\u6210\u6570\n#\u53C2\u8003\u5143:https://qiita.com/convexineq/items/e3d599cb9f91a73f936d\n\
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
  timestamp: '2023-03-18 02:55:12+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Integer/Divisors.py
layout: document
redirect_from:
- /library/Integer/Divisors.py
- /library/Integer/Divisors.py.html
title: Integer/Divisors.py
---
