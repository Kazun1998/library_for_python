---
title: General Binary Search
documentation_of: //Binary_Search/General.py
---

## Outline

整数 (実数) $x$ に関する条件 $\operatorname{cond}(x)$ について, 以下を求める.

* $\operatorname{cond}$ が単調増加の場合 : $\operatorname{cond}(x)=\mathbb{T}$ になるような最小の整数 (実数) $x$.
* $\operatorname{cond}$ が単調減少の場合 : $\operatorname{cond}(x)=\mathbb{T}$ になるような最大の整数 (実数) $x$.

## Theory

$X$ は $\mathbb{Z}$ か $\mathbb{R}$ であるとする. $X$ 上の条件 $\operatorname{cond}: X \to \\{\mathbb{T}, \mathbb{F}\\}$ について, 以下を定義する.

* 以下を満たすとき, $\operatorname{cond}$ は単調増加であるという. $$\forall x \in X;\,\operatorname{cond}(x)=\mathbb{T} \Rightarrow \left(\forall y \geq x;\, \operatorname{cond}(x)=\mathbb{T} \right)$$
* 以下を満たすとき, $\operatorname{cond}$ は単調減少であるという. $$\forall x \in X;\,\operatorname{cond}(x)=\mathbb{F} \Rightarrow \left(\forall y \geq x;\,\operatorname{cond}(x)=\mathbb{F} \right)$$
* 単調増加または単調減少であるとき, 単調という.

$X=\mathbb{Z}$ とする. このとき, 単調増加である $\operatorname{cond}$ に対して, $\operatorname{cond}(x)=\mathbb{T}$ となる最小の $x \in \mathbb{Z}$ を $X$ として, $X$ を求める.

1. $L,R \in \mathbb{Z}$ を $\operatorname{cond}(L)=\mathbb{F}, \operatorname{cond}(R)=\mathbb{T}$ であるとする. このとき, $L \lt X \leq R$ が保証されている.
2. $R-L>1$ である限り, 以下を繰り返し行う.
    * $C:=\left \lfloor \dfrac{L+R}{2} \right \rfloor$ とする.
    * $\operatorname{cond}(C)=\mathbb{T}$ ならば, $L \lt X \leq C$ であることが分かる. よって, $R \gets C$ とする.
    * $\operatorname{cond}(C)=\mathbb{F}$ ならば, $C \lt X \leq L$ であることが分かる. よって, $L \gets C$ とする.
3. $R-L>1$ のとき, 初期値の定め方から, $R-L=1$ である. よって, $L \lt X \leq R$ となる整数 $X$ は $X=R$ に限られる. 従って, $R$ を出力すれば良い.

$\operatorname{cond}$ が単調減少の場合も同様であり, $X=\mathbb{R}$ の場合も $C:=\dfrac{L+R}{2}$ と変更すればよい. ただし, $X=\mathbb{R}$ の場合は厳密に求めることは不可能であり, ある程度の誤差の範囲で求めることになる.

また, $L, R$ は自分で見つける必要があり, $L,R$ が最初に満たすべき条件 (単調増加か単調減少かでかわる) を満たしていない場合は例外処理となる (特に $\operatorname{cond}(L)=\operatorname{cond}(R)=\mathbb{F}$) のとき.
