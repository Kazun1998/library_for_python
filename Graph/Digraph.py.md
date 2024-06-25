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
    - https://judge.yosupo.jp/submission/23992
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.4/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.4/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class Digraph:\n    \"\"\"\u91CD\u307F[\u306A\u3057]\u6709\u5411\u30B0\u30E9\
    \u30D5\u3092\u751F\u6210\u3059\u308B.\n\n    \"\"\"\n\n    #\u5165\u529B\u5B9A\
    \u7FA9\n    def __init__(self, N=0):\n        \"\"\" N \u9802\u70B9\u306E\u7A7A\
    \u30B0\u30E9\u30D5\u3092\u751F\u6210\u3059\u308B. \"\"\"\n\n\n        self.arc_number=0\n\
    \        self.adjacent_out=[set() for v in range(N)]#\u51FA\u8FD1\u508D(v\u304C\
    \u59CB\u70B9)\n        self.adjacent_in=[set() for v in range(N)] #\u5165\u8FD1\
    \u508D(v\u304C\u7D42\u70B9)\n\n    #\u9802\u70B9\u306E\u8FFD\u52A0\n    def add_vertex(self):\n\
    \        \"\"\" \u9802\u70B9\u3092\u8FFD\u52A0\u3059\u308B.\n\n        \"\"\"\n\
    \        self.adjacent_out.append(set())\n        self.adjacent_in.append(set())\n\
    \        return self.order()-1\n\n    def add_vertices(self, k=1):\n        \"\
    \"\" \u9802\u70B9\u3092 k \u500B\u8FFD\u52A0\u3059\u308B.\n\n        k: int\n\
    \        \"\"\"\n        n=self.order()\n        self.adjacent_out.extend([set()\
    \ for _ in range(k)])\n        self.adjacent_in.extend([set() for _ in range(k)])\n\
    \        return list(range(n,n+k))\n\n    #\u8FBA\u306E\u8FFD\u52A0\n    def add_arc(self,\
    \ source, target, mode=0):\n        if target not in self.adjacent_out[source]:\n\
    \            self.adjacent_out[source].add(target)\n            self.adjacent_in[target].add(source)\n\
    \            self.arc_number+=1\n            if mode:\n                return\
    \ self.arc_number-1\n        else:\n            if mode:\n                return\
    \ -1\n    #\u8FBA\u3092\u9664\u304F\n    def remove_arc(self, source, target):\n\
    \        if target in self.adjacent_out[source]:\n            self.adjacent_out[source].discard(target)\n\
    \            self.adjacent_in[target].discard(source)\n            self.arc_number-=1\n\
    \n    def reset_vertex(self, u):\n        \"\"\" \u9802\u70B9 u \u306B\u63A5\u7D9A\
    \u3057\u3066\u3044\u308B\u8FBA\u3092\u5168\u3066\u6D88\u3059.\"\"\"\n\n      \
    \  X=self.adjacent_out[u].copy()\n        for v in X:\n            self.remove_arc(u,v)\n\
    \n        X=self.adjacent_in[u].copy()\n        for w in X:\n            self.remove_arc(w,u)\n\
    \n\n    #Walk\u306E\u8FFD\u52A0\n    def add_walk(self,*walk):\n        \"\"\"\
    \ \u6709\u5411\u6B69\u9053 walk=(w[0], ..., w[n-1]) \u3092\u8FFD\u52A0\u3059\u308B\
    . \"\"\"\n\n        N=len(walk)\n        for k in range(N-1):\n            self.add_arc(walk[k],walk[k+1])\n\
    \n    #Cycle\u306E\u8FFD\u52A0\n    def add_cycle(self,*cycle):\n        \"\"\"\
    \ \u6709\u5411\u30B5\u30A4\u30AF\u30EB cycle=(c[0] ..., c[n-1]) \u3092\u8FFD\u52A0\
    \u3059\u308B. \"\"\"\n\n        self.add_walk(*cycle)\n        self.add_arc(cycle[-1],cycle[0])\n\
    \n    #\u30B0\u30E9\u30D5\u306B\u8FBA\u304C\u5B58\u5728\u3059\u308B\u304B\u5426\
    \u304B\n    def arc_exist(self, u, v):\n        \"\"\" \u6709\u5411\u8FBA u ->\
    \ v \u306F\u5B58\u5728\u3059\u308B\u304B? \"\"\"\n        return (v in self.adjacent_out[u])\n\
    \n    #\u8FD1\u508D\n    def neighbohood(self,v):\n        \"\"\"v\u306E\u51FA\
    \u8FD1\u508D, \u5165\u8FD1\u508D\u3092\u51FA\u529B\u3059\u308B.\n\n        Input:\n\
    \        v:\u9802\u70B9\n\n        Output:\n        (\u51FA\u8FD1\u508D, \u5165\
    \u8FD1\u508D)\n        \"\"\"\n        return (self.adjacent_out[v],self.adjacent_in[v])\n\
    \n    #\u51FA\u6B21\u6570\n    def out_degree(self,v):\n        return len(self.adjacent_out[v])\n\
    \n    #\u5165\u6B21\u6570\n    def in_degree(self,v):\n        return len(self.adjacent_in[v])\n\
    \n    #\u6B21\u6570\n    def degree(self,v):\n        return (self.out_degree(v),self.in_degree(v))\n\
    \n    #\u76F8\u5BFE\u6B21\u6570\n    def relative_degree(self,v):\n        return\
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
    \ reachable_to(self,v):\n        \"\"\" \u9802\u70B9 v \u306B\u5230\u9054\u53EF\
    \u80FD\u306A\u9802\u70B9\u3092\u6C42\u3081\u308B. \"\"\"\n        from collections\
    \ import deque\n\n        N=self.vertex_count()\n        T=[0]*N; T[v]=1\n   \
    \     Q=deque([v])\n        while Q:\n            x=Q.pop()\n            for y\
    \ in self.adjacent_in[x]:\n                if not T[y]:\n                    T[y]=1\n\
    \                    Q.append(y)\n        return [x for x in range(N) if T[x]]\n\
    \n    #\u9802\u70B9v\u304B\u3089\u5230\u9054\u53EF\u80FD\u306A\u9802\u70B9\n \
    \   def reachable_from(self,v):\n        \"\"\" \u9802\u70B9 v \u3078\u5230\u9054\
    \u53EF\u80FD\u306A\u9802\u70B9\u3092\u6C42\u3081\u308B. \"\"\"\n        from collections\
    \ import deque\n\n        N=self.vertex_count()\n        T=[0]*N; T[v]=1\n   \
    \     Q=deque([v])\n        while Q:\n            x=Q.pop()\n            for y\
    \ in self.adjacent_out[x]:\n                if not T[y]:\n                   \
    \ T[y]=1\n                    Q.append(y)\n        return [x for x in range(N)\
    \ if T[x]]\n\n    #\u9802\u70B9 u,v \u306E\u8DDD\u96E2\u3092\u6C42\u3081\u308B\
    .\n    def distance(self,u,v):\n        if u==v:\n            return 0\n\n   \
    \     from collections import deque\n        inf=float(\"inf\")\n        N=self.vertex_count()\n\
    \        adj_out=self.adjacent_out\n        T=[inf]*N; T[u]=0\n\n        Q=deque([u])\n\
    \        while Q:\n            w=Q.popleft()\n            for x in adj_out[w]:\n\
    \                if T[x]==inf:\n                    T[x]=T[w]+1\n            \
    \        Q.append(x)\n                    if x==v:\n                        return\
    \ T[x]\n        return inf\n\n    #\u3042\u308B1\u70B9\u304B\u3089\u306E\u8DDD\
    \u96E2\n    def distance_all(self,u):\n        \"\"\" \u9802\u70B9 u \u304B\u3089\
    \u306E\u8DDD\u96E2\u3092\u6C42\u3081\u308B.\"\"\"\n\n        from collections\
    \ import deque\n        inf=float(\"inf\")\n        adj_out=self.adjacent_out\n\
    \        T=[inf]*self.vertex_count(); T[u]=0\n\n        Q=deque([u])\n       \
    \ while Q:\n            w=Q.popleft()\n            for x in adj_out[w]:\n    \
    \            if T[x]==inf:\n                    T[x]=T[w]+1\n                \
    \    Q.append(x)\n        return T\n\n    def shortest_path(self,u,v, dist=False):\n\
    \        \"\"\" u \u304B\u3089 v \u3078\u306E\u6700\u77ED\u8DEF\u3092\u6C42\u3081\
    \u308B (\u5B58\u5728\u3057\u306A\u3044\u5834\u5408\u306F None).\n\n        dist:\
    \ False \u2192 shortest_path \u306E\u307F, True \u2192 (dist, shortest_path)\"\
    \"\"\n\n        if u==v:\n            if dist:\n                return (0,[u])\n\
    \            else:\n                return [u]\n\n        from collections import\
    \ deque\n        inf=float(\"inf\")\n\n        adj_in=self.adjacent_in\n     \
    \   T=[-1]*self.vertex_count()\n\n        Q=deque([v]); T[v]=v\n        while\
    \ Q:\n            w=Q.popleft()\n            for x in adj_in[w]:\n           \
    \     if T[x]==-1:\n                    T[x]=w\n                    Q.append(x)\n\
    \                    if x==u:\n                        P=[u]\n               \
    \         a=u\n                        while a!=v:\n                         \
    \   a=T[a]\n                            P.append(a)\n                        if\
    \ dist:\n                            return (len(P)-1,P)\n                   \
    \     else:\n                            return P\n        if dist:\n        \
    \    return (inf,None)\n        else:\n            return None\n\n    #\u6DF1\u3044\
    \u30B3\u30D4\u30FC\n    def deepcopy(self):\n        from copy import deepcopy\n\
    \        D=Digraph(self.vertex_count())\n        D.arc_number=self.arc_count()\n\
    \        D.adjacent_out=deepcopy(self.adjacent_out)\n        D.adjacent_in=deepcopy(self.adjacent_in)\n\
    \        return D\n\n#================================================\n#Dijkstra\n\
    def One_Point_Distance(D, From, with_path=False):\n    \"\"\" \u5358\u4E00\u59CB\
    \u70B9 From \u304B\u3089\u306E\u8DDD\u96E2\u3092\u6C42\u3081\u308B.\n\n    D:\
    \ \u8FBA\u306E\u91CD\u307F\u304C\u5168\u3066\u975E\u8CA0\u306E\u6709\u5411\u30B0\
    \u30E9\u30D5\n    From:\u59CB\u70B9\n    with_path:\u6700\u77ED\u8DEF\u3082\u542B\
    \u3081\u3066\u51FA\u529B\u3059\u308B\u304B?\n\n    (\u51FA\u529B\u306E\u7D50\u679C\
    )\n    with_path=True \u2192 (\u8DDD\u96E2, \u6700\u77ED\u7D4C\u8DEF\u306E\u8FBF\
    \u308B\u969B\u306E\u524D\u306E\u9802\u70B9)\n    with_path=False \u2192 \u8DDD\
    \u96E2\n    \"\"\"\n\n    N=D.vertex_count(); inf=float(\"inf\"); adj_out=D.adjacent_out\n\
    \    T=[inf]*N; T[From]=0\n\n    if with_path:\n        Prev=[None]*N\n\n    from\
    \ collections import deque\n    Q=deque([From])\n    while Q:\n        u=Q.popleft()\n\
    \n        for v in D.adjacent_out[u]:\n            if T[v]==inf:\n           \
    \     T[v]=T[u]+1\n                Q.append(v)\n\n                if with_path:\n\
    \                    Prev[v]=u\n\n    if with_path:\n        return (T,Prev)\n\
    \    else:\n        return  T\n\n#Warshall\u2013Floyd\ndef Warshall_Floyd(D):\n\
    \    \"\"\"Warshall\u2013Floyd\u6CD5\u3092\u7528\u3044\u3066,\u5168\u70B9\u9593\
    \u8DDD\u96E2\u3092\u6C42\u3081\u308B.\n\n    D: \u6709\u5411\u30B0\u30E9\u30D5\
    \n    \"\"\"\n\n    N=D.vertex_count(); inf=float(\"inf\"); adj_out=D.adjacent_out\n\
    \    T=[[0]*N for _ in range(N)]\n\n    for u in range(N):\n        for v in range(N):\n\
    \            Tu=T[u]\n            if v==u:\n                T[u][v]=0\n      \
    \      elif v in adj_out[u]:\n                T[u][v]=1\n            else:\n \
    \               T[u][v]=float(\"inf\")\n\n    for u in range(N):\n        Tu=T[u]\n\
    \        for v in range(N):\n            Tv=T[v]\n            for w in range(N):\n\
    \                Tv[w]=min(Tv[w],Tv[u]+Tu[w])\n\n    return T\n\n#From\u304B\u3089\
    To\u3078\u306E(\u9577\u3055\u304C\u4E01\u5EA6L or L\u4EE5\u4E0B\u306E)Walk\u304C\
    \u5B58\u5728\u3059\u308B\u304B\u5426\u304B\ndef walk_exist(graph,From,To,L,just=False):\n\
    \    pass\n\n#\u9006\u30B0\u30E9\u30D5\u306E\u4F5C\u6210\ndef Inverse_Graph(D):\n\
    \    \"\"\"\u6709\u5411\u30B0\u30E9\u30D5D\u306E\u5168\u3066\u306E\u8FBA\u306E\
    \u5411\u304D\u3092\u5909\u3048\u305F\u30B0\u30E9\u30D5\u3092\u51FA\u529B\u3059\
    \u308B.\n\n    D:\u6709\u5411\u30B0\u30E9\u30D5\n    \"\"\"\n    E=D.deepcopy()\n\
    \    E.adjacent_out,E.adjacent_in=E.adjacent_in,E.adjacent_out\n    return E\n\
    \n#\u88DC\u30B0\u30E9\u30D5\u306E\u4F5C\u6210\ndef Complement_Graph(G):\n    pass\n\
    \n#n\u9802\u70B9\u306E\u30E9\u30F3\u30C0\u30E0\u30B0\u30E9\u30D5\ndef Random_Graph(n,p=0.5,seed=None):\n\
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
    def Cycle_Reduction(D):\n    C=Strongly_Connected_Component_Decomposition(D,1)\n\
    \n    E=Digraph(max(C)+1)\n    for v in range(D.vertex_count()):\n        for\
    \ w in D.adjacent_out[v]:\n            if C[v]!=C[w]:\n                E.add_arc(C[v],C[w])\n\
    \    return E\n\n#\u5F37\u9023\u7D50\u6210\u5206\u306B\u5206\u89E3\ndef Strongly_Connected_Component_Decomposition(D,Mode=0):\n\
    \    \"\"\"\u6709\u5411\u30B0\u30E9\u30D5D\u3092\u5F37\u9023\u7D50\u6210\u5206\
    \u306B\u5206\u89E3\n\n    Mode:\n    0(Defalt)---\u5404\u5F37\u9023\u7D50\u6210\
    \u5206\u306E\u9802\u70B9\u306E\u30EA\u30B9\u30C8\n    1        ---\u5404\u9802\
    \u70B9\u304C\u5C5E\u3057\u3066\u3044\u308B\u5F37\u9023\u7D50\u6210\u5206\u306E\
    \u756A\u53F7\n    2        ---0,1\u306E\u4E21\u65B9\n\n    \u203B0\u3067\u5E30\
    \u3063\u3066\u304F\u308B\u30EA\u30B9\u30C8\u306F\u5404\u5F37\u9023\u7D50\u6210\
    \u5206\u306B\u95A2\u3057\u3066\u30C8\u30DD\u30ED\u30B8\u30AB\u30EB\u30BD\u30FC\
    \u30C8\u3067\u3042\u308B.\n    \"\"\"\n\n    N=D.vertex_count()\n    Group=[0]*N\n\
    \    Order=[]\n    adj_out=D.adjacent_out; adj_in=D.adjacent_in\n\n    for v in\
    \ range(N):\n        if Group[v]==-1:\n            continue\n\n        S=[v]\n\
    \        Group[v]=-1\n\n        while S:\n            u=S.pop()\n            for\
    \ w in adj_out[u]:\n                if Group[w]:\n                    continue\n\
    \n                Group[w]=-1\n                S.append(u)\n                S.append(w)\n\
    \                break\n            else:\n                Order.append(u)\n\n\
    \    k=0\n    for v in Order[::-1]:\n        if Group[v]!=-1:\n            continue\n\
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
    \    return len(Strongly_Connected_Component_Decomposition(D))\n\n#\u8A98\u5C0E\
    \u30B0\u30E9\u30D5\ndef Induced_Subgraph(D,S):\n    \"\"\" \u4EE5\u4E0B\u3092\u6E80\
    \u305F\u3059\u3088\u3046\u306A\u30B0\u30E9\u30D5 D' \u3092\u751F\u6210\u3059\u308B\
    .\n    V(D')=V(D), st in A(D') iff st in A(D), s,t in S\n\n    D: \u6709\u5411\
    \u30B0\u30E9\u30D5\n    S: \u9802\u70B9\u96C6\u5408\n    \"\"\"\n    S=set(S)\n\
    \n    N=D.vertex_count()\n    E=Digraph(N); adj_out=D.adjacent_out\n\n    for\
    \ s in range(N):\n        if s not in S:\n            continue\n\n        for\
    \ t in adj_out[s]:\n            if t in S:\n                E.add_arc(s,t)\n \
    \   return E\n\n#Cycle\u304C\u5B58\u5728\u3059\u308B?\ndef Is_Exist_Cycle(D):\n\
    \    return not Is_Directed_Acyclic_Graph(D)\n\n#Cycle\u3092\u898B\u3064\u3051\
    \u308B.\n#\u53C2\u8003\u5143:https://judge.yosupo.jp/submission/23992\ndef Find_Cycle(D):\n\
    \    from collections import deque\n\n    N=D.vertex_count()\n    in_deg=[D.in_degree(v)\
    \ for v in range(N)]\n    adj_out=D.adjacent_out\n    Q=deque([v for v in range(N)\
    \ if in_deg[v]==0])\n\n    while Q:\n        v=Q.popleft()\n        for w in adj_out[v]:\n\
    \            in_deg[w]-=1\n            if in_deg[w]==0:\n                Q.append(w)\n\
    \n    for v in range(N):\n        P=[]\n        if in_deg[v]==0:\n           \
    \ continue\n\n        Q=deque([v])\n        prev=[-1]*N\n        while Q:\n  \
    \          x=Q.popleft()\n            for y in adj_out[x]:\n                if\
    \ y==v:\n                    prev[v]=x\n                    break\n          \
    \      if prev[y]!=-1:\n                    continue\n\n                prev[y]=x\n\
    \                Q.append(y)\n            else:\n                continue\n  \
    \          break\n        else:\n            continue\n        P=[v]\n       \
    \ x=v\n        while prev[x]!=v:\n            x=prev[x]\n            P.append(x)\n\
    \        break\n    if P:\n        return P[::-1]\n    else:\n        return None\n\
    \n#2\u90E8\u30B0\u30E9\u30D5?\ndef Is_Bipartite_Graph(G):\n    pass\n\n#2\u90E8\
    \u30B0\u30E9\u30D5\u306E\u90E8\u96C6\u5408\u306B\u5206\u5272\ndef Bipartite_Separate(G):\n\
    \    pass\n\n#\u30AA\u30A4\u30E9\u30FC\u30B0\u30E9\u30D5?\ndef Is_Eulerian_Graph(D):\n\
    \    pass\n\n#\u6E96\u30AA\u30A4\u30E9\u30FC\u30B0\u30E9\u30D5?\ndef Is_Semi_Eulerian_Graph(D):\n\
    \    pass\n\n#Euler\u9053\u3092\u898B\u3064\u3051\u308B\ndef Find_Eulerian_Trail(D):\n\
    \    N=D.vertex_count()\n    s=-1\n    for v in range(N):\n        k=D.relative_degree(v)\n\
    \        if abs(k)>=2:\n            return None\n        elif k==1:\n        \
    \    if s>=0:\n                return None\n            s=v\n    if s==-1:\n \
    \       return None\n\n    from copy import deepcopy\n    A=deepcopy(D.adjacent_out)\n\
    \n    def dfs(w):\n        X=[w]\n        while A[w]:\n            u=A[w].pop()\n\
    \            A[u].discard(w)\n            X.append(u)\n            w=u\n     \
    \   return X\n\n    P=[]\n    Q=dfs(s)\n    while Q:\n        u=Q.pop()\n    \
    \    P.append(u)\n        if len(A[u])>0:\n            Q.extend(dfs(u)[:-1])\n\
    \n    if len(P)-1==D.arc_count():\n        return P[::-1]\n    else:\n       \
    \ return None\n\n#Euler\u9589\u8DEF\u3092\u898B\u3064\u3051\u308B\ndef Find_Eulerian_Cycle(D):\n\
    \    N=D.vertex_count()\n    for v in range(N):\n        if D.relative_degree(v):\n\
    \            return None\n\n    from copy import deepcopy\n    A=deepcopy(D.adjacent_out)\n\
    \    def dfs(w):\n        X=[w]\n        while A[w]:\n            u=A[w].pop()\n\
    \            A[u].discard(w)\n            X.append(u)\n            w=u\n     \
    \   return X\n\n    P=[]\n    Q=dfs(0)\n    while Q:\n        u=Q.pop()\n    \
    \    P.append(u)\n        if len(A[u])>0:\n            Q.extend(dfs(u)[:-1])\n\
    \n    if len(P)-1==D.arc_count():\n        return P[::-1]\n    else:\n       \
    \ return None\n\n#\u30CF\u30DF\u30EB\u30C8\u30F3\u30B0\u30E9\u30D5?\ndef Is_Hamiltonian_Graph(G):\n\
    \    pass\n\n#\u30CF\u30DF\u30EB\u30C8\u30F3\u3092\u63A2\u3059.\ndef Find_Hamiltonian_Graph(G):\n\
    \    pass\n\n#-------------------------------------------------\n#\u7279\u5225\
    \u306A\u30B0\u30E9\u30D5\n#-------------------------------------------------\n\
    #\u5B8C\u5168\u30B0\u30E9\u30D5\u306E\u4F5C\u6210\ndef Complete_Graph(n):\n  \
    \  pass\n\n#\u5B8C\u51682\u90E8\u30B0\u30E9\u30D5\ndef Complete_Bipartite_Graph(m,n):\n\
    \    pass\n\n#\u30B0\u30E9\u30D5\u4F5C\u6210\ndef Making_Digraph(N, A):\n    D=Digraph(N)\n\
    \    for a in A:\n        D.add_arc(*a)\n    return D\n\n#\u7A7A\u30B0\u30E9\u30D5\
    \u306E\u4F5C\u6210\ndef Empty_Graph(N):\n    return Digraph(N)\n\n#\u30DA\u30C6\
    \u30EB\u30BB\u30F3\u30B0\u30E9\u30D5\ndef Petersen_Graph(n=5,k=2):\n    pass\n\
    \n#\u683C\u5B50\u30B0\u30E9\u30D5\ndef Grid_Graph(m,n):\n    pass\n\n#Path\u30B0\
    \u30E9\u30D5\ndef Directed_Path_Graph(N):\n    \"\"\" N \u9802\u70B9\u306E\u6709\
    \u5411\u30B5\u30A4\u30AF\u30EB\u3092\u751F\u6210\u3059\u308B. \"\"\"\n\n    P=Digraph(N)\n\
    \    for i in range(N-1):\n        P.add_arc(i,i+1)\n    return P\n\n#Cycle\u30B0\
    \u30E9\u30D5\ndef Directed_Cycle_Graph(N, reverse=False):\n    \"\"\" N \u9802\
    \u70B9\u306E\u6709\u5411\u30B5\u30A4\u30AF\u30EB\u3092\u751F\u6210\u3059\u308B\
    . \"\"\"\n\n    C=Digraph(N)\n    for i in range(N):\n        if reverse:\n  \
    \          j=(i-1)%N\n        else:\n            j=(i+1)%N\n        C.add_arc(i,j)\n\
    \    return C\n\n#Circulant \u30B0\u30E9\u30D5\ndef Circulant_Graph(N, *J):\n\
    \    \"\"\" N \u9802\u70B9, J \u30B8\u30E3\u30F3\u30D7\u306E\u5DE1\u56DE\u30B0\
    \u30E9\u30D5\u3092\u751F\u6210\u3059\u308B.\"\"\"\n\n    C=Digraph(N)\n    for\
    \ j in J:\n        for v in range(N):\n            w=(v+j)%N\n            C.add_arc(v,w)\n\
    \    return C\n\n#Star\u30B0\u30E9\u30D5\ndef Star_Graph(n):\n    pass\n\n#Wheel\u30B0\
    \u30E9\u30D5\ndef Wheel_Graph(n):\n    pass\n\n#\u9A0E\u58EB\u5DE1\u56DE\u30B0\
    \u30E9\u30D5\ndef Knight_Tour_Graph(m,n):\n    pass\n\n#\u5B8C\u5168k\u5206\u6728\
    \ndef Complete_Kary_Tree(n,k=2):\n    pass\n\n#---------------------------------------\n\
    #\u30B0\u30E9\u30D5\u306E\u635C\u67FB\n#---------------------------------------\n\
    def Depth_First_Search(D, start, prefunc=None, postfunc=None):\n    \"\"\"\u6DF1\
    \u3055\u512A\u5148\u63A2\u7D22\u3092\u884C\u3046.\n\n    D: \u6709\u5411\u30B0\
    \u30E9\u30D5\n    prefunc: \u9802\u70B9\u3092Stack\u306B\u5165\u308C\u308B\u6642\
    ,\u305D\u306E\u9802\u70B9v\u306B\u5BFE\u3057\u3066\u5B9F\u884C\u3059\u308B\u95A2\
    \u6570,\u547D\u4EE4.\n    postfunc: \u9802\u70B9\u3092Stack\u304B\u3089\u51FA\u3059\
    \u6642,\u305D\u306E\u9802\u70B9v\u306B\u5BFE\u3057\u3066\u5B9F\u884C\u3059\u308B\
    \u95A2\u6570,\u547D\u4EE4.\n    \"\"\"\n    from collections import deque\n\n\
    \    N=D.vertex_count()\n    T=[0]*N; T[start]=1\n    adj_out=D.adjacent_out\n\
    \n    S=deque([start])\n\n    if prefunc:\n        prefunc(start)\n\n    while\
    \ S:\n        v=S.pop()\n        if postfunc:\n            postfunc(v)\n\n   \
    \     for u in adj_out[v]:\n            if T[u]==0:\n                T[u]=1\n\
    \                S.append(u)\n                if prefunc:\n                  \
    \  prefunc(u)\n\ndef Breath_First_Search(D, start, prefunc=None, postfunc=None):\n\
    \    \"\"\" \u5E45\u512A\u5148\u63A2\u7D22\u3092\u884C\u3046.\n\n    D: \u6709\
    \u5411\u30B0\u30E9\u30D5\n    prefunc: \u9802\u70B9\u3092Stack\u306B\u5165\u308C\
    \u308B\u6642,\u305D\u306E\u9802\u70B9v\u306B\u5BFE\u3057\u3066\u5B9F\u884C\u3059\
    \u308B\u95A2\u6570,\u547D\u4EE4.\n    postfunc: \u9802\u70B9\u3092Stack\u304B\u3089\
    \u51FA\u3059\u6642,\u305D\u306E\u9802\u70B9v\u306B\u5BFE\u3057\u3066\u5B9F\u884C\
    \u3059\u308B\u95A2\u6570,\u547D\u4EE4.\n    \"\"\"\n    from collections import\
    \ deque\n\n    N=D.vertex_count()\n    T=[0]*N; T[start]=1\n    adj_out=D.adjacent_out\n\
    \n    Q=deque([start])\n\n    if prefunc:\n        prefunc(start)\n\n    while\
    \ Q:\n        v=Q.popleft()\n        if postfunc:\n            postfunc(v)\n\n\
    \        for u in adj_out[v]:\n            if T[u]==0:\n                T[u]=1\n\
    \                Q.append(u)\n                if prefunc:\n                  \
    \  prefunc(u)\n"
  dependsOn: []
  isVerificationFile: false
  path: Graph/Digraph.py
  requiredBy: []
  timestamp: '2022-04-16 12:03:09+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Graph/Digraph.py
layout: document
redirect_from:
- /library/Graph/Digraph.py
- /library/Graph/Digraph.py.html
title: Graph/Digraph.py
---
