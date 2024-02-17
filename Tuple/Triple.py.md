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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.2/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.2/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class Triple:\n    __slot__=(\"first\", \"second\", \"third\")\n\n    def\
    \ __init__(self, first, second, third):\n        self.first=first\n        self.second=second\n\
    \        self.third=third\n\n    def __str__(self):\n        return \"({}, {},\
    \ {})\".format(self.first, self.second, self.third)\n\n    def __repr__(self):\n\
    \        return \"[Triple] : \"+str(self)\n\n    def __iter__(self):\n       \
    \ yield from [self.first, self.second, self.third]\n\n    def __eq__(self, other):\n\
    \        return (self.first==other.first) and (self.second==other.second) and\
    \ (self.thrid==other.third)\n\n    def __neq__(self, other):\n        return not\
    \ (self==other)\n\n    def __le__(self, other):\n        f=(self.first<other.first)\n\
    \        g=(self.first==other.first and self.second<other.second)\n        h=(self.first==other.first\
    \ and self.second==self.second and self.third<=other.third)\n        return  f\
    \ or g or h\n\n    def __lt__(self, other):\n        f=(self.first<other.first)\n\
    \        g=(self.first==other.first and self.second<other.second)\n        h=(self.first==other.first\
    \ and self.second==self.second and self.third<other.third)\n        return  f\
    \ or g or h\n\n    def __ge__(self, other):\n        f=(self.first>other.first)\n\
    \        g=(self.first==other.first and self.second>other.second)\n        h=(self.first==other.first\
    \ and self.second==self.second and self.third>=other.third)\n        return  f\
    \ or g or h\n\n    def __gt__(self, other):\n        f=(self.first>other.first)\n\
    \        g=(self.first==other.first and self.second>other.second)\n        h=(self.first==other.first\
    \ and self.second==self.second and self.third>other.third)\n        return  f\
    \ or g or h\n\n    def __add__(self, other):\n        return Triple(self.first+other.first,\
    \ self.second+other.second, self.third+other.third)\n\n    def __radd__(self,\
    \ other):\n        self.first+=other.first\n        self.second+=other.second\n\
    \        self.third+=other.third\n        return self\n\n    def __sub__(self,\
    \ other):\n        return Triple(self.first-other.first, self.second-other.second,\
    \ self.third-other.third)\n\n    def __rsub__(self, other):\n        self.first-=other.first\n\
    \        self.second-=other.second\n        self.third-=other.third\n        return\
    \ self\n\n    def __mul__(self, other):\n        return Triple(self.first*other.first,\
    \ self.second*other.second, self.third*other.third)\n\n    def __rmul__(self,\
    \ other):\n        self.first*=other.first\n        self.second*=other.second\n\
    \        self.third*=other.third\n        return self\n\n    def __floordiv__(self,\
    \ other):\n        return Triple(self.first//other.first, self.second//other.second,\
    \ self.third//other.third)\n\n    def __rfloordiv__(self, other):\n        self.first//=other.first\n\
    \        self.second//=other.second\n        self.third//=other.third\n      \
    \  return self\n\n    def __truediv__(self, other):\n        return Triple(self.first/other.first,\
    \ self.second/other.second, self.third/other.third)\n\n    def __rtruediv__(self,\
    \ other):\n        self.first/=other.first\n        self.second/=other.second\n\
    \        self.third/=other.third\n        return self\n"
  dependsOn: []
  isVerificationFile: false
  path: Tuple/Triple.py
  requiredBy: []
  timestamp: '2023-01-01 16:05:24+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Tuple/Triple.py
layout: document
redirect_from:
- /library/Tuple/Triple.py
- /library/Tuple/Triple.py.html
title: Tuple/Triple.py
---
