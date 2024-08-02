---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test_verify/yosupo_library_checker/Data_Structure/Cartesian_Tree.test.py
    title: test_verify/yosupo_library_checker/Data_Structure/Cartesian_Tree.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.4/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.4/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class Cartesian_Tree:\n    def __init__(self, sequence: list):\n        self.sequence\
    \ = sequence\n        self.N = len(sequence)\n        self.left = [-1] * self.N\n\
    \        self.right = [-1] * self.N\n        self.parent = [-1] * self.N\n   \
    \     self.root = -1\n\n        self._build()\n\n    def _build(self):\n     \
    \   A = self.sequence\n        stack = []\n\n        for i in range(self.N):\n\
    \            if i == 0:\n                stack.append(0)\n                self.root\
    \ = 0\n                continue\n\n            last_pop = None\n            while\
    \ stack and A[stack[-1]] >= A[i]:\n                last_pop = stack.pop()\n\n\
    \            # \u5DE6\u306E\u5B50\u306B\u95A2\u3059\u308B\u8A2D\u5B9A\n      \
    \      if last_pop is not None:\n                self.left[i] = last_pop\n   \
    \             self.parent[last_pop] = i\n\n            # \u53F3\u306E\u5B50\u306B\
    \u95A2\u3059\u308B\u8A2D\u5B9A\n            if stack:\n                self.right[stack[-1]]\
    \ = i\n                self.parent[i] = stack[-1]\n            else:\n       \
    \         self.root = i\n\n            stack.append(i)\n"
  dependsOn: []
  isVerificationFile: false
  path: Sequence/Cartesian_Tree.py
  requiredBy: []
  timestamp: '2024-08-02 23:18:01+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test_verify/yosupo_library_checker/Data_Structure/Cartesian_Tree.test.py
documentation_of: Sequence/Cartesian_Tree.py
layout: document
redirect_from:
- /library/Sequence/Cartesian_Tree.py
- /library/Sequence/Cartesian_Tree.py.html
title: Sequence/Cartesian_Tree.py
---
