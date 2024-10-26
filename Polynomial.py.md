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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.7/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.7/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class Polynominal_Error(Exception):\n    pass\n\nclass Polynominal():\n \
    \   def __init__(self,P=[],C=\"X\"):\n        self.Poly=P\n        self.Char=C\n\
    \n    def __str__(self):\n        S=\"\"\n        flag=False\n        \n     \
    \   for k in range(len(self.Poly)):\n            if self.Poly[k]:\n          \
    \      if flag:\n                    if k==1:\n                        S+=\"{:+}{}\"\
    .format(self.Poly[1],self.Char)\n                    else:\n                 \
    \       S+=\"{:+}{}^{}\".format(self.Poly[k],self.Char,k)\n                else:\n\
    \                    flag=True\n                    if k==0:\n               \
    \         S=str(self.Poly[0])\n                    elif k==1:\n              \
    \          S=str(self.Poly[1])+self.Char\n                    else:\n        \
    \                S=str(self.Poly[k])+\"{}^{}\".format(self.Char,k)\n\n       \
    \ if S:\n            return S\n        else:\n            return \"0\"\n\n   \
    \ #+,-\n    def __pos__(self):\n        return self\n\n    def __neg__(self):\n\
    \        return self.scale(-1)\n\n    #Boole\n    def __bool__(self):\n      \
    \  return not(self.reduce().Poly==[0])\n    #\u7C21\u7565\u5316\n    def reduce(self):\n\
    \        P_deg=self.degree()\n        \n        if not(P_deg>=0):\n          \
    \  return Polynominal([0],self.Char)\n            \n        for i in range(self.degree(),-1,-1):\n\
    \            if self.Poly[i]:\n                return Polynominal(self.Poly[:i+1],self.Char)\n\
    \        \n    #\u6B21\u6570\n    def degree(self):\n        x=-float(\"inf\"\
    )\n        k=0\n        for y in self.Poly:\n            if y!=0:\n          \
    \      x=k\n            k+=1\n        return x\n\n    #\u52A0\u6CD5\n    def __add__(self,other):\n\
    \        if isinstance(other,Polynominal):\n            P_deg=max(self.degree(),0)\n\
    \            Q_deg=max(other.degree(),0)\n            R=[0]*(min(P_deg,Q_deg)+1)\n\
    \n            for k in range(min(P_deg,Q_deg)+1):\n                R[k]=self.Poly[k]+other.Poly[k]\n\
    \n            if P_deg>=Q_deg:\n                R+=self.Poly[Q_deg+1:]\n     \
    \       else:\n                R+=other.Poly[P_deg+1:]\n\n            return Polynominal(R,self.Char).reduce()\n\
    \        else:\n            P_deg=self.degree()\n            R=[0]*(P_deg+1)\n\
    \            \n            for i in range(P_deg+1):\n                if i:\n \
    \                   R[i]=self.Poly[i]\n                else:\n               \
    \     R[i]=self.Poly[i]+other\n\n            return Polynominal(R,self.Char).reduce()\n\
    \n    def __radd__(self,other):\n        return self+other\n\n    #\u6E1B\u6CD5\
    \n    def __sub__(self,other):\n        return self+(-other)\n\n    def __rsub__(self,other):\n\
    \        return (-self)+other\n    \n    #\u4E57\u6CD5\n    def __mul__(self,other):\n\
    \        if self==0 or other==0:\n            return Polynominal([0],self.Char)\n\
    \n        if isinstance(other,Polynominal):\n            P_deg=max(self.degree(),0)\n\
    \            Q_deg=max(other.degree(),0)\n\n            R=[0]*(P_deg+Q_deg+1)\n\
    \n            for i in range(P_deg+1):\n                for j in range(Q_deg+1):\n\
    \                    R[i+j]+=self.Poly[i]*other.Poly[j]\n            return Polynominal(R,self.Char).reduce()\n\
    \        else:\n            return self.scale(other)\n\n    def __rmul__(self,other):\n\
    \        return self.scale(other)\n\n    #\u9664\u6CD5\n    def __floordiv__(self,other):\n\
    \        if not other:\n            raise ZeroDivisionError\n\n        pass\n\n\
    \    #\u5270\u4F59\n    def __mod__(self,other):\n        return self-(self//other)*other\n\
    \n    #\u7D2F\u4E57\n    def __pow__(self,n):\n        if n<0:\n            raise\
    \  Polynominal_Error(\"n\u304C\u8CA0\u3067\u3059.\")\n\n        R=Polynominal([1],self.Char)\n\
    \        P=self\n        \n        while n>0:\n            if n%2:\n         \
    \       R*=P\n            P*=P\n            n=n>>1\n                \n       \
    \ return R\n    \n    #\u30B9\u30AB\u30E9\u30FC\u500D\n    def scale(self,s):\n\
    \        P_deg=self.degree()\n        \n        Q=[0]*(P_deg+1)\n        for i\
    \ in range(P_deg+1):\n            Q[i]=s*self.Poly[i]\n\n        return Polynominal(Q,self.Char).reduce()\n\
    \n    #\u4FC2\u6570\n    def coefficient(self,n):\n        try:\n            if\
    \ n<0:\n                raise IndexError\n\n            return self.Poly[n]\n\
    \        except IndexError:\n            return  0\n        except TypeError:\n\
    \            return 0\n\n    #\u6700\u9AD8\u6B21\u306E\u4FC2\u6570\n    def leading_coefficient(self):\n\
    \        for x in self.Poly[::-1]:\n            if x:\n                return\
    \ x\n        return 0\n    \n    #\u4EE3\u5165\n    def substitute(self,a):\n\
    \        x=1\n        P_deg=self.degree()\n\n        S=0\n        for i in range(P_deg+1):\n\
    \            S+=self.Poly[i]*x\n            x*=a\n        return S\n\n#\u6700\u5927\
    \u516C\u7D04\u6570\ndef gcd(P,Q):\n    \"\"\"Gauss\u6574\u6570 x,y\u306E\u6700\
    \u5927\u516C\u7D04\u6570\u3092\u6C42\u3081\u308B.\n\n    x,y:Gauss\u6574\u6570\
    \n    \"\"\"\n\n    if P.degree()<Q.degree():\n        P,Q=Q,P\n\n    while Q:\n\
    \        P.Q=Q,P%Q\n\n    return P\n\n#\u62E1\u5F35Euclid\u306E\u4E92\u9664\u6CD5\
    \ndef Extended_Euclid(x,y):\n    \"\"\"\u62E1\u5F35Euclid\u306E\u4E92\u9664\u6CD5\
    \u3092\u7528\u3044\u3066,xa+yb=gcd(x,y)\u3092\u6E80\u305F\u3059Gauss\u6574\u6570\
    a,b\u3092\u6C42\u3081\u308B.\n\n    x,y:Gauss\u6574\u6570\n\n    [\u51FA\u529B\
    ]:(a,b,gcd(x,y))\n    \"\"\"\n\n    a0,b0,a1,b1=1,0,0,1\n    while y:\n      \
    \  q,x,y=x//y,y,x%y\n        a0,a1=a1,a0-q*a1\n        b0,b1=b1,b0-q*b1\n    return\
    \ a0,b0,x\n    \n"
  dependsOn: []
  isVerificationFile: false
  path: Polynomial.py
  requiredBy: []
  timestamp: '2021-04-27 14:48:27+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Polynomial.py
layout: document
redirect_from:
- /library/Polynomial.py
- /library/Polynomial.py.html
title: Polynomial.py
---
