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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.2/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.2/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from Point import *\n\nclass Triangle():\n    __slots__=[\"A\",\"B\",\"C\"\
    ,\"id\"]\n    ep=1e-9\n    def __init__(self,A,B,C):\n        \"\"\" 3\u70B9 A,B,C\
    \ \u3092\u9802\u70B9\u3068\u3059\u308B\u4E09\u89D2\u5F62\u3092\u751F\u6210\u3059\
    \u308B.\n\n        A,B,C: Point\n        \"\"\"\n\n        assert A!=B and B!=C\
    \ and C!=A\n        self.A=A\n        self.B=B\n        self.C=C\n        self.id=6\n\
    \n    def __str__(self):\n        return \"[Triangle] {}, {}, {}\".format(self.A,self.B,self.C)\n\
    \n    __repr__=__str__\n\n    def area(self):\n        return abs((self.B-self.A).det(self.C-self.A)/2)\n\
    \n    def three_edges(self):\n        \"\"\" \u8FBA BC, CA, AB \u306E\u9577\u3055\
    \u3092\u6C42\u3081\u308B.\n\n        \"\"\"\n        return abs(self.B-self.C),abs(self.C-self.A),abs(self.A-self.B)\n\
    \n#=== \u4E09\u89D2\u5F62\u306E\u5FC3\ndef Center_of_Gravity(T):\n    \"\"\" \u4E09\
    \u89D2\u5F62 T \u306E\u91CD\u5FC3\u3092\u6C42\u3081\u308B.\n\n    T: Triangle\n\
    \    \"\"\"\n\n    return (T.A+T.B+T.C)/3\n\ndef CircumCenter(T):\n    \"\"\"\
    \ \u4E09\u89D2\u5F62 T \u306E\u5916\u5FC3\u3092\u6C42\u3081\u308B.\n\n    T: Triangle\n\
    \    \"\"\"\n\n    da=(T.B-T.C).norm_2()\n    db=(T.C-T.A).norm_2()\n    dc=(T.A-T.B).norm_2()\n\
    \    ta=da*(-da+db+dc)\n    tb=db*(da-db+dc)\n    tc=dc*(da+db-dc)\n    s=ta+tb+tc\n\
    \    return (ta/s)*T.A+(tb/s)*T.B+(tc/s)*T.C\n\ndef InnerCenter(T):\n    \"\"\"\
    \ \u4E09\u89D2\u5F62 T \u306E\u5185\u5FC3\u3092\u6C42\u3081\u308B.\n\n    T: Triangle\n\
    \    \"\"\"\n    a,b,c=T.three_edges()\n    return (a*T.A+b*T.B+c*T.C)/(a+b+c)\n\
    \ndef OrthoCenter(T):\n    \"\"\" \u4E09\u89D2\u5F62 T \u306E\u5782\u5FC3\u3092\
    \u6C42\u3081\u308B.\n\n    T: Triangle\n    \"\"\"\n    return T.A+T.B+T.C-2*CircumCenter(T)\n\
    \ndef Excenter(T):\n    \"\"\" \u4E09\u89D2\u5F62 T \u306E\u508D\u5FC3 (3\u500B\
    ) \u3092\u6C42\u3081\u308B.\n\n    T: Triangle\n    \"\"\"\n    a,b,c=T.three_edges()\n\
    \    Ea=(-a*T.A+b*T.B+c*T.C)/(-a+b+c)\n    Eb=(a*T.A-b*T.B+c*T.C)/(a-b+c)\n  \
    \  Ec=(a*T.A+b*T.B-c*T.C)/(a+b-c)\n    return [Ea,Eb,Ec]\n\n#=== \u4E09\u89D2\u5F62\
    \u306E\u5F62\u72B6\ndef is_Acute_Triangle(T):\n    \"\"\" \u4E09\u89D2\u5F62 T\
    \ \u304C\u92ED\u89D2\u4E09\u89D2\u5F62\u304B\u3069\u3046\u304B\u3092\u5224\u5B9A\
    \u3059\u308B.\n\n    T: Triangle\n    \"\"\"\n\n    a,b,c=T.three_edges()\n  \
    \  m=max(a,b,c)\n    return compare(a*a+b*b+c*c-2*m*m,0,T.ep)==1\n\ndef is_Right_Triangle(T):\n\
    \    \"\"\" \u4E09\u89D2\u5F62 T \u304C\u76F4\u89D2\u4E09\u89D2\u5F62\u304B\u3069\
    \u3046\u304B\u3092\u5224\u5B9A\u3059\u308B.\n\n    T: Triangle\n    \"\"\"\n\n\
    \    a,b,c=T.three_edges()\n    m=max(a,b,c)\n    return compare(a*a+b*b+c*c-2*m*m,0,T.ep)==0\n\
    \ndef is_Obtuse_Triangle(T):\n    \"\"\" \u4E09\u89D2\u5F62 T \u304C\u920D\u89D2\
    \u4E09\u89D2\u5F62\u304B\u3069\u3046\u304B\u3092\u5224\u5B9A\u3059\u308B.\n\n\
    \    T: Triangle\n    \"\"\"\n\n    a,b,c=T.three_edges()\n    m=max(a,b,c)\n\
    \    return compare(a*a+b*b+c*c-2*m*m,0,T.ep)==-1\n\ndef Triangle_Division_by_Angle(T):\n\
    \    \"\"\" \u4E09\u89D2\u5F62 T \u304C\u92ED\u89D2\u304B\u76F4\u89D2\u304B\u920D\
    \u89D2\u304B\u3092\u5224\u5B9A\u3059\u308B.\n\n    [Input]\n    T: Triangle\n\n\
    \    [Output]\n    1: \u92ED\u89D2, 0: \u76F4\u89D2, -1: \u920D\u89D2\n    \"\"\
    \"\n\n    a,b,c=T.three_edges()\n    m=max(a,b,c)\n    return compare(a*a+b*b+c*c-2*m*m,0,T.ep)\n\
    \ndef is_Isosceles_Triangle(T):\n    \"\"\" \u4E09\u89D2\u5F62 T \u304C\u4E8C\u7B49\
    \u8FBA\u4E09\u89D2\u5F62\u304B\u3092\u5224\u5B9A\u3059\u308B.\n\n    [Input]\n\
    \    T: Triangle\n    \"\"\"\n\n    a,b,c=T.three_edges()\n    return compare(a,b,T.ep)==0\
    \ or compare(b,c,T.ep)==0 or compare(c,a,T.ep)==0\n\ndef is_Isosceles_Right_Triangle(T):\n\
    \    \"\"\" \u4E09\u89D2\u5F62 T \u304C\u76F4\u89D2\u4E8C\u7B49\u8FBA\u4E09\u89D2\
    \u5F62\u304B\u3092\u5224\u5B9A\u3059\u308B.\n\n    [Input]\n    T: Triangle\n\
    \    \"\"\"\n\n    return is_Right_Triangle(T) and is_Isosceles_Triangle(T)\n\n\
    \ndef is_Equilateral_Triangle(T):\n    \"\"\" \u4E09\u89D2\u5F62 T \u304C\u6B63\
    \u4E09\u89D2\u5F62\u304B\u3092\u5224\u5B9A\u3059\u308B.\n\n    [Input]\n    T:\
    \ Triangle\n    \"\"\"\n\n    a,b,c=T.three_edges()\n    return compare(a,b,T.ep)==0\
    \ and compare(b,c,T.ep)==0 and compare(c,a,T.ep)==0\n\n#=== \u4E09\u89D2\u5F62\
    \u306E\u6C7A\u5B9A\ndef SSS_Triangle(a, b, c):\n    \"\"\" 3 \u8FBA\u306E\u9577\
    \u3055\u304C a,b,c \u3067\u3042\u308B\u4E09\u89D2\u5F62\u3092\u751F\u6210\u3059\
    \u308B.\n\n    a,b,c: int or float\n    \"\"\"\n    assert 2*max(a,b,c)<a+b+c\n\
    \n    t=a+b+c\n\n    A=Point(); B=Point(c,0)\n    C=Point((-a*a+b*b+c*c)/(2*c),\
    \ sqrt(t*(t-2*a)*(t-2*b)*(t-2*c))/(2*c))\n    return Triangle(A,B,C)\n\ndef SAS_Triangle(a,\
    \ gamma, b):\n    \"\"\" 2 \u8FBA\u306E\u9577\u3055\u304C a,b \u3067 ,\u9593\u306E\
    \u89D2\u5EA6\u304C gamma \u3067\u3042\u308B\u4E09\u89D2\u5F62\u3092\u751F\u6210\
    \u3059\u308B.\n\n    a,b: int or float\n    gamma: int or float\n    \"\"\"\n\n\
    \    t=sqrt(a*a+b*b-2*a*b*cos(gamma))\n\n    A=Point(); B=Point(t,0)\n    C=Point((b*b-a*b*cos(gamma))/t,\
    \ (a*b*sin(gamma))/t)\n    return Triangle(A,B,C)\n\ndef ASA_Triangle(alpha ,c,\
    \ beta):\n    \"\"\" 1\u8FBA\u306E\u9577\u3055\u304C c \u3067, \u4E21\u7AEF\u306E\
    \u89D2\u5EA6\u304C alpha, beta \u3067\u3042\u308B\u4E09\u89D2\u5F62\u3092\u751F\
    \u6210\u3059\u308B.\n\n    c: int or float\n    alpha, beta: int or float (alpha+beta<pi)\n\
    \    \"\"\"\n\n    assert alpha+beta<pi\n    t=sin(beta)/sin(alpha+beta)\n\n \
    \   A=Point(); B=Point(c,0)\n    C=Point(c*t*cos(alpha), c*t*sin(alpha))\n   \
    \ return Triangle(A,B,C)\n\ndef AAS_Triangle(alpha, beta, a):\n    \"\"\" 1\u8FBA\
    \u306E\u9577\u3055\u304C a \u3067, 2\u3064\u306E\u89D2\u304C alpha, beta \u3067\
    \u3042\u308B\u4E09\u89D2\u5F62\u3092\u751F\u6210\u3059\u308B (a \u306E\u5BFE\u89D2\
    \u304C alpha).\n\n    a: int or float\n    alpha ,beta: int or float\n    \"\"\
    \"\n\n    assert alpha+beta<pi\n\n    A=Point(); B=Point(a*sin(alpha+beta)/sin(alpha),0)\n\
    \    C=Point(a*sin(beta)*cos(alpha)/ sin(alpha), a*sin(beta))\n    return Triangle(A,B,C)\n"
  dependsOn: []
  isVerificationFile: false
  path: Geometric/Triangle.py
  requiredBy: []
  timestamp: '2022-02-28 18:37:36+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Geometric/Triangle.py
layout: document
redirect_from:
- /library/Geometric/Triangle.py
- /library/Geometric/Triangle.py.html
title: Geometric/Triangle.py
---
