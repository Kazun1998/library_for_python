---
title: Totient Function
documentation_of: //Integer/Totient.py
---

## Outline

Euler の Totient 関数 $\varphi$ に関する計算を行う.

正の整数 $N$ に対して, $N$ と互いに素な $1$ 以上 $N$ 未満の整数の個数を $\varphi(N)$ と書く.

## Theory

Euler の Totient 関数 に対して, 以下の性質が成り立つ.

* 素数 $p$ と非負整数 $k$ に対して, $\varphi(p^k) = p^k - p^{k-1} = p^{k-1} (p-1)$.
* 互いに素な正の整数 $m, n$ に対して, $\varphi(mn) = \varphi(m) \varphi(n)$.

このことから, $N$ の素因数分解を

$$ N = p_1^{e_1} \times \dots \times p_r^{e_r} = \prod_{i = 1}^r p_i^{e_i} \quad (i \neq j \Rightarrow p_i \neq p_j)$$

としたとき,

$$ \varphi(N) = \prod_{i=1}^r p_i^{e_i-1} (p_i - 1) = N \prod_{i=1}^r \left(1 - \dfrac{1}{p_i} \right)$$

となる.

$N$ の素因数分解は試し割りを用いると, $O(\sqrt{N})$ 時間, 高速な方法で $O(N^{1/4})$ 時間で求められるので, $\varphi(N)$ もこれらと同程度の時間で求められる.

### $\varphi$ の性質

$\varphi$ について, 以下が成り立つ.

* $N \geq 2$ とする. $\mathbb{Z}/N \mathbb{Z}$ における可逆元の個数は $\varphi(N)$ 個である.
* $d$ を $N$ の約数とする. $\gcd(N,x) = \frac{N}{d}$ となる $N$ 未満の非負整数の数は $\varphi(d)$ 個である. このことから, $\displaystyle \sum_{d \mid N} \varphi(d) = N$ が成り立つ.
