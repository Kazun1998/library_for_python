---
data:
  _extendedDependsOn:
  - icon: ':warning:'
    path: Complex.py
    title: Complex.py
  - icon: ':warning:'
    path: Fraction.py
    title: Fraction.py
  - icon: ':warning:'
    path: Quaternion.py
    title: Quaternion.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.0/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.0/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "import math\nfrom Fraction import Fraction\nfrom Complex import Complex\n\
    from Quaternion import Quaternion\n\nclass Vector3(Quaternion):\n    #\u5165\u529B\
    \u5B9A\u7FA9\n    def __init__(self,x=0,y=0,z=0):\n        self.x=x\n        self.y=y\n\
    \        self.z=z\n\n    #\u8868\u793A\u5B9A\u7FA9\n    def __str__(self):\n \
    \       return \"(\"+str(self.x)+\",\"+str(self.y)+\",\"+str(self.z)+\")\"\n\n\
    \    #\u56DB\u5247\u6F14\u7B97\u5B9A\u7FA9\n    def __add__(self,other):\n   \
    \     v=Vector3()\n        v.x=self.x+other.x\n        v.y=self.y+other.y\n  \
    \      v.z=self.z+other.z\n        return v\n\n    def __radd__(self,other):\n\
    \        v=Vector3()\n        v.x=self.x+other.x\n        v.y=self.y+other.y\n\
    \        v.z=self.z+other.z\n        return v\n\n    def __sub__(self,other):\n\
    \        return self+(-other)\n\n    def __rsub__(self,other):\n        return\
    \ -self+other\n\n    def __mul__(self,other):\n        v=Vector3()\n        v.x=self.x*other.x\n\
    \        v.y=self.y*other.y\n        v.z=self.z*other.z\n        return v\n\n\
    \    def __rmul__(self,other):\n        v=Vector3()\n        v.x=self.x*other.x\n\
    \        v.y=self.y*other.y\n        v.z=self.z*other.z\n        return v\n\n\
    \    def __truediv__(self,other):\n        return self*Vector3.__inverse(other)\n\
    \n    def __rtruediv__(self,other):\n        return Vector3.__inverse(self)*other\n\
    \n    def scaling(self,scale):\n        s=Vector3(scale,scale,scale)\n       \
    \ return self*s\n\n    #\u6BD4\u8F03\u6F14\u7B97\u5B50\n    def __eq__(self,other):\n\
    \        return (self-other)==Vector3()\n\n    #\u305D\u306E\u4ED6\n    def inner(self,other):\n\
    \        r=Quaternion()\n        r+=Quaternion.conjugate(self.x)*other.x\n   \
    \     r+=Quaternion.conjugate(self.y)*other.y\n        r+=Quaternion.conjugate(self.z)*other.z\n\
    \        return r.r\n\n    def cross(self,other):\n        v=Vector3()\n     \
    \   v.x=self.y*other.z-self.z*other.y\n        v.y=self.z*other.x-self.x*other.z\n\
    \        v.z=self.x*other.y-self.y*other.x\n        return v\n\n    def __abs__(self):\n\
    \        return math.sqrt(Vector3.inner(v,v))\n\n    def abs2(self):\n       \
    \ return Vector3.inner(v,v)\n\n    def internal(self,other,m,n):\n        if m==-n:\n\
    \            return Vector3.scaling(Vector3.scaling(other,m)+Vector3.scaling(self,n),Fraction(1,m+n))\n\
    \n        else:\n            print(\"Cannot internal divide\",m,\":\",n,\"!\"\
    )\n            return Vector3()\n\n    def external(self,other,m,n):\n       \
    \ if m!=n:\n            return Vector3.internal(self,other,m,-n)\n\n        else:\n\
    \            print(\"Cannot external divide\",m,\":\",n,\"!\")\n            return\
    \ Vector3()\n\n    def middle(self,other):\n        return Vector3.internal(self,other,1,1)\n\
    \n    #\u6B63\u8CA0\u5224\u5B9A\n\n    #\u8981\u7D04\n\n    #\u9006\u6570\n  \
    \  def __inverse(self):\n        v=Vector3()\n        if self.x!=0:v.x=1/self.x\n\
    \        else:v.x=0\n        if self.y!=0:v.y=1/self.y\n        else:v.y=0\n \
    \       if self.z!=0:v.z=1/self.z\n        else:v.z=0\n\n        return v\n\n\
    \    #\u7B26\u53F7\n    def __pos__(self):\n        return self\n\n    def __neg__(self):\n\
    \        return Vector3(-self.x,-self.y,-self.z)\n\n\n\n\n"
  dependsOn:
  - Quaternion.py
  - Complex.py
  - Fraction.py
  isVerificationFile: false
  path: Vector3.py
  requiredBy: []
  timestamp: '2023-08-09 23:41:14+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Vector3.py
layout: document
redirect_from:
- /library/Vector3.py
- /library/Vector3.py.html
title: Vector3.py
---
