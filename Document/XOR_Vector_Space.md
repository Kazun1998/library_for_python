---
title: XOR Vector Space
documentation_of: //XOR_Vector_Space.py
---

## Outline

演算 XOR によって作られるベクトル空間に関する計算を行う.

## Theory

非負整数全体の集合を $\mathbb{N}$ とする. このとき, $\mathbb{N}$ は次のようにして体 $\mathbb{F}_2:=\mathbb{Z}/2\mathbb{Z}$ 上のベクトル空間とみなすことができる.

* $x,y \in \mathbb{N}$ に対して, 和 $x \oplus y$ を $x,y$ の XOR とする.
* $x \in \mathbb{N}$ に対して, スカラー倍をそれぞれ $[0]_2 x:=0, [1]_2x:=x$ と定義する.

なお, 実用的には整数 $K$ に対して, $V_K$ を $0$ 以上 $2^K$ 未満の非負整数全体の集合とすると, $V_K$ は $\mathbb{N}$ の部分空間になり, $V_K$ を全体として扱うことになる.

ここで, 体が $\mathbb{F}_2$ という位数 $2$ の体であることから, $\# V_K=2^{\dim V_K}$ が成り立つ.

## Contents

### Constructer

```Python
V=XOR_Vector_Space()
```

- XOR ベクトル空間を生成する.

---
