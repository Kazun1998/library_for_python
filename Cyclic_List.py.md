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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.6/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.6/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class Cyclic_List:\n    def __init__(self, N, default):\n        \"\"\" N\
    \ \u500B\u306E\u8981\u7D20\u5168\u3066\u304C default \u3067\u3042\u308B\u30EA\u30B9\
    \u30C8\u3092\u751F\u6210\u3059\u308B.\n\n        Args:\n            N (int): \u8981\
    \u7D20\u6570\n            default : \u57CB\u3081\u308B\u5024\n        \"\"\"\n\
    \n        self.list = [default for _ in range(N)]\n        self.N = N\n      \
    \  self.offset = 0\n\n    def push(self, k = 1):\n        \"\"\" k \u8981\u7D20\
    \u3060\u3051\u9032\u3081\u308B (\u7B2C i \u8981\u7D20\u304C\u7B2C (i+k) \u8981\
    \u7D20\u306B\u79FB\u52D5\u3059\u308B)\n\n        Args:\n            k (int, optional):\
    \ \u79FB\u52D5\u91CF. Defaults to 1.\n        \"\"\"\n\n        self.offset +=\
    \ k\n        self.offset %= self.N\n\n    def pull(self, k = 1):\n        \"\"\
    \" k \u8981\u7D20\u3060\u3051\u623B\u3059 (\u7B2C i \u8981\u7D20\u304C\u7B2C (i-k)\
    \ \u8981\u7D20\u306B\u79FB\u52D5\u3059\u308B)\n\n        Args:\n            k\
    \ (int, optional): \u79FB\u52D5\u91CF. Defaults to 1.\n        \"\"\"\n\n    \
    \    self.offset -= k\n        self.offset %= self.N\n\n    def __setitem__(self,\
    \ index, value):\n        self.list[(index - self.offset) % self.N] = value\n\n\
    \    def __getitem__(self, index):\n        return self.list[(index - self.offset)\
    \ % self.N]\n\n    def __len__(self):\n        return self.N\n\n    def __iter__(self):\n\
    \        for i in range(len(self)):\n            yield self[i]\n\n    def __str__(self):\n\
    \        return f\"[{', '.join(map(str, self))}]\"\n\n    __repr__ = __str__\n"
  dependsOn: []
  isVerificationFile: false
  path: Cyclic_List.py
  requiredBy: []
  timestamp: '2024-09-22 11:03:05+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Cyclic_List.py
layout: document
redirect_from:
- /library/Cyclic_List.py
- /library/Cyclic_List.py.html
title: Cyclic_List.py
---
