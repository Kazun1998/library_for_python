---
title: Line
documentation_of: //Geometric/Line.py
---

## Theory

### 線分, 半直線, 直線の定義

${\rm A}, {\rm B}$ を相異なる2点とする.

* ${\rm A}, {\rm B}$ を端点とする線分 (Segment) $s$ は以下のようにして定義される. $$s:=\\{t {\rm A}+(1-t) {\rm B} \mid 0 \leq t \leq 1\\}$$
* ${\rm A}$ を端点とし, ${\rm B}$ を通る半直線 (Ray) $r$ は以下のようにして定義される. $$r:=\\{t {\rm A}+(1-t) {\rm B} \mid 0 \leq t\\}$$
* ${\rm A}, {\rm B}$ を通る直線 (Line) $\ell$ は以下のようにして定義される. $$\ell:=\\{t {\rm A}+(1-t) {\rm B} \mid t \in \mathbb{R} \\}$$

どの場合でも $\overrightarrow{{\rm AB}}$ が方向ベクトルになる.

### 線分, 半直線, 直線上の点かの判定

${\rm A}, {\rm B}$ を相異なる2点とする. ${\rm P}$ が線分, 半直線, 直線上の点であるかの判定をする. これは3点の位置関係を利用することが出来る.

* $s$ を ${\rm A}, {\rm B}$ を端点とする線分とする. ${\rm P}$ が $s$ 上の点であることの判定は3点の位置関係でそのまま判定できる.
* $r$ を ${\rm A}$ を端点とし, ${\rm B}$ を通る半直線とする. ${\rm P}$ が $r$ 上の点であることの必要十分条件は以下のうちのどちらか一方が成り立つことである.
  * ${\rm P}$ が線分 ${\rm AB}$ 上の点である.
  * ${\rm B}$ が線分 ${\rm AP}$ 上の点である.
* $\ell$ を ${\rm A}, {\rm B}$ を通る直線とする. ${\rm P}$ が $\ell$ 上の点であることの必要十分条件は以下である.
  * ${\rm P}$ が線分 ${\rm AB}$ 上の点である.
  * ${\rm B}$ が線分 ${\rm AP}$ 上の点である.
  * ${\rm A}$ が線分 ${\rm BP}$ 上の点である.

なお, ${\rm P}$ が $\ell$ 上の点の判定についてはよくみると ${\rm iSP}$ が $\pm 1$ でないことと同値であるから, これは以下のように帰着である.

$${\rm P} \in \ell \iff \overrightarrow{{\rm PA}} \times \overrightarrow{{\rm PB}}=0$$

### 2直線 (線分) の関係性

直線 (線分) $\ell ,m$ をそれぞれ以下のようにする.

* $\ell$ : 点 ${\rm A}, {\rm B}$ を通る直線 (を端点とする線分).
* $m$ : 点 ${\rm C}, {\rm D}$ を通る直線 (を端点とする線分).

このとき, 以下が成り立つ.

* $l,m$ が平行 (または一致) $\iff \overrightarrow{{\rm AB}} \times \overrightarrow{{\rm CD}}=0$
* $l,m$ が (共有点を持つならば) 直交 $\iff \overrightarrow{{\rm AB}} \cdot \overrightarrow{{\rm CD}}=0$

### 線分と線分の交差判定

### 直線と直線の交差判定

2つの直線 $\ell, m$ はそれぞれ次のようになっているとする.

* $\ell$ : 点 ${\rm A}$ を通り, 方向ベクトルが $\bm{u}$ である.
* $m$ : 点 ${\rm B}$ を通り, 方向ベクトルが $\bm{v}$ であるとする.

このとき, $\ell, m$ の関係は交差, 平行 (かつ 非一致), 一致のどれかである.

* 一致 $\iff \bm{u} \times \bm{v}=0$ かつ ${\rm B} \in \ell$
* 平行かつ不一致 $\iff \bm{u} \times \bm{v}=0$ かつ $B \not \in \ell$
* 交差 $\iff \bm{u} \times \bm{v} \neq 0$

### 直線と直線の交点

以下, 2つの直線 $\ell, m$ 交差するとする. このとき, 交点は唯一存在する.

このことから, 線分と半直線の交点のような場合でも交点が存在する場合, 両者を直線に拡張して直線同士の交点を求めれば, その点がそのまま元問題の交点にもなる.

直線 ${\rm H}$ は次のようにして求められる.

$\ell,m$ をそれぞれ次のようにする.

* $\ell$ : 2点 ${\rm A}, {\rm B}$ を通る直線.
* $m$ : 2点 ${\rm C}, {\rm D}$ を通る直線.

このとき, 次のようにして点 ${\rm E}, {\rm F}$ を定める.

* ${\rm E}$ : 次の2つの直線の交点
  * ${\rm A}$ を通り, $m$ と平行な直線
  * ${\rm C}$ を通り, $\overrightarrow{{\rm AD}}$ と平行な直線
* ${\rm F}$ : 次の2つの直線の交点
  * ${\rm B}$ を通り, $m$ と平行な直線
  * ${\rm E}$ を通り, $l$ と平行な直線

このとき, ${\rm CE} \parallel {\rm AD}, {\rm AE} \parallel {\rm CD}$ であるから, 四角形 ${\rm AECD}$ は平行四辺形である. 同様にして, ${\rm AE} \parallel {\rm BF}, {\rm EF} \parallel {\rm AB}$ であるから, 四角形 ${\rm AEFB}$ も平行四辺形である.

よって, $\overrightarrow{{\rm AE}}=\overrightarrow{{\rm DC}}, \overrightarrow{{\rm AE}}=\overrightarrow{{\rm BF}}$ が導ける.

また, 平行四辺形 ${\rm AECD}, {\rm AEFB}$ は辺 ${\rm AE}$ を共有しているので, この2つの平行四辺形の面積を $S,T$ とすると, ある線分 ${\rm AB}$ 上の点 ${\rm G}$ が存在して,

$$S:T={\rm AG} : {\rm GB} \cdots (\spadesuit) $$

が成り立つ. そして, 3つの直線 ${\rm AE}, {\rm CD} (=m), {\rm BF}$ は互いに平行であるから, この ${\rm G}$ は直線 ${\rm CD} (=m)$ 上の点でもある.

よって, この点 ${\rm G}$ が直線 $l,m$ の交点であり,$(\spadesuit)$ および, $S,T$ が平行四辺形の面積であることから, $k$ を

$$k:=\dfrac{S}{T}=\dfrac{\overrightarrow{{\rm AE}} \times \overrightarrow{{\rm AD}}}{\overrightarrow{{\rm AE}} \times \overrightarrow{{\rm AB}}}=\dfrac{\overrightarrow{{\rm DC}} \times \overrightarrow{{\rm AD}}}{\overrightarrow{{\rm DC}} \times \overrightarrow{{\rm AB}}}=\dfrac{\overrightarrow{{\rm AD}} \times \overrightarrow{{\rm CD}}}{\overrightarrow{{\rm AB}} \times \overrightarrow{{\rm CD}}}$$

とすると, 点 ${\rm G}$ は線分 ${\rm AB}$ を $k:(1-k)$ に内分する点である.

### 射影

点 ${\rm P}$ の直線 $\ell$ への射影 ${\rm H}$ を求める. $\ell$ は2点 ${\rm A}, {\rm B}$ を通る直線とする. $\theta:=\angle {\rm PAB}$ とする. このとき,

$$\overrightarrow{{\rm AP}} \cdot \overrightarrow{{\rm AB}}=\left \lvert \overrightarrow{{\rm AP}} \right \rvert \left \lvert \overrightarrow{{\rm AB}} \right \rvert \cos \theta$$

である.

ここで, ${\rm H}$ は ${\rm P}$ の $\ell$ への射影であるから, ${\rm PH}$ と $\ell$ は直交する. そして, ${\rm H}$ は $\ell$ 上の点であるから, 直角三角形 ${\rm AHP}$ を考えることにより,

$$\left \lvert \overrightarrow{{\rm AH}} \right \rvert=\left \lvert \overrightarrow{{\rm AP}} \right \rvert \cos \theta$$

となる.

以上から,

$$\left \lvert \overrightarrow{{\rm AH}} \right \rvert=\dfrac{\overrightarrow{{\rm AP}} \cdot \overrightarrow{{\rm AB}}}{\left \lvert \overrightarrow{{\rm AB}} \right \rvert}$$

となり,

$$\overrightarrow{{\rm OH}}=\overrightarrow{{\rm OA}}+\dfrac{\left \lvert \overrightarrow{{\rm AH}}\right \rvert}{\left \lvert \overrightarrow{{\rm AB}}\right \rvert} \overrightarrow{{\rm AB}}=\overrightarrow{{\rm OA}}+\dfrac{\overrightarrow{{\rm AP}} \cdot \overrightarrow{{\rm AB}}}{\left \lvert \overrightarrow{{\rm AB}} \right \rvert^2}\overrightarrow{{\rm AB}}$$

が得られる.

### 反射

点 ${\rm P}$ を直線 $\ell$ に関して対称移動させた点を ${\rm P}'$  とする. このとき, ${\rm P}'$ は ${\rm P}$ の $\ell$ への射影を ${\rm H}$ とすると,

$$\overrightarrow{{\rm OP}'}=\overrightarrow{{\rm OP}}+2\overrightarrow{{\rm PH}}$$

を満たす.
