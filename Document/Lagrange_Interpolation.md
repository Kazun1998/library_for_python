---
title: Lagrange Interpolation
documentation_of: //Lagrange_Interpolation.py
---

## Outline

$(N+1)$ 個の条件 $y_i=f(x_i)$ $(0 \leq i \leq N)$ を満たす高々 $N$ 次多項式 $f(x)$ や, $f$ のある点での値 $f(X)$ を求める.

## Theory

$x_0, \dots, x_N$ は全て異なるとする. このとき, $(N+1)$ 個の条件式

$$y_i=f(x_i) \quad (0 \leq i\leq N)$$

を満たす高々 $N$ 次の多項式を求める. $x_0, \dots, x_N$ が全て異なるという条件下では $f$ は必ず一意に存在する.

$i=0,1,2, \dots, N$ に対して, Lagrange 基底多項式 $\ell_i(x)$ を

$$\ell_i(x):=\prod_{\substack{0 \leq k \leq N \\ k \neq i}} \dfrac{x-x_k}{x_i-x_k}$$

とする. このとき, $j=0,1, \dots, N$ に対して,

$$\ell_i(x_j)=[i=j]$$

が成り立つ.

よって,

$$f:=\sum_{i=0}^N y_i \ell_i$$

がその求めるべき多項式になる.

ここで, $x_0, \dots, x_N$ が等差数列であったとする. つまり, $x_i=ai+b$ であるとする. このとき,

$$x_i-x_k=(ai+b)-(ak+b)=a(i-k)$$

が成り立つから, Lagrange 基底多項式は

$$\begin{align*}
\ell_i(x)
&=\prod_{\substack{0 \leq k \leq N \\ k \neq i}} \dfrac{x-x_k}{x_i-x_k} \\
&=\prod_{\substack{0 \leq k \leq N \\ k \neq i}} \dfrac{x-(ai+b)}{a(i-k)} \\
&=\dfrac{1}{(-a)^N} \cdot \dfrac{{\rm Left}_{i-1}(x) \cdot {\rm Right}_{i+1}(x)}{(-1)^{i} i! (N-i)!} \\
\end{align*}$$

である. ただし,

$${\rm Left}_i(x):=\prod_{k=0}^i (x-(ak+b)), \quad {\rm Right}_i(x):=\prod_{k=i}^N (x-(ak+b))$$

である.

よって, 評価点の $x$ 座標が等差数列であるとき, ある点 $X$ での値 $f(X) \pmod{P} $ を $O(N+\log P)$ 時間で求めることができる.
