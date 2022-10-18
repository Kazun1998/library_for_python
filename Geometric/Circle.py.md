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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.7/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.7/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
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
    \        Distance_betweem_Point_and_Segment(c,L),\n        C.radius,\n       \
    \ ep)<=0)\n    flag2=(compare(max(abs(c-L.begin),abs(c-L.end)),C.radius,ep)>=0)\n\
    \    return flag1 and flag2\n\ndef has_Intersection_between_Circle_and_Line(C,L):\n\
    \    \"\"\"\u5186 C \u3068\u76F4\u7DDA L \u306E\u4EA4\u5DEE\u5224\u5B9A\u3092\u884C\
    \u3046.\n\n    \"\"\"\n    return compare(\n        Distance_betweem_Point_and_Line(C.center,L),\n\
    \        C.radius,\n        max(C.ep,L.ep)\n        )<=0\n\ndef has_Intersection_between_Circle_and_Circle(C,D):\n\
    \    \"\"\"2\u3064\u306E\u5186 C,D \u306E\u4EA4\u5DEE\u5224\u5B9A\u3092\u884C\u3046\
    .\n\n    \"\"\"\n\n    r=C.radius; s=D.radius;\n    d=abs(C.center-D.center)\n\
    \    ep=max(C.ep,D.ep)\n\n    return compare(d,abs(r-s),ep)>=0 and compare(d,r+s,ep)<=0\n\
    \n#=== \u4EA4\u70B9\u3092\u6C42\u3081\u308B\ndef Intersection_between_Circle_and_Line(C,L):\n\
    \    \"\"\" \u5186 C \u3068\u76F4\u7DDA L \u306E\u4EA4\u70B9\u3092\u6C42\u3081\
    \u308B.\n\n    \"\"\"\n\n    if not has_Intersection_between_Circle_and_Line(C,L):\n\
    \        return []\n\n    H=Projection(C.Center,L)\n    d=Distance_betweem_Point_and_Line(C.Center,L)\n\
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
  timestamp: '2021-10-01 03:13:23+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Geometric/Circle.py
layout: document
redirect_from:
- /library/Geometric/Circle.py
- /library/Geometric/Circle.py.html
title: Geometric/Circle.py
---