---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links:
    - https://snuke.hatenablog.com/entry/2019/05/07/013609
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.8/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.8/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# Thank you Snuke !!\n# https://snuke.hatenablog.com/entry/2019/05/07/013609\n\
    \nclass Bipartite_Matching:\n    def __init__(self,M,N):\n        \"\"\" \u30B5\
    \u30A4\u30BA\u304C M,N \u304B\u3089\u306A\u308B\u4E8C\u90E8\u7A7A\u30B0\u30E9\u30D5\
    \u3092\u4F5C\u6210\u3059\u308B.\n        \"\"\"\n        self.M=M; self.N=N\n\
    \        self.edge=[[] for _ in range(M)]\n\n    def add_edge(self, a, b):\n \
    \       \"\"\" \u8FBA Aa Bb \u3092\u52A0\u3048\u308B.\n\n        \"\"\"\n    \
    \    assert 0<=a<self.M and 0<=b<self.N\n        self.edge[a].append(b)\n\n  \
    \  def max_matching(self, mode):\n        M=self.M; N=self.N; edge=self.edge\n\
    \        pre=[-1]*M; root=[-1]*M\n        p=[-1]*M; q=[-1]*N\n\n        upd=True\n\
    \        size=0\n        while upd:\n            upd=False\n            S=[]\n\
    \            Index=0\n\n            for i in range(M):\n                if p[i]==-1:\n\
    \                    root[i]=i\n                    S.append(i)\n\n          \
    \  while Index<len(S):\n                v=S[Index]\n                Index+=1\n\
    \n                if p[root[v]]!=-1:\n                    continue\n\n       \
    \         for u in edge[v]:\n                    if q[u]==-1:\n              \
    \          while u!=-1:\n                            q[u]=v\n                \
    \            p[v],u=u,p[v]\n                            v=pre[v]\n           \
    \             upd=True\n                        size+=1\n                    \
    \    break\n\n                    u=q[u]\n                    if pre[u]!=-1:\n\
    \                        continue\n\n                    pre[u]=v\n          \
    \          root[u]=root[v]\n                    S.append(u)\n\n            if\
    \ upd:\n                pre=[-1]*M\n                root=[-1]*M\n\n        if\
    \ mode==0:\n            return size\n        else:\n            A=[-1]*M; B=[-1]*N\n\
    \            for i in range(M):\n                if p[i]!=-1:\n              \
    \      A[i]=p[i]\n                    B[p[i]]=i\n            return size,(A,B)\n"
  dependsOn: []
  isVerificationFile: false
  path: Bipart_Matching.py
  requiredBy: []
  timestamp: '2022-01-07 17:52:59+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Bipart_Matching.py
layout: document
redirect_from:
- /library/Bipart_Matching.py
- /library/Bipart_Matching.py.html
title: Bipart_Matching.py
---
