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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.7/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.7/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class Partial_Persistent_List:\n    def __init__(self, A, manual_mode=False):\n\
    \        from bisect import bisect_left\n\n        self.__N=N=len(A)\n       \
    \ self.mode=manual_mode\n\n        self.__bis=bisect_left\n        self.__set_time=[[-1]\
    \ for _ in range(N)]\n        self.__set_value=[[a] for a in A]\n        self.__time=0\n\
    \n    def get_time(self):\n        return self.__time\n\n    def get_value(self,\
    \ index, time=-1):\n        if time>=0:\n            j=self.__bis(self.__set_time[index],\
    \ time)-1\n        else:\n            j=len(self.__set_time[index])-1\n      \
    \  return self.__set_value[index][j]\n\n    def set_value(self, index, value):\n\
    \        T=self.__set_time[index]\n        V=self.__set_value[index]\n\n     \
    \   if T[-1]==self.__time:\n            V[-1]=value\n        else:\n         \
    \   T.append(self.__time)\n            V.append(value)\n\n        if not self.mode:\n\
    \            self.__time+=1\n\n    def forward_time(self):\n        self.__time+=1\n\
    \n    def __len__(self):\n        return self.__N\n\n    def __str__(self):\n\
    \        return str([self[i] for i in range(self.__N)])\n\n    def __repr__(self):\n\
    \        return repr([self[i] for i in range(self.__N)])\n\n    def __iter__(self):\n\
    \        for i in range(self.__N):\n            yield self[i]\n\n    def __setitem__(self,\
    \ index, value):\n        self.set_value(index, value)\n\n    def __getitem__(self,\
    \ index):\n        return self.__set_value[index][-1]\n"
  dependsOn: []
  isVerificationFile: false
  path: Partial_Persistent_List.py
  requiredBy: []
  timestamp: '2022-10-18 23:48:31+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Partial_Persistent_List.py
layout: document
redirect_from:
- /library/Partial_Persistent_List.py
- /library/Partial_Persistent_List.py.html
title: Partial_Persistent_List.py
---