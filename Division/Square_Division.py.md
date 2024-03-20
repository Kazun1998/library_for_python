---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test_verify/yosupo_library_checker/Data_Structure/Square_Division.test.py
    title: test_verify/yosupo_library_checker/Data_Structure/Square_Division.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.2/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.2/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class Square_Division:\n    def __init__(self, L, op, unit):\n        self.op\
    \ = op\n        self.unit = unit\n\n        self.N = N = len(L)\n        self.bucket_size\
    \ = int(pow(N, 0.5) + 1)\n        self.bucket_number = (N - 1) // self.bucket_size\
    \ + 1\n\n        self.upper = [unit] * self.bucket_number\n        self.lower\
    \ = [unit] * self.bucket_number * self.bucket_size\n\n        for i in range(N):\n\
    \            self.lower[i] = L[i]\n\n            t = i // self.bucket_size\n \
    \           self.upper[t] = op(self.upper[t], self.lower[i])\n\n    def update(self,\
    \ k, x):\n        \"\"\" \u7B2C k \u8981\u7D20\u3092 x \u306B\u5909\u66F4\u3059\
    \u308B.\n\n        Args:\n            k (int): index\n            x : value\n\
    \        \"\"\"\n\n        self.lower[k] = x\n\n        l = self.bucket_size *\
    \ (k // self.bucket_size)\n        r = l + self.bucket_size\n        y = self.unit\n\
    \        for i in range(l, r):\n            y = self.op(y, self.lower[i])\n\n\
    \        self.upper[k // self.bucket_size] = y\n\n    def product(self, l, r,\
    \ left_close = True, right_close = True):\n        \"\"\" \u7B2C l \u9805\u304B\
    \u3089\u7B2C r \u9805\u307E\u3067\u306E\u7A4D\u3092\u6C42\u3081\u308B.\n\n   \
    \     Args:\n            l (int): \u5DE6\u7AEF\n            r (int): \u53F3\u7AEF\
    \n        \"\"\"\n\n        if not left_close:\n            l += 1\n\n       \
    \ if not right_close:\n            r -= 1\n\n        b = self.bucket_size\n  \
    \      op = self.op\n        lower = self.lower\n        upper = self.upper\n\
    \        prod = self.unit\n\n        if l // b == r // b:\n            for i in\
    \ range(l, r + 1):\n                prod = op(prod, lower[i])\n            return\
    \ prod\n\n        while l % b != 0:\n            prod = op(prod, lower[l])\n \
    \           l += 1\n\n        while l + (b - 1) <= r:\n            prod = op(prod,\
    \ upper[l // b])\n            l += b\n\n        while l <= r:\n            prod\
    \ = op(prod, lower[l])\n            l += 1\n\n        return prod\n\n    def __getitem__(self,\
    \ k):\n        return self.lower[k]\n"
  dependsOn: []
  isVerificationFile: false
  path: Division/Square_Division.py
  requiredBy: []
  timestamp: '2024-03-05 00:39:44+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test_verify/yosupo_library_checker/Data_Structure/Square_Division.test.py
documentation_of: Division/Square_Division.py
layout: document
redirect_from:
- /library/Division/Square_Division.py
- /library/Division/Square_Division.py.html
title: Division/Square_Division.py
---
