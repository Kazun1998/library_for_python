---
title: Modulo Polynominal
documentation_of: //Modulo_Sequence/Modulo_Polynominal.py
---

## Outline

多項式, 形式的ベキ級数に関する計算を行う.

## Theory

### 解析

$f \in \mathbb{F}_p[\\![X]\\!]$ に対する形式的積分 $\displaystyle \int f(X)~dX$ , 形式的微分 $f'(X)$ をそれぞれ

- $\displaystyle f'(X)=\sum_{n=0}^{\infty} (n+1) f_{n+1} X^n$
- $\displaystyle \int f(X) dX=\sum_{n=0}^{\infty} \dfrac{f_n}{n+1} X^{n+1}$

と定義する.

### Newton 法

線形部分空間 $D \subset \mathbb{F}_p[\\![X]\\!]$ に対して, $T: D \to \mathbb{F}_p[\\![X]\\!]$ が与えられているとする. このとき, $f \in \mathbb{F}_p$ に対して, $T(g)=f$ となる $g \in D$ を求めたい.

$T(\beta)=f_0$ となる $\beta \in F_p$ を何かしらの方法で求め, $g^{(1)}=\beta$ とする.

$T(g^{(N)}) \equiv f \pmod{X^N}$ となる多項式 $g^{(N)}$ が求まっているとする. Taylor 展開から

$$f=T(g)=T(g^{(N)})+T'(g^{(N)})(g-g^{(N)})+O((g-g^{(N)})^2)$$

となる. $\pmod{X^{2N}}$ での剰余を考えることによって,

$$f \equiv T(g^{(N)})+T'(g^{(N)})(g-g^{(N)}) \pmod{X^{2N}}$$

となる. これを整理することによって,

$$g \equiv g^{(N)}+\dfrac{f-T(g^{(N)})}{T'(g^{(N)})} \pmod{X^{2N}}$$

となる. よって, $g^{(2N)}:=g^{(N)}+\dfrac{f-T(g^{(N)})}{T'(g^{(N)})} \pmod{X^{2N}}$ とすればよい.

### 逆元

$f \in \mathbb{F}_p[\\![X]\\!]$ に対して, $f_0 \neq 0$ ならば, $fg=1$ となる $g \in \mathbb{F}_p[\\![X]\\!]$ が存在する.

$D$ を $f_0 \neq 0$ となる $f \in \mathbb{F}_p[\![X]\!]$ 全体の集合とする. $T: D \to \mathbb{F}_p[\\![X]\\!]$ を $T(g):=g^{-1}$ と定める.

Newton 法で求める. $g^{(0)}=f_0^{-1}$ である. また, $T'(g)=-\dfrac{1}{g^2}$ であるから,

$$g^{(2N)}=g^{(N)}+\dfrac{f-(1/g^{(N)})}{-(1/{g^{(N)}}^2)}=g^{(N)}(2-fg^{(N)})$$

となる.

### 対数関数

$f \in F_p[\\![X]\\!]$ に対して, $\displaystyle \log f:=\int \dfrac{f(X)}{f'(X)}~dX$ と定義する.

### 指数関数

$f_0=0$ となる $f \in \mathbb{F}_p[\\![X]\\!]$ に対して, $\displaystyle \exp f:=\sum_{n=0}^{\infty} \dfrac{f_n}{n!} X^n$ と定義する.

このとき, $\exp (\log f)=\log(\exp f)=f$ が成り立つ. よって, $g=\exp f \iff f=\log g$ である.

Newton 法において, $T(g):=\log g$ とすると, $T'(g)=\dfrac{1}{g}$ であるから, $g^{(1)}=1$ 及び,

$$g^{(N)}+\dfrac{f-\log g^{(N)}}{\log'g^{(N)}}=g^{(N)}(1+f-\log g^{(N)})$$

となるから, $g^{(2N)}=g^{(N)}(1+f-\log g^{(N)}) \pmod{X^{2N}}$ である.

### 累乗

$f \in \mathbb{F}_p[\\![X]\\!]$ に対して, $f \neq 0$ ならば, $f=\alpha X^d g, g_0=1$ となる $\alpha \in F_p^\times, d \geq 0, g \in \mathbb{F}_p[\\![X]\\!]$ が唯一存在する. ここで, $g=\exp(\log g)$ であるから, $g^M=\exp(M \log g)$ である. これを利用することによって, $f^M=\alpha^M X^{Md} \exp(M \log g)$ となる.

### 平方根

$f \in \mathbb{F}_p[\\![X]\\!]$ に対して, $h^2=f$ となる $\mathbb{F}_p[\\![X]\\!]$ となる $h$ が存在することと, 以下の2条件のうち, どちらか一方が成り立つことは同値である.

- $f=0$
- $f=\alpha X^d g, g_0=1$ となる $\alpha \in F_p$, 非負整数 $d$, $g_0 \in \mathbb{F}_p[\\![X]\\!]$ は唯一存在するが, $\alpha$ が平方剰余で, $d$ が偶数.

$g_0=1$ とする. このとき, $T(h):=h^2$ として, $T(h)=g$ となる $h$ を Newton 法で求めることにする.

まず, $h^{(1)}=1$ である. また, $T'(h)=2hh'$ であるから,

$$g^{(N)}+\dfrac{f-{g^{(N)}}^2}{2g^{(N)}}=\dfrac{1}{2}\left(g^{(N)}+\dfrac{f}{g^{(N)}} \right)$$

より, $g^{(2N)}=\dfrac{1}{2}\left(g^{(N)}+\dfrac{f}{g^{(N)}} \right) \pmod{X^{2N}}$ である.

### 多項式の商と剰余

$f,g \in \mathbb{F}_p[X]$ は多項式で, $g \neq 0$ であるとする. このとき, $f=q g+r, \deg r < \deg g$ となる多項式の組 $(q,r)$ が唯一存在する. このとき, $q,r$ をそれぞれ多項式 $f$ を多項式 $g$ で割った商, 余りという.

多項式 $h$ が高々 $K$ 次になるとき, $\widetilde{h}(X):=h(X^{-1}) X^K$ は多項式になる. なお, $h(X)=\alpha_0+\alpha_1 X+\dots+\alpha_K X^K$ のとき, $h(X)=\alpha_K+\dots+\alpha_1 X^{K-1}+\alpha_0 X^K$ である.

$\deg f=N, \deg g=M$ とすると, $\deg q=N-M, \deg r<M$ となる. $f=q g+r$ の両辺に $X^N$ を掛けると,

$$\widetilde{f}=\widetilde{g} \widetilde{q}+\widetilde{r} X^{N-(M-1)} \equiv \widetilde{g} \widetilde{q} \pmod{X^{N-M+1}}$$

である. $g \neq 0$ から, $\left(\widetilde{g} \right)_0 \neq 0$ なので,

$$\widetilde{q}=\dfrac{\widetilde{f}}{\widetilde{g}} \pmod{X^{N-M+1}}$$

であり, $q=\widetilde{\widetilde{q}}$ によって $q$ を求めることが出来る. これにより, $r=f-pg$ で $r$ も求められる.

### 除算における $N$ 次の係数

$P$ は高々 $(d-1)$ 次未満の多項式, $Q$ は $d$ 次の多項式であるとする. このとき,

$$\left[X^N \right] \dfrac{P(X)}{Q(X)}$$

を求めたい.

$\left[X^0 \right] Q \in \mathbb{F}_p^\times$ とする.

分子と分母の両方に $Q(-X)$ を掛けると, $Q(X)Q(-X)$ が偶多項式になるので, $V(X^2)=Q(X)Q(-X)$ となる多項式 $V$ が存在する.

また, 多項式 $P(X)Q(-X)$ を $P(X)Q(-X)=S_{{\rm even}}(X^2)+XS_{{\rm odd}}(X^2)$ と分解する.

このとき, 分母が偶多項式であるから, $N$ が偶数のときは

$$\left[X^N \right] \dfrac{P(X)}{Q(X)}=\left[X^N \right] \dfrac{S_{{\rm even}}(X^2)}{V(X^2)}=\left[X^{N/2} \right] \dfrac{S_{{\rm even}}(X)}{V(X)}\$$

が成り立つ. $N$ が奇数のときも同様にして,

$$\left[X^N \right] \dfrac{P(X)}{Q(X)}=\left[X^N \right] \dfrac{XS_{{\rm odd}}(X^2)}{V(X^2)}=\left[X^{(N-1)/2} \right] \dfrac{S_{{\rm odd}}(X)}{V(X)}\$$

が成り立つ.

これにより, 1回関係式を利用することにより, 求める指数をが $1/2$ に落とすことが出来る.

また, 自明な場合として,

$$\left[X^0 \right] \dfrac{P(X)}{Q(X)}=\dfrac{\left[X^0 \right] P}{\left[X^0 \right] Q}$$

が成り立つ.

よって, $d$ 次の多項式の積を $O(\log N)$ 回求めることによって, $\displaystyle \left[X^N \right] \dfrac{P(X)}{Q(X)}$ を求めることができる.

この多項式の積を求めるパートがボトルネックになるから, 計算量は $O(d \log d \log N)$ Time である.
