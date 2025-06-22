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
  code: "from heapq import heappop, heappush\n\nclass Dijkstra_Point:\n    __slots__\
    \ = (\"__point\", \"__dist\")\n\n    def __init__(self, point: int, dist: int):\n\
    \        self.__dist = dist\n        self.__point = point\n\n    @property\n \
    \   def dist(self) -> int:\n        return self.__dist\n\n    @property\n    def\
    \ point(self) -> int:\n        return self.__point\n\n    def __str__(self) ->\
    \ str:\n        return f\"(point: {self.point}, dist: {self.dist})\"\n\n    def\
    \ __repr__(self) -> str:\n        return f\"{self.__class__.__name__}(point={self.point},\
    \ dist={self.dist})\"\n\n    def __lt__(self, other: \"Dijkstra_Point\") -> bool:\n\
    \        return self.dist < other.dist\n\n    def __iter__(self):\n        yield\
    \ from (self.point, self.dist)\n\nclass Dijkstra_Heap:\n    def __init__(self):\n\
    \        self.__heap: list[Dijkstra_Point] = []\n\n    def __bool__(self) -> bool:\n\
    \        return bool(self.__heap)\n\n    def push(self, point: int, dist: int):\n\
    \        \"\"\" \u9802\u70B9 point \u307E\u3067\u306E\u8DDD\u96E2\u304C dist \u3067\
    \u3042\u308B\u60C5\u5831\u3092\u30D2\u30FC\u30D7\u306B\u8FFD\u52A0\u3059\u308B\
    .\n\n        Args:\n            point (int): \u9802\u70B9\n            dist (int):\
    \ \u8DDD\u96E2\n        \"\"\"\n\n        heappush(self.__heap, Dijkstra_Point(point,\
    \ dist))\n\n    def pop(self) -> Dijkstra_Point:\n        \"\"\" \u6B21\u306B\u78BA\
    \u5B9A\u3055\u305B\u308B\u3079\u304D\u9802\u70B9\u3068\u8DDD\u96E2\u306E\u60C5\
    \u5831\u3092 pop \u3059\u308B.\n\n        Returns:\n            Dijkstra_Point:\
    \ \u6B21\u306B\u78BA\u5B9A\u3055\u305B\u308B\u3079\u304D\u9802\u70B9\u3068\u8DDD\
    \u96E2\u306E\u60C5\u5831\n        \"\"\"\n        assert self.__heap\n       \
    \ return heappop(self.__heap)\n"
  dependsOn: []
  isVerificationFile: false
  path: Dijkstra_Heap.py
  requiredBy: []
  timestamp: '2025-06-22 10:21:17+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Dijkstra_Heap.py
layout: document
redirect_from:
- /library/Dijkstra_Heap.py
- /library/Dijkstra_Heap.py.html
title: Dijkstra_Heap.py
---
