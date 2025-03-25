---
title: Nimber
documentation_of: //Nimber.py
---

## Outline

組み合わせゲーム理論において用いられる Nim から導入された Nimber の計算を行う.

## Theory

非負整数 $n$ に対して,
    $$ F_n := \{0, 1, \dots, 2^n - 1 \} $$
とする.

### 加法

$F_n$ 上の演算 $\oplus: F_n \times F_n \to F_n$ を
    $$ x \oplus y := \mathrm{mex} \left(\{ a \oplus y \mid 0 \leq a < x \} \cup \{ x \oplus b \mid 0 \leq b < y \} \right)$$
によって帰納的に定める. ただし, $S \subsetneq \mathbb{N}$ に対して, $S$ の最小除外数 $\mathrm{mex}~S$ を
    $$ \mathrm{mex}~S := \min (\mathbb{N} \setminus S) $$
で定義する.

すると, $\oplus$ は Bitwise-XOR と一致する.

このことから, 以下が従う.

* $\oplus$ は $F_n$ において可換群になる. 特に, 以下が成り立つ.
  * $x < 2^m < 2^n$ に対して, $x \oplus 2^m = x + 2^m$.
  * 単位元は $0$ である.
  * $x \in F_n$ の逆元は $x$ 自身である.

### 乗法

$F_{2^n}$ 上の演算 $\otimes: F_{2^n} \times F_{2^n} \to F_{2^n}$ を
    $$ x \otimes y := \mathrm{mex} \left(\{(a \otimes y) \oplus (x \otimes b) \oplus (a \otimes b) \mid 0 \leq a < x, 0 \leq b < y\} \right)$$
によって帰納的に定める.

このとき, $(F_{2^n}, \oplus, \otimes)$ は $1$ を乗法単位元とする可換体になる.

### 計算

可換体 $(F_{2^n}, \oplus, \otimes)$ に対して, 以下が成り立つ. ただし, 非負整数 $k~(< n) $ に対して,
    $$e_k := 2^{2^k}, \quad e'_k := 2^{2^k - 1} \left(= e_k / 2 \right)$$
とする.

* $x \in F$ に対して, $x < e_k$ ならば, $x \otimes e_k = x \times e_k$ である.
* $e_k \otimes e_k = \frac{3}{2} e_k = e_k + e'_k = e_k \oplus e'_k $.

これらの性質により, $x, y \in F_{2^n}$ に対して, $x \oplus y$ の計算を次のようにして, $F_{2^{n-1}}$ 上の計算に帰着させることができる.

まず, $x,y \in F_{2^n}$ より, $x, y$ はそれぞれ $x_0, x_1, y_0, y_1 \in F_{2^{n-1}}$ を用いて,
    $$ x = x_1 e_{k-1} + x_0, \quad y = y_1 e_{k-1} + y_0 $$
と表せる.

すると,
$$
\begin{align*}
    x \otimes y
    &= (x_1 e_{k-1} + x_0) \otimes (y_1 e_{k-1} + y_0) \\
    &= (x_1 e_{k-1} \oplus x_0) \otimes (y_1 e_{k-1} \oplus y_0) \\
    &= (x_1 \otimes e_{k-1} \oplus x_0) \otimes (y_1 \otimes e_{k-1} \oplus y_0) \\
    &= \left((x_1 \otimes y_1) \otimes (e_{k-1} \otimes e_{k-1}) \right) \oplus \left((x_0 \otimes y_1 \oplus x_1 \otimes y_0) \otimes e_{k-1} \right) \oplus (x_0 \otimes y_0) \\
    &= \left((x_1 \otimes y_1) \otimes (e_{k-1} \otimes e'_{k-1}) \right) \oplus \left((x_0 \otimes y_1 \oplus x_1 \otimes y_0) \otimes e_{k-1} \right) \oplus (x_0 \otimes y_0) \\
    &= \left((x_1 \otimes y_1 \oplus x_0 \otimes y_1 \oplus x_1 \otimes y_0) \otimes e_{k-1} \right) \oplus (x_1 \otimes y_1 \otimes e'_{k-1}) \oplus (x_0 \otimes y_0) \\
    &= \left(((x_1 \otimes y_1 \oplus x_0 \otimes y_1 \oplus x_1 \otimes y_0 \oplus x_0 \otimes y_0) \oplus x_0 \otimes y_0) \otimes e_{k-1} \right) \oplus (x_1 \otimes y_1 \otimes e'_{k-1}) \oplus (x_0 \otimes y_0) \\
    &= \left(((x_1 \oplus x_0) \otimes (y_1 \oplus y_0) \oplus (x_0 \otimes y_0)) \otimes e_{k-1} \right) \oplus (x_1 \otimes y_1 \otimes e'_{k-1}) \oplus (x_0 \otimes y_0)\\
    &= \left(((x_1 \oplus x_0) \otimes (y_1 \oplus y_0) \oplus (x_0 \otimes y_0)) \times e_{k-1} \right) \oplus (x_1 \otimes y_1 \otimes e'_{k-1}) \oplus (x_0 \otimes y_0) \\
\end{align*}
$$

となり,
    $$(x_1 \oplus x_0) \otimes (y_1 \oplus y_0), \quad x_0 \otimes y_0, \quad x_1 \otimes y_1 \otimes e'_{k-1}$$
の $4$ つの "1 レベル下" の積に帰着される.

## Reference

* https://drive.google.com/file/d/16g1tfSHUU4NXNTDgaD8FSA1WB4FtJCyV/edit
* https://natsugiri.hatenablog.com/entry/2020/03/29/073605
