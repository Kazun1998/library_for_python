---
title: Binary Indexed Tree (Fenwick Tree)
documentation_of: //Binary_Indexed_Tree/Binary_Indexed_Tree.py
---

## Outline

可換群 $G=(G, +, 0_G)$ の列に対する1点更新, 区間和の取得を得意とするデータ構造

## Contents

---

### Constructer

```Python
B=Binary_Indexed_Tree(L, calc, unit, inv)
```

- $L$ : $G$ の列

以下, $N=|L|$ とする.

- $\operatorname{calc} : G \times G \to G; (x,y) \mapsto x+y$ 二項演算.
- $\mathrm{unit}$ : $G$  の単位元 $0_G$.
- $\operatorname{inv}$ : $G \to G; x \mapsto -x$ : $x$ の逆元.
- **計算量** : $O(N)$ Time.

---

### get

```Pyhon
B.get(k)
```

- 第 $k$ 要素を返す.
- **制約**
  - $0 \leq k \lt N$
- **計算量** : $O(\log N)$ Time.

---

### add

```Pyhon
B.add(k)
```

- 第 $k$ 要素に $x$ を加算する.
- **制約**
  - $0 \leq k \lt N$
  - $x \in G$
- **計算量** : $O(\log N)$ Time.

---

### update

```Pyhon
B.update(k,x)
```

- 第 $k$ 要素を $x$ に変更する.
- **制約**
  - $0 \leq k \lt N$
  - $x \in G$
- **計算量** : $O(\log N)$ Time.

---

### sum

```Pyhon
B.sum(l, r)
```

- $\displaystyle \sum_{k=l}^r B_k$ を求める ( $l \gt r$ の場合は $0_G$ とする).
- **制約**
  - $0 \leq l \lt N$
  - $0 \leq r \lt N$
- **計算量** : $O(\log N)$ Time.

---

### all_sum

```Pyhon
B.all_sum(k)
```

- $\displaystyle \sum_{k=0}^{N-1} B_k$ を求める.
- **制約**
- **計算量** : $O(\log N)$ Time.

---

### binary_search

```Pyhon
B.binary_search(cond)
```

- $G$ が単位元で, $\operatorname{cond}$ が単調増加であるとき, $\displaystyle \operatorname{cond} \left(\sum_{i=0}^k B_i \right)=\mathbb{T}$ となるような最小の $k$ を求める.
- なお, 次のような例外ケースがある.
  - $\displaystyle \operatorname{cond} (0_G)=\mathbb{T}$ の場合, $k=-1$ とする.
  - $\displaystyle \operatorname{cond} \left(\sum_{i=0}^{N-1} B_i\right)=\mathbb{F}$ の場合, $k=N$ とする.
- **制約**
  - $\operatorname{cond}: G \to \{\mathbb{T}, \mathbb{F} \}$ : 単調増加
- **計算量** : $O(\log N)$ Time.
