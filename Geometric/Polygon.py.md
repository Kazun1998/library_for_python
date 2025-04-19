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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.13.3/x64/lib/python3.13/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.13.3/x64/lib/python3.13/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from Point import *\n\nclass Polygon:\n    __slots__ = (\"vertices\", )\n\
    \n    def __init__(self, *points: Point):\n        self.vertices = list(points)\n\
    \n    def __str__(self):\n        return f\"[Polygon] {', '.join(map(str, self.vertices))}\"\
    \n\n    def __repr__(self) -> str:\n        return f\"{self.__class__.__name__}({',\
    \ '.join(map(repr, self.vertices))})\"\n\n    def area(self):\n        S = 0\n\
    \        vertices = self.vertices\n        for i in range(len(vertices) - 1):\n\
    \            S += vertices[i].det(vertices[i + 1])\n        S += vertices[-1].det(vertices[0])\n\
    \        return abs(S) / 2\n\ndef Convex_Hull(S: list[Point], online = False)\
    \ -> Polygon:\n    \"\"\" S \u306E\u51F8\u5305\u3092\u6C42\u3081\u308B\n\n   \
    \ Args:\n        S (list[Point]): \u70B9\u96C6\u5408\n        online (bool, optional):\
    \ False \u306E\u3068\u304D, \u5185\u89D2\u304C 180 \u5EA6\u306B\u306A\u308B\u306E\
    \u3092\u8A31\u5BB9\u3057\u306A\u3044. Defaults to False.\n\n    Returns:\n   \
    \     Polygon: S \u306E\u51F8\u5305\n    \"\"\"\n\n    def cover(reverse_flag):\n\
    \        vertices = []\n        for P in (reversed(S) if reverse_flag else S):\n\
    \            if not online and vertices and vertices[-1] == P:\n             \
    \   continue\n\n            while len(vertices)>=2:\n                m = iSP(vertices[-2],\
    \ vertices[-1], P)\n                if m == -1 or (not online and m == 2):\n \
    \                   vertices.pop()\n                else:\n                  \
    \  break\n            vertices.append(P)\n        return vertices\n\n    S.sort()\n\
    \n    #\u4E0A\u5074\n    upper = cover(True)\n\n    #\u4E0B\u5074\n    lower =\
    \ cover(False)\n\n    return Polygon(*(upper + lower[1:-1]))\n\ndef is_Convex(P:\
    \ Polygon,rigit=True):\n    \"\"\" \u591A\u89D2\u5F62 P \u304C\u51F8\u304B\u3069\
    \u3046\u304B\u3092\u5224\u5B9A\u3059\u308B.\n\n    P: Polygon\n    right: True\
    \ \u306E\u3068\u304D, \u8FBA\u4E0A\u306E\u70B9\u3092\u8A8D\u3081\u306A\u3044.\n\
    \    \"\"\"\n\n    pass\n"
  dependsOn: []
  isVerificationFile: false
  path: Geometric/Polygon.py
  requiredBy: []
  timestamp: '2025-03-01 11:09:03+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Geometric/Polygon.py
layout: document
redirect_from:
- /library/Geometric/Polygon.py
- /library/Geometric/Polygon.py.html
title: Geometric/Polygon.py
---
