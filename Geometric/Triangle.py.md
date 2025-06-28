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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.13.5/x64/lib/python3.13/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.13.5/x64/lib/python3.13/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from Point import *\n\nclass Triangle():\n    __slots__ = ('A', 'B', 'C')\n\
    \n    def __init__(self, A: Point, B: Point, C: Point):\n        \"\"\" 3 \u70B9\
    \ A, B, C \u3092\u9802\u70B9\u3068\u3059\u308B\u4E09\u89D2\u5F62\u3092\u751F\u6210\
    \u3059\u308B.\n\n        Args:\n            A (Point):\n            B (Point):\n\
    \            C (Point):\n        \"\"\"\n\n        self.A = A\n        self.B\
    \ = B\n        self.C = C\n\n    def __str__(self) -> str:\n        return f\"\
    [Triangle] {self.A}, {self.B}, {self.C}\"\n\n    def __repr__(self) -> str:\n\
    \        return f\"{self.__class__.__name__}({self.A}, {self.B}, {self. C})\"\n\
    \n    def area(self) -> float:\n        return abs((self.B - self.A).det(self.C\
    \ - self.A) / 2)\n\n    def three_edges(self) -> tuple[float, float, float]:\n\
    \        \"\"\" \u8FBA BC, \u8FBA CA, \u8FBA AB \u306E\u9577\u3055\u3092\u51FA\
    \u529B\u3059\u308B.\n\n        Returns:\n            tuple[float, float, float]:\
    \ \u8FBA BC, \u8FBA CA, \u8FBA AB \u306E\u9577\u3055\u306E\u30BF\u30D7\u30EB\n\
    \        \"\"\"\n\n        return abs(self.B - self.C), abs(self.C - self.A),\
    \ abs(self.A - self.B)\n\n#=== \u4E09\u89D2\u5F62\u306E\u5FC3\ndef Center_of_Gravity(T:\
    \ Triangle) -> Point:\n    \"\"\" \u4E09\u89D2\u5F62 T \u306E\u91CD\u5FC3\u3092\
    \u6C42\u3081\u308B\n\n    Args:\n        T (Triangle): \u4E09\u89D2\u5F62\n\n\
    \    Returns:\n        Point: \u4E09\u89D2\u5F62 T \u306E\u91CD\u5FC3\n    \"\"\
    \"\n\n    return (T.A + T.B + T.C) / 3\n\ndef CircumCenter(T: Triangle) -> Point:\n\
    \    \"\"\" \u4E09\u89D2\u5F62 T \u306E\u5916\u5FC3\u3092\u6C42\u3081\u308B\n\n\
    \    Args:\n        T (Triangle): \u4E09\u89D2\u5F62\n\n    Returns:\n       \
    \ Point: \u4E09\u89D2\u5F62 T \u306E\u5916\u5FC3\n    \"\"\"\n\n    da=(T.B-T.C).norm_2()\n\
    \    db=(T.C-T.A).norm_2()\n    dc=(T.A-T.B).norm_2()\n    ta=da*(-da+db+dc)\n\
    \    tb=db*(da-db+dc)\n    tc=dc*(da+db-dc)\n    s=ta+tb+tc\n    return (ta/s)*T.A+(tb/s)*T.B+(tc/s)*T.C\n\
    \ndef InnerCenter(T: Triangle) -> Point:\n    \"\"\" \u4E09\u89D2\u5F62 T \u306E\
    \u5185\u5FC3\u3092\u6C42\u3081\u308B\n\n    Args:\n        T (Triangle): \u4E09\
    \u89D2\u5F62\n\n    Returns:\n        Point: \u4E09\u89D2\u5F62 T \u306E\u5185\
    \u5FC3\n    \"\"\"\n\n    a,b,c=T.three_edges()\n    return (a*T.A+b*T.B+c*T.C)/(a+b+c)\n\
    \ndef OrthoCenter(T: Triangle) -> Point:\n    \"\"\" \u4E09\u89D2\u5F62 T \u306E\
    \u5782\u5FC3\u3092\u6C42\u3081\u308B\n\n    Args:\n        T (Triangle): \u4E09\
    \u89D2\u5F62\n\n    Returns:\n        Point: \u4E09\u89D2\u5F62 T \u306E\u5782\
    \u5FC3\n    \"\"\"\n\n    return T.A+T.B+T.C-2*CircumCenter(T)\n\ndef Excenter(T:\
    \ Triangle) -> tuple[Point, Point, Point]:\n    \"\"\" \u4E09\u89D2\u5F62 T \u306E\
    \u508D\u5FC3 (3 \u500B) \u3092\u6C42\u3081\u308B\n\n    Args:\n        T (Triangle):\
    \ \u4E09\u89D2\u5F62\n\n    Returns:\n        tuple[Point, Point, Point]: \u4E09\
    \u89D2\u5F62 T \u306E\u5782\u5FC3 3\u500B\u306E\u30BF\u30D7\u30EB\n    \"\"\"\n\
    \n    a,b,c=T.three_edges()\n    Ea=(-a*T.A+b*T.B+c*T.C)/(-a+b+c)\n    Eb=(a*T.A-b*T.B+c*T.C)/(a-b+c)\n\
    \    Ec=(a*T.A+b*T.B-c*T.C)/(a+b-c)\n    return (Ea, Eb, Ec)\n\n#=== \u4E09\u89D2\
    \u5F62\u306E\u5F62\u72B6\ndef is_Acute_Triangle(T: Triangle) -> bool:\n    \"\"\
    \" \u4E09\u89D2\u5F62 T \u304C\u92ED\u89D2\u4E09\u89D2\u5F62\u304B\u3069\u3046\
    \u304B\u3092\u5224\u5B9A\u3059\u308B.\n\n    Args:\n        T (Triangle): \u4E09\
    \u89D2\u5F62\n\n    Returns:\n        bool: \u92ED\u89D2\u4E09\u89D2\u5F62 ?\n\
    \    \"\"\"\n\n    a, b, c =  T.three_edges()\n    m = max(a, b, c)\n    return\
    \ compare(a * a + b * b + c * c, 2 * m * m) == 1\n\ndef is_Right_Triangle(T: Triangle)\
    \ -> bool:\n    \"\"\" \u4E09\u89D2\u5F62 T \u304C\u76F4\u89D2\u4E09\u89D2\u5F62\
    \u304B\u3069\u3046\u304B\u3092\u5224\u5B9A\u3059\u308B.\n\n    Args:\n       \
    \ T (Triangle): \u4E09\u89D2\u5F62\n\n    Returns:\n        bool: \u76F4\u89D2\
    \u4E09\u89D2\u5F62 ?\n    \"\"\"\n\n    a, b, c =  T.three_edges()\n    m = max(a,\
    \ b, c)\n    return compare(a * a + b * b + c * c, 2 * m * m) == 0\n\ndef is_Obtuse_Triangle(T:\
    \ Triangle) -> bool:\n    \"\"\" \u4E09\u89D2\u5F62 T \u304C\u920D\u89D2\u4E09\
    \u89D2\u5F62\u304B\u3069\u3046\u304B\u3092\u5224\u5B9A\u3059\u308B.\n\n    Args:\n\
    \        T (Triangle): \u4E09\u89D2\u5F62\n\n    Returns:\n        bool: \u920D\
    \u89D2\u4E09\u89D2\u5F62 ?\n    \"\"\"\n\n    a, b, c =  T.three_edges()\n   \
    \ m = max(a, b, c)\n    return compare(a * a + b * b + c * c, 2 * m * m) == -1\n\
    \ndef Triangle_Division_by_Angle(T: Triangle) -> int:\n    \"\"\" \u4E09\u89D2\
    \u5F62 T \u306E\u5F62\u72B6\u3092\u6C42\u3081\u308B\n\n    Args:\n        T (Triangle):\
    \ \u4E09\u89D2\u5F62\n\n    Returns:\n        int:\n            1: \u92ED\u89D2\
    \u4E09\u89D2\u5F62\n            0: \u76F4\u89D2\u4E09\u89D2\u5F62\n          \
    \  -1: \u920D\u89D2\u4E09\u89D2\u5F62\n    \"\"\"\n\n    a, b, c =  T.three_edges()\n\
    \    m = max(a, b, c)\n    return compare(a * a + b * b + c * c, 2 * m * m)\n\n\
    def is_Isosceles_Triangle(T: Triangle) -> bool:\n    \"\"\" \u4E09\u89D2\u5F62\
    \ T \u304C\u4E8C\u7B49\u8FBA\u4E09\u89D2\u5F62\u304B\u3069\u3046\u304B\u3092\u5224\
    \u5B9A\u3059\u308B.\n\n    Args:\n        T (Triangle): \u4E09\u89D2\u5F62\n\n\
    \    Returns:\n        bool: \u4E8C\u7B49\u8FBA\u4E09\u89D2\u5F62 ?\n    \"\"\"\
    \n\n    a, b, c = T.three_edges()\n    return equal(a, b) or equal(b, c) or equal(c,\
    \ a)\n\ndef is_Isosceles_Right_Triangle(T: Triangle) -> bool:\n    \"\"\" \u4E09\
    \u89D2\u5F62 T \u304C\u76F4\u89D2\u4E8C\u7B49\u8FBA\u4E09\u89D2\u5F62\u304B\u3069\
    \u3046\u304B\u3092\u5224\u5B9A\u3059\u308B.\n\n    Args:\n        T (Triangle):\
    \ \u4E09\u89D2\u5F62\n\n    Returns:\n        bool: \u76F4\u89D2\u4E8C\u7B49\u8FBA\
    \u4E09\u89D2\u5F62 ?\n    \"\"\"\n\n    return is_Right_Triangle(T) and is_Isosceles_Triangle(T)\n\
    \n\ndef is_Equilateral_Triangle(T: Triangle) -> bool:\n    \"\"\" \u4E09\u89D2\
    \u5F62 T \u304C\u6B63\u4E09\u89D2\u5F62\u304B\u3069\u3046\u304B\u3092\u5224\u5B9A\
    \u3059\u308B.\n\n    Args:\n        T (Triangle): \u4E09\u89D2\u5F62\n\n    Returns:\n\
    \        bool: \u6B63\u4E09\u89D2\u5F62 ?\n    \"\"\"\n\n    a, b, c = T.three_edges()\n\
    \    return equal(a, b) and equal(b, c) and equal(c, a)\n\n#=== \u4E09\u89D2\u5F62\
    \u306E\u6C7A\u5B9A\ndef SSS_Triangle(a: float, b: float, c: float) -> Triangle:\n\
    \    \"\"\" 3 \u8FBA\u306E\u9577\u3055\u304C a, b, c \u3067\u3042\u308B\u4E09\u89D2\
    \u5F62\u3092\u751F\u6210\u3059\u308B.\n\n    Args:\n        a (float): \u8FBA\
    \ BC \u306E\u9577\u3055\n        b (float): \u8FBA CA \u306E\u9577\u3055\n   \
    \     c (float): \u8FBA AB \u306E\u9577\u3055\n\n    Raises:\n        ValueError:\
    \ a + b < c, b + c < a, c + a < b \u3092\u6E80\u305F\u3057\u3066\u3044\u306A\u3051\
    \u308C\u3070\u306A\u3089\u306A\u3044.\n\n    Returns:\n        Triangle: 3 \u8FBA\
    \u306E\u9577\u3055\u304C a, b, c \u3067\u3042\u308B\u4E09\u89D2\u5F62\u3092\u751F\
    \u6210\u3059\u308B.\n    \"\"\"\n\n    if compare(2 * max(a, b, c), a + b + c)\
    \ == -1:\n        raise ValueError\n\n    t=a+b+c\n\n    A = Point()\n    B =\
    \ Point(c, 0)\n\n    x = (- a * a + b * b + c * c) / (2 * c)\n    y = sqrt(t *\
    \ (t - 2 * a) * (t - 2 * b) * (t - 2  *c)) / (2 * c)\n    C = Point(x, y)\n  \
    \  return Triangle(A, B, C)\n\ndef SAS_Triangle(a: float, gamma: float, b: float)\
    \ -> Triangle:\n    \"\"\" 2 \u8FBA\u306E\u9577\u3055\u304C a,b \u3067, \u305D\
    \u306E\u9593\u306E\u89D2\u5EA6\u304C gamma \u3067\u3042\u308B\u4E09\u89D2\u5F62\
    \u3092\u751F\u6210\u3059\u308B.\n\n    Args:\n        a (float): \u8FBA BC \u306E\
    \u9577\u3055\n        gamma (float): \u89D2 C \u306E\u5927\u304D\u3055\n     \
    \   b (float): \u8FBA CA \u306E\u9577\u3055\n\n    Raises:\n        ValueError:\
    \ 0 <= gamma <= pi \u3067\u306A\u304F\u3066\u306F\u306A\u3089\u306A\u3044.\n\n\
    \    Returns:\n        Triangle: 2 \u8FBA\u306E\u9577\u3055\u304C a,b \u3067,\
    \ \u305D\u306E\u9593\u306E\u89D2\u5EA6\u304C gamma \u3067\u3042\u308B\u4E09\u89D2\
    \u5F62\n    \"\"\"\n\n    if not(0 <= gamma <= pi):\n        raise ValueError\n\
    \n    t = sqrt(a * a + b * b - 2 * a * b * cos(gamma))\n\n    A = Point()\n  \
    \  B = Point(t,0)\n    C = Point((b * b- a * b * cos(gamma)) / t, (a * b * sin(gamma))\
    \ / t)\n    return Triangle(A, B, C)\n\ndef ASA_Triangle(alpha: float, c: float,\
    \ beta: float) -> Triangle:\n    \"\"\" 1 \u8FBA\u306E\u9577\u3055\u304C c \u3067\
    , \u4E21\u7AEF\u306E\u89D2\u5EA6\u304C alpha, beta \u3067\u3042\u308B\u4E09\u89D2\
    \u5F62\u3092\u751F\u6210\u3059\u308B\n\n    Args:\n        alpha (float): \u89D2\
    \ A \u306E\u5927\u304D\u3055\n        c (float): \u8FBA AB \u306E\u9577\u3055\n\
    \        beta (float): \u89D2 B \u306E\u5927\u304D\u3055\n\n    Raises:\n    \
    \    ValueError: alpha + beta <= pi \u3067\u306A\u304F\u3066\u306F\u306A\u3089\
    \u306A\u3044.\n\n    Returns:\n        Triangle: 1 \u8FBA\u306E\u9577\u3055\u304C\
    \ c \u3067, \u4E21\u7AEF\u306E\u89D2\u5EA6\u304C alpha, beta \u3067\u3042\u308B\
    \u4E09\u89D2\u5F62\n    \"\"\"\n\n    if not alpha + beta <= pi:\n        raise\
    \ ValueError\n\n    t = sin(beta) / sin(alpha + beta)\n\n    A = Point()\n   \
    \ B = Point(c, 0)\n    C = Point(c * t * cos(alpha), c * t * sin(alpha))\n   \
    \ return Triangle(A, B, C)\n\ndef AAS_Triangle(alpha: float, beta: float, a: float)\
    \ -> Triangle:\n    \"\"\" 1 \u8FBA\u306E\u9577\u3055\u304C a \u3067, 2\u3064\u306E\
    \u89D2\u304C alpha, beta \u3067\u3042\u308B\u4E09\u89D2\u5F62\u3092\u751F\u6210\
    \u3059\u308B (a \u306E\u5BFE\u89D2\u304C alpha).\n\n    Args:\n        alpha (float):\
    \ \u89D2 A \u306E\u5927\u304D\u3055\n        beta (float): \u89D2 B \u306E\u5927\
    \u304D\u3055\n        a (float): \u8FBA BC \u306E\u9577\u3055\n\n    Raises:\n\
    \        ValueError: alpha + beta <= pi \u3067\u306A\u304F\u3066\u306F\u306A\u3089\
    \u306A\u3044.\n\n    Returns:\n        Triangle: 1 \u8FBA\u306E\u9577\u3055\u304C\
    \ a \u3067, 2\u3064\u306E\u89D2\u304C alpha, beta \u3067\u3042\u308B\u4E09\u89D2\
    \u5F62\n    \"\"\"\n    if alpha + beta <= pi:\n        raise ValueError\n\n \
    \   A = Point()\n    B = Point(a * sin(alpha + beta) / sin(alpha), 0)\n    C =\
    \ Point(a * sin(beta) * cos(alpha) / sin(alpha), a * sin(beta))\n    return Triangle(A,\
    \ B, C)\n"
  dependsOn: []
  isVerificationFile: false
  path: Geometric/Triangle.py
  requiredBy: []
  timestamp: '2025-03-01 16:16:33+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Geometric/Triangle.py
layout: document
redirect_from:
- /library/Geometric/Triangle.py
- /library/Geometric/Triangle.py.html
title: Geometric/Triangle.py
---
