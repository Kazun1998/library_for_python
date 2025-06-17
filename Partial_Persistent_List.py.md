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
  code: "from bisect import bisect_left\n\nclass Partial_Persistent_List:\n    def\
    \ __init__(self, A: list, auto_commit = False):\n        \"\"\" \u30EA\u30B9\u30C8\
    \ A \u3092\u534A\u6C38\u7D9A\u30EA\u30B9\u30C8\u306B\u3059\u308B.\n\n        Args:\n\
    \            A (list): \u5143\u3068\u306A\u308B\u30EA\u30B9\u30C8\n          \
    \  auto_commit (bool, optional): True \u306A\u3089\u3070\u4EE3\u5165\u3059\u308B\
    \u3068\u81EA\u52D5\u7684\u306B\u6642\u523B\u304C\u9032\u307F, False \u306A\u3089\
    \u3070\u6642\u523B\u306F self.forward_time() \u3067\u9032\u3081\u306A\u3051\u308C\
    \u3070\u306A\u3089\u306A\u3044. Defaults to False.\n        \"\"\"\n\n       \
    \ self.__N = N = len(A)\n        self.__auto_commit = auto_commit\n\n        self.__set_time\
    \ = [[-1] for _ in range(N)]\n        self.__set_value = [[a] for a in A]\n  \
    \      self.__time = 0\n\n    @property\n    def auto_commit(self) -> bool:\n\
    \        return self.__auto_commit\n\n    @property\n    def get_time(self) ->\
    \ int:\n        return self.__time\n\n    def get_value(self, index: int, time:\
    \ int = -1):\n        \"\"\" \u6642\u523B time \u306E\u7B2C index \u8981\u7D20\
    \u3092\u53D6\u5F97\u3059\u308B.\n\n        Args:\n            index (int): \u8981\
    \u7D20\u756A\u53F7\n            time (int, optional): \u6642\u523B. \u305F\u3060\
    \u3057, time = -1 \u306B\u3059\u308B\u3068, \u6700\u65B0\u306E\u7B2C index \u8981\
    \u7D20\u3092\u53D6\u5F97\u3059\u308B. Defaults to -1.\n\n        Returns:\n  \
    \          _type_: _description_\n        \"\"\"\n        if time >= 0:\n    \
    \        j = bisect_left(self.__set_time[index], time) - 1\n        else:\n  \
    \          j = len(self.__set_time[index]) - 1\n\n        return self.__set_value[index][j]\n\
    \n    def set_value(self, index: int, value):\n        \"\"\" \u7B2C index \u8981\
    \u7D20\u3092 value \u306B\u5909\u66F4\u3059\u308B.\n\n        Args:\n        \
    \    index (int): \u8981\u7D20\u756A\u53F7\n            value : \u8981\u7D20\n\
    \        \"\"\"\n\n        times = self.__set_time[index]\n        values = self.__set_value[index]\n\
    \n        if times[-1] == self.time:\n            values[-1] = value\n       \
    \ else:\n            times.append(self.time)\n            values.append(value)\n\
    \n        if self.auto_commit:\n            self.commit()\n\n    def commit(self)\
    \ -> int:\n        \"\"\" \u6642\u523B\u3092 1 \u3064\u3059\u3059\u3081\u308B\
    .\n\n        Returns:\n            int: \u9032\u3081\u305F\u5F8C\u306E\u6642\u523B\
    \n        \"\"\"\n\n        self.__time += 1\n        return self.time\n\n   \
    \ def __len__(self) -> int:\n        return len(self.__set_value)\n\n    def __str__(self):\n\
    \        return str([self[i] for i in range(self.__N)])\n\n    def __repr__(self):\n\
    \        return f\"{self.__class__.__name__}(A={repr([self[i] for i in range(len(self))])},\
    \ auto_commit={self.auto_commit})\"\n\n    def __iter__(self):\n        for i\
    \ in range(self.__N):\n            yield self[i]\n\n    def __setitem__(self,\
    \ index, value):\n        self.set_value(index, value)\n\n    def __getitem__(self,\
    \ index: int):\n        return self.__set_value[index][-1]\n"
  dependsOn: []
  isVerificationFile: false
  path: Partial_Persistent_List.py
  requiredBy: []
  timestamp: '2025-06-17 00:15:54+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Partial_Persistent_List.py
layout: document
redirect_from:
- /library/Partial_Persistent_List.py
- /library/Partial_Persistent_List.py.html
title: Partial_Persistent_List.py
---
