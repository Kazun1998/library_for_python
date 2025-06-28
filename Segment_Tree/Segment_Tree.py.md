---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test_verify/yosupo_library_checker/Data_Structure/Segment_Tree.test.py
    title: test_verify/yosupo_library_checker/Data_Structure/Segment_Tree.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.13.5/x64/lib/python3.13/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.13.5/x64/lib/python3.13/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from typing import TypeVar, Generic, Callable, Iterator\n\nM = TypeVar('M')\n\
    class Segment_Tree(Generic[M]):\n    def __init__(self, L: list[M], op: Callable[[M,\
    \ M], M], unit: M):\n        \"\"\" op \u3092\u6F14\u7B97\u3068\u3059\u308B\u521D\
    \u671F\u72B6\u614B L \u306E Segment Tree \u3092\u751F\u6210\u3059\u308B.\n\n \
    \       Args:\n            L (list[M]): \u521D\u671F\u72B6\u614B\n           \
    \ op (Callable[[M, M], M]): \u6F14\u7B97\n            unit (M): M \u306E\u5358\
    \u4F4D\u5143\n        \"\"\"\n        self.op=op\n        self.unit=unit\n\n \
    \       N=len(L); self.n=N\n        d=max(1,(N-1).bit_length())\n        k=1<<d\n\
    \n        self.data=data=[unit]*k+L+[unit]*(k-len(L))\n        self.N=k\n    \
    \    self.depth=d\n\n        for i in range(k-1,0,-1):\n            data[i]=op(data[i<<1],\
    \ data[i<<1|1])\n\n    def get(self, k: int) -> M:\n        \"\"\" \u7B2C k \u8981\
    \u7D20\u3092\u53D6\u5F97\u3059\u308B.\n\n        Args:\n            k (int): \u8981\
    \u7D20\u306E\u5834\u6240\n\n        Returns:\n            M: \u7B2C k \u8981\u7D20\
    \n        \"\"\"\n        assert 0<=k<self.N,\"\u6DFB\u5B57\u304C\u7BC4\u56F2\u5916\
    \"\n        return self.data[k+self.N]\n\n    def update(self, k: int, x: M) ->\
    \ None:\n        \"\"\" \u7B2C k \u8981\u7D20\u3092 x \u306B\u5909\u3048, \u66F4\
    \u65B0\u3059\u308B.\n\n        Args:\n            k (int): \u8981\u7D20\u306E\u5834\
    \u6240\n            x (M): \u66F4\u65B0\u5F8C\u306E\u7B2C k \u8981\u7D20\n   \
    \     \"\"\"\n\n        assert 0<=k<self.N,\"\u6DFB\u5B57\u304C\u7BC4\u56F2\u5916\
    \"\n        m=k+self.N\n\n        data=self.data; op=self.op\n        data[m]=x\n\
    \n        while m>1:\n            m>>=1\n            data[m]=op(data[m<<1], data[m<<1|1])\n\
    \n    def product(self, l: int, r: int, left_closed: bool = True, right_closed:\
    \ bool = True) -> M:\n        \"\"\" \u7B2C l \u8981\u7D20\u304B\u3089\u7B2C r\
    \ \u8981\u7D20\u307E\u3067\u306E\u7DCF\u7A4D\u3092\u6C42\u3081\u308B.\n\n    \
    \    Args:\n            l (int): \u5DE6\u7AEF\n            r (int): \u53F3\u7AEF\
    \n            left_closed (bool, optional): False \u306B\u3059\u308B\u3068, \u5DE6\
    \u7AEF\u304C\u958B\u533A\u9593\u306B\u306A\u308B. Defaults to True.\n        \
    \    right_closed (bool, optional): False \u306B\u3059\u308B\u3068, \u53F3\u7AEF\
    \u304C\u958B\u533A\u9593\u306B\u306A\u308B. Defaults to True.\n\n        Returns:\n\
    \            M: \u7B2C l \u8981\u7D20\u304B\u3089\u7B2C r \u8981\u7D20\u307E\u3067\
    \u306E\u7A4D\n        \"\"\"\n\n        L=l+self.N+(not left_closed)\n       \
    \ R=r+self.N+(right_closed)\n\n        vL=self.unit\n        vR=self.unit\n\n\
    \        data=self.data; op=self.op\n        while L<R:\n            if L&1:\n\
    \                vL=op(vL, data[L])\n                L+=1\n\n            if R&1:\n\
    \                R-=1\n                vR=op(data[R], vR)\n\n            L>>=1\n\
    \            R>>=1\n\n        return op(vL,vR)\n\n    def all_product(self) ->\
    \ M:\n        return self.data[1]\n\n    def max_right(self, left: int, cond:\
    \ Callable[[int], bool]) -> int:\n        \"\"\" \u4EE5\u4E0B\u306E2\u3064\u3092\
    \u3068\u3082\u306B\u6E80\u305F\u3059 r \u306E1\u3064\u3092\u8FD4\u3059.\\n\n \
    \       (1) r=left or cond(data[left]*data[left+1]*...*data[r-1]): True\\n\n \
    \       (2) r=N or cond(data[left]*data[left+1]*...*data[r]): False\\n\n\n   \
    \     \u203B cond \u304C\u5358\u8ABF\u6E1B\u5C11\u306E\u6642, cond(data[left]*...*data[r-1])\
    \ \u3092\u6E80\u305F\u3059\u6700\u5927\u306E r \u3068\u306A\u308B.\\n\n      \
    \  \u203B cond(unit) = True \u3092\u8AB2\u3059.\n\n        Args:\n           \
    \ left (int): \u5DE6\u7AEF\n            cond (Callable[[int], bool]): \u6761\u4EF6\
    \n\n        Returns:\n            int: r\n        \"\"\"\n\n        assert 0<=left<=self.N,\"\
    \u6DFB\u5B57\u304C\u7BC4\u56F2\u5916\"\n        assert cond(self.unit),\"\u5358\
    \u4F4D\u5143\u304C\u6761\u4EF6\u3092\u6E80\u305F\u3055\u306A\u3044.\"\n\n    \
    \    if left==self.N:\n            return self.N\n\n        left+=self.N\n   \
    \     sm=self.unit\n\n        op=self.op; data=self.data\n        first=True\n\
    \n        while first or (left & (-left))!=left:\n            first=False\n  \
    \          while left%2==0:\n                left>>=1\n            if not cond(op(sm,\
    \ data[left])):\n                while left<self.N:\n                    left<<=1\n\
    \                    if cond(op(sm, data[left])):\n                        sm=op(sm,\
    \ data[left])\n                        left+=1\n                return left-self.N\n\
    \            sm=op(sm, data[left])\n            left+=1\n        return self.N\n\
    \n    def min_left(self, right: int, cond: Callable[[int], bool]) -> int:\n  \
    \      \"\"\" \u4EE5\u4E0B\u306E 2 \u3064\u3092\u3068\u3082\u306B\u6E80\u305F\u3059\
    \ l \u306E1\u3064\u3092\u8FD4\u3059.\\n\n        (1) l=right or cond(data[l]*data[l+1]*...*data[right-1]):\
    \ True\\n\n        (2) l=0 or cond(data[l-1]*data[l]*...*data[right-1]): False\\\
    n\n\n        \u203B cond \u304C\u5358\u8ABF\u5897\u52A0\u306E\u6642, cond(data[l]*...*data[right-1])\
    \ \u3092\u6E80\u305F\u3059\u6700\u5C0F\u306E l \u3068\u306A\u308B.\\n\n      \
    \  \u203B cond(unit) = True \u3092\u8AB2\u3059.\n\n        Args:\n           \
    \ right (int): \u53F3\u7AEF\n            cond (Callable[[int], bool]): \u6761\u4EF6\
    \n\n        Returns:\n            int: l\n        \"\"\"\n\n        assert 0<=right<=self.N,\"\
    \u6DFB\u5B57\u304C\u7BC4\u56F2\u5916\"\n        assert cond(self.unit),\"\u5358\
    \u4F4D\u5143\u304C\u6761\u4EF6\u3092\u6E80\u305F\u3055\u306A\u3044.\"\n\n    \
    \    if right==0:\n            return 0\n\n        right+=self.N\n        sm=self.unit\n\
    \n        op=self.op; data=self.data\n        first=1\n        while first or\
    \ (right & (-right))!=right:\n            first=0\n            right-=1\n    \
    \        while right>1 and right&1:\n                right>>=1\n\n           \
    \ if not cond(op(data[right], sm)):\n                while right<self.N:\n   \
    \                 right=2*right+1\n                    if cond(op(data[right],\
    \ sm)):\n                        sm=op(data[right], sm)\n                    \
    \    right-=1\n                return right+1-self.N\n            sm=op(data[right],\
    \ sm)\n        return 0\n\n    def __getitem__(self, k: int) -> M:\n        return\
    \ self.get(k)\n\n    def __setitem__(self, k: int, x: M) -> None:\n        return\
    \ self.update(k,x)\n\n    def __iter__(self) -> Iterator[M]:\n        for i in\
    \ range(self.n):\n            yield self.get(i)\n"
  dependsOn: []
  isVerificationFile: false
  path: Segment_Tree/Segment_Tree.py
  requiredBy: []
  timestamp: '2025-02-22 11:32:25+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test_verify/yosupo_library_checker/Data_Structure/Segment_Tree.test.py
documentation_of: Segment_Tree/Segment_Tree.py
layout: document
title: Segment Tree
---

## Outline

モノイド $M=(M, \*, e_M)$ の列に対する1点更新, 区間積の取得を得意とするデータ構造

## Contents

---

### Constructer

```Python
S=Segment_Tree(L, calc, unit)
```

- $L$ : $M$ の列

以下, $N:=\lvert L \rvert$ とする.

- $\operatorname{calc} : M \times M \to M; (x,y) \mapsto x \* y$ : 二項演算.
- $\mathrm{unit}$ : $M$  の単位元 $e_M$.
- **計算量** : $O(N \log N)$ Time.

---

### get

```Pyhon
S.get(k)
```

- 第 $k$ 要素を返す.
- **制約**
  - $0 \leq k \lt N$
- **計算量** : $O(1)$ Time.

---

### update

```Pyhon
S.update(k,x)
```

- 第 $k$ 要素を $x$ に変更する.
- **制約**
  - $0 \leq k \lt N$
  - $x \in M$
- **計算量** : $O(\log N)$ Time.

---

### product

```Pyhon
B.product(l, r)
```

- $B_l \* B_{l+1} \* \dots \* B_r$ を求める ( $l \gt r$ の場合は $e_M$ とする).
- **制約**
  - $0 \leq l \lt N$
  - $0 \leq r \lt N$
- **計算量** : $O(\log N)$ Time.

---

### all_sum

```Pyhon
B.all_product(k)
```

- $B_0 \* B_1 \* \dots \* B_{N-1}$ を求める.
- **計算量** : $O(1)$ Time.

---

### max_right

```Pyhon
B.max_right(left, cond)
```

- 以下の2条件を共に満たすような $r$ のうちの1つを返す.
  1. $r={\rm left}$ または $\operatorname{cond}(B_{ {\rm left}} \* B_{ {\rm left}+1} \* \dots \* B_{r-1})=\mathbb{T}$
  1. $r=N$ または $\operatorname{cond}(B_{ {\rm left}} \* B_{ {\rm left}+1} \* \dots \* B_r)=\mathbb{F}$
- 特に, $\operatorname{cond}$ が単調減少のときは, 整数 $r$ は $\operatorname{cond}(B_{ {\rm left}} \* B_{ {\rm left}+1} \* \dots \* B_{r-1})=\mathbb{T}$ を満たす最大の整数となる.
- **制約**
  - $0 \leq {\rm left} \leq N$
  - $\operatorname{cond}: G \to \\{\mathbb{T}, \mathbb{F} \\}$
- **計算量** : $O(\log N)$ Time.

### min_left

```Pyhon
B.min_left(right, cond)
```

- 以下の2条件を共に満たすような $l$ のうちの1つを返す.
  1. $l={\rm right}$ または $\operatorname{cond}(B_l \* B_{l+1} \* \dots \* B_{ {\rm right}-1})=\mathbb{T}$
  1. $l=0$ または $\operatorname{cond}(B_{l-1} \* B_l \* \dots \* B_{ {\rm right}-1})=\mathbb{F}$
- 特に, $\operatorname{cond}$ が単調増加のときは, 整数 $l$ は $\operatorname{cond}(B_l \* B_{l+1} \* \dots * B_{ {\rm right}-1})=\mathbb{T}$ を満たす最小の整数となる.
- **制約**
  - $0 \leq {\rm right} \leq N$
  - $\operatorname{cond}: G \to \\{\mathbb{T}, \mathbb{F} \\}$
- **計算量** : $O(\log N)$ Time.
