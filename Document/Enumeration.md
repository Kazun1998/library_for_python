---
title: Enumeration
documentation_of: //Enumeration.py
---

## Outline

組合せ論における基本計算を行う関数

## Theory

### 組み合わせを表す関数

(人は互いに区別がつき, ものは互いに区別がつかないとする.)

||意味合い|計算方法|
|:--:|:--:|:--:|
|$N!$|$N$ 人を1列に並べる方法|$N!=1 \times 2 \times \dots \times N$|
|$\dbinom{N}{r}$|$N$ 人から $r$ 人を選び出す方法 |$\dbinom{N}{r}=\dfrac{N!}{r!(N-r)!}$|
|${}_N P_r$|$N$ 人から $r$ 人を選び出し, その $r$ 人を一列に並べる方法|${}_N P_r=\dfrac{N!}{(N-r)!}$|
|${}_N H_r$|$N$ 個のものを $r$ 人に配る方法|${}_N H_r=\dbinom{N+r-1}{r}$ <br> (ただし, $_0H_0=1$ とする.)|
|$\dbinom{N}{r_1, r_2, \dots, r_m}$ <br> $(N=r_1+\dots+r_m)$|$N$ 人を $r_1$ 人の $1$ 班, $\cdots$, $r_m$ 人の $m$ 班に分ける方法|$\dbinom{N}{r_1,r_2, \dots, r_m}=\dfrac{N!}{r_1!r_2! \dots r_m!}$|
|$C_n$<br>(カタラン数)|$N$ 個の `(` と $N$ 個の `)` からなる文字列が正しい文字列になる文字列の数 (など) |$C_N=\dfrac{(2N)!}{(N+1)!N!}$|

### 組み合わせに関する定理

#### Lucas の定理

$p$ を素数とする. $N,r$ の $p$ 進表記をそれぞれ $(N_i)\_{i=0}^{\infty}, (r_i)\_{i=0}^\infty$ としたとき,

$$\dbinom{N}{r} \equiv \prod_{i=0}^\infty \dbinom{N_i}{r_i} \pmod{p}$$

が成り立つ.
