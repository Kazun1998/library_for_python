---
title: Flow
documentation_of: //Flow/Flow.py
---

## Outline

有向グラフ $D=(V,A)$ において, 各孤 $a \in A$ には容量 $u(a)$ が定められている.

2頂点 $s, t \in V$ に対して, $s$ から $t$ へ流せる水の最大量を求める.

厳密には, 以下の問題を解く.

- Maximize : $F$
- Subject to :
  - $\displaystyle \sum_{\substack{a \in A \\\\ s=\operatorname{sink}(a)}} f_{a}-\sum_{\substack{a \in A \\\\ s=\operatorname{target}(a)}} f_{a}=F$
  - $\displaystyle \sum_{\substack{a \in A \\\\ t=\operatorname{sink}(a)}} f_{a}-\sum_{\substack{a \in A \\\\ t=\operatorname{target}(a)}} f_{a}=-F$
  - $\displaystyle \sum_{\substack{a \in A \\\\ v=\operatorname{sink}(a)}} f_{a}-\sum_{\substack{a \in A \\\\ v=\operatorname{target}(a)}} f_{a}=0 \quad (\forall v \in V \setminus \\{s,t\\})$
  - $0 \leq f_{a} \leq u(a) \quad (\forall a \in A)$

## Contents

---

### Constructer

```Python
F=Flow(N=0)
```

- $N$ 頂点からなる空グラフを用意する.

---

### add_vertex

```Pyhon
F.add_vertex()
```

- $1$ 頂点を追加する. 返り値としてその追加した頂点の番号を返す.

---

### add_vertices

```Pyhon
F.add_vertices(k)
```

- $k$ 頂点を追加する. 返り値としてその追加した $k$ 個の頂点の番号のリストを返す.

---

### add_arc

```Pyhon
F.add_arc(v, w, cap)
```

- 容量 ${\rm cap}$ の孤 $\overrightarrow{vw}$ を追加する. 返り値として, 追加した辺の番号を返す.

---

### get_arc

```Pyhon
F.get_arc(i, mode=0)
```

- $i$ 番目の辺に関する情報を得る. ${\rm mode}=1$ とすると, $i$ 番目の辺だけでなく, $i$ 番目の辺の逆辺に関する情報も得る.

---

### get_all_arcs

```Pyhon
F.get_all_arcs()
```

- 全ての辺に関する情報を得る (逆辺は得られない).

---

### vertex_count

```Pyhon
F.vertetx_count()
```

- 有向グラフの位数 (頂点数) を得る.

---

### arc_count

```Pyhon
F.arc_count()
```

- 有向グラフのサイズ (辺の数) を得る.

---

### change_arc

```Pyhon
F.change_arc(i, new_cap, new_flow)
```

- $i$ 番目の辺を容量 `new_cap` で現在 `new_flow` である状態に変更する.

---

### add_edge

```Pyhon
F.add_edge(v, w, cap)
```

- 容量が `cap` である **無向辺** $vw$ を追加する.

---

### max_flow

```Pyhon
F.max_flow(source, target, flow_limit)
```

- $s=$ `source` , $t=$ `target` である場合の最大流問題を解く. なお,答えの最大値は `flow_limit` とする.

### get_flow

```Pyhon
F.get_flow(mode=0)
```

- `mode` $=0$ のとき : 長さがサイズのリストが与えられる. 第 $i$ 要素には $i$ 番目の (有向) 辺にながれている水量が格納されている.
- `mode` $=1$ のとき : 位数を $N$ とする. 長さ $N$ のリストが返され, 第 $v$ 要素には $v$ を始点とする各有向辺について $($`辺の番号` $,$  `終点` $,$ `辺に流れる水量`$)$ の情報を持つタプルのリストである.
