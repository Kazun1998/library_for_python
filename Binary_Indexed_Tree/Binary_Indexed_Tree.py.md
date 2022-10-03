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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.7/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.7/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class Binary_Indexed_Tree():\n    def __init__(self, L, calc, unit, inv):\n\
    \        \"\"\" calc \u3092\u6F14\u7B97\u3068\u3059\u308B N \u9805\u306E Binary\
    \ Indexed Tree \u3092\u4F5C\u6210\n        calc: \u6F14\u7B97 (2\u5909\u6570\u95A2\
    \u6570, \u53EF\u63DB\u7FA4)\n        unit: \u7FA4 calc \u306E\u5358\u4F4D\u5143\
    \ (x+e=e+x=x \u3092\u6E80\u305F\u3059 e)\n        inv : \u7FA4 calc \u306E\u9006\
    \u5143 (1\u5909\u6570\u95A2\u6570, x+inv(x)=inv(x)+x=e \u3092\u307F\u305F\u3059\
    \ inv(x))\n        \"\"\"\n        self.calc=calc\n        self.unit=unit\n  \
    \      self.inv=inv\n        self.N=N=len(L)\n        self.log=N.bit_length()-1\n\
    \n        X=[unit]*(N+1)\n\n        for i in range(N):\n            p=i+1\n  \
    \          X[p]=calc(X[p],L[i])\n            q=p+(p&(-p))\n            if q<=N:\n\
    \                X[q]=calc(X[q], X[p])\n        self.data=X\n\n    def get(self,\
    \ k):\n        \"\"\" \u7B2C k \u8981\u7D20\u306E\u5024\u3092\u51FA\u529B\u3059\
    \u308B.\n\n        k    : \u6570\u5217\u306E\u8981\u7D20\n        index: \u5148\
    \u982D\u306E\u8981\u7D20\u306E\u756A\u53F7\n        \"\"\"\n        return self.sum(k,k)\n\
    \n    def add(self, k, x):\n        \"\"\" \u7B2C k \u8981\u7D20\u306B x \u3092\
    \u52A0\u3048, \u66F4\u65B0\u3092\u884C\u3046.\n\n        k    : \u6570\u5217\u306E\
    \u8981\u7D20\n        x    : \u52A0\u3048\u308B\u5024\n        \"\"\"\n      \
    \  data=self.data; calc=self.calc\n        p=k+1\n        while p<=self.N:\n \
    \           data[p]=calc(self.data[p],x)\n            p+=p&(-p)\n\n    def update(self,\
    \ k, x):\n        \"\"\" \u7B2C k \u8981\u7D20\u3092 x \u306B\u5909\u3048, \u66F4\
    \u65B0\u3092\u884C\u3046.\n\n        k: \u6570\u5217\u306E\u8981\u7D20\n     \
    \   x: \u66F4\u65B0\u5F8C\u306E\u5024\n        \"\"\"\n\n        a=self.get(k)\n\
    \        y=self.calc(self.inv(a),x)\n\n        self.add(k,y)\n\n    def sum(self,\
    \ l, r):\n        \"\"\" \u7B2C l \u8981\u7D20\u304B\u3089\u7B2C r \u8981\u7D20\
    \u307E\u3067\u306E\u7DCF\u548C\u3092\u6C42\u3081\u308B.\n        \u203B l != 0\
    \ \u3092\u4F7F\u3046\u306A\u3089\u3070, \u7FA4\u3067\u306A\u304F\u3066\u306F\u306A\
    \u3089\u306A\u3044.\n        l: \u59CB\u307E\u308A\n        r: \u7D42\u308F\u308A\
    \n        \"\"\"\n        l=l+1 if 0<=l else 1\n        r=r+1 if r<self.N else\
    \ self.N\n\n        if l>r:\n            return self.unit\n        elif l==1:\n\
    \            return self.__section(r)\n        else:\n            return self.calc(self.inv(self.__section(l-1)),self.__section(r))\n\
    \n    def __section(self,x):\n        \"\"\" B[0]+...+B[x] \u3092\u6C42\u3081\u308B\
    . \"\"\"\n        data=self.data; calc=self.calc\n        S=self.unit\n      \
    \  while x>0:\n            S=calc(data[x],S)\n            x-=x&(-x)\n        return\
    \ S\n\n    def all_sum(self):\n        return self.sum(0,self.N-1)\n\n    def\
    \ binary_search(self, cond):\n        \"\"\" cond(B[0]+...+B[k]) \u3092\u6E80\u305F\
    \u3059\u6700\u5C0F\u306E k \u3092\u8FD4\u3059.\n\n        cond: \u5358\u8ABF\u5897\
    \u52A0\n\n        \u203B cond(unit)=True \u306E\u5834\u5408\u306E\u8FD4\u308A\u5024\
    \u306F -1\n        \u203B cond(B[0]+...+B[k]) \u306A\u308B k \u304C (0<=k<N \u306B\
    ) \u5B58\u5728\u3057\u306A\u3044\u5834\u5408\u306E\u8FD4\u308A\u5024\u306F N\n\
    \        \"\"\"\n\n        if cond(self.unit):\n            return -1\n\n    \
    \    j=0\n        r=self.N\n        t=1<<self.log\n        data=self.data; calc=self.calc\n\
    \        alpha=self.unit\n\n        while t>0:\n            if j+t<=self.N:\n\
    \                beta=calc(alpha,data[j+t])\n                if not cond(beta):\n\
    \                    alpha=beta\n                    j+=t\n            t>>=1\n\
    \n        return j\n\n    def __getitem__(self,index):\n        if isinstance(index,int):\n\
    \            return self.get(index)\n        else:\n            return [self.get(t)\
    \ for t in index]\n\n    def __setitem__(self,index,val):\n        self.update(index,val)\n\
    \n    def __iter__(self):\n        for k in range(self.N):\n            yield\
    \ self.sum(k,k)\n"
  dependsOn: []
  isVerificationFile: false
  path: Binary_Indexed_Tree/Binary_Indexed_Tree.py
  requiredBy: []
  timestamp: '2022-10-02 18:20:23+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
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

以下, $N=\\|L\\|$ とする.

- $\operatorname{calc} : G \times G \to G; (x,y) \mapsto x+y$ 二項演算.
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
