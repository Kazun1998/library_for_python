---
title: Point
documentation_of: //Geometric/Point.py
---

## Outline

座標平面 $\mathbb{R}^2$ 上の図形における計算を行う.

ただし, このライブラリ及び, ドキュメント内では座標平面内の点 $\mathrm{A}=(x,y)$ と2次元実ベクトル $\bm{a}=(x,y)$ を同一視する.

また, 2次元ベクトル $\bm{a}=(a_x, a_y), \bm{b}=(b_x, b_y)$ に対する外積 $\bm{a} \times \bm{b}$ を
$$\bm{a} \times \bm{b}:=\det (\bm{a}, \bm{b})=a_x b_y-b_x a_y$$
とする.

## Theory

### 3点の進行方向

相異なる3点 $\mathrm{A}, \mathrm{B}, \mathrm{C}$ に対して, $\mathrm{A} \to \mathrm{B} \to \mathrm{C}$ がどのようにして進むことになるかを考える.

$\bm{u}:=\overrightarrow{\mathrm{AB}}, \bm{v}:=\overrightarrow{\mathrm{AC}}$ とする.

- $\bm{u} \times \bm{v}>0$ ならば, 左折 (反時計回り) である.
- $\bm{u} \times \bm{v}<0$ ならば 右折 (時計回り) である.
- $\bm{u} \times \bm{v}=0$ のとき, 3点は同一直線上の3点である. この場合, どの順にならんでいるかを調べる.
  - $\overrightarrow{\mathrm{AB}} \cdot \overrightarrow{\mathrm{AC}}<0$ ならば, 線分 $\mathrm{A}$ は線分 $\mathrm{BC}$ 上の点である.
  - $\overrightarrow{\mathrm{BA}} \cdot \overrightarrow{\mathrm{BC}}<0$ ならば, 線分 $\mathrm{B}$ は線分 $\mathrm{AC}$ 上の点である.
  - これ以外の場合 (この場合, $\overrightarrow{\mathrm{CA}} \cdot \overrightarrow{\mathrm{CB}}<0$ になる) ならば, 線分 $\mathrm{C}$ は線分 $\mathrm{AB}$ 上の点である.
