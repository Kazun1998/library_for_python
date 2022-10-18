---
title: 2-SAT
documentation_of: //Two-SAT.py
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

> リテラル全体の集合を $\mathcal{X}:=\{X_1, \ldots, X_N, \lnot X_1, \dots, \lnot X_N\}$ とする.
>
> $j=1,2, \dots, M$ に対して, $F_j, G_j \in \mathcal{X}$ とする.
>
> $$\varphi(X_1, \dots, X_N):=\bigwedge_{j=1}^M (F_j \lor G_j)$$
>
> と定めるとき, $\varphi(X_1, \dots, X_N)=\mathbb{T}$ となるような　$X_1, \dots, X_N$ への $\mathbb{T}, \mathbb{F}$ の割り当ては存在するか?

## Theory

$2N$ 頂点, $2M$ 辺の有向グラフ $D=(\mathcal{X}, A)$ を次のように定める.

- $A:=\{\lnot F_j \Rightarrow G_j \mid 1 \leq j \leq M\} \cup \{\lnot G_j \Rightarrow F_j \mid 1 \leq j \leq M\}$

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

- $I=[I_0, \dots, I_{n-1}]$ に対して, 以下の $n$ 個の節を追加する.
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
