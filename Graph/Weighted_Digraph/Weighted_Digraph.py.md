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
  code: "class Weigthed_Digraph:\n    \"\"\"\u91CD\u307F[\u4ED8\u304D]\u6709\u5411\
    \u30B0\u30E9\u30D5\u3092\u751F\u6210\u3059\u308B.\n\n    \"\"\"\n    #\u5165\u529B\
    \u5B9A\u7FA9\n    def __init__(self, N = 0, arc_offset = 0):\n        \"\"\" \u91CD\
    \u307F[\u4ED8\u304D]\u6709\u5411\u30B0\u30E9\u30D5\u3092\u751F\u6210\u3059\u308B\
    .\n\n        N: \u9802\u70B9\u6570\n        \"\"\"\n\n        self.adjacent_out\
    \ = [[] for _ in range(N)] #\u51FA\u8FD1\u508D (v \u304C\u59CB\u70B9)\n      \
    \  self.adjacent_in = [[] for _ in range(N)] #\u5165\u8FD1\u508D (v \u304C\u7D42\
    \u70B9)\n        self.arc_offset = arc_offset\n        self.arc_count = 0\n\n\
    \    #\u9802\u70B9\u306E\u8FFD\u52A0\n    def add_vertex(self):\n        \"\"\"\
    \ \u9802\u70B9\u3092\u8FFD\u52A0\u3059\u308B.\n\n        \"\"\"\n        self.adjacent_out.append([])\n\
    \        self.adjacent_in.append([])\n        return self.order() - 1\n\n    def\
    \ add_vertices(self, k):\n        \"\"\" \u9802\u70B9\u3092 k \u500B\u8FFD\u52A0\
    \u3059\u308B.\n\n        k: int\n        \"\"\"\n\n        n = self.order()\n\
    \        self.adjacent_out.extend([[] for _ in range(k)])\n        self.adjacent_in.extend([[]\
    \ for _ in range(k)])\n        return list(range(n, n + k))\n\n    #\u8FBA\u306E\
    \u8FFD\u52A0\n    def add_arc(self, source, target, weight = 1):\n        id =\
    \ self.arc_count + self.arc_offset\n        self.adjacent_out[source].append((target,\
    \ weight, id))\n        self.adjacent_in[target].append((source, weight, id))\n\
    \        self.arc_count += 1\n        return id\n\n    #\u8FD1\u508D\n\n    #\u51FA\
    \u6B21\u6570\n    def out_degree(self, v):\n        return len(self.adjacent_out[v])\n\
    \n    #\u5165\u6B21\u6570\n    def in_degree(self,v):\n        return len(self.adjacent_in[v])\n\
    \n    #\u6B21\u6570\n    def degree(self,v):\n        return (len(self.adjacent_out[v]),\
    \ len(self.adjacent_in[v]))\n\n    #\u76F8\u5BFE\u6B21\u6570\n    def relative_degree(self,\
    \ v):\n        return len(self.adjacent_out[v]) - len(self.adjacent_in[v])\n\n\
    \    #\u9802\u70B9\u6570\n    def vertex_count(self):\n        \"\"\" \u30B0\u30E9\
    \u30D5\u306E\u9802\u70B9\u6570 (\u4F4D\u6570) \u3092\u6C42\u3081\u308B.\"\"\"\n\
    \        return len(self.adjacent_out)\n\n    def order(self):\n        \"\"\"\
    \ \u30B0\u30E9\u30D5\u306E\u4F4D\u6570 (\u9802\u70B9\u6570) \u3092\u6C42\u3081\
    \u308B.\"\"\"\n        return len(self.adjacent_out)\n\n    #\u8FBA\u6570\n  \
    \  def arc_count(self):\n        \"\"\" \u30B0\u30E9\u30D5\u306E\u8FBA\u6570 (\u30B5\
    \u30A4\u30BA) \u3092\u6C42\u3081\u308B.\"\"\"\n        return self.arc_count\n\
    \n    def size(self):\n        \"\"\" \u30B0\u30E9\u30D5\u306E\u30B5\u30A4\u30BA\
    \ (\u8FBA\u6570) \u3092\u6C42\u3081\u308B. \"\"\"\n        return self.arc_count\n\
    \n#================================================\n#Dijkstra\ndef Dijkstra_All(D,\
    \ start, with_path=False):\n    \"\"\" Dijksta \u6CD5\u3092\u7528\u3044\u3066\
    , \u5358\u4E00\u59CB\u70B9 start \u304B\u3089\u306E\u8DDD\u96E2\u3092\u6C42\u3081\
    \u308B.\n\n    D: \u8FBA\u306E\u91CD\u307F\u304C\u5168\u3066\u975E\u8CA0\u306E\
    \u6709\u5411\u30B0\u30E9\u30D5\n    start: \u59CB\u70B9, to: \u7D42\u70B9\n  \
    \  with_path: \u6700\u77ED\u8DEF\u3082\u542B\u3081\u3066\u51FA\u529B\u3059\u308B\
    \u304B?\n\n    (\u51FA\u529B\u306E\u7D50\u679C)\n    with_path=True \u2192 (\u8DDD\
    \u96E2, \u6700\u77ED\u7D4C\u8DEF\u306E\u8FBF\u308B\u969B\u306E\u524D\u306E\u9802\
    \u70B9)\n    with_path=False \u2192 \u8DDD\u96E2\n    \"\"\"\n    from heapq import\
    \ heappush,heappop\n\n    inf=float(\"inf\")\n    N=D.vertex_count()\n    T=[inf]*N;\
    \ T[start]=0\n\n    if with_path:\n        prev=[None]*N\n        prev[start]=start\n\
    \n    adj_out=D.adjacent_out\n    Q=[(0, start)]\n    while Q:\n        c,u=heappop(Q)\n\
    \        if T[u]<c:\n            continue\n\n        E=adj_out[u]\n        for\
    \ v in E:\n            if T[v]>c+E[v]:\n                T[v]=c+E[v]\n        \
    \        heappush(Q,(T[v],v))\n\n                if with_path:\n             \
    \       prev[v]=u\n\n    if with_path:\n        return (T,prev)\n    else:\n \
    \       return  T\n\n#Bellman_Ford\ndef Bellman_Ford_All(D, start):\n    \"\"\"\
    \ Bellman_Ford \u6CD5\u3092\u7528\u3044\u3066, \u5358\u4E00\u59CB\u70B9 start\
    \ \u304B\u3089\u306E\u8DDD\u96E2\u3092\u6C42\u3081\u308B (\u8FD4\u308A\u5024\u304C\
    \ -inf \u306B\u306A\u308B\u5834\u5408\u304C\u3042\u308B).\n\n    D: \u6709\u5411\
    \u30B0\u30E9\u30D5\n    start: \u59CB\u70B9\n    \"\"\"\n\n    inf=float(\"inf\"\
    )\n    N=D.vertex_count()\n    T=[inf]*N; T[start]=0\n\n    adj_out=D.adjacent_out\n\
    \    E=[]\n    for u in range(N):\n        F=adj_out[u]\n        for v,cost in\
    \ F.items():\n            E.append((u,v,cost))\n\n    for k in range(N):\n   \
    \     update=0\n        for u,v,c in E:\n            if T[v]>T[u]+c:\n       \
    \         T[v]=T[u]+c\n                update=1\n        if update==0:\n     \
    \       return T\n\n    for _ in range(N):\n        update=0\n        for u,v,c\
    \ in E:\n            if T[v]>T[u]+c:\n                T[v]=-inf\n            \
    \    update=1\n        if update==0:\n            break\n    return T\n\n#From\u304B\
    \u3089To\u3078\u306E(\u9577\u3055\u304C\u4E01\u5EA6L or L\u4EE5\u4E0B\u306E)Walk\u304C\
    \u5B58\u5728\u3059\u308B\u304B\u5426\u304B\ndef walk_exist(graph,From,To,L,just=False):\n\
    \    pass\n\n#\u9006\u30B0\u30E9\u30D5\u306E\u4F5C\u6210\ndef Inverse_Graph(D):\n\
    \    \"\"\"\u6709\u5411\u30B0\u30E9\u30D5D\u306E\u5168\u3066\u306E\u8FBA\u306E\
    \u5411\u304D\u3092\u5909\u3048\u305F\u30B0\u30E9\u30D5\u3092\u51FA\u529B\u3059\
    \u308B.\n\n    D:\u6709\u5411\u30B0\u30E9\u30D5\n    \"\"\"\n    from copy import\
    \ deepcopy\n\n    F=Weigthed_Digraph(D.vertex)\n\n    F.arc_number=D.arc_number\n\
    \    F.vertex_number=D.vertex_number\n\n    F.adjacent_in=deepcopy(D.adjacent_out)\n\
    \    F.adjacent_out=deepcopy(D.adjacent_in)\n    return F\n\n#\u88DC\u30B0\u30E9\
    \u30D5\u306E\u4F5C\u6210\ndef Complement_Graph(G):\n    pass\n\n#n\u9802\u70B9\
    \u306E\u30E9\u30F3\u30C0\u30E0\u30B0\u30E9\u30D5\ndef Random_Graph(n,p=0.5,seed=None):\n\
    \    pass\n\n#\u9023\u7D50\u30B0\u30E9\u30D5?\ndef Is_Connected(G):\n    pass\n\
    \n#Topologycal Sort\ndef Topological_Sort(D):\n    from collections import deque\n\
    \n    N=D.vertex_count()\n    X=[D.in_degree(x) for x in range(N)]\n    Q=deque([v\
    \ for v in range(N) if X[v]==0])\n\n    adj_out=D.adjacent_out\n    S=[]\n   \
    \ while Q:\n        u=Q.pop()\n        S.append(u)\n        for v in adj_out[u]:\n\
    \            X[v]-=1\n            if X[v]==0:\n                Q.append(v)\n\n\
    \    if len(S)==N:\n        return S\n    else:\n        return None\n\n#DAG?\n\
    def Is_Directed_Acyclic_Graph(D):\n    from collections import deque\n\n    N=D.vertex_count()\n\
    \    X=[D.in_degree(x) for x in range(N)]\n    Q=deque([v for v in range(N) if\
    \ X[v]==0])\n\n    S=0\n    while Q:\n        u=Q.pop()\n        S+=1\n      \
    \  for v in D.adjacent_out[u]:\n            X[v]-=1\n            if X[v]==0:\n\
    \                Q.append(v)\n\n    return S==N\n\n#Cycle\u3092\u7E2E\u7D04\n\
    def Cycle_Reduction(D):\n    pass\n\n#\u5F37\u9023\u7D50\u6210\u5206\u306B\u5206\
    \u89E3\ndef Strongly_Connected_Component_Decomposition(D,Mode=0):\n    \"\"\"\u6709\
    \u5411\u30B0\u30E9\u30D5D\u3092\u5F37\u9023\u7D50\u6210\u5206\u306B\u5206\u89E3\
    \n\n    Mode:\n    0(Defalt)---\u5404\u5F37\u9023\u7D50\u6210\u5206\u306E\u9802\
    \u70B9\u306E\u30EA\u30B9\u30C8\n    1        ---\u5404\u9802\u70B9\u304C\u5C5E\
    \u3057\u3066\u3044\u308B\u5F37\u9023\u7D50\u6210\u5206\u306E\u756A\u53F7\n   \
    \ 2        ---0,1\u306E\u4E21\u65B9\n\n    \u203B0\u3067\u5E30\u3063\u3066\u304F\
    \u308B\u30EA\u30B9\u30C8\u306F\u5404\u5F37\u9023\u7D50\u6210\u5206\u306B\u95A2\
    \u3057\u3066\u30C8\u30DD\u30ED\u30B8\u30AB\u30EB\u30BD\u30FC\u30C8\u3067\u3042\
    \u308B.\n    \"\"\"\n    N=D.vertex_count()\n    Group=[0]*N\n    Order=[]\n \
    \   adj_out=D.adjacent_out; adj_in=D.adjacent_in\n\n    for v in range(N):\n \
    \       if Group[v]==-1:\n            continue\n\n        S=[v]\n        Group[v]=-1\n\
    \n        while S:\n            u=S.pop()\n            for w in adj_out[u]:\n\
    \                if Group[w]:\n                    continue\n\n              \
    \  Group[w]=-1\n                S.append(u)\n                S.append(w)\n   \
    \             break\n            else:\n                Order.append(u)\n\n  \
    \  k=0\n    for v in Order[::-1]:\n        if Group[v]!=-1:\n            continue\n\
    \n        S=[v]\n        Group[v]=k\n\n        while S:\n            u=S.pop()\n\
    \            for w in adj_in[u]:\n                if Group[w]!=-1:\n         \
    \           continue\n\n                Group[w]=k\n                S.append(w)\n\
    \        k+=1\n\n    if Mode==0 or Mode==2:\n        T=[[] for _ in range(k)]\n\
    \        for v in range(N):\n            T[Group[v]].append(v)\n\n    if Mode==0:\n\
    \        return T\n    elif Mode==1:\n        return Group\n    else:\n      \
    \  return (Group,T)\n\n#\u5F37\u9023\u7D50\u6210\u5206\u306E\u4EE3\u8868\u5143\
    \ndef Strongly_Connected_Component_Representative(D):\n    X=Strongly_Connected_Component_Decomposition(D)\n\
    \    return [C[0] for C in X]\n\n#\u5F37\u9023\u7D50\u6210\u5206\u306E\u500B\u6570\
    \ndef Strongly_Connected_Component_Number(D):\n    \"\"\"\u6709\u5411\u30B0\u30E9\
    \u30D5D\u306E\u5F37\u9023\u7D50\u6210\u5206\u306E\u500B\u6570\n\n    \"\"\"\n\
    \    return len(Strongly_Connected_Component_Decomposition(D))\n\n#Cycle\u304C\
    \u5B58\u5728\u3059\u308B?\ndef Is_Exist_Cycle(D):\n    return not Is_Directed_Acyclic_Graph(D)\n\
    \n#2\u90E8\u30B0\u30E9\u30D5?\ndef Is_Bipartite_Graph(G):\n    pass\n\n#2\u90E8\
    \u30B0\u30E9\u30D5\u306E\u90E8\u96C6\u5408\u306B\u5206\u5272\ndef Bipartite_Separate(G):\n\
    \    pass\n\n#\u30AA\u30A4\u30E9\u30FC\u30B0\u30E9\u30D5?\ndef Is_Eulerian_Graph(G):\n\
    \    pass\n\n#\u7D14\u30AA\u30A4\u30E9\u30FC\u30B0\u30E9\u30D5?\ndef Is_Semi_Eulerian_Graph(G):\n\
    \    pass\n\n#Euler\u9053\u3092\u898B\u3064\u3051\u308B\ndef Find_Eulerian_Trail(G):\n\
    \    pass\n\n#Euler\u9589\u8DEF\u3092\u898B\u3064\u3051\u308B\ndef Find_Eulerian_Cycle(G):\n\
    \    pass\n\n#\u30CF\u30DF\u30EB\u30C8\u30F3\u30B0\u30E9\u30D5?\ndef Is_Hamiltonian_Graph(G):\n\
    \    pass\n\n#\u30CF\u30DF\u30EB\u30C8\u30F3\u3092\u63A2\u3059.\ndef Find_Hamiltonian_Graph(G):\n\
    \    pass\n"
  dependsOn: []
  isVerificationFile: false
  path: Graph/Weighted_Digraph/Weighted_Digraph.py
  requiredBy: []
  timestamp: '2024-02-25 12:52:08+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Graph/Weighted_Digraph/Weighted_Digraph.py
layout: document
redirect_from:
- /library/Graph/Weighted_Digraph/Weighted_Digraph.py
- /library/Graph/Weighted_Digraph/Weighted_Digraph.py.html
title: Graph/Weighted_Digraph/Weighted_Digraph.py
---
