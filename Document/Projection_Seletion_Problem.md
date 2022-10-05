---
title: Projection_Selection_Problem
documentation_of: //Flow/Projection_Selection_Problem.py.py
---

## Outline

$\mathbb{Z}':=\mathbb{Z} \cup \\{\pm \infty\\}$ とする.

$X, \Lambda$ を有限集合とし, 各 $\lambda \in \Lambda$ には評価観点 $\tau_\lambda : \operatorname{Map} (X, \\{0,1\\}) \to \mathbb{Z}$ が設定されている. このとき,
$$\operatorname{eval} : \operatorname{Map} (X, \\{0,1\\}) \to \mathbb{Z}; \quad h \mapsto \sum_{\lambda \in \Lambda} \tau_\lambda(h)$$
の最大値及び, それを達成する一例を求めたい.

一般的には $N:=\# X, K:=\# \Lambda$ とすると, 時間計算量として, $O(K 2^N)$ TIme かかってしまうが, 評価観点 $\tau_\lambda$ が特別な場合は最大フローを用いて高速に計算することが出来る.

主には以下のような場合に適用できる. ただし, $x_{\lambda}, y_{\lambda}, x_{\lambda, i} \in X, a_\lambda, b_\lambda \in \mathbb{Z}'$ で, $a_\lambda^\pm \in \mathbb{Z}$ はそれぞれ正 (負) であるとする.

* $\tau_\lambda(h)=\begin{cases} a_{\lambda} & (h(x_\lambda)=0) \\ b_{\lambda} & (h(x_\lambda)=1) \end{cases}$
* $\tau_\lambda(h)=\begin{cases} a^{-}_{\lambda} & (h(x_\lambda)=0, h(y_\lambda)=1) \\ 0 & ({\rm otherwise}) \end{cases}$
* $\tau_\lambda(h)=\begin{cases} a^{+}_{\lambda} & (h(x_{\lambda,1})=\dots=h(x_{\lambda, m_\lambda})=0) \\ 0 & ({\rm otherwise}) \end{cases}$
* $\tau_\lambda(h)=\begin{cases} a^{+}_{\lambda} & (h(x_{\lambda,1})=\dots=h(x_{\lambda, m_\lambda})=1) \\ 0 & ({\rm otherwise}) \end{cases}$

なお, 上に無いような評価観点においても, 工夫することによって, 最大フローを利用することができる場合がある.

* [1] $\tau_\lambda(h)=\begin{cases} a^{-}_{\lambda} & (h(x_\lambda)=h(y_\lambda)=0) \\ 0 & ({\rm otherwise}) \end{cases} \quad \left(\begin{cases} a^{-}_{\lambda} & (h(x_\lambda)=h(y_\lambda)=1) \\ 0 & ({\rm otherwise}) \end{cases} \right)$ の場合.
  * グラフが二部グラフ (部集合を $A,B$ とする) であり, $x_\lambda \in A, y_\lambda \in B$ ならば, 以下のようにして変換する: $$h'(z)=\begin{cases} h(z) & (z \in X) \\ 1-h(z) & (z \in Y) \end{cases}$$ と変換する.
  こうすると, $$\tau_\lambda(h')=\begin{cases} a^{-}_{\lambda} & (h'(x_\lambda)=0, h'(y_\lambda)=1) \\ 0 & ({\rm otherwise}) \end{cases}$$ に帰着できる.
* [2] $\tau_\lambda(h)=\begin{cases} a^{+}_{\lambda} & (h(x_\lambda) \neq h(y_\lambda)) \\ 0 & ({\rm otherwise}) \end{cases}$ の場合
  * グラフが二部グラフ (部集合を $A,B$ とする) であり, $x_\lambda \in A, y_\lambda \in B$ ならば, 以下のようにして変換する. $$h'(z)=\begin{cases} h(z) & (z \in X) \\ 1-h(z) & (z \in Y) \end{cases}$$ と変換する. このようにすると, $$\tau_\lambda(h')=a^{+}_\lambda+\begin{cases} -a^+_\lambda & (h'(x_\lambda)=h'(y_\lambda)) \\ 0 & ({\rm otherwise}) \end{cases}$$ となる.
  右辺の第2項は [1] に帰着される.
