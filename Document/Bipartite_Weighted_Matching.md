---
title: Bipartite Weighted Matching
documentation_of: //Min_Cost_Flow/Bipartite_Weighted_Matching.py
---

## Outline

二部グラフ $G=(X,Y,E)$ における最大重みマッチング問題 (及びそれらの派生問題) を解く.

## Theory

二部グラフ $G=(X,Y,E)$ における最大重みマッチング問題は次のようにして多項式時間で解くことが出来る.

* $G$ に対して, 次のような有向グラフを $H=(V,A)$ 作成する.
  * $V=X \coprod Y \coprod \\{s,t\\}$
  * $A=\\{\overrightarrow{xy} \mid xy \in E\\} \coprod \\{\overrightarrow{sx} \mid x \in X\\} \coprod \\{\overrightarrow{yt} \mid x \in X\\}$
  * 各孤の容量は全て $1$ とし,　単位あたりの費用 $c(a)$ は次のようにする.
    * $xy \in E$ のとき, $c(\overrightarrow{xy})$ は辺 $xy$ の重みとする.
    * $c(\overrightarrow{sx})=c(\overrightarrow{yt})=0$
