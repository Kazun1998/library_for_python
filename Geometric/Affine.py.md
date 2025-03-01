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
  code: "from Point import *\nfrom Line import *\nfrom Circle import *\nfrom Triangle\
    \ import *\nfrom Polygon import *\n\nclass Affine:\n    __slots__ = ('mat', 'vec')\n\
    \n    def __init__(self, mat: list[list[float]] = None, vec: list[float] = None):\n\
    \        if mat is None:\n            mat = [[1, 0], [0, 1]]\n\n        if vec\
    \ is None:\n            vec = [0, 0]\n\n        self.mat = mat\n        self.vec\
    \ = vec\n\n    def __str__(self) -> str:\n        return f\"Matrix: {self.mat},\
    \ Vector: {self.vec}\"\n\n    def __repr__(self) -> str:\n        return f\"{self.__class__.__name__}({self.mat},\
    \ {self.vec})\"\n\n    def __iter__(self):\n        yield self.mat\n        yield\
    \ self.vec\n\n    def __pos__(self) -> \"Affine\":\n        return self\n\n  \
    \  def __neg__(self):\n        [[a,b],[c,d]], [x, y] = self\n        return Affine([[-a,\
    \ -b], [-c, -d]], [-x, -y])\n\n    def __add__(self, other):\n        a = self.mat[0][0]\
    \ + other.mat[0][0]\n        b = self.mat[0][1] + other.mat[0][1]\n        c =\
    \ self.mat[1][0] + other.mat[1][0]\n        d = self.mat[1][1] + other.mat[1][1]\n\
    \n        u = self.vec[0] + other.vec[1]\n        v = self.vec[1] + other.vec[1]\n\
    \n        return Affine([[a, b], [c, d]], [u, v])\n\n    def __sub__(self,other):\n\
    \        a = self.mat[0][0] - other.mat[0][0]\n        b = self.mat[0][1] - other.mat[0][1]\n\
    \        c = self.mat[1][0] - other.mat[1][0]\n        d = self.mat[1][1] - other.mat[1][1]\n\
    \n        u = self.vec[0] - other.vec[1]\n        v = self.vec[1] - other.vec[1]\n\
    \n        return Affine([[a, b], [c, d]], [u, v])\n\n    def __mul__(self, other):\n\
    \        a = self.mat[0][0] * other.mat[0][0] + self.mat[0][1] * other.mat[1][0]\n\
    \        b = self.mat[0][0] * other.mat[0][1] + self.mat[0][1] * other.mat[1][1]\n\
    \        c = self.mat[1][0] * other.mat[0][0] + self.mat[1][1] * other.mat[1][0]\n\
    \        d = self.mat[1][0] * other.mat[0][1] + self.mat[1][1] * other.mat[1][1]\n\
    \n        u = self.mat[0][0] * other.vec[0] + self.mat[0][1] * other.vec[1] +\
    \ self.vec[0]\n        v = self.mat[1][0] * other.vec[0] + self.mat[1][1] * other.vec[1]\
    \ + self.vec[1]\n\n        return Affine([[a, b], [c, d]], [u, v])\n\n    def\
    \ __pow__(self, n):\n        if n < 0:\n            return pow(self, -n).inverse()\n\
    \n        A = self\n        B = Affine()\n        while n:\n            if n &\
    \ 1:\n                B *= A\n            n >>= 1\n            A *= A\n      \
    \  return  B\n\n    def __eq__(self, other):\n        return self.mat == other.mat\
    \ and self.vec == other.vec\n\n    def inverse(self) -> \"Affine\":\n        [[a,\
    \ b], [c, d]], [x, y] = self\n\n        det = a * d - b * c\n        p, q, r,\
    \ s = d / det, -b / det, -c / det, a/ det\n        return Affine([[p, q], [r,\
    \ s]], [-(p * x  + q * y), -(r * x + s * y)])\n\n    def integerization(self,\
    \ delta = 1e-7):\n        for i in [0, 1]:\n            for j in [0, 1]:\n   \
    \             if abs(self.mat[i][j] - floor(self.mat[i][j] + 0.5)) < delta:\n\
    \                    self.mat[i][j] = floor(self.mat[i][j] + 0.5)\n\n        if\
    \ abs(self.vec[0] - floor(self.vec[0] + 0.5)) < delta:\n            self.vec[0]\
    \ = floor(self.vec[0] + 0.5)\n\n        if abs(self.vec[1] - floor(self.vec[1]\
    \ + 0.5)) < delta:\n            self.vec[1] = floor(self.vec[1] + 0.5)\n\n   \
    \ def __getitem__(self, shape):\n        return Action(self, shape)\n\n#=== \u4F5C\
    \u7528\ndef Action(A: Affine, S):\n    \"\"\" \u56F3\u5F62 S \u306B\u30A2\u30D5\
    \u30A3\u30F3\u5909\u63DB A \u3092\u65BD\u3057\u305F\u5F8C\u306E\u7D50\u679C\u3092\
    \u8FD4\u3059.\n\n    Args:\n        A (Affine): \u30A2\u30D5\u30A3\u30F3\u5909\
    \u63DB\n        S : \u56F3\u5F62\n\n    Raises:\n        NotImplemented: \u30A2\
    \u30D5\u30A3\u30F3\u5909\u63DB\u3067\u5186\u304C\u5186\u306B\u6620\u308B\u3068\
    \u306F\u9650\u3089\u306A\u3044 (\u4E00\u822C\u306B\u306F\u6955\u5186)\n\n    Returns:\
    \ \u30A2\u30D5\u30A3\u30F3\u5909\u63DB\u5F8C\u306E\u56F3\u5F62\n    \"\"\"\n\n\
    \    if isinstance(S, Point):\n        [[a, b], [c, d]], [x, y] = A\n        return\
    \ Point(a * S.x + b * S.y + x, c * S.x + d * S.y + y)\n    elif isinstance(S,\
    \ Segment):\n        return Segment(Action(A, S.begin), Action(A, S.end))\n  \
    \  elif isinstance(S, Ray):\n        return Ray(Action(A, S.begin), Action(A,\
    \ S.end))\n    elif isinstance(S, Line):\n        return Line(Action(A, S.begin),\
    \ Action(A, S.end))\n    elif isinstance(S, Circle):\n        raise NotImplemented\n\
    \    elif isinstance(S, Triangle):\n        return Triangle(Action(A, S.A), Action(A,\
    \ S.B), Action(A, S.C))\n    elif isinstance(S, Polygon):\n        return Polygon(*[Action(A,\
    \ P) for P in S.vertices])\n\n#=== \u30A2\u30D5\u30A3\u30F3\u5909\u63DB\u306E\u751F\
    \u6210\ndef Translation(x: float, y: float) -> Affine:\n    \"\"\" (x, y) \u3060\
    \u3051\u5E73\u884C\u79FB\u52D5\u3055\u305B\u308B\u30A2\u30D5\u30A3\u30F3\u5909\
    \u63DB\u3092\u6C42\u3081\u308B.\n\n    Args:\n        x (float): x \u5EA7\u6A19\
    \u306E\u79FB\u52D5\u91CF\n        y (float): y \u5EA7\u6A19\u306E\u79FB\u52D5\u91CF\
    \n\n    Returns:\n        Affine: (x, y) \u3060\u3051\u5E73\u884C\u79FB\u52D5\u3055\
    \u305B\u308B\u30A2\u30D5\u30A3\u30F3\u5909\u63DB\n    \"\"\"\n    return Affine(vec=[x,\
    \ y])\n\ndef Point_Reflection(x: float = 0, y: float = 0) -> Affine:\n    \"\"\
    \" \u70B9 (x,y) \u306B\u95A2\u3059\u308B\u5BFE\u79F0\u79FB\u52D5\u3092\u3059\u308B\
    \u30A2\u30D5\u30A3\u30F3\u5909\u63DB\u3092\u751F\u6210\u3059\u308B.\n\n    Args:\n\
    \        x (float, optional): \u70B9\u306E x \u5EA7\u6A19. Defaults to 0.\n  \
    \      y (float, optional): \u70B9\u306E y \u5EA7\u6A19. Defaults to 0.\n\n  \
    \  Returns:\n        Affine: \u70B9 (x,y) \u306B\u95A2\u3059\u308B\u5BFE\u79F0\
    \u79FB\u52D5\u3092\u3059\u308B\u30A2\u30D5\u30A3\u30F3\u5909\u63DB\n    \"\"\"\
    \n\n    return Affine([[-1, 0], [0, -1]], [2 * x, 2 * y])\n\ndef Line_Reflection(a:\
    \ float, b: float, c: float) -> Affine:\n    \"\"\" \u76F4\u7DDA a x + b y + c\
    \ = 0 \u306B\u95A2\u3059\u308B\u5BFE\u79F0\u79FB\u52D5\u3092\u3059\u308B\u30A2\
    \u30D5\u30A3\u30F3\u5909\u63DB\u3092\u751F\u6210\u3059\u308B.\n\n    Args:\n \
    \       a (float):\n        b (float):\n        c (float):\n\n    Raises:\n  \
    \      ValueError: a = b = 0 \u306E\u3068\u304D\u306B\u767A\u751F\n\n    Returns:\n\
    \        Affine: \u76F4\u7DDA a x + b y + c = 0 \u306B\u95A2\u3059\u308B\u5BFE\
    \u79F0\u79FB\u52D5\n    \"\"\"\n    if (sign(a) == 0) or (sign(b) == 0):\n   \
    \     raise ValueError\n\n    k = a * a + b * b\n\n    p = (- a * a + b * b) /\
    \ k\n    q = - 2 * a * b / k\n    r = - 2 * c / k\n\n    return Affine([[p, q],\
    \ [q, -p]], [a * r , b * r])\n\ndef Rotation(theta: float, x: float = 0, y: float\
    \ = 0) -> Affine:\n    \"\"\" \u70B9 (x, y) \u5468\u308A\u3067 theta (\u6642\u8A08\
    \u56DE\u308A) \u306B\u56DE\u8EE2\u3055\u305B\u308B\u30A2\u30D5\u30A3\u30F3\u5909\
    \u63DB\u3092\u751F\u6210\u3059\u308B.\n\n    Args:\n        theta (float): \u56DE\
    \u8EE2\u89D2\n        x (float, optional): \u4E2D\u5FC3\u3068\u306A\u308B\u70B9\
    \u306E x \u5EA7\u6A19. Defaults to 0.\n        y (float, optional): \u4E2D\u5FC3\
    \u3068\u306A\u308B\u70B9\u306E y \u5EA7\u6A19. Defaults to 0.\n\n    Returns:\n\
    \        Affine: \u70B9 (x, y) \u5468\u308A\u3067 theta (\u6642\u8A08\u56DE\u308A\
    ) \u306B\u56DE\u8EE2\u3055\u305B\u308B\u30A2\u30D5\u30A3\u30F3\u5909\u63DB\n \
    \   \"\"\"\n\n    c = cos(theta); s = sin(theta)\n    return Affine([[c, -s],\
    \ [s, c]], [(1 - c) * x + s * y, -s * x + (1 - c) * y])\n\n#=== \u30A2\u30D5\u30A3\
    \u30F3\u5909\u63DB\u306E\u6C7A\u5B9A\ndef Translation_and_Rotate_Affine_Determine(A:\
    \ Point, B: Point, P: Point, Q: Point) -> Affine:\n    \"\"\" \u5E73\u884C\u79FB\
    \u52D5\u3068\u56DE\u8EE2\u306E\u307F\u306B\u3088\u3063\u3066\u751F\u6210\u3055\
    \u308C F(A) = P, F(B) = Q \u3092\u6E80\u305F\u3059\u30A2\u30D5\u30A3\u30F3\u5909\
    \u63DB\u3092\u6C42\u3081\u308B.\n\n    Args:\n        A (Point):\n        B (Point):\n\
    \        P (Point): F(A)\n        Q (Point): F(B)\n\n    Raises:\n        ValueError:\
    \ |AB| = |PQ| \u3067\u306A\u304F\u3066\u306F\u306A\u3089\u306A\u3044.\n\n    Returns:\n\
    \        Affine: \u5E73\u884C\u79FB\u52D5\u3068\u56DE\u8EE2\u306E\u307F\u306B\u3088\
    \u3063\u3066\u751F\u6210\u3055\u308C F(A) = P, F(B) = Q \u3092\u6E80\u305F\u3059\
    \n    \"\"\"\n\n    if not equal(abs(B - A), abs(Q - P)):\n        raise ValueError\n\
    \n    return Rotation(Arg(Q, P) - Arg(B, A), *P) * Translation(*(P-A))\n\ndef\
    \ Affine_Determine(A: Point, B: Point, C: Point, P: Point, Q: Point, R: Point)\
    \ -> Affine:\n    \"\"\" \u5E73\u884C\u79FB\u52D5\u3068\u56DE\u8EE2\u306E\u307F\
    \u306B\u3088\u3063\u3066\u751F\u6210\u3055\u308C F(A) = P, F(B) = Q, F(C) = R\
    \ \u3092\u6E80\u305F\u3059\u30A2\u30D5\u30A3\u30F3\u5909\u63DB\u3092\u6C42\u3081\
    \u308B.\n\n    Args:\n        A (Point):\n        B (Point):\n        C (Point):\n\
    \        P (Point): F(A)\n        Q (Point): F(B)\n        R (Point): F(C)\n\n\
    \    Raises:\n        ValueError: A, B, C \u306F\u540C\u4E00\u76F4\u7DDA\u4E0A\
    \u306E 3 \u70B9\u3067\u3042\u3063\u3066\u306F\u3044\u3051\u306A\u3044.\n\n   \
    \ Returns:\n        Affine: \u5E73\u884C\u79FB\u52D5\u3068\u56DE\u8EE2\u306E\u307F\
    \u306B\u3088\u3063\u3066\u751F\u6210\u3055\u308C F(A) = P, F(B) = Q, F(C) = R\
    \ \u3092\u6E80\u305F\u3059\u30A2\u30D5\u30A3\u30F3\u5909\u63DB\n    \"\"\"\n\n\
    \    if equal((B - A).det(C - A)):\n        raise ValueError\n\n    q1, q2 = Q\
    \ - P\n    r1, r2 = R - P\n    b1, b2 = B - A\n    c1, c2 = C - A\n    det = b1\
    \ * c2 - b2 * c1\n\n    M = [\n            [(q1 * c2 - r1 * b2) / det, (-q1 *\
    \ c1 + r1 * b1) / det],\n            [(q2 *c2 - r2 * b2) / det, (-q2 * c1 + r2\
    \ * b1) / det]\n        ]\n\n    v = [\n            P.x - (M[0][0] * A.x + M[0][1]\
    \ * A.y),\n            P.y - (M[1][0] * A.x + M[1][1] * A.y)\n        ]\n\n  \
    \  return Affine(M, v)\n"
  dependsOn: []
  isVerificationFile: false
  path: Geometric/Affine.py
  requiredBy: []
  timestamp: '2025-03-01 16:16:33+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Geometric/Affine.py
layout: document
title: Affine
---

## Theory

### アフィン変換の定義

2次実行列 $A \in M_2(\mathbb{R})$ と2次ベクトル $\boldsymbol{b} \in \mathbb{R}^2$ に対して, 写像

$$\Phi(A, \boldsymbol{b}): \mathbb{R}^2 \to \mathbb{R}^2; \boldsymbol{x} \mapsto A \boldsymbol{x}+\boldsymbol{b}$$

をアフィン写像という.

このとき,

$$\Phi(A,\boldsymbol{b})(\boldsymbol{x})=\begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \end{pmatrix} \begin{pmatrix} A & \boldsymbol{b} \\ \boldsymbol{0}^\top & 1 \end{pmatrix} \begin{pmatrix} \boldsymbol{x} \\ 1 \end{pmatrix} $$

が成り立つ. このとき, 和とスカラー倍と積において,

* $\Phi(A, \boldsymbol{b})+\Phi(B, \boldsymbol{c})=\Phi(A+B, \boldsymbol{b}+\boldsymbol{c})$
* $\lambda \Phi(A, \boldsymbol{b})=\Phi(\lambda A, \lambda \boldsymbol{b})$
* $\Phi(A, \boldsymbol{b}) \circ \Phi(B, \boldsymbol{c})=\Phi(A+B, \boldsymbol{b}+\boldsymbol{c})=\Phi(AB, A \boldsymbol{c}+\boldsymbol{b})$

が成り立つ (積については真ん中の項の行列積の結果と一致する).

アフィン変換 $\Phi(A,\boldsymbol{b})$ に対して, $A$ を行列部, $\boldsymbol{b}$ をベクトル部という.

### アフィン変換の特徴づけ

* アフィン変換が **全単射** であることの必要十分条件は行列部が **正則行列** であることである.
* アフィン変換が **等距離写像** であることの必要十分条件は行列部が **直交行列** であることである.
* アフィン変換が **線形写像** になることの必要十分条件はベクトル部が **零ベクトル** になることである.

### 変換とアフィン変換

座標空間における変換の多くはアフィン変換によって記述できる.

* $\boldsymbol{v}$ だけ平行移動 $\cdots \Phi(I_2, \boldsymbol{v})$
* 点 $\mathrm{P}$ に関して対称移動 $\cdots \Phi(-I_2, -\mathrm{P})$

### アフィン変換の決定

同一直線上にない3点 $\mathrm{A}, \mathrm{B}, \mathrm{C}$ に対して, アフィン変換 $F$ で

$$F(\mathrm{A})=\mathrm{P}, \quad F(\mathrm{B})=\mathrm{Q}, \quad F(\mathrm{C})=\mathrm{R}$$

を満たすものが唯一存在する. つまり, 2次正方行列 $M$ と2次ベクトル $\boldsymbol{v}$ で

* $M \boldsymbol{a}+\boldsymbol{v}=\boldsymbol{p}$
* $M \boldsymbol{b}+\boldsymbol{v}=\boldsymbol{q}$
* $M \boldsymbol{c}+\boldsymbol{v}=\boldsymbol{r}$

を満たすものを求める. 式を引くことによって,

$$M (\boldsymbol{b}-\boldsymbol{a}, \boldsymbol{c}-\boldsymbol{a})=(\boldsymbol{q}-\boldsymbol{p}, \boldsymbol{r}-\boldsymbol{p})$$

である. $\mathrm{A}, \mathrm{B}, \mathrm{C}$ は同一直線上にない3点なので, 行列 $X:=(\boldsymbol{b}-\boldsymbol{a}, \boldsymbol{c}-\boldsymbol{b})$ は正則行列である. よって,

$$M=(\boldsymbol{q}-\boldsymbol{p}, \boldsymbol{r}-\boldsymbol{p})X^{-1}$$

である.

そして, $M \boldsymbol{a}+\boldsymbol{v}=\boldsymbol{p}$ を利用して $\boldsymbol{v}$ も求められる.
