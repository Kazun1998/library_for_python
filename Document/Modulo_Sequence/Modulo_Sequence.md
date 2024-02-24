---
title: Modulo Sequence
documentation_of: //Modulo_Sequence/Modulo_Sequence.py
---

## Outline

線形漸化式で表された数列に関する計算を行う.

## Theory

### 線形漸化式の第 $N$ 項

数列 $A=(A_n)$ は漸化式

$$A_n=\sum_{k=0}^{d-1} C_k A_{n-k-1} \quad (n \geq d)$$

を満たしているとする.

このとき, 形式的ベキ級数 $Q$, 多項式 $P$ をそれぞれ

- $Q(X)=1-C_0 X-C_1 X^2-\dots-C_{d-1} X^d$
- $P(X)=(A_0+A_1 X+\dots+A_{d-1} X^{d-1}) Q(X) \pmod{X^d}$

とすると, 任意の非負整数 $n$ において,

$$A_n=\left[X^n \right] \dfrac{P(X)}{Q(X)}$$

となる.

### 分割数

非負整数 $N$ に対して, $N$ を $0$ 個以上の正の整数の和で表す方法 (ただし, 順番の違いは同一視する) を分割数といい, $P_N$ と書く.

このとき, $P_N$ は

$$P_N=\left[X^N \right] \prod_{n=1}^\infty \dfrac{1}{1-X^n}$$

である.

なお, 五角数定理 により,

$$\prod_{n=1}^\infty (1-X^n)=\sum_{n=-\infty}^{\infty} (-1)^n X^{n(3n-1)/2}$$

となるから, 高速化できる.

### 相異なる整数への分割

非負整数 $N$ に対して, $N$ を $0$ 個以上相異なる正の整数の和で表す方法 (ただし, 順番の違いは同一視する) を $Q_N$ と書く.

このとき, $Q_N$ は

$$Q_N=\left[X^N \right] \prod_{n=1}^\infty (1+X^n)$$

である.

なお, ベキ級数展開することによって,

$$1+X^n=\exp \left(\log (1+X^n) \right)=\exp \left( \sum_{k=1}^\infty (-1)^{k-1} X^{kn} \right)$$

であるから,

$$Q_N=\left[X^N \right] \exp \left(\sum_{n=1}^\infty \sum_{k=1}^\infty (-1)^{k-1} X^{kn} \right)$$

となる. なお, $Q_N$ を求める際には, $N$ 次まであれば十分でるが, $kn \leq N$ となる非負整数の組の個数は $O(N \log N)$ 個程度になる.

## Contents

---

### Nth_Term_of_Linearly_Recurrent_Sequence

```Pyhon
Nth_Term_of_Linearly_Recurrent_Sequence(A, C, N, offset=0)
```

- $A,C$ の長さを $d$ とする.
- 線形漸化式 $\displaystyle A_n=\sum_{k=0}^{d-1} C_k A_{n-k-1} \quad (n \geq d)$ で表される整数列 $A=(A_i)$ の第 $N$ 項 $A_N$ を求める.
- **制約**
  - $A$ と $C$ の長さは等しい.
- **計算量** : $O(d \log d \log N)$ Time.

---

### Find_Linear_Recurrence

```Python
Find_Linear_Recurrence(A)
```

- 整数列 $A=(A_0, \dots, A_{N-1})$ が見たす最小の次数の漸化式を求める.

---

### Fibonacci

```Python
Fibonacci(N)
```

- 以下で定義される Fibonacci 数列 $F=(F_n)$ の第 $N$ 項を求める.
  - $F_0=0, F_1=1$
  - $F_n=F_{n-1}+F_{n-2} \quad (n \geq 2)$
- **計算量** : $O(\log N)$ Time.

---

### Lucas

```Python
Lucas(N)
```

- 以下で定義される Lucas 数列 $L=(L_n)$ の第 $N$ 項を求める.
  - $L_0=2, L_1=1$
  - $L_n=L_{n-1}+L_{n-2} \quad (n \geq 2)$
- **計算量** : $O(\log N)$ Time.

---

### Cumulative

```Python
Cumulative(A,N)
```

- $A$ の長さを $d$ とする. 以下で定義される数列 $B=(B_n)$ の第 $N$ 項を求める.
  - $B_n=A_n \quad (0 \leq n \leq d-1)$
  - $B_n=B_{n-1}+B_{n-2}+\dots+B_{n-d} \quad (n \geq d)$
- **計算量** : $A$ の長さを $d$ として, $O(d \log d \log N)$ Time.

---

### Factorial_Modulo

```Python
Factorial_Modulo(N)
```

- $N! \pmod{\mathrm{mod}}$ を求める.

- **計算量** : $O(\sqrt{N} (\log N)^2)$ Time.

---

### Bernoulli

```Python
Bernoulli(N, mode=0)
```

- Bernoulli 数を求める.
- ${\rm mode}=0$ ならば, $B_N$ のみ, ${\rm mode}=1$ ならば, $B_0, \dots, B_N$ からなるリスト.
- **計算量** : $O(N \log N)$ TIme.

---

### PartitionsP

```Python
PartitionsP(N, mode=0)
```

- 以下で定義される $P_k$ を求める.
  - 整数 $k$ を順番を考慮せずに自然数の和にわける場合の数
- ${\rm mode}=0$ ならば, $P_N$ のみ, ${\rm mode}=1$ ならば, $P_0, \dots, P_N$ からなるリスト.
- **計算量** : $O(N \log N)$ TIme.

---

### PartitionsQ

```Python
PartitionsQ(N, mode=0)
```

- 以下で定義される $Q_k$ を求める.
  - 整数 $k$ を相異なる自然数の和にわける場合の数
- ${\rm mode}=0$ ならば, $Q_N$ のみ, ${\rm mode}=1$ ならば, $Q_0, \dots, Q_N$ からなるリスト.
- **計算量** : $O(N \log N)$ TIme.

---

### Stirling_1st

``` Python
Stirling_1st(N)
```

- $k=0,1,\dots,N$ に対する第 I 種スターリング数 $\begin{bmatrix} n \\ k \end{bmatrix}$ を求める.
- **計算量** : $O(N (\log N)^2)$ Time ?

### Stirling_2nd

``` Python
Stirling_2nd(N)
```

- $k=0,1,\dots,N$ に対する第 II 種スターリング数 $\begin{Bmatrix} n \\ k \end{Bmatrix}$ を求める.
- **計算量** : $O(N \log N)$ Time.

### Bell

```Pythoon
Bell(N, mode=0)
```

- 次の式で定義される Bell 数 $B_n$ を求める. $\displaystyle \sum_{n=0}^\infty B_n x^n=\exp(\exp(x)-1)$

- ${\rm mode}=0$ ならば, $B_N$ のみ, ${\rm mode}=1$ ならば, $B_0, \dots, B_N$ からなるリスト.
- **計算量** : $O(N \log N)$ TIme.

### Motzkin

```Pythoon
Motzkin(N, mode=0)
```

- 次の式で定義される Motzkin 数 $M_n$ を求める. $\displaystyle \sum_{n=0}^\infty M_n x^n=\dfrac{1-x-\sqrt{1-2x-3x^2}}{2x^2}$

- ${\rm mode}=0$ ならば, $M_N$ のみ, ${\rm mode}=1$ ならば, $M_0, \dots, M_N$ からなるリスト.
- **計算量** : $O(N \log N)$ TIme.
