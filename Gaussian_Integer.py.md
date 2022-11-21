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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class Gaussian_Integer():\n    #\u5165\u529B\u5B9A\u7FA9\n    def __init__(self,Real_part=0,Imaginary_part=0):\n\
    \        self.re=Real_part\n        self.im=Imaginary_part\n\n    #\u8868\u793A\
    \u5B9A\u7FA9\n    def __str__(self):\n        if self.re==0:\n            if self.im==0:\n\
    \                return \"0\"\n            elif self.im==1:\n                return\
    \ \"i\"\n            elif self.im==-1:\n                return \"-i\"\n      \
    \      else:\n                return \"{}i\".format(self.im)\n        else:\n\
    \            if self.im==0:\n                return str(self.re)\n           \
    \ elif self.im==1:\n                return \"{}+i\".format(self.re)\n        \
    \    elif self.im==-1:\n                return \"{}-i\".format(self.re)\n    \
    \        else:\n                return \"{}{:+}i\".format(self.re,self.im)\n\n\
    \    __repr__=__str__\n\n    #\u56DB\u5247\u6F14\u7B97\u5B9A\u7FA9\n    #\u52A0\
    \u6CD5\n    def __add__(self,other):\n        if isinstance(other,Gaussian_Integer):\n\
    \            return Gaussian_Integer(self.re+other.re,self.im+other.im)\n    \
    \    else:\n            return Gaussian_Integer(self.re+other,self.im)\n\n   \
    \ def __radd__(self,other):\n        if isinstance(other,int):\n            return\
    \ Gaussian_Integer(self.re+other,self.im)\n\n    #\u6E1B\u6CD5\n    def __sub__(self,other):\n\
    \        return self+(-other)\n\n    def __rsub__(self,other):\n        if isinstance(other,int):\n\
    \            return (-self)+other\n\n    #\u4E57\u6CD5\n    def __mul__(self,other):\n\
    \        a,b=self.re,self.im\n        if isinstance(other,Gaussian_Integer):\n\
    \            c,d=other.re,other.im\n            return Gaussian_Integer(a*c-b*d,a*d+b*c)\n\
    \        else:\n            return Gaussian_Integer(other*a,other*b)\n\n    def\
    \ __rmul__(self,other):\n        if isinstance(other,int):\n            a,b=self.re,self.im\n\
    \            return Gaussian_Integer(other*a,other*b)\n\n    #\u9664\u6CD5\n \
    \   def __truediv__(self,other):\n        pass\n\n    def __rtruediv__(self,other):\n\
    \        pass\n\n    def __floordiv__(self,other):\n        if isinstance(other,int):\n\
    \            other=Gaussian_Integer(other,0)\n\n        a,b=self.re,self.im\n\
    \        c,d=other.re,other.im\n\n        n=other.norm()\n\n        p=(2*(a*c+b*d)+n)//(2*n)\n\
    \        q=(2*(b*c-a*d)+n)//(2*n)\n\n        return Gaussian_Integer(p,q)\n\n\
    \    def __divmod__(self,other):\n        x=self//other\n        return (x,self-other*x)\n\
    \n    def __mod__(self,other):\n        return  self-other*(self//other)\n   \
    \ #\u6BD4\u8F03\u6F14\u7B97\u5B50\n    def __eq__(self,other):\n        if isinstance(other,Gaussian_Integer):\n\
    \            return (self.re==other.re) and (self.im==other.im)\n        else:\n\
    \            return (self-other)==Gaussian_Integer(0,0)\n\n    def __bool__(self):\n\
    \        return not(self==0)\n\n    #\u305D\u306E\u4ED6\n    def conjugate(self):\n\
    \        return Gaussian_Integer(self.re,-self.im)\n\n    def __abs__(self):\n\
    \        import math\n        return math.sqrt(self.norm())\n\n    def norm(self):\n\
    \        return self.re*self.re+self.im*self.im\n\n    #\u5B9F\u6570\u304B\u3089\
    \u8907\u7D20\u6570\u306B\u5909\u63DB\n    def Real_to_Complex(self):\n       \
    \ pass\n\n    #\u6B63\u8CA0\u5224\u5B9A\n\n    #\u8981\u7D04\n\n    #\u9006\u6570\
    \n    def __inverse(self):\n        pass\n\n    #\u7B26\u53F7\n    def __pos__(self):\n\
    \        return self\n\n    def __neg__(self):\n        return Gaussian_Integer(-self.re,-self.im)\n\
    \n    #\u30B3\u30D4\u30FC\n    def __copy__(self):\n        return self\n\n  \
    \  #\u30CF\u30C3\u30B7\u30E5\n    def __hash__(self):\n        return hash((self.re,self.im))\n\
    \n#\u6700\u5927\u516C\u7D04\u6570\ndef gcd(x,y):\n    \"\"\"Gauss\u6574\u6570\
    \ x,y\u306E\u6700\u5927\u516C\u7D04\u6570\u3092\u6C42\u3081\u308B.\n\n    x,y:Gauss\u6574\
    \u6570\n    \"\"\"\n\n    while y:\n        x,y=y,x%y\n\n    return x\n\n#\u62E1\
    \u5F35Euclid\u306E\u4E92\u9664\u6CD5\ndef Extended_Euclid(x,y):\n    \"\"\"\u62E1\
    \u5F35Euclid\u306E\u4E92\u9664\u6CD5\u3092\u7528\u3044\u3066,xa+yb=gcd(x,y)\u3092\
    \u6E80\u305F\u3059Gauss\u6574\u6570a,b\u3092\u6C42\u3081\u308B.\n\n    x,y:Gauss\u6574\
    \u6570\n\n    [\u51FA\u529B]:(a,b,gcd(x,y))\n    \"\"\"\n\n    a0,b0,a1,b1=1,0,0,1\n\
    \    while y:\n        q,x,y=x//y,y,x%y\n        a0,a1=a1,a0-q*a1\n        b0,b1=b1,b0-q*b1\n\
    \    return a0,b0,x\n\n#\u540C\u4F34?\ndef Is_Associate(x,y):\n    \"\"\"x,y\u306F\
    \u540C\u4F34?\n\n    x,y:Gauss\u6574\u6570\n    \"\"\"\n    e=Gaussian_Integer(0,1)\n\
    \n    a=(x==y)\n    b=(x==-y)\n    c=(x==y*e)\n    d=(x==y*(-e))\n\n    return\
    \ a|b|c|d\n\n"
  dependsOn: []
  isVerificationFile: false
  path: Gaussian_Integer.py
  requiredBy: []
  timestamp: '2021-10-01 03:09:20+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Gaussian_Integer.py
layout: document
redirect_from:
- /library/Gaussian_Integer.py
- /library/Gaussian_Integer.py.html
title: Gaussian_Integer.py
---