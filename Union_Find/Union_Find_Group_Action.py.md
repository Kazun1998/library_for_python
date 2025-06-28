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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.13.5/x64/lib/python3.13/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.13.5/x64/lib/python3.13/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from typing import TypeVar, Generic, Callable\n\nG = TypeVar('G')\nclass\
    \ Union_Find_Group_Action(Generic[G]):\n    def __init__(self, N: int, op: Callable[[G,\
    \ G], G], unit: G, inv: Callable[[G], G]):\n        # Union Find \u3067\u7528\u3044\
    \u308B\u5909\u6570\n        self.__groups = [[x] for x in range(N)]\n        self.__belong\
    \ = [x for x in range(N)]\n\n        # Group \u306B\u95A2\u3059\u308B\u5024\n\
    \        self.__op = op\n        self.__inv = inv\n\n        # Group \u306E\u7A4D\
    \u306B\u95A2\u3059\u308B\u5909\u6570\n        self.__lazy = [unit for _ in range(N)]\n\
    \        self.__provisional = [unit for _ in range(N)]\n\n    def find(self, x:\
    \ int) -> int:\n        \"\"\" \u9802\u70B9 x \u304C\u5C5E\u3059\u308B\u9023\u7D50\
    \u6210\u5206\u306E\u4EE3\u8868\u5143\u3092\u6C42\u3081\u308B.\n\n        Args:\n\
    \            x (int): \u9802\u70B9\u756A\u53F7\n\n        Returns:\n         \
    \   int: \u9802\u70B9 x \u304C\u5C5E\u3059\u308B\u9023\u7D50\u6210\u5206\u306E\
    \u4EE3\u8868\u5143\n        \"\"\"\n        return self.__belong[x]\n\n    def\
    \ union(self, x: int, y: int) -> bool:\n        \"\"\" \u9802\u70B9 x \u3068\u9802\
    \u70B9 y \u3092\u7D50\u3076\u8FBA\u3092\u8FFD\u52A0\u3059\u308B.\n\n        Args:\n\
    \            x (int): \u9802\u70B9\u756A\u53F7\n            y (int): \u9802\u70B9\
    \u756A\u53F7\n\n        Returns:\n            bool: \u5143\u3005\u9802\u70B9 x\
    \ \u3068\u9802\u70B9 y \u304C\u975E\u9023\u7D50\u306A\u3089\u3070 True, \u9023\
    \u7D50\u306A\u3089\u3070 False\n        \"\"\"\n        x = self.find(x)\n   \
    \     y = self.find(y)\n        if x == y:\n            return False\n\n     \
    \   if self.size(x) < self.size(y):\n            x, y = y, x\n\n        self.__groups[x].extend(self.__groups[y])\n\
    \        memo = [self.get(z) for z in self.__groups[y]]\n        for z, b in zip(self.__groups[y],\
    \ memo):\n            self.__belong[z] = x\n            self.update(z, b)\n\n\
    \        self.__groups[y].clear()\n\n        return True\n\n    def same(self,\
    \ x: int, y: int) -> bool:\n        return self.find(x) == self.find(y)\n\n  \
    \  def size(self, x: int) -> int:\n        return len(self.__groups[self.find(x)])\n\
    \n    def action(self, x: int, a: G):\n        \"\"\" x \u304C\u5C5E\u3059\u308B\
    \u9023\u7D50\u6210\u5206\u5168\u3066\u306B a \u3092\u4F5C\u7528\u3055\u305B\u308B\
    .\n\n        Args:\n            x (int): \u9802\u70B9\u756A\u53F7\n          \
    \  a (G): \u4F5C\u7528\n        \"\"\"\n\n        x = self.find(x)\n        self.__lazy[x]\
    \ = self.__op(a, self.__lazy[x])\n\n    def update(self, x: int, a: G):\n    \
    \    \"\"\" \u9802\u70B9 x \u306E\u30E9\u30D9\u30EB\u3092 a \u306B\u66F4\u65B0\
    \u3059\u308B.\n\n        Args:\n            x (int): \u9802\u70B9\u756A\u53F7\n\
    \            a (G): \u5909\u66F4\u5F8C\u306E\u30E9\u30D9\u30EB\n        \"\"\"\
    \n\n        self.__provisional[x] = self.__op(self.__inv(self.__lazy[self.find(x)]),\
    \ a)\n\n    def get(self, x: int) -> G:\n        \"\"\" \u9802\u70B9 x \u306E\u30E9\
    \u30D9\u30EB\u3092\u53D6\u5F97\u3059\u308B.\n\n        Args:\n            x (int):\
    \ \u9802\u70B9\u756A\u53F7\n\n        Returns:\n            G: \u9802\u70B9 x\
    \ \u306E\u30E9\u30D9\u30EB\n        \"\"\"\n\n        return self.__op(self.__lazy[self.find(x)],\
    \ self.__provisional[x])\n\n    def __getitem__(self, x: int) -> G:\n        return\
    \ self.get(x)\n\n    def __len__(self) -> int:\n        return len(self.__belong)\n\
    \n    def __iter__(self):\n        yield from [self.get(x) for x in range(len(self))]\n"
  dependsOn: []
  isVerificationFile: false
  path: Union_Find/Union_Find_Group_Action.py
  requiredBy: []
  timestamp: '2025-03-29 15:18:46+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Union_Find/Union_Find_Group_Action.py
layout: document
title: "\u7FA4\u4F5C\u7528\u4ED8\u304D Union Find"
---

## Outline

各頂点に群 $G$ の元がラベルとして付いている無向 Graph 上 $H = (V, E)$ に対して, 以下の処理を高速に行う.

* `union(x, y)`: 頂点 $x$ と頂点 $y$ を結ぶ辺を追加する.
* `find(x)`: 頂点 $x$ が属する連結成分の代表元を求める.
* `same(x, y)`: 頂点 $x$ と頂点 $y$ は連結か?
* `action(x, a)`: 頂点 $x$ が属する連結成分上の頂点全てに対して, $a \in G$ を作用させる。.
* `update(x, a)`: 頂点 $x$ を $a \in G$ に更新する.
* `get(x)`: 頂点 $x$ のラベルを求める.

## Theory

$H = (V,E)$ を無向 Graph とし, $G$ を群とする.

## Contents

$G$ における演算, 逆元計算の計算量を $O(f)$ Times とする.

---

### Constructer

```Python
U = Union_Find_Action(N, op, unit, inv)
```

* $N$ 頂点の $G$ の元がラベルとして付いている無向 Graph を生成する.
* **制約**
  * $\operatorname{op}: G \times G \to G; (x, y) \mapsto xy$: 群 $G$ の演算
  * $\mathrm{unit} \in G$: 群 $G$ の単位元
  * $\mathrm{inv}: G \to G; x \mapsto x^{-1}$: 群 $G$ の逆元関数
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
* **計算量** : $O(f \log N)$ Time

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
  * $a \in G$
* **計算量** : $O(f)$ Time.

---

### get

```Python
U.get(x)
```

* 頂点 $x$ におけるラベルを求める.
* **制約**
  * $0 \leq x \lt N$
* **計算量** : $O(f)$ Time.
