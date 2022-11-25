---
title: Run Length Encoding
documentation_of: //Sequence/Run_Length_Encoding.py
---

## Outline

$\mathcal{A}$ をアルファベットする. 長さ $N$ の $\mathcal{A}$ の列 $S=(S\_i)\_{i=1}^N$ に対して, 以下を満たすような列 $T=((\alpha\_j, k\_j))\_{j=1}^M$ を求める.

* $\forall j=1,2, \dots, M;~\alpha \in \mathcal{A}, k_j \geq 0$.
* $\forall j=1,2, \dots, M-1;~\alpha_j \neq \alpha_{j+1}$
* $S=(\underbrace{\alpha_1, \dots, \alpha_1}\_{k_1}, \dots, \underbrace{\alpha_M, \dots, \alpha_M}\_{k_M})$

このような $T$ を $S$ の Run Length Encoding (連長圧縮) という. なお, RLE は一意に定まる.
