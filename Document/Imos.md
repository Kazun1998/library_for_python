---
title: Imos 法
documentation_of: //Imos.py
---

## Outline

最初に $M$ 個の区間加算クエリが与えられた後の $Q$ 個の一点取得クエリの処理をまとめて $O(M + Q)$ 時間で行うことができる.

## Theory

$R$ を環として, $\mathcal{A}$ を $R$ を要素に持つ列全体の集合とする. このとき, $\mathcal{A}$ は区間ごとの和とスカラー倍によって, $R$ 係数の加群と見ることができる.

写像 $D: \mathcal{A} \to \mathcal{A}$ を

$$ D\bm{e}_n := \bm{e}_n - \bm{e}_{n+1} $$

となるような線形写像で定める. ただし, $\bm{e}_n$ とは, 第 $n$ 項のみ $1$ でそれ以外が全て $0$ である列とする.

すると,

$$ D \left(\sum_{n=l}^r \bm{e}_n \right) = \sum_{n=l}^r D \bm{e}_n = \sum_{n=l}^r (\bm{e}_n - \bm{e}_{n+1}) = \bm{e}_l - \bm{e}_{r+1} $$

になる.

従って, $Q$ 個の区間加算クエリの合計を $D$ で送った像は次のように, $2N$ 個の項の和で表すことができる.

$$ \begin{align*}
  D \left(\sum_{q=1}^Q \left( \alpha_q \sum_{n={l_q}}^{r_q} \bm{e}_n \right) \right)
  &= \sum_{q=1}^Q \alpha_q \left(D \sum_{n={l_q}}^{r_q} \bm{e}_n \right) \\
  &= \sum_{q=1}^Q \alpha_q (\bm{e}_{l_q} - \bm{e}_{r_q + 1}) \\
  &= \sum_{q=1}^Q (\alpha_q \bm{e}_{l_q} - \bm{e}_{r_q + 1})
\end{align*} $$

そして, $D$ は同型写像になる. 実際, $D^{-1}: \mathcal{A} \to \mathcal{A}$ は以下を満たす線形写像となる.

$$ D^{-1} \bm{e}_n = \sum_{k=0}^n \bm{e}_k $$

よって,

$$ \bm{x} := \sum_{n=0}^\infty \alpha_n \bm{e}_n $$

とすると,

$$ T_n D^{-1} \bm{x} = \sum_{k=0}^n \alpha_k $$

となる. 特に, $n \geq 1$ のときは

$$ T_n D^{-1} \bm{x} = T_{n-1} D^{-1} \bm{x} + \alpha_n $$

となる. これはまさに $(T_n D^{-1} \bm{x})$ の累積和を表している式になる.

以上から,

$$ \bm{y} := \sum_{q=1}^Q \left( \alpha_q \sum_{n={l_q}}^{r_q} \bm{e}_n \right) $$

は

$$ \bm{x} := D \bm{y} = \sum_{q=1}^Q (\alpha_q \bm{e}_{l_q} - \bm{e}_{r_q + 1}) $$

として, $\beta_n$ を $\beta_n := T_n \bm{x}$ で定めることによって,

$$ T_n \bm{y} = \begin{cases} \beta_0 & (n = 0) \\ T_{n-1} \bm{y} + \beta_n & (n \geq 1) \end{cases} $$

で求められる.
