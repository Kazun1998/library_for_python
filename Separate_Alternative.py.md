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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.13.1/x64/lib/python3.13/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.13.1/x64/lib/python3.13/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class Separate_Alternative:\n    def __init__(self, N):\n        self.N=N\n\
    \n        self.same_edge=[[] for _ in range(N)]\n        self.diff_edge=[[] for\
    \ _ in range(N)]\n\n    def same(self, x, y):\n        self.same_edge[x].append(y)\n\
    \        self.same_edge[y].append(x)\n\n    def difference(self, x, y):\n    \
    \    self.diff_edge[x].append(y)\n        self.diff_edge[y].append(x)\n\n    def\
    \ is_reasonable(self):\n        T=[0]*self.N\n        for x in range(self.N):\n\
    \            if T[x]!=0:\n                continue\n\n            T[x]=1\n   \
    \         S=[x]\n            while S:\n                y=S.pop()\n           \
    \     for z in self.same_edge[y]:\n                    if T[z]==0:\n         \
    \               T[z]=T[y]\n                        S.append(z)\n             \
    \       elif T[z]!=T[y]:\n                        return False\n\n           \
    \     for z in self.diff_edge[y]:\n                    if T[z]==0:\n         \
    \               T[z]=-T[y]\n                        S.append(z)\n            \
    \        elif T[z]==T[y]:\n                        return False\n        return\
    \ True\n\n    def separate(self):\n        Sep=[]\n        seen=[0]*self.N\n\n\
    \        for x in range(self.N):\n            if seen[x]!=0:\n               \
    \ continue\n\n            seen[x]=1\n            U=[x]; V=[]\n            S=[x]\n\
    \            while S:\n                y=S.pop()\n                for z in self.same_edge[y]:\n\
    \                    if seen[z]==0:\n                        seen[z]=seen[y]\n\
    \                        S.append(z)\n\n                        if seen[z]==1:\n\
    \                            U.append(z)\n                        else:\n    \
    \                        V.append(z)\n\n                    elif seen[z]!=seen[y]:\n\
    \                        return None\n\n                for z in self.diff_edge[y]:\n\
    \                    if seen[z]==0:\n                        seen[z]=-seen[y]\n\
    \                        S.append(z)\n\n                        if seen[z]==1:\n\
    \                            U.append(z)\n                        else:\n    \
    \                        V.append(z)\n\n                    elif seen[z]==seen[y]:\n\
    \                        return None\n\n            Sep.append((U,V))\n      \
    \  return Sep\n"
  dependsOn: []
  isVerificationFile: false
  path: Separate_Alternative.py
  requiredBy: []
  timestamp: '2023-06-17 23:42:00+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Separate_Alternative.py
layout: document
redirect_from:
- /library/Separate_Alternative.py
- /library/Separate_Alternative.py.html
title: Separate_Alternative.py
---
