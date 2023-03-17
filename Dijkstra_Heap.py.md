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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.2/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.2/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from heapq import heappop,heappush\nclass Heap_Point:\n        def __init__(self,x,d):\n\
    \            self.d=d\n            self.x=x\n\n        def __str__(self):\n  \
    \          return \"(point:{}, dist:{})\".format(self.x,self.d)\n\n        def\
    \ __repr__(self):\n            return str(self)\n\n        def __lt__(self,other):\n\
    \            return self.d<other.d\n\n        def __iter__(self):\n          \
    \  yield from (self.x,self.d)\n\nclass Dijkstra_Heap:\n    def __init__(self):\n\
    \        self.heap=[]\n\n    def __str__(self):\n        return str(self.heap)\n\
    \n    def __repr__(self):\n        return repr(self.heap)\n\n    def __bool__(self):\n\
    \        return bool(self.heap)\n\n    def push(self,point,dist):\n        heappush(self.heap,Heap_Point(point,dist))\n\
    \n    def pop(self):\n        assert self.heap\n        return heappop(self.heap)\n"
  dependsOn: []
  isVerificationFile: false
  path: Dijkstra_Heap.py
  requiredBy: []
  timestamp: '2021-04-27 14:48:27+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Dijkstra_Heap.py
layout: document
redirect_from:
- /library/Dijkstra_Heap.py
- /library/Dijkstra_Heap.py.html
title: Dijkstra_Heap.py
---
