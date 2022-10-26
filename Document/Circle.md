---
title: Circle
documentation_of: //Geometric/Circle.py
---

## Theory

### 円の定義

点 $\mathrm{P}$ と正の実数 $r$ に対して, 点 $\mathrm{P}$ からの距離が $r$ であるような座標平面の部分集合を円という. つまり, この円を $\mathrm{C}$ とすると,

$$\mathrm{C}:=\\{\mathrm{X} \in \mathbb{R}^2 \mid \operatorname{dist}(\mathrm{P}, \mathrm{X})=r \\}$$

である. このとき, $\mathrm{P}$ を円 $\mathrm{C}$ の中心, $r$ を $\mathrm{C}$ の半径という.

### 2 円の位置関係

$\mathrm{C}$ は中心 $\mathrm{P}$ , 半径 $r$ の円, $\mathrm{D}$ は中心 $\mathrm{Q}$ , 半径 $s$ の円とする.

このとき, 2 円 $\mathrm{C}, \mathrm{D}$ の関係は以下 5 種類の場合分け出来る. なお, $d:=\operatorname{dist}(\mathrm{P}, \mathrm{Q})$ とする.

|関係|条件|共通接線の数|
|:--:|:--:|:--:|
|一方が他方の外部にある| $d \gt r+s$ |4 本|
|外接している| $d=r+s$ |3 本|
|交わっている| $\lvert r-s \rvert \lt d \lt r+s$ |2 本|
|内接している| $d=\lvert r-s \rvert$ |1 本|
|一方が他方を含んでいる| $d \lt \lvert r-s \rvert$ |0 本|

### 2 円の交差判定

2 円の位置関係における交わっているのみが交差している.

共有点判定の場合, 必要十分条件は $\lvert r-s \rvert \leq d \leq r+s$ になる.

### 2円の交点

$\mathrm{C}$ は中心 $\mathrm{P}$ , 半径 $r$ の円, $\mathrm{D}$ は中心 $\mathrm{Q}$ , 半径 $s$ の円とし, この 2 円は共通点を持つとする.

2 つの交点を $\mathrm{X}, \mathrm{X}'$ とする (内接, 外接の場合は $\mathrm{X}=\mathrm{X}'$ とする).

このとき, $\mathrm{X}, \mathrm{X}'$ は線分 $\mathrm{PQ}$ に関して線対称な位置にある. よって, $\mathrm{X}$ を求められれば十分である.

$\operatorname{dist}(\mathrm{P}, \mathrm{X})=r, \operatorname{dist}(\mathrm{Q}, \mathrm{X})=s$ である. また, $\mathrm{X}$ の線分 $\mathrm{PQ}$ への射影を $\mathrm{H}$ とし, $\theta:=\angle \mathrm{XPH}$ とすると,

直角三角形 $\mathrm{PXH}$ を考えることにより,

$$\mathrm{PH}=\mathrm{PX} \cos \theta=r \cos \theta =:x$$

である. そして, 三角形 $\mathrm{PQX}$ における第 II 余弦定理から

$$\cos \theta=\dfrac{r^2+d^2-s^2}{2dr}$$

である. よって, 直角三角形 $\mathrm{PXH}$　三平方の定理から

$$\mathrm{HX}=\sqrt{\mathrm{PX}^2-\mathrm{PH}^2}=\sqrt{r^2-\mathrm{PH}^2} =:y$$

である.

よって, $\overrightarrow{\mathrm{PQ}}$ の単位ベクトルを $\boldsymbol{e}$ , 単位法線ベクトルを $\boldsymbol{n}$ とすると,

$$\overrightarrow{\mathrm{OX}}=\overrightarrow{\mathrm{OP}}+\overrightarrow{\mathrm{PH}}+\overrightarrow{\mathrm{HX}}=\overrightarrow{\mathrm{OP}}+x \boldsymbol{e}+y \boldsymbol{n}$$

である.
