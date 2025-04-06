---
title: Monoid 作用付き Union Find
documentation_of: //Union_Find/Union_Find_Action.py
---

## Outline

各頂点に Monoid $M$ の元がラベルとして付いている無向 Graph 上 $H = (V, E)$ に対して, 以下の処理を高速に行う.

* `union(x, y)`: 頂点 $x$ と頂点 $y$ を結ぶ辺を追加する.
* `find(x)`: 頂点 $x$ が属する連結成分の代表元を求める.
* `same(x, y)`: 頂点 $x$ と頂点 $y$ は連結か?
* `action(x, a)`: 頂点 $x$ が属する連結成分上の頂点全てに対して, $a \in M$ を作用させる。.
* `update(x, a)`: 頂点 $x$ を $a \in M$ に更新する.
* `get(x)`: 頂点 $x$ のラベルを求める.

## Theory

$H = (V,E)$ を無向 Graph とし, $M$ を Monoid とする.

## Contents

$M$ における演算の計算量を $O(f)$ Times とする.

---

### Constructer

```Python
U = Union_Find_Action(N, op, unit)
```

* $N$ 頂点の $M$ の元がラベルとして付いている無向 Graph を生成する.
* **制約**
  * $\operatorname{op}: M \times M \to M$: Monoid $M$ の演算
  * $\mathrm{unit} \in M$: Monoid $M$ の単位元
* **計算量** : $O(N)$ Time.

---

### find

```Pyhon
U.find(x)
```

* 頂点 $x$ が属する連結成分の代表元を返す.
* **制約**
  * $0 \leq x \lt N$
* **計算量** : $O(1)$ Time.

---

### union

```Python
U.union(x, y)
```

* 無向辺 $xy$ を追加する.
* **制約**
  * $0 \leq x \lt N$
  * $0 \leq y \lt N$
* **計算量** : Amortized $O(f (\log N)^2)$ Time

---

### size

```Python
U.size(x)
```

* $x$ が属する連結成分の頂点数を求める.
* **制約**
  * $0 \leq x \lt N$
* **計算量** : $O(1)$ Time.

---

### same

```Python
U.same(x, y)
```

* 2頂点 $x,y$ が連結かどうかを判定する.
* **制約**
  * $0 \leq x \lt N$
  * $0 \leq y \lt N$
* **計算量** : $O(1)$ Time.

---

### update

```Python
U.update(x, a)
```

* 頂点 $x$ のラベルを $a$ に変更する.
* **制約**
  * $0 \leq x \lt N$
  * $a \in M$
* **計算量** : $O(1)$ Time.

---

### get

```Python
U.get(x)
```

* 頂点 $x$ におけるラベルを求める.
* **制約**
  * $0 \leq x \lt N$
* **計算量** : $O(f \log N)$ Time.
