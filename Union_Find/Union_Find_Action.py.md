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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.13.3/x64/lib/python3.13/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.13.3/x64/lib/python3.13/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from typing import TypeVar, Generic, Callable\n\nM = TypeVar('M')\nclass\
    \ Union_Find_Action(Generic[M]):\n    def __init__(self, N: int, op: Callable[[M,\
    \ M], M], unit: M):\n        # Union Find \u3067\u7528\u3044\u308B\u5909\u6570\
    \n        self.__groups = [[x] for x in range(N)]\n        self.__belong = [x\
    \ for x in range(N)]\n\n        # Monoid \u306B\u95A2\u3059\u308B\u5024\n    \
    \    self.__op = op\n        self.__unit = unit\n\n        # Monoid \u306E\u7A4D\
    \u306B\u95A2\u3059\u308B\u5909\u6570\n        self.__segments = [[[]] for _ in\
    \ range(N)]\n        self.__provisional = [unit for _ in range(N)]\n        self.__time_offset\
    \ = [0] * N\n\n    def find(self, x: int) -> int:\n        return self.__belong[x]\n\
    \n    def union(self, x: int, y: int) -> bool:\n        x = self.find(x)\n   \
    \     y = self.find(y)\n        if x == y:\n            return False\n\n     \
    \   if self.size(x) < self.size(y):\n            x, y = y, x\n\n        self.__groups[x].extend(self.__groups[y])\n\
    \        memo = [self.get(z) for z in self.__groups[y]]\n        for z, b in zip(self.__groups[y],\
    \ memo):\n            self.__belong[z] = x\n            self.update(z, b)\n\n\
    \        self.__groups[y].clear()\n\n        return True\n\n    def same(self,\
    \ x: int, y: int) -> bool:\n        return self.find(x) == self.find(y)\n\n  \
    \  def size(self, x: int) -> int:\n        return len(self.__groups[self.find(x)])\n\
    \n    def action(self, x: int, a: M):\n        \"\"\" x \u304C\u5C5E\u3059\u308B\
    \u9023\u7D50\u6210\u5206\u5168\u3066\u306B a \u3092\u4F5C\u7528\u3055\u305B\u308B\
    .\n\n        Args:\n            x (int): \u9802\u70B9\u756A\u53F7\n          \
    \  a (M): \u4F5C\u7528\n        \"\"\"\n\n        x = self.find(x)\n        segment\
    \ = self.__segments[x]\n        op = self.__op\n\n        i = 0\n        segment[0].append(a)\n\
    \        while True:\n            if len(segment[i]) % 2 == 1:\n             \
    \   break\n\n            if len(segment[i]) == 2:\n                segment.append([])\n\
    \n            i += 1\n            segment[i].append(op(segment[i - 1][-1], segment[i\
    \ - 1][-2]))\n\n    def update(self, x: int, a: M):\n        \"\"\" \u9802\u70B9\
    \ x \u306E\u30E9\u30D9\u30EB\u3092 a \u306B\u66F4\u65B0\u3059\u308B.\n\n     \
    \   Args:\n            x (int): \u9802\u70B9\u756A\u53F7\n            a (M): \u5909\
    \u66F4\u5F8C\u306E\u30E9\u30D9\u30EB\n        \"\"\"\n        self.__time_offset[x]\
    \ = len(self.__segments[self.find(x)][0])\n        self.__provisional[x] = a\n\
    \n    def get(self, x: int) -> M:\n        root = self.find(x)\n        lazy =\
    \ self.__product(self.__segments[root], self.__time_offset[x])\n        return\
    \ self.__op(lazy, self.__provisional[x])\n\n    def __getitem__(self, x: int):\n\
    \        return self.get(x)\n\n    def __product(self, segment: list[list[M]],\
    \ t: int):\n        vl = self.__unit\n        vr = self.__unit\n\n        l =\
    \ t; r = len(segment[0])\n        op = self.__op\n        for seg in segment:\n\
    \            if not l < r:\n                break\n\n            if l & 1:\n \
    \               vl = op(seg[l], vl)\n                l += 1\n\n            if\
    \ r & 1:\n                r -= 1\n                vr = op(vr, seg[r])\n\n    \
    \        l >>= 1\n            r >>= 1\n\n        return op(vr, vl)\n"
  dependsOn: []
  isVerificationFile: false
  path: Union_Find/Union_Find_Action.py
  requiredBy: []
  timestamp: '2025-03-29 14:18:42+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Union_Find/Union_Find_Action.py
layout: document
title: "Monoid \u4F5C\u7528\u4ED8\u304D Union Find"
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
