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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.8/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.8/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from math import sqrt,sin,cos,tan,asin,acos,atan2,pi,floor,gcd\n\ndef compare(x,y,ep):\n\
    \    \"\"\" x,y \u306E\u5927\u5C0F\u6BD4\u8F03\u3092\u3059\u308B. \u305F\u3060\
    \u3057, ep \u306E\u8AA4\u5DEE\u306F\u540C\u4E00\u8996\u3059\u308B.\n\n    [Input]\n\
    \    x,y: float\n    ep: float\n\n    [Output]\n    x>y: 1\n    x=y: 0\n    x<y:\
    \ -1\n    \"\"\"\n\n    if x-y>ep: return 1\n    elif x-y<-ep: return -1\n   \
    \ else: return 0\n\ndef max_ep(*X):\n    e=-1\n    for x in X:\n        if x.ep>e:e=x.ep\n\
    \    return e\n\nclass Point():\n    __slots__=[\"x\",\"y\",\"id\"]\n    ep=1e-9\n\
    \n    def __init__(self,x=0,y=0):\n        self.x=x\n        self.y=y\n      \
    \  self.id=0\n\n    def sign(self,a):\n        return compare(a,0,self.ep)\n\n\
    \    #\u6587\u5B57\u5217\n    def __str__(self):\n        return \"({}, {})\"\
    .format(self.x,self.y)\n\n    __repr__=__str__\n\n    #Bool\n    def __bool__(self):\n\
    \        return self.sign(self.x)!=0 or self.sign(self.y)!=0\n\n    #\u7B49\u53F7\
    \n    def __eq__(self,other):\n        return self.sign(self.x-other.x)==0 and\
    \ self.sign(self.y-other.y)==0\n\n    #\u4E0D\u7B49\u53F7\n    def __ne__(self,other):\n\
    \        return not self==other\n\n    #\u6BD4\u8F03(<)\n    def __lt__(self,other):\n\
    \        T=self.sign(self.x-other.x)\n        if T:\n            return T<0\n\
    \        else:\n            return self.sign(self.y-other.y)<0\n\n    #\u6BD4\u8F03\
    (<=)\n    def __le__(self,other):\n        return self<other or self==other\n\n\
    \    #\u6BD4\u8F03(>)\n    def __gt__(self,other):\n        return other<self\n\
    \n    #\u6BD4\u8F03(>=)\n    def __ge__(self,other):\n        return other<=self\n\
    \n    #\u6B63\u3068\u8CA0\n    def __pos__(self):\n        return self\n\n   \
    \ def __neg__(self):\n        return Point(-self.x,-self.y)\n\n    #\u52A0\u6CD5\
    \n    def __add__(self,other):\n        return Point(self.x+other.x,self.y+other.y)\n\
    \n    def __iadd__(self,other):\n        self.x+=other.x\n        self.y+=other.y\n\
    \        return self\n\n    #\u6E1B\u6CD5\n    def __sub__(self,other):\n    \
    \    return Point(self.x-other.x,self.y-other.y)\n\n    def __isub__(self,other):\n\
    \        self.x-=other.x\n        self.y-=other.y\n        return self\n\n   \
    \ #\u4E57\u6CD5\n    def __mul__(self,other):\n        x,y=self.x,self.y\n   \
    \     u,v=other.x,other.y\n        return Point(x*u-y*v,x*v+y*u)\n\n    def __imul__(self,\
    \ other):\n        return other*self\n\n    def __rmul__(self,other):\n      \
    \  if isinstance(other,(int,float)):\n            return Point(other*self.x,other*self.y)\n\
    \n    #\u9664\u6CD5\n    def __truediv__(self,other):\n        if other==0:\n\
    \            raise ZeroDivisionError\n        return Point(self.x/other,self.y/other)\n\
    \n    #\u7D76\u5BFE\u5024\n    def __abs__(self):\n        return sqrt(self.x*self.x+self.y*self.y)\n\
    \n    norm=__abs__\n\n    def norm_2(self):\n        return self.x*self.x+self.y*self.y\n\
    \n    #\u56DE\u8EE2\n    def rotate(self,theta):\n        x,y=self.x,self.y\n\
    \        s,c=sin(theta),cos(theta)\n        return Point(c*x-s*y,s*x+c*y)\n\n\
    \    def __iter__(self):\n        yield self.x\n        yield self.y\n\n    def\
    \ __hash__(self):\n        return hash((self.x,self.y))\n\n    def latticization(self,delta=1e-7):\n\
    \        \"\"\" \u683C\u5B50\u70B9\u306B\u5341\u5206\u8FD1\u3044\u306A\u3089\u3070\
    , \u305D\u306E\u683C\u5B50\u70B9\u306B\u5438\u3044\u5BC4\u305B\u308B\"\"\"\n\n\
    \        if abs(self.x-floor(self.x+0.5))<delta and abs(self.y-floor(self.y+0.5))<delta:\n\
    \            self.x=floor(self.x+0.5)\n            self.y=floor(self.y+0.5)\n\n\
    \    def normalization(self):\n        a=abs(self)\n        self.x/=a\n      \
    \  self.y/=a\n\n    def normal_unit_vector(self):\n        \"\"\" \u5358\u4F4D\
    \u6CD5\u7DDA\u30D9\u30AF\u30C8\u30EB\u3092\u6C42\u3081\u308B\"\"\"\n\n       \
    \ assert self\n        d=self.norm()\n        return Point(-self.y/d,self.x/d)\n\
    \n    def dot(self,other):\n        return self.x*other.x+self.y*other.y\n\n \
    \   def det(self,other):\n        return self.x*other.y-self.y*other.x\n\n   \
    \ def arg(self):\n        return atan2(self.y,self.x)\n\n    def copy(self):\n\
    \        return Point(self.x,self.y)\n\ndef iSP(A,B,C):\n    \"\"\" A->B->C \u3068\
    \u9032\u3093\u3060\u3068\u304D\u306E\u9032\u884C\u65B9\u5411\u3092\u898B\u308B\
    . \u203B B \u304C\u4E2D\u5FC3\n\n    A,B,C: Point\n\n    \u5DE6\u6298 (\u53CD\u6642\
    \u8A08\u56DE\u308A):+1\n    \u53F3\u6298 (\u6642\u8A08\u56DE\u308A)   :-1\n  \
    \  C-A-B\u306E\u9806\u306B\u4E26\u3093\u3067\u3044\u308B: -2\n    A-B-C\u306E\u9806\
    \u306B\u4E26\u3093\u3067\u3044\u308B: 2\n    A-C-B\u306E\u9806\u306B\u4E26\u3093\
    \u3067\u3044\u308B: 0\n    \"\"\"\n\n    ep=max_ep(A,B,C)\n    p=compare((B-A).det(C-A),0,ep)\n\
    \    if p==1:\n        return 1\n    elif p==-1:\n        return -1\n    else:\n\
    \        if compare((B-A).dot(C-A),0,ep)==-1:\n            return -2\n       \
    \ if compare((A-B).dot(C-B),0,ep)==-1:\n            return 2\n        return 0\n\
    \ndef Arg(P,Q=Point(0,0)):\n    \"\"\"\u70B9 Q \u304B\u3089\u898B\u305F\u70B9\
    \ P \u306E\u504F\u89D2\u3092\u6C42\u3081\u308B.\n\n    P,Q: Point\n    \"\"\"\n\
    \n    R=P-Q\n    return atan2(R.y,R.x)\n\ndef Angle_Type(A,B,C):\n    \"\"\" \u89D2\
    ABC \u304C\u92ED\u89D2\u304B\u76F4\u89D2\u304B\u920D\u89D2\u304B\u3092\u5224\u5B9A\
    \u3059\u308B.\n\n    [Input]\n    A,B,C: Point\n\n    [Output]\n    1: \u92ED\u89D2\
    , 0: \u76F4\u89D2, -1: \u920D\u89D2\n    \"\"\"\n\n    return compare((A-B).dot(C-B),0,max_ep(A,B,C))\n\
    \ndef Inner(P,Q):\n    \"\"\"\u70B9P,Q\u306E\u5185\u7A4D\u3092\u6C42\u3081\u308B\
    .\n\n    P,Q:Point\n    \"\"\"\n    return P.x*Q.x+P.y*Q.y\n\ndef Det(P,Q):\n\
    \    \"\"\"\u70B9P,Q\u304C\u5F35\u308B\u5E73\u884C\u56DB\u8FBA\u5F62\u306E\u7B26\
    \u53F7\u4ED8\u304D\u9762\u7A4D\u3092\u6C42\u3081\u308B.\n\n    P,Q:Point\n   \
    \ \"\"\"\n    return P.x*Q.y-P.y*Q.x\n\ndef Internal_Division_Point(P,Q,p,q):\n\
    \    \"\"\"\u7DDA\u5206PQ\u3092p:q\u306B\u5185\u5206\u3059\u308B\u70B9\u3092\u6C42\
    \u3081\u308B.\n\n    P,Q:Point\n    p,q:int or float\n    \"\"\"\n    assert p+q\n\
    \    return (q*P+p*Q)/(p+q)\n\ndef External_Division_Point(P,Q,p,q):\n    \"\"\
    \"\u7DDA\u5206PQ\u3092p:q\u306B\u5185\u5206\u3059\u308B\u70B9\u3092\u6C42\u3081\
    \u308B.\n\n    P,Q:Point\n    p,q:int or float\n    \"\"\"\n    assert p-q\n \
    \   return (-q*P+p*Q)/(p-q)\n\ndef MidPoint(P,Q):\n    \"\"\"\u7DDA\u5206PQ\u306E\
    \u4E2D\u70B9\u3092\u6C42\u3081\u308B.\n\n    P,Q:Point\n    \"\"\"\n    a=(P.x+Q.x)/2\n\
    \    b=(P.y+Q.y)/2\n    return Point(a,b)\n\ndef Argument_Compare(P,Q):\n    \"\
    \"\" OQ \u304C OP \u304B\u3089\u307F\u3066\u53CD\u6642\u8A08\u56DE\u308A\u304B\
    \u3069\u3046\u304B\u3092\u5224\u5B9A\u3059\u308B.\"\"\"\n    return compare(Q.det(P),0,max(P.ep,Q.ep))\n\
    \ndef Argument_Sort(L):\n    \"\"\" \u70B9\u3092\u504F\u89D2\u30BD\u30FC\u30C8\
    \u3059\u308B.\n\n    L: \u70B9\u306E\u30EA\u30B9\u30C8\n    \"\"\"\n\n    from\
    \ functools import cmp_to_key\n\n    ep=max_ep(*L)\n    def position(P):\n   \
    \     m=compare(P.y,0,ep)\n        if m==-1:\n            return -1\n        elif\
    \ m==0 and compare(P.x,0,ep)>=0:\n            return 0\n        else:\n      \
    \      return 1\n\n    def cmp(P,Q):\n        a=position(P); b=position(Q)\n \
    \       if a<b: return -1\n        elif a>b: return 1\n        else:return -compare(P.det(Q),0,ep)\n\
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
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Geometric/Point.py
layout: document
title: Point
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
