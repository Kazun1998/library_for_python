---
title: Imos 法
documentation_of: //Imos.py
---

## Outline

最初に $M$ 個の区間加算クエリが与えられた後の $Q$ 個の一点取得クエリの処理をまとめて $O(M + Q)$ 時間で行うことができる.

## Theory

$R$ を環として, $\mathcal{A}$ を $R$ を要素に持つ列全体の集合とする. このとき, $\mathcal{A}$ は区間ごとの和とスカラー倍によって, $R$ 係数の加群と見ることができる.

写像 $D: \mathcal{A} \to \mathcal{A}$ を

$$ D\boldsymbol{e}_n := \boldsymbol{e}_n - \boldsymbol{e}_{n+1} $$

となるような線形写像で定める. ただし, $\boldsymbol{e}_n$ とは, 第 $n$ 項のみ $1$ でそれ以外が全て $0$ である列とする.

すると,

$$ D \left(\sum_{n=l}^r \boldsymbol{e}_n \right) = \sum_{n=l}^r D \boldsymbol{e}_n = \sum_{n=l}^r (\boldsymbol{e}_n - \boldsymbol{e}_{n+1}) = \boldsymbol{e}_l - \boldsymbol{e}_{r+1} $$

になる.

従って, $Q$ 個の区間加算クエリの合計を $D$ で送った像は次のように, $2N$ 個の項の和で表すことができる.

$$ \begin{align*}
  D \left(\sum_{q=1}^Q \left( \alpha_q \sum_{n={l_q}}^{r_q} \boldsymbol{e}_n \right) \right)
  &= \sum_{q=1}^Q \alpha_q \left(D \sum_{n={l_q}}^{r_q} \boldsymbol{e}_n \right) \\
  &= \sum_{q=1}^Q \alpha_q (\boldsymbol{e}_{l_q} - \boldsymbol{e}_{r_q + 1}) \\
  &= \sum_{q=1}^Q (\alpha_q \boldsymbol{e}_{l_q} - \alpha \boldsymbol{e}_{r_q + 1})
\end{align*} $$

そして, $D$ は同型写像になる. 実際, $D^{-1}: \mathcal{A} \to \mathcal{A}$ は以下を満たす線形写像となる.

$$ D^{-1} \boldsymbol{e}_n = \sum_{k=0}^n \boldsymbol{e}_k $$

よって,

$$ \boldsymbol{x} := \sum_{n=0}^\infty \alpha_n \boldsymbol{e}_n $$

とすると,

$$ T_n D^{-1} \boldsymbol{x} = \sum_{k=0}^n \alpha_k $$

となる. 特に, $n \geq 1$ のときは

$$ T_n D^{-1} \boldsymbol{x} = T_{n-1} D^{-1} \boldsymbol{x} + \alpha_n $$

となる. これはまさに $(T_n D^{-1} \boldsymbol{x})$ の累積和を表している式になる.

以上から,

$$ \boldsymbol{y} := \sum_{q=1}^Q \left( \alpha_q \sum_{n={l_q}}^{r_q} \boldsymbol{e}_n \right) $$

は

$$ \boldsymbol{x} := D \boldsymbol{y} = \sum_{q=1}^Q (\alpha_q \boldsymbol{e}_{l_q} - \boldsymbol{e}_{r_q + 1}) $$

として, $\beta_n$ を $\beta_n := T_n \boldsymbol{x}$ で定めることによって,

$$ T_n \boldsymbol{y} = \begin{cases} \beta_0 & (n = 0) \\ T_{n-1} \boldsymbol{y} + \beta_n & (n \geq 1) \end{cases} $$

で求められる.
