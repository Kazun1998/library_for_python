---
title: Topological Sort
documentation_of: //Topological_Sort.py
---

## Outline

有向グラフ $D = (V, A)$ に対して, $V$ 上の全順序関係 $\leq$ が $D$ のトポロジカルソートであるとは, 以下を満たすことである.

* 任意の $u, v \in V~(u \neq v)$ に対して, $\overrightarrow{uv} \in A$ ならば, $u \leq v$ である.

位数 $N$, サイズ $M$ の有向グラフ $D$ に対して, $D$ のトポロジカルソートの存在判定及び構築を $O(N + M)$ 時間で行う.

## Theory

有向グラフ $D = (V, A)$ に対して, 以下が同値になる.

* (a) $D$ のトポロジカルソートが存在する.
* (b) $D$ において, サイクルが存在しない.

これを証明する.

### Proof

#### (a) ならば (b)

対偶を証明する. $D$ 上の有向サイクルを $v_1 v_2 \dots v_k$ ($k$ 個の頂点は全て相異なる) とする.

$\leq$ を $D$ 上の Topological Sort とする. ここで, サイクルの対称性により,

$$ v_1 = \min_{\leq}(v_1, v_2, \dots, v_k) $$

であるとしても一般性を失わない.

すると, $\overrightarrow{v_k v_1} \in A$ となるが, $\leq$ が Topological Sort より $v_k \leq v_1$ である.

一方で, $v_1$ の定め方より, $v_1 \leq v_k$ である.

$\leq$ が全順序であるので, $v_1 = v_k$ となる.

しかし, $v_1, \dots, v_k$ が相異なる $k$ 個の頂点であることに矛盾する.

よって, $D$ に Topological Sort は存在しない.

#### (b) ならば (a)

DAG $D$ の位数 $n$ に関する数学的帰納法で示す.

$1$ 頂点のときは任意の順序がトポロジカルソートになる.

$(n-1)$ 頂点の任意の DAG が Topological Sort を持つと仮定する. $D$ が $n$ 頂点の DAG とする.

$D$ は DAG なので, 入近傍が存在しない頂点 $x \in V$ が存在する. $D$ から頂点 $x$ を除いた $D$ の部分グラフ $D' := D - x$ は $D$ が DAG であるから, $D'$ も DAG である.

$D'$ の位数が $(n-1)$ であるので, 数学的帰納法の仮定により, $D'$ の Topological Sort $\leq'$ が存在する.

この $\leq'$ を用いて, $V$ 上の関係 $\leq$ を次のようにして定義する. ただし, $u,v \in V$ とする.

$$ u \leq v :\iff (u = x) \lor (u,v \neq x \land u \leq' v) $$

すると, この $\leq$ は $D$ 上の Topological Sort になる. 実際, $\overrightarrow{uv} \in A~(u \neq v)$ に対して,

* $u = x$ のときは, $\leq$ の定義により $u \leq v$ である.
* $v = x$ とはなり得ない. これは $x$ が $D$ 上で入近傍が存在しない頂点として取ってきており, $u \neq v$ であることから従う.
* $u,v \neq x$ のときは, $u \leq' v$ より $u \leq v$ となる.

この同値性における 「(b) ならば (a)」の証明を利用することによって, Topological Sort の判定と構築を行うことができる.
