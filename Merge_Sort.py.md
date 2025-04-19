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
  code: "from typing import TypeVar, Callable, Generic\n\nT = TypeVar('T')\nclass\
    \ Merge_Sort(Generic[T]):\n    @staticmethod\n    def sort_by_index(X: list[T],\
    \ reverse: bool = False, key: Callable[[T, T], int] = None) -> list[int]:\n  \
    \      \"\"\" \u5B89\u5B9A\u30DE\u30FC\u30B8\u30BD\u30FC\u30C8 (\u6607\u9806)\
    \ \u306E\u7D50\u679C\u3092\u30A4\u30F3\u30C7\u30C3\u30AF\u30B9\u306E\u914D\u5217\
    \u3067\u6C42\u3081\u308B.\n\n        Args:\n            X (list[T]): \u30BD\u30FC\
    \u30C8\u5BFE\u8C61\n            reverse (bool, optional): True \u306A\u3089\u3070\
    \u964D\u9806\u306B\u4E26\u3073\u66FF\u3048\u308B.. Defaults to False.\n      \
    \      key (Callable[[T, T], int], optional): \u6BD4\u8F03\u65B9\u6CD5\u306E\u6307\
    \u5B9A (key(x, y) \u306F x < y \u306A\u3089\u3070\u8CA0, x == y \u306A\u3089\u3070\
    \ 0, x > y \u306A\u3089\u3070\u6B63\u3068\u306A\u308B\u3088\u3046\u306B\u3059\u308B\
    ). Defaults to None.\n\n        Returns:\n            list[int]: \u5B89\u5B9A\u30DE\
    \u30FC\u30B8\u30BD\u30FC\u30C8 (\u6607\u9806) \u306E\u7D50\u679C\u306E\u30A4\u30F3\
    \u30C7\u30C3\u30AF\u30B9\u306E\u914D\u5217\n        \"\"\"\n\n        if not X:\n\
    \            return []\n\n        if key is None:\n            def key(x: T, y:\
    \ T) -> int:\n                if x < y:\n                    return -1\n     \
    \           elif x == y:\n                    return 0\n                elif x\
    \ > y:\n                    return 1\n\n        from collections import deque\n\
    \        queue = deque([[k] for k in range(len(X))])\n\n        def merge(A: list[int],\
    \ B: list[int]) -> list[int]:\n            i = j = 0\n            C= [-1] * (len(A)\
    \ + len(B))\n            for t in range(len(A) + len(B)):\n                if\
    \ (i < len(A)) and (j < len(B)):\n                    cmp = key(X[A[i]], X[B[j]])\n\
    \                    if cmp == 0:\n                        cmp = 1 if A[i] < B[j]\
    \ else -1\n                elif i == len(A):\n                    cmp = 1\n  \
    \              elif j == len(B):\n                    cmp = -1\n\n           \
    \     if cmp < 0:\n                    C[t] = A[i]\n                    i += 1\n\
    \                else:\n                    C[t] = B[j]\n                    j\
    \ += 1\n            return C\n\n        for _ in range(len(X) - 1):\n        \
    \    A = queue.popleft()\n            B = queue.popleft()\n            queue.append(merge(A,\
    \ B))\n\n        res = queue.pop()\n        if reverse:\n            res.reverse()\n\
    \        return res\n\n    @classmethod\n    def sort(cls, X: list[T], reverse:\
    \ bool = False, key: Callable[[T, T], int] = None) -> list[int]:\n        return\
    \ [X[k] for k in cls.sort_by_index(X, reverse = reverse, key = key)]\n"
  dependsOn: []
  isVerificationFile: false
  path: Merge_Sort.py
  requiredBy: []
  timestamp: '2025-02-22 17:04:02+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Merge_Sort.py
layout: document
redirect_from:
- /library/Merge_Sort.py
- /library/Merge_Sort.py.html
title: Merge_Sort.py
---
