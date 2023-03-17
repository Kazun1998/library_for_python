---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.2/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.2/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from Point import *\nfrom Line import *\nfrom Affine import *\n\nclass Circle():\n\
    \    __slots__=[\"center\",\"radius\",\"id\"]\n\n    ep=1e-9\n    def __init__(self,Center:Point,Radius:float):\n\
    \        \"\"\" 2\u70B9 P \u3092\u4E2D\u5FC3\u3068\u3059\u308B\u534A\u5F84 r \u306E\
    \u5186\u3092\u751F\u6210\u3059\u308B.\n\n        P: Point\n        r>=0\n    \
    \    \"\"\"\n        assert Radius>=0\n\n        self.center=Center\n        self.radius=Radius\n\
    \        self.id=5\n\n    def __str__(self):\n        return \"[Circle] Center:\
    \ {}, Radius: {}\".format(self.center,self.radius)\n\n    __repr__=__str__\n\n\
    \    def __contains__(self,Point):\n        return compare(abs(Point-self.center),self.radius,self.ep)==0\n\
    \n#=== \u4EA4\u5DEE\u5224\u5B9A\ndef has_Intersection_between_Circle_and_Segment(C,L,endpoint=True):\n\
    \    \"\"\"\u5186 C \u3068\u7DDA\u5206 L \u306E\u4EA4\u5DEE\u5224\u5B9A\u3092\u884C\
    \u3046.\n\n    \"\"\"\n\n    c=C.center\n    ep=max(C.ep,L.ep)\n    flag1=(compare(\n\
    \        Distance_between_Point_and_Segment(c,L),\n        C.radius,\n       \
    \ ep)<=0)\n    flag2=(compare(max(abs(c-L.begin),abs(c-L.end)),C.radius,ep)>=0)\n\
    \    return flag1 and flag2\n\ndef has_Intersection_between_Circle_and_Line(C,L):\n\
    \    \"\"\"\u5186 C \u3068\u76F4\u7DDA L \u306E\u4EA4\u5DEE\u5224\u5B9A\u3092\u884C\
    \u3046.\n\n    \"\"\"\n    return compare(\n        Distance_between_Point_and_Line(C.center,L),\n\
    \        C.radius,\n        max(C.ep,L.ep)\n        )<=0\n\ndef has_Intersection_between_Circle_and_Circle(C,D):\n\
    \    \"\"\"2\u3064\u306E\u5186 C,D \u306E\u4EA4\u5DEE\u5224\u5B9A\u3092\u884C\u3046\
    .\n\n    \"\"\"\n\n    r=C.radius; s=D.radius;\n    d=abs(C.center-D.center)\n\
    \    ep=max(C.ep,D.ep)\n\n    return compare(d,abs(r-s),ep)>=0 and compare(d,r+s,ep)<=0\n\
    \n#=== \u4EA4\u70B9\u3092\u6C42\u3081\u308B\ndef Intersection_between_Circle_and_Line(C,L):\n\
    \    \"\"\" \u5186 C \u3068\u76F4\u7DDA L \u306E\u4EA4\u70B9\u3092\u6C42\u3081\
    \u308B.\n\n    \"\"\"\n\n    if not has_Intersection_between_Circle_and_Line(C,L):\n\
    \        return []\n\n    H=Projection(C.Center,L)\n    d=Distance_between_Point_and_Line(C.Center,L)\n\
    \    x=sqrt(max(C.radius*C.radius-d*d,0))\n    v=L.vectorize(); v.normalization()\n\
    \n    return [H+x*v,H-x*v]\n\ndef Intersection_between_Circle_and_Circle(C,D):\n\
    \    \"\"\" 2\u3064\u306E\u5186 C,D \u306E\u4EA4\u70B9\u3092\u6C42\u3081\u308B\
    .\n\n    \"\"\"\n\n    if not has_Intersection_between_Circle_and_Circle(C,D):\n\
    \        return []\n\n    r=C.radius; s=D.radius\n\n    v=D.center-C.center\n\
    \    d=abs(v)\n    v.normalization()\n    w=v*Point(0,1)\n\n    x=(d*d+r*r-s*s)/(2*d)\n\
    \    y=sqrt(max(r*r-x*x,0))\n    return [C.center+x*v+y*w,C.center+x*v-y*w]\n\n\
    #=== \u63A5\u7DDA\ndef Tangent_to_Circle_on_Point(P,C):\n    \"\"\" \u5186 C \u4E0A\
    \u306E\u70B9 P \u3092\u63A5\u70B9\u3068\u3059\u308B\u63A5\u7DDA\u3092\u6C42\u3081\
    \u308B.\n\n    \"\"\"\n\n    assert P in C\n    v=(P-C.center)*Point(0,1)\n\n\
    \    return Line(P,P+v)\n\ndef Tangent_to_Circle_from_Point(P,C):\n    \"\"\"\
    \ \u70B9 P \u304B\u3089\u5F15\u304F\u5186 C \u3078\u306E\u63A5\u7DDA\u3092\u6C42\
    \u3081\u308B.\"\"\"\n\n    v=C.center-P\n    d=abs(v); v.normalization()\n   \
    \ r=C.radius\n\n    x=sqrt(max(d*d-r*r,0))\n    theta=asin(r/d)\n\n    return\
    \ [Line(P,P+x*v.rotate(theta)),Line(P,P+x*v.rotate(-theta))]\n\ndef Common_Tangent_between_Circle_and_Circle(C,D):\n\
    \    \"\"\" \u5186 C,D \u306E\u5171\u901A\u63A5\u7DDA\u3092\u6C42\u3081\u308B\
    .\"\"\"\n\n    ep=max(C.ep,D.ep)\n    r=C.radius; s=D.radius\n    d=abs(C.center-D.center)\n\
    \n    X=[]\n\n    K=Circle(Point(),r)\n    if compare(d,abs(r-s),ep)>=0:\n   \
    \     a=r*(r-s)/d\n        b=sqrt(max(0,r*r-a*a))\n\n        X.append(Tangent_to_Circle_on_Point(Point(a,b),K))\n\
    \        X.append(Tangent_to_Circle_on_Point(Point(a,-b),K))\n    if compare(d,abs(r+s),ep)>=0:\n\
    \        a=r*(r+s)/d\n        b=sqrt(max(0,r*r-a*a))\n\n        X.append(Tangent_to_Circle_on_Point(Point(a,b),K))\n\
    \        X.append(Tangent_to_Circle_on_Point(Point(a,-b),K))\n\n    F=Translation_and_Rotate_Affine_Determine(Point(),Point(d,0),C.center,D.center)\n\
    \    return [F[l] for l in X]\n\n#=== 2\u3064\u306E\u5186\u306E\u4F4D\u7F6E\u95A2\
    \u4FC2\u3092\u6C42\u3081\u308B.\ndef Relationship_between_Circle_and_Circle(C:\
    \ Circle, D:Circle):\n    \"\"\" 2\u3064\u306E\u5186\u306E\u4F4D\u7F6E\u95A2\u4FC2\
    \u3092\u6C42\u3081\u308B.\n\n    [Input]\n    C,D: Circle\n\n    [Output]\n  \
    \  4: \u96E2\u308C\u3066\u3044\u308B\n    3: \u5916\u63A5\n    2: \u4EA4\u308F\
    \u3063\u3066\u3044\u308B\n    1: \u5185\u63A5\n    0: \u542B\u3093\u3067\u3044\
    \u308B\n    \"\"\"\n\n    d=abs(C.center-D.center)\n    r=C.radius; s=D.radius\n\
    \    ep=max(C.ep, D.ep)\n\n    alpha=compare(d,r+s,ep)\n    if alpha==1:\n   \
    \     return 4\n    elif alpha==0:\n        return 3\n    else:\n        beta=compare(d,abs(r-s),ep)\n\
    \        if beta==1:\n            return 2\n        elif beta==0:\n          \
    \  return 1\n        else:\n            return 0\n\n#=== \u5171\u901A\u90E8\u5206\
    \ndef Circles_Intersection_Area(C,D):\n    \"\"\" 2\u3064\u306E\u5186 C, D \u306E\
    \u5171\u901A\u90E8\u5206\u306E\u9762\u7A4D\u3092\u6C42\u3081\u308B.\n\n    C,\
    \ D: Circle\n    \"\"\"\n\n    d=abs(C.P-D.P)\n    r=C.r; s=D.r\n    ep=max(C.ep,\
    \ D.ep)\n\n    if compare(d,r+s,ep)==1:\n        return 0\n    if compare(d,abs(r-s),ep)==-1:\n\
    \        a=min(r,s)\n        return pi*a*a\n\n    alpha=acos((d*d+r*r-s*s)/(2*d*r))\n\
    \    beta =acos((d*d-r*r+s*s)/(2*d*s))\n\n    X=r*r*alpha\n    Y=s*s*beta\n  \
    \  Z=d*r*sin(alpha)\n    return X+Y-Z\n"
  dependsOn: []
  isVerificationFile: false
  path: Geometric/Circle.py
  requiredBy: []
  timestamp: '2022-10-27 18:35:31+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Geometric/Circle.py
layout: document
title: Circle
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
