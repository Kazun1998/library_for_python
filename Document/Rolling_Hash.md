---
title: Rolling  Hash
documentation_of: //Rolling_Hash.py
---

## Outline

列に対して, Rolling Hash を用いて一致判定を高速化する.

## Theory

$\mathcal{A}$ をアルファベット (文字全体の集合) とし, $p$ を $\\# \mathcal{A}$ より非常に大きい **素数** とする.

また, $\beta \in \mathbb{F}\_p$ とし, $h: \mathcal{A} \to \mathbb{F}\_p$ を単射とする. このとき, $\mathcal{A}$ の列 $S=(S\_i)\_{i=1}^{\left \lvert S \right \rvert}$ に対する Rolling Hash $\operatorname{hash}(S)$ を

$$\operatorname{hash}(S):=\sum_{i=1}^{\left \lvert S \right \rvert} S_i \beta^{\left \lvert S \right \rvert-i}$$

と定義する.

$R=0,1,2, \dots, \lvert S \rvert$ に対して, $H_R$ を

$$H_R:=\begin{cases} \operatorname{hash}(S[1:R]) & (R \geq 0) \\ 0 & (R=0) \end{cases}$$

と定義する. すると, $1 \leq L \leq R \leq \lvert S \rvert$ に対して,

$$\operatorname{hash}(S[L:R])=H_R-H_{L-1}\beta^{R-L}$$

が成り立つ.
