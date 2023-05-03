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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.3/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.3/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class Mo:\n    def __init__(self, N):\n        \"\"\" \u7BC4\u56F2\u304C\
    \ 0 \u4EE5\u4E0A N \"\u672A\u6E80\" \u306E Mo's Algorithm \u306E\u6E96\u5099\u3092\
    \u3059\u308B.\n\n        \"\"\"\n        self.N=N\n        self.Q=0\n        self.left=[]\n\
    \        self.right=[]\n\n    def add_query(self, l, r):\n        \"\"\" \u9589\
    \u533A\u9593 [l,r] \u306B\u5BFE\u3059\u308B\u30AF\u30A8\u30EA\u3092\u8FFD\u52A0\
    \u3059\u308B.\n        \"\"\"\n\n        self.left.append(l)\n        self.right.append(r+1)\n\
    \        self.Q+=1\n\n    def calculate(self, add, delete, rem):\n        \"\"\
    \" \u30AF\u30A8\u30EA\u3092\u51E6\u7406\u3059\u308B.\n\n        \"\"\"\n\n   \
    \     block_size=self.N//(min(self.N, int(self.Q**0.5+0.5)))\n        t=(self.N+block_size-1)//block_size\n\
    \        B=[[] for __ in range(t)]\n\n        left=self.left; right=self.right\n\
    \n        for q in range(self.Q):\n            B[left[q]//block_size].append(q)\n\
    \n        for i in range(t):\n            B[i].sort(key=lambda q: right[q], reverse=i%2)\n\
    \n        x=y=0\n        for b in B:\n            for q in b:\n              \
    \  l=left[q]; r=right[q]\n                for i in range(x, l): delete(i)\n  \
    \              for i in range(x-1, l-1, -1): add(i)\n                for j in\
    \ range(y, r): add(j)\n                for j in range(y-1, r-1, -1): delete(j)\n\
    \                x=l; y=r\n                rem(q)\n        return\n\n    def calculate_noncommutative(self,\
    \ add_left, add_right, delete_left, delete_right, rem):\n        block_size=self.N//(min(self.N,\
    \ int(self.Q**0.5+0.5)))\n        t=(self.N+block_size-1)//block_size\n      \
    \  B=[[] for __ in range(t)]\n\n        left=self.left; right=self.right\n\n \
    \       for q in range(self.Q):\n            B[left[q]//block_size].append(q)\n\
    \n        for i in range(t):\n            B[i].sort(key=lambda q: right[q], reverse=i%2)\n\
    \n        x=y=0\n        for b in B:\n            for q in b:\n              \
    \  l=left[q]; r=right[q]\n                for i in range(x, l): delete_left(i)\n\
    \                for i in range(x-1, l-1, -1): add_left(i)\n                for\
    \ j in range(y, r): add_right(j)\n                for j in range(y-1, r-1, -1):\
    \ delete_right(j)\n                x=l; y=r\n                rem(q)\n        return\n"
  dependsOn: []
  isVerificationFile: false
  path: Mo.py
  requiredBy: []
  timestamp: '2022-03-20 20:43:59+09:00'
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
