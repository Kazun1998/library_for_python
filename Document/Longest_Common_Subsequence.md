---
title: Longest Common Subsequence (最長共通部分列)
documentation_of: //Sequence/Longest_Common_Subsequence.py
---

## Outline

2つの列 $S,T$ に対する最長共通部分や, その長さを求める.

## Theory

$\mathcal{A}$ をアルファベットとする. $S \in W(\mathcal{A})$ に対して, 以下を満たすような正の整数列 $\rho$ が存在するとき, $T \in W(\mathcal{A})$ は $S$ の部分列であるという.

* $i=1,2, \dots, \lvert T \rvert$ に対して, $S_{\rho(i)}=T_i$ が成り立つ.

2つの列 $S,T \in W(\mathcal{A})$ に対して, $S,T$ 両方の部分列であるような列のことを $S,T$ の共通部分列という.

$S,T$ の共通部分列のうち, 長さが最大であるようなものを最長共通部分列という (存在はするが, 一意とは限らない).

$S,T$ の最長共通部分列の長さは以下のようにして動的計画法で求めることができる.

${\rm DP}[i,j]$ を $S[1:i], T[1:j]$ の最長共通部分列の長さとする. 自明なケースとして,

$${\rm DP}[0,j]=0 \quad (0 \leq j \leq \lvert T \rvert), \quad {\rm DP}[i,0]=0 \quad (0 \leq i \leq \lvert S \rvert)$$

である.

また, 更新式は次のようになる.

$${\rm DP}[i,j]=\begin{cases} {\rm DP}[i-1, j-1]+1 & (S_i=T_j) \\ \max ({\rm DP}[i-1,j], {\rm DP}[i, j-1]) & (S_i \neq T_j) \end{cases}$$

この動的計画法によって, ${\rm DP}[\lvert S \rvert, \lvert T \rvert]$ が $S,T$ の最長共通部分列の長さになる.
