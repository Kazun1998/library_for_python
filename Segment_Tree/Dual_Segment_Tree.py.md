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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class Dual_Segment_Tree:\n    def __init__(self, L, comp, id):\n        \"\
    \"\" comp \u3092\u6F14\u7B97\u3068\u3059\u308B\u30EA\u30B9\u30C8 L \u306E Dual\
    \ Segment Tree \u3092\u4F5C\u6210\n\n        comp : \u4F5C\u7528\u7D20\n     \
    \   id : \u5358\u4F4D\u5143\n\n        [\u6CE8\u8A18]\n        \u66F4\u65B0\u306F\
    \u5DE6\u304B\u3089. \u3064\u307E\u308A, comp(new, old) \u3068\u306A\u308B.\n \
    \       \"\"\"\n\n        self.comp=comp\n        self.id=id\n\n        N=len(L)\n\
    \        d=max(1,(N-1).bit_length())\n        k=1<<d\n\n        self.lazy=[self.id]*k+L+[self.id]*(k-N)\n\
    \        self.N=k\n        self.depth=d\n\n    #\u914D\u5217\u306E\u7B2C m \u8981\
    \u7D20\u3092\u4E0B\u306B\u4F1D\u642C\n    def _propagate_at(self,m):\n       \
    \ lazy=self.lazy\n        if lazy[m]!=self.id:\n            lazy[(m<<1)|0]=self.comp(lazy[m],lazy[(m<<1)|0])\n\
    \            lazy[(m<<1)|1]=self.comp(lazy[m],lazy[(m<<1)|1])\n            lazy[m]=self.id\n\
    \n    #\u914D\u5217\u306E\u7B2C m \u8981\u7D20\u3088\u308A\u4E0A\u3092\u5168\u3066\
    \u4F1D\u642C\n    def _propagate_above(self,m):\n        H=m.bit_length()\n  \
    \      for h in range(H-1,0,-1):\n            self._propagate_at(m>>h)\n\n   \
    \ #\u4F5C\u7528\n    def operate(self, l, r, alpha, left_closed=True, right_closed=True):\n\
    \        L=l+self.N+(not left_closed)\n        R=r+self.N+(right_closed)\n\n \
    \       L0=R0=-1\n        X,Y=L,R-1\n        while X<Y:\n            if X&1:\n\
    \                L0=max(L0,X)\n                X+=1\n\n            if Y&1==0:\n\
    \                R0=max(R0,Y)\n                Y-=1\n\n            X>>=1\n   \
    \         Y>>=1\n\n        L0=max(L0,X)\n        R0=max(R0,Y)\n\n        self._propagate_above(L0)\n\
    \        self._propagate_above(R0)\n\n        lazy=self.lazy; comp=self.comp\n\
    \        while L<R:\n            if L&1:\n                lazy[L]=comp(alpha,\
    \ lazy[L])\n                L+=1\n\n            if R&1:\n                R-=1\n\
    \                lazy[R]=comp(alpha, lazy[R])\n\n            L>>=1\n         \
    \   R>>=1\n\n    #\u30EA\u30D5\u30EC\u30C3\u30B7\u30E5\n    def refresh(self):\n\
    \        for m in range(1,self.N):\n            self._propagate_at(m)\n\n    #\u53D6\
    \u5F97\n    def get(self,k):\n        m=k+self.N\n        self._propagate_above(m)\n\
    \        return self.lazy[m]\n\n    def __getitem__(self,index):\n        m=index+self.N\n\
    \        self._propagate_above(m)\n        return self.lazy[m]\n\n    def __setitem__(self,index,value):\n\
    \        self.operate(index, index, value)\n"
  dependsOn: []
  isVerificationFile: false
  path: Segment_Tree/Dual_Segment_Tree.py
  requiredBy: []
  timestamp: '2022-11-22 04:21:42+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
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
