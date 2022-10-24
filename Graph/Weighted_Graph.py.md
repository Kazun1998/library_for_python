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
  code: "class Weigthed_Graph:\n    #\u5165\u529B\u5B9A\u7FA9\n    def __init__(self,\
    \ N=0, allow_multi=False, initialize=None, multi_edge=None):\n\n        self.edge_number=0\n\
    \n        self.allow_multi=allow_multi\n        self.initialize=initialize\n \
    \       self.multi_edge=multi_edge\n\n        self.adjacent=[{} for _ in range(N)]\n\
    \n    #\u9802\u70B9\u306E\u8FFD\u52A0\n    def add_vertex(self):\n        \"\"\
    \" \u9802\u70B9\u3092\u8FFD\u52A0\u3059\u308B.\n\n        \"\"\"\n        self.adjacent.append({})\n\
    \        return self.order()-1\n\n    def add_vertices(self, k):\n        \"\"\
    \" \u9802\u70B9\u3092 k \u500B\u8FFD\u52A0\u3059\u308B.\n\n        k: int\n  \
    \      \"\"\"\n\n        n=self.order()\n        self.adjacent.extend([{} for\
    \ _ in range(k)])\n        return list(range(n,n+k))\n\n    #\u8FBA\u306E\u8FFD\
    \u52A0\n    def add_edge(self, u, v, weight=1):\n        \"\"\" \u91CD\u3055\u304C\
    \ weight \u306E\u8FBA uv \u3092\u52A0\u3048\u308B. \"\"\"\n\n        if self.allow_multi:\n\
    \            self.edge_number+=1\n            self.adjacent[u][v]=self.multi_edge(self.adjacent[u].get(v,self.initialize),\
    \ weight)\n            self.adjacent[v][u]=self.multi_edge(self.adjacent[v].get(u,self.initialize),\
    \ weight)\n        else:\n            if not self.edge_exist(u,v):\n         \
    \       self.edge_number+=1\n            self.adjacent[u][v]=weight\n        \
    \    self.adjacent[v][u]=weight\n\n    #\u8FBA\u3092\u9664\u304F\n    def remove_edge(self,u,v):\n\
    \        \"\"\" \u8FBA uv \u304C\u5B58\u5728\u3059\u308B\u306A\u3089\u3070\u53D6\
    \u308A\u9664\u304F. \"\"\"\n\n        if self.edge_exist(u,v):\n            del\
    \ self.adjacent[u][v]\n            del self.adjacent[v][u]\n            self.edge_number-=1\n\
    \            return  True\n        else:\n            return False\n\n    #\u9802\
    \u70B9\u3092\u9664\u304F\n\n    #Walk\u306E\u8FFD\u52A0\n\n    #Cycle\u306E\u8FFD\
    \u52A0\n\n    #\u9802\u70B9\u306E\u4EA4\u63DB\n\n    #\u30B0\u30E9\u30D5\u306B\
    \u8FBA\u304C\u5B58\u5728\u3059\u308B\u304B\u5426\u304B\n    def edge_exist(self,\
    \ u, v):\n        \"\"\" \u8FBA uv \u304C\u5B58\u5728\u3059\u308B\u304B\u3069\u3046\
    \u304B\u3092\u5224\u5B9A\u3059\u308B. \"\"\"\n\n        return v in self.adjacent[u]\n\
    \n    #\u8FD1\u508D\n    def neighbohood(self,v):\n        \"\"\" \u9802\u70B9\
    \ v \u306E\u8FD1\u508D\u3092\u8FD4\u3059. \"\"\"\n        return list(self.adjacent[v].keys())\n\
    \n\n    #\u9802\u70B9\u6570\n    def vertex_count(self):\n        \"\"\" \u30B0\
    \u30E9\u30D5\u306E\u9802\u70B9\u6570 (\u4F4D\u6570) \u3092\u51FA\u529B\u3059\u308B\
    . \"\"\"\n        return len(self.adjacent)\n\n    def order(self):\n        \"\
    \"\" \u30B0\u30E9\u30D5\u306E\u4F4D\u6570 (\u9802\u70B9\u6570) \u3092\u51FA\u529B\
    \u3059\u308B. \"\"\"\n        return len(self.adjacent)\n\n    #\u8FBA\u6570\n\
    \    def edge_count(self):\n        \"\"\" \u8FBA\u306E\u672C\u6570 (\u30B5\u30A4\
    \u30BA) \u3092\u51FA\u529B\u3059\u308B.\"\"\"\n\n        return self.edge_number\n\
    \n    def size(self):\n        \"\"\" \u30B5\u30A4\u30BA (\u8FBA\u306E\u672C\u6570\
    ) \u3092\u51FA\u529B\u3059\u308B. \"\"\"\n\n        return self.edge_number\n\n\
    \    #\u9802\u70B9v\u3092\u542B\u3080\u9023\u7D50\u6210\u5206\n\n    #\u8DDD\u96E2\
    \n\n    #\u6700\u77ED\u8DEF\n\n    #\u4F55\u304B\u3057\u3089\u306E\u9802\u70B9\
    \u3092\u9078\u3076.\n\n#Dijkstra\ndef Dijkstra(G, From, To, with_path=False):\n\
    \    \"\"\" Dijksta \u6CD5\u3092\u7528\u3044\u3066, From \u304B\u3089 To \u307E\
    \u3067\u306E\u8DDD\u96E2\u3092\u6C42\u3081\u308B.\n\n    G: \u8FBA\u306E\u91CD\
    \u307F\u304C\u5168\u3066\u975E\u8CA0\u306E\u7121\u5411\u30B0\u30E9\u30D5\n   \
    \ From: \u59CB\u70B9\n    To: \u7D42\u70B9\n    with_path: \u6700\u77ED\u8DEF\u3082\
    \u542B\u3081\u3066\u51FA\u529B\u3059\u308B\u304B?\n\n    (\u51FA\u529B\u306E\u7D50\
    \u679C)\n    with_path=True  \u2192(\u8DDD\u96E2, \u6700\u77ED\u7D4C\u8DEF\u306E\
    \u8FBF\u308B\u969B\u306E\u524D\u306E\u9802\u70B9)\n    with_path=False \u2192\u8DDD\
    \u96E2\n    \"\"\"\n    from heapq import heappush,heappop\n\n    inf=float(\"\
    inf\")\n    N=G.vertex_count()\n    adj=G.adjacent\n\n    T=[inf]*N; T[From]=0\n\
    \n    if with_path:\n        Prev=[-1]*N\n\n    Q=[(0,From)]\n\n    while Q:\n\
    \        c,u=heappop(Q)\n\n        if u==To:\n            break\n\n        if\
    \ T[u]<c:\n            continue\n\n        E=adj[u]\n        for v in E:\n   \
    \         p=T[u]+E[v]\n            if T[v]>p:\n                T[v]=p\n      \
    \          heappush(Q,(p,v))\n\n                if with_path:\n              \
    \      Prev[v]=u\n\n    if T[To]==inf:\n        if with_path:\n            return\
    \ (inf,None)\n        else:\n            return inf\n\n    if with_path:\n   \
    \     path=[To]\n        u=To\n        while (Prev[u]!=None):\n            u=Prev[u]\n\
    \            path.append(u)\n        return (T[To],path[::-1])\n    else:\n  \
    \      return T[To]\n\ndef Dijkstra_All(G, From, with_path=False):\n    \"\"\"\
    \ Dijksta \u6CD5\u3092\u7528\u3044\u3066, From \u304B\u3089\u5404\u9802\u70B9\u307E\
    \u3067\u306E\u8DDD\u96E2\u3092\u6C42\u3081\u308B.\n\n    G: \u8FBA\u306E\u91CD\
    \u307F\u304C\u5168\u3066\u975E\u8CA0\u306E\u7121\u5411\u30B0\u30E9\u30D5\n   \
    \ From: \u59CB\u70B9\n    with_path: \u6700\u77ED\u8DEF\u3082\u542B\u3081\u3066\
    \u51FA\u529B\u3059\u308B\u304B?\n\n    (\u51FA\u529B\u306E\u7D50\u679C)\n    with_path=True\
    \  \u2192 (\u8DDD\u96E2\u306E\u30EA\u30B9\u30C8, \u6700\u77ED\u7D4C\u8DEF\u306E\
    \u8FBF\u308B\u969B\u306E\u524D\u306E\u9802\u70B9)\n    with_path=False \u2192\
    \ \u8DDD\u96E2\u306E\u30EA\u30B9\u30C8\n    \"\"\"\n    from heapq import heappush,heappop\n\
    \n    inf=float(\"inf\")\n    N=G.vertex_count()\n    adj=G.adjacent\n\n    T=[inf]*N;\
    \ T[From]=0\n\n    if with_path:\n        Prev=[-1]*N\n\n    Q=[(0,From)]\n\n\
    \    while Q:\n        c,u=heappop(Q)\n\n        if T[u]<c:\n            continue\n\
    \n        E=adj[u]\n        for v in E:\n            p=T[u]+E[v]\n           \
    \ if T[v]>p:\n                T[v]=p\n                heappush(Q,(p,v))\n\n  \
    \              if with_path:\n                    Prev[v]=u\n\n    if with_path:\n\
    \        return (T,Prev)\n    else:\n        return  T\n\n#Warshall\u2013Floyd\n\
    def Warshall_Floyd(G):\n    \"\"\" Warshall\u2013Floyd \u6CD5\u3092\u7528\u3044\
    \u3066, \u5168\u70B9\u9593\u8DDD\u96E2\u3092\u6C42\u3081\u308B.\n\n    G: \u91CD\
    \u307F\u4ED8\u304D\u7121\u5411\u30B0\u30E9\u30D5\n    \u203B\u8CA0\u306E\u8FBA\
    \u304C\u5B58\u5728\u3059\u308B\u5834\u5408, -inf \u304C\u767A\u751F\u3059\u308B\
    .\n    \"\"\"\n\n    def three_loop():\n        for u in range(N):\n         \
    \   Tu=T[u]\n            for v in range(N):\n                Tv=T[v]\n       \
    \         for w in range(N):\n                    Tv[w]=min(Tv[w],Tv[u]+Tu[w])\n\
    \n    inf=float(\"inf\"); N=G.vertex_count()\n\n    T=[[0]*N for _ in range(N)]\n\
    \    adj=G.adjacent\n    for u in range(N):\n        Tu=T[u]\n        E=adj[u]\n\
    \        for v in range(N):\n            if v==u:\n                Tu[v]=0\n \
    \           elif v in E:\n                Tu[v]=E[v]\n            else:\n    \
    \            Tu[v]=inf\n\n    three_loop()\n\n    flag=1\n    for v in range(N):\n\
    \        if T[v][v]<0:\n            T[v][v]=-inf\n            flag=0\n\n    if\
    \ flag==1:\n        return T\n    else:\n        three_loop()\n        return\
    \ T\n\n#\u5DE1\u56DE\u30BB\u30FC\u30EB\u30B9\u30DE\u30F3\u554F\u984C\u3092\u89E3\
    \u304F.\ndef Traveling_Salesman_Problem(G):\n    N=G.vertex_count()\n\n    inf=float(\"\
    inf\")\n    T=[[inf]*N for _ in range(1<<N)]\n    T[0][0]=0\n\n    for S in range(1<<N):\n\
    \        F=T[S]\n        for v in range(N):\n            if S&(1<<v):\n      \
    \          continue\n\n            E=T[S|1<<v]\n            cost=G.adjacent[v]\n\
    \n            for w,c in cost.items():\n                if v!=w and G.edge_exist(v,w)\
    \ and E[v]>F[w]+c:\n                    E[v]=F[w]+c\n    return T[-1][0]\n\n#\u6728\
    \u306E\u76F4\u5F84\u3092\u6C42\u3081\u308B.\ndef Tree_Diameter(T, Mode=False):\n\
    \    \"\"\" \u91CD\u307F\u4ED8\u304D\u6728 T \u306E\u76F4\u5F84\u3092\u6C42\u3081\
    \u308B.\n\n    T: \u6728\n\n    (\u51FA\u529B\u306E\u7D50\u679C)\n    Mode=True\
    \  \u2192 (\u76F4\u5F84, (\u76F4\u5F84\u3092\u6210\u3059\u7AEF\u70B91, \u76F4\u5F84\
    \u3092\u6210\u3059\u7AEF\u70B92))\n    Mode=False \u2192 \u76F4\u5F84\n    \"\"\
    \"\n    from collections import deque\n\n    def bfs(x):\n        dist=[-1]*N;\
    \ dist[x]=0\n        adj=T.adjacent\n        Q=deque([x])\n\n        while Q:\n\
    \            x=Q.popleft()\n            for y,c in adj[x].items():\n         \
    \       if dist[y]==-1:\n                    dist[y]=dist[x]+c\n             \
    \       Q.append(y)\n\n        z=max(range(N),key=lambda x:dist[x])\n        return\
    \ z,dist[z]\n\n    N=T.vertex_count()\n    u,_=bfs(0)\n    v,d=bfs(u)\n\n    if\
    \ Mode:\n        return (d,(u,v))\n    else:\n        return d\n\n#\u6700\u5C0F\
    \u5168\u57DF\u6728\u3092\u30AF\u30E9\u30B7\u30AB\u30EB\u6CD5\u3067\u6C42\u3081\
    \u308B.\ndef Minimum_Spanning_Tree_by_Kruskal(G,Mode=0):\n    \"\"\" \u30B0\u30E9\
    \u30D5 G \u306E\u6700\u5C0F\u5168\u57DF\u6728\u3092\u30AF\u30E9\u30B7\u30AB\u30EB\
    \u6CD5\u3067\u6C42\u3081\u308B.\n\n    G: \u30B0\u30E9\u30D5\n    Mode=0 \u2192\
    \ \u91CD\u3055\u306E\u307F\n    Mode=1 \u2192 \u91CD\u3055\u3068\u4F7F\u3046\u8FBA\
    \n    Mode=2 \u2192 \u91CD\u3055\u3068\u6700\u5C0F\u5168\u57DF\u6728\n    \"\"\
    \"\n\n    N=G.vertex_count()\n    #Union-Find\u3092\u5B9A\u7FA9\u3059\u308B.\n\
    \    U=list(range(N))\n    R=[1]*N\n\n    def find(x):\n        if U[x]==x:\n\
    \            return x\n\n        A=[x]\n        while x!=U[x]:\n            x=U[x]\n\
    \            A.append(x)\n\n        for a in A:\n            U[a]=x\n        return\
    \ x\n\n    def union(x,y):\n        x=find(x)\n        y=find(y)\n\n        if\
    \ x==y:\n            return\n\n        if R[x]>R[y]:\n            U[y]=x\n   \
    \     else:\n            U[x]=y\n            if R[x]==R[y]:\n                R[y]+=1\n\
    \n    def same(x,y):\n        return find(x)==find(y)\n\n    E=set()\n    adj=G.adjacent\n\
    \    for x in range(N):\n        adj_x=adj[x]\n        for y in adj_x:\n     \
    \       if x<y:\n                E.add((x,y,adj_x[y]))\n    E=sorted(E,key=lambda\
    \ x:x[-1])\n\n    W=0\n    if Mode==1:\n        F=[]\n    elif Mode==2:\n    \
    \    T=Weigthed_Graph(N)\n\n    count=N-1\n    for x,y,w in E:\n        if not\
    \ same(x,y):\n            count-=1\n            union(x,y)\n            W+=w\n\
    \n            if Mode==1:\n                F.append((x,y))\n            elif Mode==2:\n\
    \                T.add_edge(x,y,w)\n\n            if count==0:\n             \
    \   break\n\n    if Mode==0:\n        return W\n    elif Mode==1:\n        return\
    \ W,F\n    else:\n        return W,T\n\ndef Minimum_Spanning_Tree_by_Prim(G,Mode=0):\n\
    \    \"\"\" \u30B0\u30E9\u30D5 G \u306E\u6700\u5C0F\u5168\u57DF\u6728\u3092\u30D7\
    \u30EA\u30E0\u6CD5\u3067\u6C42\u3081\u308B.\n\n    G: \u30B0\u30E9\u30D5\n   \
    \ Mode=0 \u2192 \u91CD\u3055\u306E\u307F\n    Mode=1 \u2192 \u91CD\u3055\u3068\
    \u4F7F\u3046\u8FBA\n    Mode=2 \u2192 \u91CD\u3055\u3068\u6700\u5C0F\u5168\u57DF\
    \u6728\n    \"\"\"\n    from heapq import heapify,heappop,heappush\n    N=G.vertex_count()\n\
    \n    S=[0]*N; S[0]=1\n    H=[(w,0,y) for y,w in G.adjacent[0].items()]\n    heapify(H)\n\
    \n    W=0\n    if Mode==1:\n        F=[]\n    elif Mode==2:\n        T=Weigthed_Graph(N)\n\
    \n    count=N-1\n    while count:\n        w,u,v=heappop(H)\n        if S[u]==S[v]:\n\
    \            continue\n\n        count-=1\n        W+=w\n\n        if Mode==1:\n\
    \            F.append((u,v))\n        else:\n            G.add_edge(u,v,w)\n\n\
    \        if S[v]:\n            u,v=v,u\n\n        S[v]=1\n        V=G.adjacent[v]\n\
    \        for x in V:\n            if not S[x]:\n                heappush(H,(V[x],v,x))\n\
    \n    if Mode==0:\n        return W\n    elif Mode==1:\n        return W,F\n \
    \   else:\n        return W,T\n"
  dependsOn: []
  isVerificationFile: false
  path: Graph/Weighted_Graph.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Graph/Weighted_Graph.py
layout: document
redirect_from:
- /library/Graph/Weighted_Graph.py
- /library/Graph/Weighted_Graph.py.html
title: Graph/Weighted_Graph.py
---
