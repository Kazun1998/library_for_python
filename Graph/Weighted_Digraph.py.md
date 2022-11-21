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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class Weigthed_Digraph:\n    \"\"\"\u91CD\u307F[\u4ED8\u304D]\u6709\u5411\
    \u30B0\u30E9\u30D5\u3092\u751F\u6210\u3059\u308B.\n\n    \"\"\"\n    #\u5165\u529B\
    \u5B9A\u7FA9\n    def __init__(self, N=0, allow_multi=False, multi_edge=None,\
    \ initialize=None):\n        \"\"\" \u91CD\u307F[\u4ED8\u304D]\u6709\u5411\u30B0\
    \u30E9\u30D5\u3092\u751F\u6210\u3059\u308B.\n\n        N: \u9802\u70B9\u6570\n\
    \        allow_multi: \u591A\u91CD\u8FBA\u3092\u8A8D\u3081\u308B\u304B?\n    \
    \    multi_edge: \u591A\u91CD\u8FBA\u306B\u304A\u3051\u308B\u91CD\u307F\u306E\u307E\
    \u3068\u3081\u65B9 (\u91CD\u307F\u306B\u95A2\u3059\u308B2\u5909\u6570\u95A2\u6570\
    )\n        initilize: multi_edge \u306E\u5358\u4F4D\u5143\n        \"\"\"\n\n\
    \        self.arc_number=0\n\n        self.allow_multi=allow_multi\n        self.initialize=initialize\n\
    \        self.multi_edge=multi_edge\n\n        self.adjacent_out=[{} for _ in\
    \ range(N)] #\u51FA\u8FD1\u508D(v\u304C\u59CB\u70B9)\n        self.adjacent_in=[{}\
    \ for _ in range(N)] #\u5165\u8FD1\u508D(v\u304C\u7D42\u70B9)\n\n    #\u9802\u70B9\
    \u306E\u8FFD\u52A0\n    def add_vertex(self):\n        \"\"\" \u9802\u70B9\u3092\
    \u8FFD\u52A0\u3059\u308B.\n\n        \"\"\"\n        self.adjacent_out.append({})\n\
    \        self.adjacent_in.append({})\n        return self.order()-1\n\n    def\
    \ add_vertices(self, k):\n        \"\"\" \u9802\u70B9\u3092 k \u500B\u8FFD\u52A0\
    \u3059\u308B.\n\n        k: int\n        \"\"\"\n\n        n=self.order()\n  \
    \      self.adjacent_out.extend([{} for _ in range(k)])\n        self.adjacent_in.extend([{}\
    \ for _ in range(k)])\n        return list(range(n,n+k))\n\n    #\u8FBA\u306E\u8FFD\
    \u52A0(\u66F4\u65B0)\n    def add_arc(self, source, target, weight=1):\n     \
    \   if self.allow_multi:\n            self.arc_number+=1\n            self.adjacent_out[source][target]=self.multi_edge(self.adjacent_out[source].get(target,\
    \ self.initialize), weight)\n            self.adjacent_in[target][source]=self.multi_edge(self.adjacent_in[source].get(target,\
    \ self.initialize), weight)\n        else:\n            if target not in self.adjacent_out[source]:\n\
    \                self.arc_number+=1\n            self.adjacent_out[source][target]=weight\n\
    \            self.adjacent_in[target][source]=weight\n\n    #\u8FBA\u3092\u9664\
    \u304F\n    def remove_arc(self, source, target):\n        if self.arc_exist(source,\
    \ target):\n            self.arc_number-=1\n            del self.adjacent_out[source][target]\n\
    \            del self.adjacent_in[target][source]\n            return True\n \
    \       else:\n            return False\n\n    #\u9802\u70B9\u3092\u9664\u304F\
    \n    def remove_vertex(self,*vertexes):\n        pass\n\n    #Walk\u306E\u8FFD\
    \u52A0\n    def add_walk(self,*walk):\n        pass\n\n    #Cycle\u306E\u8FFD\u52A0\
    \n    def add_cycle(self,*cycle):\n        pass\n\n    #\u9802\u70B9\u306E\u4EA4\
    \u63DB\n    def __vertex_swap(self,p,q):\n        pass\n\n    #\u30B0\u30E9\u30D5\
    \u306B\u8FBA\u304C\u5B58\u5728\u3059\u308B\u304B\u5426\u304B\n    def arc_exist(self,\
    \ source, target):\n        return target in self.adjacent_out[source]\n\n   \
    \ #\u8FD1\u508D\n    def neighbohood(self,v):\n        \"\"\"v\u306E\u51FA\u8FD1\
    \u508D, \u5165\u8FD1\u508D\u3092\u51FA\u529B\u3059\u308B.\n\n        Input:\n\
    \        v:\u9802\u70B9\n\n        Output:\n        (\u51FA\u8FD1\u508D, \u5165\
    \u8FD1\u508D)\n        \"\"\"\n\n        return (set(self.adjacent_out[v].keys()),set(self.adjacent_in[v].keys()))\n\
    \n    #\u51FA\u6B21\u6570\n    def out_degree(self,v):\n        return len(self.adjacent_out[v])\n\
    \n    #\u5165\u6B21\u6570\n    def in_degree(self,v):\n        return len(self.adjacent_in[v])\n\
    \n    #\u6B21\u6570\n    def degree(self,v):\n        return (self.out_degree(v),self.in_degree(v))\n\
    \n    #\u76F8\u5BFE\u6B21\u6570\n    def relative_degree(self, v):\n        return\
    \ self.out_degree(v)-self.in_degree(v)\n\n    #\u9802\u70B9\u6570\n    def vertex_count(self):\n\
    \        \"\"\" \u30B0\u30E9\u30D5\u306E\u9802\u70B9\u6570 (\u4F4D\u6570) \u3092\
    \u6C42\u3081\u308B.\"\"\"\n        return len(self.adjacent_out)\n\n    def order(self):\n\
    \        \"\"\" \u30B0\u30E9\u30D5\u306E\u4F4D\u6570 (\u9802\u70B9\u6570) \u3092\
    \u6C42\u3081\u308B.\"\"\"\n        return len(self.adjacent_out)\n\n    #\u8FBA\
    \u6570\n    def arc_count(self):\n        \"\"\" \u30B0\u30E9\u30D5\u306E\u8FBA\
    \u6570 (\u30B5\u30A4\u30BA) \u3092\u6C42\u3081\u308B.\"\"\"\n        return self.arc_number\n\
    \n    def size(self):\n        \"\"\" \u30B0\u30E9\u30D5\u306E\u30B5\u30A4\u30BA\
    \ (\u8FBA\u6570) \u3092\u6C42\u3081\u308B. \"\"\"\n        return self.arc_number\n\
    \n    #\u9802\u70B9v\u306B\u5230\u9054\u53EF\u80FD\u306A\u9802\u70B9\n    def\
    \ reachable_to(self,v):\n        from collections import deque\n\n        N=self.vertex_count()\n\
    \        adj_in=self.adjacent_in\n\n        T=[0]*N; T[v]=1\n        Q=deque([v])\n\
    \        while Q:\n            x=Q.popleft()\n            for y in adj_in[x]:\n\
    \                if not T[y]:\n                    T[y]=1\n                  \
    \  Q.append(y)\n        return [x for x in range(N) if T[x]]\n\n    #\u9802\u70B9\
    v\u304B\u3089\u5230\u9054\u53EF\u80FD\u306A\u9802\u70B9\n    def reachable_from(self,v):\n\
    \        from collections import deque\n\n        N=self.vertex_count()\n    \
    \    adj_out=self.adjacent_out\n\n        T=[0]*N; T[v]=1\n        Q=deque([v])\n\
    \        while Q:\n            x=Q.popleft()\n            for y in adj_out[x]:\n\
    \                if not T[y]:\n                    T[y]=1\n                  \
    \  Q.append(y)\n        return [x for x in range(N) if T[x]]\n\n    #\u6DF1\u3044\
    \u30B3\u30D4\u30FC\n    def deepcopy(self):\n        from copy import deepcopy\n\
    \        D=Weigthed_Digraph(self.vertex_count())\n        D.arc_number=self.arc_count()\n\
    \        D.adjacent_out=deepcopy(self.adjacent_out)\n        D.adjacent_in=deepcopy(self.adjacent_in)\n\
    \        return D\n#================================================\n#Dijkstra\n\
    def Dijkstra(D, start , goal, with_path=False):\n    \"\"\" Dijksta \u6CD5\u3092\
    \u7528\u3044\u3066, start \u304B\u3089 goal \u307E\u3067\u306E\u8DDD\u96E2\u3092\
    \u6C42\u3081\u308B.\n\n    D: \"\u8FBA\u306E\u91CD\u307F\u304C\u5168\u3066\u975E\
    \u8CA0\" \u306E\u6709\u5411\u30B0\u30E9\u30D5\n    start: \u59CB\u70B9, goal:\
    \ \u7D42\u70B9\n    with_path: \u6700\u77ED\u8DEF\u3082\u542B\u3081\u3066\u51FA\
    \u529B\u3059\u308B\u304B?\n\n    (\u51FA\u529B\u306E\u7D50\u679C)\n    with_path=True\
    \ \u2192 (\u8DDD\u96E2, \u6700\u77ED\u7D4C\u8DEF)\n    with_path=False \u2192\
    \ \u8DDD\u96E2\n    \"\"\"\n\n    from heapq import heappush,heappop\n\n    inf=float(\"\
    inf\")\n    N=D.vertex_count()\n    T=[inf]*N; T[start]=0\n\n    if with_path:\n\
    \        prev=[None]*N\n        prev[start]=start\n\n    Q=[(0, start)]\n\n  \
    \  adj_out=D.adjacent_out\n    flag=0\n    while Q:\n        c,u=heappop(Q)\n\n\
    \        if u==goal:\n            flag=1\n            break\n\n        if T[u]<c:\n\
    \            continue\n\n        E=adj_out[u]\n        for v in E:\n         \
    \   p=T[u]+E[v]\n            if T[v]>p:\n                T[v]=p\n            \
    \    heappush(Q,(p,v))\n\n                if with_path:\n                    prev[v]=u\n\
    \n    if not flag:\n        if with_path:\n            return (inf,[])\n     \
    \   else:\n            return inf\n\n    if with_path:\n        path=[goal]\n\
    \        u=goal\n        while u!=start:\n            u=prev[u]\n            path.append(u)\n\
    \        return (T[goal],path[::-1])\n    else:\n        return T[goal]\n\ndef\
    \ Dijkstra_All(D, start, with_path=False):\n    \"\"\" Dijksta \u6CD5\u3092\u7528\
    \u3044\u3066, \u5358\u4E00\u59CB\u70B9 start \u304B\u3089\u306E\u8DDD\u96E2\u3092\
    \u6C42\u3081\u308B.\n\n    D: \u8FBA\u306E\u91CD\u307F\u304C\u5168\u3066\u975E\
    \u8CA0\u306E\u6709\u5411\u30B0\u30E9\u30D5\n    start: \u59CB\u70B9, to: \u7D42\
    \u70B9\n    with_path: \u6700\u77ED\u8DEF\u3082\u542B\u3081\u3066\u51FA\u529B\u3059\
    \u308B\u304B?\n\n    (\u51FA\u529B\u306E\u7D50\u679C)\n    with_path=True \u2192\
    \ (\u8DDD\u96E2, \u6700\u77ED\u7D4C\u8DEF\u306E\u8FBF\u308B\u969B\u306E\u524D\u306E\
    \u9802\u70B9)\n    with_path=False \u2192 \u8DDD\u96E2\n    \"\"\"\n    from heapq\
    \ import heappush,heappop\n\n    inf=float(\"inf\")\n    N=D.vertex_count()\n\
    \    T=[inf]*N; T[start]=0\n\n    if with_path:\n        prev=[None]*N\n     \
    \   prev[start]=start\n\n    adj_out=D.adjacent_out\n    Q=[(0, start)]\n    while\
    \ Q:\n        c,u=heappop(Q)\n        if T[u]<c:\n            continue\n\n   \
    \     E=adj_out[u]\n        for v in E:\n            if T[v]>c+E[v]:\n       \
    \         T[v]=c+E[v]\n                heappush(Q,(T[v],v))\n\n              \
    \  if with_path:\n                    prev[v]=u\n\n    if with_path:\n       \
    \ return (T,prev)\n    else:\n        return  T\n\n#Bellman_Ford\ndef Bellman_Ford(D,\
    \ start, goal):\n    \"\"\" Bellman_Ford \u6CD5\u3092\u7528\u3044\u3066, start\
    \ \u304B\u3089 goal \u307E\u3067\u306E\u8DDD\u96E2\u3092\u6C42\u3081\u308B (\u8FD4\
    \u308A\u5024\u304C -inf \u306B\u306A\u308B\u5834\u5408\u304C\u3042\u308B).\n\n\
    \    D:\u6709\u5411\u30B0\u30E9\u30D5\n    start: \u59CB\u70B9, goal: \u7D42\u70B9\
    \n    \"\"\"\n\n    inf=float(\"inf\")\n    N=D.vertex_count()\n    T=[inf]*N;\
    \ T[start]=0\n\n    adj_out=D.adjacent_out\n    E=[]\n    for u in range(N):\n\
    \        F=adj_out[u]\n        for v,cost in F.items():\n            E.append((u,v,cost))\n\
    \n    for k in range(N):\n        update=0\n        for u,v,c in E:\n        \
    \    if T[v]>T[u]+c:\n                T[v]=T[u]+c\n                update=1\n\
    \        if update==0:\n            return T[goal]\n\n    for _ in range(N):\n\
    \        update=0\n        for u,v,c in E:\n            if T[v]>T[u]+c:\n    \
    \            T[v]=-inf\n                update=1\n        if update==0:\n    \
    \        break\n    return T[goal]\n\ndef Bellman_Ford_All(D, start):\n    \"\"\
    \" Bellman_Ford \u6CD5\u3092\u7528\u3044\u3066, \u5358\u4E00\u59CB\u70B9 start\
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
    \    update=1\n        if update==0:\n            break\n    return T\n\n#Warshall\u2013\
    Floyd\ndef Warshall_Floyd(D):\n    \"\"\" Warshall\u2013Floyd \u6CD5\u3092\u7528\
    \u3044\u3066, \u5168\u70B9\u9593\u8DDD\u96E2\u3092\u6C42\u3081\u308B.\n\n    D:\
    \ \u91CD\u307F\u4ED8\u304D\u6709\u5411\u30B0\u30E9\u30D5\n    \"\"\"\n\n    def\
    \ three_loop():\n        for u in range(N):\n            Tu=T[u]\n           \
    \ for v in range(N):\n                Tv=T[v]\n                for w in range(N):\n\
    \                    Tv[w]=min(Tv[w],Tv[u]+Tu[w])\n\n    inf=float(\"inf\"); N=D.vertex_count()\n\
    \n    T=[[0]*N for _ in range(N)]\n    adj_out=D.adjacent_out\n    for u in range(N):\n\
    \        Tu=T[u]\n        E=adj_out[u]\n        for v in range(N):\n         \
    \   if v==u:\n                Tu[v]=0\n            elif v in E:\n            \
    \    Tu[v]=E[v]\n            else:\n                Tu[v]=inf\n\n    three_loop()\n\
    \n    flag=1\n    for v in range(N):\n        if T[v][v]<0:\n            T[v][v]=-inf\n\
    \            flag=0\n\n    if flag==1:\n        return T\n    else:\n        three_loop()\n\
    \        return T\n\n#\u5DE1\u56DE\u30BB\u30FC\u30EB\u30B9\u30DE\u30F3\u554F\u984C\
    \u3092\u89E3\u304F.\ndef Traveling_Salesman_Problem(D):\n    \"\"\" \u5DE1\u56DE\
    \u30BB\u30FC\u30EB\u30B9\u30DE\u30F3\u554F\u984C\u3092\u89E3\u304F. \"\"\"\n\n\
    \    N=D.vertex_count()\n\n    inf=float(\"inf\")\n    T=[[inf]*N for _ in range(1<<N)]\n\
    \    T[0][0]=0\n\n    for S in range(1<<N):\n        F=T[S]\n        for v in\
    \ range(N):\n            if S&(1<<v):\n                continue\n\n          \
    \  E=T[S|1<<v]\n            cost=D.adjacent_out[v]\n\n            for w in cost:\n\
    \                if v!=w and E[v]>F[w]+cost[w]:\n                    E[v]=F[w]+cost[w]\n\
    \    return T[-1][0]\n\n#From\u304B\u3089To\u3078\u306E(\u9577\u3055\u304C\u4E01\
    \u5EA6L or L\u4EE5\u4E0B\u306E)Walk\u304C\u5B58\u5728\u3059\u308B\u304B\u5426\u304B\
    \ndef walk_exist(graph,From,To,L,just=False):\n    pass\n\n#\u9006\u30B0\u30E9\
    \u30D5\u306E\u4F5C\u6210\ndef Inverse_Graph(D):\n    \"\"\"\u6709\u5411\u30B0\u30E9\
    \u30D5D\u306E\u5168\u3066\u306E\u8FBA\u306E\u5411\u304D\u3092\u5909\u3048\u305F\
    \u30B0\u30E9\u30D5\u3092\u51FA\u529B\u3059\u308B.\n\n    D:\u6709\u5411\u30B0\u30E9\
    \u30D5\n    \"\"\"\n    from copy import deepcopy\n\n    F=Weigthed_Digraph(D.vertex)\n\
    \n    F.arc_number=D.arc_number\n    F.vertex_number=D.vertex_number\n\n    F.adjacent_in=deepcopy(D.adjacent_out)\n\
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
    \    pass\n#-------------------------------------------------\n#\u7279\u5225\u306A\
    \u30B0\u30E9\u30D5\n#-------------------------------------------------\n#\u5B8C\
    \u5168\u30B0\u30E9\u30D5\u306E\u4F5C\u6210\ndef Complete_Graph(n):\n    pass\n\
    \n#\u5B8C\u51682\u90E8\u30B0\u30E9\u30D5\ndef Complete_Bipartite_Graph(m,n):\n\
    \    pass\n\n#\u30B0\u30E9\u30D5\u4F5C\u6210\ndef Making_Graph(V,E):\n    pass\n\
    \n#\u7A7A\u30B0\u30E9\u30D5\u306E\u4F5C\u6210\ndef Empty_Graph(n):\n    pass\n\
    \n#\u30DA\u30C6\u30EB\u30BB\u30F3\u30B0\u30E9\u30D5\ndef Petersen_Graph(n=5,k=2):\n\
    \    pass\n\n#\u683C\u5B50\u30B0\u30E9\u30D5\ndef Grid_Graph(m,n):\n    pass\n\
    \n#Path\u30B0\u30E9\u30D5\ndef Path_Graph(n):\n    pass\n\n#Cycle\u30B0\u30E9\u30D5\
    \ndef Cycle_Graph(n):\n    pass\n\n#Star\u30B0\u30E9\u30D5\ndef Star_Graph(n):\n\
    \    pass\n\n#Wheel\u30B0\u30E9\u30D5\ndef Wheel_Graph(n):\n    pass\n\n#\u9A0E\
    \u58EB\u5DE1\u56DE\u30B0\u30E9\u30D5\ndef Knight_Tour_Graph(m,n):\n    pass\n\n\
    #\u5B8C\u5168k\u5206\u6728\ndef Complete_Kary_Tree(n,k=2):\n    pass\n\n#---------------------------------------\n\
    #\u30B0\u30E9\u30D5\u306E\u635C\u67FB\n#---------------------------------------\n\
    def Depth_First_Search(D, start, prefunc=None, postfunc=None):\n    \"\"\"\u6DF1\
    \u3055\u512A\u5148\u63A2\u7D22\u3092\u884C\u3046.\n\n    D: \u30B0\u30E9\u30D5\
    \n    prefunc: \u9802\u70B9\u3092Stack\u306B\u5165\u308C\u308B\u6642,\u305D\u306E\
    \u9802\u70B9v\u306B\u5BFE\u3057\u3066\u5B9F\u884C\u3059\u308B\u95A2\u6570,\u547D\
    \u4EE4.\n    postfunc: \u9802\u70B9\u3092Stack\u304B\u3089\u51FA\u3059\u6642,\u305D\
    \u306E\u9802\u70B9v\u306B\u5BFE\u3057\u3066\u5B9F\u884C\u3059\u308B\u95A2\u6570\
    ,\u547D\u4EE4.\n    \"\"\"\n    from collections import deque\n\n    N=D.vertex_count()\n\
    \    T=[0]*N; T[start]=1\n    adj_out=D.adjacent_out\n\n    S=deque([start])\n\
    \n    if prefunc:\n        prefunc(start)\n\n    while S:\n        v=S.pop()\n\
    \        if postfunc:\n            postfunc(v)\n\n        for u in adj_out[v]:\n\
    \            if T[u]==0:\n                T[u]=1\n                S.append(u)\n\
    \                if prefunc:\n                    prefunc(u)\n\ndef Breath_First_Search(D,\
    \ start, prefunc=None, postfunc=None):\n    \"\"\"\u5E45\u512A\u5148\u63A2\u7D22\
    \u3092\u884C\u3046.\n\n    D: \u30B0\u30E9\u30D5\n    prefunc: \u9802\u70B9\u3092\
    Queue\u306B\u5165\u308C\u308B\u6642,\u305D\u306E\u9802\u70B9v\u306B\u5BFE\u3057\
    \u3066\u5B9F\u884C\u3059\u308B\u95A2\u6570,\u547D\u4EE4.\n    postfunc: \u9802\
    \u70B9\u3092Queue\u304B\u3089\u51FA\u3059\u6642,\u305D\u306E\u9802\u70B9v\u306B\
    \u5BFE\u3057\u3066\u5B9F\u884C\u3059\u308B\u95A2\u6570,\u547D\u4EE4.\n    \"\"\
    \"\n    from collections import deque\n\n    N=D.vertex_count()\n    T=[0]*N;\
    \ T[start]=1\n    adj_out=D.adjacent_out\n\n    Q=deque([start])\n\n    if prefunc:\n\
    \        prefunc(start)\n\n    while Q:\n        v=Q.popleft()\n        if postfunc:\n\
    \            postfunc(v)\n\n        for u in adj_out[v]:\n            if T[u]==0:\n\
    \                T[u]=1\n                Q.append(u)\n                if prefunc:\n\
    \                    prefunc(u)\n"
  dependsOn: []
  isVerificationFile: false
  path: Graph/Weighted_Digraph.py
  requiredBy: []
  timestamp: '2022-04-16 12:03:09+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Graph/Weighted_Digraph.py
layout: document
redirect_from:
- /library/Graph/Weighted_Digraph.py
- /library/Graph/Weighted_Digraph.py.html
title: Graph/Weighted_Digraph.py
---
