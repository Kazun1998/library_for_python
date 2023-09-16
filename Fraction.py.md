---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':warning:'
    path: Quaternion.py
    title: Quaternion.py
  - icon: ':warning:'
    path: Root.py
    title: Root.py
  - icon: ':warning:'
    path: Vector3.py
    title: Vector3.py
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.5/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.5/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from math import gcd\n\nclass Fraction():\n    reduction = False\n    expand\
    \ = False\n\n    \"\"\"\n    reduction : \u5206\u6570\u3092\u7D04\u5206\u3057\u305F\
    \u72B6\u614B\u3067\u4FDD\u5B58\u3059\u308B\u304B\u3069\u3046\u304B\n    expand\
    \ : 1/0, -1/0 \u3092\u8A8D\u3081\u308B\u304B\u3069\u3046\u304B\n    \"\"\"\n\n\
    \    ##\u5165\u529B\u5B9A\u7FA9\n    def __init__(self, Numerator = 0, Denominator\
    \ = 1):\n        \"\"\"\u5206\u6570\u306E\u30AA\u30D6\u30B8\u30A7\u30AF\u30C8\u3092\
    \u751F\u6210\u3059\u308B.\n\n        Numerator : \u5206\u5B50\n        Denominator\
    \ : \u5206\u6BCD\n        \"\"\"\n        assert Denominator or Fraction.expand,\
    \ \"\u5206\u6BCD\u304C0\"\n\n        if Denominator < 0:\n            Numerator\
    \ *= -1\n            Denominator *= -1\n\n        self.__a = Numerator\n     \
    \   self.__b = Denominator\n        if Fraction.reduction:\n            g = gcd(Numerator,\
    \ Denominator)\n            self.__a = Numerator // g\n            self.__b =\
    \ Denominator // g\n\n    def numerator(self):\n        return self.__a\n\n  \
    \  def denominator(self):\n        return  self.__b\n\n    def __iter__(self):\n\
    \        yield self.__a\n        yield self.__b\n\n    #\u8868\u793A\u5B9A\u7FA9\
    \n    def __str__(self):\n        if self.__b == 1:\n            return str(self.__a)\n\
    \        else:\n            return f\"{self.__a}/{self.__b}\"\n\n    __repr__\
    \ = __str__\n\n    #\u56DB\u5247\u6F14\u7B97\u5B9A\u7FA9\n    def __add__(self,\
    \ other):\n        if isinstance(other, Fraction):\n            x = self.__a *\
    \ other.__b + self.__b * other.__a\n            y = self.__b * other.__b\n   \
    \     elif isinstance(other, int):\n            x = self.__a + self.__b * other\n\
    \            y = self.__b\n        else:\n            raise TypeError(f\"{other}\
    \ \u306E\u578B\u304C\u304A\u304B\u3057\u3044\u3067\u3059.\")\n        return Fraction(x,\
    \ y)\n\n    def __radd__(self, other):\n        return self + other\n\n    def\
    \ __sub__(self, other):\n        if isinstance(other, Fraction):\n           \
    \ x = self.__a * other.__b - self.__b * other.__a\n            y = self.__b *\
    \ other.__b\n        elif isinstance(other, int):\n            x = self.__a -\
    \ self.__b * other\n            y = self.__b\n        else:\n            raise\
    \ TypeError(f\"{other} \u306E\u578B\u304C\u304A\u304B\u3057\u3044\u3067\u3059\
    .\")\n        return Fraction(x, y)\n\n    def __rsub__(self, other):\n      \
    \  return -self + other\n\n    def __mul__(self, other):\n        if isinstance(other,\
    \ Fraction):\n            x = self.__a * other.__a\n            y = self.__b *\
    \ other.__b\n        elif isinstance(other, int):\n            x = self.__a *\
    \ other\n            y = self.__b\n        else:\n            raise TypeError(f\"\
    {other} \u306E\u578B\u304C\u304A\u304B\u3057\u3044\u3067\u3059.\")\n\n       \
    \ return Fraction(x, y)\n\n    def __rmul__(self, other):\n        return self\
    \ * other\n\n    def __floordiv__(self, other):\n        if other == Fraction():\n\
    \            raise ZeroDivisionError\n\n        H = self / other\n        return\
    \ H.a // H.b\n\n    def __rfloordiv__(self, other):\n        if self == Fraction():\n\
    \            raise ZeroDivisionError\n\n        H = other / self\n        return\
    \ H.a // H.b\n\n    def __truediv__(self, other):\n        if not other:\n   \
    \         raise ZeroDivisionError(\"\u30BC\u30ED\u9664\u7B97\")\n\n        if\
    \ isinstance(other, Fraction):\n            x = self.__a * other.__b\n       \
    \     y = self.__b * other.__a\n        elif other.__class__ == int:\n       \
    \     x = self.__a\n            y = self.__b * other\n        else:\n        \
    \    raise TypeError(f\"{other} \u306E\u578B\u304C\u304A\u304B\u3057\u3044\u3067\
    \u3059.\")\n\n        return Fraction(x, y)\n\n    def __rtruediv__(self, other):\n\
    \        if not self:\n            raise ZeroDivisionError(\"\u30BC\u30ED\u9664\
    \u7B97\")\n\n        if isinstance(other, Fraction):\n            x = other.__a\
    \ * self.__b\n            y = other.__b * self.__a\n        elif isinstance(other,\
    \ int):\n            x = other * self.__b\n            y = self.__a\n        else:\n\
    \            raise TypeError(f\"{other} \u306E\u578B\u304C\u304A\u304B\u3057\u3044\
    \u3067\u3059.\")\n        return Fraction(x, y)\n\n    def __pow__(self, m):\n\
    \        alpha, beta = self\n\n        if m < 0:\n            alpha, beta = beta,\
    \ alpha\n            m = -m\n\n        return Fraction(pow(alpha, m), pow(beta,\
    \ m))\n\n    #\u4E38\u3081\n    def __floor__(self):\n        return self.__a\
    \ // self.__b\n\n    def __ceil__(self):\n        return (self.__a + self.__b\
    \ - 1) // self.__b\n\n    #\u771F\u507D\u5024\n    def __bool__(self):\n     \
    \   return bool(self.__a)\n\n    def __compare(self, other):\n        \"\"\" self\
    \ < other \u306A\u3089\u3070 -1, self = other \u306A\u3089\u3070 0, self > other\
    \ \u306A\u3089\u3070, +1\n        \"\"\"\n        if isinstance(other, Fraction):\n\
    \            x = self.__a * other.__b\n            y = self.__b * other.__a\n\
    \        else:\n            x = self.__a\n            y = self.__b * other\n\n\
    \        if x < y:\n            return -1\n        elif x > y:\n            return\
    \ 1\n        else:\n            return 0\n\n    #\u6BD4\u8F03\n    def __eq__(self,\
    \ other):\n        return self.__compare(other) == 0\n\n    def __neq__(self,\
    \ other):\n        return self.__compare(other) != 0\n\n    def __lt__(self, other):\n\
    \        return self.__compare(other) == -1\n\n    def __le__(self, other):\n\
    \        return self.__compare(other) != 1\n\n    def __gt__(self, other):\n \
    \       return self.__compare(other) == 1\n\n    def __ge__(self, other):\n  \
    \      return self.__compare(other) != -1\n\n    #\u305D\u306E\u4ED6\n    def\
    \ __float__(self):\n        return self.__a / self.__b\n\n    def sign(self):\n\
    \        if self.__a > 0:\n            return 1\n        elif self.__a == 0:\n\
    \            return 0\n        else:\n            return -1\n\n    #\u7B26\u53F7\
    \n    def __pos__(self):\n        return self\n\n    def __neg__(self):\n    \
    \    return Fraction(-self.__a, self.__b)\n\n    def __abs__(self):\n        if\
    \ self.__a > 0:\n            return self\n        else:\n            return -self\n\
    \n    #\u305D\u306E\u4ED6\n    def is_unit(self):\n        return self.__a ==\
    \ 1\n\n    def __hash__(self):\n        x, y = self\n        if not Fraction.reduction:\n\
    \            g = gcd(x, y)\n            x //= g; y //= g\n        return hash((x,\
    \ y))\n"
  dependsOn: []
  isVerificationFile: false
  path: Fraction.py
  requiredBy:
  - Quaternion.py
  - Root.py
  - Vector3.py
  timestamp: '2023-08-09 23:41:14+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Fraction.py
layout: document
redirect_from:
- /library/Fraction.py
- /library/Fraction.py.html
title: Fraction.py
---
