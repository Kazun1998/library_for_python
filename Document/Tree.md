---
title: Tree
documentation_of: //Tree/Tree.py
---

## Outline

木 $T=(V,E)$ における様々な計算をまとめたデータ構造

## Contents

---

### Constructer

```Python
T=Tree(N, index=0)
```

- $N$ 頂点の木グラフの準備をする.
- 頂点の番号は ${\rm index}, {\rm index}+1, \cdots, {\rm index}+(N-1)$ である.
- **計算量** : $O(N)$ Time.

---

### is_mutable

```Pyhon
T.is_mutable()
```

- 木が変更可能な状態かどうかを返す.

---

### root

```Python
T.root_set(root)
```

- 根を ${\rm root}$ に設定する.
- **制約**
  - ${\rm index} \leq {\rm root} \lt {\rm index}+N$

---

### parent_set

```Python
T.parent_set(x, y)
```

- 頂点 $x$ の親を頂点 $y$ に設定する.
- **制約**
  - ${\rm index} \leq x \lt {\rm index}+N$
  - ${\rm index} \leq y \lt {\rm index}+N$

---

### child_set

```Python
T.child_set(x, y)
```

- 頂点 $x$ の子の一つに頂点 $y$ に設定する.
- **制約**
  - ${\rm index} \leq x \lt {\rm index}+N$
  - ${\rm index} \leq y \lt {\rm index}+N$

---

### seal

```Python
T.seal()
```

- 木の情報を確定させる. これ以降木の変更は不可能.

---

### depth_search

```Python
T.depth_search(mode=True)
```

- 各頂点の深さを求める. `mode=True` ならば, 各頂点の深さのリストを返す.
- **制約**
  - ${\rm mode}$ は `True` または `False`
- **計算量** : $O(N)$ Time.

---

### vertex_depth

```Python
T.vertex_depth(x)
```

- 頂点 $x$ の深さを求める.
- **制約**
  - ${\rm index} \leq x \lt {\rm index}+N$

---

### upper

```Python
T.upper(x, k, over)
```

- 頂点 $x$ から親に移動することを $k$ 回行った後の頂点を求める. ただし, $\operatorname{depth}(x) <k$ のとき, `over=True` ならば根を返り値とし, `over=False` ならば, `ValueError` を吐く.
- **制約**
  - ${\rm index} \leq x \lt {\rm index}+N$
  - $k \geq 0$
- **計算量** : $O(\log N)$ Time.

---

### lowest_common_ancestor_greedy

```Python
T.lowest_common_ancestor_greedy(x, y)
```

- 2頂点 $x,y$ の最小共通先祖を愚直な方法で求める.
- **制約**
  - ${\rm index} \leq x \lt {\rm index}+N$
  - ${\rm index} \leq y \lt {\rm index}+N$
- **計算量** : $O(N)$ Time.

---

### lowest_common_ancestor

```Python
T.lowest_common_ancestor(x, y)
```

- 2頂点 $x,y$ の最小共通先祖を高速な方法で求める.
- **制約**
  - ${\rm index} \leq x \lt {\rm index}+N$
  - ${\rm index} \leq y \lt {\rm index}+N$
- **計算量** : 前計算: $O(N \log N)$ Time, 1 クエリ当たり $O(1)$ Time/Query.

---

### degree

```Python
T.degree(v)
```

- 頂点 $v$ の (グラフ理論における) 次数 を求める.
- **制約**
  - ${\rm index} \leq v \lt {\rm index}+N$

---

### diameter

```Python
T.diameter()
```

- 木の直径を求める.
- **計算量** : $O(N)$ Time.

---

### Path

```Python
T.path(u, v, falser=False)
```

- 木 $u,v$ -Path を求める.
- **制約**
  - ${\rm index} \leq u \lt {\rm index}+N$
  - ${\rm index} \leq v \lt {\rm index}+N$
- **計算量** :
  - ${\rm faster}=$ `False` のとき, $O(N)$ Time.
  - ${\rm faster}=$ `True` のとき, 1回でも `lowest_common_ansector` を使っていれば前計算がかからずに $O(N)$ Time. 使っていなければ初回のみ $O(N \log N)$ Time で, 2回目以降は $O(N)$ Time.

---
(作成途中)
