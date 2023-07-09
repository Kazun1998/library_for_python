---
data:
  _extendedDependsOn:
  - icon: ':warning:'
    path: Fraction.py
    title: Fraction.py
  - icon: ':warning:'
    path: Number.py
    title: Number.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "import math\nfrom copy import *\nfrom Number  import Number\nfrom Fraction\
    \  import Fraction\nfrom functools import total_ordering\n\n\nclass root(Fraction):\n\
    \    def __init__(self,c=0,b=1):\n        self.c=c\n        self.b=b\n\n    def\
    \ __str__(self):\n        if self.c==0:return \"\"\n\n        if self.b==1:\n\
    \            if self.c>0:return \"+\"+str(self.c)\n            else:return str(self.c)\n\
    \n        t=\"sqrt[\"+str(self.b)+\"]\"\n\n        if self.c>0:\n            if\
    \ self.c==1:return \"+\"+t\n            else:return \"+\"+str(self.c)+t\n    \
    \    else:\n            if self.c==-1:return  \"-\"+t\n            else:return\
    \ str(self.c)+t\n\n    def string(self):\n        if self.c==0:return \"\"\n\n\
    \        if self.b==1:\n            if self.c>0:return \"+\"+str(self.c)\n   \
    \         else:return str(self.c)\n\n        t=\"sqrt[\"+str(self.b)+\"]\"\n\n\
    \        if self.c>0:\n            if self.c==1:return \"+\"+t\n            else:return\
    \ \"+\"+str(self.c)+t\n        else:\n            if self.c==-1:return  \"-\"\
    +t\n            else:return str(self.c)+t\n\n    def __add__(self,other):\n  \
    \      r=root()\n        if self.b!=other.b:\n            print(\"Unmatch base!\"\
    )\n        else:\n            r=root(self.c+other.c,self.b)\n        return r\n\
    \n    def __radd__(self,other):\n        r=root()\n        if self.b!=other.b:\n\
    \            print(\"Unmatch base!\")\n        else:\n            r=root(self.c+other.c,self.b)\n\
    \        return r\n\n    def __sub__(self,other):\n        return self+(-other)\n\
    \n    def __rsub__(self,other):\n        return -self+other\n\n    def __mul__(self,other):\n\
    \        return root.__reduce(root(self.c*other.c,self.b*other.b))\n\n    def\
    \ __rmul__(self,other):\n        return root.__reduce(root(self.c*other.c,self.b*other.b))\n\
    \n    def __truediv__(self,other):\n        a=self.c\n        b=self.b\n     \
    \   c=other.c\n        d=other.b\n        return root.__reduce(root(Fraction(a,c*d),b*d))\n\
    \n    def __rtruediv__(self,other):\n        a=other.c\n        b=other.b\n  \
    \      c=self.c\n        d=self.b\n        return root.__reduce(root(Fraction(a,c*d),b*d))\n\
    \n    def __eq__(self,other):\n        if self.b!=other.b:return False\n     \
    \   return (self-other).c==0\n\n    def __pos__(self):\n        return self\n\n\
    \    def __neg__(self):\n        return root(-self.c,self.b)\n\n    def __reduce(self):\n\
    \        for i in range(2,math.floor(math.sqrt(self.b)+1)):\n            while(self.b\
    \ % (i*i)==0):\n                self.c*=i\n                self.b//=i*i\n\n  \
    \      return root(self.c,self.b)\n\n@total_ordering\nclass Root(root):\n    ##\u5165\
    \u529B\u5B9A\u7FA9\n    def __init__(self,*Term):\n        self.term=[]\n    \
    \    for t in Term:\n            self.term.append(root(t[0],t[1]))\n\n    #\u8868\
    \u793A\u5B9A\u7FA9\n    def __str__(self):\n        s=\"\"\n        for t in self.term:\n\
    \            s+=root.string(t)\n\n        if s==\"\":return \"0\"\n        else:return\
    \ s\n\n    #\u56DB\u5247\u6F14\u7B97\u5B9A\u7FA9\n    def __add__(self,other):\n\
    \        r=Root()\n        if not(isinstance(other,Root)):other=Root((other,1))\n\
    \        r.term=[]\n        r.term+=self.term\n        r.term+=other.term\n  \
    \      return Root.__reduce(r)\n\n    def __radd__(self,other):\n        r=Root()\n\
    \        if not(isinstance(other,Root)):other=Root((other,1))\n        r.term=[]\n\
    \        r.term+=self.term\n        r.term+=other.term\n        return Root.__reduce(r)\n\
    \n    def __sub__(self,other):\n        return self+(-other)\n\n    def __rsub__(self,other):\n\
    \        return -self+other\n\n    def __mul__(self,other):\n        r=Root()\n\
    \        for t in self.term:\n            for u in other.term:\n             \
    \   r.term.append(t*u)\n        return Root.__reduce(r)\n\n    def __rmul__(self,other):\n\
    \        r=Root()\n        for t in self.term:\n            for u in other.term:\n\
    \                r.term.append(t*u)\n        return Root.__reduce(r)\n\n    def\
    \ __truediv__(self,other):\n        if not(isinstance(self,Fraction)):self=Root((self,1))\n\
    \n        u=Root()\n        u.term=copy(self.term)\n\n        if len(u.term)==1:\n\
    \            r=Root()\n            for a in u.term:\n                r+=a/u\n\
    \        else:\n            p=Root()\n            v=Root()\n            p.term=copy(other.term)\n\
    \            v.term=list.pop(u.term)\n            return (p*(u-v))/(u*u+v*v)\n\
    \n        return r\n\n    def __rtruediv__(self,other):\n        if not(isinstance(other,Fraction)):other=Root((other,1))\n\
    \n        u=Root()\n        u.term=copy(other.term)\n\n        if len(u.term)==1:\n\
    \            r=Root()\n            for a in u.term:\n                r+=a/u\n\
    \        else:\n            p=Root()\n            v=Root()\n            p.term=copy(self.term)\n\
    \            v.term=list.pop(u.term)\n            return (p*(u-v))/(u*u+v*v)\n\
    \n        return r\n\n    #\u6BD4\u8F03\u6F14\u7B97\u5B50\n    def __eq__(self,other):\n\
    \        return (self-other).a==0\n\n    def __lt__(self,other):\n        return\
    \ (self-other).a<0\n\n    #\u305D\u306E\u4ED6\n    def ToNumber(self):\n     \
    \   return self.a/self.b\n\n    def sign(self):\n        s=self.a*self.b\n   \
    \     if s>0:return 1\n        elif s==0:return 0\n        else:return -1\n\n\
    \    def __reduce(self):\n        r=Root()\n        r.term=copy(self.term)\n\n\
    \        for t in range(len(self.term)):\n            for u in range(t+1,len(self.term)):\n\
    \                if r.term[t].b==r.term[u].b:\n                    r.term[t]+=r.term[u]\n\
    \                    r.term[u]=root(0,1)\n\n        s=Root()\n        s.term=copy(r.term)\n\
    \n        for t in s.term:\n            if t==root():r.term.remove(t)\n      \
    \  return\n\n    def __pos__(self):\n        return self\n\n    def __neg__(self):\n\
    \        r=Root()\n        r.term=[]\n        for t in self.term:\n          \
    \  r.term+=[-t]\n        return r\n\n    def __abs__(self):\n        if self>=0:return\
    \ self\n        else:return -self\n\n    def __len__(self):\n        return len(self.term)\n"
  dependsOn:
  - Number.py
  - Fraction.py
  isVerificationFile: false
  path: Root.py
  requiredBy: []
  timestamp: '2023-07-02 11:15:33+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Root.py
layout: document
redirect_from:
- /library/Root.py
- /library/Root.py.html
title: Root.py
---
