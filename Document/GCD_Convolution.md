---
title: Gcd Convolution
documentation_of: //Convolution/GCD_Convolution.py
---

## Outline

長さ $N$ の数列, $A=(A_i)_{1 \leq i \leq N}, B=(B_j)_{1 \leq j \leq N}$ に対し, $A,B$ の Gcd Convolution $A \oplus B$ を

$$A \oplus B:=\left(\sum_{\substack{1 \leq i,j \leq N \\ \gcd(i,j)=k}} A_i B_j \right)_{1 \leq k \leq N}$$

と定義する.

## Remark

実装において, 長さが $N$ の数列を使いたい場合, プログラム言語の仕様上, 初項が第 $0$ 項になるため, 長さ $(N+1)$ のリストを入力しなければならない.

ただし, 第 $0$ 項は無視して計算される.
