---
title: Graph
documentation_of: //Graph//Graph//Graph.py
---

## Outline

多重辺がない無向グラフ $G=(V,E)$ に対する様々なアルゴリズム

## Theory

無向グラフ $G=(V,E)$ に対して, $V$ の濃度を $G$ の位数 (Order), $E$ の濃度を $G$ のサイズ (Size) という.

## Contents

---

### Constructer

```Python
G=Graph(N=0)
```

* 位数 $N$ の空グラフ (edgeless graph) を生成する.

### add_vertex

```Python
G.add_vertex()
```

* $G$ に 1 頂点を追加する. 追加された頂点の番号を返り値とする.

### add_vertices

```Python
G.add_vertices(k)
```

* $G$ に $k$ 頂点を追加する. 追加された $k$ 個の頂点の番号のリストを返り値とする.

### add_edge

``` Python
G.add_edge(u,v)
```

* 無向辺 $uv$ を存在しないならば追加する.
* 返り値は, 元々辺 $uv$ が存在しないならば, 辺の番号 (0-indexed) を, 存在するならば $-1$ とする.

### remove_edge

``` Python
G.remove_edge(u,v)
```

* 辺 $uv$ が削除するならば, 辺 $uv$ を削除する.
