---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test_verify/yosupo_library_checker/Graph/Strongly_Connected_Components-class.test.py
    title: test_verify/yosupo_library_checker/Graph/Strongly_Connected_Components-class.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links:
    - https://atcoder.jp/contests/typical90/submissions/21969418
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.1/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.1/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "\"\"\"Thanks to toyuzuko\nhttps://atcoder.jp/contests/typical90/submissions/21969418\n\
    \"\"\"\n\nclass Strongly_Connected_Components:\n    def __init__(self,N):\n  \
    \      self.N=N\n        self.arc=[[] for _ in range(N)]\n        self.rev=[[]\
    \ for _ in range(N)]\n\n    def add_arc(self,source,target):\n        self.arc[source].append(target)\n\
    \        self.rev[target].append(source)\n\n    def decomposition(self,Mode=0):\n\
    \        \"\"\"\u6709\u5411\u30B0\u30E9\u30D5\u3092\u5F37\u9023\u7D50\u6210\u5206\
    \u306B\u5206\u89E3\n\n        Mode:\n        0(Defalt)---\u5404\u5F37\u9023\u7D50\
    \u6210\u5206\u306E\u9802\u70B9\u306E\u30EA\u30B9\u30C8\n        1        ---\u5404\
    \u9802\u70B9\u304C\u5C5E\u3057\u3066\u3044\u308B\u5F37\u9023\u7D50\u6210\u5206\
    \u306E\u756A\u53F7\n        2        ---0,1\u306E\u4E21\u65B9\n\n        \u203B\
    0 or 2\u3067\u5E30\u3063\u3066\u304F\u308B\u30EA\u30B9\u30C8\u306F\u5404\u5F37\
    \u9023\u7D50\u6210\u5206\u306B\u95A2\u3057\u3066\u30C8\u30DD\u30ED\u30B8\u30AB\
    \u30EB\u30BD\u30FC\u30C8\u3067\u3042\u308B.\n        \"\"\"\n\n        G=[0]*self.N\n\
    \        D=[0]*self.N\n        O=[]\n\n        for v in range(self.N):\n     \
    \       if G[v]: continue\n            S=[~v,v]\n\n            while S:\n    \
    \            v=S.pop()\n                if v>=0:\n                    if G[v]:\
    \ continue\n                    G[v]=-1\n                    for u in self.arc[v]:\n\
    \                        if G[u]: continue\n                        S.append(~u)\n\
    \                        S.append(u)\n                else:\n                \
    \    if D[~v]: continue\n                    D[~v]=1\n                    O.append(~v)\n\
    \n        K=0\n        for v in O[::-1]:\n            if G[v]!=-1: continue\n\n\
    \            S=[v]\n            G[v]=K\n\n            while S:\n             \
    \   w=S.pop()\n                for u in self.rev[w]:\n                    if G[u]!=-1:\
    \ continue\n                    G[u]=K\n                    S.append(u)\n    \
    \        K+=1\n\n        if Mode==0 or Mode==2:\n            R=[[] for _ in range(K)]\n\
    \            for i in range(self.N):\n                R[G[i]].append(i)\n\n  \
    \      if Mode==0:\n            return R\n        elif Mode==1:\n            return\
    \ G\n        else:\n            return R,G\n"
  dependsOn: []
  isVerificationFile: false
  path: Strongly_Connected_Components.py
  requiredBy: []
  timestamp: '2022-11-22 01:17:17+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test_verify/yosupo_library_checker/Graph/Strongly_Connected_Components-class.test.py
documentation_of: Strongly_Connected_Components.py
layout: document
redirect_from:
- /library/Strongly_Connected_Components.py
- /library/Strongly_Connected_Components.py.html
title: Strongly_Connected_Components.py
---
