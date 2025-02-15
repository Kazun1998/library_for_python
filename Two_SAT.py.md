---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test_verify/yosupo_library_checker/Math/Two_Sat.test.py
    title: test_verify/yosupo_library_checker/Math/Two_Sat.test.py
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
  code: "\"\"\"\n\u5909\u6570 X_i \u306E\u5426\u5B9A\u306F ~i \u3067\u5BA3\u8A00\u3059\
    \u308B.\n\u4F8B\u3048\u3070, ~0=-1 \u306A\u306E\u3067, X_{-1} \u306F not X_0 \u3092\
    \u610F\u5473\u3059\u308B.\n\"\"\"\n\nclass Two_SAT:\n    def __init__(self, N=0):\n\
    \        \"\"\" N \u5909\u6570\u306E 2-SAT \u3092\u5B9A\u7FA9\u3059\u308B.\n\n\
    \        N: int\n        \"\"\"\n\n        self.N=N\n        self.var_num=N\n\
    \        self.__cost=2*N\n\n        self.arc=[[] for _ in range(2*N)]\n      \
    \  self.rev=[[] for _ in range(2*N)]\n\n    def cost(self):\n        return self.__cost\n\
    \n    def var_to_index(self, v):\n        if v>=0:\n            return 2*v\n \
    \       else:\n            return 2*(-v-1)+1\n\n    def index_to_var(self, i):\n\
    \        if i%2:\n            return -(i+1)//2\n        else:\n            return\
    \ i//2\n\n    def add_variable(self, k=1):\n        \"\"\" \u65B0\u305F\u306B\u5909\
    \u6570 k \u500B\u3092\u52A0\u3048\u308B.\n        \"\"\"\n\n        m=self.var_num\n\
    \        self.var_num+=k\n        self.__cost+=2*k\n\n        self.arc+=[[] for\
    \ _ in range(2*k)]\n        self.rev+=[[] for _ in range(2*k)]\n\n        return\
    \ list(range(m, m+k))\n\n    def __add_clause(self,i,j):\n        self.__cost+=1\n\
    \        self.arc[self.var_to_index(i)].append(self.var_to_index(j))\n       \
    \ self.rev[self.var_to_index(j)].append(self.var_to_index(i))\n\n    def add_imply(self,\
    \ i, j):\n        \"\"\" X_i -> X_j \u3092\u52A0\u3048\u308B.\n        \"\"\"\n\
    \        self.__add_clause(i, j)\n        self.__add_clause(~j, ~i)\n\n    def\
    \ add_or(self, i, j):\n        \"\"\" X_i or X_j \u3092\u52A0\u3048\u308B.\n \
    \       \"\"\"\n\n        self.add_imply(~i, j)\n\n    def add_nand(self, i, j):\n\
    \        \"\"\" not (X_i and X_j) \u3092\u52A0\u3048\u308B.\n        \"\"\"\n\n\
    \        self.add_imply(i, ~j)\n\n    def add_equal(self, i, j):\n        \"\"\
    \" X_i=X_j \u3092\u8FFD\u52A0\u3059\u308B.\n        \"\"\"\n\n        self.add_imply(i,\
    \ j)\n        self.add_imply(~i, ~j)\n\n    def add_not_equal(self, i, j):\n \
    \       \"\"\" X_i != X_j \u3092\u8FFD\u52A0\u3059\u308B.\n        \"\"\"\n  \
    \      self.add_equal(i, ~j)\n\n    def add_equivalent(self, *I):\n        \"\"\
    \" I=[i_0, ..., i_{k-1}] \u306B\u5BFE\u3057\u3066, X_{i_0}=...=X_{i_{k-1}} \u3092\
    \u8FFD\u52A0\u3059\u308B.\n        \"\"\"\n\n        k=len(I)\n\n        if k<=1:\n\
    \            return\n\n        for j in range(k-1):\n            self.add_imply(I[j],I[j+1])\n\
    \        self.add_imply(I[-1],I[0])\n\n    def set_true(self, i):\n        \"\"\
    \" \u5909\u6570 X_i \u3092 True \u306B\u3059\u308B.\n        \"\"\"\n\n      \
    \  self.__add_clause(~i, i)\n\n    def set_false(self, i):\n        \"\"\" \u5909\
    \u6570 X_i \u3092 False \u306B\u3059\u308B.\n        \"\"\"\n\n        self.__add_clause(i,\
    \ ~i)\n\n    def at_most_one(self, *I):\n        \"\"\" X_i (i in I) \u3092\u6E80\
    \u305F\u3059\u3088\u3046\u306A i \u306F\u9AD8\u30051\u3064\u3060\u3051\u3068\u3044\
    \u3046\u6761\u4EF6\u3092\u8FFD\u52A0\u3059\u308B.\n        \"\"\"\n\n        k=len(I)\n\
    \n        if k<=1:\n            return\n\n        A=self.add_variable(k)\n\n \
    \       self.add_imply(I[0],A[0])\n        for i in range(1,k):\n            self.add_imply(A[i-1],A[i])\n\
    \            self.add_imply(I[i],A[i])\n            self.add_nand(A[i-1],I[i])\n\
    \n    def is_satisfy(self, Mode=0):\n        \"\"\" Two-SAT \u306F\u5145\u8DB3\
    \u53EF\u80FD?\n\n        Mode:\n        0 (Defalt): \u5145\u8DB3\u53EF\u80FD?\n\
    \        1: \u5145\u8DB3\u53EF\u80FD\u306A\u3089\u3070,\u305D\u306E\u5909\u6570\
    \u306E\u5272\u5F53\u3092\u4E0E\u3048\u308B (\u4E0D\u53EF\u80FD\u306A\u3068\u304D\
    \u306FNone).\n        2: \u5145\u8DB3\u4E0D\u80FD\u306E\u539F\u56E0\u3067\u3042\
    \u308B\u5909\u6570\u3092\u5168\u3066\u6319\u3052\u308B.\n        \"\"\"\n    \
    \    N=self.var_num\n        Group=[0]*(2*N)\n        Order=[]\n\n        for\
    \ s in range(2*N):\n            if Group[s]:continue\n\n            S=[s]\n  \
    \          Group[s]=-1\n\n            while S:\n                u=S.pop()\n  \
    \              for v in self.arc[u]:\n                    if Group[v]:continue\n\
    \                    Group[v]=-1\n                    S.append(u);S.append(v)\n\
    \                    break\n                else:\n                    Order.append(u)\n\
    \n        K=0\n        for s in Order[::-1]:\n            if Group[s]!=-1:continue\n\
    \n            S=[s]\n            Group[s]=K\n\n            while S:\n        \
    \        u=S.pop()\n                for v in self.rev[u]:\n                  \
    \  if Group[v]!=-1:continue\n\n                    Group[v]=K\n              \
    \      S.append(v)\n            K+=1\n\n        if Mode==0:\n            for i\
    \ in range(N):\n                if Group[2*i]==Group[2*i+1]:\n               \
    \     return False\n            return True\n        elif Mode==1:\n         \
    \   T=[0]*N\n            for i in range(N):\n                if Group[2*i]>Group[2*i+1]:\n\
    \                    T[i]=1\n                elif Group[2*i]==Group[2*i+1]:\n\
    \                    return None\n            return T\n        elif Mode==2:\n\
    \            return [i for i in range(self.var_num) if Group[2*i]==Group[2*i+1]]\n\
    \n    def solve(self):\n        return self.is_satisfy(1)\n"
  dependsOn: []
  isVerificationFile: false
  path: Two_SAT.py
  requiredBy: []
  timestamp: '2022-11-23 16:35:22+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test_verify/yosupo_library_checker/Math/Two_Sat.test.py
documentation_of: Two_SAT.py
layout: document
title: 2-SAT
---

## Outline

- 論理変数 $X_1, \dots, X_N$ 及び, これらの否定 $\lnot X_1, \dots, \lnot X_N$ をリテラルという.
- リテラル $V_1, \dots, V_K$ の論理和 $V_1 \lor \dots \lor V_K$ を節という.

SATISFIABILITY (SAT) とは, 次のような問題である.

> $2N$ 個のリテラルからなる論理式 $\varphi(X_1,\dots, X_N)$　に対して, これを $\mathbb{T}$ にするような $X_1, \dots, X_N$ への $\mathbb{T}, \mathbb{F}$ は存在するか?

また, SAT のうち, 次のような特別な場合には名前がついている.

- CNF-SAT : $\varphi(X_1, \dots, X_N)$ が節の論理積からなっているもの.
- 2-SAT : CNF-SAT のうち, 全ての節の中のリテラルが高々2つであるもの.

つまり, 2-SAT とは次のような問題である.

> リテラル全体の集合を $\mathcal{X}:=\\{X_1, \ldots, X_N, \lnot X_1, \dots, \lnot X_N\\}$ とする.
>
> $j=1,2, \dots, M$ に対して, $F_j, G_j \in \mathcal{X}$ とする.
>
> $$\varphi(X_1, \dots, X_N):=\bigwedge_{j=1}^M (F_j \lor G_j)$$
>
> と定めるとき, $\varphi(X_1, \dots, X_N)=\mathbb{T}$ となるような　$X_1, \dots, X_N$ への $\mathbb{T}, \mathbb{F}$ の割り当ては存在するか?

## Theory

$2N$ 頂点, $2M$ 辺の有向グラフ $D=(\mathcal{X}, A)$ を次のように定める.

- $A:=\\{\lnot F_j \Rightarrow G_j \mid 1 \leq j \leq M\\} \cup \\{\lnot G_j \Rightarrow F_j \mid 1 \leq j \leq M\\}$

このとき, 以下は同値である.

- 充足可能
- 全ての $i=1,2, \dots, N$ に対して, $X_i$ と $\lnot X_i$ は異なる強連結成分に属している.

$D$ における強連結成分を $C_1 \sqsupset C_2 \sqsupset \dots \sqsupset C_P$ とし $X \in \mathcal{X}$ が属している連結成分が $C_p$ であるとき, $\gamma(X)=p$ と書くことにする.

このとき, $i=1,2, \dots, N$ に対して,

$$X_i=\begin{cases}
\mathbb{T} & (\gamma(X_i)>\gamma(\lnot X_i)) \\
\mathbb{F} & (\gamma(X_i)<\gamma(\lnot X_i))
\end{cases}$$

が充足を可能にする一例になる.

※ $F \Rightarrow G$ への変換方法

|変換前|変換後|
|:---:|:---:|
|$X \Rightarrow Y$|$X \Rightarrow Y$|
|$X \lor Y$|$\lnot X \Rightarrow Y$|
|$\lnot (X \land Y)$|$X \Rightarrow \lnot Y$|
|$X = Y$|$(X \Rightarrow Y) \land (\lnot X \Rightarrow \lnot Y)$|
|$X \neq Y$|$(X \Rightarrow \lnot Y) \land (\lnot X \Rightarrow Y)$|
|$X$|$\lnot X \Rightarrow X$|
|$\lnot X$|$X \Rightarrow \lnot X$|

- $Y_1=Y_2= \dots =Y_K$
  - 以下の $K$ 個の含意の連言
    - $Y_1 \Rightarrow Y_2$
    - $Y_2 \Rightarrow Y_3$
    - $\vdots$
    - $Y_{K-1} \Rightarrow Y_K$
    - $Y_K \Rightarrow Y_1$
- $Y_1, \dots, Y_K$ のうち, 高々1つが $\mathbb{T}$.
  - $K$ 個の変数 $Z_1, \dots, Z_K$ を追加し, 以下の $(3K-2)$ 個の連言に帰着させる.
    - $Y_i \Rightarrow Z_i \quad (i=1,2, \dots, K)$
    - $Z_{i-1} \Rightarrow Z_i \quad (i=2,3, \dots, K)$
    - $\lnot (Y_i \land Z_{i-1}) \quad  (i=2,3, \dots, K)$

## Contents

---

### Constructer

```Python
T=Two_SAT(N=0)
```

- $N$ 変数の 2-SAT を定義する.
- **計算量** : $O(N)$ Time.

---

### add_variable

```Python
T.add_variable(k=0)
```

- $k$ 個の変数を新たに追加する.
- **計算量** : $O(k)$ Time.

---

### add_impfy

```Python
T.add_imply(i, j)
```

- 節 $X_i \Rightarrow X_j$ を追加する.

---

### add_or

```Python
T.add_or(i, j)
```

- 節 $X_i \lor X_j$ を追加する.

---

### add_nand

```Python
T.add_nand(i, j)
```

- 節 $\lnot (X_i \land X_j)$ を追加する.

---

### add_equivalent

```Python
T.add_equivalent(*I)
```

- $I=(I_0, \dots, I_{n-1})$ に対して, 以下の $n$ 個の節を追加する.
  - $X_{I_0} \Rightarrow X_{I_1}$
  - $X_{I_1} \Rightarrow X_{I_2}$
  - $\vdots$
  - $X_{I_{n-2}} \Rightarrow X_{I_{n-1}}$
  - $X_{I_{n-1}} \Rightarrow X_{I_0}$
- これは $X_{I_0}=\dots=X_{I_n}$ であることと同値である.

---

### add_not_equal

```Python
T.add_not_equal(i,j)
```

- 条件 $X_i \neq X_j$ を追加する.

---

### add_true

```Python
T.add_true(i)
```

- 条件 $X_i$ を追加する.

---

### add_false

```Python
T.add_false(i)
```

- 条件 $\lnot X_i$ を追加する.

---

### at_most_one

```Python
T.at_most_one(*I)
```

- 次の条件を追加する.
  - $X_i=\mathbb{T}$ となるような $i \in I$ は高々1つである (存在しなくても良い).

---

### is_satisfy

```Python
T.is_satisfy(mode)
```

- 2-SAT が充足可能かどうかを判定する.
- ${\rm mode}$ の値と返り値
  - ${\rm mode}=0$ : 充足可能ならば `True`, 充足不可能ならば `False`
  - ${\rm mode}=1$ : 充足可能ならば, 充足例を $0,1$ で表したリスト, 充足不可能ならば `None`
  - ${\rm mode}=2$ : $\gamma(X_i)=\gamma(\lnot X_i)$ となった $i$ 全てのリスト
- **計算量** : 変数の数を $N$, 節の数を $M$ としたとき, $O(N+M)$ Time.

---

### solve

```Python
T.solve()
```

- `T.is_satisfy(1)` と同等
