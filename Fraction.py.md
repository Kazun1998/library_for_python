---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':warning:'
    path: Quaternion.py
    title: Quaternion.py
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
  code: "from math import gcd\n\nclass Fraction():\n    __slots__=(\"a\",\"b\")\n\n\
    \    ##\u5165\u529B\u5B9A\u7FA9\n    def __init__(self, Numerator=0, Denominator=1,\
    \ reduction=True, expanded=False):\n        \"\"\"\u5206\u6570\u306E\u30AA\u30D6\
    \u30B8\u30A7\u30AF\u30C8\u3092\u751F\u6210\u3059\u308B.\n\n        Numerator:\
    \ \u5206\u5B50\n        Denominator: \u5206\u6BCD (!=0)\n        \"\"\"\n    \
    \    assert Denominator or expanded,\"\u5206\u6BCD\u304C0\"\n\n        if Denominator<0:\n\
    \            Numerator*=-1\n            Denominator*=-1\n\n        self.a=Numerator\n\
    \        self.b=Denominator\n        if reduction:\n            g=gcd(Numerator,\
    \ Denominator)\n            self.a=Numerator//g\n            self.b=Denominator//g\n\
    \n    #\u8868\u793A\u5B9A\u7FA9\n    def __str__(self):\n        if self.b==1:\n\
    \            return str(self.a)\n        else:\n            return \"{}/{}\".format(self.a,self.b)\n\
    \n    __repr__=__str__\n\n    #\u56DB\u5247\u6F14\u7B97\u5B9A\u7FA9\n    def __add__(self,other):\n\
    \        if other.__class__==Fraction:\n            x=self.a*other.b+self.b*other.a\n\
    \            y=self.b*other.b\n        elif other.__class__==int:\n          \
    \  x=self.a+self.b*other\n            y=self.b\n        else:\n            assert\
    \ 0,\"\u578B\u304C\u9055\u3046\"\n        return Fraction(x,y)\n\n    def __radd__(self,other):\n\
    \        return self+other\n\n    def __sub__(self,other):\n        if other.__class__==Fraction:\n\
    \            x=self.a*other.b-self.b*other.a\n            y=self.b*other.b\n \
    \       elif other.__class__==int:\n            x=self.a-self.b*other\n      \
    \      y=self.b\n        else:\n            assert 0,\"\u578B\u304C\u9055\u3046\
    \"\n        return Fraction(x,y)\n\n    def __rsub__(self,other):\n        return\
    \ -self+other\n\n    def __mul__(self,other):\n        if other.__class__==Fraction:\n\
    \            x=self.a*other.a\n            y=self.b*other.b\n        elif other.__class__==int:\n\
    \            x=self.a*other\n            y=self.b\n        else:\n           \
    \ assert 0,\"\u578B\u304C\u9055\u3046\"\n\n        return Fraction(x,y)\n\n  \
    \  def __rmul__(self,other):\n        return self*other\n\n    def __floordiv__(self,other):\n\
    \        if other==Fraction():\n            raise ZeroDivisionError\n\n      \
    \  H=self/other\n        return H.a//H.b\n\n    def __rfloordiv__(self,other):\n\
    \        if self==Fraction():\n            raise ZeroDivisionError\n\n       \
    \ H=other/self\n        return H.a//H.b\n\n    def __truediv__(self,other):\n\
    \        assert other,\"\u9664\u6570\u304C0\"\n\n        if other.__class__==Fraction:\n\
    \            x=self.a*other.b\n            y=self.b*other.a\n        elif other.__class__==int:\n\
    \            x=self.a\n            y=self.b*other\n        else:\n           \
    \ assert 0,\"\u578B\u304C\u9055\u3046\"\n\n        return Fraction(x,y)\n\n  \
    \  def __rtruediv__(self,other):\n        assert self,\"\u9664\u6570\u304C0\"\n\
    \        if other.__class__==Fraction:\n            x=other.a*self.b\n       \
    \     y=other.b*self.a\n        elif other.__class__==int:\n            x=other*self.b\n\
    \            y=self.a\n        else:\n            assert 0,\"\u578B\u304C\u9055\
    \u3046\"\n        return Fraction(x,y)\n\n    def __pow__(self,m):\n        alpha,beta=self.a,self.b\n\
    \        if m<0:\n            alpha,beta=beta,alpha\n            m=-m\n\n    \
    \    return Fraction(pow(alpha,m),pow(beta,m))\n\n    #\u4E38\u3081\n    def __floor__(self):\n\
    \        return self.a//self.b\n\n    def __ceil__(self):\n        return (self.a+self.b-1)//self.b\n\
    \n    #\u771F\u507D\u5024\n    def __bool__(self):\n        return bool(self.a)\n\
    \n    #\u6BD4\u8F03\n    def __eq__(self,other):\n        if other.__class__==Fraction:\n\
    \            return self.a*other.b==self.b*other.a\n        elif other.__class__==int:\n\
    \            return self.a==self.b*other\n        else:\n            assert 0,\"\
    \u578B\u304C\u9055\u3046\"\n\n    def __nq__(self,other):\n        return not(self==other)\n\
    \n    def __lt__(self,other):\n        return self<=other and self!=other\n\n\
    \    def __le__(self,other):\n        if other.__class__==Fraction:\n        \
    \    return self.a*other.b<=self.b*other.a\n        elif other.__class__==int:\n\
    \            return self.a<=self.b*other\n        else:\n            assert 0,\"\
    \u578B\u304C\u9055\u3046\"\n\n    def __gt__(self,other):\n        return other<=self\
    \ and other!=self\n\n    def __ge__(self,other):\n        return other<=self\n\
    \n    #\u305D\u306E\u4ED6\n    def __float__(self):\n        return self.a/self.b\n\
    \n    def sign(self):\n        s=self.a*self.b\n        if s>0:return 1\n    \
    \    elif s==0:return 0\n        else:return -1\n\n    #\u7B26\u53F7\n    def\
    \ __pos__(self):\n        return self\n\n    def __neg__(self):\n        return\
    \ Fraction(-self.a,self.b)\n\n    def __abs__(self):\n        if self.a>0:\n \
    \           return self\n        else:\n            return -self\n\n    #\u305D\
    \u306E\u4ED6\n    def is_unit(self):\n        return self.a==1\n\n    def __hash__(self):\n\
    \        return hash(10**9*self.a+self.b)\n"
  dependsOn: []
  isVerificationFile: false
  path: Fraction.py
  requiredBy:
  - Quaternion.py
  - Vector3.py
  timestamp: '2022-02-12 00:31:19+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Fraction.py
layout: document
redirect_from:
- /library/Fraction.py
- /library/Fraction.py.html
title: Fraction.py
---
