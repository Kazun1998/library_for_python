---
title: Functional Graph
documentation_of: //Functional_Graph/Functional_Graph.py
---

## Outline

Functional Graph における様々な計算を行う.

## Theory

### 定義

各頂点における出次数が $1$ であるような有向グラフを Functional Graph という.

このとき, 次の2つは1対1対応する.

* Functional Graph
* Map $F: V \to V$

対応の方法としては, Function Graph $D=(V,A)$ において, 各 $v \in V$ に対して唯一の出近傍を $F(v)$ で割り当てればよく. 逆に, 写像 $F: V \to V$ に対して, 有向グラフ $D=(V,A)$ を

$$A=\\{\overrightarrow{v F(v)} \mid v \in V\\}$$

とすると, $D$ は Functional Graph になる.

### サイクルへの分解

Functional Graph $D=(V,A)$ において, 各弱連結成分は次のものから構成されている.

* 有向サイクル $C: v_1 v_2 \dots v_m$
* $j=1,2, \dots, m$ に対して, $v_j$ を根とする根付き木 (ただし, 根付き木における各辺の向きは根へ向かう向きである).

このことから, 非負整数 $k$ と $v \in V$ が与えられたとき, $v$ から有向辺で $k$ 回辿った頂点 $w$ を次の方法で前計算のもと, 各クエリに対して $O(\log N)$ 時間/クエリ で求めることができる.

* $v$ がサイクル上の頂点であるとき, 周期性を利用することによって $w$ を $O(1)$ 時間で求められる.
* $v$ がサイクル上の頂点ではないとき, $v$ が属する部分木における頂点 $v$ の深さを $d$ とする.
  * $k \leq d$ ならば, $w$ は頂点 $v$ の $(d-k)$ 代親になる. これは $O(N \log N)$ 時間で求められる.
  * $k \gt d$ ならば, $v$ を $v$ が属している根付き木の根に, $k \gets k-d$ に置き換えることにより, $v$ がサイクル上の頂点の場合に帰着できる.

## Contents

---

### Constructer

```Python
F=Functional_Graph(N, F=[])
```

* $V=\\{0,1,2 \dots, N-1\\}$ とし, $v \mapsto F[v]$ に対応する Functional Graph を生成する.
* **計算量** : $O(N \log N)$ Times.

---

### on_cycle

```Python
F.on_cycle(x)
```

* 頂点 $x$ がサイクル上の頂点かどうかを判定する.
* 制約
  * $0 \leq x \lt N$.
* **計算量** : $O(1)$ Times.

---

### calculate

```Python
F.calculate(x, k)
```

* $F^k(x)=(\underbrace{F \circ \dots \circ F}_{k~{\rm times}})(x)$ を求める.
* 制約
  * $0 \leq x \lt N$.
  * $0 \leq k$
* **計算量** : $O(\log N)$ Times.

### calculate_list

```Python
F.calculate_list(x, k)
```

* リスト $[F^k(0), F^k(1), \dots, F^k(N-1)]$ を求める.
* 制約
  * $0 \leq k$
* **計算量** : $O(\log N)$ Times.

### get_cycle

```Python
F.get_cycle()
```

* Functional Graph にあるサイクルを返す.
* リストは $[[u_{0,0}, \dots, u_{0,m_0-1}], \dots, [u_{k-1,0}, \dots, u_{k-1, m_{k-1}-1}]]$ の形であり, $i=0,2, \dots, k-1$ に対して, $u_{i,0}, \dots, u_{i,m_i-1}$ がこの順に有向サイクルを成す.

### get_inverse

```Python
F.get_inverse()
```

* 次の条件を満たすような各要素がリストである長さ $N$ のリスト $[G_0, \dots, G_{N-1}]$ を返す.

$$\forall v \in V;~v \in G_x \iff f(x)=v$$

要は, $G_x$ は $f(v)=x$ となるような $v$ 全体のリスト.
