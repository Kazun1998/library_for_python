---
title: Point
documentation_of: //Geometric/Point.py
---

## Outline

座標平面 $\mathbb{R}^2$ 上の図形における計算を行う.

ただし, このライブラリ及び, ドキュメント内では座標平面内の点 ${\rm A}=(x,y)$ と2次元実ベクトル $\bm{a}=(x,y)$ を同一視する.

また, 2次元ベクトル $\bm{a}=(a_x, a_y), \bm{b}=(b_x, b_y)$ に対する外積 $\bm{a} \times \bm{b}$ を
$$\bm{a} \times \bm{b}:=\det (\bm{a}, \bm{b})=a_x b_y-b_x a_y$$
とする.

## Theory

### 3点の進行方向

相異なる3点 ${\rm A}, {\rm B}, {\rm C}$ に対して, ${\rm A} \to {\rm B} \to {\rm C}$ がどのようにして進むことになるかを考える.

$\bm{u}:=\overrightarrow{{\rm AB}}, \bm{v}:=\overrightarrow{{\rm AC}}$ とする.

- $\bm{u} \times \bm{v}>0$ ならば, 左折 (反時計回り) である.
- $\bm{u} \times \bm{v}<0$ ならば 右折 (時計回り) である.
- $\bm{u} \times \bm{v}=0$ のとき, 3点は同一直線上の3点である. この場合, どの順にならんでいるかを調べる.
  - $\overrightarrow{{\rm AB}} \cdot \overrightarrow{{\rm AC}}<0$ ならば, 線分 ${\rm A}$ は線分 ${\rm BC}$ 上の点である.
  - $\overrightarrow{{\rm BA}} \cdot \overrightarrow{{\rm BC}}<0$ ならば, 線分 ${\rm B}$ は線分 ${\rm AC}$ 上の点である.
  - これ以外の場合 (この場合, $\overrightarrow{{\rm CA}} \cdot \overrightarrow{{\rm CB}}<0$ になる) ならば, 線分 ${\rm C}$ は線分 ${\rm AB}$ 上の点である.
