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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.2/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.2/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from Graph import *\n\ndef Lowlink(G: Graph):\n    \"\"\" G \u306E ord, lowlink\
    \ \u3092\u6C42\u3081\u308B.\n\n    G: Graph\n    \"\"\"\n\n    N = G.order()\n\
    \    tower = []\n    children = [[] for _ in range(N)]\n    ord = [-1] * N\n \
    \   low = [-1] * N\n    def dfs(start, t):\n        ord[start] = low[start] =\
    \ t\n        t += 1\n        tower.append(start)\n        stack = [(start, v,\
    \ j) for v, j in G.partner_with_label_yield(start)]\n        while stack:\n  \
    \          u, v, j = stack.pop()\n            if ord[v] != -1:\n             \
    \   low[u] = min(low[u], ord[v])\n                continue\n\n            ord[v]\
    \ = low[v] = t\n            tower.append(v)\n            children[u].append(v)\n\
    \            t += 1\n            stack.extend([(v, w, k) for w, k in G.partner_with_label_yield(v)\
    \ if k != j])\n        return t\n\n    t = 0\n    for x in range(G.order()):\n\
    \        if ord[x] == -1:\n            t = dfs(x, t)\n\n    for x in reversed(tower):\n\
    \        for y in children[x]:\n            low[x] = min(low[x], low[y])\n\n \
    \   return { 'ord': ord, 'low': low }\n\n# \u6A4B\u5217\u6319\ndef Bridge(G: Graph):\n\
    \    \"\"\" G \u306B\u3042\u308B\u6A4B\u306E id \u3092\u5217\u6319\u3059\u308B\
    .\n\n    G: Graph\n    \"\"\"\n\n    data = Lowlink(G)\n    ord = data['ord'];\
    \ low = data['low']\n    return [t for u, v, t in G.edge_yielder_with_label()\
    \ if (ord[u] < low[v]) or (ord[v] < low[u])]\n\n# \u95A2\u7BC0\u70B9\u306E\u5217\
    \u6319\ndef Articulation_Point(G: Graph):\n    from collections import deque\n\
    \n    N=G.vertex_count()\n    A=[]\n    ord=[-1]*N; low=[-1]*N\n    flag=[0]*N\n\
    \n    parent=[-1]*N\n    children=[[] for _ in range(N)]\n\n    #BFS\u30D1\u30FC\
    \u30C8\n    for v in range(N):\n        if flag[v]:\n            continue\n\n\
    \        k=0\n        S=deque([v])\n        T=[]\n        X=[]\n\n        while\
    \ S:\n            u=S.pop()\n            if flag[u]:\n                continue\n\
    \n            T.append(u)\n            ord[u]=k\n            k+=1\n          \
    \  flag[u]=1\n\n            for w in G.partner_yield(u):\n                if not\
    \ flag[w]:\n                    S.append(w)\n                    parent[w]=u\n\
    \n        for w in T:\n            low[w]=ord[w]\n\n        for w in T[:0:-1]:\n\
    \            children[parent[w]].append(w)\n\n        for w in T[:0:-1]:\n   \
    \         for x in G.partner_yield(w):\n                if w==v or x!=parent[w]:\n\
    \                    low[w]=min(low[w],low[x],ord[x])\n\n        #\u6839\u3067\
    \u306E\u5224\u5B9A\n        if len(children[v])>=2:\n            A.append(v)\n\
    \n        #\u6839\u4EE5\u5916\u306E\u5224\u5B9A\n        for w in T[:0:-1]:\n\
    \            for u in children[w]:\n                if ord[w]<=low[u]:\n     \
    \               A.append(w)\n                    break\n    return A\n\n#\u4E8C\
    \u8FBA\u9023\u7D50\u6210\u5206\u5206\u89E3\ndef Two_Edge_Connected_Components(G:\
    \ Graph):\n    \"\"\"\u30B0\u30E9\u30D5 G \u3092\u4E8C\u8FBA\u9023\u7D50\u6210\
    \u5206\u5206\u89E3 (\u6A4B\u3092\u542B\u307E\u306A\u3044) \u3059\u308B.\n\n  \
    \  [input]\n    G: Graph\n    \"\"\"\n\n    bridges = set(Bridge(G))\n\n    comps\
    \ = []\n    t = 0\n    comp_id = [-1] * G.order()\n    for x in range(G.order()):\n\
    \        if comp_id[x] != -1:\n            continue\n\n        comp_id[x] = t\n\
    \        c = [x]\n        stack = [x]\n        while stack:\n            u = stack.pop()\n\
    \            for v, j in G.partner_with_label_yield(u):\n                if (j\
    \ not in bridges) and (comp_id[v] == -1):\n                    comp_id[v] = t\n\
    \                    c.append(v)\n                    stack.append(v)\n      \
    \  comps.append(c)\n        t += 1\n\n    return { 'group': comp_id, 'comps':\
    \ comps }\n"
  dependsOn: []
  isVerificationFile: false
  path: Graph/Graph/LowLink.py
  requiredBy: []
  timestamp: '2024-03-20 19:52:44+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Graph/Graph/LowLink.py
layout: document
redirect_from:
- /library/Graph/Graph/LowLink.py
- /library/Graph/Graph/LowLink.py.html
title: Graph/Graph/LowLink.py
---
