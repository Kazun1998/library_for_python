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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.8/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.8/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class Topological_Sort:\n    __slots__=(\"N\",\"__arc\",\"__rev\")\n    def\
    \ __init__(self, N: int):\n        \"\"\" N \u9802\u70B9\u304B\u3089\u306A\u308B\
    \u7A7A\u30B0\u30E9\u30D5\u3092\u7528\u610F\u3059\u308B.\n\n        N: int\n  \
    \      \"\"\"\n        self.N=N\n        self.__arc=[[] for _ in  range(N)]\n\
    \        self.__rev=[[] for _ in range(N)]\n\n    def add_arc(self, source: int,\
    \ target: int):\n        \"\"\" \u6709\u5411\u8FBA source \u2192 taeget \u3092\
    \u8FFD\u52A0\u3059\u308B.\n\n        \"\"\"\n        self.__arc[source].append(target)\n\
    \        self.__rev[target].append(source)\n\n    def sort(self):\n        \"\"\
    \" \u30C8\u30DD\u30ED\u30B8\u30AB\u30EB\u30BD\u30FC\u30C8\u3092\u6C42\u3081\u308B\
    .\n\n        [Ouput]\n        \u5B58\u5728\u3059\u308B \u2192 \u30C8\u30DD\u30ED\
    \u30B8\u30AB\u30EB\u30BD\u30FC\u30C8 (source \u5074\u304C\u30EA\u30B9\u30C8\u306E\
    \u5148\u982D)\n        \u5B58\u5728\u3057\u306A\u3044 \u2192 None\n        \"\"\
    \"\n\n        in_deg=[len(self.__rev[x]) for x in range(self.N)]\n        Q=[x\
    \ for x in range(self.N) if in_deg[x]==0]\n\n        S=[]\n        while Q:\n\
    \            u=Q.pop()\n            S.append(u)\n\n            for v in self.__arc[u]:\n\
    \                in_deg[v]-=1\n                if in_deg[v]==0:\n            \
    \        Q.append(v)\n\n        return S if len(S)==self.N else None\n\n    def\
    \ is_DAG(self):\n        \"\"\" DAG \u304B\u3069\u3046\u304B\u3092\u5224\u5B9A\
    \u3059\u308B.\n        \"\"\"\n        in_deg=[len(self.__rev[x]) for x in range(self.N)]\n\
    \        Q=[x for x in range(self.N) if in_deg[x]==0]\n\n        K=0\n       \
    \ while Q:\n            u=Q.pop()\n            K+=1\n\n            for v in self.__arc[u]:\n\
    \                in_deg[v]-=1\n                if in_deg[v]==0:\n            \
    \        Q.append(v)\n\n        return K==self.N\n"
  dependsOn: []
  isVerificationFile: false
  path: Topological_Sort.py
  requiredBy: []
  timestamp: '2021-09-12 03:03:28+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Topological_Sort.py
layout: document
redirect_from:
- /library/Topological_Sort.py
- /library/Topological_Sort.py.html
title: Topological_Sort.py
---
