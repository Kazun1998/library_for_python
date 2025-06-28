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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.13.5/x64/lib/python3.13/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.13.5/x64/lib/python3.13/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class Permutation:\n    __slots__ = ('_n', '__p', '__ind')\n\n    def __init__(self,\
    \ p: list[int] = None):\n        \"\"\" N \u8981\u7D20\u306E\u7F6E\u63DB\u3092\
    \u751F\u6210\u3059\u308B.\n\n        Args:\n            p (list[int], optional):\
    \ \u521D\u671F\u72B6\u614B. None \u306E\u3068\u304D\u306F\u6052\u7B49\u7F6E\u63DB\
    \u306B\u306A\u308B. Defaults to None.\n        \"\"\"\n\n        if p is None:\n\
    \            p = list(range(n))\n\n        n = len(p)\n        ind = [0] * n\n\
    \n        for i in range(n):\n            ind[p[i]] = i\n\n        self.__p =\
    \ p\n        self.__ind = ind\n        self._n = n\n\n    @property\n    def N(self)\
    \ -> int:\n        return self._n\n\n    def __getitem__(self, k: int) -> int:\n\
    \        return self.__p[k]\n\n    def __str__(self) -> str:\n        return str(self.__p)\n\
    \n    def __repr__(self) -> str:\n        return f\"{self.__class__.__name__}({self.p})\"\
    \n\n    def __eq__(self, other: \"Permutation\") -> bool:\n        return (self.N\
    \ == other.N) and (self.__p == other.__p)\n\n    def __iter__(self):\n       \
    \ return iter(self.__p)\n\n    def __len__(self) -> int:\n        return self.N\n\
    \n    def index(self, x: int) -> int:\n        return self.__ind[x]\n\n    def\
    \ __mul__(self, other: \"Permutation\") -> \"Permutation\":\n        assert self.N\
    \ == other.N\n\n        p = self.__p\n        q = other.__p\n        return Permutation([p[q[i]]\
    \ for i in range(self.N)])\n\n    def __pow__(self, k: int) -> \"Permutation\"\
    :\n        if k < 0:\n            return pow(self, -k).inverse()\n\n        N\
    \ = len(self)\n        a = list(range(N))\n        e = self.__p[:]\n\n       \
    \ while k:\n            if k & 1:\n                a = [a[e[i]] for i in range(N)]\n\
    \            e = [e[e[i]] for i in range(N)]\n            k >>= 1\n\n        return\
    \ Permutation(a)\n\n    def sgn(self) -> int:\n        \"\"\" \u7F6E\u63DB\u306E\
    \u7B26\u53F7\u3092\u6C42\u3081\u308B\n\n        Returns:\n            int: \u5076\
    \u7F6E\u63DB\u306A\u3089\u3070 +1, \u5947\u7F6E\u63DB\u306A\u3089\u3070 -1\n \
    \       \"\"\"\n\n        return -1 if self.minimum_transposition() % 2 else 1\n\
    \n    def inverse(self) -> \"Permutation\":\n        \"\"\" \u9006\u7F6E\u63DB\
    \u3092\u6C42\u3081\u308B.\n\n        Returns:\n            Permutation: \u9006\
    \u7F6E\u63DB\n        \"\"\"\n\n        return Permutation(self.__ind)\n\n   \
    \ def inversion(self) -> int:\n        \"\"\" \u8EE2\u5012\u6570\u3092\u6C42\u3081\
    \u308B.\n\n        Returns:\n            int: \u8EE2\u5012\u6570\n        \"\"\
    \"\n\n        BIT = [0] * (len(self) + 1)\n        y = (self.N * (self.N - 1))\
    \ // 2\n\n        for a in self.__p:\n            s = a\n            while 1 <=\
    \ s:\n                y -= BIT[s]\n                s -= s & (-s)\n\n         \
    \   r = a + 1\n            while r <= self.N:\n                BIT[r] += 1\n \
    \               r += r & (-r)\n        return y\n\n    def swap(self, i: int,\
    \ j: int):\n        \"\"\" i \u756A\u76EE\u3068 j \u756A\u76EE\u3092\u4EA4\u63DB\
    \u3059\u308B (\u203B i \u3068 j \u3092\u4EA4\u63DB\u3067\u306F\u306A\u3044)\n\n\
    \        Args:\n            i (int):\n            j (int):\n        \"\"\"\n\n\
    \        u=self.__p[i]; v=self.__p[j]\n\n        self.__p[i]=v; self.__p[j]=u\n\
    \        self.__ind[v]=i; self.__ind[u]=j\n\n    def transposition(self, u: int,\
    \ v: int):\n        \"\"\" u \u3068 v \u3092\u4EA4\u63DB\u3059\u308B (\u203B u\
    \ \u756A\u76EE\u3068 v \u756A\u76EE\u3067\u306F\u306A\u3044)\n\n        Args:\n\
    \            u (int):\n            v (int):\n        \"\"\"\n\n        a=self.__ind[u];\
    \ b=self.__ind[v]\n\n        self.__p[a]=v; self.__p[b]=u\n        self.__ind[u]=b;\
    \ self.__ind[v]=a\n\n    def minimum_transposition(self) -> int:\n        \"\"\
    \" \u4E92\u63DB\u306E\u6700\u5C0F\u56DE\u6570\u3092\u6C42\u3081\u308B.\n\n   \
    \     Returns:\n            int: \u4E92\u63DB\u306E\u6700\u5C0F\u56DE\u6570\n\
    \        \"\"\"\n\n        return len(self) - len(self.cycle_division())\n\n \
    \   def cycle_division(self, self_loop = True) -> list[list[int]]:\n        \"\
    \"\" \u7F6E\u63DB\u3092\u5DE1\u56DE\u7F6E\u63DB\u306E\u7A4D\u306B\u5206\u89E3\u3059\
    \u308B.\n\n        Args:\n            self_loop (bool, optional): \u9577\u3055\
    \ 1 \u306E\u81EA\u5DF1\u30EB\u30FC\u30D7\u3092\u5165\u308C\u308B\u304B\u3069\u3046\
    \u304B. Defaults to True.\n\n        Returns:\n            list[list[int]]: \u5404\
    \u8981\u7D20\u304C\u30B5\u30A4\u30AF\u30EB\u306B\u306A\u308B.\n        \"\"\"\n\
    \n        N = len(self)\n        p = self.__p\n        seen = [False] * N\n  \
    \      cycles: list[list[int]] = []\n\n        for k in range(N):\n          \
    \  if seen[k]:\n                continue\n\n            cycle = [k]\n        \
    \    seen[k] = True\n            v = k\n\n            while (v := p[v]) != k:\n\
    \                seen[v] = True\n                cycle.append(v)\n\n         \
    \   if self_loop or len(cycle)>=2:\n                cycles.append(cycle)\n\n \
    \       return cycles\n\n    def operate_list(self, list: list) -> list:\n   \
    \     \"\"\" \u7F6E\u63DB\u3092\u30EA\u30B9\u30C8\u306B\u4F5C\u7528\u3055\u305B\
    \u308B.\n\n        Args:\n            list (list): \u4F5C\u7528\u5148\u306E\u30EA\
    \u30B9\u30C8\n\n        Returns:\n            list: \u4F5C\u7528\u5F8C\u306E\u30EA\
    \u30B9\u30C8\n        \"\"\"\n\n        if len(self) != len(list):\n         \
    \   raise ValueError(\"\u7F6E\u63DB\u306E\u9577\u3055\u3068\u30EA\u30B9\u30C8\u306E\
    \u9577\u3055\u304C\u9055\u3044\u307E\u3059.\")\n\n        return [list[self.__ind[i]]\
    \ for i in range(self.N)]\n\n\n    def order(self, mod: int = None) -> int:\n\
    \        \"\"\" \u4F4D\u6570\u3092\u6C42\u3081\u308B (mod \u3092\u6307\u5B9A\u3059\
    \u308B\u3068, mod \u3067\u5272\u3063\u305F\u4F59\u308A\u306B\u306A\u308B).\n\n\
    \        Args:\n            mod (int, optional): \u6307\u5B9A\u3059\u308B\u3068\
    , \u51FA\u529B\u304C mod \u3067\u5272\u3063\u305F\u4F59\u308A\u306B\u306A\u308B\
    . Defaults to None.\n\n        Returns:\n            int: \u4F4D\u6570\n     \
    \   \"\"\"\n\n        if mod is None:\n            from math import lcm\n    \
    \        x = 1\n            for cycle in self.cycle_division():\n            \
    \    x = lcm(x, len(cycle))\n            return x\n\n        def factor(n):\n\
    \            e = (n & (-n)).bit_length() - 1\n            yield 2, e\n\n     \
    \       n >>= e\n\n            p = 3\n            while p * p <= n:\n        \
    \        if n % p == 0:\n                    e = 0\n                    while\
    \ n % p == 0:\n                        n //= p\n                        e += 1\n\
    \                    yield p, e\n                p += 2\n\n            if n >\
    \ 1:\n                yield n, 1\n\n        power = {}\n        for cycle in self.cycle_division():\n\
    \            for p, e in factor(len(cycle)):\n                power[p] = max(power.get(p,\
    \ 0), e)\n\n        x=1\n        for p, e in power.items():\n            x *=\
    \ pow(p, e, mod)\n            x %= mod\n        return x\n\n    def conjugate(self)\
    \ -> \"Permutation\":\n        \"\"\" \u5171\u5F79\u306E\u4E92\u63DB\u3092\u6C42\
    \u3081\u308B.\n\n        Returns:\n            Permutation: \u5171\u5F79\u306E\
    \u4E92\u63DB\n        \"\"\"\n\n        N = len(self)\n        return Permutation([N\
    \ - 1 - x for x in self.__p])\n\n    def next(self):\n        p = self.__p\n \
    \       y = []\n        for i in range(self.N - 1, 0, -1):\n            y.append(p[i])\n\
    \            if p[i - 1] < p[i]:\n                y.append(p[i - 1])\n       \
    \         a = p[i - 1]\n                break\n\n        x=p[:i - 1]\n       \
    \ y.sort()\n        for j, b in enumerate(y):\n            if a < b:\n       \
    \         x.append(b)\n                del y[j]\n                break\n\n   \
    \     return Permutation(x + y)\n\n    def is_identity(self) -> bool:\n      \
    \  \"\"\" \u6052\u7B49\u7F6E\u63DB ?\n\n        Returns:\n            bool: \u6052\
    \u7B49\u7F6E\u63DB ?\n        \"\"\"\n\n        return all(self.__p[i] == i for\
    \ i in range(self.N))\n\n#=================================================\n\
    def Permutation_Inversion(P: Permutation, Q: Permutation) -> int:\n    \"\"\"\
    \ P \u304B\u3089 Q \u3078\u96A3\u63A5\u9805\u540C\u58EB\u306E\u5165\u308C\u66FF\
    \u3048\u306E\u307F\u306E\u6700\u5C0F\u56DE\u6570\u3092\u6C42\u3081\u308B.\n\n\
    \    Args:\n        P (Permutation): \u8D77\u70B9\u3068\u306A\u308B\u7F6E\u63DB\
    \n        Q (Permutation): \u76EE\u6A19\u3068\u306A\u308B\u7F6E\u63DB\n\n    Returns:\n\
    \        int: \u96A3\u63A5\u9805\u540C\u58EB\u306E\u5165\u308C\u66FF\u3048\u306E\
    \u307F\u306E\u6700\u5C0F\u56DE\u6570\n    \"\"\"\n\n    return (Q*(P.inverse())).inversion()\n\
    \ndef List_Inversion(A: list, B: list, default = None) -> int:\n    \"\"\" \u9577\
    \u3055\u304C\u7B49\u3057\u3044\u30EA\u30B9\u30C8 A,B \u306B\u5BFE\u3057\u3066\
    , \u4EE5\u4E0B\u306E\u64CD\u4F5C\u306E\u6700\u5C0F\u56DE\u6570\u3092\u6C42\u3081\
    \u308B.\n    \u5217 A[i] \u3068 A[i+1] \u3092\u5165\u308C\u66FF\u3048, B \u3068\
    \u4E00\u81F4\u3055\u305B\u308B.\n\n    Args:\n        A (list):\n        B (list):\n\
    \        default: \u4E0D\u53EF\u80FD\u306A\u5834\u5408\u306E\u8FD4\u308A\u5024\
    . Defaults to None.\n\n    Raises:\n        ValueError: A, B \u306E\u9577\u3055\
    \u304C\u7570\u306A\u308B\u3068\u767A\u751F\n\n    Returns:\n        int: \u5165\
    \u308C\u66FF\u3048\u56DE\u6570\u306E\u6700\u5C0F\u5024. \u4E0D\u53EF\u80FD\u306A\
    \u5834\u5408\u306F default\n    \"\"\"\n    from collections import defaultdict\n\
    \n    if len(A) != len(B):\n        raise ValueError(f'A, B \u306E\u9577\u3055\
    \u304C\u7570\u306A\u308A\u307E\u3059. (len(A) = {len(A)}, len(B) = {len(B)})')\n\
    \n    N = len(A)\n    D = defaultdict(list)\n\n    for i in range(N):\n      \
    \  D[A[i]].append(i)\n\n    for key in D:\n        D[key].reverse()\n\n    try:\n\
    \        return Permutation([D[B[i]].pop() for i in range(N)]).inversion()\n \
    \   except:\n        return default\n\n#=================================================\n\
    def Random_Permutation(N: int) -> Permutation:\n    \"\"\" \u9577\u3055 N \u306E\
    \u7F6E\u63DB\u3092\u30E9\u30F3\u30C0\u30E0\u306B\u751F\u6210\u3059\u308B.\n\n\
    \    Args:\n        N (int): \u9577\u3055\n\n    Returns:\n        Permutation:\
    \ \u9577\u3055 N \u306E\u7F6E\u63DB\n    \"\"\"\n\n    from random import shuffle\n\
    \    p = list(range(N))\n    shuffle(p)\n    return Permutation(p)\n\ndef Generate_Permutation(P:\
    \ list[int], Q: list[int]) -> Permutation:\n    \"\"\" P \u304B\u3089 Q \u306B\
    \u5909\u63DB\u3059\u308B\u7F6E\u63DB\u3092\u751F\u6210\u3059\u308B.\n\n    Args:\n\
    \        P (list[int]):\n        Q (list[int]):\n\n    Raises:\n        ValueError:\
    \ P, Q \u306E\u9577\u3055\u304C\u7570\u306A\u308B\u5834\u5408\u306B\u767A\u751F\
    \n\n    Returns:\n        Permutation: P \u304B\u3089 Q \u306B\u5909\u63DB\u3059\
    \u308B\u7F6E\u63DB\n    \"\"\"\n\n    if len(P) != len(Q):\n        raise ValueError\n\
    \n    N = len(P)\n    X = [-1]*N\n    for i in range(N):\n        X[P[i]] = Q[i]\n\
    \    return Permutation(X)\n"
  dependsOn: []
  isVerificationFile: false
  path: Permutation.py
  requiredBy: []
  timestamp: '2025-03-15 10:34:17+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Permutation.py
layout: document
redirect_from:
- /library/Permutation.py
- /library/Permutation.py.html
title: Permutation.py
---
