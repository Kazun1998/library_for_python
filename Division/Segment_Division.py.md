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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.8/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.8/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class Segment_Division:\n    def __init__(self, N: int):\n        self.N\
    \ = N\n        self.depth = max(1, (N - 1).bit_length())\n        self.size =\
    \ 1 << self.depth\n\n        self.range = [None] * (self.size) + [(i, i) for i\
    \ in range(self.N)] + [None] * (self.size - self.N)\n\n        for i in range(self.size\
    \ - 1, 0, -1):\n            if (self.range[2 * i] is not None) and (self.range[2\
    \ * i + 1] is not None):\n                self.range[i] = (self.range[2 * i][0],\
    \ self.range[2 * i + 1][1])\n\n    def interval(self, left: int, right: int, left_closed\
    \ = True, right_closed = True):\n        assert (0 <= left < self.size) and (0\
    \ <= right < self.size)\n\n        l = left + self.size + (not left_closed)\n\
    \        r = right + self.size + (right_closed)\n\n        left_seg = []\n   \
    \     right_seg = []\n        while l < r:\n            if l & 1:\n          \
    \      yield self.range[l]\n                l += 1\n\n            if r & 1:\n\
    \                r -= 1\n                yield self.range[r]\n\n            l\
    \ >>= 1\n            r >>= 1\n\n        return left_seg + right_seg[::-1]\n\n\
    \    def all_segments(self):\n        return [seg for seg in self.range[1:] if\
    \ seg is not None]\n"
  dependsOn: []
  isVerificationFile: false
  path: Division/Segment_Division.py
  requiredBy: []
  timestamp: '2024-02-10 23:31:10+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Division/Segment_Division.py
layout: document
redirect_from:
- /library/Division/Segment_Division.py
- /library/Division/Segment_Division.py.html
title: Division/Segment_Division.py
---
