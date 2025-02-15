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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.13.2/x64/lib/python3.13/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.13.2/x64/lib/python3.13/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class Bitwise_Set:\n    @staticmethod\n    def emptyset(n):\n        \"\"\
    \" {0, 1, ..., n} \u306E\u90E8\u5206\u96C6\u5408\u3067\u7A7A\u96C6\u5408\u3092\
    \u8868\u3059\u6574\u6570\u3092\u6C42\u3081\u308B (\u8981\u3059\u308B\u306B 0).\n\
    \        \"\"\"\n\n        return 0\n\n    @staticmethod\n    def universal_set(n):\n\
    \        \"\"\" {0, 1, ..., n} \u3092\u8868\u3059\u6574\u6570\u3092\u6C42\u3081\
    \u308B.\n        \"\"\"\n\n        return (1 << n) - 1\n\n    @classmethod\n \
    \   def subset_yield(cls, S, _):\n        \"\"\" S \u306E\u90E8\u5206\u96C6\u5408\
    \u306E\u30B8\u30A7\u30CD\u30EC\u30FC\u30BF\u3092\u4F5C\u6210\u3059\u308B.\n  \
    \      \"\"\"\n\n        T = S\n        while True:\n            yield T\n   \
    \         if T == 0:\n                break\n\n            T = (T - 1) & S\n\n\
    \    @classmethod\n    def betweenset_yield(cls, S, T):\n        \"\"\" S subset\
    \ U subset T \u3092\u6E80\u305F\u3059\u96C6\u5408 U \u306E\u30B8\u30A7\u30CD\u30EC\
    \u30FC\u30BF\u3092\u4F5C\u6210\u3059\u308B.\n        \"\"\"\n\n        if S |\
    \ T != T:\n            return\n\n        for V in cls.subset_yield(T ^ S, 0):\n\
    \            yield S | V\n\n    @classmethod\n    def superset_yield(cls, S, n):\n\
    \        \"\"\" S \u306E\u4E0A\u4F4D\u96C6\u5408\u306E\u30B8\u30A7\u30CD\u30EC\
    \u30FC\u30BF\u3092\u4F5C\u6210\u3059\u308B.\n        \"\"\"\n\n        yield from\
    \ cls.betweenset_yield(S, cls.universal_set(n))\n\n    @classmethod\n    def build(cls,\
    \ E):\n        \"\"\" \u96C6\u5408 E \u3092\u8868\u3059\u6574\u6570\u3092\u8FD4\
    \u3059.\n        \"\"\"\n\n        return sum(1 << k for k in E)\n\n    @classmethod\n\
    \    def bit(cls, A, k):\n        return (A >> k) & 1\n\n    @classmethod\n  \
    \  def add(cls, A, k):\n        return A | (1 << k)\n\n    @classmethod\n    def\
    \ remove(cls, A, k):\n        return A & (~ (1 << k))\n\n    @classmethod\n  \
    \  def switch(cls, A, k):\n        return A ^ (1 << k)\n\n    @classmethod\n \
    \   def popcount(cls, A: int):\n        return A.bit_count()\n\n    @classmethod\n\
    \    def get_min(self, A: int):\n        return (A & (-A)).bit_length() - 1\n"
  dependsOn: []
  isVerificationFile: false
  path: Bitwise_Set.py
  requiredBy: []
  timestamp: '2024-11-16 23:59:30+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Bitwise_Set.py
layout: document
redirect_from:
- /library/Bitwise_Set.py
- /library/Bitwise_Set.py.html
title: Bitwise_Set.py
---
