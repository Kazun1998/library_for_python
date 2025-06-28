---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':warning:'
    path: Binary_Indexed_Tree/Range_Binary_Indexed_Tree.py
    title: Binary_Indexed_Tree/Range_Binary_Indexed_Tree.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test_verify/yosupo_library_checker/Data_Structure/Binary_Indexed_Tree.test.py
    title: test_verify/yosupo_library_checker/Data_Structure/Binary_Indexed_Tree.test.py
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
  code: "from typing import TypeVar, Generic, Callable, Generator\n\nGroup = TypeVar('Group')\n\
    class Binary_Indexed_Tree(Generic[Group]):\n    def __init__(self, L: list[Group],\
    \ op: Callable[[Group, Group], Group], zero: Group, neg: Callable[[Group], Group]):\n\
    \        \"\"\" op \u3092\u7FA4 Group \u306E\u6F14\u7B97\u3068\u3057\u3066 L \u304B\
    \u3089 Binary Indexed Tree \u3092\u751F\u6210\u3059\u308B.\n\n        Args:\n\
    \            L (list[Group]): \u521D\u671F\u72B6\u614B\n            op (Callable[[Group,\
    \ Group], Group]): \u7FA4\u6F14\u7B97\n            zero (Group): \u7FA4 Group\
    \ \u306B\u304A\u3051\u308B\u5358\u4F4D\u5143 (\u4EFB\u610F\u306E x in Group \u306B\
    \u5BFE\u3057\u3066, x + e = e + x = x \u3068\u306A\u308B e in Group)\n       \
    \     neg (Callable[[Group], Group]): x in Group \u306B\u304A\u3051\u308B\u9006\
    \u5143 (x + y = y + x = e \u3068\u306A\u308B y) \u3092\u6C42\u3081\u308B\u95A2\
    \u6570\n        \"\"\"\n\n        self.op=op\n        self.zero=zero\n       \
    \ self.neg=neg\n        self.sub: Callable[[Group, Group], Group] = lambda x,\
    \ y: self.op(x, self.neg(y))\n        self.N=N=len(L)\n        self.log=N.bit_length()-1\n\
    \n        X=[zero]*(N+1)\n\n        for i in range(N):\n            p=i+1\n  \
    \          X[p]=op(X[p],L[i])\n            q=p+(p&(-p))\n            if q<=N:\n\
    \                X[q]=op(X[q], X[p])\n        self.data=X\n\n    def get(self,\
    \ k: int) -> Group:\n        \"\"\" \u7B2C k \u9805\u3092\u6C42\u3081\u308B.\n\
    \n        Args:\n            k (int): \u8981\u7D20\u306E\u4F4D\u7F6E\n\n     \
    \   Returns:\n            Group: \u7B2C k \u9805\n        \"\"\"\n        return\
    \ self.sum(k, k)\n\n    def add(self, k: int, x: Group) -> None:\n        \"\"\
    \" \u7B2C k \u9805\u306B x \u3092\u52A0\u3048, \u66F4\u65B0\u3059\u308B.\n\n \
    \       Args:\n            k (int): \u8981\u7D20\u306E\u4F4D\u7F6E\n         \
    \   x (Group): \u52A0\u3048\u308B Group \u306E\u8981\u7D20\n        \"\"\"\n\n\
    \        data=self.data; op=self.op\n        p=k+1\n        while p<=self.N:\n\
    \            data[p]=op(self.data[p], x)\n            p+=p&(-p)\n\n    def update(self,\
    \ k: int, x: Group) -> None:\n        \"\"\" \u7B2C k \u9805\u3092 x \u306B\u5909\
    \u3048\u3066\u66F4\u65B0\u3059\u308B.\n\n        Args:\n            k (int): \u8981\
    \u7D20\u306E\u4F4D\u7F6E\n            x (Group): \u66F4\u65B0\u5148\u306E\u5024\
    \n        \"\"\"\n\n        a=self.get(k)\n        y = self.sub(x, a)\n\n    \
    \    self.add(k,y)\n\n    def sum(self, l: int, r: int) -> Group:\n        \"\"\
    \" \u7B2C l \u9805\u304B\u3089\u7B2C r \u9805\u307E\u3067\u306E\u7DCF\u548C\u3092\
    \u6C42\u3081\u308B (\u305F\u3060\u3057, l != 0 \u306E\u3068\u304D\u306F Group\
    \ \u304C\u7FA4\u3067\u306A\u304F\u3066\u306F\u306A\u3089\u306A\u3044).\n\n   \
    \     Args:\n            l (int): \u5DE6\u7AEF\n            r (int): \u53F3\u7AEF\
    \n\n        Returns:\n            Group: \u7DCF\u548C\n        \"\"\"\n\n    \
    \    l=l+1 if 0<=l else 1\n        r=r+1 if r<self.N else self.N\n\n        if\
    \ l>r:\n            return self.zero\n        elif l==1:\n            return self.__section(r)\n\
    \        else:\n            return self.sub(self.__section(r), self.__section(l\
    \ - 1))\n\n    def __section(self, x: int) -> Group:\n        \"\"\" B[0] + B[1]\
    \ + ... + B[x] \u3092\u6C42\u3081\u308B.\n\n        Args:\n            x (int):\
    \ \u53F3\u7AEF\n\n        Returns:\n            Group: \u7DCF\u548C\n        \"\
    \"\"\n\n        data=self.data; op=self.op\n        S=self.zero\n        while\
    \ x>0:\n            S=op(data[x], S)\n            x-=x&(-x)\n        return S\n\
    \n    def all_sum(self) -> Group:\n        \"\"\" B[0] + B[1] + ... + B[len(B)\
    \ - 1] \u3092\u6C42\u3081\u308B.\n\n        Returns:\n            Group: \u7DCF\
    \u548C\n        \"\"\"\n        return self.sum(0, self.N-1)\n\n    def binary_search(self,\
    \ cond: Callable[[Group], bool]) -> int:\n        \"\"\" cond(B[0] + B[1] + ...\
    \ + B[k]) \u304C True \u306B\u306A\u308B\u6700\u5C0F\u306E k \u3092\u6B62\u3081\
    \u308B.\n\n        \u203B Group \u306F\u9806\u5E8F\u7FA4\u3067\u3042\u308B\u5FC5\
    \u8981\u304C\u3042\u308B.\n        \u203B cond(zero) = True \u306E\u3068\u304D\
    , \u8FD4\u308A\u5024\u306F -1 \u3068\u3059\u308B.\n        \u203B cond(B[0] +\
    \ ... + B[k]) \u306A\u308B k \u304C (0 <= k < N \u306B) \u5B58\u5728\u3057\u306A\
    \u3044\u5834\u5408, \u8FD4\u308A\u5024\u306F N \u3068\u3059\u308B.\n\n       \
    \ Args:\n            cond (Callable[[Group], bool]): \u5358\u8ABF\u5897\u52A0\u306A\
    \u6761\u4EF6\n\n        Returns:\n            int: cond(B[0] + B[1] + ... + B[k])\
    \ \u304C True \u306B\u306A\u308B\u6700\u5C0F\u306E k\n        \"\"\"\n\n     \
    \   if cond(self.zero):\n            return -1\n\n        j=0\n        t=1<<self.log\n\
    \        data=self.data; op=self.op\n        alpha=self.zero\n\n        while\
    \ t>0:\n            if j+t<=self.N:\n                beta=op(alpha, data[j+t])\n\
    \                if not cond(beta):\n                    alpha=beta\n        \
    \            j+=t\n            t>>=1\n\n        return j\n\n    def __getitem__(self,\
    \ index) -> Group:\n        if isinstance(index, int):\n            return self.get(index)\n\
    \        else:\n            return [self.get(t) for t in index]\n\n    def __setitem__(self,\
    \ index: int, val: Group):\n        self.update(index, val)\n\n    def __iter__(self):\n\
    \        for k in range(self.N):\n            yield self.sum(k, k)\n"
  dependsOn: []
  isVerificationFile: false
  path: Binary_Indexed_Tree/Binary_Indexed_Tree.py
  requiredBy:
  - Binary_Indexed_Tree/Range_Binary_Indexed_Tree.py
  timestamp: '2025-06-22 18:31:18+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test_verify/yosupo_library_checker/Data_Structure/Binary_Indexed_Tree.test.py
documentation_of: Binary_Indexed_Tree/Binary_Indexed_Tree.py
layout: document
title: Binary Indexed Tree (Fenwick Tree)
---

## Outline

可換群 $G=(G, +, 0_G)$ の列に対する1点更新, 区間和の取得を得意とするデータ構造

## Contents

---

### Constructer

```Python
B=Binary_Indexed_Tree(L, calc, unit, inv)
```

- $L$ : $G$ の列

以下, $N:=\lvert L \rvert$ の長さとする.

- $\operatorname{calc} : G \times G \to G; (x,y) \mapsto x+y$ : 二項演算.
- $\mathrm{unit}$ : $G$  の単位元 $0_G$.
- $\operatorname{inv}$ : $G \to G; x \mapsto -x$ : $x$ の逆元.
- **計算量** : $O(N)$ Time.

---

### get

```Pyhon
B.get(k)
```

- 第 $k$ 要素を返す.
- **制約**
  - $0 \leq k \lt N$
- **計算量** : $O(\log N)$ Time.

---

### add

```Pyhon
B.add(k, x)
```

- 第 $k$ 要素に $x$ を加算する.
- **制約**
  - $0 \leq k \lt N$
  - $x \in G$
- **計算量** : $O(\log N)$ Time.

---

### update

```Pyhon
B.update(k,x)
```

- 第 $k$ 要素を $x$ に変更する.
- **制約**
  - $0 \leq k \lt N$
  - $x \in G$
- **計算量** : $O(\log N)$ Time.

---

### sum

```Pyhon
B.sum(l, r)
```

- $\displaystyle \sum_{k=l}^r B_k$ を求める ( $l \gt r$ の場合は $0_G$ とする).
- **制約**
  - $0 \leq l \lt N$
  - $0 \leq r \lt N$
- **計算量** : $O(\log N)$ Time.

---

### all_sum

```Pyhon
B.all_sum(k)
```

- $\displaystyle \sum_{k=0}^{N-1} B_k$ を求める.
- **制約**
- **計算量** : $O(\log N)$ Time.

---

### binary_search

```Pyhon
B.binary_search(cond)
```

- $G$ が単位元で, $\operatorname{cond}$ が単調増加であるとき, $\displaystyle \operatorname{cond} \left(\sum_{i=0}^k B_i \right)=\mathbb{T}$ となるような最小の $k$ を求める.
- なお, 次のような例外ケースがある.
  - $\displaystyle \operatorname{cond} (0_G)=\mathbb{T}$ の場合, $k=-1$ とする.
  - $\displaystyle \operatorname{cond} \left(\sum_{i=0}^{N-1} B_i\right)=\mathbb{F}$ の場合, $k=N$ とする.
- **制約**
  - $\operatorname{cond}: G \to \\{\mathbb{T}, \mathbb{F} \\}$ : 単調増加
- **計算量** : $O(\log N)$ Time.
