---
title: Or Convolution
documentation_of: //Convolution/OR_Convolution.py
---

## Outline

以降では $N$ を正の整数とし, $(\!(N)\!)$ を $N$ 未満の非負整数全体の集合とする. つまり,
$$(\!(N)\!)=\\{0,1,2 \dots, N-1\\}$$
である.

長さ $2^N$ の数列, $A=(A_i)_{0 \leq i \lt 2^N}, B=(B_j)_{0 \leq j \lt 2^N}$ に対し, $A,B$ の Or Convolution $A \oplus B$ を

$$A \oplus B:=\left(\sum_{\substack{0 \leq i,j \lt 2^N \\ i ~\lor~ j=k}} A_i B_j \right)_{0 \leq k \lt 2^N}$$

と定義する.

なお, 写像 $\operatorname{bit}: \mathcal{P}((\!(N)\!)) \to (\!(2^N)\!)$ を
$$\operatorname{bit}(S):=\sum_{a \in S} 2^a$$
と定義すると, $\operatorname{bit}$ はこの2つモノイド $((\!(2^N)\!), \lor), (\mathcal{P}((\!(N)\!)), \cup)$ 間の同型写像になることから, 次のような言い換えができる.

> $A,B$ は添字集合が $\mathcal{P}((\!(N)\!))$ である列であるとする.
> このとき, $A=(A_S)_{S \in \mathcal{P}((\!(N)\!))}, B=(B_T)_{T \in \mathcal{P}((\!(N)\!))}$ の Or Convolution $A \oplus B$ を
> $$A \oplus B:=\left(\sum_{\substack{S,T \in \mathcal{P}((\!(N)\!)) \\ S ~\cup~ T=U}} A_S B_T \right)_{U \in \mathcal{P}((\!(N)\!))}$$
> と定義する.
