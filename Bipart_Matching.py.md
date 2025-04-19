---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test_verify/yosupo_library_checker/Graph/Matching_on_Bipartite_Graph.test.py
    title: test_verify/yosupo_library_checker/Graph/Matching_on_Bipartite_Graph.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links:
    - https://snuke.hatenablog.com/entry/2019/05/07/013609
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.13.3/x64/lib/python3.13/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.13.3/x64/lib/python3.13/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# \u53C2\u8003 URL\n# https://snuke.hatenablog.com/entry/2019/05/07/013609\n\
    \nfrom random import shuffle\nclass Bipartite_Matching:\n    __slots__ = (\"__M\"\
    , \"__N\", \"__edges\", \"__size\", \"__matching\")\n\n    def __init__(self,\
    \ M: int, N: int):\n        \"\"\" \u90E8\u96C6\u5408\u306E\u5927\u304D\u3055\u304C\
    \ M, N \u3067\u3042\u308B\u4E8C\u90E8\u30B0\u30E9\u30D5\u3092\u751F\u6210\u3059\
    \u308B.\n\n        Args:\n            M (int): \u90E8\u96C6\u5408 1 \u306E\u5927\
    \u304D\u3055\n            N (int): \u90E8\u96C6\u5408 2 \u306E\u5927\u304D\u3055\
    \n        \"\"\"\n\n        self.__M = M\n        self.__N = N\n        self.__edges:\
    \ list[list[int]] = [[] for _ in range(M)]\n\n    @property\n    def M(self) ->\
    \ int:\n        \"\"\" \u90E8\u96C6\u5408 1 \u306E\u5927\u304D\u3055\u3092\u8FD4\
    \u3059.\n\n        Returns:\n            int: \u90E8\u96C6\u5408 1 \u306E\u5927\
    \u304D\u3055\n        \"\"\"\n\n        return self.__M\n\n    @property\n   \
    \ def N(self) -> int:\n        \"\"\" \u90E8\u96C6\u5408 2 \u306E\u5927\u304D\u3055\
    \u3092\u8FD4\u3059.\n\n        Returns:\n            int: \u90E8\u96C6\u5408 2\
    \ \u306E\u5927\u304D\u3055\n        \"\"\"\n\n        return self.__N\n\n    def\
    \ add_edge(self, a: int, b: int):\n        \"\"\" \u8FBA Aa \u3068\u8FBA Bb \u3092\
    \u7D50\u3076\u7121\u5411\u8FBA\u3092\u8FFD\u52A0\u3059\u308B.\n\n        Args:\n\
    \            a (int): \u90E8\u96C6\u5408 1 \u5074\u306E\u9802\u70B9\u756A\u53F7\
    \n            b (int): \u90E8\u96C6\u5408 2 \u5074\u306E\u9802\u70B9\u756A\u53F7\
    \n        \"\"\"\n\n        assert 0 <= a < self.M\n        assert 0 <= b < self.N\n\
    \n        self.__edges[a].append(b)\n\n    def calculate(self, matching = False):\n\
    \        \"\"\" \u6700\u5927\u30DE\u30C3\u30C1\u30F3\u30B0\u3092\u8A08\u7B97\u3059\
    \u308B (\u7D50\u679C\u306F property \u30E1\u30BD\u30C3\u30C9\u3067\u53C2\u7167\
    \u3059\u308B).\n\n        Args:\n            matching (bool, optional): True \u306B\
    \u3059\u308B\u3068, \u6700\u5927\u30DE\u30C3\u30C1\u30F3\u30B0\u306E\u4E00\u4F8B\
    \u3082\u4E00\u7DD2\u306B\u6C42\u3081\u308B. Defaults to False.\n        \"\"\"\
    \n\n        for a in range(self.M):\n            shuffle(self.__edges[a])\n\n\
    \        edge = self.__edges\n        pre = [-1] * self.M\n        root = [-1]\
    \ * self.M\n        p = [-1] * self.M\n        q = [-1] * self.N\n\n        updated\
    \ = True\n        size = 0\n        while updated:\n            updated = False\n\
    \            S = []\n            index = 0\n\n            for i in range(self.M):\n\
    \                if p[i] == -1:\n                    root[i] = i\n           \
    \         S.append(i)\n\n            while index < len(S):\n                v\
    \ = S[index]\n                index += 1\n\n                if p[root[v]] != -1:\n\
    \                    continue\n\n                for u in edge[v]:\n         \
    \           if q[u] == -1:\n                        while u != -1:\n         \
    \                   q[u] = v\n                            p[v], u = u, p[v]\n\
    \                            v = pre[v]\n                        updated = True\n\
    \                        size += 1\n                        break\n\n        \
    \            u = q[u]\n                    if pre[u] != -1:\n                \
    \        continue\n\n                    pre[u] = v\n                    root[u]\
    \ = root[v]\n                    S.append(u)\n\n            if updated:\n    \
    \            pre = [-1] * self.M\n                root = [-1] * self.M\n\n   \
    \     self.__size = size\n\n        if not matching:\n            self.__matching\
    \ = None\n\n        A = [-1] * self.M\n        B = [-1] * self.N\n\n        for\
    \ i in range(self.M):\n            if p[i] != -1:\n                A[i] = p[i]\n\
    \                B[p[i]] = i\n\n        self.__matching = (A, B)\n\n    @property\n\
    \    def max_matching_size(self) -> int:\n        \"\"\" calculate \u3067\u6C42\
    \u3081\u305F\u6700\u5927\u30DE\u30C3\u30C1\u30F3\u30B0\u306E\u30B5\u30A4\u30BA\
    \u3092\u6C42\u3081\u308B.\n\n        Returns:\n            int: \u6700\u5927\u30DE\
    \u30C3\u30C1\u30F3\u30B0\u306E\u30B5\u30A4\u30BA\n        \"\"\"\n\n        return\
    \ self.__size\n\n    @property\n    def max_matching(self) -> tuple[list[int],\
    \ list[int]]:\n        \"\"\" calculate \u3067\u6C42\u3081\u305F\u6700\u5927\u30DE\
    \u30C3\u30C1\u30F3\u30B0\u306E\u4E00\u4F8B\u3092\u6C42\u3081\u308B.\n\n      \
    \  Returns:\n            tuple[list[int], list[int]]: (A, B)\n               \
    \ A[i] \u304C -1 \u3067\u306F\u306A\u3044\u3068\u304D, \u8FBA (i, A[i]) \u304C\
    \u30DE\u30C3\u30C1\u30F3\u30B0\u3068\u3057\u3066\u63A1\u7528\u3055\u308C\u3066\
    \u3044\u308B. A[i] = -1 \u306E\u3068\u304D\u306F\u30DE\u30C3\u30C1\u30F3\u30B0\
    \u306E\u9802\u70B9\u3068\u3057\u3066\u63A1\u7528\u3055\u308C\u3066\u3044\u306A\
    \u3044.\n                B[j] \u304C -1 \u3067\u306F\u306A\u3044\u3068\u304D,\
    \ \u8FBA (B[j], j) \u304C\u30DE\u30C3\u30C1\u30F3\u30B0\u3068\u3057\u3066\u63A1\
    \u7528\u3055\u308C\u3066\u3044\u308B. B[j] = -1 \u306E\u3068\u304D\u306F\u30DE\
    \u30C3\u30C1\u30F3\u30B0\u306E\u9802\u70B9\u3068\u3057\u3066\u63A1\u7528\u3055\
    \u308C\u3066\u3044\u306A\u3044.\n        \"\"\"\n\n        return self.__matching\n"
  dependsOn: []
  isVerificationFile: false
  path: Bipart_Matching.py
  requiredBy: []
  timestamp: '2025-04-13 21:46:29+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test_verify/yosupo_library_checker/Graph/Matching_on_Bipartite_Graph.test.py
documentation_of: Bipart_Matching.py
layout: document
redirect_from:
- /library/Bipart_Matching.py
- /library/Bipart_Matching.py.html
title: Bipart_Matching.py
---
