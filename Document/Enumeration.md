---
title: Enumeration
documentation_of: //Enumeration.py
---

## Outline

組合せ論における基本計算を行う関数

## Theory

### 組み合わせを表す関数

||意味合い|計算方法|
|:--:|:--:|:--:|
|$N!$||$N!=1 \times 2 \times \dots \times N$|
|$\dbinom{N}{r}$||$\dbinom{N}{r}=\dfrac{N!}{r!(N-r)!}$|
|${}_n P_r$||${}\_n P_r=\dfrac{N!}{(N-r)!}$|
|${}_n H_r$||${}\_n H_r=\dbinom{N+r-1}{r}$ <br> (ただし, $_0H_0=1$ とする.)|
|$\dbinom{N}{r_1, r_2, \dots, r_m}$ <br> $(N=r_1+\dots+r_m)$||$\dbinom{N}{r_1,r_2, \dots, r_m}=\dfrac{N!}{r_1!r_2! \dots r_m!}$|

### 組み合わせに関する定理

#### Lucas の定理

$N,r$ の $p$ 進表記をそれぞれ $(N_i)_{i=0}^{\infty}, (r_i)_{i=0}^\infty$ としたとき,

$$\dbinom{N}{r}=\prod_{i=0}^\infty \dbinom{N_i}{r_i}$$

が成り立つ.