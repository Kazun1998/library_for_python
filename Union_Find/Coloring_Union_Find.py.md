---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class Coloring_Union_Find():\n    __slots__=(\"n\", \"parents\", \"rank\"\
    , \"data\", \"merge\", \"__group_number\")\n\n    def __init__(self, N, merge,\
    \ unit):\n        \"\"\" 0,1,...,N-1 \u3092\u8981\u7D20\u3068\u3057\u3066\u521D\
    \u671F\u5316\u3059\u308B.\n\n        N: \u8981\u7D20\u6570\n        merge: \u5408\
    \u6210\u306E\u65B9\u6CD5\n        e: \u6700\u521D\u306E\u5024\n        \"\"\"\n\
    \        self.n=N\n        self.parents=[-1]*N\n        self.data=[unit]*N\n \
    \       self.rank=[0]*N\n        self.merge=merge\n        self.__group_number=N\n\
    \n    def find(self, x):\n        \"\"\" \u8981\u7D20 x \u306E\u5C5E\u3057\u3066\
    \u3044\u308B\u65CF\u3092\u8ABF\u3079\u308B.\n\n        x: \u8981\u7D20\n     \
    \   \"\"\"\n        V=[]\n        while self.parents[x]>=0:\n            V.append(x)\n\
    \            x=self.parents[x]\n\n        for v in V:\n            self.parents[v]=x\n\
    \        return x\n\n    def union(self, x, y):\n        \"\"\" \u8981\u7D20 x,y\
    \ \u3092\u540C\u4E00\u8996\u3057, \u305D\u308C\u305E\u308C\u304C\u6301\u3063\u3066\
    \u3044\u308B\u65CF\u306E\u8272\u3092\u7D71\u5408\u3059\u308B.\n\n        x,y:\
    \ \u8981\u7D20\n        \"\"\"\n        x=self.find(x)\n        y=self.find(y)\n\
    \n        if x==y:\n            return\n\n        self.__group_number-=1\n\n \
    \       self.data[x]=self.data[y]=self.merge(self.data[x], self.data[y])\n\n \
    \       if self.rank[x]<self.rank[y]:\n            x,y=y,x\n\n        self.parents[x]+=self.parents[y]\n\
    \        self.parents[y]=x\n\n        if self.rank[x]==self.rank[y]:\n       \
    \     self.rank[x]+=1\n\n    def size(self, x):\n        \"\"\" \u8981\u7D20 x\
    \ \u306E\u5C5E\u3057\u3066\u3044\u308B\u65CF\u306E\u8981\u7D20\u306E\u6570.\n\n\
    \        x: \u8981\u7D20\n        \"\"\"\n        return -self.parents[self.find(x)]\n\
    \n    def same(self, x, y):\n        \"\"\" \u8981\u7D20 x,y \u306F\u540C\u4E00\
    \u8996\u3055\u308C\u3066\u3044\u308B\u304B?\n\n        x,y: \u8981\u7D20\n   \
    \     \"\"\"\n        return self.find(x) == self.find(y)\n\n    def update(self,\
    \ x, color):\n        \"\"\" \u8981\u7D20 x \u306E\u5C5E\u3059\u308B\u65CF\u306E\
    \u8272\u3092 color \u306B\u5909\u66F4\u3059\u308B.\n\n        x: \u8981\u7D20\n\
    \        color: \u8272\n        \"\"\"\n        self.data[self.find(x)]=color\n\
    \n    def get(self, x):\n        \"\"\" \u8981\u7D20 x \u306E\u5C5E\u3059\u308B\
    \u5C5E\u306E\u8272\u3092\u6C42\u3081\u308B.\n\n        x: \u8981\u7D20\n     \
    \   \"\"\"\n        return self.data[self.find(x)]\n\n    def members(self, x):\n\
    \        \"\"\" \u8981\u7D20 x \u304C\u5C5E\u3057\u3066\u3044\u308B\u65CF\u306E\
    \u8981\u7D20.\n        \u203B\u65CF\u306E\u8981\u7D20\u306E\u500B\u6570\u304C\u6B32\
    \u3057\u3044\u3068\u304D\u306F size \u3092\u4F7F\u3046\u3053\u3068!!\n\n     \
    \   x: \u8981\u7D20\n        \"\"\"\n        root = self.find(x)\n        return\
    \ [i for i in range(self.n) if self.find(i) == root]\n\n    def roots(self):\n\
    \        \"\"\" \u65CF\u306E\u540D\u524D\u306E\u30EA\u30B9\u30C8\n        \"\"\
    \"\n        return [i for i,x in enumerate(self.parents) if x < 0]\n\n    def\
    \ group_count(self):\n        \"\"\" \u65CF\u306E\u500B\u6570\n        \"\"\"\n\
    \        return self.__group_number\n\n    def all_group_members(self):\n    \
    \    \"\"\" \u5168\u3066\u306E\u65CF\u306E\u51FA\u529B\n        \"\"\"\n     \
    \   X={r:[] for r in self.roots()}\n        for k in range(self.n):\n        \
    \    X[self.find(k)].append(k)\n        return X\n\n    def list(self):\n    \
    \    return [self.get(x) for x in range(self.n)]\n\n    def map(self):\n     \
    \   return {x:self.get(x) for x in self.roots()}\n\n    def __str__(self):\n \
    \       string=[]\n        for x,g in self.all_group_members().items():\n    \
    \        string.append(\" ({}) {}\".format(self.get(x), g))\n        return \"\
    ,\".join(string)\n\n    def __repr__(self):\n        return \"Coloring Union Find:\"\
    +str(self)\n\n    def __getitem__(self,index):\n        return self.data[self.find(index)]\n\
    \n    def __setitem__(self,index,value):\n        self.data[self.find(index)]=value\n"
  dependsOn: []
  isVerificationFile: false
  path: Union_Find/Coloring_Union_Find.py
  requiredBy: []
  timestamp: '2022-12-24 17:43:44+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Union_Find/Coloring_Union_Find.py
layout: document
title: "\u8272\u4ED8\u304D Union Find"
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
