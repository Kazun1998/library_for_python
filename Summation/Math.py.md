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
  code: "class Sum:\n    @staticmethod\n    def linear(a: int, b: int, l: int, r:\
    \ int) -> int:\n        \"\"\" sum_{k=l}^r (a k + b) \u3092\u6C42\u3081\u308B\n\
    \n        Args:\n            a (int): 1 \u6B21\u306E\u9805\n            b (int):\
    \ \u5B9A\u6570\u9805\n            l (int):\n            r (int):\n\n        Returns:\n\
    \            int: \u7DCF\u548C\n        \"\"\"\n\n        return (a * (l + r)\
    \ + 2 * b) * (r - l + 1) // 2 if l <= r else 0\n\n    @classmethod\n    def max_linear(cls,\
    \ a: int, b: int, c: int, d: int, l: int, r: int) -> int:\n        \"\"\" sum_{k\
    \ = l}^r max(a k + b, c k + d) \u3092\u6C42\u3081\u308B.\n\n        Args:\n  \
    \          a (int):\n            b (int):\n            c (int):\n            d\
    \ (int):\n            l (int):\n            r (int):\n\n        Returns:\n   \
    \         int:\n        \"\"\"\n\n        if l > r:\n            return 0\n\n\
    \        if a == c:\n            return cls.linear(a, max(b, d), l, r)\n\n   \
    \     if a < c:\n            a, b, c, d = c, d, a, b\n\n        if a * l + b >\
    \ c * l + d:\n            return cls.linear(a, b, l, r)\n        elif a * r +\
    \ b < c * r + d:\n            return cls.linear(c, d, l, r)\n\n        m = (d\
    \ - b) // (a - c)\n        return cls.linear(c, d, l, m) + cls.linear(a, b, m\
    \ + 1, r)\n\n    @classmethod\n    def min_linear(cls, a: int, b: int, c: int,\
    \ d: int, l: int, r: int):\n        \"\"\" sum_{k = l}^r min(a k + b, c k + d)\
    \ \u3092\u6C42\u3081\u308B.\n\n        Args:\n            a (int):\n         \
    \   b (int):\n            c (int):\n            d (int):\n            l (int):\n\
    \            r (int):\n\n        Returns:\n            int:\n        \"\"\"\n\n\
    \        return -cls.max_linear(-a, -b, -c, -d, l, r)\n\n    @classmethod\n  \
    \  def linear_lower_cut(cls, a: int, b: int, d: int, l: int, r: int) -> int:\n\
    \        \"\"\" sum_{k=l}^r max(ak+b, d) \u3092\u6C42\u3081\u308B.\n\n       \
    \ Args:\n            a (int):\n            b (int):\n            d (int):\n  \
    \          l (int):\n            r (int):\n\n        Returns:\n            int:\n\
    \        \"\"\"\n\n        return cls.max_linear(a, b, 0, d, l, r)\n\n    @classmethod\n\
    \    def linear_upper_cut(cls, a: int, b: int, u: int, l: int, r: int) -> int:\n\
    \        \"\"\" sum_{k=l}^r min(ak+b, u) \u3092\u6C42\u3081\u308B.\n\n       \
    \ Args:\n            a (int):\n            b (int):\n            d (int):\n  \
    \          l (int):\n            r (int):\n\n        Returns:\n            int:\n\
    \        \"\"\"\n\n        return cls.min_linear(a, b, 0, u, l, r)\n\n    @classmethod\n\
    \    def bound(cls, a: int, b: int, d: int, u: int, l: int, r: int) -> int:\n\
    \        \"\"\" p[k]:=ak+b, q[k]:= u (u <= p[k]), d (d>=p[k]), p[k] (otherwise)\
    \ \u3068\u3057\u305F\u3068\u304D, sum_{k = l}^r q[k] \u3092\u6C42\u3081\u308B\
    .\n\n        Args:\n            a (int):\n            b (int):\n            d\
    \ (int):\n            u (int):\n            l (int):\n            r (int):\n\n\
    \        Returns:\n            int:\n        \"\"\"\n        assert d <= u\n\n\
    \        if l > r:\n            return 0\n\n        if a == 0:\n            return\
    \ max(d, min(b, u)) * (r - l + 1)\n\n        X = 0\n        if a > 0:\n      \
    \      s = (d - b + a -1) // a\n            t = (u - b) // a\n\n            if\
    \ r < s:\n                return d * (r - l + 1)\n            elif t < l:\n  \
    \              return u * (r - l + 1)\n\n            if l < s:\n             \
    \   X += d * (s - l)\n                l = s\n            if t < r:\n         \
    \       X += u * (r - t)\n                r = t\n        elif a < 0:\n       \
    \     a_abs = abs(a)\n            s = (b - u + a_abs - 1) // a_abs\n         \
    \   t = (b - d) // a_abs\n\n            if r < s:\n                return u *\
    \ (r - l + 1)\n            elif t < l:\n                return d * (r - l + 1)\n\
    \n            if l < s:\n                X += u * (s - l)\n                l =\
    \ s\n            if t < r:\n                X += d * (r - t)\n               \
    \ r = t\n\n        X += cls.linear(a, b, l, r)\n        return X\n\n#==================================================\n\
    #Sum_Count\u7CFB\ndef Range_Sum_Inclusion(Range, S, Mod=None):\n    \"\"\"Range=[(A_0,B_0),...,(A_{N-1},\
    \ B_{N-1})] \u3068\u3057\u3068\u305F\u304D,\n    A_i<=X_i<=B_i, X_0+...+X_{n-1}=S\
    \ \u3092\u6E80\u305F\u3059\u7D44\u306E\u500B\u6570\u3092\u5305\u9664\u539F\u7406\
    \u3067\u6C42\u3081\u308B.\n\n    0<=A_i<=B_i\n    0<=S\n    \u8A08\u7B97\u91CF\
    : O(N2^N)\n    \"\"\"\n    from itertools import product\n\n    def nCr(n,r):\n\
    \        if n<0: return 0\n        if r<0 or n<r: return 0\n\n        a=b=1\n\
    \        r=min(r,n-r)\n\n        while r:\n            a*=n; b*=r\n\n        \
    \    if Mod!=None:\n                a%=Mod; b%=Mod\n\n            n-=1; r-=1\n\
    \n        if Mod!=None:\n            return (a * pow(b, -1, Mod)) % Mod\n    \
    \    else:\n            return a//b\n\n    def nHr(n,r):\n        if n==r==0:\n\
    \            return 1\n        else:\n            return nCr(n+r-1,n-1)\n\n  \
    \  N=len(Range)\n    X=0\n    for p in product((0,1),repeat=N):\n        T=S\n\
    \        for i in range(N):\n            a,b=Range[i]\n            if p[i]:\n\
    \                T-=b+1\n            else:\n                T-=a\n\n        X+=pow(-1,sum(p))*nHr(N,T)\n\
    \n    if Mod==None:\n        return X\n    else:\n        return X%Mod\n\n#==================================================\n\
    #Find_Sum\u7CFB\ndef Find_Range_Sum(Range, S):\n    \"\"\"Range=[(A_0,B_0),...,(A_{N-1},\
    \ B_{N-1})] \u3068\u3057\u3068\u305F\u304D,\n    A_i<=X_i<=B_i, X_0+...+X_{n-1}=S\
    \ \u3092\u6E80\u305F\u3059\u7D44\u306E\u4F8B\u30921\u3064\u6C42\u3081\u308B.\n\
    \n    A_i<=B_i\n    \"\"\"\n\n    alpha=beta=0\n    for a,b in Range:\n      \
    \  alpha+=a\n        beta +=b\n\n    if not (alpha<=S<=beta): return None\n\n\
    \    N=len(Range)\n    X=[a for a,_ in Range]\n    remain=S-sum(X)\n    for i\
    \ in range(N):\n        y=min(Range[i][1],X[i]+remain)\n        remain-=y-X[i]\n\
    \        X[i]=y\n    return X\n#==================================================\n\
    #\u5E7E\u4F55\u7D1A\u6570\u7CFB\n\ndef Geometric_Sequence_Sum(r, n, Mod=None):\n\
    \    \"\"\" sum_{i=0}^{n-1} r^i [(mod Mod)] \"\"\"\n\n    if Mod==None:\n    \
    \    if r==1: return n\n        else: return (pow(r,n)-1)/(r-1)\n    else:\n \
    \       if r==1: return n%Mod\n        else: return (pow(r,n,(r-1)*Mod)//(r-1))%Mod\n"
  dependsOn: []
  isVerificationFile: false
  path: Summation/Math.py
  requiredBy: []
  timestamp: '2025-01-19 11:40:17+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Summation/Math.py
layout: document
redirect_from:
- /library/Summation/Math.py
- /library/Summation/Math.py.html
title: Summation/Math.py
---
