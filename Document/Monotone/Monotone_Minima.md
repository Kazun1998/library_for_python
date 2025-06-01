---
title: Monotone Minima
documentation_of: //Nimber.py
---

## Outline

$N$ 行 $M$ 列の行列 $A = (a_{i,j})$ が Monotone であるとは,
  $$ \min \left(\argmin_{0 \leq j < M} a_{0,j} \right) \leq \min \left(\argmin_{0 \leq j < M} a_{1,j} \right) \leq \dots \leq \min \left(\argmin_{0 \leq j < M} a_{N-1,j} \right)$$

を満たすことである.

このとき, $0 \leq i < N$ それぞれに対する
  $$ \min \left(\argmin_{0 \leq j < M} a_{i,j} \right) $$
を合計で $O(N + M \log N)$ 時間で求める.

## Contents

```Python
Monotone_Minima(N: int, M: int, eval: Callable[[int, int], int]) -> list[int]
```

* Monotone な行列 $A = (a_{i,j})$ に対して, 各 $0 \leq i < N$ に対する $\displaystyle \min \left(\argmin_{0 \leq j < M} a_{i,j} \right)$ を求める.
* **引数**
  * $N$: 行数
  * $M$: 列数
  * $\textrm{eval}$: $a_{i,j} = \textrm{eval}(i,j)$ を満たす $2$ 変数関数
* **計算量**
  * $O(N + M \log N)$ 時間
