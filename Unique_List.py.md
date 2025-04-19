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
  code: "from typing import TypeVar, Generic\n\nclass DuplicateValue(Exception):\n\
    \    pass\n\nT = TypeVar('T')\nclass Unique_List(Generic[T]):\n    def __init__(self,\
    \ A: list[T | None]):\n        \"\"\" \u8981\u7D20\u306E\u4E00\u610F\u6027\u304C\
    \u4FDD\u8A3C\u3055\u308C\u305F\u30EA\u30B9\u30C8\u3092\u751F\u6210\u3059\u308B\
    .\n\n        Args:\n            A (list[T]): \u91CD\u8907\u304C\u5B58\u5728\u3057\
    \u306A\u3044\u30EA\u30B9\u30C8\n\n        Raises:\n            DuplicateValue:\
    \ A \u306B\u91CD\u8907\u304C\u3042\u3063\u305F\u3068\u304D\u306B\u767A\u751F\n\
    \        \"\"\"\n\n        index: dict[T, int] = {}\n        for i, a in enumerate(A):\n\
    \            if a is None:\n                continue\n\n            if a in index:\n\
    \                raise DuplicateValue('\u91CD\u8907\u3059\u308B\u8981\u7D20\u304C\
    \u3042\u308A\u307E\u3059')\n\n            index[a] = i\n\n        self.__list\
    \ = A\n        self.__index = index\n\n    def __repr__(self) -> str:\n      \
    \  return f\"{self.__class__.__name__}({self.__list})\"\n\n    def update(self,\
    \ i: int, a: T):\n        \"\"\" \u7B2C i \u8981\u7D20\u3092 a \u306B\u5909\u66F4\
    \u3059\u308B (\u5909\u66F4\u5F8C\u306B\u91CD\u8907\u3059\u308B\u8981\u7D20\u304C\
    \u3042\u3063\u3066\u306F\u3044\u3051\u306A\u3044)\n\n        Args:\n         \
    \   i (int): \u5909\u66F4\u3059\u308B\u5834\u6240\n            a (T): \u5909\u66F4\
    \u5F8C\u306E\u5024\n\n        Raises:\n            DuplicateValue: (\u5909\u66F4\
    \u5F8C\u306B\u91CD\u8907\u3059\u308B\u8981\u7D20\u304C\u3042\u3063\u3066\u306F\
    \u3044\u3051\u306A\u3044)\n        \"\"\"\n\n        # \u5909\u308F\u3089\u306A\
    \u3044\u306A\u3089\u3070\u65E9\u671F Return\n        if self[i] == a:\n      \
    \      return\n\n        # \u91CD\u8907\u30C1\u30A7\u30C3\u30AF\n        if a\
    \ in self.__index:\n            raise DuplicateValue\n\n        del self.__index[self[i]]\n\
    \n        if a is not None:\n            self.__index[a] = i\n\n        self.__list[i]\
    \ = a\n\n    def __getitem__(self, i: int) -> T:\n        return self.__list[i]\n\
    \n    __setitem__ = update\n\n    def __include__(self, a: T) -> bool:\n     \
    \   return a in self.__index\n\n    def index(self, a: T, default = None) -> int:\n\
    \        \"\"\" a \u304C\u3042\u308B\u5834\u6240\u3092\u53D6\u5F97\u3059\u308B\
    \ (\u5B58\u5728\u3057\u306A\u3044\u5834\u5408\u306F default)\n\n        Args:\n\
    \            a (T): \u63A2\u7D22\u3059\u308B\u8981\u7D20\n            default\
    \ (_type_, optional): \u5B58\u5728\u3057\u306A\u3044\u5834\u5408\u306E\u8FD4\u308A\
    \u5024. Defaults to None.\n\n        Returns:\n            int: a \u304C\u3042\
    \u308B\u5834\u6240\n        \"\"\"\n\n        return self.__index.get(a, default)\n\
    \n    def swap(self, i: int, j: int):\n        \"\"\" \u7B2C i \u8981\u7D20\u3068\
    \u7B2C j \u8981\u7D20\u3092\u4EA4\u63DB\u3059\u308B.\n\n        Args:\n      \
    \      i (int):\n            j (int):\n        \"\"\"\n\n        a = self.__list[i];\
    \ b = self.__list[j]\n\n        self.__list[i] = b; self.__list[j] = a\n     \
    \   self.__index[a] = j; self.__index[b] = i\n\n    def transposition(self, a:\
    \ T, b: T):\n        \"\"\" \u8981\u7D20 a \u3068\u8981\u7D20 b \u3092\u4EA4\u63DB\
    \u3059\u308B.\n\n        Args:\n            a (T):\n            b (T):\n     \
    \   \"\"\"\n\n        i = self.__index[a]; j = self.__index[b]\n\n        self.__list[i]\
    \ = b; self.__list[j] = a\n        self.__index[a] = j; self.__index[b] = i\n"
  dependsOn: []
  isVerificationFile: false
  path: Unique_List.py
  requiredBy: []
  timestamp: '2025-03-28 23:59:07+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Unique_List.py
layout: document
redirect_from:
- /library/Unique_List.py
- /library/Unique_List.py.html
title: Unique_List.py
---
