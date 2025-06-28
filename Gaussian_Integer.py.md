---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test_verify/yosupo_library_checker/Math/Gcd_of_Gaussian_Integers.test.py
    title: test_verify/yosupo_library_checker/Math/Gcd_of_Gaussian_Integers.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.13.5/x64/lib/python3.13/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.13.5/x64/lib/python3.13/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class Gaussian_Integer:\n    def __new__(cls, real: int = 0, imaginary: int\
    \ = 0) -> \"Gaussian_Integer\":\n        \"\"\" \u5B9F\u90E8 real, \u865A\u90E8\
    \ imaginary \u306E Gauss \u6574\u6570\u3092\u751F\u6210\u3059\u308B.\n\n     \
    \   Args:\n            real (int, optional): \u5B9F\u90E8. Defaults to 0.\n  \
    \          imaginary (int, optional): \u865A\u90E8. Defaults to 0.\n\n       \
    \ Returns:\n            Gaussian_Integer:\n        \"\"\"\n\n        self = super().__new__(cls)\n\
    \        self.__re = real\n        self.__im = imaginary\n        return self\n\
    \n    @property\n    def re(self) -> int:\n        return self.__re\n\n    @property\n\
    \    def im(self) -> int:\n        return self.__im\n\n    #\u8868\u793A\u5B9A\
    \u7FA9\n    def __str__(self) -> str:\n        if self.re == 0:\n            if\
    \ self.im == 0:\n                return \"0\"\n            elif self.im == 1:\n\
    \                return \"i\"\n            elif self.im == -1:\n             \
    \   return \"-i\"\n            else:\n                return f\"{self.im}i\"\n\
    \        else:\n            if self.im == 0:\n                return str(self.re)\n\
    \            elif self.im == 1:\n                return f\"{self.re}+i\"\n   \
    \         elif self.im == -1:\n                return f\"{self.re}-i\"\n     \
    \       else:\n                return f\"{self.re}{self.im:+}i\"\n\n    def __repr__(self)\
    \ -> str:\n        return f\"{self.__class__.__name__}({self.re}, {self.im})\"\
    \n\n    #\u56DB\u5247\u6F14\u7B97\u5B9A\u7FA9\n    #\u52A0\u6CD5\n    def __add__(self,\
    \ other: \"Gaussian_Integer\") -> \"Gaussian_Integer\":\n        if isinstance(other,\
    \ Gaussian_Integer):\n            return Gaussian_Integer(self.re + other.re,\
    \ self.im + other.im)\n        elif isinstance(other, int):\n            return\
    \ Gaussian_Integer(self.re + other, self.im)\n        else:\n            raise\
    \ NotImplementedError\n\n    def __radd__(self, other: \"Gaussian_Integer\") ->\
    \ \"Gaussian_Integer\":\n        return self + other\n\n    #\u6E1B\u6CD5\n  \
    \  def __sub__(self, other: \"Gaussian_Integer\") -> \"Gaussian_Integer\":\n \
    \       if isinstance(other, Gaussian_Integer):\n            return Gaussian_Integer(self.re\
    \ - other.re, self.im - other.im)\n        elif isinstance(other, int):\n    \
    \        return Gaussian_Integer(self.re - other, self.im)\n        else:\n  \
    \          raise NotImplementedError\n\n    def __rsub__(self, other: \"Gaussian_Integer\"\
    ) -> \"Gaussian_Integer\":\n        return (-self) + other\n\n    #\u4E57\u6CD5\
    \n    def __mul__(self, other: \"Gaussian_Integer\") -> \"Gaussian_Integer\":\n\
    \        a, b = self.re, self.im\n        if isinstance(other, Gaussian_Integer):\n\
    \            c, d = other.re, other.im\n        elif isinstance(other, int):\n\
    \            c, d = other, 0\n        else:\n            raise NotImplementedError\n\
    \n        x = a * c - b * d\n        y = a * d + b * c\n        return Gaussian_Integer(x,\
    \ y)\n\n    def __rmul__(self, other: \"Gaussian_Integer\") -> \"Gaussian_Integer\"\
    :\n        return self * other\n\n    def __floordiv__(self, other: \"Gaussian_Integer\"\
    ) -> \"Gaussian_Integer\":\n        if isinstance(other, int):\n            other\
    \ = Gaussian_Integer(other, 0)\n\n        a, b = self.re, self.im\n        c,\
    \ d = other.re, other.im\n\n        n = other.norm()\n\n        p = (2 * (a *\
    \ c + b * d) + n) // (2 * n)\n        q = (2 * (b * c - a * d) + n) // (2 * n)\n\
    \n        return Gaussian_Integer(p, q)\n\n    def __divmod__(self, other: \"\
    Gaussian_Integer\") -> \"Gaussian_Integer\":\n        x = self // other\n    \
    \    return (x, self - other * x)\n\n    def __mod__(self, other: \"Gaussian_Integer\"\
    ) -> \"Gaussian_Integer\":\n        return  self - other * (self // other)\n\n\
    \    #\u6BD4\u8F03\u6F14\u7B97\u5B50\n    def __eq__(self, other: \"Gaussian_Integer\"\
    ) -> bool:\n        if isinstance(other, Gaussian_Integer):\n            return\
    \ (self.re == other.re) and (self.im == other.im)\n        elif isinstance(other,\
    \ int):\n            return (self.re == other) and (self.im == 0)\n        else:\n\
    \            return NotImplementedError\n\n    def __bool__(self):\n        return\
    \ not self.is_zero()\n\n    #\u305D\u306E\u4ED6\n    def is_zero(self) -> bool:\n\
    \        \"\"\" 0 \u304B?\n\n        Returns:\n            bool: 0 \u306A\u3089\
    \ True, \u305D\u3046\u3067\u306A\u3044\u306A\u3089\u3070 False\n        \"\"\"\
    \n        return (self.re == 0) and (self.im == 0)\n\n    def conjugate(self)\
    \ -> \"Gaussian_Integer\":\n        \"\"\" \u5171\u5F79\u3092\u6C42\u3081\u308B\
    \n\n        Returns:\n            Gaussian_Integer: \u5171\u5F79\n        \"\"\
    \"\n        return Gaussian_Integer(self.re, -self.im)\n\n    def __abs__(self)\
    \ -> float:\n        import math\n        return math.sqrt(self.norm())\n\n  \
    \  def norm(self) -> int:\n        \"\"\" Gauss \u6574\u6570\u4E0A\u30CE\u30EB\
    \u30E0 (= \u7D76\u5BFE\u5024\u306E 2 \u4E57) \u3092\u6C42\u3081\u308B\n\n    \
    \    Returns:\n            int: Gauss \u6574\u6570\u306E\u30CE\u30EB\u30E0\n \
    \       \"\"\"\n        return self.re * self.re + self.im * self.im\n\n    #\u7B26\
    \u53F7\n    def __pos__(self) -> \"Gaussian_Integer\":\n        return self\n\n\
    \    def __neg__(self) -> \"Gaussian_Integer\":\n        return Gaussian_Integer(-self.re,\
    \ -self.im)\n\n    #\u30B3\u30D4\u30FC\n    def __copy__(self):\n        return\
    \ self\n\n    #\u30CF\u30C3\u30B7\u30E5\n    def __hash__(self):\n        return\
    \ hash((self.re, self.im))\n\n#\u6700\u5927\u516C\u7D04\u6570\ndef gcd(x: Gaussian_Integer,\
    \ y: Gaussian_Integer) -> Gaussian_Integer:\n    \"\"\"  Gauss \u6574\u6570 x,\
    \ y \u306E\u6700\u5927\u516C\u7D04\u6570 gcd(x, y) \u3092\u6C42\u3081\u308B.\n\
    \n    Args:\n        x (Gaussian_Integer):\n        y (Gaussian_Integer):\n\n\
    \    Returns:\n        Gaussian_Integer: \u6700\u5927\u516C\u7D04\u6570 (\u5358\
    \u6570\u500D\u306E\u9055\u3044\u306B\u3088\u308B\u5DEE\u304C\u751F\u307E\u308C\
    \u308B\u53EF\u80FD\u6027\u306F\u3042\u308B)\n    \"\"\"\n\n    while not y.is_zero():\n\
    \        x, y = y, x % y\n    return x\n\n#\u62E1\u5F35Euclid\u306E\u4E92\u9664\
    \u6CD5\ndef Extended_Euclid(x: Gaussian_Integer, y: Gaussian_Integer) -> tuple[Gaussian_Integer,\
    \ Gaussian_Integer, Gaussian_Integer]:\n    \"\"\" Gauss \u6574\u6570 x, y \u306B\
    \u3064\u3044\u3066, a x + b y = gcd(x, y) \u3068\u306A\u308B (a, b, gcd(x, y))\
    \ \u306E\u4F8B\u3092\u6C42\u3081\u308B.\n\n    Args:\n        x (Gaussian_Integer):\n\
    \        y (Gaussian_Integer):\n\n    Returns:\n        tuple[Gaussian_Integer,\
    \ Gaussian_Integer, Gaussian_Integer]: (a, b, g) \u306E\u30BF\u30D7\u30EB\u3067\
    \u3042\u308A, \u4EE5\u4E0B\u3092\u6E80\u305F\u3059.\n            g = gcd(x, y)\n\
    \            a x + b y = g\n    \"\"\"\n\n    a0, b0, a1, b1 = 1, 0, 0, 1\n  \
    \  while y:\n        q, x, y = x // y, y, x % y\n        a0, a1 = a1, a0 - q *\
    \ a1\n        b0, b1 = b1, b0 - q * b1\n    return a0, b0, x\n\n#\u540C\u4F34\
    ?\ndef Is_Associate(x: Gaussian_Integer, y: Gaussian_Integer) -> bool:\n    \"\
    \"\" x, y \u306F\u540C\u4F34?\n\n    Args:\n        x (Gaussian_Integer):\n  \
    \      y (Gaussian_Integer):\n\n    Returns:\n        bool: \u540C\u4F34 ?\n \
    \   \"\"\"\n\n    e = Gaussian_Integer(0, 1)\n\n    a = (x == y)\n    b = (x ==\
    \ -y)\n    c = (x == y * e)\n    d = (x == y * (-e))\n\n    return a or b or c\
    \ or d\n"
  dependsOn: []
  isVerificationFile: false
  path: Gaussian_Integer.py
  requiredBy: []
  timestamp: '2025-03-27 23:13:02+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test_verify/yosupo_library_checker/Math/Gcd_of_Gaussian_Integers.test.py
documentation_of: Gaussian_Integer.py
layout: document
redirect_from:
- /library/Gaussian_Integer.py
- /library/Gaussian_Integer.py.html
title: Gaussian_Integer.py
---
