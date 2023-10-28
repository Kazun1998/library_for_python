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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.0/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.0/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from Point import *\nfrom Line import *\nfrom Circle import *\nfrom Triangle\
    \ import *\nfrom Polygon import *\n\nclass Affine():\n    def __init__(self,Mat=[[1,0],[0,1]],Vec=[0,0]):\n\
    \        self.Mat=Mat\n        self.Vec=Vec\n\n    def __str__(self):\n      \
    \  return \"Mat: {}, Vec:{}\".format(self.Mat,self.Vec)\n\n    __repr__=__str__\n\
    \n    def __pos__(self):\n        return self\n\n    def __neg__(self):\n    \
    \    [[a,b],[c,d]]=self.Mat\n        x,y=self.Vec\n        return Affine([[-a,-b],[-c,-d]],[-x,-y])\n\
    \n    def __add__(self,other):\n        M=[[0,0],[0,0]]\n        M[0][0]=self.Mat[0][0]+other.Mat[0][0]\n\
    \        M[0][1]=self.Mat[0][1]+other.Mat[0][1]\n        M[1][0]=self.Mat[1][0]+other.Mat[1][0]\n\
    \        M[1][1]=self.Mat[1][1]+other.Mat[1][1]\n\n        v=[self.Vec[0]+other.Vec[0],\
    \ self.Vec[1]+other.Vec[1]]\n\n        return Affine(M,v)\n\n    def __sub__(self,other):\n\
    \        M=[[0,0],[0,0]]\n        M[0][0]=self.Mat[0][0]-other.Mat[0][0]\n   \
    \     M[0][1]=self.Mat[0][1]-other.Mat[0][1]\n        M[1][0]=self.Mat[1][0]-other.Mat[1][0]\n\
    \        M[1][1]=self.Mat[1][1]-other.Mat[1][1]\n\n        v=[self.Vec[0]-other.Vec[0],\
    \ self.Vec[1]-other.Vec[1]]\n\n        return Affine(M,v)\n\n    def __mul__(self,other):\n\
    \        M=[[0,0],[0,0]]\n        M[0][0]=self.Mat[0][0]*other.Mat[0][0]+self.Mat[0][1]*other.Mat[1][0]\n\
    \        M[0][1]=self.Mat[0][0]*other.Mat[0][1]+self.Mat[0][1]*other.Mat[1][1]\n\
    \        M[1][0]=self.Mat[1][0]*other.Mat[0][0]+self.Mat[1][1]*other.Mat[1][0]\n\
    \        M[1][1]=self.Mat[1][0]*other.Mat[0][1]+self.Mat[1][1]*other.Mat[1][1]\n\
    \n        v=[\n            self.Mat[0][0]*other.Vec[0]+self.Mat[0][1]*other.Vec[1]+self.Vec[0],\n\
    \            self.Mat[1][0]*other.Vec[0]+self.Mat[1][1]*other.Vec[1]+self.Vec[1]\n\
    \            ]\n        return Affine(M,v)\n\n    def __pow__(self,n):\n     \
    \   if n<0:\n            return pow(self,-n).inverse()\n\n        A=self\n   \
    \     B=Affine()\n        while n:\n            if n&1:\n                B*=A\n\
    \            n>>=1\n            A*=A\n        return  B\n\n    def __eq__(self,other):\n\
    \        return self.Mat==other.Mat and self.Vec==other.Vec\n\n    def inverse(self):\n\
    \        [[a,b],[c,d]]=self.Mat\n        x,y=self.Vec\n\n        det=a*d-b*c\n\
    \        p,q,r,s=d/det,-b/det,-c/det,a/det\n        return Affine([[p,q],[r,s]],[-(p*x+q*y),\
    \ -(r*x+s*y)])\n\n    def integerization(self,delta=1e-7):\n        for i in [0,1]:\n\
    \            for j in [0,1]:\n                if abs(self.Mat[i][j]-floor(self.Mat[i][j]+0.5))<delta:\n\
    \                    self.Mat[i][j]=floor(self.Mat[i][j]+0.5)\n\n        if abs(self.Vec[0]-floor(self.Vec[0]+0.5))<delta:\n\
    \            self.Vec[0]=floor(self.Vec[0]+0.5)\n\n        if abs(self.Vec[1]-floor(self.Vec[1]+0.5))<delta:\n\
    \            self.Vec[1]=floor(self.Vec[1]+0.5)\n\n    def __getitem__(self,shape):\n\
    \        return Action(self,shape)\n\n#=== \u4F5C\u7528\ndef Action(A: Affine,S):\n\
    \    \"\"\" \u30A2\u30D5\u30A3\u30F3\u5909\u63DB A \u306B\u56F3\u5F62 S \u3092\
    \u4F5C\u7528\u3055\u305B\u308B.\n\n    A: Affine\n    S: \u56F3\u5F62 (Point,\
    \ Line_Segment, Triangle)\n    \"\"\"\n\n    if isinstance(S,Point):\n       \
    \ [[a,b],[c,d]]=A.Mat\n        u,v=A.Vec\n        return Point(a*S.x+b*S.y+u,\
    \ c*S.x+d*S.y+v)\n    elif isinstance(S,Segment):\n        return Segment(Action(A,S.begin),Action(A,S.end))\n\
    \    elif isinstance(S,Ray):\n        return Ray(Action(A,S.begin),Action(A,S.end))\n\
    \    elif isinstance(S,Line):\n        return Line(Action(A,S.begin),Action(A,S.end))\n\
    \    elif isinstance(S,Circle):\n        pass\n    elif isinstance(S,Triangle):\n\
    \        return Triangle(Action(A,S.A), Action(A,S.B), Action(A,S.C))\n    elif\
    \ isinstance(S,Polygon):\n        return Polygon(*[Action(A,p) for p in S.vertices])\n\
    \n#=== \u30A2\u30D5\u30A3\u30F3\u5909\u63DB\u306E\u751F\u6210\ndef Translation(x,y):\n\
    \    \"\"\" (x,y) \u3060\u3051\u5E73\u884C\u79FB\u52D5\u3055\u305B\u308B\u30A2\
    \u30D5\u30A3\u30F3\u5909\u63DB\u3092\u751F\u6210\u3059\u308B.\n    \"\"\"\n\n\
    \    return Affine(Vec=[x,y])\n\ndef Point_Reflection(x=0,y=0):\n    \"\"\" \u70B9\
    \ (x,y) \u306B\u95A2\u3059\u308B\u5BFE\u79F0\u79FB\u52D5\u3092\u3059\u308B\u30A2\
    \u30D5\u30A3\u30F3\u5909\u63DB\u3092\u751F\u6210\u3059\u308B.\n    \"\"\"\n\n\
    \    return Affine([[-1,0],[0,-1]],[2*x,2*y])\n\ndef Line_Reflection(a,b,c):\n\
    \    \"\"\" \u76F4\u7DDA ax+by+c=0 \u306B\u95A2\u3059\u308B\u5BFE\u79F0\u79FB\u52D5\
    \u3092\u3059\u308B\u30A2\u30D5\u30A3\u30F3\u5909\u63DB\u3092\u751F\u6210\u3059\
    \u308B.\n    \"\"\"\n\n    assert (a!=0) or (b!=0)\n\n    k=a*a+b*b\n\n    p=(-a*a+b*b)/k;\
    \ q=-2*a*b/k; r=-2*c/k\n    return Affine([[p,q],[q,-p]],[a*r,b*r])\n\ndef Rotation(theta,Px=0,Py=0):\n\
    \    \"\"\" \u70B9 P=(Px,Py) \u5468\u308A\u3067 theta (\u6642\u8A08\u56DE\u308A\
    ) \u306B\u56DE\u8EE2\u3055\u305B\u308B\u30A2\u30D5\u30A3\u30F3\u5909\u63DB\u3092\
    \u751F\u6210\u3059\u308B.\n    \"\"\"\n    c=cos(theta); s=sin(theta)\n    return\
    \ Affine([[c,-s],[s,c]], [(1-c)*Px+s*Py,-s*Px+(1-c)*Py])\n\n#=== \u30A2\u30D5\u30A3\
    \u30F3\u5909\u63DB\u306E\u6C7A\u5B9A\ndef Translation_and_Rotate_Affine_Determine(A,B,P,Q):\n\
    \    \"\"\" F(A)=P, F(B)=Q \u3068\u306A\u308B\u30A2\u30D5\u30A3\u30F3\u5909\u63DB\
    \ F \u306E\u3046\u3061, \u5E73\u884C\u79FB\u52D5\u3068\u56DE\u8EE2\u3067\u751F\
    \u6210\u3055\u308C\u308B\u3082\u306E\u3092\u751F\u6210\u3059\u308B.\n\n    A,B,P,Q:\
    \ Point\n    \u203B |AB|=|PQ| \u3067\u306A\u304F\u3066\u306F\u306A\u3089\u306A\
    \u3044.\n    \"\"\"\n\n    ep=max_ep(A,B,P,Q)\n\n    assert abs(B-A)==abs(Q-P)\n\
    \n\n    return Rotation(Arg(Q,P)-Arg(B,A),*P)*Translation(*(P-A))\n\ndef Affine_Determine(A,B,C,P,Q,R):\n\
    \    \"\"\" F(A)=P, F(B)=Q, F(C)=R \u3068\u306A\u308B\u30A2\u30D5\u30A3\u30F3\u5909\
    \u63DB F \u3092\u6C42\u3081\u308B.\n\n    A,B,C,P,Q,R: Point\n    \u203B A,B,C\
    \ \u306F\u540C\u4E00\u76F4\u7DDA\u4E0A\u306E\u70B9\u3067\u3042\u3063\u3066\u306F\
    \u3044\u3051\u306A\u3044.\n    \"\"\"\n\n    ep=max_ep(A,B,C,P,Q,R)\n\n    assert\
    \ compare((B-A).det(C-A),0,ep)\n\n    q1,q2=Q-P; r1,r2=R-P\n    b1,b2=B-A; c1,c2=C-A;\
    \ det=b1*c2-b2*c1\n\n    M=[\n        [(q1*c2-r1*b2)/det, (-q1*c1+r1*b1)/det],\n\
    \        [(q2*c2-r2*b2)/det, (-q2*c1+r2*b1)/det]\n        ]\n\n    v=[P.x-(M[0][0]*A.x+M[0][1]*A.y),\
    \ P.y-(M[1][0]*A.x+M[1][1]*A.y)]\n\n    return Affine(M,v)\n"
  dependsOn: []
  isVerificationFile: false
  path: Geometric/Affine.py
  requiredBy: []
  timestamp: '2021-08-20 04:19:27+09:00'
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
