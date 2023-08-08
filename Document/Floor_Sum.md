---
title: Floor Sum
documentation_of: //Summation/Floor_Sum.py
---

## Outline

$\displaystyle \sum\_{i=K}^N \left \lfloor \dfrac{Ai+B}{M}\right \rfloor$ を高速に求めるアルゴリズム.

## Theory

$\displaystyle S(A,B,M,N):=\sum\_{i=0}^N \left \lfloor \dfrac{Ai+B}{M}\right \rfloor$ とする.

$A$ を $M$ で割った商と余りを $Q_A, R_A$, $B$ を $M$ で割った余りを $Q_B, R_B$ とすると,

$$\begin{align*}
\left \lfloor \dfrac{Ai+B}{M}\right \rfloor
&=\left \lfloor \dfrac{(Q_A M+R_A) i+(Q_B M+R_B)}{M}\right \rfloor \\
&=\left \lfloor \dfrac{(Q_A i+Q_B)M+(R_A i+R_B)}{M}\right \rfloor \\
&=\left \lfloor (Q_A i+Q_B) + \dfrac{R_A i+R_B}{M}\right \rfloor \\
&=(Q_A i+Q_B) \left \lfloor \dfrac{R_A i+R_B}{M}\right \rfloor
\end{align*}$$

であるから,

$$\begin{align*}
S(A,B,M,N)
&=\sum_{i=0}^{N-1} \left(Q_A i+ Q_B+\left \lfloor \dfrac{R_A i+R_B}{M}\right \rfloor \right)\\
&=\dfrac{Q_A}{2} N(N-1)+Q_B N +\sum_{i=0}^{N-1} \left \lfloor \dfrac{R_A i+R_B}{M}\right \rfloor\\
&=\dfrac{Q_A}{2} N(N-1)+Q_B N +S(R_A, R_B, M, N)
\end{align*}$$

となり, $0 \leq A,B \lt M$ の場合のみを考慮すれば十分であることが分かる.

以降では $0 \leq A,B \lt M$ とする.

(途中)

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
