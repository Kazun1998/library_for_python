---
title: Line
documentation_of: //Geometric/Line.py
---

## Theory

### 線分, 半直線, 直線の定義

$\mathrm{A}, \mathrm{B}$ を相異なる2点とする.

* $\mathrm{A}, \mathrm{B}$ を端点とする線分 (Segment) $s$ は以下のようにして定義される. $$s:=\\{t \mathrm{A}+(1-t) \mathrm{B} \mid 0 \leq t \leq 1\\}$$
* $\mathrm{A}$ を端点とし, $\mathrm{B}$ を通る半直線 (Ray) $r$ は以下のようにして定義される. $$r:=\\{t \mathrm{A}+(1-t) \mathrm{B} \mid 0 \leq t\\}$$
* $\mathrm{A}, \mathrm{B}$ を通る直線 (Line) $\ell$ は以下のようにして定義される. $$\ell:=\\{t \mathrm{A}+(1-t) \mathrm{B} \mid t \in \mathbb{R} \\}$$

どの場合でも $\overrightarrow{\mathrm{AB}}$ が方向ベクトルになる.

### 線分, 半直線, 直線上の点かの判定

$\mathrm{A}, \mathrm{B}$ を相異なる2点とする. $\mathrm{P}$ が線分, 半直線, 直線上の点であるかの判定をする. これは3点の位置関係を利用することが出来る.

* $s$ を $\mathrm{A}, \mathrm{B}$ を端点とする線分とする. $\mathrm{P}$ が $s$ 上の点であることの判定は3点の位置関係でそのまま判定できる.
* $r$ を $\mathrm{A}$ を端点とし, $\mathrm{B}$ を通る半直線とする. $\mathrm{P}$ が $r$ 上の点であることの必要十分条件は以下のうちのどちらか一方が成り立つことである.
  * $\mathrm{P}$ が線分 $\mathrm{AB}$ 上の点である.
  * $\mathrm{B}$ が線分 $\mathrm{AP}$ 上の点である.
* $\ell$ を $\mathrm{A}, \mathrm{B}$ を通る直線とする. $\mathrm{P}$ が $\ell$ 上の点であることの必要十分条件は以下である.
  * $\mathrm{P}$ が線分 $\mathrm{AB}$ 上の点である.
  * $\mathrm{B}$ が線分 $\mathrm{AP}$ 上の点である.
  * $\mathrm{A}$ が線分 $\mathrm{BP}$ 上の点である.

なお, $\mathrm{P}$ が $\ell$ 上の点の判定についてはよくみると $\mathrm{iSP}$ が $\pm 1$ でないことと同値であるから, これは以下のように帰着である.

$$\mathrm{P} \in \ell \iff \overrightarrow{\mathrm{PA}} \times \overrightarrow{\mathrm{PB}}=0$$

### 2直線 (線分) の関係性

直線 (線分) $\ell ,m$ をそれぞれ以下のようにする.

* $\ell$ : 点 $\mathrm{A}, \mathrm{B}$ を通る直線 (を端点とする線分).
* $m$ : 点 $\mathrm{C}, \mathrm{D}$ を通る直線 (を端点とする線分).

このとき, 以下が成り立つ.

* $l,m$ が平行 (または一致) $\iff \overrightarrow{\mathrm{AB}} \times \overrightarrow{\mathrm{CD}}=0$
* $l,m$ が (共有点を持つならば) 直交 $\iff \overrightarrow{\mathrm{AB}} \cdot \overrightarrow{\mathrm{CD}}=0$

### 線分と線分の交差判定

### 直線と直線の交差判定

2つの直線 $\ell, m$ はそれぞれ次のようになっているとする.

* $\ell$ : 点 $\mathrm{A}$ を通り, 方向ベクトルが $\bm{u}$ である.
* $m$ : 点 $\mathrm{B}$ を通り, 方向ベクトルが $\bm{v}$ であるとする.

このとき, $\ell, m$ の関係は交差, 平行 (かつ 非一致), 一致のどれかである.

* 一致 $\iff \bm{u} \times \bm{v}=0$ かつ $\mathrm{B} \in \ell$
* 平行かつ不一致 $\iff \bm{u} \times \bm{v}=0$ かつ $B \not \in \ell$
* 交差 $\iff \bm{u} \times \bm{v} \neq 0$

### 直線と直線の交点

以下, 2つの直線 $\ell, m$ 交差するとする. このとき, 交点は唯一存在する.

このことから, 線分と半直線の交点のような場合でも交点が存在する場合, 両者を直線に拡張して直線同士の交点を求めれば, その点がそのまま元問題の交点にもなる.

直線 $\mathrm{H}$ は次のようにして求められる.

$\ell,m$ をそれぞれ次のようにする.

* $\ell$ : 2点 $\mathrm{A}, \mathrm{B}$ を通る直線.
* $m$ : 2点 $\mathrm{C}, \mathrm{D}$ を通る直線.

このとき, 次のようにして点 $\mathrm{E}, \mathrm{F}$ を定める.

* $\mathrm{E}$ : 次の2つの直線の交点
  * $\mathrm{A}$ を通り, $m$ と平行な直線
  * $\mathrm{C}$ を通り, $\overrightarrow{\mathrm{AD}}$ と平行な直線
* $\mathrm{F}$ : 次の2つの直線の交点
  * $\mathrm{B}$ を通り, $m$ と平行な直線
  * $\mathrm{E}$ を通り, $l$ と平行な直線

このとき, $\mathrm{CE} \parallel \mathrm{AD}, \mathrm{AE} \parallel \mathrm{CD}$ であるから, 四角形 $\mathrm{AECD}$ は平行四辺形である. 同様にして, $\mathrm{AE} \parallel \mathrm{BF}, \mathrm{EF} \parallel \mathrm{AB}$ であるから, 四角形 $\mathrm{AEFB}$ も平行四辺形である.

よって, $\overrightarrow{\mathrm{AE}}=\overrightarrow{\mathrm{DC}}, \overrightarrow{\mathrm{AE}}=\overrightarrow{\mathrm{BF}}$ が導ける.

また, 平行四辺形 $\mathrm{AECD}, \mathrm{AEFB}$ は辺 $\mathrm{AE}$ を共有しているので, この2つの平行四辺形の面積を $S,T$ とすると, ある線分 $\mathrm{AB}$ 上の点 $\mathrm{G}$ が存在して,

$$S:T=\mathrm{AG} : \mathrm{GB} \cdots (\spadesuit) $$

が成り立つ. そして, 3つの直線 $\mathrm{AE}, \mathrm{CD} (=m), \mathrm{BF}$ は互いに平行であるから, この $\mathrm{G}$ は直線 $\mathrm{CD} (=m)$ 上の点でもある.

よって, この点 $\mathrm{G}$ が直線 $l,m$ の交点であり,$(\spadesuit)$ および, $S,T$ が平行四辺形の面積であることから, $k$ を

$$k:=\dfrac{S}{T}=\dfrac{\overrightarrow{\mathrm{AE}} \times \overrightarrow{\mathrm{AD}}}{\overrightarrow{\mathrm{AE}} \times \overrightarrow{\mathrm{AB}}}=\dfrac{\overrightarrow{\mathrm{DC}} \times \overrightarrow{\mathrm{AD}}}{\overrightarrow{\mathrm{DC}} \times \overrightarrow{\mathrm{AB}}}=\dfrac{\overrightarrow{\mathrm{AD}} \times \overrightarrow{\mathrm{CD}}}{\overrightarrow{\mathrm{AB}} \times \overrightarrow{\mathrm{CD}}}$$

とすると, 点 $\mathrm{G}$ は線分 $\mathrm{AB}$ を $k:(1-k)$ に内分する点である.

### 射影

点 $\mathrm{P}$ の直線 $\ell$ への射影 $\mathrm{H}$ を求める. $\ell$ は2点 $\mathrm{A}, \mathrm{B}$ を通る直線とする. $\theta:=\angle \mathrm{PAB}$ とする. このとき,

$$\overrightarrow{\mathrm{AP}} \cdot \overrightarrow{\mathrm{AB}}=\left \lvert \overrightarrow{\mathrm{AP}} \right \rvert \left \lvert \overrightarrow{\mathrm{AB}} \right \rvert \cos \theta$$

である.

ここで, $\mathrm{H}$ は $\mathrm{P}$ の $\ell$ への射影であるから, $\mathrm{PH}$ と $\ell$ は直交する. そして, $\mathrm{H}$ は $\ell$ 上の点であるから, 直角三角形 $\mathrm{AHP}$ を考えることにより,

$$\left \lvert \overrightarrow{\mathrm{AH}} \right \rvert=\left \lvert \overrightarrow{\mathrm{AP}} \right \rvert \cos \theta$$

となる.

以上から,

$$\left \lvert \overrightarrow{\mathrm{AH}} \right \rvert=\dfrac{\overrightarrow{\mathrm{AP}} \cdot \overrightarrow{\mathrm{AB}}}{\left \lvert \overrightarrow{\mathrm{AB}} \right \rvert}$$

となり,

$$\overrightarrow{\mathrm{OH}}=\overrightarrow{\mathrm{OA}}+\dfrac{\left \lvert \overrightarrow{\mathrm{AH}}\right \rvert}{\left \lvert \overrightarrow{\mathrm{AB}}\right \rvert} \overrightarrow{\mathrm{AB}}=\overrightarrow{\mathrm{OA}}+\dfrac{\overrightarrow{\mathrm{AP}} \cdot \overrightarrow{\mathrm{AB}}}{\left \lvert \overrightarrow{\mathrm{AB}} \right \rvert^2}\overrightarrow{\mathrm{AB}}$$

が得られる.

### 反射

点 $\mathrm{P}$ を直線 $\ell$ に関して対称移動させた点を $\mathrm{P}'$  とする. このとき, $\mathrm{P}'$ は $\mathrm{P}$ の $\ell$ への射影を $\mathrm{H}$ とすると,

$$\overrightarrow{\mathrm{OP}'}=\overrightarrow{\mathrm{OP}}+2\overrightarrow{\mathrm{PH}}$$

を満たす.
