---
data:
  _extendedDependsOn:
  - icon: ':warning:'
    path: Fraction.py
    title: Fraction.py
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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.4/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.4/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "import math\nfrom Fraction import Fraction\n#from Complex import Complex\n\
    \nclass Quaternion(Complex):\n    #\u5165\u529B\u5B9A\u7FA9\n    def __init__(self,Real_part=0,Imaginary_part_i=0,Imaginary_part_j=0,Imaginary_part_k=0):\n\
    \        self.r=Real_part\n        self.i=Imaginary_part_i\n        self.j=Imaginary_part_j\n\
    \        self.k=Imaginary_part_k\n\n    #\u8868\u793A\u5B9A\u7FA9\n    def __str__(self):\n\
    \        s=\"\"\n        s=Quaternion.__strmake(s,self.r,\"\")\n        s=Quaternion.__strmake(s,self.i,\"\
    i\")\n        s=Quaternion.__strmake(s,self.j,\"j\")\n        s=Quaternion.__strmake(s,self.k,\"\
    k\")\n        if s==\"\":return \"0\"\n        else:return s\n\n    def __strmake(self,coefficient,axis):\n\
    \        if coefficient==0:return self\n        else:\n            if self==\"\
    \":\n                if axis==\"\":\n                    self+=str(coefficient)\n\
    \                else:\n                    if coefficient==1:self+=axis\n   \
    \                 elif coefficient==-1:self+=\"-\"+axis\n                    else:self+=str(coefficient)+axis\n\
    \            else:\n                if coefficient>0:\n                    if\
    \ coefficient==1:self+=\"+\"+axis\n                    else:self+=\"+\"+str(coefficient)+axis\n\
    \                else:\n                    if coefficient==-1:self+=\"-\"+axis\n\
    \                    else:self+=str(coefficient)+axis\n\n        return self\n\
    \n    #\u56DB\u5247\u6F14\u7B97\u5B9A\u7FA9\n    def __add__(self,other):\n  \
    \      q=Quaternion()\n        if not(isinstance(other,Quaternion)):other=Quaternion.Complex_to_Quatrarnion(other)\n\
    \        q.r=self.r+other.r\n        q.i=self.i+other.i\n        q.j=self.j+other.j\n\
    \        q.k=self.k+other.k\n        return q\n\n    def __radd__(self,other):\n\
    \        q=Quaternion()\n        if not(isinstance(other,Quaternion)):other=Quaternion.Complex_to_Quatrarnion(other)\n\
    \        q.r=self.r+other.r\n        q.i=self.i+other.i\n        q.j=self.j+other.j\n\
    \        q.k=self.k+other.k\n        return q\n\n    def __sub__(self,other):\n\
    \        return self+(-other)\n\n    def __rsub__(self,other):\n        return\
    \ -self+other\n\n    def __mul__(self,other):\n        q=Quaternion()\n      \
    \  if not(isinstance(other,Quaternion)):other=Quaternion.Complex_to_Quatrarnion(other)\n\
    \        s=self\n        o=other\n        q.r=s.r*o.r-s.i*o.i-s.j*o.j-s.k*o.k\n\
    \        q.i=s.r*o.i+s.i*o.r+s.j*o.k-s.k*o.j\n        q.j=s.r*o.j+s.j*o.r+s.k*o.i-s.i*o.k\n\
    \        q.k=s.r*o.k+s.k*o.r+s.i*o.j-s.j*o.i\n        return q\n\n    def __rmul__(self,other):\n\
    \        q=Quaternion()\n        if not(isinstance(other,Quaternion)):other=Quaternion.Complex_to_Quatrarnion(other)\n\
    \        s=self\n        o=other\n        q.r=s.r*o.r-s.i*o.i-s.j*o.j-s.k*o.k\n\
    \        q.i=s.r*o.i+s.i*o.r+s.j*o.k-s.k*o.j\n        q.j=s.r*o.j+s.j*o.r+s.k*o.i-s.i*o.k\n\
    \        q.k=s.r*o.k+s.k*o.r+s.i*o.j-s.j*o.i\n        return q\n\n    def __truediv__(self,other):\n\
    \        if not(isinstance(other,Quaternion)):other=Quaternion.Complex_to_Quatrarnion(other)\n\
    \        return self*Quaternion.__inverse(other)\n\n    def __rtruediv__(self,other):\n\
    \        if not(isinstance(other,Quaternion)):other=Quaternion.Complex_to_Quatrarnion(other)\n\
    \        return Quaternion.__inverse(self)*other\n\n    #\u6BD4\u8F03\u6F14\u7B97\
    \u5B50\n    def __eq__(self,other):\n        return (self-other)==Quaternion()\n\
    \n    #\u305D\u306E\u4ED6\n    def conjugate(self):\n        self=Quaternion.Complex_to_Quatrarnion(self)\n\
    \        return Quaternion(self.r,-self.i,-self.j,-self.k)\n\n    def __abs__(self):\n\
    \        return math.sqrt((self*Quaternion.conjugate(self)).r)\n\n    def abs2(self):\n\
    \        return (self*Quaternion.conjugate(self)).r\n\n    #\u8907\u7D20\u6570\
    \u304B\u3089\u56DB\u5143\u6570\u306B\u5909\u63DB\n    def Complex_to_Quatrarnion(self):\n\
    \        if not(isinstance(self,Quaternion)):\n            #if not(isinstance(self,Complex)):self=Complex.Real_to_Complex(self)\n\
    \            return Quaternion(self.re,self.im,0,0)\n        else:\n         \
    \   return self\n\n    #\u6B63\u8CA0\u5224\u5B9A\n\n    #\u8981\u7D04\n\n    #\u9006\
    \u6570\n    def __inverse(self):\n        return  Fraction(1,Quaternion.abs2(self))*Quaternion.conjugate(self)\n\
    \n    #\u7B26\u53F7\n    def __pos__(self):\n        return self\n\n    def __neg__(self):\n\
    \        return Quaternion(-self.r,-self.i,-self.j,-self.k)\n"
  dependsOn:
  - Fraction.py
  isVerificationFile: false
  path: Quaternion.py
  requiredBy:
  - Vector3.py
  timestamp: '2023-08-09 23:41:14+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Quaternion.py
layout: document
redirect_from:
- /library/Quaternion.py
- /library/Quaternion.py.html
title: Quaternion.py
---
