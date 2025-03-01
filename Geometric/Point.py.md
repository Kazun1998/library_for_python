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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.13.2/x64/lib/python3.13/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.13.2/x64/lib/python3.13/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from math import sqrt,sin,cos,tan,asin,acos,atan2,pi,floor,gcd\n\nepsilon\
    \ = 1e-8\ndef compare(x: float, y: float, ep: float = epsilon) -> int:\n    \"\
    \"\" x,y \u306E\u5927\u5C0F\u6BD4\u8F03\u3092\u3059\u308B. \u305F\u3060\u3057\
    , ep \u306E\u8AA4\u5DEE\u306F\u540C\u4E00\u8996\u3059\u308B.\n\n    Args:\n  \
    \      x (float):\n        y (float):\n        ep (float, optional): \u8A31\u5BB9\
    \u8AA4\u5DEE. Defaults to epsilon.\n\n    Returns:\n        x > y \u306E\u3068\
    \u304D\u306F 1\n        x = y \u306E\u3068\u304D\u306F 0\n        x < y \u306E\
    \u3068\u304D\u306F -1\n    \"\"\"\n\n    diff = x - y\n    if diff > ep:\n   \
    \     return 1\n    elif diff < -ep:\n        return -1\n    else:\n        return\
    \ 0\n\ndef sign(x: float, ep: float = epsilon) -> int:\n    if x > ep:\n     \
    \   return 1\n    elif x < -ep:\n        return -1\n    else:\n        return\
    \ 0\n\ndef equal(x: float, y: float, ep: float = epsilon) -> bool:\n    return\
    \ abs(x - y) < ep\n\nclass Point:\n    __slots__ = ('x', 'y')\n\n    def __init__(self,\
    \ x: float = 0, y: float = 0):\n        self.x = x\n        self.y = y\n\n   \
    \ #\u6587\u5B57\u5217\n    def __str__(self):\n        return f\"({self.x}, {self.y})\"\
    \n\n    def __repr__(self):\n        return f\"{self.__class__.__name__}({self.x},\
    \ {self.y})\"\n\n    #Bool\n    def __bool__(self):\n        return (sign(self.x)\
    \ != 0) or (sign(self.y) != 0)\n\n    #\u7B49\u53F7\n    def __eq__(self, other:\
    \ \"Point\") -> bool:\n        return equal(self.x, other.x) and equal(self.y,\
    \ other.y)\n\n    #\u4E0D\u7B49\u53F7\n    def __ne__(self, other: \"Point\")\
    \ -> bool:\n        return not (self == other)\n\n    #\u6BD4\u8F03(<)\n    def\
    \ __lt__(self, other: \"Point\") -> bool:\n        if (t := compare(self.x, other.x)):\n\
    \            return t < 0\n        return compare(self.y, other.y) < 0\n\n   \
    \ #\u6BD4\u8F03(<=)\n    def __le__(self, other: \"Point\") -> bool:\n       \
    \ return self < other or self == other\n\n    #\u6BD4\u8F03(>)\n    def __gt__(self,\
    \ other: \"Point\") -> bool:\n        return other < self\n\n    #\u6BD4\u8F03\
    (>=)\n    def __ge__(self, other: \"Point\") -> bool:\n        return other <=\
    \ self\n\n    #\u6B63\u3068\u8CA0\n    def __pos__(self) -> \"Point\":\n     \
    \   return self\n\n    def __neg__(self) -> \"Point\":\n        return Point(-self.x,\
    \ -self.y)\n\n    #\u52A0\u6CD5\n    def __add__(self, other: \"Point\") -> \"\
    Point\":\n        return Point(self.x + other.x, self.y + other.y)\n\n    def\
    \ __iadd__(self, other: \"Point\") -> \"Point\":\n        self.x += other.x\n\
    \        self.y += other.y\n        return self\n\n    #\u6E1B\u6CD5\n    def\
    \ __sub__(self, other: \"Point\") -> \"Point\":\n        return Point(self.x -\
    \ other.x, self.y - other.y)\n\n    def __isub__(self, other: \"Point\") -> \"\
    Point\":\n        self.x -= other.x\n        self.y -= other.y\n        return\
    \ self\n\n    #\u4E57\u6CD5\n    def __mul__(self, other: \"Point\") -> \"Point\"\
    :\n        x, y = self.x, self.y\n        u, v = other.x, other.y\n        return\
    \ Point(x * u- y * v, x * v + y * u)\n\n    def __imul__(self, other: \"Point\"\
    ) -> \"Point\":\n        return other * self\n\n    def __rmul__(self, other:\
    \ int | float) -> \"Point\":\n        if isinstance(other, (int, float)):\n  \
    \          return Point(other * self.x, other * self.y)\n        raise NotImplemented\n\
    \n    #\u9664\u6CD5\n    def __truediv__(self, other) -> \"Point\":\n        if\
    \ other == 0:\n            raise ZeroDivisionError\n        return Point(self.x\
    \ / other, self.y / other)\n\n    #\u7D76\u5BFE\u5024\n    def __abs__(self) ->\
    \ float:\n        return sqrt(self.x * self.x + self.y * self.y)\n\n    norm =\
    \ __abs__\n\n    def norm_2(self) -> float:\n        \"\"\" \u30CE\u30EB\u30E0\
    \u306E 2 \u4E57\u3092\u6C42\u3081\u308B\n\n        Returns:\n            float:\
    \ \u30CE\u30EB\u30E0\u306E 2 \u4E57\n        \"\"\"\n        return self.x * self.x\
    \ + self.y * self.y\n\n    #\u56DE\u8EE2\n    def rotate(self, theta: float) ->\
    \ \"Point\":\n        \"\"\" \u539F\u70B9\u4E2D\u5FC3\u306B theta \u3060\u3051\
    \u56DE\u8EE2\u3055\u305B\u305F\u5F8C\u306E\u70B9\u3092\u6C42\u3081\u308B.\n\n\
    \        Args:\n            theta (float): \u56DE\u8EE2\u89D2\n\n        Returns:\n\
    \            Point: \u56DE\u8EE2\u5F8C\u306E\u70B9\n        \"\"\"\n        x,\
    \ y = self.x, self.y\n        s, c = sin(theta), cos(theta)\n        return Point(c\
    \ * x - s * y , s * x + c * y)\n\n    def __iter__(self):\n        yield self.x\n\
    \        yield self.y\n\n    def __hash__(self):\n        return hash((self.x,self.y))\n\
    \n    def latticization(self, delta: float = 1e-7):\n        \"\"\" \u70B9\u304C\
    \u683C\u5B50\u70B9\u306B\u5341\u5206\u8FD1\u3044\u3068\u304D, \u3053\u306E\u70B9\
    \u3092\u683C\u5B50\u70B9\u306E\u70B9\u3068\u3057\u3066\u4FEE\u6B63\u3059\u308B\
    .\n\n        Args:\n            delta (float, optional): \u5224\u65AD\u306E\u305F\
    \u3081\u306E\u95BE\u5024. Defaults to 1e-7.\n        \"\"\"\n\n        if (abs(self.x\
    \ - floor(self.x + 0.5)) < delta) and (abs(self.y-floor(self.y + 0.5)) < delta):\n\
    \            self.x = floor(self.x+0.5)\n            self.y = floor(self.y+0.5)\n\
    \n    def normalization(self):\n        \"\"\" \u5411\u304D\u3092\u305D\u306E\u307E\
    \u307E\u306B, \u9577\u3055\u3092 1 \u306B\u5909\u63DB\u3059\u308B.\n        \"\
    \"\"\n\n        r = abs(self)\n        self.x /= r\n        self.y /= r\n\n  \
    \  def normal_unit_vector(self) -> \"Point\":\n        \"\"\" \u5358\u4F4D\u6CD5\
    \u7DDA\u30D9\u30AF\u30C8\u30EB\u3092\u6C42\u3081\u308B.\n\n        Returns:\n\
    \            Point: \u5358\u4F4D\u6CD5\u7DDA\u30D9\u30AF\u30C8\u30EB\n       \
    \ \"\"\"\n\n        assert self, ValueError\n\n        d = self.norm()\n     \
    \   return Point(-self.y / d, self.x / d)\n\n    def dot(self, other: \"Point\"\
    ) -> float:\n        \"\"\" \u5185\u7A4D\u3092\u6C42\u3081\u308B\n\n        Args:\n\
    \            other (Point):\n\n        Returns:\n            Point: \u5185\u7A4D\
    \n        \"\"\"\n        return self.x * other.x + self.y * other.y\n\n    def\
    \ det(self, other: \"Point\") -> float:\n        \"\"\" \u5916\u7A4D\u3092\u6C42\
    \u3081\u308B\n\n        Args:\n            other (Point):\n\n        Returns:\n\
    \            float: \u5916\u7A4D\n        \"\"\"\n\n        return self.x * other.y\
    \ - self.y * other.x\n\n    def arg(self) -> float:\n        \"\"\" \u539F\u70B9\
    \u304B\u3089\u307F\u305F\u3053\u306E\u70B9\u306E\u504F\u89D2\n\n        Returns:\n\
    \            float: \u504F\u89D2\n        \"\"\"\n\n        return atan2(self.y,self.x)\n\
    \n    def copy(self):\n        return Point(self.x,self.y)\n\ndef iSP(A: Point,\
    \ B: Point, C: Point) -> int:\n    \"\"\" A->B->C \u3068\u9032\u3093\u3060\u3068\
    \u304D\u306E\u9032\u884C\u65B9\u5411\u3092\u898B\u308B. \u203B B \u304C\u4E2D\u5FC3\
    \n\n    Args:\n        A (Point): \u59CB\u70B9\n        B (Point): \u4E2D\u7D99\
    \u70B9\n        C (Point): \u7D42\u70B9\n\n    Returns:\n        int:\n      \
    \      \u5DE6\u6298 (\u53CD\u6642\u8A08\u56DE\u308A): +1\n            \u53F3\u6298\
    \ (\u6642\u8A08\u56DE\u308A): -1\n            C-A-B \u306E\u9806\u306B\u4E26\u3093\
    \u3067\u3044\u308B: -2\n            A-B-C \u306E\u9806\u306B\u4E26\u3093\u3067\
    \u3044\u308B: 2\n            A-C-B \u306E\u9806\u306B\u4E26\u3093\u3067\u3044\u308B\
    : 0\n    \"\"\"\n\n    if (p := sign((B - A).det(C - A))) != 0:\n        return\
    \ p\n\n    if sign((B - A).dot(C - A)) == -1:\n        return -2\n    if sign((A\
    \ - B).dot(C - B)) == -1:\n        return 2\n    return 0\n\ndef Arg(P: Point,\
    \ Q: Point = Point(0,0)) -> float:\n    \"\"\" \u70B9 Q \u304B\u3089\u898B\u305F\
    \u70B9 P \u306E\u504F\u89D2\u3092\u6C42\u3081\u308B.\n\n    Args:\n        P (Point):\
    \ \u70B9\n        Q (Point, optional): \u57FA\u6E96\u70B9. Defaults to Point(0,0).\n\
    \n    Returns:\n        float: \u504F\u89D2\n    \"\"\"\n\n    R = P - Q\n   \
    \ return atan2(R.y, R.x)\n\ndef Angle_Type(A: Point, B: Point, C: Point) -> int:\n\
    \    \"\"\" \u89D2ABC \u304C\u92ED\u89D2\u304B\u76F4\u89D2\u304B\u920D\u89D2\u304B\
    \u3092\u5224\u5B9A\u3059\u308B.\n\n    Args:\n        A (Point):\n        B (Point):\n\
    \        C (Point):\n\n    Returns:\n        int:\n            1: \u92ED\u89D2\
    \n            0: \u76F4\u89D2\n            -1: \u920D\u89D2\n    \"\"\"\n\n  \
    \  return sign((A-B).dot(C-B))\n\ndef Inner(P: Point, Q: Point) -> float:\n  \
    \  \"\"\" \u70B9 P \u3068\u70B9 Q \u306E\u5185\u7A4D\u3092\u6C42\u3081\u308B.\n\
    \n    Args:\n        P (Point):\n        Q (Point):\n\n    Returns:\n        float:\
    \ \u5185\u7A4D\n    \"\"\"\n\n    return P.x * Q.x + P.y * Q.y\n\ndef Det(P: Point,\
    \ Q: Point) -> float:\n    \"\"\" \u70B9 P \u3068\u70B9 Q \u304C\u8CBC\u308B\u5E73\
    \u884C\u56DB\u8FBA\u5F62\u306E\u7B26\u53F7\u4ED8\u304D\u9762\u7A4D (\u5916\u7A4D\
    ) \u3092\u6C42\u3081\u308B.\n\n    Args:\n        P (Point):\n        Q (Point):\n\
    \n    Returns:\n        float: \u5916\u7A4D\n    \"\"\"\n\n    return P.x * Q.y\
    \ - P.y * Q.x\n\ndef Internal_Division_Point(P: Point, Q: Point, a: float, b:\
    \ float) -> Point:\n    \"\"\" \u7DDA\u5206 PQ \u3092 a:b \u306B\u5185\u5206\u3059\
    \u308B\u70B9\u3092\u6C42\u3081\u308B.\n\n    Args:\n        P (Point):\n     \
    \   Q (Point):\n        a (float): P \u5074\u306E\u6BD4\u7387\n        b (float):\
    \ Q \u5074\u306E\u6BD4\u7387\n\n    Returns:\n        Point: \u7DDA\u5206 PQ \u3092\
    \ a:b \u306B\u5185\u5206\u3059\u308B\u70B9\u3092\u6C42\u3081\u308B\n    \"\"\"\
    \n\n    assert a + b != 0\n\n    return (b * P + a * Q) / (a + b)\n\ndef External_Division_Point(P:\
    \ Point, Q: Point, a: float, b: float) -> Point:\n    \"\"\" \u7DDA\u5206 PQ \u3092\
    \ a:b \u306B\u5916\u5206\u3059\u308B\u70B9\u3092\u6C42\u3081\u308B.\n\n    Args:\n\
    \        P (Point):\n        Q (Point):\n        a (float): P \u5074\u306E\u6BD4\
    \u7387\n        b (float): Q \u5074\u306E\u6BD4\u7387\n\n    Returns:\n      \
    \  Point: \u7DDA\u5206 PQ \u3092 a:b \u306B\u5185\u5206\u3059\u308B\u70B9\u3092\
    \u6C42\u3081\u308B\n    \"\"\"\n\n    assert a - b != 0\n    return (-b * P +\
    \ a * Q) / (a - b)\n\ndef MidPoint(P: Point, Q: Point) -> Point:\n    \"\"\" \u7DDA\
    \u5206 PQ \u306E\u4E2D\u70B9\u3092\u6C42\u3081\u308B.\n\n    Args:\n        P\
    \ (Point):\n        Q (Point):\n\n    Returns:\n        Point: \u4E2D\u70B9\n\
    \    \"\"\"\n\n    return Point((P.x + Q.x) / 2, (P.y + Q.y) / 2)\n\ndef Argument_Compare(P:\
    \ Point, Q: Point)  -> bool:\n    \"\"\" OQ \u304C OP \u304B\u3089\u307F\u3066\
    \u53CD\u6642\u8A08\u56DE\u308A\u304B\u3069\u3046\u304B?\n\n    Args:\n       \
    \ P (Point): \u57FA\u6E96\u70B9\n        Q (Point): \u5224\u5B9A\u70B9\n\n   \
    \ Returns:\n        bool: \u53CD\u6642\u8A08\u56DE\u308A\u306A\u3089\u3070 True\n\
    \    \"\"\"\n    return sign(Q.det(P))\n\ndef Argument_Sort(L):\n    \"\"\" \u70B9\
    \u3092\u504F\u89D2\u30BD\u30FC\u30C8\u3059\u308B.\n\n    L: \u70B9\u306E\u30EA\
    \u30B9\u30C8\n    \"\"\"\n\n    from functools import cmp_to_key\n\n    def position(P):\n\
    \        m=compare(P.y,0)\n        if m==-1:\n            return -1\n        elif\
    \ m==0 and compare(P.x,0)>=0:\n            return 0\n        else:\n         \
    \   return 1\n\n    def cmp(P,Q):\n        a=position(P); b=position(Q)\n    \
    \    if a<b: return -1\n        elif a>b: return 1\n        else:return -compare(P.det(Q),0)\n\
    \n    L.sort(key=cmp_to_key(cmp))\n\ndef Argument_Sort_by_Index(L):\n    \"\"\"\
    \ \u70B9\u3092\u504F\u89D2\u30BD\u30FC\u30C8\u3059\u308B (\u8FD4\u308A\u5024\u306F\
    \u6DFB\u5B57).\n\n    L: \u70B9\u306E\u30EA\u30B9\u30C8\n    \"\"\"\n\n    def\
    \ merge(a,b):\n        I=[]\n\n        la=len(a); lb=len(b)\n        ia=0; ib=0\n\
    \n        while (ia<la) and (ib<lb):\n            if Argument_Compare(L[a[ia]],L[b[ib]])<=0:\n\
    \                I.append(a[ia])\n                ia+=1\n            else:\n \
    \               I.append(b[ib])\n                ib+=1\n\n        for i in range(ia,la):\n\
    \            I.append(a[i])\n\n        for i in range(ib,lb):\n            I.append(b[i])\n\
    \n        return I\n\n    def sorting(a):\n        if len(a)==1:\n           \
    \ return a\n        else:\n            return merge(sorting(a[:len(a)//2]),sorting(a[len(a)//2:]))\n\
    \n    return sorting(list(range(len(L))))\n"
  dependsOn: []
  isVerificationFile: false
  path: Geometric/Point.py
  requiredBy: []
  timestamp: '2025-03-01 16:16:33+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Geometric/Point.py
layout: document
title: Point
---

## Outline

座標平面 $\mathbb{R}^2$ 上の図形における計算を行う.

ただし, このライブラリ及び, ドキュメント内では座標平面内の点 $\mathrm{A}=(x,y)$ と2次元実ベクトル $\boldsymbol{a}=(x,y)$ を同一視する.

また, 2次元ベクトル $\boldsymbol{a}=(a_x, a_y), \boldsymbol{b}=(b_x, b_y)$ に対する外積 $\boldsymbol{a} \times \boldsymbol{b}$ を

$$\boldsymbol{a} \times \boldsymbol{b}:=\det (\boldsymbol{a}, \boldsymbol{b})=a_x b_y-b_x a_y$$

とする.

## Theory

### 3点の進行方向

相異なる3点 $\mathrm{A}, \mathrm{B}, \mathrm{C}$ に対して, $\mathrm{A} \to \mathrm{B} \to \mathrm{C}$ がどのようにして進むことになるかを考える.

$\boldsymbol{u}:=\overrightarrow{\mathrm{AB}}, \boldsymbol{v}:=\overrightarrow{\mathrm{AC}}$ とする.

- $\boldsymbol{u} \times \boldsymbol{v}>0$ ならば, 左折 (反時計回り) である.
- $\boldsymbol{u} \times \boldsymbol{v}<0$ ならば 右折 (時計回り) である.
- $\boldsymbol{u} \times \boldsymbol{v}=0$ のとき, 3点は同一直線上の3点である. この場合, どの順にならんでいるかを調べる.
  - $\overrightarrow{\mathrm{AB}} \cdot \overrightarrow{\mathrm{AC}}<0$ ならば, 線分 $\mathrm{A}$ は線分 $\mathrm{BC}$ 上の点である.
  - $\overrightarrow{\mathrm{BA}} \cdot \overrightarrow{\mathrm{BC}}<0$ ならば, 線分 $\mathrm{B}$ は線分 $\mathrm{AC}$ 上の点である.
  - これ以外の場合 (この場合, $\overrightarrow{\mathrm{CA}} \cdot \overrightarrow{\mathrm{CB}}<0$ になる) ならば, 線分 $\mathrm{C}$ は線分 $\mathrm{AB}$ 上の点である.
