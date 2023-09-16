---
title: Project Selection Problem
documentation_of: //Flow/Project_Selection_Problem.py
---

## Outline

$X,I$ を有限集合とする. 各 $i \in I$ に対して, 観点 $\tau_i: \mathrm{Map}(X, \{0,1\}) \to \mathbb{Z}$ が定まっている.

そして, この観点によって, 評価 $\operatorname{eval}: \mathrm{Map}(X, \{0,1\}) \to \mathbb{Z}$ を
$$\operatorname{eval}(h) := \sum_{i \in I} \tau_i(h)$$
として定める.

このとき, $h \in \mathrm{Map}(X, \{0,1\})$ における $\operatorname{eval}(h)$ の最大値と, 最大値を達成する $h$ を求める.

## Theory

$\tau_i$ が全て特殊な形であるとき, この問題は最小カット問題に帰着できる. そして, 最小カット問題は最大フロー問題の双対問題である. 従って, 最大フロー問題で解くことができる.

最大フロー問題で解くことができるような $\tau_i$ は以下のような形式である.

ただし,

* $x_i, y_i, z_{i,j} \in X$.
* $a_i, b_i$ は整数, $a_{+,i}$ は非負の整数, $a_{-,i}$ は非正の整数.

とする.

* $\tau_i(h) =\begin{cases} a_i & (h(x_i) = 0) \\ b_i & (h(x_i) = 1) \end{cases}$
* $\tau_i(h) = \begin{cases} a_{-,i} & (h(x_i) = 0, h(y_i) = 1) \\ 0 & (\text{otherwise}) \end{cases}$
* $\tau_i(h) = \begin{cases} a_{+,i} & (h(z_{i,1}) = \dots = h(z_{i, k_i}) = 0) \\ 0 & (\text{otherwise}) \end{cases}$
* $\tau_i(h) = \begin{cases} a_{+,i} & (h(z_{i,1}) = \dots = h(z_{i, k_i}) = 1) \\ 0 & (\text{otherwise}) \end{cases}$

---
なお, 以下の場合については, 一般的には対応できないが, 特殊な状況下では適当な変形によって最小カットに帰着できる.

(Pattern 1)

* 任意の $i \in I$ に対して, $\tau_i$ は以下の形式のいずれかである.
  * $\tau_i(h) =\begin{cases} a_i & (h(x_i) = 0) \\ b_i & (h(x_i) = 1) \end{cases}$
  * $\tau_i(h) = \begin{cases} a_{-,i} & (h(x_i) = h(y_i) = 0) \\ 0 & (\text{otherwise}) \end{cases}$
  * $\tau_i(h) = \begin{cases} a_{-,i} & (h(x_i) = h(y_i) = 1) \\ 0 & (\text{otherwise}) \end{cases}$
* $2$ 番目または $3$ 番目の形である $i \in I$ 全体の集合を $J$ として, $$E:=\{x_j y_j \mid j \in J\}$$ としたとき, 無向グラフ $(X,E)$ は二部グラフになる.

このとき, 二部グラフ $(X,E)$ の部集合を $A,B$ とする. $\bullet': \mathrm{Map}(X, \{0,1\}) \to \mathrm{Map}(X, \{0,1\})$ を
$$h'(x) = \begin{cases} h(x) & (x \in A) \\ 1-h(x) & (x \in B) \end{cases}$$
と定めると, $\bullet'$ は全単射になり, $h'$ に関して最小カットへ帰着できる.

(Pattern 2)

* 任意の $i \in I$ に対して, $\tau_i$ は以下の形式のいずれかである.
  * $\tau_i(h) =\begin{cases} a_i & (h(x_i) = 0) \\ b_i & (h(x_i) = 1) \end{cases}$
  * $\tau_i(h) = \begin{cases} a_{+,i} & (h(x_i) \neq h(y_i)) \\ 0 & (\text{otherwise}) \end{cases}$
* $2$ 番目の形である $i \in I$ 全体の集合を $J$ として, $$E:=\{x_j y_j \mid j \in J\}$$ としたとき, 無向グラフ $(X,E)$ は二部グラフになる.

このとき, $\bullet'$ を考えることにより, 次のようにして帰着できる.

* $\displaystyle \sum_{j \in J} a_{+,j}$ 点の下駄を履かせて, 「$h(x_j)=h(y_j)$ ならば $-a_{+,j}$ 点を得る」に置き換えることにより, (Pattern 1) に帰着させる.

このとき, 帰着先での最大値を $X$ としたとき, 本問題での最大値は $\displaystyle \left(\sum_{j \in J} a_{+,j} + X \right)$ であることに注意.
