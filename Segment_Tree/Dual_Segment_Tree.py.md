---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test_verify/yosupo_library_checker/Data_Structure/Dual_Segment_Tree.test.py
    title: test_verify/yosupo_library_checker/Data_Structure/Dual_Segment_Tree.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.13.5/x64/lib/python3.13/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.13.5/x64/lib/python3.13/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from typing import TypeVar, Generic, Callable\n\nF = TypeVar('F')\nclass\
    \ Dual_Segment_Tree(Generic[F]):\n    def __init__(self, A: list[F], comp: Callable[[F,\
    \ F], F], id: F):\n        \"\"\" comp \u3092\u6F14\u7B97\u3068\u3059\u308B\u30EA\
    \u30B9\u30C8 L \u306E Dual Segment Tree \u3092\u4F5C\u6210\n\n        comp : \u4F5C\
    \u7528\u7D20\n        id : \u5358\u4F4D\u5143\n\n        [\u6CE8\u8A18]\n    \
    \    \u66F4\u65B0\u306F\u5DE6\u304B\u3089. \u3064\u307E\u308A, comp(new, old)\
    \ \u3068\u306A\u308B.\n        \"\"\"\n\n        self.__comp = comp\n        self.__id\
    \ = id\n\n        N = len(A)\n        d = max(1, (N - 1).bit_length())\n     \
    \   k = 1 << d\n\n        self.lazy = [self.id] * k + A + [self.id] * (k - N)\n\
    \        self.__size = k\n\n    @property\n    def comp(self) -> Callable[[F,\
    \ F], F]:\n        return self.__comp\n\n    @property\n    def id(self) -> F:\n\
    \        return self.__id\n\n    @property\n    def size(self) -> int:\n     \
    \   \"\"\" Dual Segment Tree \u306E\u5927\u304D\u3055 (\u6271\u3048\u308B\u8981\
    \u7D20\u756A\u53F7\u306E\u6700\u5927\u5024)\n\n        Returns:\n            int:\
    \ Dual Segment Tree \u306E\u5927\u304D\u3055\n        \"\"\"\n        return self.__size\n\
    \n    #\u914D\u5217\u306E\u7B2C m \u8981\u7D20\u3092\u4E0B\u306B\u4F1D\u642C\n\
    \    def _propagate_at(self, m: int):\n        \"\"\" \u9045\u5EF6\u4F1D\u642C\
    \u914D\u5217\u306E\u7B2C m \u8981\u7D20\u3092 1 \u500B\u4E0B\u306E\u5B50\u306B\
    \u4F1D\u642C\u3055\u305B\u308B.\n\n        Args:\n            m (int): \u8981\u7D20\
    \u756A\u53F7\n        \"\"\"\n\n        lazy = self.lazy\n        if lazy[m] ==\
    \ self.id:\n            return\n\n        lazy[(m << 1) | 0] = self.comp(lazy[m],\
    \ lazy[(m << 1) | 0])\n        lazy[(m << 1) | 1] = self.comp(lazy[m], lazy[(m\
    \ << 1) | 1])\n        lazy[m] = self.id\n\n    #\u914D\u5217\u306E\u7B2C m \u8981\
    \u7D20\u3088\u308A\u4E0A\u3092\u5168\u3066\u4F1D\u642C\n    def _propagate_above(self,\
    \ m: int):\n        \"\"\" \u9045\u5EF6\u4F1D\u642C\u914D\u5217\u306E\u7B2C m\
    \ \u8981\u7D20\u306E\u5148\u7956 (\u81EA\u5206\u81EA\u8EAB\u9664\u304F) \u3092\
    \u6839\u304B\u3089\u9806\u306B\u4F1D\u642C\u3055\u305B\u308B.\n\n        Args:\n\
    \            m (int): \u914D\u5217\u306E\u756A\u53F7\n        \"\"\"\n\n     \
    \   for h in range(m.bit_length() - 1, 0, -1):\n            self._propagate_at(m\
    \ >> h)\n\n    #\u4F5C\u7528\n    def action(self, l: int, r: int, alpha: F, left_closed:\
    \ bool = True, right_closed: bool = True):\n        \"\"\" \u7B2C l \u8981\u7D20\
    \u304B\u3089\u7B2C r \u8981\u7D20\u307E\u3067\u306E\u5404\u8981\u7D20\u306B alpha\
    \ \u3092\u4F5C\u7528\u3055\u305B\u308B.\n\n        Args:\n            l (int):\
    \ \u5DE6\u7AEF\n            r (int): \u53F3\u7AEF\n            alpha (F): \u4F5C\
    \u7528\u3055\u305B\u308B\u5024\n            left_closed (bool, optional): False\
    \ \u306B\u3059\u308B\u3068, \u5DE6\u7AEF\u304C\u958B\u533A\u9593\u306B\u306A\u308B\
    . Defaults to True.\n            right_closed (bool, optional): False \u306B\u3059\
    \u308B\u3068, \u53F3\u7AEF\u304C\u958B\u533A\u9593\u306B\u306A\u308B. Defaults\
    \ to True.\n        \"\"\"\n        L = l + self.size + (not left_closed)\n  \
    \      R = r + self.size + (right_closed)\n\n        L0 = R0 = -1\n        X,\
    \ Y = L, R - 1\n        while X < Y:\n            if X & 1:\n                L0\
    \ = max(L0, X)\n                X += 1\n\n            if Y & 1 == 0:\n       \
    \         R0 = max(R0, Y)\n                Y -= 1\n\n            X >>= 1\n   \
    \         Y >>= 1\n\n        L0 = max(L0, X)\n        R0 = max(R0, Y)\n\n    \
    \    self._propagate_above(L0)\n        self._propagate_above(R0)\n\n        lazy\
    \ = self.lazy\n        comp = self.comp\n        while L < R:\n            if\
    \ L & 1:\n                lazy[L] = comp(alpha, lazy[L])\n                L +=\
    \ 1\n\n            if R & 1:\n                R -= 1\n                lazy[R]\
    \ = comp(alpha, lazy[R])\n\n            L >>= 1\n            R >>= 1\n\n    #\u30EA\
    \u30D5\u30EC\u30C3\u30B7\u30E5\n    def refresh(self):\n        \"\"\" \u5168\u3066\
    \u306E\u9045\u5EF6\u3057\u3066\u3044\u308B\u4F1D\u642C\u3092\u89E3\u9664\u3059\
    \u308B.\n        \"\"\"\n\n        for m in range(1, self.size):\n           \
    \ self._propagate_at(m)\n\n    #\u53D6\u5F97\n    def get(self, k: int) -> F:\n\
    \        \"\"\" \u7B2C k \u8981\u7D20\u3092\u53D6\u5F97\u3059\u308B.\n\n     \
    \   Args:\n            k (int): \u8981\u7D20\u306E\u756A\u53F7\n\n        Returns:\n\
    \            F: \u7B2C k \u8981\u7D20\n        \"\"\"\n\n        m = k + self.size\n\
    \        self._propagate_above(m)\n        return self.lazy[m]\n\n    def __getitem__(self,\
    \ index: int) -> F:\n        m = index + self.size\n        self._propagate_above(m)\n\
    \        return self.lazy[m]\n"
  dependsOn: []
  isVerificationFile: false
  path: Segment_Tree/Dual_Segment_Tree.py
  requiredBy: []
  timestamp: '2025-05-23 00:45:05+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test_verify/yosupo_library_checker/Data_Structure/Dual_Segment_Tree.test.py
documentation_of: Segment_Tree/Dual_Segment_Tree.py
layout: document
title: Dual Segment Tree
---

## Outline

モノイド $F=(F, \circ, 1_F)$ の列に対する区間更新, 1点取得を得意とするデータ構造

## Contents

---

### Constructer

```Python
S=Dual_Segment_Tree(L, comp, id)
```

- $L$ : $M$ の列

以下, $N:=\lvert L \rvert$ とする.

- $\mathrm{comp} : F \times F \to F; (\alpha, \beta) \mapsto \alpha \circ \beta$ : 二項演算.
- $\mathrm{id}$ : $F$  の単位元 $1_F$.
- **計算量** : $O(N)$ Time.
- (※ 現在, $L$ は無効である)

---

### operate

```Python
S.operate(self, l, r, alpha, left_closed=True, right_closed=True)
```

- 第 $l$ 要素から第 $r$ 要素全てに対して, 左から $\alpha$ を作用させる.
- `left_close`=`False` にすると, 左側が開区間になる (つまり, 左端が含まれなくなる). `right_close` についても同様.
- **制約**
  - 作用させる区間を $I$ としたとき, $I$ は $[0,N)$ に含まれる.
  - $\alpha \in F$
- **計算量** : $O(\log N)$ Time.

---

### get

```Pyhon
S.get(k)
```

- 第 $k$ 要素を返す.
- **制約**
  - $0 \leq k \lt N$
- **計算量** : $O(\log N)$ Time.

---

### refresh

```Pyhon
B.refresh()
```

- 更新を遅延していた作用の記録を全て更新する.
- **計算量** : $O(N \log N)$ Time.
