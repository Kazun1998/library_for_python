---
title: Circle
documentation_of: //Geometric/Circle.py
---

## Theory

### 円の定義

点 $\mathrm{P}$ と正の実数 $r$ に対して, 点 $\mathrm{P}$ からの距離が $r$ であるような座標平面の部分集合を円という. つまり, この円を $\mathrm{C}$ とすると,

$$\mathrm{C}:=\{\mathrm{X} \in \mathbb{R}^2 \mid \operatorname{dist}(\mathrm{P}, \mathrm{X})=r \}$$

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

### 直線と円の位置関係

$\mathrm{C}$ は中心 $\mathrm{P}$, 半径 $r$ の円とし, $\ell$ は直線とする. このとき, $\mathrm{C}$ と $\ell$ の関係は次のようにして 3 種類に分けられる. なお, $\mathrm{P}$ と $\ell$ との距離を $d$ とする.

|関係|条件|
|:--:|:--:|
|共有点なし| $d \gt r$ |
|接している| $d=r$ |
|交わっている| $d \lt r$ |

### 直線と円の交差判定

$\mathrm{C}$ は中心 $\mathrm{P}$, 半径 $r$ の円とし, $\ell$ は直線とする. また, $\mathrm{C}$ と $\ell$ は共有点を持つとする.

共有点を $\mathrm{X}, \mathrm{X}'$ (接する場合は $\mathrm{X}=\mathrm{X}'$ とする) とする.

このとき, $\mathrm{P}$ の $\ell$ への射影を $\mathrm{H}$ とすると, $\mathrm{X}, \mathrm{X}'$ は直線 $\mathrm{PH}$ に関して線対称である.

直角三角形 $\mathrm{PHX}$ に関する三平方の定理より

$$\mathrm{PX}^2=\mathrm{PH}^2+\mathrm{XH}^2$$

である. $\mathrm{X}$ は円 $\mathrm{C}$ 上の点であるから, $\mathrm{PX}=r$ である. よって,

$$\mathrm{XH}=\sqrt{\mathrm{PX}^2-\mathrm{PH}^2}=\sqrt{r^2-\mathrm{PH}^2}=:x$$

となる.

よって, $\ell$ の単位方向ベクトルを $\boldsymbol{e}$ とおくと,

$$\overrightarrow{\mathrm{OX}}=\overrightarrow{\mathrm{OH}}+\overrightarrow{\mathrm{HX}}=\overrightarrow{\mathrm{OH}}+x \boldsymbol{e}$$

である.

そして, $\mathrm{X}'$ は直線 $\mathrm{PH}$ に関して $\mathrm{X}$ と線対称であったから,

$$\overrightarrow{\mathrm{OX}'}=\overrightarrow{\mathrm{OH}}-x \boldsymbol{e}$$

である.

以上から, 交点は

$$\overrightarrow{\mathrm{OH}} \pm x \boldsymbol{e}$$

であるとわかった.

### 直線と円の交点

### 2 円の交差判定

2 円の位置関係における交わっているのみが交差している.

共有点判定の場合, 必要十分条件は $\lvert r-s \rvert \leq d \leq r+s$ になる.

### 2円の交点

$\mathrm{C}$ は中心 $\mathrm{P}$, 半径 $r$ の円, $\mathrm{D}$ は中心 $\mathrm{Q}$, 半径 $s$ の円とし, この 2 円は共通点を持つとする.

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

である. また, $\mathrm{X}'$ は線分 $\mathrm{PQ}$ に関して $\mathrm{X}$ の線対称な位置にあり, $\boldsymbol{n}$ は $\boldsymbol{e}$ の単位法線ベクトルであったので,

$$\overrightarrow{\mathrm{OX}'}=\overrightarrow{\mathrm{OP}}+x \boldsymbol{e}-y \boldsymbol{n}$$

である.

以上から, 交点は

$$\overrightarrow{\mathrm{OP}}+x \boldsymbol{e} \pm y \boldsymbol{n}$$

であることがわかった.

### 円の接線 (円上の点)

$\mathrm{C}$ は $\mathrm{P}$ を中心とする円であるとする. 円 $\mathrm{C}$ 上の点 $\mathrm{A}$ を通る円 $\mathrm{C}$ の接線 $\ell$ は次のようにして求められる.

$\mathrm{A} \in \ell$ であることが確定しているので, $\ell$ 上の点をもう一つ求められれば良い.

$\boldsymbol{v}:=\overrightarrow{\mathrm{PA}}$ とし, $\boldsymbol{v}'$ を $\boldsymbol{v}$ の法線ベクトルとすると, $\mathrm{B}:=\mathrm{A}+\boldsymbol{v}'$ において, $\mathrm{B} \in \ell$ である.

よって, $\ell$ は $\mathrm{A}, \mathrm{B}$ を通る直線である.

### 円の接線 (円外の点)

$\mathrm{C}$ は $\mathrm{P}$ を中心とする半径 $r$ の円であるとする. 円 $\mathrm{C}$ の外にある点 $\mathrm{A}$ を通る円 $\mathrm{C}$ の接線を求める.

$d:=\operatorname{dist}(\mathrm{P}, \mathrm{A})$ とする. 円 $\mathrm{C}$ の接点を $\mathrm{X}, \mathrm{X}'$ とする. この $\mathrm{X}, \mathrm{X}'$ は直線 $\mathrm{AP}$ に関して線対称の関係にある.

$\mathrm{X}, \mathrm{A}$ は円 $\mathrm{C}$ 上の接線で, $\mathrm{X}$ が接点になるので, $\angle \mathrm{PXA}=90^\circ$ である. よって, 直角三角形 $\mathrm{PXA}$ における三平方の定理により,

$$\mathrm{PA}^2=\mathrm{PX}^2+\mathrm{AX}^2$$

であるから, $d:=\operatorname{dist}(\mathrm{P}, \mathrm{A})$ 及び, $\mathrm{X}$ は $\mathrm{C}$ 上の点だったので,

$$\mathrm{AX}=\sqrt{\mathrm{PA}^2-\mathrm{PX}^2}=\sqrt{d^2-r^2}:=x$$

である. また, $\theta:=\angle \mathrm{PAX}$ とすると,

$$\theta=\operatorname{Sin}^{-1} \dfrac{\mathrm{PX}}{\mathrm{PA}}=\operatorname{Sin}^{-1} \dfrac{r}{d}$$

である.

従って, $\overrightarrow{\mathrm{AP}}$ の単位ベクトルを $\boldsymbol{e}$ とし, $\boldsymbol{e}$ を $\alpha$ だけ回転させたベクトルを $\boldsymbol{e}_\alpha$ とすると,

$$\overrightarrow{\mathrm{OX}}=\overrightarrow{\mathrm{OA}}+\overrightarrow{\mathrm{AX}}=\overrightarrow{\mathrm{OA}}+x\boldsymbol{e}_{\theta}$$

である. これにより, 接線の一つとして $\mathrm{A}, \mathrm{X}$ を通る直線となる.

また, $\mathrm{X}'$ は直線 $\mathrm{AP}$ に関して $\mathrm{X}$ と線対称の位置であるから,

$$\overrightarrow{\mathrm{OX}'}=\overrightarrow{\mathrm{OA}}+x\boldsymbol{e}_{-\theta}$$

である.
