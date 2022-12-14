---
title: Wavelet Matrix
documentation_of: //Wavelet_Matrix.py
---

## Outline

静的な数列 $X=(X_0, \dots, X_{N-1})$ に対する様々な検索, 計算を得意とするデータ構造

## Contents

---

### Constructer

```Python
W=Wavelet_Matrix(X)
```

- 整数列 $X$ に対する Wavelet Matrix を生成する.

以降の説明では, $N:=\lvert X \rvert$ とする.

- **計算量** : $O(N \log N)$ Times.

---

### rank

```Python
W.rank(i, value)
```

- $X_0, X_1, \dots, X_{i-1}$ にある `value` の個数を求める.
- **計算量** : $O(\log N)$ Times.

---

### range_rank

```Python
W.rank(l, r, value)
```

- 部分列 $(X_l, X_{l+1}, \dots, X_{r-1})$ にある `value` の個数を求める.
- `rank` は `range_rank` の特別な場合
- **計算量** : $O(\log N)$ Times.

---

### select

```Python
W.select(value, k ,default=-1)
```

- $X_0, X_1, \dots, X_{N-1}$ において, $k$ 番目 (1-indexed) に `value` が現れる整数列の添字を求める (存在しない場合は `default` が返り値).
- **計算量** : $O(\log N)$ Times.

---

### quantile

```Python
W.quantile(l, r, k)
```

- 部分列 $(X_l, X_{l+1}, \dots, X_{r-1})$ のうち, $k$ (1-indexed) に小さい値を求める.
- **計算量** : $O(\log N)$ Times.

---

### kth_max

```Python
W.kth_max(l, r, k)
```

- 部分列 $(X_l, X_{l+1}, \dots, X_{r-1})$ のうち, $k$ (1-indexed) に大きい値を求める.
- `quantile` の双対に当たる.
- **計算量** : $O(\log N)$ Times.

---

### top

```Python
W.top(l, r, k)
```

- 部分列 $(X_l, X_{l+1}, \dots, X_{r-1})$ のうち, 出現回数が多い順に $k$ 個, (値, 回数) のタプルを生成する.
- 回数が同率の場合は値が小さい方が優先される.
- **計算量** : $O((r-l) \log N)$ Times.

---

### intersect

```Python
W.intersect(l1, r1, l2, r2)
```

- 2つの部分列 $(X_{l_1}, X_{l_1+1}, \dots, X_{r_1-1}), (X_{l_2}, X_{l_2+1}, \dots, X_{r_2-1})$ のうち, に共通して出てくる要素 $v$ を ($m$, 1番目の区間にある $v$ の個数, 2番目の区間にある $v$ の個数) という形式のタプルを生成する.
- **計算量** : $O((r_1-l_1)+(r_2-l_2))$ Times.

---
