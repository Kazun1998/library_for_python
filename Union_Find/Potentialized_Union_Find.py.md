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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.5/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.5/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class Potentilized_Union_Find():\n    def __init__(self, N, op, zero, neg):\n\
    \        \"\"\" 0,1,...,N-1 \u3092\u8981\u7D20\u3068\u3057\u3066\u521D\u671F\u5316\
    \u3059\u308B.\n\n        N: \u8981\u7D20\u6570\n        \"\"\"\n        self.n=N\n\
    \        self.parents=[-1]*N\n        self.rank=[0]*N\n        self.edges=[0]*N\n\
    \        self.pot=[0]*N\n        self.valid=[True]*N\n        self.__group_number=N\n\
    \n        self.op=op\n        self.diff=lambda u,v:self.op(u, self.neg(v)) # diff(u,v)=U(u)-U(v)\n\
    \        self.zero=zero\n        self.neg=neg\n\n\n    def find(self, x):\n  \
    \      \"\"\" \u8981\u7D20 x \u306E\u5C5E\u3057\u3066\u3044\u308B\u65CF\u3092\u8ABF\
    \u3079\u308B.\n\n        x: \u8981\u7D20\n        \"\"\"\n\n\n        if self.parents[x]<0:\n\
    \            return x\n\n        par=self.parents; pot=self.pot; op=self.op\n\n\
    \        r=x\n        data=[]\n        while par[r]>=0:\n            data.append(r)\n\
    \            r=par[r]\n\n        for x in data[::-1]:\n            pot[x]=self.op(pot[x],\
    \ pot[par[x]])\n            par[x]=r\n\n        return r\n\n    def union(self,\
    \ x, y, u):\n        \"\"\" \u8981\u7D20 x,y \u3092\u540C\u4E00\u8996\u3057, U(y)-U(x)=u\
    \ \u3068\u3044\u3046\u60C5\u5831\u3092\u52A0\u3048\u308B.\n\n        x,y: \u8981\
    \u7D20\n        \"\"\"\n\n        a=self.find(x); b=self.find(y)\n        u=self.op(u,\
    \ self.diff(self.pot[x],self.pot[y]))\n        x=a; y=b\n\n        if x==y:\n\
    \            self.valid[x]&=self.diff(self.pot[y],self.pot[x])==u\n          \
    \  self.edges[x]+=1\n            return\n\n        if self.rank[x]<self.rank[y]:\n\
    \            x,y=y,x\n            u=self.neg(u)\n        elif self.rank[x]==self.rank[y]:\n\
    \            self.rank[x]+=1\n\n        self.parents[x]+=self.parents[y]\n   \
    \     self.parents[y]=x\n\n        self.edges[x]+=self.edges[y]+1\n        self.edges[y]=0\n\
    \n        self.valid[x]&=self.valid[y]\n\n        self.pot[y]=u\n\n        self.__group_number-=1\n\
    \n        return\n\n    def size(self, x):\n        \"\"\" \u8981\u7D20 x \u306E\
    \u5C5E\u3057\u3066\u3044\u308B\u65CF\u306E\u8981\u7D20\u306E\u6570.\n\n      \
    \  x: \u8981\u7D20\n        \"\"\"\n        return -self.parents[self.find(x)]\n\
    \n    def potential_energy(self, x, y):\n        \"\"\" x \u3092\u57FA\u6E96\u306B\
    \u3057\u305F y \u306E\u30DD\u30C6\u30F3\u30B7\u30E3\u30EB\u30A8\u30CD\u30EB\u30AE\
    \u30FC\"\"\"\n\n        if self.same(x,y) and self.is_valid(x):\n            return\
    \ self.diff(self.pot[y], self.pot[x])\n        else:\n            return None\n\
    \n    def same(self, x, y):\n        \"\"\" \u8981\u7D20 x,y \u306F\u540C\u4E00\
    \u8996\u3055\u308C\u3066\u3044\u308B\u304B?\n\n        x,y: \u8981\u7D20\n   \
    \     \"\"\"\n        return self.find(x) == self.find(y)\n\n    def members(self,\
    \ x):\n        \"\"\" \u8981\u7D20 x \u304C\u5C5E\u3057\u3066\u3044\u308B\u65CF\
    \u306E\u8981\u7D20.\n        \u203B\u65CF\u306E\u8981\u7D20\u306E\u500B\u6570\u304C\
    \u6B32\u3057\u3044\u3068\u304D\u306F size \u3092\u4F7F\u3046\u3053\u3068!!\n\n\
    \        x: \u8981\u7D20\n        \"\"\"\n        root = self.find(x)\n      \
    \  return [i for i in range(self.n) if self.find(i) == root]\n\n    def edge_count(self,\
    \ x):\n        \"\"\" \u8981\u7D20 x \u304C\u5C5E\u3059\u308B\u65CF\u306E\u8FBA\
    \u306E\u672C\u6570\u3092\u6C42\u3081\u308B.\n\n        x: \u8981\u7D20\n     \
    \   \"\"\"\n        return self.edges[self.find(x)]\n\n    def is_valid(self,\
    \ x):\n        \"\"\" x \u304C\u5C5E\u3057\u3066\u3044\u308B\u65CF\u306E\u30DD\
    \u30C6\u30F3\u30B7\u30E3\u30EB\u304C\u59A5\u5F53\u304B\u3069\u3046\u304B\u3092\
    \u5224\u5B9A\u3059\u308B. \"\"\"\n\n        return self.valid[self.find(x)]\n\n\
    \    def is_well_defined(self):\n        \"\"\" \u3053\u306E\u7CFB\u5168\u4F53\
    \u306E\u30DD\u30C6\u30F3\u30B7\u30E3\u30EB\u304C\u59A5\u5F53\u304B\u3069\u3046\
    \u304B\u3092\u5224\u5B9A\u3059\u308B. \"\"\"\n\n        return all(self.is_valid(x)\
    \ for x in range(self.n))\n\n    def is_tree(self, x):\n        \"\"\" \u8981\u7D20\
    \ x \u304C\u5C5E\u3059\u308B\u65CF\u304C\u68EE\u304B\u3069\u3046\u304B\u3092\u5224\
    \u5B9A\u3059\u308B.\n\n        x: \u8981\u7D20\n        \"\"\"\n        return\
    \ self.size(x)==self.edges[self.find(x)]+1\n\n    def tree_count(self):\n    \
    \    \"\"\" \u68EE\u306B\u306A\u3063\u3066\u3044\u308B\u5C5E\u306E\u500B\u6570\
    \u3092\u6C42\u3081\u308B.\n        \"\"\"\n\n        return sum(self.is_tree(g)\
    \ for g in self.representative())\n\n    def representative(self):\n        \"\
    \"\" \u4EE3\u8868\u5143\u306E\u540D\u524D\u306E\u30EA\u30B9\u30C8\n        \"\"\
    \"\n        return [i for i, x in enumerate(self.parents) if x < 0]\n\n    def\
    \ group_count(self):\n        \"\"\" \u65CF\u306E\u500B\u6570\n        \"\"\"\n\
    \        return self.__group_number\n\n    def all_group_members(self):\n    \
    \    \"\"\" \u5168\u3066\u306E\u65CF\u306E\u51FA\u529B\n        \"\"\"\n     \
    \   X={r:[] for r in self.roots()}\n        for k in range(self.n):\n        \
    \    X[self.find(k)].append(k)\n        return X\n\n    def refresh(self):\n \
    \       for i in range(self.n):\n            _=self.find(i)\n\n    def __str__(self):\n\
    \        return '\\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())\n\
    \n    __repr__=__str__\n"
  dependsOn: []
  isVerificationFile: false
  path: Union_Find/Potentialized_Union_Find.py
  requiredBy: []
  timestamp: '2023-03-20 03:47:37+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Union_Find/Potentialized_Union_Find.py
layout: document
title: "\u30DD\u30C6\u30F3\u30B7\u30E3\u30EB\u4ED8\u304D Union Find"
---

## Outline

Union Find にポテンシャルの概念を付け加え, ポテンシャルの差を取得する.

## Theory

$G=(G,+,0)$ を可換群とする. $V:=\\{0,1,\dots, N-1\\}$ として, 写像 $U: V \to G$ には $M$ 個の関係式が以下の形で与えられている.

$$U(y_j)-U(x_j)=u_j \quad (x_j, y_j \in V, u_j \in G \quad (1 \leq j \leq M))$$

## Contents

---

### Constructer

```Python
U=Union_Find(N)
```

- $N$ 頂点の空グラフを生成する.
- **計算量** : $O(N)$ Time.

---

### find

```Pyhon
U.find(x)
```

- $x$ が属する連結成分の代表元を返す.
- **制約**
  - $0 \leq x \lt N$
- **計算量** : Amortized $O(\alpha(N))$ Time.

---

### union

```Python
U.union(x,y)
```

- 無向辺 $xy$ を追加する (この追加によって単純グラフにならなくてもよい).
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
