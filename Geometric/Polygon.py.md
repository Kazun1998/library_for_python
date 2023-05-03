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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.3/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.3/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from Point import *\n\nclass Polygon:\n    __slots__=[\"vertices\",\"id\"\
    ]\n    ep=1e-9\n\n    def __init__(self,*Points):\n        self.vertices=list(Points)\n\
    \        self.id=7\n\n    def __str__(self):\n        return \"[Polygon] \"+\"\
    , \".join(map(repr,self.vertices))\n\n    __repr__=__str__\n\n    def area(self):\n\
    \        S=0\n        p=self.vertices\n        for i in range(len(p)-1):\n   \
    \         S+=p[i].det(p[i+1])\n        S+=p[-1].det(p[0])\n        return abs(S)/2\n\
    \n            \np=lambda x,y:Point(x,y)\nX=[p(0,4),p(1,5),p(1,1),p(2,3),p(2,0),p(3,6),p(4,4),p(4,1),p(5,3),p(6,5),p(6,1),p(7,4)]\n\
    \ndef Convex_Hull(S,online=False):\n    \"\"\" S \u306E\u51F8\u5305\u3092\u6C42\
    \u3081\u308B.\n\n    [Input]\n    S: \u70B9\u306E\u30EA\u30B9\u30C8\n    online:\
    \ \u8FBA\u4E0A\u306E\u70B9\u3092\u8A8D\u3081\u308B\u304B.\n    \"\"\"\n\n    from\
    \ collections import deque\n\n    T=sorted(S)\n\n    #\u4E0A\u5074\n    U=[]\n\
    \    for p in T[::-1]:\n        while len(U)>=2:\n            m=iSP(U[-2],U[-1],p)\n\
    \            if m==-1 or (not online and m==2):\n                U.pop()\n   \
    \         else:\n                break\n        U.append(p)\n\n    #\u4E0B\u5074\
    \n    L=[]\n    for q in T:\n        while len(L)>=2:\n            m=iSP(L[-2],L[-1],q)\n\
    \            if m==-1 or (not online and m==2):\n                L.pop()\n   \
    \         else:\n                break\n        L.append(q)\n\n    return Polygon(*(U+L[1:-1]))\n\
    \ndef is_Convex(P: Polygon,rigit=True):\n    \"\"\" \u591A\u89D2\u5F62 P \u304C\
    \u51F8\u304B\u3069\u3046\u304B\u3092\u5224\u5B9A\u3059\u308B.\n\n    P: Polygon\n\
    \    right: True \u306E\u3068\u304D, \u8FBA\u4E0A\u306E\u70B9\u3092\u8A8D\u3081\
    \u306A\u3044.\n    \"\"\"\n\n    pass\n"
  dependsOn: []
  isVerificationFile: false
  path: Geometric/Polygon.py
  requiredBy: []
  timestamp: '2021-09-04 16:56:37+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Geometric/Polygon.py
layout: document
redirect_from:
- /library/Geometric/Polygon.py
- /library/Geometric/Polygon.py.html
title: Geometric/Polygon.py
---
