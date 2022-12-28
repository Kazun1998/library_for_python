---
title: Strongly Connected Components (強連結成分分解)
documentation_of: //Strongly_Connected_Components.py
---

## Outline

有向グラフにおける強連結成分分解を行う.

## Theory

$D=(V,A)$ を有向グラフとする.

$V$ 上の関係 $\sim$ を次のように定義する.

* $u \sim v :\iff$ $u$ から $v$ への有向路, $v$ から $u$ への有向路が共に存在する.

この関係 $\sim$ は同値関係になる. この  $\sim$ に関する連結成分を **強連結成分** という.

そして, $A'$ を

$$A':=\left \{\overrightarrow{[u][v]}\middle| \overrightarrow{uv} \in A , [u] \neq [v] \right \}$$

と定義すると, $D'=(V/\sim, A')$ は DAG になる. よって, $D'$ には Topological Sort $\geq$ が存在する.

このアルゴリズムでは強連結成分をトポロジカルソートの順に求めることができる.
