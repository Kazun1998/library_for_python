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
  code: "from Point import *\n\nclass Segment():\n    __slots__=[\"begin\",\"end\"\
    ,\"id\"]\n\n    ep=1e-9\n    def __init__(self,P,Q):\n        \"\"\"2\u70B9 P,\
    \ Q (P!=Q) \u3092\u7AEF\u70B9\u3068\u3059\u308B\u7DDA\u5206\u3092\u751F\u6210\u3059\
    \u308B.\n\n        P,Q: Point\n        \"\"\"\n        assert P!=Q\n        self.begin=P\n\
    \        self.end=Q\n        self.id=2\n\n    def __str__(self):\n        return\
    \ \"[Segment] {}, {}\".format(self.begin,self.end)\n\n    __repr__=__str__\n\n\
    \    def __eq__(self,other):\n        return (\n            (self.begin==other.begin)\
    \ and (self.end==other.end) or\n            (self.begin==other.end) and (self.end==other.begin)\n\
    \            )\n\n    def __contains__(self,point):\n        return iSP(self.begin,self.end,point)==2\n\
    \n    def vectorize(self):\n        return self.end-self.begin\n\n    def counter_vectorize(self):\n\
    \        return self.begin-self.end\n\nclass Ray():\n    __slots__=[\"begin\"\
    ,\"end\",\"id\"]\n\n    ep=1e-9\n    def __init__(self,P,Q):\n        \"\"\" P\
    \ \u3092\u7AEF\u70B9\u3068\u3057, Q \u3092\u901A\u308B\u534A\u76F4\u7DDA\u3092\
    \u901A\u308B.\n\n        P,Q: Point\n        \"\"\"\n        assert P!=Q\n   \
    \     self.begin=P\n        self.end=Q\n        self.id=3\n\n    def __str__(self):\n\
    \        return \"[Ray] {} -> {}\".format(self.begin,self.end)\n\n    __repr__=__str__\n\
    \n    def __eq__(self,other):\n        if self.begin!=other.begin:\n         \
    \   return False\n\n        m=iSP(self.begin,self.end,other.end)\n        return\
    \ m==0 or m==2\n\n    def __contains__(self,point):\n        m=iSP(self.begin,self.end,point)\n\
    \        return m==0 or m==2\n\n    def vectorize(self):\n        return self.end-self.begin\n\
    \n    def counter_vectorize(self):\n        return self.begin-self.end\n\nclass\
    \ Line():\n    __slots__=[\"begin\",\"end\",\"id\"]\n\n    ep=1e-9\n    def __init__(self,P,Q):\n\
    \        \"\"\"2\u70B9 P, Q (P!=Q) \u3092\u901A\u308B\u76F4\u7DDA\u3092\u751F\u6210\
    \u3059\u308B.\n\n        P,Q: Point\n        \"\"\"\n        assert P!=Q\n   \
    \     self.begin=P\n        self.end=Q\n        self.id=4\n\n    def __str__(self):\n\
    \        return \"[Line] {}, {}\".format(self.begin,self.end)\n\n    __repr__=__str__\n\
    \n    def __eq__(self,other):\n        a=self.begin; b=self.end; c=other.begin;\
    \ d=other.end\n        return (b-a).det(c-d)==0 and (b-a).det(c-a)==0\n\n    def\
    \ __contains__(self,point):\n        return abs(iSP(self.begin,point,self.end))!=1\n\
    \n    def vectorize(self):\n        return self.end-self.begin\n\n    def counter_vectorize(self):\n\
    \        return self.begin-self.end\n\n#=== \u751F\u6210\ndef Line_from_General_Form(a,b,c):\n\
    \    \"\"\" ax+by+c=0 \u3068\u3044\u3046\u5F62\u306E\u76F4\u7DDA\u3092\u751F\u6210\
    \u3059\u308B.\n\n    a,b,c: int or float ((a,b) neq (0,0))\n    \"\"\"\n\n   \
    \ assert (a!=0) or (b!=0)\n\n    k=sqrt(a*a+b*b)\n\n    if b==0:\n        x=-c/a;\
    \ y=0\n    else:\n        x=0; y=-c/b\n\n    return Line(Point(x,y),Point(x-b/k,\
    \ y+a/k))\n\n#=== \u4E00\u822C\u5F62\ndef General_Form_from_Line(L, lattice=False):\n\
    \    \"\"\" \u76F4\u7DDA L \u304C\u6E80\u305F\u3059\u5F0F ax+by+c=0 \u306E a,b,c\
    \ \u3092\u6C42\u3081\u308B.\n    \"\"\"\n\n    s=L.begin.x; t=L.begin.y\n    v=L.vectorize();\
    \ alpha=v.x; beta=v.y\n\n    sgn=compare(beta,0,L.ep)\n    if sgn==0:\n      \
    \  sgn=compare(-alpha,0,L.ep)\n\n    k=alpha*t-beta*s\n    if lattice:\n     \
    \   g=gcd(gcd(alpha,beta),k)\n        alpha//=g; beta//=g; k//=g\n\n    return\
    \ (sgn*beta,sgn*(-alpha),sgn*k)\n\n#=== \u4EA4\u5DEE\u5224\u5B9A\ndef has_Intersection_between_Segment_and_Segment(L,M,endpoint=True):\n\
    \    \"\"\" \u7DDA\u5206 L,M \u304C\u4EA4\u308F\u308B\u304B\u3069\u3046\u304B\u3092\
    \u5224\u5B9A\u3059\u308B.\n\n    L,M: \u76F4\u7DDA\n    \"\"\"\n\n    a=L.begin;\
    \ b=L.end; c=M.begin; d=M.end\n    if not(iSP(a,b,c)*iSP(a,b,d)<=0 and iSP(c,d,a)*iSP(c,d,b)<=0):\n\
    \        return False\n\n    if endpoint:\n        return True\n\ndef has_Intersection_between_Line_and_Segment(L,M,endpoint=True):\n\
    \    \"\"\" \u76F4\u7DDA L \u3068\u7DDA\u5206 M \u304C\u4EA4\u308F\u308B\u304B\
    \u3069\u3046\u304B\u3092\u5224\u5B9A\u3059\u308B.\n\n    L: \u76F4\u7DDA\n   \
    \ M: \u7DDA\u5206\n    \"\"\"\n\n    a=L.begin; b=L.end; c=M.begin; d=M.end\n\
    \    return iSP(a,b,c)*iSP(a,b,d)<=0\n\ndef has_Intersection_between_Line_and_Line(L,M):\n\
    \    \"\"\" \u76F4\u7DDA L,M \u304C\u4EA4\u308F\u308B\u304B\u3069\u3046\u304B\u3092\
    \u5224\u5B9A\u3059\u308B.\n\n    L,M: \u76F4\u7DDA\n    \"\"\"\n\n    return compare(L.vectorize().det(M.vectorize()),0,max(L.ep,M.ep))!=0\n\
    \n#=== \u4EA4\u70B9\u3092\u6C42\u3081\u308B\ndef Intersection_between_Line_and_Line(L,M,Mode=False):\n\
    \    \"\"\" \u76F4\u7DDA L,M \u306E\u4EA4\u70B9\u3092\u6C42\u3081\u308B.\n\n \
    \   L,M: \u76F4\u7DDA\n    Mode=False: \u4EA4\u70B9\u304C\u4E00\u610F\u306B\u5B9A\
    \u307E\u3089\u306A\u3044\u5834\u5408\u30A8\u30E9\u30FC\u3092\u5410\u304F.\n  \
    \  Mode=True: \u4E00\u81F4\u3059\u308B\u5834\u5408, True, \u4EA4\u70B9\u304C\u5B58\
    \u5728\u3057\u306A\u3044\u5834\u5408 False \u3092\u8FD4\u3059.\n    \"\"\"\n\n\
    \    if L==M:\n        if Mode:\n            return True\n        else:\n    \
    \        assert 0,\"\u76F4\u7DDA\u304C\u4E00\u81F4\u3057\u307E\u3059\"\n    if\
    \ is_Parallel(L,M):\n        if Mode:\n            return False\n        else:\n\
    \            assert 0,\"\u4EA4\u70B9\u304C\u5B58\u5728\u307E\u305B\u3093\"\n\n\
    \    a=L.begin; b=L.end; c=M.begin; d=M.end\n    k=(c-a).det(d-c)/(b-a).det(d-c)\n\
    \    return a+k*(b-a)\n\n#=== \u5782\u76F4\u4E8C\u7B49\u5206\u7DDA\ndef Perpendicular_Bisector(S,\
    \ lattice=False):\n    \"\"\" \u7DDA\u5206 S \u306E\u5782\u76F4\u4E8C\u7B49\u5206\
    \u7DDA\u3092\u6C42\u3081\u308B.\"\"\"\n\n    u=S.vectorize()\n\n    M=S.begin+S.end\n\
    \    if lattice:\n        M.x//=2; M.y//=2\n    else:\n        M.x/=2; M.y/=2\n\
    \    return Line(M,M+u*Point(0,1))\n\n#=== 2\u76F4\u7DDA\u306E\u95A2\u4FC2\ndef\
    \ is_Parallel(L,M):\n    \"\"\"2\u3064\u306E\u76F4\u7DDA (\u7DDA\u5206) L,M \u304C\
    \u5E73\u884C\u304B\u3069\u3046\u304B\u3092\u5224\u5B9A\u3059\u308B.\n\n    L,M:\
    \ \u76F4\u7DDA or \u7DDA\u5206\n    \"\"\"\n\n    u=L.vectorize(); v=M.vectorize()\n\
    \    return compare(u.det(v),0,max(L.ep,M.ep))==0\n\ndef is_Orthogonal(L,M):\n\
    \    \"\"\"2\u3064\u306E\u76F4\u7DDA (\u7DDA\u5206) L,M \u304C\u76F4\u884C\u3059\
    \u308B\u304B\u3069\u3046\u304B\u3092\u5224\u5B9A\u3059\u308B.\n\n    L,M: \u76F4\
    \u7DDA or \u7DDA\u5206\n    \"\"\"\n\n    u=L.vectorize(); v=M.vectorize()\n \
    \   return compare(u.dot(v),0,max(L.ep,M.ep))==0\n\n#=== \u70B9\u3068\u306E\u8DDD\
    \u96E2\ndef Distance_between_Point_and_Segment(P,L):\n    \"\"\" \u70B9 P \u3068\
    \u7DDA\u5206 L \u306E\u8DDD\u96E2\u3092\u6C42\u3081\u308B.\n\n    \"\"\"\n\n \
    \   A=L.begin; B=L.end\n    if Angle_Type(P,A,B)==-1:\n        return abs(P-A)\n\
    \    elif Angle_Type(P,B,A)==-1:\n        return abs(P-B)\n    else:\n       \
    \ v=L.vectorize()\n        return abs((P-L.begin).det(v)/abs(v))\n\ndef Distance_between_Point_and_Line(P,L):\n\
    \    \"\"\" \u70B9 P \u3068\u76F4\u7DDA L \u306E\u8DDD\u96E2\u3092\u6C42\u3081\
    \u308B.\n\n    \"\"\"\n\n    v=L.vectorize()\n    return abs((P-L.begin).det(v)/abs(v))\n\
    \n#=== \u7DDA\u540C\u58EB\u306E\u8DDD\u96E2\ndef Distance_between_Line_and_Line(L,M):\n\
    \    \"\"\" 2\u76F4\u7DDA L,M \u306E\u8DDD\u96E2\u3092\u6C42\u3081\u308B.\n\n\
    \    L,M: \u76F4\u7DDA\n    \"\"\"\n\n    if is_Parallel(L,M):\n        return\
    \ Distance_between_Point_and_Line(L.begin,M)\n    else:\n        return 0\n\n\
    def Distance_between_Line_and_Segment(L,M):\n    \"\"\" \u76F4\u7DDA L \u3068\u7DDA\
    \u5206 M \u306E\u8DDD\u96E2\u3092\u6C42\u3081\u308B.\n\n    L: \u76F4\u7DDA, M:\
    \ \u7DDA\u5206\n    \"\"\"\n\n    if has_Intersection_between_Line_and_Segment(L,M):\n\
    \        return 0\n    else:\n        return min(\n            Distance_between_Point_and_Line(M.begin,\
    \ L),\n            Distance_between_Point_and_Line(M.end, L)\n            )\n\n\
    def Distance_between_Segment_and_Segment(L,M):\n    \"\"\" 2\u7DDA\u5206 L,M \u306E\
    \u8DDD\u96E2\u3092\u6C42\u3081\u308B.\n\n    L,M: \u7DDA\u5206\n    \"\"\"\n\n\
    \    if has_Intersection_between_Segment_and_Segment(L,M):\n        return 0\n\
    \n    return min(\n        Distance_between_Point_and_Segment(L.begin,M),\n  \
    \      Distance_between_Point_and_Segment(L.end  ,M),\n        Distance_between_Point_and_Segment(M.begin,L),\n\
    \        Distance_between_Point_and_Segment(M.end  ,L)\n        )\n\n#=== \u70B9\
    \u3068\u76F4\u7DDA\u306E\u5E7E\u4F55\ndef Projection(P,L):\n    \"\"\" \u70B9\
    \ P \u306E\u76F4\u7DDA L \u4E0A\u306E\u5C04\u5F71\u3092\u6C42\u3081\u308B.\n\n\
    \    \"\"\"\n\n    v=L.vectorize()\n    return L.begin-((L.begin-P).dot(v)/v.norm_2())*v\n\
    \ndef Reflection(P,L):\n    \"\"\" \u70B9 P \u306E\u76F4\u7DDA L \u306B\u3088\u308B\
    \u53CD\u5C04\u3092\u6C42\u3081\u308B.\n\n    \"\"\"\n\n    return P+2*(Projection(P,L)-P)\n"
  dependsOn: []
  isVerificationFile: false
  path: Geometric/Line.py
  requiredBy: []
  timestamp: '2022-09-10 17:09:03+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Geometric/Line.py
layout: document
redirect_from:
- /library/Geometric/Line.py
- /library/Geometric/Line.py.html
title: Geometric/Line.py
---
