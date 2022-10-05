---
title: Lazy Segment Tree
documentation_of: //Segment_Tree/Lazy_Segment_Tree.py
---

## Outline

$M=(M, \*, e_M), F=(F, \circ, 1_F)$ はそれぞれモノイドであり, $F$ は $M$ に左から作用するとし, この作用を $F \times M \to M; (f,x) \mapsto f(x)$ と書くことにする.

また, この作用は準同型であるとする.

つまり, この作用は以下を満たすとする.

- $\forall \alpha, \beta \in F, \forall x \in M; (\alpha \circ \beta)(x)=\alpha(\beta(x))$
- $\forall x \in M; 1_F(x)=x$
- $\forall \alpha \in F, \forall x,y \in M; \alpha(x \* y)=\alpha(x) \* \alpha(y)$

このような $M$ の列に対する1点更新, $X$ の元による区間更新, 区間積の取得を得意とするデータ構造である.

## Contents

---

### Constructer

```Python
S=Lazy_Evaluation_Tree(L, calc, unit, op, comp, id)
```

- $L$ : $M$ の列

以下, $L$ の長さを $N$ とする.

- $\operatorname{calc} : M \times M \to M; (x,y) \mapsto x \* y$ : 二項演算.
- $\mathrm{unit}$ : $M$  の単位元 $e_M$.
- $\mathrm{op}$ : $F \times M; (\alpha, x) \mapsto \alpha(x)$ : $F$ の $M$ への作用
- $\mathrm{comp}$ : $F \times F \to F; (\alpha,\beta) \mapsto \alpha \circ \beta$ : $F$ における合成
- $\mathrm{id}$ : $F$ の単位元 $1_F$ .
- **計算量** : $O(N)$ Time.

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

### operate

```Pyhon
S.get(l, r, alpha, left_close=True, right_close=True)
```

- 第 $l$ 要素から第 $r$ 要素に $\alpha$ を作用させる.
- `left_close`=`False` にすると, 左側が開区間になる (つまり, 左端が含まれなくなる). `right_close` についても同様.
- **制約**
  - 作用させる区間を $I$ としたとき, $I$ は $[0,N)$ に含まれる.
  - $\alpha \in F$
- **計算量** : $O(\log N)$ Time.

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
B.product(l, r, left_close=True, right_close=True)
```

- $B_l \* B_{l+1} \* \dots \* B_r$ を求める (ただし, 空積は $e_M$ とする) .
- `left_close`=`False` にすると, 左側が開区間になる (つまり, 左端が含まれなくなる). `right_close` についても同様.
- **制約**
  - 作用させる区間を $I$ としたとき, $I$ は $[0,N)$ に含まれる.
  - $\alpha \in F$

- **計算量** : $O(\log N)$ Time.

---

### all_product

```Pyhon
B.all_product()
```

- $B_0 \* B_1 \* \dots \* B_{N-1}$ を求める.
- **計算量** : $O(N \log N)$ Time.

---

### refresh

```Pyhon
B.refresh()
```

- 更新を遅延していた作用の記録を全て更新する.
- **計算量** : $O(N \log N)$ Time.
