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
  code: "class Graph:\n    __slots__=(\"edge_number\", \"adjacent\")\n\n    #\u5165\
    \u529B\u5B9A\u7FA9\n    def __init__(self, N=0):\n        \"\"\" N \u9802\u70B9\
    \u306E\u7A7A\u30B0\u30E9\u30D5 (\u591A\u91CD\u8FBA\u306A\u3057) \u3092\u751F\u6210\
    \u3059\u308B.\"\"\"\n\n        self.edge_number=0\n        self.adjacent=[set()\
    \ for _ in range(N)]\n\n    #\u9802\u70B9\u306E\u8FFD\u52A0\n    def add_vertex(self):\n\
    \        \"\"\" \u9802\u70B9\u3092\u8FFD\u52A0\u3059\u308B.\n\n        \"\"\"\n\
    \        self.adjacent.append(set())\n        return self.order()-1\n\n    def\
    \ add_vertices(self, k):\n        \"\"\" \u9802\u70B9\u3092 k \u500B\u8FFD\u52A0\
    \u3059\u308B.\n\n        k: int\n        \"\"\"\n\n        n=self.order()\n  \
    \      self.adjacent.extend([set() for _ in range(k)])\n        return list(range(n,n+k))\n\
    \n    #\u8FBA\u306E\u8FFD\u52A0\n    def add_edge(self,u,v):\n        \"\"\" \u7121\
    \u5411\u8FBA uv \u3092\u52A0\u3048\u308B\"\"\"\n\n        if not self.edge_exist(u,v):\n\
    \            self.adjacent[u].add(v)\n            self.adjacent[v].add(u)\n  \
    \          self.edge_number+=1\n            return self.edge_number-1\n      \
    \  else:\n            return -1\n\n    #\u8FBA\u3092\u9664\u304F\n    def remove_edge(self,u,v):\n\
    \        \"\"\" \u7121\u5411\u8FBA uv \u304C\u5B58\u5728\u3059\u308B\u306A\u3089\
    \u3070\u9664\u304F\"\"\"\n\n        if self.edge_exist(u,v):\n            self.adjacent[u].discard(v)\n\
    \            self.adjacent[v].discard(u)\n            self.edge_number-=1\n  \
    \          return True\n        else:\n            return False\n\n    def reset_vertex(self,\
    \ u):\n        \"\"\" \u9802\u70B9 u \u306B\u63A5\u7D9A\u3057\u3066\u3044\u308B\
    \u8FBA\u3092\u5168\u3066\u6D88\u3059.\"\"\"\n\n        X=self.adjacent[u].copy()\n\
    \        for v in X:\n            self.remove_edge(u,v)\n\n    #Walk\u306E\u8FFD\
    \u52A0\n    def add_walk(self,*walk):\n        \"\"\" walk=(w[0],...,w[n-1]) \u306B\
    \u5BFE\u3057\u3066, n-1 \u672C\u306E\u8FBA w[i]w[i+1] \u3092\u52A0\u3048\u308B\
    .\"\"\"\n        n=len(walk)\n        for i in range(n-1):\n            self.add_edge(walk[i],walk[i+1])\n\
    \n    #Cycle\u306E\u8FFD\u52A0\n    def add_cycle(self,*cycle):\n        \"\"\"\
    \ cycle=(c[0], ..., c[n-1]) \u3092\u52A0\u3048\u308B. \"\"\"\n        self.add_walk(*cycle)\n\
    \        self.add_edge(cycle[-1],cycle[0])\n\n    #\u30B0\u30E9\u30D5\u306B\u8FBA\
    \u304C\u5B58\u5728\u3059\u308B\u304B\u5426\u304B\n    def edge_exist(self,u,v):\n\
    \        \"\"\" \u8FBA uv \u304C\u5B58\u5728\u3059\u308B\u304B? \"\"\"\n     \
    \   return v in self.adjacent[u]\n\n    #\u8FD1\u508D\n    def neighbohood(self,v):\n\
    \        \"\"\" \u9802\u70B9 v  \u306E\u8FD1\u508D\u3092\u6C42\u3081\u308B. \"\
    \"\"\n        return self.adjacent[v]\n\n    #\u6B21\u6570\n    def degree(self,v):\n\
    \        \"\"\" \u9802\u70B9 v \u306E\u6B21\u6570\u3092\u6C42\u3081\u308B. \"\"\
    \"\n        if v in self.adjacent[v]:\n            return len(self.adjacent[v])+1\n\
    \        else:\n            return len(self.adjacent[v])\n\n    #\u9802\u70B9\u6570\
    \n    def vertex_count(self):\n        \"\"\" \u30B0\u30E9\u30D5\u306E\u9802\u70B9\
    \u6570 (\u4F4D\u6570) \u3092\u51FA\u529B\u3059\u308B. \"\"\"\n        return len(self.adjacent)\n\
    \n    def order(self):\n        \"\"\" \u30B0\u30E9\u30D5\u306E\u4F4D\u6570 (\u9802\
    \u70B9\u6570) \u3092\u51FA\u529B\u3059\u308B. \"\"\"\n        return len(self.adjacent)\n\
    \n    #\u8FBA\u6570\n    def edge_count(self):\n        \"\"\" \u8FBA\u306E\u672C\
    \u6570 (\u30B5\u30A4\u30BA) \u3092\u51FA\u529B\u3059\u308B.\"\"\"\n\n        return\
    \ self.edge_number\n\n    def size(self):\n        \"\"\" \u30B5\u30A4\u30BA (\u8FBA\
    \u306E\u672C\u6570) \u3092\u51FA\u529B\u3059\u308B. \"\"\"\n\n        return self.edge_number\n\
    \n    #\u9802\u70B9v\u3092\u542B\u3080\u9023\u7D50\u6210\u5206\n    def connected_component(self,v):\n\
    \        \"\"\" \u9802\u70B9 v \u3092\u542B\u3080\u9023\u7D50\u6210\u5206\u3092\
    \u51FA\u529B\u3059\u308B.\"\"\"\n\n        from collections import deque\n   \
    \     N=len(self.adjacent)\n        T=[0]*N; T[v]=1\n        Q=deque([v])\n  \
    \      while Q:\n            u=Q.popleft()\n            for w in self.adjacent[u]:\n\
    \                if T[w]==0:\n                    T[w]=1\n                   \
    \ Q.append(w)\n        return [x for x in range(N) if T[x]]\n\n    #\u8DDD\u96E2\
    \n    def distance(self,u,v):\n        \"\"\" 2\u9802\u70B9 u,v \u9593\u306E\u8DDD\
    \u96E2\u3092\u6C42\u3081\u308B.\"\"\"\n\n        if u==v:\n            return\
    \ 0\n\n        from collections import deque\n        inf=float(\"inf\")\n   \
    \     N=len(self.adjacent)\n        T=[inf]*N; T[u]=0\n\n        Q=deque([u])\n\
    \        while Q:\n            w=Q.popleft()\n            for x in self.adjacent[w]:\n\
    \                if T[x]==inf:\n                    T[x]=T[w]+1\n            \
    \        Q.append(x)\n                    if x==v:\n                        return\
    \ T[x]\n        return inf\n\n    #\u3042\u308B1\u70B9\u304B\u3089\u306E\u8DDD\
    \u96E2\n    def distance_all(self,u):\n        \"\"\" \u9802\u70B9 u \u304B\u3089\
    \u306E\u8DDD\u96E2\u3092\u6C42\u3081\u308B.\"\"\"\n\n        from collections\
    \ import deque\n        inf=float(\"inf\")\n        N=len(self.adjacent)\n   \
    \     T=[inf]*N; T[u]=0\n\n        Q=deque([u])\n        while Q:\n          \
    \  w=Q.popleft()\n            for x in self.adjacent[w]:\n                if T[x]==inf:\n\
    \                    T[x]=T[w]+1\n                    Q.append(x)\n        return\
    \ T\n\n    #\u6700\u77ED\u8DEF\n    def shortest_path(self,u,v):\n        \"\"\
    \" u \u304B\u3089 v \u3078\u306E\u6700\u77ED\u8DEF\u3092\u6C42\u3081\u308B (\u5B58\
    \u5728\u3057\u306A\u3044\u5834\u5408\u306F None). \"\"\"\n\n        if u==v:\n\
    \            return [u]\n\n        from collections import deque\n        inf=float(\"\
    inf\")\n        T=[-1]*len(self.adjacent)\n\n        Q=deque([u]); T[u]=u\n  \
    \      while Q:\n            w=Q.popleft()\n            for x in self.adjacent[w]:\n\
    \                if T[x]==-1:\n                    T[x]=w\n                  \
    \  Q.append(x)\n                    if x==v:\n                        P=[v]\n\
    \                        a=v\n                        while a!=u:\n          \
    \                  a=T[a]\n                            P.append(a)\n         \
    \               return P[::-1]\n        return None\n\n    def edge_yielder(self):\n\
    \        g=self.adjacent\n        for v in range(self.vertex_count()):\n     \
    \       for w in g[v]:\n                if v<=w:\n                    yield (v,w)\n\
    \n#==========\n#\u30B0\u30E9\u30D5\u306E\u751F\u6210\n#==========\n#\u88DC\u30B0\
    \u30E9\u30D5\u306E\u4F5C\u6210\ndef Complement_Graph(G):\n    \"\"\" \u30B0\u30E9\
    \u30D5 G \u306E\u88DC\u30B0\u30E9\u30D5\u3092\u6C42\u3081\u308B.\"\"\"\n\n   \
    \ N=G.vertex_count(); V=set(range(N))\n    H=Graph(N)\n\n    for u in range(N):\n\
    \        H.adjacent[u]=V-G.adjacent[u]-{u}\n    return H\n\n# N \u9802\u70B9\u306E\
    \u30E9\u30F3\u30C0\u30E0\u30B0\u30E9\u30D5\ndef Random_Graph(N, p=0.5, self_loop=False,\
    \ seed=None):\n    import random\n    G=Graph(N)\n\n    random.seed(seed)\n  \
    \  for u in range(N):\n        for v in range(u,N):\n            if u==v and self_loop==False:\n\
    \                continue\n\n            if random.random()<p:\n             \
    \   G.add_edge(u,v)\n    return G\n\ndef Directed_Sum(*G):\n    offset=0\n   \
    \ H=Graph()\n    for g in G:\n        n=g.vertex_count()\n        H.add_vertices(n)\n\
    \        for i,j in g.edge_yielder():\n            H.add_edge(i+offset, j+offset)\n\
    \        offset+=n\n    return H\n\n#==========\n#\u9023\u7D50\u30B0\u30E9\u30D5\
    ?\ndef Is_Connected(G):\n    from collections import deque\n\n    N=G.vertex_count()\n\
    \    T=[0]*N; T[0]=1\n    Q=deque([0])\n\n    Q_popleft=Q.popleft\n    Q_append=Q.append\n\
    \    adj=G.adjacent\n\n    while Q:\n        u=Q_popleft()\n        for v in adj[u]:\n\
    \            if T[v]==0:\n                T[v]=1\n                Q_append(v)\n\
    \n    return all(T)\n\ndef Lowlink(G, mode=0):\n    \"\"\" G \u306E ord, lowlink\
    \ \u3092\u6C42\u3081\u308B.\n\n    G: Graph\n\n    output: (ord, lowlink)\n  \
    \  \"\"\"\n\n    from collections import deque\n\n    N=G.vertex_count()\n   \
    \ ord=[-1]*N; low=[-1]*N\n    flag=[0]*N\n    adj=G.adjacent\n    parent=[-1]*N\n\
    \n    #BFS\u30D1\u30FC\u30C8\n    for v in range(N):\n        if flag[v]:\n  \
    \          continue\n\n        k=0\n        S=deque([v])\n        T=[]\n\n   \
    \     while S:\n            u=S.pop()\n            if flag[u]:\n             \
    \   continue\n\n            T.append(u)\n            ord[u]=k\n            k+=1\n\
    \            flag[u]=1\n\n            for w in adj[u]:\n                if not\
    \ flag[w]:\n                    S.append(w)\n                    parent[w]=u\n\
    \n        for u in T:\n            low[u]=ord[u]\n\n        for w in T[:0:-1]:\n\
    \            for x in adj[w]:\n                if w==v or x!=parent[w]:\n    \
    \                low[w]=min(low[w],low[x],ord[x])\n\n    if mode==0:\n       \
    \ return ord, low\n    else:\n        return ord, low, parent\n\n#\u6A4B\u5217\
    \u6319\ndef Bridge(G):\n    \"\"\" G \u306B\u3042\u308B\u6A4B\u3092\u5217\u6319\
    \u3059\u308B.\n\n    G: Graph\n    \"\"\"\n    ord,low=Lowlink(G)\n    return\
    \ [(u,v) for u,v in G.edge_yielder() if ord[u]<low[v] or ord[v]<low[u]]\n\n#\u95A2\
    \u7BC0\u70B9\u306E\u5217\u6319\ndef Articulation_Point(G):\n    from collections\
    \ import deque\n\n    N=G.vertex_count()\n    A=[]; A_append=A.append\n    ord=[-1]*N;\
    \ low=[-1]*N\n    flag=[0]*N\n    adj=G.adjacent\n\n    parent=[-1]*N; children=[[]\
    \ for _ in range(N)]\n\n    #BFS\u30D1\u30FC\u30C8\n    for v in range(N):\n \
    \       if flag[v]:\n            continue\n\n        k=0\n        S=deque([v])\n\
    \        T=[]\n        X=[]\n\n        while S:\n            u=S.pop()\n     \
    \       if flag[u]:\n                continue\n\n            T.append(u)\n   \
    \         ord[u]=k\n            k+=1\n            flag[u]=1\n\n            for\
    \ w in adj[u]:\n                if not flag[w]:\n                    S.append(w)\n\
    \                    parent[w]=u\n\n        for w in T:\n            low[w]=ord[w]\n\
    \n        for w in T[:0:-1]:\n            children[parent[w]].append(w)\n\n  \
    \      for w in T[:0:-1]:\n            for x in adj[w]:\n                if w==v\
    \ or x!=parent[w]:\n                    low[w]=min(low[w],low[x],ord[x])\n\n \
    \       #\u6839\u3067\u306E\u5224\u5B9A\n        if len(children[v])>=2:\n   \
    \         A_append(v)\n\n        #\u6839\u4EE5\u5916\u306E\u5224\u5B9A\n     \
    \   for w in T[:0:-1]:\n            for u in children[w]:\n                if\
    \ ord[w]<=low[u]:\n                    A_append(w)\n                    break\n\
    \    return A\n\n#\u4E8C\u8FBA\u9023\u7D50\u6210\u5206\u5206\u89E3\ndef Two_Edge_Connected_Components(G):\n\
    \    \"\"\"\u30B0\u30E9\u30D5 G \u3092\u4E8C\u8FBA\u9023\u7D50\u6210\u5206\u5206\
    \u89E3 (\u6A4B\u3092\u542B\u307E\u306A\u3044) \u3059\u308B.\n\n    [input]\n \
    \   G: Graph\n    \"\"\"\n\n    N=G.vertex_count()\n\n    ord,low=Lowlink(G)\n\
    \n    T=[0]*N; C=[]\n    for v in range(N):\n        if T[v]==1:\n           \
    \ continue\n\n        T[v]=1\n        Q=[v]; c=[]\n        while Q:\n        \
    \    v=Q.pop()\n            c.append(v)\n\n            for w in G.adjacent[v]:\n\
    \                if (ord[v]>=low[w] and ord[w]>=low[v]) and T[w]==0:\n       \
    \             T[w]=1\n                    Q.append(w)\n        C.append(c)\n \
    \   return C\n\n#=====\n#\u68EE?\ndef Is_Forest(G):\n    \"\"\" \u68EE\u304B\u3069\
    \u3046\u304B\u5224\u5B9A\u3059\u308B. \"\"\"\n\n    C=Connected_Component_Number(G)\n\
    \    M=G.edge_count()\n    return G.vertex_count()==M+C\n\n#\u6728?\ndef Is_Tree(G):\n\
    \    \"\"\" \u6728\u304B\u3069\u3046\u304B\u5224\u5B9A\u3059\u308B. \"\"\"\n \
    \   C=Connected_Component_Number(G)\n    M=G.edge_count()\n    return C==1 and\
    \ G.vertex_count()==M+C\n\n#\u6728\u306E\u76F4\u5F84\ndef Tree_Diameter(T,Mode=False):\n\
    \    \"\"\" \u6728 T \u306E\u76F4\u5F84\u3092\u6C42\u3081\u308B.\n\n    T: \u6728\
    \n\n    (\u51FA\u529B\u306E\u7D50\u679C)\n    Mode=True \u2192 (\u76F4\u5F84,\
    \ (\u76F4\u5F84\u3092\u6210\u3059\u7AEF\u70B91, \u76F4\u5F84\u3092\u6210\u3059\
    \u7AEF\u70B92))\n    Mode=False \u2192 \u76F4\u5F84\n    \"\"\"\n    from collections\
    \ import deque\n\n    def __bfs(x):\n        N=T.vertex_count()\n        D=[-1]*N\n\
    \        D[x]=0\n        Q=deque([x])\n        while Q:\n            x=Q.popleft()\n\
    \n            for y in T.adjacent[x]:\n                if D[y]==-1:\n        \
    \            D[y]=D[x]+1\n                    Q.append(y)\n        z=max(range(N),key=lambda\
    \ x:D[x])\n        return z,D[z]\n\n    u,_=__bfs(0)\n    v,d=__bfs(u)\n\n   \
    \ if Mode:\n        return (d,(u,v))\n    else:\n        return d\n\n#\u9023\u7D50\
    \u6210\u5206\u306B\u5206\u89E3\ndef Connected_Component_Decomposition(G, mode=0):\n\
    \    \"\"\" \u9023\u7D50\u6210\u5206\u6BCE\u306B\u5206\u89E3\u3059\u308B.\n\n\
    \    G: Graph\n    mode: 0\u2192\u9023\u7D50\u6210\u5206, 1, \u9023\u7D50\u6210\
    \u5206\u756A\u53F7, 2\u2192 (\u9023\u7D50\u6210\u5206, \u9023\u7D50\u6210\u5206\
    \u756A\u53F7)\"\"\"\n    from collections import deque\n\n    N=G.vertex_count()\n\
    \    T=[-1]*N\n    C=[]\n    k=0\n    for v in range(N):\n        if T[v]==-1:\n\
    \            Q=deque([v]); T[v]=k\n            c=[]\n            while Q:\n  \
    \              u=Q.popleft()\n                c.append(u)\n                for\
    \ w in G.adjacent[u]:\n                    if T[w]==-1:\n                    \
    \    T[w]=k\n                        Q.append(w)\n            k+=1\n         \
    \   C.append(c)\n\n    if mode==0:\n        return C\n    elif mode==1:\n    \
    \    return  T\n    else:\n        return C,T\n\n#\u9023\u7D50\u6210\u5206\u306E\
    \u500B\u6570\ndef Connected_Component_Number(G):\n    \"\"\" \u9023\u7D50\u6210\
    \u5206\u306E\u500B\u6570\u3092\u6C42\u3081\u308B. \"\"\"\n\n    from collections\
    \ import deque\n\n    N=G.vertex_count()\n    T=[0]*N\n    K=0\n    for v in range(N):\n\
    \        if T[v]==0:\n            Q=deque([v]);T[v]=1\n            K+=1\n    \
    \        while Q:\n                u=Q.popleft()\n                for w in G.adjacent[u]:\n\
    \                    if T[w]==0:\n                        T[w]=1\n           \
    \             Q.append(w)\n    return K\n\n#Cycle\u304C\u5B58\u5728\u3059\u308B\
    ?\ndef Is_Exist_Cycle(G):\n    from collections import deque\n\n    N=G.vertex_count()\n\
    \    T=[0]*N\n    adj=G.adjacent\n\n    for v in range(N):\n        if not T[v]:\n\
    \            x=v\n            T[v]=1\n            S=deque([v])\n            while\
    \ S:\n                u=S.popleft()\n                for w in adj[u]:\n      \
    \              if T[w]==0:\n                        T[w]=1\n                 \
    \       S.append(w)\n                    elif x!=w:\n                        return\
    \ True\n                x=u\n\n    return False\n\n#2\u90E8\u30B0\u30E9\u30D5\
    ?\ndef Is_Bipartite_Graph(G):\n    \"\"\" 2\u90E8\u30B0\u30E9\u30D5\u304B\u3069\
    \u3046\u304B\u3092\u5224\u5B9A\u3059\u308B. \"\"\"\n\n    N=G.vertex_count()\n\
    \    T=[0]*N\n    adj=G.adjacent\n\n    for v in range(N):\n        if T[v]==0:\n\
    \            T[v]=1\n            S=[v]\n            while S:\n               \
    \ u=S.pop()\n                for w in adj[u]:\n                    if T[w]==0:\n\
    \                        T[w]=-T[u]\n                        S.append(w)\n   \
    \                 elif T[w]==T[u]:\n                        return False\n   \
    \ return True\n\n#2\u90E8\u30B0\u30E9\u30D5\u306E\u90E8\u96C6\u5408\u306B\u5206\
    \u5272\ndef Bipartite_Separate(G):\n    \"\"\" 2\u90E8\u30B0\u30E9\u30D5\u306E\
    \u9802\u70B9\u3092\u90E8\u96C6\u5408\u306B\u5206\u5272\u3059\u308B. \"\"\"\n\n\
    \    N=G.vertex_count()\n    T=[0]*N\n    adj=G.adjacent\n\n    for v in range(N):\n\
    \        if T[v]==0:\n            T[v]=1\n            S=[v]\n            while\
    \ S:\n                u=S.pop()\n                for w in adj[u]:\n          \
    \          if T[w]==0:\n                        T[w]=-T[u]\n                 \
    \       S.append(w)\n                    elif T[w]==T[u]:\n                  \
    \      return None, None\n\n    U=[u for u in range(N) if T[u]==1]\n    V=[v for\
    \ v in range(N) if T[v]==-1]\n    return U,V\n\n#\u30AA\u30A4\u30E9\u30FC\u30B0\
    \u30E9\u30D5?\ndef Is_Eulerian_Graph(G):\n    \"\"\" \u30B0\u30E9\u30D5 G \u304C\
    \u30AA\u30A4\u30E9\u30FC\u30B0\u30E9\u30D5\u304B\u3069\u3046\u304B\u3092\u5224\
    \u5B9A\u3059\u308B. \"\"\"\n\n    N=G.vertex_count()\n    for v in range(N):\n\
    \        if G.degree(v)%2:\n            return False\n    return Is_Connected(G)\n\
    \n#\u6E96\u30AA\u30A4\u30E9\u30FC\u30B0\u30E9\u30D5?\ndef Is_Semi_Eulerian_Graph(G):\n\
    \    \"\"\" \u30B0\u30E9\u30D5 G \u304C\u6E96\u30AA\u30A4\u30E9\u30FC\u30B0\u30E9\
    \u30D5\u304B\u3069\u3046\u304B\u3092\u5224\u5B9A\u3059\u308B. \"\"\"\n\n    K=0\n\
    \    N=G.vertex_count()\n    for v in range(N):\n        if G.degree(v)%2:\n \
    \           K+=1\n            if K==3:\n                return False\n    return\
    \ K==2 and Is_Connected(G)\n\n#Euler \u8DEF\u3092\u898B\u3064\u3051\u308B\ndef\
    \ Find_Eulerian_Trail(G):\n    K=0\n    N=G.vertex_count()\n    for v in range(N-1,-1,-1):\n\
    \        if G.degree(v)%2:\n            K+=1\n            s=v\n\n            if\
    \ K==3:\n                return None\n    if K==0:\n        return None\n\n  \
    \  from copy import deepcopy\n    E=deepcopy(G.adjacent)\n\n    def dfs(w):\n\
    \        X=[w]\n        while E[w]:\n            u=E[w].pop()\n            E[u].discard(w)\n\
    \            X.append(u)\n            w=u\n        return X\n\n    P=[]\n    Q=dfs(s)\n\
    \    while Q:\n        u=Q.pop()\n        P.append(u)\n        if len(E[u])>0:\n\
    \            Q.extend(dfs(u)[:-1])\n\n    if len(P)-1==G.edge_count():\n     \
    \   return P\n    else:\n        return None\n\n#Euler\u9589\u8DEF\u3092\u898B\
    \u3064\u3051\u308B\ndef Find_Eulerian_Cycle(G):\n    N=G.vertex_count()\n    for\
    \ v in range(N-1,-1,-1):\n        if G.degree(v)%2:\n            return None\n\
    \n    from copy import deepcopy\n    E=deepcopy(G.adjacent)\n\n    def dfs(w):\n\
    \        X=[w]\n        while E[w]:\n            u=E[w].pop()\n            E[u].discard(w)\n\
    \            X.append(u)\n            w=u\n        return X\n\n    P=[]\n    Q=dfs(0)\n\
    \    while Q:\n        u=Q.pop()\n        P.append(u)\n        if len(E[u])>0:\n\
    \            Q.extend(dfs(u)[:-1])\n\n    if len(P)-1==G.edge_count():\n     \
    \   return P\n    else:\n        return None\n\n#\u30CF\u30DF\u30EB\u30C8\u30F3\
    \u30B0\u30E9\u30D5?\ndef Is_Hamiltonian_Graph(G):\n    N=len(G.vertex)\n    if\
    \ N==2 or N==0:\n        return False\n    elif N==1:\n        return True\n\n\
    \    A=G.vertex[0]\n    B=G.vertex[1]\n    C=G.vertex[2]\n\n    X={v:False for\
    \ v in G.vertex}\n    X[A]=True\n    #------------------------------\n    def\
    \ __f__(v,k):\n        if k==0:\n            return v in G.adjacent[A]\n\n   \
    \     if v==B and X[C]:\n            return False\n\n        for w in G.adjacent[v]:\n\
    \            if not X[w]:\n                X[w]=True\n                if __f__(w,k-1):\n\
    \                    return True\n                X[w]=False\n\n        return\
    \ False\n    #------------------------------\n    return __f__(A,N-1)\n\n#\u30CF\
    \u30DF\u30EB\u30C8\u30F3\u3092\u63A2\u3059.\ndef Find_Hamiltonian_Graph(G):\n\
    \    from collections import deque\n\n    N=len(G.vertex)\n    if N==2 or N==0:\n\
    \        return None\n    elif N==1:\n        return G.vertex\n\n    A=G.vertex[0]\n\
    \    B=G.vertex[1]\n    C=G.vertex[2]\n\n    X={v:False for v in G.vertex}\n \
    \   X[A]=True\n    Y=deque([A])\n    #------------------------------\n    def\
    \ __f__(v,k):\n        if k==0:\n            return v in G.adjacent[A]\n\n   \
    \     if v==B and X[C]:\n            return False\n\n        for w in G.adjacent[v]:\n\
    \            if not X[w]:\n                X[w]=True\n                Y.append(w)\n\
    \                if __f__(w,k-1):\n                    return True\n         \
    \       X[w]=False\n                _=Y.pop()\n\n        return False\n    #------------------------------\n\
    \    if __f__(A,N-1):\n        return list(Y)\n    else:\n        return None\n\
    \n#\u30AF\u30EA\u30FC\u30AF\ndef Clique(G: Graph, calc, merge, unit, empty=False):\n\
    \    \"\"\"\n    \u30B0\u30E9\u30D5 G \u306B\u5BFE\u3059\u308B Clique C \u5168\
    \u3066\u306B\u5BFE\u3059\u308B calc (C) \u3092\u8A08\u7B97\u3057, merge \u3067\
    \u30DE\u30FC\u30B8\u3059\u308B.\n\n    G: Graph\n    calc: calc(C) Clique \u3067\
    \u3042\u308B\u90E8\u5206\u96C6\u5408 C \u306B\u5BFE\u3059\u308B\u5024\n    merge:\
    \ merge(x,y) x,y \u306E\u30DE\u30FC\u30B8\u306E\u65B9\u6CD5\n    empty: \u7A7A\
    \u96C6\u5408\u3092 Clique \u3068\u3059\u308B\u304B?\n\n    \u8A08\u7B97\u91CF\
    : O(2^{sqrt(2M)} N)\n    \"\"\"\n\n    N=G.order(); M=G.size()\n    deg=[G.degree(v)\
    \ for v in range(N)]; V=[1]*N\n\n    M_sqrt=0\n    while (M_sqrt+1)**2<=2*M:\n\
    \        M_sqrt+=1\n\n    X=unit\n    while True:\n        A=[]\n        for u\
    \ in range(N):\n            if V[u] and deg[u]<M_sqrt:\n                for v\
    \ in range(N):\n                    if u!=v and V[v] and G.edge_exist(u,v):\n\
    \                        A.append(v)\n                A.append(u)\n          \
    \      break\n\n        if not A:\n            break\n\n        K=len(A)-1\n \
    \       bit=[0]*K\n        for i in range(K):\n            for j in range(i):\n\
    \                if not G.edge_exist(A[i],A[j]):\n                    bit[i]|=1<<j\n\
    \                    bit[j]|=1<<i\n\n        for S in range(1<<K):\n         \
    \   flag=1\n            for i in range(K):\n                if (S>>i)&1:\n   \
    \                 flag&=(S&bit[i]==0)\n\n            if flag:\n              \
    \  B=[A[-1]]\n                for i in range(K):\n                    if (S>>i)&1:\n\
    \                        B.append(A[i])\n\n                X=merge(X,calc(B))\n\
    \n        V[A[-1]]=0; deg[A[-1]]=0\n        for v in range(N):\n            if\
    \ A[-1]!=v and V[v] and G.edge_exist(A[-1],v):\n                deg[v]-=1\n\n\
    \    A=[]\n    for u in range(N):\n        if V[u]:\n            A.append(u)\n\
    \n    K=len(A)\n    bit=[0]*K\n    for i in range(K):\n        for j in range(i):\n\
    \            if not G.edge_exist(A[i], A[j]):\n                bit[i]|=1<<j\n\
    \                bit[j]|=1<<i\n\n    for S in range(1<<K):\n        flag=1\n \
    \       for i in range(K):\n            if (S>>i)&1:\n                flag&=(S&bit[i]==0)\n\
    \n        if flag and (S or empty):\n            B=[]\n            for i in range(K):\n\
    \                if (S>>i)&1:\n                    B.append(A[i])\n\n        \
    \    X=merge(X,calc(B))\n\n    return X\n\n# \u4E09\u89D2\u5F62\ndef Triangle(G:\
    \ Graph , calc, merge, unit):\n    \"\"\"\n    calc: calc(i,j,k) 3\u9802\u70B9\
    \ i,j,k \u304B\u3089\u306A\u308B\u9802\u70B9\u306B\u5BFE\u3059\u308B\u5024\n \
    \   merge: merge(x,y) x,y \u306E\u30DE\u30FC\u30B8\u306E\u65B9\u6CD5\n    unit:\
    \ \u5358\u4F4D\u5143\n\n    \u8A08\u7B97\u91CF: O(M sqrt(2M))\n    \"\"\"\n\n\
    \    N=G.order()\n    A=[[] for _ in range(N)]\n\n    deg=G.degree; adj=G.adjacent\n\
    \    for i in range(N):\n        for j in adj[i]:\n            if (deg(i)>deg(j))\
    \ or (deg(i)==deg(j) and i>j):\n                A[i].append(j)\n\n    X=unit\n\
    \    used=[False]*N\n    for i in range(N):\n        for k in A[i]:\n        \
    \    used[k]=True\n\n        for j in A[i]:\n            for k in A[j]:\n    \
    \            if used[k]:\n                    X=merge(X,calc(i,j,k))\n       \
    \ for k in A[i]:\n            used[k]=False\n    return X\n\n#=================================================\n\
    #\u7279\u5225\u306A\u30B0\u30E9\u30D5\n#=================================================\n\
    #\u5B8C\u5168\u30B0\u30E9\u30D5\u306E\u4F5C\u6210\ndef Complete_Graph(N):\n  \
    \  \"\"\" N \u9802\u70B9\u306E\u5B8C\u5168\u30B0\u30E9\u30D5\u3092\u751F\u6210\
    \u3059\u308B. \"\"\"\n\n    G=Graph(N)\n    for u in range(N):\n        for v\
    \ in range(u+1,N):\n            G.add_edge(u,v)\n    return G\n\n#\u5B8C\u5168\
    2\u90E8\u30B0\u30E9\u30D5\ndef Complete_Bipartite_Graph(M,N):\n    \"\"\" M,N\
    \ \u9802\u70B9\u306E\u5B8C\u51682\u90E8\u30B0\u30E9\u30D5\u3092\u751F\u6210\u3059\
    \u308B. \"\"\"\n\n    G=Graph(M+N)\n\n    for a in range(M):\n        for b in\
    \ range(M,M+N):\n            G.add_edge(a,b)\n    return G\n\n#\u30B0\u30E9\u30D5\
    \u4F5C\u6210\ndef Making_Graph(N,E):\n    \"\"\" \u8FBA\u306E\u60C5\u5831 E \u304B\
    \u3089\u30B0\u30E9\u30D5\u3092\u751F\u6210\u3059\u308B. \"\"\"\n\n    G=Graph(N)\n\
    \    for e in E:\n        G.add_edge(*e)\n    return G\n\n#\u30DA\u30C6\u30EB\u30BB\
    \u30F3\u30B0\u30E9\u30D5\ndef Petersen_Graph(N=5,K=2):\n    \"\"\" (n,k) -\u578B\
    \u306E\u30DA\u30C6\u30EB\u30BB\u30F3\u30B0\u30E9\u30D5\u3092\u7D39\u4ECB\u3059\
    \u308B. \"\"\"\n\n    G=Graph(2*N)\n\n    for i in range(N):\n        G.add_edge(i,(i+1)%N)\n\
    \        G.add_edge(i,i+N)\n\n        j=(i+K)%N\n        G.add_edge(i+N,j+N)\n\
    \    return G\n\n#\u683C\u5B50\u30B0\u30E9\u30D5\ndef Grid_Graph(M, N):\n    \"\
    \"\" M x N \u30DE\u30B9\u306E\u30B0\u30E9\u30D5\u3092\u751F\u6210\u3059\u308B\
    .  \"\"\"\n\n    G=Graph(M*N)\n\n    for p in range(M*N):\n        if p%N!=N-1:\n\
    \            G.add_edge(p,p+1)\n        if p<(M-1)*N:\n            G.add_edge(p,p+N)\n\
    \    return G\n\n#\u30C8\u30FC\u30E9\u30B9\ndef Torus_Graph(M, N):\n    \"\"\"\
    \ M x N \u306E\u30C8\u30FC\u30E9\u30B9\u30B0\u30E9\u30D5\u3092\u751F\u6210\u3059\
    \u308B. \"\"\"\n\n    G=Graph(M*N)\n    for i in range(M):\n        for j in range(N):\n\
    \            p=i*N+j\n            q=i*N+(j+1)%N\n            r=((i+1)%M)*N+j\n\
    \n            G.add_edge(p,q)\n            G.add_edge(p,r)\n    return G\n\n#Path\u30B0\
    \u30E9\u30D5\ndef Path_Graph(N):\n    \"\"\" N \u9802\u70B9\u304B\u3089\u306A\u308B\
    \u30D1\u30B9\u30B0\u30E9\u30D5\u3092\u751F\u6210\u3059\u308B. \"\"\"\n\n    P=Graph(N)\n\
    \    for i in range(N-1):\n        P.add_edge(i,i+1)\n    return P\n\n#Cycle\u30B0\
    \u30E9\u30D5\ndef Cycle_Graph(N):\n    \"\"\" N \u9802\u70B9\u304B\u3089\u306A\
    \u308B\u30B5\u30A4\u30AF\u30EB\u30B0\u30E9\u30D5\u3092\u751F\u6210\u3059\u308B\
    . \"\"\"\n\n    C=Graph(N)\n    for i in range(N):\n        C.add_edge(i, (i+1)%N)\n\
    \    return C\n\n#Circulant \u30B0\u30E9\u30D5\ndef Circulant_Graph(N, *J):\n\
    \    \"\"\" N \u9802\u70B9, J \u30B8\u30E3\u30F3\u30D7\u306E\u5DE1\u56DE\u30B0\
    \u30E9\u30D5\u3092\u751F\u6210\u3059\u308B.\"\"\"\n\n    C=Graph(N)\n    for j\
    \ in J:\n        for v in range(N):\n            w=(v+j)%N\n            C.add_edge(v,w)\n\
    \    return C\n\n#Star\u30B0\u30E9\u30D5\ndef Star_Graph(N):\n    \"\"\" \u8449\
    \u3092 N \u500B\u6301\u3064\u30B9\u30BF\u30FC\u30B0\u30E9\u30D5\u3092\u751F\u6210\
    \u3059\u308B. \"\"\"\n\n    S=Graph(N+1)\n    for i in range(1,N+1):\n       \
    \ S.add_edge(0,i)\n    return S\n\n#Wheel\u30B0\u30E9\u30D5\ndef Wheel_Graph(N):\n\
    \    \"\"\" \u5916\u5468\u90E8\u304C N \u9802\u70B9\u304B\u3089\u306A\u308B\u8ECA\
    \u8F2A\u30B0\u30E9\u30D5\u3092\u751F\u6210\u3059\u308B. \"\"\"\n\n    W=Graph(N+1)\n\
    \    for i in range(1,N+1):\n        W.add_edge(0,i)\n\n    for j in range(N):\n\
    \        W.add_edge(j%N+1,(j+1)%N+1)\n    return W\n\n#\u9A0E\u58EB\u5DE1\u56DE\
    \u30B0\u30E9\u30D5\ndef Knight_Tour_Graph(M, N, s=1, t=2):\n    \"\"\" M x N \u306E\
    \u30C1\u30A7\u30B9\u76E4\u306B (s,t)-Knight \u304C\u79FB\u52D5\u3059\u308B\u30B0\
    \u30E9\u30D5\u3092\u751F\u6210\u3059\u308B.\n    \"\"\"\n\n    G=Graph(M*N)\n\n\
    \    H=[(s,t),(t,s),(s,-t),(t,-s)]\n\n    for a,b in H:\n        for i in range(max(0,-a),min(M,M-a)):\n\
    \            for j in range(max(0,-b),min(N,N-b)):\n                p=i*N+j; q=(i+a)*N+(j+b)\n\
    \                G.add_edge(p,q)\n    return G\n\n#\u5B8C\u5168k\u5206\u6728\n\
    def Complete_Kary_Tree(n,k=2):\n    \"\"\" \u6DF1\u3055\u304C n \u306E\u5B8C\u5168\
    \ k \u5206\u6728\u3092\u751F\u6210\u3059\u308B. \"\"\"\n\n    m=(k**n-1)//(k-1)\n\
    \    T=Graph(m)\n\n    for i in range(1,m):\n        T.add_edge((i-1)//k,i)\n\
    \    return T\n\n#---------------------------------------\ndef One_Point_Distance(G,From,with_path=False):\n\
    \    \"\"\" \u5358\u4E00\u59CB\u70B9 From \u304B\u3089\u306E\u8DDD\u96E2\u3092\
    \u6C42\u3081\u308B.\n\n    G: \u30B0\u30E9\u30D5\n    From: \u59CB\u70B9\n   \
    \ with_path: \u6700\u77ED\u8DEF\u3082\u542B\u3081\u3066\u51FA\u529B\u3059\u308B\
    \u304B?\n\n    (\u51FA\u529B\u306E\u7D50\u679C)\n    with_path=True \u2192 (\u8DDD\
    \u96E2, \u6700\u77ED\u7D4C\u8DEF\u306E\u8FBF\u308B\u969B\u306E\u524D\u306E\u9802\
    \u70B9)\n    with_path=False \u2192 \u8DDD\u96E2\n    \"\"\"\n\n    from collections\
    \ import deque\n\n    N=G.vertex_count(); adj=G.adjacent\n    inf=float(\"inf\"\
    )\n    T=[inf]*N; T[From]=0\n\n    if with_path:\n        Prev=[None]*N\n\n  \
    \  Q=deque([From])\n\n    while Q:\n        u=Q.popleft()\n\n        for v in\
    \ adj[u]:\n            if T[v]==inf:\n                T[v]=T[u]+1\n          \
    \      Q.append(v)\n\n                if with_path:\n                    Prev[v]=u\n\
    \n    if with_path:\n        return (T,Prev)\n    else:\n        return  T\n\n\
    #Warshall\u2013Floyd\ndef Warshall_Floyd(G):\n    \"\"\" Warshall-Floyd \u6CD5\
    \u3092\u7528\u3044\u3066, \u5168\u70B9\u9593\u8DDD\u96E2\u3092\u6C42\u3081\u308B\
    .\n\n    \"\"\"\n\n    N=G.vertex_count(); inf=float(\"inf\"); adj=G.adjacent\n\
    \    T=[[0]*N for _ in range(N)]\n\n    for u in range(N):\n        Tu=T[u]\n\
    \        for v in range(N):\n            if v==u:\n                T[u][v]=0\n\
    \            elif v in adj[u]:\n                T[u][v]=1\n            else:\n\
    \                T[u][v]=float(\"inf\")\n\n    for u in range(N):\n        Tu=T[u]\n\
    \        for v in range(N):\n            Tv=T[v]\n            for w in range(N):\n\
    \                Tv[w]=min(Tv[w],Tv[u]+Tu[w])\n\n    return T\n#==========\n#\
    \ \u30B0\u30E9\u30D5\u306E\u8D70\u67FB\n#==========\ndef Depth_First_Search_yielder(G):\n\
    \    \"\"\" \u6DF1\u3055\u512A\u5148\u63A2\u7D22\u3092\u884C\u3046.\n\n    [Input]\n\
    \    G: \u30B0\u30E9\u30D5\n\n    [Output]\n    (-1, v, 1): v \u304C\u63A2\u7D22\
    \u958B\u59CB\u306E\u9802\u70B9\u3067\u3042\u308B.\n    (u,v,1): u \u304B\u3089\
    \ v \u3078\u5411\u304B\u3046\u8FBA\u3067, DFS \u6728\u3067\u8449\u306B\u9032\u3080\
    \u5411\u304D\u306B\u306A\u308B\u8FBA\n    (u,v,0): u \u304B\u3089 v \u3078\u5411\
    \u304B\u3046\u8FBA\u3067\u5F8C\u9000\u8FBA (DFS \u6728\u306B\u306F\u4E0D\u63A1\
    \u7528)\n    (u,v,-1): u \u304B\u3089 v \u3078\u5411\u304B\u3046\u8FBA\u3067,\
    \ DFS \u6728\u3067\u306F\u6839\u306B\u9032\u3080\u5411\u304D\u306B\u306A\u308B\
    \u8FBA\n    (u,-1,-1): u \u304B\u3089\u59CB\u307E\u3063\u305F DFS \u304C\u7D42\
    \u4E86\n    \"\"\"\n\n    from collections import deque\n\n    N=G.vertex_count();\
    \ adj=[list(a) for a in G.adjacent]\n    T=[0]*N; R=[0]*N; parent=[-1]*N\n\n \
    \   for x in range(N):\n        if T[x]==0:\n            S=deque([x])\n\n    \
    \        yield (-1, x, 1)\n            while S:\n                x=S.pop()\n \
    \               T[x]=1\n\n                while R[x]<len(adj[x]):\n          \
    \          y=adj[x][R[x]]\n                    R[x]+=1\n\n                   \
    \ if T[y]==0:\n                        S.append(x); S.append(y)\n            \
    \            parent[y]=x\n                        yield (x,y,1)\n            \
    \            break\n                    else:\n                        yield (x,y,0)\n\
    \                else:\n                    yield (x, parent[x], -1)\n       \
    \     yield (x, -1, -1)\n"
  dependsOn: []
  isVerificationFile: false
  path: Graph/Graph.py
  requiredBy: []
  timestamp: '2022-09-28 11:01:42+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Graph/Graph.py
layout: document
redirect_from:
- /library/Graph/Graph.py
- /library/Graph/Graph.py.html
title: Graph/Graph.py
---
