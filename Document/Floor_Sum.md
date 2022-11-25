---
title: Floor Sum
documentation_of: //Summation/Floor_Sum.py
---

## Outline

$\displaystyle \sum\_{i=K}^N \left \lfloor \dfrac{Ai+B}{M}\right \rfloor$ を高速に求めるアルゴリズム.

## Contents

---

### floor_sum

```Python
floor_sum(A,B,M,N)
```

* $\displaystyle \sum\_{i=0}^{N-1} \left \lfloor \dfrac{Ai+B}{M}\right \rfloor$ を求める.

### Floor_Sum

```Python
Floor_Sum(A,B,M,N,K=0)
```

* $\displaystyle \sum\_{i=K}^{N} \left \lfloor \dfrac{Ai+B}{M}\right \rfloor$ を求める.
  * 範囲の右端が `floor_sum` だと開だが, `Floor_Sum` だと閉になっていることに注意せよ.
