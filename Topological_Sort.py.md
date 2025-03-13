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
  code: "class Topological_Sort:\n    __slots__=(\"__arc\", \"__rev\", \"__reflexive\"\
    , \"__is_DAG\", \"__order\")\n\n    def __init__(self, N: int, reflexive: bool\
    \ = False):\n        \"\"\" N \u9802\u70B9\u304B\u3089\u306A\u308B\u6709\u5411\
    \u7A7A\u30B0\u30E9\u30D5\u3092\u751F\u6210\u3059\u308B.\n\n        Args:\n   \
    \         N (int): \u9802\u70B9\u6570\n            reflexive (bool, optional):\
    \ True \u306B\u3059\u308B\u3068, \u81EA\u5DF1\u30EB\u30FC\u30D7\u306E\u8FFD\u52A0\
    \u3092\u8A8D\u3081\u308B. Defaults to False.\n        \"\"\"\n\n        self.__arc=[[]\
    \ for _ in  range(N)]\n        self.__rev=[[] for _ in range(N)]\n        self.__reflexive=reflexive\n\
    \n    @property\n    def N(self):\n        return len(self.__arc)\n\n    @property\n\
    \    def reflexive(self):\n        return self.__reflexive\n\n    def add_arc(self,\
    \ source: int, target: int):\n        \"\"\" source \u304B\u3089 target \u3078\
    \u306E\u5F27\u3092\u8FFD\u52A0\u3059\u308B.\n\n        Args:\n            source\
    \ (int): \u59CB\u70B9\n            target (int): \u7D42\u70B9\n        \"\"\"\n\
    \n        # \u81EA\u5DF1\u30EB\u30FC\u30D7\u3092\u8A8D\u3081\u306A\u3044\u5834\
    \u5408\u306E source == target \u306E\u3068\u304D\u306F\u68C4\u5374\u3059\u308B\
    .\n        if source == target and (not self.reflexive):\n            return\n\
    \n        self.__arc[source].append(target)\n        self.__rev[target].append(source)\n\
    \n    def add_vertex(self) -> int:\n        \"\"\" 1 \u9802\u70B9\u8FFD\u52A0\n\
    \n        Returns:\n            int: \u8FFD\u52A0\u3055\u308C\u305F\u9802\u70B9\
    \u306E\u9802\u70B9\u756A\u53F7\n        \"\"\"\n\n        self.__arc.append([])\n\
    \        self.__rev.append([])\n        return self.N - 1\n\n    def add_arc_multiple(self,\
    \ sources: list[int], targets: list[int]) -> int:\n        \"\"\" \u4EFB\u610F\
    \u306E s in sources, t in targets \u306B\u5BFE\u3057\u3066, s \u304B\u3089 t \u3078\
    \u306E\u5F27\u3092\u4F5C\u6210\u3059\u308B (\u4EEE\u60F3\u7684\u306B 1 \u9802\u70B9\
    \u3092\u8FFD\u52A0\u3059\u308B).\n\n        Args:\n            sources (list[int]):\
    \ \u59CB\u70B9\u306E\u30EA\u30B9\u30C8\n            targets (list[int]): \u7D42\
    \u70B9\u306E\u30EA\u30B9\u30C8\n\n        Returns:\n            int: \u8D85\u9802\
    \u70B9\u3068\u3057\u3066\u8FFD\u52A0\u3055\u308C\u305F\u9802\u70B9\u306E\u756A\
    \u53F7\n        \"\"\"\n\n        # \u65B9\u91DD\n        # (1) \u8D85\u9802\u70B9\
    \ x \u3092\u8FFD\u52A0\u3059\u308B.\n        # (2) \u4EFB\u610F\u306E s in sources\
    \ \u306B\u5BFE\u3057\u3066, \u5F27 sx \u3092\u8FFD\u52A0\u3059\u308B.\n      \
    \  # (3) \u4EFB\u610F\u306E t in targets \u306B\u5BFE\u3057\u3066, \u5F27 xt \u3092\
    \u8FFD\u52A0\u3059\u308B.\n        # \u3053\u306E\u3088\u3046\u306B\u3059\u308B\
    \u3053\u3068\u3067, \u8FFD\u52A0\u3059\u308B\u5F27\u306E\u6570\u3092 |sources|\
    \ x |targets| \u304B\u3089 |sources| + |targets| \u306B\u843D\u3068\u305B\u308B\
    .\n\n        x = self.add_vertex()\n        for s in sources:\n            self.add_arc(s,\
    \ x)\n\n        for t in targets:\n            self.add_arc(x, t)\n\n    def calculate(self):\n\
    \        \"\"\" DAG \u306B\u95A2\u3059\u308B\u8A08\u7B97\u3092\u884C\u3046.\n\
    \        \"\"\"\n\n        in_deg = [len(self.__rev[x]) for x in range(self.N)]\n\
    \        order = []\n        stack = [x for x in range(self.N) if in_deg[x] ==\
    \ 0]\n\n        while stack:\n            x = stack.pop()\n            order.append(x)\n\
    \n            for y in self.__arc[x]:\n                in_deg[y] -= 1\n      \
    \          if in_deg[y] == 0:\n                    stack.append(y)\n\n       \
    \ if len(order) == self.N:\n            self.__is_DAG = True\n            self.__order\
    \ = order\n        else:\n            self.__is_DAG = False\n            self.__order\
    \ = None\n\n    @property\n    def is_DAG(self):\n        return self.__is_DAG\n\
    \n    @property\n    def order(self):\n        return self.__order\n"
  dependsOn: []
  isVerificationFile: false
  path: Topological_Sort.py
  requiredBy: []
  timestamp: '2025-03-14 00:26:13+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Topological_Sort.py
layout: document
redirect_from:
- /library/Topological_Sort.py
- /library/Topological_Sort.py.html
title: Topological_Sort.py
---
