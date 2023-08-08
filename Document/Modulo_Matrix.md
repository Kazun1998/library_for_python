---
title: Modulo_Matrix
documentation_of: //Modulo_Matrix/Modulo_Matrix.py
---

## Outline

$m$ を素数とする. $\mathbb{Z}/m \mathbb{Z}$ を要素に持つ行列に対する様々な計算を行うクラス, 関数.

ただし, たいていの場合は $m$ が素数であることを要求する. これにより, $\mathbb{Z}/m \mathbb{Z}$ は体になる.

以降, $p$ が素数の時には体 $\mathbb{Z}/p \mathbb{Z}$ を $\mathbb{F}_p$ と書く.

## Theory

### 逆行列

行列に対する次の操作を行基本変形という.

* $i$ 行目と $j$ 行目を交換する $(i \neq j)$
* $i$ 行目を $\alpha$ 倍 $(\alpha \in \mathbb{F}_p^\times)$ する.
* $i$ 行目に $j$ 行目の $\beta$ 倍 $(\beta \in \mathbb{F}_p)$ を加える.

次のような行列を基本行列という.

* $P_{N,i,j}:=(\bm{e}_1, \dots, \bm{e}_{i-1}, \bm{e}_j, \bm{e}_{i+1}, \dots, \bm{e}_{j-1}, \bm{e}_i, \bm{e}_{j+1}, \dots \bm{e}_N)$
* $Q_{N,i,\alpha}:=(\bm{e}_1, \dots, \bm{e}_{i-1}, \alpha \bm{e}_i, \bm{e}_{i+1}, \dots, \bm{e}_N)$
* $R_{N,i,j,\beta}:=(\bm{e}_1, \dots, \bm{e}_{j-1}, \bm{e}_j+\beta \bm{e}_i, \bm{e}_{j+1}, \dots \bm{e}_N)$

ここで, $A \in M_N(\mathbb{F}_p)$ に対して,

* $P_{N,i,j}A$ は $A$ の第 $i$ 行と第 $j$ 行を入れ替えた行列
* $Q_{N,i,\alpha} A$ は $A$ の第 $i$ 行を $\alpha$ 倍した行列
* $R_{N,i,j,\beta} A$ は $A$ の第 $i$ 行に第 $j$ 行の $\beta$ 倍を加えた行列

になり, 左から基本行列を掛けることと, 行基本変形を行うことが1対1に対応する.

ここで, 任意の $A \in M_N(\mathbb{F}_p)$ に対して, 基本行列 $S_1, \dots, S_L$ と $0 \leq K \leq N$ が存在して,

$$S_L S_{L-1} \dots S_1 A=(\bm{e}_1, \dots, \bm{e}_K, \bm{0}, \dots \bm{0})$$

となる. ここで, $K$ については $S_1, \dots, S_L$ の取り方に依らず, $A$ のみによって定まる. よって, この $K$ のことを行列 $A$ の Rank (階数) といい, $\operatorname{rank} A$ と表す.

そして, $A \in M_N(\mathbb{F}_p)$ に対して, 以下は同値になる.

* $A \in M_N(\mathbb{F}_p)^\times$
* $\operatorname{rank} A=N$

つまり, $A \in M_N(\mathbb{F}_p)^\times$ のとき,

$$S_L S_{L-1} \dots S_1 A=(\bm{e}_1, \dots, \bm{e}_N)=I_N$$

である. $S:=_L S_{L-1} \dots S_1$ とすると, $SA=I_N$ となる. このとき, $A^{-1}=S$ であることも導ける.

### 行列式

行列式 $\det: M_N(\mathbb{F}_p) \to \mathbb{F}_p$ を以下で定義する. ただし,$\mathfrak{S}_N$ で $N$ 次対称群を表すとする.

$$ \det A:=\sum_{\sigma \in \mathfrak{S}_N} \operatorname{sgn} \sigma \prod_{i=1}^N A_{i, \sigma(i)}$$

この行列式は次のような性質を満たす.

* 各行に対する多重線形性
* 交代性
* $\det I_N=1$

実はこの3条件を満たすような写像は行列式のみである.

また, 行列式は積に関して準同型を成す. つまり, $A,B \in M_N(\mathbb{F}_p)$ に対して,

$$ \det (AB)=(\det A)(\det B)$$

となる.

このとき, 逆行列の求め方と同様にして, 行基本行列 $S_1, \dots, S_L$ と上三角行列が存在して,

$$S_1 S_2 \dots S_K A=U$$

となる.

そして,

* $\det P_{i,j}=-1$
* $\det Q_{i,\alpha}=\alpha$
* $\det R_{i,j,\beta}=1$
* $\det U$ は $N$ 個の対角成分の積

である.

これによって,

$$\det A=\dfrac{\det U}{(\det S_1) \dots (\det S_K)}$$

として求められることができる. 計算量は $O(N^3)$ である.
