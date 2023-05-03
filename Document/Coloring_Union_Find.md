---
title: 色付き Union Find
documentation_of: //Union_Find/Coloring_Union_Find.py
---

## Outline

Union Find の機能に加え, 各連結成分に色という情報を持たせ, マージによって連結成分がまとめられる際, その連結成分の色は元の2つの連結成分の色から決定される.

## Theory

$G=(V,E)$ を無向グラフとし, $X$ を色の集合とする. また, 色の基底状態として, ${\rm unit} \in X$ とする.

## Contents

---

### Constructer

```Python
U=Coloring_Union_Find(N, merge, unit)
```

- $N$ 頂点色付き Union Find を生成する. 色のマージの方法は $\operatorname{merge}$ で, 基底状態は $\mathrm{unit}$ である.
- **制約**
  - $\operatorname{merge}:X \times X \to X$
  - $\mathrm{ground} \in X$
- **計算量** : $O(N)$ Time.

---

### find

```Pyhon
U.find(x)
```

- $x$ が属する連結成分の代表元を返す (色は得られない).
- **制約**
  - $0 \leq x \lt N$
- **計算量** : Amortized $O(\alpha(N))$ Time.

---

### union

```Python
U.union(x,y)
```

- 無向辺 $xy$ を追加する. この辺によって連結成分がまとめ統合される場合, 新たな連結成分の色として, $\operatorname{merge}(\operatorname{color}(x), \operatorname{color}(y))$ が設定される.
- なお, $x,y$ が同じ連結成分にある場合, 色の変更は起こらない.
- **制約**
  - $0 \leq x \lt N$
  - $0 \leq y \lt N$
- **計算量** : Amortized $O(\alpha(N))$ Time

---

### size

```Python
U.size(x)
```

- $x$ が属する連結成分の頂点数を求める.
- **制約**
  - $0 \leq x \lt N$
- **計算量** : Amortized $O(\alpha(N))$ Time.

---

### same

```Python
U.same(x,y)
```

- 2頂点 $x,y$ が連結かどうかを判定する.
- **制約**
  - $0 \leq x \lt N$
- **計算量** : Amortized $O(\alpha(N))$ Time.

---

### update

```Python
U.update(x, color)
```

- 頂点 $x$ が属する連結成分の色を $\mathrm{color}$ に変更する.
- **制約**
  - $0 \leq x \lt N$
  - $\operatorname{color} \in X$
- **計算量** : Amortized $O(\alpha(N))$ Time.

---

### get

```Python
U.get(x)
```

- 頂点 $x$ が属する連結成分の色を求める.
- **制約**
  - $0 \leq x \lt N$
- **計算量** : Amortized $O(\alpha(N))$ Time.

---

### members

```Python
U.members(x)
```

- 頂点 $x$ が属する連結成分のリストを求める.
- **制約**
  - $0 \leq x \lt N$
- **計算量** : $O(N)$ Time.

---

### edge_count

```Python
U.edge_count(x)
```

- 頂点 $x$ が属する連結成分にある辺の数を求める.
- **制約**
  - $0 \leq x \lt N$
- **計算量** : Amortized $O(\alpha(N))$ Time.

---

### is_tree

```Python
U.is_tree()
```

- 頂点 $x$ が属する連結成分が木かどうかを判定する.
- **制約**
  - $0 \leq x \lt N$
- **計算量** : Amortized $O(\alpha(N))$ Time.

---

### tree_count

```Python
U.tree_count()
```

- 木になっている連結成分の数を求める.
- **計算量** : $O(N)$ Time.

---

### representive

```Python
U.representative()
```

- 代表元のリストを返す.
- **計算量** : Amortized $O(N)$ Time.

---

### group_count

```Python
U.group_count()
```

- 連結成分の数を求める.
- **計算量** : $O(1)$ Time.

---

### all_group_members

```Python
U.all_group_members()
```

- 連結成分ごとに分割した dict を返す.
- **計算量** : $O(N)$ Time.

---

### group_list

```Python
U.group_list(x,y)
```

- 各頂点が属している連結成分の代表元を返す.
- **計算量** : $O(N)$ Time.

---

### refresh

```Python
U.refresh()
```

- 現時点での情報を整理し, データ構造を単純化する.
- **計算量** : $O(N)$ Time.

---

### getitem

```Python
U[x]
```

- `U.find(x)` と同等.
- **制約**
  - $0 \leq x \lt N$
- **計算量** : Amortized $O(\alpha(N))$ Time.

---

### setitem

```Python
U[x]=y
```

- `U.union(x,y)` と同等
- **制約**
  - $0 \leq x \lt N$
- **計算量** : Amortized $O(\alpha(N))$ Time.
