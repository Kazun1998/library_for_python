---
title: Affine
documentation_of: //Geometric/Affine.py
---

## Theory

### アフィン変換の定義

2次実行列 $A \in M_2(\mathbb{R})$ と2次ベクトル $\boldsymbol{b} \in \mathbb{R}^2$ に対して, 写像

$$\varphi(A, \boldsymbol{b}): \mathbb{R}^2 \to \mathbb{R}^2; \boldsymbol{x} \mapsto A \boldsymbol{x}+\boldsymbol{b}$$

をアフィン写像という.

このとき,

$$\varphi(A,\boldsymbol{b})(\boldsymbol{x})=\begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \end{pmatrix} \begin{pmatrix} A & \boldsymbol{b} \\ \boldsymbol{0}^\top & 1 \end{pmatrix} \begin{pmatrix} \boldsymbol{x} \\ 1 \end{pmatrix} $$

が成り立つ. このとき, 和とスカラー倍と積において,

* $\varphi(A, \boldsymbol{b})+\varphi(B, \boldsymbol{c})=\varphi(A+B, \boldsymbol{b}+\boldsymbol{c})$
* $\lambda \varphi(A, \boldsymbol{b})=\varphi(\lambda A, \lambda \boldsymbol{b})$
* $\varphi(A, \boldsymbol{b}) \circ \varphi(B, \boldsymbol{c})=\varphi(A+B, \boldsymbol{b}+\boldsymbol{c})=\varphi(AB, A \boldsymbol{c}+\boldsymbol{b})$

が成り立つ (積については真ん中の項の行列積の結果と一致する).

アフィン変換 $\varphi(A,\boldsymbol{b})$ に対して, $A$ を行列部, $\boldsymbol{b}$ をベクトル部という.

### アフィン変換の特徴づけ

* アフィン変換が **全単射** を持つことの必要十分条件は行列部が **正則行列** であることである.
* アフィン変換が **等距離写像** であることの必要十分条件は行列部が **直交行列** であることである.
* アフィン変換が **線形写像** になることの必要十分条件はベクトル部が **零ベクトル** になることである.

### 変換とアフィン変換

座標空間における変換の多くはアフィン変換によって記述できる.

* $\boldsymbol{v}$ だけ平行移動 $\cdots \varphi(I_2, \boldsymbol{v})$
* 点 $\mathrm{P}$ に関して対称移動 $\cdots \varphi(-I_2, -\mathrm{P})$

### アフィン変換の決定

同一直線上にない3点 $\mathrm{A}, \mathrm{B}, \mathrm{C}$ に対して, アフィン変換 $F$ で

$$F(\mathrm{A})=\mathrm{P}, \quad F(\mathrm{B})=\mathrm{Q}, \quad F(\mathrm{C})=\mathrm{R}$$

を満たすものが唯一存在する. つまり, 2次正方行列 $M$ と2次ベクトル $\boldsymbol{v}$ で

* $M \boldsymbol{a}+\boldsymbol{v}=\boldsymbol{p}$
* $M \boldsymbol{b}+\boldsymbol{v}=\boldsymbol{q}$
* $M \boldsymbol{c}+\boldsymbol{v}=\boldsymbol{r}$

を満たすものを求める. 式を引くことによって,

$$M (\boldsymbol{b}-\boldsymbol{a}, \boldsymbol{c}-\boldsymbol{a})=(\boldsymbol{q}-\boldsymbol{p}, \boldsymbol{r}-\boldsymbol{p})$$

である. $\mathrm{A}, \mathrm{B}, \mathrm{C}$ は同一直線上にない3点なので, 行列 $X:=(\boldsymbol{b}-\boldsymbol{a}, \boldsymbol{c}-\boldsymbol{b})$ は正則行列である. よって,

$$M=(\boldsymbol{q}-\boldsymbol{p}, \boldsymbol{r}-\boldsymbol{p})X^{-1}$$

である.

そして, $M \boldsymbol{a}+\boldsymbol{v}=\boldsymbol{p}$ を利用して $\boldsymbol{v}$ も求められる.
