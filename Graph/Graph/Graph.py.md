---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test_verify/yosupo_library_checker/Graph/Two_Edge_Connected_Components.test.py
    title: test_verify/yosupo_library_checker/Graph/Two_Edge_Connected_Components.test.py
  - icon: ':heavy_check_mark:'
    path: test_verify/yosupo_library_checker/Graph/Undirected_Eulerian_Trail.test.py
    title: test_verify/yosupo_library_checker/Graph/Undirected_Eulerian_Trail.test.py
  - icon: ':heavy_check_mark:'
    path: test_verify/yosupo_library_checker/Graph/Undirected_Find_Cycle.test.py
    title: test_verify/yosupo_library_checker/Graph/Undirected_Find_Cycle.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.2/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.2/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class Graph:\n    __slots__ = (\"adjacent\", \"deg\", \"__size\")\n\n   \
    \ #\u5165\u529B\u5B9A\u7FA9\n    def __init__(self, N = 0):\n        \"\"\" N\
    \ \u9802\u70B9\u306E\u7A7A\u30B0\u30E9\u30D5 (\u591A\u91CD\u8FBA\u306A\u3057)\
    \ \u3092\u751F\u6210\u3059\u308B.\"\"\"\n\n        self.adjacent = [[] for _ in\
    \ range(N)]\n        self.deg = [0] * N\n        self.__size = 0\n\n    #\u9802\
    \u70B9\u306E\u8FFD\u52A0\n    def add_vertex(self):\n        \"\"\" \u9802\u70B9\
    \u3092\u8FFD\u52A0\u3059\u308B.\n\n        \"\"\"\n\n        self.adjacent.append([])\n\
    \        self.deg.append(0)\n\n        return self.order() - 1\n\n    def add_vertices(self,\
    \ k):\n        \"\"\" \u9802\u70B9\u3092 k \u500B\u8FFD\u52A0\u3059\u308B.\n\n\
    \        k: int\n        \"\"\"\n\n        n = self.order()\n\n        self.adjacent.extend([[]\
    \ for _ in range(k)])\n        self.deg.extend([0] * k)\n\n        return list(range(n,\
    \ n + k))\n\n    #\u8FBA\u306E\u8FFD\u52A0\n    def add_edge(self, u, v, label\
    \ = None):\n        \"\"\" \u7121\u5411\u8FBA uv \u3092\u52A0\u3048\u308B\"\"\"\
    \n\n        self.adjacent[u].append((v, label))\n        if u != v:\n        \
    \    self.adjacent[v].append((u, label))\n\n        self.deg[u] += 1\n       \
    \ self.deg[v] += 1\n        self.__size += 1\n\n    #Walk\u306E\u8FFD\u52A0\n\
    \    def add_walk(self, *walk):\n        \"\"\" walk=(w[0],...,w[n-1]) \u306B\u5BFE\
    \u3057\u3066, n-1 \u672C\u306E\u8FBA w[i]w[i+1] \u3092\u52A0\u3048\u308B.\"\"\"\
    \n        for i in range(len(walk) - 1):\n            self.add_edge(walk[i], walk[i\
    \ + 1])\n\n    #Cycle\u306E\u8FFD\u52A0\n    def add_cycle(self, *cycle):\n  \
    \      \"\"\" cycle=(c[0], ..., c[n-1]) \u3092\u52A0\u3048\u308B. \"\"\"\n   \
    \     self.add_walk(*cycle)\n        self.add_edge(cycle[-1], cycle[0])\n\n  \
    \  def partner_yield(self, v):\n        for w, _ in self.adjacent[v]:\n      \
    \      yield w\n\n    def partner(self, v):\n        return [w for w, _ in self.adjacent[v]]\n\
    \n    def partner_with_label_yield(self, v):\n        yield from self.adjacent[v]\n\
    \n    #\u8FD1\u508D\n    def neighborhood(self, v):\n        \"\"\" \u9802\u70B9\
    \ v \u306E\u8FD1\u508D\u3092\u6C42\u3081\u308B. \"\"\"\n        return set(self.partner_yield(v))\n\
    \n    #\u6B21\u6570\n    def degree(self, v):\n        \"\"\" \u9802\u70B9 v \u306E\
    \u6B21\u6570\u3092\u6C42\u3081\u308B. \"\"\"\n        return self.deg[v]\n\n \
    \   #\u9802\u70B9\u6570\n    def vertex_count(self):\n        \"\"\" \u30B0\u30E9\
    \u30D5\u306E\u9802\u70B9\u6570 (\u4F4D\u6570) \u3092\u51FA\u529B\u3059\u308B.\
    \ \"\"\"\n        return len(self.adjacent)\n\n    def order(self):\n        \"\
    \"\" \u30B0\u30E9\u30D5\u306E\u4F4D\u6570 (\u9802\u70B9\u6570) \u3092\u51FA\u529B\
    \u3059\u308B. \"\"\"\n        return len(self.adjacent)\n\n    #\u8FBA\u6570\n\
    \    def edge_count(self):\n        \"\"\" \u8FBA\u306E\u672C\u6570 (\u30B5\u30A4\
    \u30BA) \u3092\u51FA\u529B\u3059\u308B.\"\"\"\n\n        return self.__size\n\n\
    \    def size(self):\n        \"\"\" \u30B5\u30A4\u30BA (\u8FBA\u306E\u672C\u6570\
    ) \u3092\u51FA\u529B\u3059\u308B. \"\"\"\n\n        return self.__size\n\n   \
    \ #\u9802\u70B9v\u3092\u542B\u3080\u9023\u7D50\u6210\u5206\n    def connected_component(self,\
    \ v):\n        \"\"\" \u9802\u70B9 v \u3092\u542B\u3080\u9023\u7D50\u6210\u5206\
    \u3092\u51FA\u529B\u3059\u308B.\"\"\"\n\n        N = self.order()\n\n        stack\
    \ = [v]\n        comp = [0] * N; comp[v] = 1\n        while stack:\n         \
    \   x = stack.pop()\n            for y in self.partner_yield(x):\n           \
    \     if comp[y] == 0:\n                    comp[y] = 1\n                    stack.append(y)\n\
    \n        return [x for x in range(N) if comp[x]]\n\n    #\u8DDD\u96E2\n    def\
    \ distance(self, u, v, default = -1):\n        \"\"\" 2\u9802\u70B9 u,v \u9593\
    \u306E\u8DDD\u96E2\u3092\u6C42\u3081\u308B.\"\"\"\n\n        if u == v:\n    \
    \        return 0\n\n        from collections import deque\n\n        N = self.order()\n\
    \        dist = [-1] * N; dist[u]=0\n\n        queue = deque([u])\n        while\
    \ queue:\n            x = queue.popleft()\n            for y in self.partner_yield(x):\n\
    \                if dist[y] == -1:\n                    dist[y] = dist[x] + 1\n\
    \                    queue.append(y)\n\n                    if y == v:\n     \
    \                   return dist[v]\n\n        return default\n\n    #\u3042\u308B\
    1\u70B9\u304B\u3089\u306E\u8DDD\u96E2\n    def distance_all(self, u, default =\
    \ -1):\n        \"\"\" \u9802\u70B9 u \u304B\u3089\u306E\u8DDD\u96E2\u3092\u6C42\
    \u3081\u308B.\"\"\"\n\n        from collections import deque\n\n        N = self.order()\n\
    \        dist = [-1] * N; dist[u]=0\n\n        queue = deque([u])\n        while\
    \ queue:\n            x = queue.popleft()\n            for y in self.partner_yield(x):\n\
    \                if dist[y] == -1:\n                    dist[y] = dist[x] + 1\n\
    \                    queue.append(y)\n\n        return [dist[x] if dist[x] !=\
    \ -1 else default for x in range(N)]\n\n    #\u6700\u77ED\u8DEF\n    def shortest_path(self,\
    \ u, v):\n        \"\"\" u \u304B\u3089 v \u3078\u306E\u6700\u77ED\u8DEF\u3092\
    \u6C42\u3081\u308B (\u5B58\u5728\u3057\u306A\u3044\u5834\u5408\u306F None). \"\
    \"\"\n\n        if u == v:\n            return [u]\n\n        from collections\
    \ import deque\n\n        prev = [-1] * self.order()\n        prev[u] = u\n\n\
    \        queue = deque([u])\n        while queue:\n            x = queue.popleft()\n\
    \            for y in self.partner_yield(x):\n                if prev[y] != -1:\n\
    \                    continue\n\n                prev[y] = x\n               \
    \ queue.append(y)\n\n                if y != v:\n                    continue\n\
    \n                path = [v]\n                a = v\n                while a !=\
    \ u:\n                    a = prev[a]\n                    path.append(a)\n  \
    \              return path[::-1]\n        return None\n\n    def edge_yielder(self):\n\
    \        for u in range(self.order()):\n            for v in self.partner_yield(u):\n\
    \                if u <= v:\n                    yield (u, v)\n\n    def edge_yielder_with_label(self):\n\
    \        for u in range(self.order()):\n            for v, label in self.partner_with_label_yield(u):\n\
    \                if u <= v:\n                    yield (u, v, label)\n\n#==========\n\
    #\u30B0\u30E9\u30D5\u306E\u751F\u6210\n#==========\n#\u88DC\u30B0\u30E9\u30D5\u306E\
    \u4F5C\u6210\ndef Complement_Graph(G):\n    \"\"\" \u30B0\u30E9\u30D5 G \u306E\
    \u88DC\u30B0\u30E9\u30D5\u3092\u6C42\u3081\u308B.\"\"\"\n    pass\n\n# N \u9802\
    \u70B9\u306E\u30E9\u30F3\u30C0\u30E0\u30B0\u30E9\u30D5\ndef Random_Graph(N, p=0.5,\
    \ self_loop=False, seed=None):\n    pass\n\ndef Directed_Sum(*Graphs):\n    total_order\
    \ = sum(G.order() for G in Graphs)\n    order_offset = 0\n\n    H = Graph(total_order)\n\
    \    for G in Graphs:\n        for u, v, t in G.edge_yielder():\n            H.add_edge(u\
    \ + order_offset, v + order_offset, t)\n        order_offset += G.order()\n\n\
    \    return H\n\n#==========\n#\u9023\u7D50\u30B0\u30E9\u30D5?\ndef Is_Connected(G:\
    \ Graph):\n    \"\"\" G \u306F\u9023\u7D50\u30B0\u30E9\u30D5 ?\n\n    Args:\n\
    \        G (Graph)\n    \"\"\"\n\n    return (G.order() == 0) or all(d >= 0 for\
    \ d in G.distance_all(0))\n\n#=====\n#\u68EE?\ndef Is_Forest(G: Graph):\n    \"\
    \"\" \u68EE\u304B\u3069\u3046\u304B\u5224\u5B9A\u3059\u308B. \"\"\"\n\n    return\
    \ G.order() == G.size() + Connected_Component_Number(G)\n\n#\u6728?\ndef Is_Tree(G:\
    \ Graph):\n    \"\"\" \u6728\u304B\u3069\u3046\u304B\u5224\u5B9A\u3059\u308B.\
    \ \"\"\"\n    return (G.size() == G.order() - 1) and Is_Connected(G)\n\n#\u6728\
    \u306E\u76F4\u5F84\ndef Tree_Diameter(T: Graph, Mode = False):\n    \"\"\" \u6728\
    \ T \u306E\u76F4\u5F84\u3092\u6C42\u3081\u308B.\n\n    T: \u6728\n\n    (\u51FA\
    \u529B\u306E\u7D50\u679C)\n    Mode=True \u2192 (\u76F4\u5F84, (\u76F4\u5F84\u3092\
    \u6210\u3059\u7AEF\u70B91, \u76F4\u5F84\u3092\u6210\u3059\u7AEF\u70B92))\n   \
    \ Mode=False \u2192 \u76F4\u5F84\n    \"\"\"\n\n    def bfs(x):\n        dist\
    \ = [-1] * T.order(); dist[x] = 0\n        stack = [x]\n        while stack:\n\
    \            u = stack.pop()\n\n            for v in T.neighborhood(u):\n    \
    \            if dist[v] == -1:\n                    dist[v] = dist[u] + 1\n  \
    \                  stack.append(v)\n\n        y = max(range(T.order()), key =\
    \ lambda x: dist[x])\n        return y, dist[y]\n\n    u, _ = bfs(0)\n    v, d\
    \ = bfs(u)\n\n    if Mode:\n        return (d, (u, v))\n    else:\n        return\
    \ d\n\n#\u9023\u7D50\u6210\u5206\u306B\u5206\u89E3\ndef Connected_Component_Decomposition(G:\
    \ Graph):\n    \"\"\" \u9023\u7D50\u6210\u5206\u6BCE\u306B\u5206\u89E3\u3059\u308B\
    .\n\n    G: Graph\n    \"\"\"\n\n\n    group = [-1] * G.order()\n    comps = []\n\
    \n    def dfs(start, g):\n        stack = [start]\n        group[start] = g\n\
    \        comp = []\n\n        while stack:\n            x = stack.pop()\n    \
    \        comp.append(x)\n            for y in G.partner_yield(x):\n          \
    \      if group[y] == -1:\n                    group[y] = g\n                \
    \    stack.append(y)\n        comps.append(comp)\n\n    g = 0\n    for x in range(G.order()):\n\
    \        if group[x] == -1:\n            dfs(x, g)\n            g += 1\n\n   \
    \ return { 'components': comps, 'group': group }\n\n#\u9023\u7D50\u6210\u5206\u306E\
    \u500B\u6570\ndef Connected_Component_Number(G: Graph):\n    \"\"\" \u9023\u7D50\
    \u6210\u5206\u306E\u500B\u6570\u3092\u6C42\u3081\u308B. \"\"\"\n\n    seen = [False]\
    \ * G.order()\n\n    def bfs(start):\n        seen[start] = True\n        stack\
    \ = [start]\n\n        while stack:\n            x = stack.pop()\n           \
    \ for y in G.neighborhood(x):\n                if not seen[y]:\n             \
    \       seen[y] = True\n                    stack.append(y)\n\n    count = 0\n\
    \    for x in range(G.order()):\n        if not seen[x]:\n            count +=\
    \ 1\n            bfs(x)\n\n    return count\n\n#2\u90E8\u30B0\u30E9\u30D5?\ndef\
    \ Is_Bipartite_Graph(G: Graph):\n    \"\"\" 2\u90E8\u30B0\u30E9\u30D5\u304B\u3069\
    \u3046\u304B\u3092\u5224\u5B9A\u3059\u308B. \"\"\"\n\n    seen = [0] * G.order()\n\
    \n    for v in range(G.order()):\n        if seen[v] != 0:\n            continue\n\
    \n        seen[v] = 1\n        stack = [v]\n        while stack:\n           \
    \ x = stack.pop()\n            for y in G.neighborhood(x):\n                if\
    \ seen[y]==0:\n                    seen[y] = -seen[x]\n                    stack.append(y)\n\
    \                elif seen[y] == seen[x]:\n                    return False\n\
    \    return True\n\n#2\u90E8\u30B0\u30E9\u30D5\u306E\u90E8\u96C6\u5408\u306B\u5206\
    \u5272\ndef Bipartite_Separate(G: Graph):\n    \"\"\" 2\u90E8\u30B0\u30E9\u30D5\
    \u306E\u9802\u70B9\u3092\u90E8\u96C6\u5408\u306B\u5206\u5272\u3059\u308B. \"\"\
    \"\n\n    N = G.order()\n    color = [0] * N\n\n    separates = []\n    for v\
    \ in range(N):\n        if color[v] != 0:\n            continue\n\n        color[v]\
    \ = 1\n        S = [v]\n        A = []; B = []\n        while S:\n           \
    \ u = S.pop()\n\n            if color[u]==1:\n                A.append(u)\n  \
    \          else:\n                B.append(u)\n\n            for w in G.partner_yield(u):\n\
    \                if color[w] == 0:\n                    color[w] = -color[u]\n\
    \                    S.append(w)\n                elif color[w] == color[u]:\n\
    \                    return None\n        separates.append((A,B))\n\n    return\
    \ separates\n\n#\u30CF\u30DF\u30EB\u30C8\u30F3\u30B0\u30E9\u30D5?\ndef Is_Hamiltonian_Graph(G):\n\
    \    \"\"\" \u30CF\u30DF\u30EB\u30C8\u30F3\u30B0\u30E9\u30D5 (\u5168\u3066\u306E\
    \u9802\u70B9\u30921\u56DE\u305A\u3064\u901A\u308B\u30B5\u30A4\u30AF\u30EB\u3092\
    \u542B\u3080\u30B0\u30E9\u30D5) \u304B\u3069\u3046\u304B\u3092\u5224\u5B9A\u3059\
    \u308B.\n\n    \"\"\"\n    pass\n\n#\u30CF\u30DF\u30EB\u30C8\u30F3\u3092\u63A2\
    \u3059.\ndef Find_Hamiltonian_Graph(G):\n    pass\n\n#\u30AF\u30EA\u30FC\u30AF\
    \ndef Clique(G: Graph, calc, merge, unit, empty = False):\n    \"\"\"\n    \u30B0\
    \u30E9\u30D5 G \u306B\u5BFE\u3059\u308B Clique C \u5168\u3066\u306B\u5BFE\u3059\
    \u308B calc(C) \u3092\u8A08\u7B97\u3057, merge \u3067\u30DE\u30FC\u30B8\u3059\u308B\
    .\n\n    G: Graph\n    calc: calc(C) Clique \u3067\u3042\u308B\u90E8\u5206\u96C6\
    \u5408 C \u306B\u5BFE\u3059\u308B\u5024\n    merge: merge(x,y) x,y \u306E\u30DE\
    \u30FC\u30B8\u306E\u65B9\u6CD5\n    empty: \u7A7A\u96C6\u5408\u3092 Clique \u3068\
    \u3059\u308B\u304B?\n\n    \u8A08\u7B97\u91CF: O(2^{sqrt(2M)} N)\n    \"\"\"\n\
    \n    N=G.order(); M=G.size()\n    deg=[G.degree(v) for v in range(N)]; V=[1]*N\n\
    \n    M_sqrt=0\n    while (M_sqrt+1)**2<=2*M:\n        M_sqrt+=1\n\n    F = [[False]\
    \ * N for _ in range(N)]\n    for u, v in G.edge_yielder():\n        F[u][v] =\
    \ F[v][u] = True\n\n    X=unit\n    while True:\n        A=[]\n        for u in\
    \ range(N):\n            if V[u] and deg[u]<M_sqrt:\n                for v in\
    \ range(N):\n                    if u!=v and V[v] and F[u][v]:\n             \
    \           A.append(v)\n                A.append(u)\n                break\n\n\
    \        if not A:\n            break\n\n        K=len(A)-1\n        bit=[0]*K\n\
    \        for i in range(K):\n            for j in range(i):\n                if\
    \ not F[A[i]][A[j]]:\n                    bit[i]|=1<<j\n                    bit[j]|=1<<i\n\
    \n        for S in range(1<<K):\n            flag=1\n            for i in range(K):\n\
    \                if (S>>i)&1:\n                    flag&=(S&bit[i]==0)\n\n   \
    \         if flag:\n                B=[A[-1]]\n                for i in range(K):\n\
    \                    if (S>>i)&1:\n                        B.append(A[i])\n\n\
    \                X=merge(X,calc(B))\n\n        V[A[-1]]=0; deg[A[-1]]=0\n    \
    \    for v in range(N):\n            if A[-1]!=v and V[v] and F[A[-1]][v]:\n \
    \               deg[v]-=1\n\n    A=[]\n    for u in range(N):\n        if V[u]:\n\
    \            A.append(u)\n\n    K=len(A)\n    bit=[0]*K\n    for i in range(K):\n\
    \        for j in range(i):\n            if not F[A[i]][A[j]]:\n             \
    \   bit[i]|=1<<j\n                bit[j]|=1<<i\n\n    for S in range(1<<K):\n\
    \        flag=1\n        for i in range(K):\n            if (S>>i)&1:\n      \
    \          flag&=(S&bit[i]==0)\n\n        if flag and (S or empty):\n        \
    \    B=[]\n            for i in range(K):\n                if (S>>i)&1:\n    \
    \                B.append(A[i])\n\n            X=merge(X,calc(B))\n\n    return\
    \ X\n\n# \u4E09\u89D2\u5F62\ndef Triangle(G: Graph, calc, merge, unit):\n    \"\
    \"\"\n    calc: calc(i,j,k) 3\u9802\u70B9 i,j,k \u304B\u3089\u306A\u308B\u9802\
    \u70B9\u306B\u5BFE\u3059\u308B\u5024\n    merge: merge(x,y) x,y \u306E\u30DE\u30FC\
    \u30B8\u306E\u65B9\u6CD5\n    unit: \u5358\u4F4D\u5143\n\n    \u8A08\u7B97\u91CF\
    : O(M sqrt(2M))\n    \"\"\"\n\n    N=G.order()\n    A=[[] for _ in range(N)]\n\
    \n    deg=G.degree\n    for i in range(N):\n        for j in G.partner_yield(i):\n\
    \            if (deg(i)>deg(j)) or (deg(i)==deg(j) and i>j):\n               \
    \ A[i].append(j)\n\n    X=unit\n    used=[False]*N\n    for i in range(N):\n \
    \       for k in A[i]:\n            used[k]=True\n\n        for j in A[i]:\n \
    \           for k in A[j]:\n                if used[k]:\n                    X=merge(X,calc(i,j,k))\n\
    \        for k in A[i]:\n            used[k]=False\n    return X\n\n#=================================================\n\
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
    \    return T\n\n#==========\n# \u30B0\u30E9\u30D5\u306E\u8D70\u67FB\n#==========\n\
    def Depth_First_Search_yielder(G):\n    \"\"\" \u6DF1\u3055\u512A\u5148\u63A2\u7D22\
    \u3092\u884C\u3046.\n\n    [Input]\n    G: \u30B0\u30E9\u30D5\n\n    [Output]\n\
    \    (-1, v, 1): v \u304C\u63A2\u7D22\u958B\u59CB\u306E\u9802\u70B9\u3067\u3042\
    \u308B.\n    (u,v,1): u \u304B\u3089 v \u3078\u5411\u304B\u3046\u8FBA\u3067, DFS\
    \ \u6728\u3067\u8449\u306B\u9032\u3080\u5411\u304D\u306B\u306A\u308B\u8FBA\n \
    \   (u,v,0): u \u304B\u3089 v \u3078\u5411\u304B\u3046\u8FBA\u3067\u5F8C\u9000\
    \u8FBA (DFS \u6728\u306B\u306F\u4E0D\u63A1\u7528)\n    (u,v,-1): u \u304B\u3089\
    \ v \u3078\u5411\u304B\u3046\u8FBA\u3067, DFS \u6728\u3067\u306F\u6839\u306B\u9032\
    \u3080\u5411\u304D\u306B\u306A\u308B\u8FBA\n    (u,-1,-1): u \u304B\u3089\u59CB\
    \u307E\u3063\u305F DFS \u304C\u7D42\u4E86\n    \"\"\"\n\n    from collections\
    \ import deque\n\n    N=G.vertex_count(); adj=[list(a) for a in G.adjacent]\n\
    \    T=[0]*N; R=[0]*N; parent=[-1]*N\n\n    for x in range(N):\n        if T[x]==0:\n\
    \            S=deque([x])\n\n            yield (-1, x, 1)\n            while S:\n\
    \                x=S.pop()\n                T[x]=1\n\n                while R[x]<len(adj[x]):\n\
    \                    y=adj[x][R[x]]\n                    R[x]+=1\n\n         \
    \           if T[y]==0:\n                        S.append(x); S.append(y)\n  \
    \                      parent[y]=x\n                        yield (x,y,1)\n  \
    \                      break\n                    else:\n                    \
    \    yield (x,y,0)\n                else:\n                    yield (x, parent[x],\
    \ -1)\n            yield (x, -1, -1)\n"
  dependsOn: []
  isVerificationFile: false
  path: Graph/Graph/Graph.py
  requiredBy: []
  timestamp: '2024-03-20 20:56:58+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test_verify/yosupo_library_checker/Graph/Undirected_Find_Cycle.test.py
  - test_verify/yosupo_library_checker/Graph/Two_Edge_Connected_Components.test.py
  - test_verify/yosupo_library_checker/Graph/Undirected_Eulerian_Trail.test.py
documentation_of: Graph/Graph/Graph.py
layout: document
title: Graph
---

## Outline

多重辺がない無向グラフ $G=(V,E)$ に対する様々なアルゴリズム

## Theory

無向グラフ $G=(V,E)$ に対して, $V$ の濃度を $G$ の位数 (Order), $E$ の濃度を $G$ のサイズ (Size) という.

## Contents

---

### Constructer

```Python
G=Graph(N=0)
```

* 位数 $N$ の空グラフ (edgeless graph) を生成する.

### add_vertex

```Python
G.add_vertex()
```

* $G$ に 1 頂点を追加する. 追加された頂点の番号を返り値とする.

### add_vertices

```Python
G.add_vertices(k)
```

* $G$ に $k$ 頂点を追加する. 追加された $k$ 個の頂点の番号のリストを返り値とする.

### add_edge

``` Python
G.add_edge(u,v)
```

* 無向辺 $uv$ を存在しないならば追加する.
* 返り値は, 元々辺 $uv$ が存在しないならば, 辺の番号 (0-indexed) を, 存在するならば $-1$ とする.

### remove_edge

``` Python
G.remove_edge(u,v)
```

* 辺 $uv$ が削除するならば, 辺 $uv$ を削除する.
