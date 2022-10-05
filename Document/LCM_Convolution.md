---
title: Lcm Convolution
documentation_of: //Convolution/LCM_Convolution.py
---

## Outline

数列 $A=(A_i)_{1 \leq i}, B=(B_j)_{1 \leq j}$ に対し, $A,B$ の Lcm Convolution $A \oplus B$ を

$$A \oplus B:=\left(\sum_{\substack{1 \leq i,j \\ \operatorname{lcm}(i,j)=k}} A_i B_j \right)_{1 \leq k}$$

と定義する.

## Remark

実装において, 長さが $N$ の数列を使いたい場合, プログラム言語の仕様上, 初項が第 $0$ 項になるため, 長さ $(N+1)$ のリストを入力しなければならない.

ただし, 第 $0$ 項は無視して計算される.

また, Gcd Convolution と違い, $1 \leq i \leq N, 1 \leq j \leq M$ のとき, $\operatorname{lcm}(i,j)$ が最大で $NM$ 程度になるので, $L$ で長さの指定をしなければならない.
