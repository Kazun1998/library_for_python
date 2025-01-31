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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.13.1/x64/lib/python3.13/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.13.1/x64/lib/python3.13/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class Topological_Sort:\n    __slots__=(\"N\",\"__arc\",\"__rev\", \"__reflexive\"\
    )\n    def __init__(self, N: int, reflexive=False):\n        \"\"\" N \u9802\u70B9\
    \u304B\u3089\u306A\u308B\u7A7A\u30B0\u30E9\u30D5\u3092\u751F\u6210\u3059\u308B\
    .\n\n        N: \u9802\u70B9\u6570\n        reflexive: \u81EA\u5DF1\u30EB\u30FC\
    \u30D7\u306E\u8FFD\u52A0\u3092\u8A8D\u3081\u308B\u304B? (False \u306E\u5834\u5408\
    \u306F\u81EA\u5DF1\u30EB\u30FC\u30D7\u306F\u81EA\u52D5\u7684\u306B\u53D6\u308A\
    \u9664\u304B\u308C\u308B.)\n        \"\"\"\n\n        self.N=N\n        self.__arc=[[]\
    \ for _ in  range(N)]\n        self.__rev=[[] for _ in range(N)]\n        self.__reflexive=reflexive\n\
    \n    def add_arc(self, source: int, target: int):\n        \"\"\" \u6709\u5411\
    \u8FBA source -> target \u3092\u8FFD\u52A0\u3059\u308B.\n\n        source: \u59CB\
    \u70B9\n        target: \u7D42\u70B9\n        \"\"\"\n\n        if source==target\
    \ and (not self.__reflexive):\n            return\n\n        self.__arc[source].append(target)\n\
    \        self.__rev[target].append(source)\n\n    def add_vertex(self):\n    \
    \    res=self.N\n        self.N+=1\n        self.__arc.append([])\n        self.__rev.append([])\n\
    \        return res\n\n    def add_arc_multiple(self, sources, targets):\n   \
    \     v=self.add_vertex()\n        for u in sources:\n            self.add_arc(u,v)\n\
    \n        for w in targets:\n            self.add_arc(v,w)\n\n        return v\n\
    \n    def sort(self):\n        \"\"\" \u30C8\u30DD\u30ED\u30B8\u30AB\u30EB\u30BD\
    \u30FC\u30C8\u3092\u6C42\u3081\u308B\n\n        \u5B58\u5728\u3059\u308B\u306A\
    \u3089\u3070\u30C8\u30DD\u30ED\u30B8\u30AB\u30EB\u30BD\u30FC\u30C8\u3092\u3057\
    \u305F\u30EA\u30B9\u30C8, \u5B58\u5728\u3057\u306A\u3044\u306A\u3089\u3070 None\n\
    \        \"\"\"\n\n        in_deg=[len(self.__rev[x]) for x in range(self.N)]\n\
    \        Q=[x for x in range(self.N) if in_deg[x]==0]\n\n        S=[]\n      \
    \  while Q:\n            u=Q.pop()\n            S.append(u)\n\n            for\
    \ v in self.__arc[u]:\n                in_deg[v]-=1\n                if in_deg[v]==0:\n\
    \                    Q.append(v)\n\n        return S if len(S)==self.N else None\n\
    \n    def is_DAG(self):\n        \"\"\" DAG \u304C\u3069\u3046\u304B\u3092\u5224\
    \u5B9A\u3059\u308B\n\n        DAG \u306A\u3089\u3070 True, \u975E DAG \u306A\u3089\
    \u3070 False\n        \"\"\"\n\n        in_deg=[len(self.__rev[x]) for x in range(self.N)]\n\
    \        Q=[x for x in range(self.N) if in_deg[x]==0]\n\n        K=0\n       \
    \ while Q:\n            u=Q.pop()\n            K+=1\n\n            for v in self.__arc[u]:\n\
    \                in_deg[v]-=1\n                if in_deg[v]==0:\n            \
    \        Q.append(v)\n\n        return K==self.N\n"
  dependsOn: []
  isVerificationFile: false
  path: Topological_Sort.py
  requiredBy: []
  timestamp: '2023-05-03 17:38:58+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Topological_Sort.py
layout: document
redirect_from:
- /library/Topological_Sort.py
- /library/Topological_Sort.py.html
title: Topological_Sort.py
---
