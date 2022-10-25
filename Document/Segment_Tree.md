---
title: Segment Tree
documentation_of: //Segment_Tree/Segment_Tree.py
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
