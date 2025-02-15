---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test_verify/yosupo_library_checker/Data_Structure/Lazy_Segment_Tree.test.py
    title: test_verify/yosupo_library_checker/Data_Structure/Lazy_Segment_Tree.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.13.2/x64/lib/python3.13/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.13.2/x64/lib/python3.13/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "\"\"\"\nNote\n[1] RMQ(\u533A\u9593\u4E0A\u306E\u6700\u5C0F\u5024:Range Minimum\
    \ Query)\nop=lambda x,y:min(x,y)\nunit=float(\"inf\")\nact=lambda alpha,x:alpha\n\
    comp=lambda alpha,beta:alpha\n\"\"\"\n\nclass Lazy_Evaluation_Tree():\n    def\
    \ __init__(self, L, op, unit, act, comp, id):\n        \"\"\" op \u3092\u6F14\u7B97\
    , act \u3092\u4F5C\u7528\u3068\u3059\u308B\u30EA\u30B9\u30C8 L \u306E Segment\
    \ Tree \u3092\u4F5C\u6210\n\n        op: \u6F14\u7B97\n        unit: Monoid op\
    \ \u306E\u5358\u4F4D\u5143 ( xe=ex=x \u3092\u6E80\u305F\u3059 e )\n        act:\
    \ \u4F5C\u7528\u7D20\n        comp: \u4F5C\u7528\u7D20\u306E\u5408\u6210\n   \
    \     id: \u6052\u7B49\u5199\u50CF\n\n        [\u6761\u4EF6] M: Monoid, F={f:\
    \ F x M\u2192 M: \u4F5C\u7528\u7D20} \u306B\u5BFE\u3057\u3066, \u4EE5\u4E0B\u304C\
    \u6210\u7ACB\u3059\u308B.\n        F \u306F\u6052\u7B49\u5199\u50CF id \u3092\u542B\
    \u3080.\u3064\u307E\u308A, \u4EFB\u610F\u306E x in M \u306B\u5BFE\u3057\u3066\
    \ id(x)=x\n        F \u306F\u5199\u50CF\u306E\u5408\u6210\u306B\u9589\u3058\u3066\
    \u3044\u308B. \u3064\u307E\u308A, \u4EFB\u610F\u306E f,g in F \u306B\u5BFE\u3057\
    \u3066, comp(f,g) in F\n        \u4EFB\u610F\u306E f in F, x,y in M \u306B\u5BFE\
    \u3057\u3066, f(xy)=f(x) f(y) \u3067\u3042\u308B.\n\n        [\u6CE8\u8A18]\n\
    \        \u4F5C\u7528\u7D20\u306F\u5DE6\u304B\u3089\u639B\u3051\u308B. \u66F4\u65B0\
    \u3082\u5DE6\u304B\u3089.\n        \"\"\"\n\n        self.op=op\n        self.unit=unit\n\
    \        self.act=act\n        self.comp=comp\n        self.id=id\n\n        N=len(L)\n\
    \        d=max(1,(N-1).bit_length())\n        k=1<<d\n\n        self.data=data=[unit]*k+L+[unit]*(k-len(L))\n\
    \        self.lazy=[id]*(2*k)\n        self.N=k\n        self.depth=d\n\n    \
    \    for i in range(k-1,0,-1):\n            data[i]=op(data[i<<1], data[i<<1|1])\n\
    \n    def _eval_at(self, m):\n        if self.lazy[m]==self.id:\n            return\
    \ self.data[m]\n        return self.act(self.lazy[m],self.data[m])\n\n    #\u914D\
    \u5217\u306E\u7B2Cm\u8981\u7D20\u3092\u4E0B\u306B\u4F1D\u642C\n    def _propagate_at(self,\
    \ m):\n        self.data[m]=self._eval_at(m)\n        lazy=self.lazy; comp=self.comp\n\
    \n        if m<self.N and self.lazy[m]!=self.id:\n            lazy[m<<1]=comp(lazy[m],\
    \ lazy[m<<1])\n            lazy[m<<1|1]=comp(lazy[m], lazy[m<<1|1])\n        lazy[m]=self.id\n\
    \n    #\u914D\u5217\u306E\u7B2Cm\u8981\u7D20\u3088\u308A\u4E0A\u3092\u5168\u3066\
    \u4F1D\u642C\n    def _propagate_above(self, m):\n        H=m.bit_length()\n \
    \       for h in range(H-1, 0, -1):\n            self._propagate_at(m>>h)\n\n\
    \    #\u914D\u5217\u306E\u7B2Cm\u8981\u7D20\u3088\u308A\u4E0A\u3092\u5168\u3066\
    \u518D\u8A08\u7B97\n    def _recalc_above(self, m):\n        data=self.data; op=self.op\n\
    \        eval_at=self._eval_at\n        while m>1:\n            m>>=1\n      \
    \      data[m]=op(eval_at(m<<1),eval_at(m<<1|1))\n\n    def get(self,k):\n   \
    \     m=k+self.N\n        self._propagate_above(m)\n        self.data[m]=self._eval_at(m)\n\
    \        self.lazy[m]=self.id\n        return self.data[m]\n\n    #\u4F5C\u7528\
    \n    def action(self, l, r, alpha, left_closed=True, right_closed=True):\n  \
    \      \"\"\" \u7B2C l \u8981\u7D20\u304B\u3089\u7B2C r \u8981\u7D20\u5168\u3066\
    \u306B alpha \u3092\u4F5C\u7528\u3055\u305B\u308B.\n\n        \"\"\"\n\n     \
    \   L=l+self.N+(not left_closed)\n        R=r+self.N+(right_closed)\n\n      \
    \  L0=R0=-1\n        X,Y=L,R-1\n        while X<Y:\n            if X&1:\n    \
    \            L0=max(L0,X)\n                X+=1\n\n            if Y&1==0:\n  \
    \              R0=max(R0,Y)\n                Y-=1\n\n            X>>=1\n     \
    \       Y>>=1\n\n        L0=max(L0,X)\n        R0=max(R0,Y)\n\n        self._propagate_above(L0)\n\
    \        self._propagate_above(R0)\n\n        lazy=self.lazy; comp=self.comp\n\
    \        while L<R:\n            if L&1:\n                lazy[L]=comp(alpha,\
    \ lazy[L])\n                L+=1\n\n            if R&1:\n                R-=1\n\
    \                lazy[R]=comp(alpha, lazy[R])\n\n            L>>=1\n         \
    \   R>>=1\n\n        self._recalc_above(L0)\n        self._recalc_above(R0)\n\n\
    \    def update(self, k, x):\n        \"\"\" \u7B2C k \u8981\u7D20\u3092 x \u306B\
    \u5909\u66F4\u3059\u308B.\n        \"\"\"\n\n        m=k+self.N\n        self._propagate_above(m)\n\
    \        self.data[m]=x\n        self.lazy[m]=self.id\n        self._recalc_above(m)\n\
    \n    def product(self, l, r, left_closed=True, right_closed=True):\n        \"\
    \"\" \u7B2C l \u8981\u7D20\u304B\u3089\u7B2C r \u8981\u7D20\u307E\u3067\u306E\u7DCF\
    \u7A4D\u3092\u6C42\u3081\u308B.\n\n        \"\"\"\n\n        L=l+self.N+(not left_closed)\n\
    \        R=r+self.N+(right_closed)\n\n        L0=R0=-1\n        X,Y=L,R-1\n  \
    \      while X<Y:\n            if X&1:\n                L0=max(L0,X)\n       \
    \         X+=1\n\n            if Y&1==0:\n                R0=max(R0,Y)\n     \
    \           Y-=1\n\n            X>>=1\n            Y>>=1\n\n        L0=max(L0,X)\n\
    \        R0=max(R0,Y)\n\n        self._propagate_above(L0)\n        self._propagate_above(R0)\n\
    \n        vL=vR=self.unit\n        op=self.op; eval_at=self._eval_at\n       \
    \ while L<R:\n            if L&1:\n                vL=op(vL, eval_at(L))\n   \
    \             L+=1\n\n            if R&1:\n                R-=1\n            \
    \    vR=op(eval_at(R), vR)\n\n            L>>=1\n            R>>=1\n\n       \
    \ return self.op(vL,vR)\n\n    def all_product(self):\n        return self.product(0,self.N-1)\n\
    \n    def max_right(self, left: int, cond) -> int:\n        \"\"\" \u4EE5\u4E0B\
    \u306E (1), (2) \u3092\u6E80\u305F\u3059\u6574\u6570 r \u3092\u6C42\u3081\u308B\
    .\n        (1) r=left or cond(data[left] data[left+1] ... data[r-1]): True\n \
    \       (2) r=N or cond(data[left] data[left+1] ... data[r]): False\n\n      \
    \  Args:\n            left (int): \u5DE6\u7AEF\n            cond : \u6761\u4EF6\
    \n\n        Returns:\n            int: (1), (2) \u3092\u6E80\u305F\u3059\u6574\
    \u6570 r\n        \"\"\"\n\n        assert 0 <= left <= self.N, f\"\u6DFB\u5B57\
    \ ({left = }) \u304C\u7BC4\u56F2\u5916\"\n        assert cond(self.unit), \"\u5358\
    \u4F4D\u5143\u304C\u6761\u4EF6\u3092\u6E80\u305F\u3055\u306A\u3044\"\n\n     \
    \   if left == self.N:\n            return self.N\n\n        left += self.N\n\
    \        sm = self.unit\n\n        op = self.op; data = self.data\n        first\
    \ = True\n\n        self._propagate_above(left)\n\n        while first or (left\
    \ & (-left)) != left:\n            first = False\n            while left % 2 ==\
    \ 0:\n                left >>= 1\n\n            if not cond(op(sm, data[left])):\n\
    \                while left < self.N:\n                    self._propagate_at(left)\n\
    \                    left <<= 1\n                    self._propagate_at(left)\n\
    \                    if cond(op(sm, data[left])):\n                        sm\
    \ = op(sm, data[left])\n                        left += 1\n                return\
    \ left - self.N\n            sm = op(sm, data[left])\n            left += 1\n\n\
    \        return self.N\n\n    #\u30EA\u30D5\u30EC\u30C3\u30B7\u30E5\n    def refresh(self):\n\
    \        lazy=self.lazy; comp=self.comp\n        for m in range(1,2*self.N):\n\
    \            self.data[m]=self._eval_at(m)\n\n            if m<self.N and self.lazy[m]!=self.id:\n\
    \                lazy[m<<1]=comp(lazy[m], lazy[m<<1])\n                lazy[m<<1|1]=comp(lazy[m],\
    \ lazy[m<<1|1])\n            lazy[m]=self.id\n\n    def __getitem__(self,k):\n\
    \        return self.get(k)\n\n    def __setitem__(self,k,x):\n        self.update(k,x)\n"
  dependsOn: []
  isVerificationFile: false
  path: Segment_Tree/Lazy_Segment_Tree.py
  requiredBy: []
  timestamp: '2025-02-09 14:01:56+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test_verify/yosupo_library_checker/Data_Structure/Lazy_Segment_Tree.test.py
documentation_of: Segment_Tree/Lazy_Segment_Tree.py
layout: document
title: Lazy Segment Tree
---

## Outline

$M=(M, \*, e_M), F=(F, \circ, 1_F)$ はそれぞれモノイドであり, $F$ は $M$ に左から作用するとし, この作用を $F \times M \to M; (\alpha,x) \mapsto \alpha(x)$ と書くことにする.

また, この作用は各 $\alpha \in F$ に対して準同型であるとする.

つまり, この作用は以下を満たすとする.

- $\forall \alpha, \beta \in F, \forall x \in M; (\alpha \circ \beta)(x)=\alpha(\beta(x))$
- $\forall x \in M; 1_F(x)=x$
- $\forall \alpha \in F, \forall x,y \in M; \alpha(x \* y)=\alpha(x) \* \alpha(y)$

このような $M$ の列に対する1点更新, $X$ の元による区間更新, 区間積の取得を得意とするデータ構造である.

## Contents

---

### Constructer

```Python
S=Lazy_Evaluation_Tree(L, calc, unit, op, comp, id)
```

- $L$ : $M$ の列

以下, $N:=\lvert L \rvert$ とする.

- $\operatorname{calc} : M \times M \to M; (x,y) \mapsto x \* y$ : 二項演算.
- $\mathrm{unit}$ : $M$  の単位元 $e_M$.
- $\mathrm{op}$ : $F \times M; (\alpha, x) \mapsto \alpha(x)$ : $F$ の $M$ への作用
- $\mathrm{comp}$ : $F \times F \to F; (\alpha,\beta) \mapsto \alpha \circ \beta$ : $F$ における合成
- $\mathrm{id}$ : $F$ の単位元 $1_F$ .
- **計算量** : $O(N)$ Time.

---

### get

```Pyhon
S.get(k)
```

- 第 $k$ 要素を返す.
- **制約**
  - $0 \leq k \lt N$
- **計算量** : $O(1)$ Time.

---

### operate

```Pyhon
S.get(l, r, alpha, left_close=True, right_close=True)
```

- 第 $l$ 要素から第 $r$ 要素に $\alpha$ を作用させる.
- `left_close`=`False` にすると, 左側が開区間になる (つまり, 左端が含まれなくなる). `right_close` についても同様.
- **制約**
  - 作用させる区間を $I$ としたとき, $I$ は $[0,N)$ に含まれる.
  - $\alpha \in F$
- **計算量** : $O(\log N)$ Time.

---

### update

```Pyhon
S.update(k,x)
```

- 第 $k$ 要素を $x$ に変更する.
- **制約**
  - $0 \leq k \lt N$
  - $x \in M$
- **計算量** : $O(\log N)$ Time.

---

### product

```Pyhon
B.product(l, r, left_close=True, right_close=True)
```

- $B_l \* B_{l+1} \* \dots \* B_r$ を求める (ただし, 空積は $e_M$ とする) .
- `left_close`=`False` にすると, 左側が開区間になる (つまり, 左端が含まれなくなる). `right_close` についても同様.
- **制約**
  - 作用させる区間を $I$ としたとき, $I$ は $[0,N)$ に含まれる.
  - $\alpha \in F$

- **計算量** : $O(\log N)$ Time.

---

### all_product

```Pyhon
B.all_product()
```

- $B_0 \* B_1 \* \dots \* B_{N-1}$ を求める.
- **計算量** : $O(N \log N)$ Time.

---

### refresh

```Pyhon
B.refresh()
```

- 更新を遅延していた作用の記録を全て更新する.
- **計算量** : $O(N \log N)$ Time.
