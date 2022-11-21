---
title: Dual Segment Tree
documentation_of: //Segment_Tree/Dual_Segment_Tree.py
---

## Outline

モノイド $F=(F, \circ, 1_F)$ の列に対する区間更新, 1点取得を得意とするデータ構造

## Contents

---

### Constructer

```Python
S=Dual_Segment_Tree(L, comp, id)
```

- $L$ : $M$ の列

以下, $N:=\lvert L \rvert$ とする.

- $\mathrm{comp} : F \times F \to F; (\alpha, \beta) \mapsto \alpha \circ \beta$ : 二項演算.
- $\mathrm{id}$ : $F$  の単位元 $1_F$.
- **計算量** : $O(N)$ Time.
- (※ 現在, $L$ は無効である)

---

### operate

```Python
S.operate(self, l, r, alpha, left_closed=True, right_closed=True)
```

- 第 $l$ 要素から第 $r$ 要素全てに対して, 左から $\alpha$ を作用させる.
- `left_close`=`False` にすると, 左側が開区間になる (つまり, 左端が含まれなくなる). `right_close` についても同様.
- **制約**
  - 作用させる区間を $I$ としたとき, $I$ は $[0,N)$ に含まれる.
  - $\alpha \in F$
- **計算量** : $O(\log N)$ Time.

---

### get

```Pyhon
S.get(k)
```

- 第 $k$ 要素を返す.
- **制約**
  - $0 \leq k \lt N$
- **計算量** : $O(\log N)$ Time.

---

### refresh

```Pyhon
B.refresh()
```

- 更新を遅延していた作用の記録を全て更新する.
- **計算量** : $O(N \log N)$ Time.
