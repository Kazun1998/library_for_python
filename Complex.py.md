---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':warning:'
    path: Vector3.py
    title: Vector3.py
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "import math\n\nclass Complex(Fraction):\n    #\u5165\u529B\u5B9A\u7FA9\n\
    \    def __init__(self,Real_part=0,Imaginary_part=0):\n        self.re=Real_part\n\
    \        self.im=Imaginary_part\n\n    #\u8868\u793A\u5B9A\u7FA9\n    def __str__(self):\n\
    \        s=\"\"\n        s=Complex.__strmake(s,self.re,\"\")\n        s=Complex.__strmake(s,self.im,\"\
    i\")\n        if s==\"\":\n            return \"0\"\n        else:\n         \
    \   return s\n\n    def __strmake(self,coefficient,axis):\n        if coefficient==0:\n\
    \            return self\n        else:\n            if self==\"\":\n        \
    \        if axis==\"\":\n                    self+=str(coefficient)\n        \
    \        else:\n                    if coefficient==1:self+=axis\n           \
    \         elif coefficient==-1:self+=\"-\"+axis\n                    else:self+=str(coefficient)+axis\n\
    \            else:\n                if coefficient>0:\n                    if\
    \ coefficient==1:self+=\"+\"+axis\n                    else:self+=\"+\"+str(coefficient)+axis\n\
    \                else:\n                    if coefficient==-1:self+=\"-\"+axis\n\
    \                    else:self+=str(coefficient)+axis\n\n        return self\n\
    \n    #\u56DB\u5247\u6F14\u7B97\u5B9A\u7FA9\n    def __add__(self,other):\n  \
    \      c=Complex()\n        if not(isinstance(other,Complex)):\n            other=Complex.Real_Complex(other)\n\
    \        c.re=self.re+other.re\n        c.im=self.im+other.im\n        return\
    \ c\n\n    def __radd__(self,other):\n        c=Complex()\n        if not(isinstance(other,Complex)):\n\
    \            other=Complex.Real_to_Complex(other)\n        c.re=self.re+other.re\n\
    \        c.im=self.im+other.im\n        return c\n    \n    def __sub__(self,other):\n\
    \        return self+(-other)\n\n    def __rsub__(self,other):\n        return\
    \ -self+other\n\n    def __mul__(self,other):\n        c=Complex()\n        if\
    \ not(isinstance(other,Complex)):\n            other=Complex.Real_to_Complex(other)\n\
    \        c.re=self.re*other.re-self.im*other.im\n        c.im=self.re*other.im+self.im*other.re\n\
    \        return c\n\n    def __rmul__(self,other):\n        c=Complex()\n    \
    \    if not(isinstance(other,Complex)):\n            other=Complex.Real_to_Complex(other)\n\
    \        c.re=self.re*other.re-self.im*other.im\n        c.im=self.re*other.im+self.im*other.re\n\
    \        return c\n\n    def __truediv__(self,other):\n        if not(isinstance(other,(Complex))):\n\
    \            other=Complex.Real_to_Complex(other)\n        return self*Complex.__inverse(other)\n\
    \n    def __rtruediv__(self,other):\n        if not(isinstance(other,(Complex))):\n\
    \            other=Complex.Real_to_Complex(other)\n        return Complex.__inverse(self)*other\n\
    \n    #\u6BD4\u8F03\u6F14\u7B97\u5B50\n    def __eq__(self,other):\n        return\
    \ (self-other)==Complex()\n        \n    #\u305D\u306E\u4ED6\n    def conjugate(self):\n\
    \        return Complex(self.re,-self.im)\n\n    def __abs__(self):\n        return\
    \ math.sqrt((self*Complex.conjugate(self)).re)\n\n    def abs2(self):\n      \
    \  return (self*Complex.conjugate(self)).re\n\n    #\u5B9F\u6570\u304B\u3089\u8907\
    \u7D20\u6570\u306B\u5909\u63DB\n    def Real_to_Complex(self):\n        if not(isinstance(self,Complex)):\n\
    \            return Complex(self,0)\n        else:\n            return self\n\
    \    \n    #\u6B63\u8CA0\u5224\u5B9A\n\n    #\u8981\u7D04\n\n    #\u9006\u6570\
    \n    def __inverse(self):\n        return Fraction(1,Complex.abs2(self))*Complex.conjugate(self)\n\
    \n    #\u7B26\u53F7\n    def __pos__(self):\n        return self\n\n    def __neg__(self):\n\
    \        return Complex(-self.re,-self.im)\n"
  dependsOn: []
  isVerificationFile: false
  path: Complex.py
  requiredBy:
  - Vector3.py
  timestamp: '2021-04-27 14:48:27+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Complex.py
layout: document
redirect_from:
- /library/Complex.py
- /library/Complex.py.html
title: Complex.py
---