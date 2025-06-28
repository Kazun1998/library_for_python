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
  code: "class Mo:\n    def __init__(self, N: int):\n        \"\"\" \u7BC4\u56F2\u304C\
    \ 0 \u4EE5\u4E0A N \"\u672A\u6E80\" \u306E Mo's Algorithm \u306E\u6E96\u5099\u3092\
    \u3059\u308B.\n\n        Args:\n            N (int): \u7BC4\u56F2\u306E\u4E0A\u9650\
    \ (N \u306F\u542B\u307E\u306A\u3044)\n        \"\"\"\n\n        self.__N = N\n\
    \        self.__query_count = 0\n        self.left: list[int] = []\n        self.right:\
    \ list[int] = []\n\n    @property\n    def N(self) -> int:\n        return self.__N\n\
    \n    @property\n    def query_count(self) -> int:\n        \"\"\" \u73FE\u5728\
    \u767B\u9332\u3055\u308C\u3066\u3044\u308B\u30AF\u30A8\u30EA\u306E\u6570\u3092\
    \u51FA\u529B\u3059\u308B.\n\n        Returns:\n            int: \u73FE\u5728\u767B\
    \u9332\u3055\u308C\u3066\u3044\u308B\u30AF\u30A8\u30EA\u306E\u6570\n        \"\
    \"\"\n\n        return self.__query_count\n\n    def add_query(self, l: int, r:\
    \ int):\n        \"\"\" \u9589\u533A\u9593 [l,r] \u306B\u5BFE\u3059\u308B\u30AF\
    \u30A8\u30EA\u3092\u8FFD\u52A0\u3059\u308B.\n\n        Args:\n            l (int):\
    \ \u5DE6\u7AEF\n            r (int): \u53F3\u7AEF\n        \"\"\"\n\n        self.left.append(l)\n\
    \        self.right.append(r + 1)\n        self.__query_count += 1\n\n    def\
    \ calculate(self, add, delete, rem):\n        \"\"\" \u30AF\u30A8\u30EA\u3092\u51E6\
    \u7406\u3059\u308B.\n\n        Args:\n            add (Callable[[int]]): add(k):\
    \ \u533A\u9593\u306B k \u3092\u8FFD\u52A0\u3059\u308B\u5834\u5408\u306E\u51E6\u7406\
    \n            delete (Callable[[int]]): delete(k): \u533A\u753B\u304B\u3089 k\
    \ \u3092\u524A\u9664\u3059\u308B\u5834\u5408\u306E\u51E6\u7406\n            rem\
    \ (Callable[[int]]): query(q): \u7B2C q \u30AF\u30A8\u30EA (add_query \u306B\u8FFD\
    \u52A0\u3057\u305F\u9806) \u306E\u51E6\u7406\n        \"\"\"\n\n        bucket_size\
    \ = self.N // (min(self.N, int(self.query_count ** 0.5 + 0.5)))\n        bucket_count\
    \ = (self.N + bucket_size - 1) // bucket_size\n        buckets = [[] for _ in\
    \ range(bucket_count)]\n\n        left = self.left\n        right = self.right\n\
    \n        for q in range(self.query_count):\n            buckets[left[q] // bucket_size].append(q)\n\
    \n        for i in range(bucket_count):\n            buckets[i].sort(key = lambda\
    \ q: right[q], reverse = i % 2)\n\n        x = y = 0\n        for bucket in buckets:\n\
    \            for q in bucket:\n                l = left[q]\n                r\
    \ = right[q]\n\n                for i in range(x - 1, l - 1 , -1):\n         \
    \           add(i)\n\n                for j in range(y, r):\n                \
    \    add(j)\n\n                for i in range(x, l):\n                    delete(i)\n\
    \n                for j in range(y - 1, r - 1, -1):\n                    delete(j)\n\
    \n                x = l\n                y = r\n                rem(q)\n\n   \
    \ def calculate_noncommutative(self, add_left, add_right, delete_left, delete_right,\
    \ rem):\n        bucket_size = self.N // (min(self.N, int(self.query_count **\
    \ 0.5 + 0.5)))\n        bucket_count = (self.N + bucket_size - 1) // bucket_size\n\
    \        buckets = [[] for _ in range(bucket_count)]\n\n        left = self.left\n\
    \        right = self.right\n\n        for q in range(self.query_count):\n   \
    \         buckets[left[q] // bucket_size].append(q)\n\n        for i in range(bucket_count):\n\
    \            buckets[i].sort(key=lambda q: right[q], reverse=i%2)\n\n        x\
    \ = y = 0\n        for bucket in buckets:\n            for q in bucket:\n    \
    \            l = left[q]\n                r = right[q]\n\n                for\
    \ i in range(x, l):\n                    delete_left(i)\n\n                for\
    \ i in range(x-1, l-1, -1):\n                    add_left(i)\n\n             \
    \   for j in range(y, r):\n                    add_right(j)\n\n              \
    \  for j in range(y-1, r-1, -1):\n                    delete_right(j)\n\n    \
    \            x = l\n                y = r\n                rem(q)\n"
  dependsOn: []
  isVerificationFile: false
  path: Mo.py
  requiredBy: []
  timestamp: '2025-05-11 11:48:02+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Mo.py
layout: document
title: Mo
---

## Outline

長さ $N$ の列 $A=(A_0, A_1, \dots, A_{N-1})$ と以下の形式の $Q$ 個のクエリがある.

> 部分列 $(A_L, A_{L+1}, \dots, A_{R-1})$ におけるある値を $F(L,R)$ と書くことにする.
>
> このとき, $Q$ 個の整数の組 $(L_1, R_1), \dots, (L_Q, R_Q)$ が与えられるので, $F(L_1, R_1), \dots, F(L_Q, R_Q)$ を求めよ.

ここで, 以下の条件をみたしているとする.

- $A$ は $Q$ 個のクエリにおいて固定である.
- $Q$ 個のクエリが先読みできる.
- $F(L,R)$ が求まっているとき, $F(L \pm 1, R), F(L, R \pm 1)$ が容易に求める.

このとき, $F(L_1, R_1), \dots, F(L_Q, R_Q)$ を合計
で $O(N \sqrt{Q})$ Time で求めることが出来る.
