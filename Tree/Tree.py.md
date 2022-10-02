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
  code: "class Tree:\n    __slots__=(\"N\", \"index\", \"parent\", \"__mutable\",\n\
    \            \"root\", \"children\", \"depth\", \"tower\", \"upper_list\", \"\
    des_count\", \"preorder_number\",\n            \"euler_vertex\", \"euler_edge\"\
    , \"in_time\", \"out_time\", \"lca_dst\",\n            \"hld_hedge\")\n\n    def\
    \ __init__(self, N, index=0):\n        \"\"\" N \u9802\u70B9 (index, index+1,\
    \ ..., N-1+index) \u306E\u6839\u4ED8\u304D\u6728\u3092\u751F\u6210\u3059\u308B\
    . \"\"\"\n        self.N=N\n        self.index=index\n        self.parent=[-1]*(N+index)\n\
    \        self.__mutable=True\n\n    def vertex_exist(self, x):\n        \"\"\"\
    \ \u9802\u70B9 x \u304C\u5B58\u5728\u3059\u308B\u304B\u3069\u3046\u304B\u3092\u5224\
    \u5B9A\u3059\u308B. \"\"\"\n\n        return self.index<=x<self.index+self.N\n\
    \n    def __after_seal_check(self,*vertexes):\n        \"\"\" \u6728\u304C\u78BA\
    \u5B9A\u3057\u3066\u3044\u3066, vertexes \u306E\u9802\u70B9\u304C\u5B58\u5728\u3059\
    \u308B\u304B\u3069\u3046\u304B\u3092\u30C1\u30A7\u30C3\u30AF\u3059\u308B. \"\"\
    \"\n\n        if self.__mutable:\n            return False\n\n        for v in\
    \ vertexes:\n            if not self.vertex_exist(v):\n                return\
    \ False\n        return True\n\n    def is_mutable(self):\n        \"\"\" \u6728\
    \u304C\u78BA\u5B9A\u3057\u3066 [\u3044\u306A\u3044] \u304B\u3069\u3046\u304B\u3092\
    \u8FD4\u3059. \"\"\"\n        return self.__mutable\n\n    #\u8A2D\u5B9A\u30D1\
    \u30FC\u30C8\n    def root_set(self, root):\n        \"\"\" \u9802\u70B9 root\
    \ \u3092\u6839\u306B\u8A2D\u5B9A\u3059\u308B.\"\"\"\n\n        assert self.vertex_exist(root)\n\
    \        assert self.__mutable\n\n        self.root=root\n\n    def parent_set(self,x,y):\n\
    \        \"\"\" \u9802\u70B9 x \u306E\u89AA\u3092 y \u306B\u8A2D\u5B9A\u3059\u308B\
    .\"\"\"\n\n        assert self.vertex_exist(x)\n        assert self.vertex_exist(y)\n\
    \        assert self.__mutable\n\n        self.parent[x]=y\n\n    def child_set(self,\
    \ x, y):\n        \"\"\" \u9802\u70B9 x \u306E\u5B50\u306E\u4E00\u3064\u306B y\
    \ \u3092\u8A2D\u5B9A\u3059\u308B (\u9802\u70B9 x \u306E\u65B9\u304C\u89AA).\"\"\
    \"\n\n        assert self.vertex_exist(x)\n        assert self.vertex_exist(y)\n\
    \        assert self.__mutable\n\n        self.parent[y]=x\n\n    def seal(self):\n\
    \        \"\"\" \u6728\u306E\u60C5\u5831\u3092\u78BA\u5B9A\u3055\u305B\u308B (\u3053\
    \u308C\u4EE5\u964D, \u60C5\u5831\u306E\u5909\u66F4\u306F\u7981\u6B62).\"\"\"\n\
    \n        assert self.__mutable\n        assert hasattr(self, \"root\")\n\n  \
    \      a=self.index\n        b=self.index+self.N\n        C=[[] for _ in range(b)]\n\
    \n        p=self.parent\n        ve=self.vertex_exist\n        for i in range(a,b):\n\
    \            if i!=self.root:\n                assert ve(p[i])\n             \
    \   C[p[i]].append(i)\n\n        self.__mutable=False\n        self.children=C\n\
    \n    #\u30C7\u30FC\u30BF\u3092\u6C42\u3081\u308B.\n    def depth_search(self,\
    \ mode=True):\n        \"\"\" \u6728\u306E\u6DF1\u3055\u3092\u6C42\u3081\u308B\
    .\n\n        mode=True \u306A\u3089\u3070, \u5404\u9802\u70B9\u306E\u6DF1\u3055\
    \u304C\u8A18\u9332\u3055\u308C\u305F\u30EA\u30B9\u30C8\u3092\u8FD4\u3059.\"\"\"\
    \n\n        assert self.__after_seal_check()\n\n        if hasattr(self, \"depth\"\
    ):\n            if mode:\n                return self.depth\n            else:\n\
    \                return\n\n        from collections import deque\n        C=self.children\n\
    \        D=[-1]*(self.index+self.N)\n        E=[[] for _ in range(self.N)]\n\n\
    \        Q=deque([self.root])\n        D[self.root]=0\n        E[0]=[self.root]\n\
    \n        while Q:\n            x=Q.popleft()\n            d=D[x]\n          \
    \  for y in C[x]:\n                D[y]=d+1\n                E[d+1].append(y)\n\
    \                Q.append(y)\n\n        self.depth=D\n        self.tower=E\n\n\
    \        if mode:\n            return D\n\n    def vertex_depth(self, x):\n  \
    \      \"\"\" \u9802\u70B9 x \u306E\u6DF1\u3055\u3092\u6C42\u3081\u308B.\"\"\"\
    \n\n        assert self.__after_seal_check(x)\n\n        if not hasattr(self,\
    \ \"depth\"):\n            self.depth_search(mode=False)\n        return self.depth[x]\n\
    \n    def __upper_list(self):\n        assert self.__after_seal_check()\n\n  \
    \      if hasattr(self, \"upper_list\"):\n            return\n\n        if not\
    \ hasattr(self,\"depth\"):\n            self.depth_search(False)\n\n        b=max(self.depth).bit_length()\n\
    \        X=[[-1]*(self.index+self.N) for _ in range(b)]\n\n        Y=X[0]\n  \
    \      p=self.parent\n\n        for x in range(self.index,self.index+self.N):\n\
    \            if x!=self.root:\n                Y[x]=p[x]\n            else:\n\
    \                Y[x]=self.root\n\n        for k in range(1,b):\n            Y=X[k-1]\n\
    \            Z=X[k]\n\n            for x in range(self.index,self.index+self.N):\n\
    \                Z[x]=Y[Y[x]]\n        self.upper_list=X\n\n    def upper(self,\
    \ x, k, over=True):\n        \"\"\" \u9802\u70B9 x \u304B\u3089\u898B\u3066 k\
    \ \u500B\u89AA\u306E\u9802\u70B9\u3092\u6C42\u3081\u308B.\n\n        over: (\u9802\
    \u70B9 x \u306E\u6DF1\u3055)<k \u306E\u3068\u304D\u306B True \u306A\u3089\u3070\
    \u6839\u3092\u8FD4\u3057, False \u306A\u3089\u3070\u30A8\u30E9\u30FC\u3092\u5410\
    \u304F.\n        \"\"\"\n\n        assert self.__after_seal_check(x)\n       \
    \ assert 0<=k\n\n        if not hasattr(self,\"upper_list\"):\n            self.__upper_list()\n\
    \n        if self.vertex_depth(x)<k:\n            if over:\n                return\
    \ self.root\n            else:\n                raise ValueError\n\n        i=0\n\
    \        while k:\n            if k&1:\n                x=self.upper_list[i][x]\n\
    \            k>>=1\n            i+=1\n        return x\n\n    def lowest_common_ancestor_greedy(self,\
    \ x, y):\n        \"\"\"\u9802\u70B9 x, y \u306E\u6700\u5C0F\u5171\u901A\u5148\
    \u7956 (x,y\u306B\u5171\u901A\u3059\u308B\u5148\u7956\u3067\u6700\u3082\u6DF1\u3044\
    \u3082\u306E) \u3092 \"\u611A\u76F4\u306B\" \u6C42\u3081\u308B.\"\"\"\n\n    \
    \    assert self.__after_seal_check(x,y)\n        dx=self.vertex_depth(x); dy=self.vertex_depth(y)\n\
    \n        if dx<dy:\n            dx,dy=dy,dx\n            x,y=y,x\n\n        pa=self.parent\n\
    \        while dx>dy:\n            x=pa[x]\n            dx-=1\n\n        while\
    \ x!=y:\n            x=pa[x]\n            y=pa[y]\n\n        return x\n\n    def\
    \ __lca_prepare(self):\n        assert self.__after_seal_check()\n\n        N=self.N\n\
    \n        bit=((2*N-1)-1).bit_length()\n        D=[[0]*(2*N-1) for _ in range(bit)]\n\
    \n        self.euler_tour_vertex()\n        tour=self.euler_vertex\n        D[0]=tour.copy()\n\
    \        dep=self.depth_search(True)\n\n        for i in range(1, bit):\n    \
    \        shift=1<<i\n            tab=D[i]\n\n            for j in range(0, 2*N-1,\
    \ 2*shift):\n                t=min(j+shift, 2*N-1)\n                tab[t-1]=tour[t-1]\n\
    \n                for k in range(t-2, j-1, -1):\n                    if dep[tour[k]]<dep[tab[k+1]]:\n\
    \                        tab[k]=tour[k]\n                    else:\n         \
    \               tab[k]=tab[k+1]\n\n                if 2*N-1<=t:\n            \
    \        break\n\n                tab[t]=tour[t]\n                r=min(t+shift,\
    \ 2*N-1)\n\n                for k in range(t+1, r):\n                    if dep[tab[k-1]]<dep[tour[k]]:\n\
    \                        tab[k]=tab[k-1]\n                    else:\n        \
    \                tab[k]=tour[k]\n\n        self.lca_dst=D\n        return\n\n\
    \    def lowest_common_ancestor(self, x, y):\n        \"\"\"\u9802\u70B9 x, y\
    \ \u306E\u6700\u5C0F\u5171\u901A\u5148\u7956 (x,y\u306B\u5171\u901A\u3059\u308B\
    \u5148\u7956\u3067\u6700\u3082\u6DF1\u3044\u3082\u306E) \u3092 \"\u9AD8\u901F\u306B\
    \" \u6C42\u3081\u308B. \"\"\"\n\n        assert self.__after_seal_check(x,y)\n\
    \        if not hasattr(self, \"lca_dst\"):\n            self.__lca_prepare()\n\
    \n        a=self.in_time[x]; b=self.in_time[y]\n        if a>b:\n            x,y=y,x\n\
    \            a,b=b,a\n\n        if a==b:\n            return self.lca_dst[0][a]\n\
    \n        p=(a^b).bit_length()-1\n        tab=self.lca_dst[p]\n        u=tab[a];\
    \ v=tab[b]\n\n        return u if self.vertex_depth(u)<self.vertex_depth(v) else\
    \ v\n\n    def degree(self,v):\n        \"\"\" \u9802\u70B9 v \u306E\u6B21\u6570\
    \u3092\u6C42\u3081\u308B. \"\"\"\n\n        assert self.__after_seal_check(v)\n\
    \        if v==self.root:\n            return len(self.children[v])\n        else:\n\
    \            return len(self.children[v])+1\n\n    def diameter(self):\n     \
    \   \"\"\" \u6728\u306E\u76F4\u5F84\u3092\u6C42\u3081\u308B.\"\"\"\n\n       \
    \ assert self.__after_seal_check()\n\n        from collections import deque\n\
    \        def bfs(start):\n            X=[-1]*(self.index+self.N)\n           \
    \ Q=deque([start])\n            X[start]=0\n\n            pa=self.parent\n   \
    \         ch=self.children\n            while Q:\n                x=Q.popleft()\n\
    \n                if X[pa[x]]==-1:\n                    Q.append(pa[x])\n    \
    \                X[pa[x]]=X[x]+1\n\n                for y in ch[x]:\n        \
    \            if X[y]==-1:\n                        Q.append(y)\n             \
    \           X[y]=X[x]+1\n            y=max(range(self.index,self.index+self.N),\
    \ key=lambda x:X[x])\n            return y,X[y]\n\n        y,_=bfs(self.root)\n\
    \        z,d=bfs(y)\n        return d,(y,z)\n\n    def path(self, u, v, faster=False):\n\
    \        \"\"\" \u9802\u70B9 u, v \u9593\u306E\u30D1\u30B9\u3092\u6C42\u3081\u308B\
    . \"\"\"\n\n        assert self.__after_seal_check(u,v)\n\n        if faster:\n\
    \            w=self.lowest_common_ancestor(u,v)\n        else:\n            w=self.lowest_common_ancestor_greedy(u,v)\n\
    \n        pa=self.parent\n        X=[u]\n        while u!=w:\n            u=pa[u]\n\
    \            X.append(u)\n\n        Y=[v]\n        while v!=w:\n            v=pa[v]\n\
    \            Y.append(v)\n        return X+Y[-2::-1]\n\n    def is_parent(self,\
    \ u, v):\n        \"\"\" u \u306F v \u306E\u89AA\u304B? \"\"\"\n\n        assert\
    \ self.__after_seal_check(u,v)\n        return v!=self.root and u==self.parent[v]\n\
    \n    def is_children(self, u, v):\n        \"\"\" u \u306F v \u306E\u5B50\u304B\
    ? \"\"\"\n\n        assert self.__after_seal_check(u,v)\n        return self.is_parent(v,u)\n\
    \n    def is_brother(self,u,v):\n        \"\"\" 2\u3064\u306E\u9802\u70B9 u, v\
    \ \u306F\u5144\u5F1F (\u89AA\u304C\u540C\u3058) \u304B?  \"\"\"\n\n        assert\
    \ self.__after_seal_check(u,v)\n\n        if u==self.root or v==self.root:\n \
    \           return False\n        return self.parent[u]==self.parent[v]\n\n  \
    \  def is_ancestor(self,u,v):\n        \"\"\" \u9802\u70B9 u \u306F\u9802\u70B9\
    \ v \u306E\u5148\u7956\u304B? \"\"\"\n\n        assert self.__after_seal_check(u,v)\n\
    \n        dd=self.vertex_depth(v)-self.vertex_depth(u)\n        if dd<0:\n   \
    \         return False\n\n        v=self.upper(v,dd)\n        return u==v\n\n\
    \    def is_descendant(self,u,v):\n        \"\"\" \u9802\u70B9 u \u306F\u9802\u70B9\
    \ v \u306E\u5B50\u5B6B\u304B? \"\"\"\n\n        assert self.__after_seal_check(u,v)\n\
    \        return self.is_ancestor(v,u)\n\n    def direction(self, u, v):\n    \
    \    \"\"\" \u9802\u70B9 u \u304B\u3089\u9802\u70B9 v (u!=v) \u3078\u5411\u304B\
    \u3046\u30D1\u30B9\u304C\u9802\u70B9 u \u306E\u6B21\u306B\u901A\u308B\u9802\u70B9\
    \"\"\"\n\n        assert self.__after_seal_check(u,v)\n        assert u!=v\n\n\
    \        if self.is_ancestor(u,v):\n            du=self.vertex_depth(u)\n    \
    \        dv=self.vertex_depth(v)\n            return self.upper(v,dv-(du+1))\n\
    \        else:\n            return self.parent[u]\n\n    def jump(self, u, v,\
    \ k, default=-1):\n        \"\"\" \u9802\u70B9 u \u304B\u3089\u9802\u70B9 v \u3078\
    \u5411\u304B\u3046\u30D1\u30B9\u306B\u304A\u3044\u3066 k \u756A\u76EE (0-indexed)\
    \ \u306B\u901A\u308B\u9802\u70B9 (\u30D1\u30B9\u306E\u9577\u3055\u304C k \u3088\
    \u308A\u5927\u304D\u3044\u5834\u5408\u306F default)\n\n        u: int\n      \
    \  v: int\n        k: int\n        default=-1: int\n        \"\"\"\n\n       \
    \ assert self.__after_seal_check(u,v)\n\n        if k==0:\n            return\
    \ u\n\n        # lca \u3092\u6C42\u3081\u308B.\n        x=u; y=v\n        dx=self.vertex_depth(x);\
    \ dy=self.vertex_depth(y)\n        if dx>dy:\n            x,y=y,x\n          \
    \  dx,dy=dy,dx\n        y=self.upper(y, dy-dx)\n\n        if x==self.root or x==y:\n\
    \            w=x\n        else:\n            bit=dx.bit_length()\n\n         \
    \   X=self.upper_list\n            for t in range(bit-1,-1,-1):\n            \
    \    px=X[t][x]; py=X[t][y]\n                if px!=py:\n                    x=px;\
    \ y=py\n            w=self.parent[x]\n\n        dist_uw=self.vertex_depth(u)-self.vertex_depth(w)\n\
    \        dist_wv=self.vertex_depth(v)-self.vertex_depth(w)\n\n        if dist_uw+dist_wv<k:\n\
    \            return default\n        elif k<=dist_uw:\n            return self.upper(u,\
    \ k)\n        else:\n            return self.upper(v, (dist_uw+dist_wv)-k)\n\n\
    \    def is_leaf(self,v):\n        \"\"\" \u9802\u70B9 v \u306F\u8449? \"\"\"\n\
    \n        return not bool(self.children[v])\n\n    def distance(self, u, v, faster=True):\n\
    \        \"\"\" 2\u9802\u70B9 u, v \u9593\u306E\u8DDD\u96E2\u3092\u6C42\u3081\u308B\
    . \"\"\"\n\n        assert self.__after_seal_check(u,v)\n\n        dep=self.vertex_depth\n\
    \n        if faster:\n            return dep(u)+dep(v)-2*dep(self.lowest_common_ancestor(u,v))\n\
    \        else:\n            return dep(u)+dep(v)-2*dep(self.lowest_common_ancestor_greedy(u,v))\n\
    \n    def __descendant_count(self):\n        assert self.__after_seal_check()\n\
    \        if hasattr(self,\"des_count\"):\n            return\n\n        if not\
    \ hasattr(self,\"tower\"):\n            self.depth_search(False)\n\n        self.des_count=[1]*(self.index+self.N)\n\
    \        pa=self.parent\n        for T in self.tower[:0:-1]:\n            for\
    \ x in T:\n                self.des_count[pa[x]]+=self.des_count[x]\n        return\n\
    \n    def descendant_count(self, v):\n        \"\"\" \u9802\u70B9 v \u306E\u5B50\
    \u5B6B\u306E\u6570\u3092\u6C42\u3081\u308B. \"\"\"\n        assert self.__after_seal_check(v)\n\
    \        self.__descendant_count()\n        return self.des_count[v]\n\n    def\
    \ subtree_size(self, v):\n        \"\"\" \u9802\u70B9 v \u3092\u6839\u3068\u3057\
    \u305F\u90E8\u5206\u6839\u4ED8\u304D\u6728\u306E\u30B5\u30A4\u30BA\u3092\u6C42\
    \u3081\u308B. \"\"\"\n        return self.descendant_count(v)\n\n    def preorder(self,v):\n\
    \        \"\"\" \u9802\u70B9 v \u306E\u884C\u304D\u304C\u3051\u9806\u3092\u6C42\
    \u3081\u308B. \"\"\"\n        assert self.__after_seal_check(v)\n        if hasattr(self,\
    \ \"preorder_number\"):\n            self.preorder_number[v]\n\n        from collections\
    \ import deque\n        Q=deque([self.root])\n        T=[-1]*(self.N+self.index)\n\
    \n        p=1\n        while Q:\n            x=Q.popleft()\n            T[x]=p\n\
    \            p+=1\n\n            C=self.children[x]\n            for y in C:\n\
    \                Q.append(y)\n        self.preorder_number=T\n        return T[v]\n\
    \n    def dfs_yielder(self, order=None):\n        \"\"\" DFS \u306B\u304A\u3051\
    \u308B\u9802\u70B9\u306E\u51FA\u5165\u308A\u3092 yield \u3059\u308B.\n\n     \
    \   \u4EE5\u4E0B\u306E\u3088\u3046\u306A\u95A2\u6570\u3092 (\u4EEE\u60F3\u7684\
    \u306B) \u5B9F\u884C\u3059\u308B.\n\n        def dfs(v):\n            yield (v,1)\
    \ #\u9802\u70B9 v \u306B\u5165\u308B\n            for w in self.children[v]:\n\
    \                dfs(w) #\u9802\u70B9 v \u3092\u51FA\u308B.\n            yield\
    \ (v,-1)\n\n        order (1\u5909\u6570\u95A2\u6570): for w in self.children[v]\
    \ \u306E\u9806\u756A\u3092\u6307\u5B9A\u3059\u308B (\u6607\u9806) (\u203B \u7121\
    \u3044\u5834\u5408\u306F\u4EFB\u610F, \u7834\u58CA\u7684)\n        \"\"\"\n  \
    \      assert self.__after_seal_check()\n\n        #\u6700\u521D\n        yield\
    \ (self.root, 1)\n\n        v=self.root\n\n        ch=self.children\n        pa=self.parent\n\
    \n        R=[-1]*self.index+[len(ch[x]) for x in range(self.index,self.index+self.N)]\n\
    \        S=[0]*(self.index+self.N)\n\n        if order!=None:\n            for\
    \ w in range(self.index, self.index+self.N):\n                ch[w].sort(key=order)\n\
    \n        while True:\n            if R[v]==S[v]:  #\u3082\u3057, \u9032\u3081\
    \u306A\u3044\u306A\u3089\u3070\n                yield (v,-1) #\u9802\u70B9v\u3092\
    \u51FA\u308B\n                if v==self.root:\n                    break\n  \
    \              else:\n                    v=pa[v]\n            else:   #\u9032\
    \u3081\u308B\n                w=v\n                v=ch[v][S[v]]\n           \
    \     S[w]+=1\n                yield (v, 1)\n\n    def top_down(self):\n     \
    \   \"\"\" \u6728\u306E\u6839\u304B\u3089 yield \u3059\u308B. \"\"\"\n\n     \
    \   assert self.__after_seal_check()\n        if not hasattr(self,\"tower\"):\n\
    \            self.depth_search(False)\n\n        for E in self.tower:\n      \
    \      for v in E:\n                yield v\n\n    def bottom_up(self):\n    \
    \    \"\"\" \u6728\u306E\u8449\u304B\u3089 yield \u3059\u308B. \"\"\"\n\n    \
    \    assert self.__after_seal_check()\n        if not hasattr(self,\"tower\"):\n\
    \            self.depth_search(False)\n\n        for E in self.tower[::-1]:\n\
    \            for v in E:\n                yield v\n\n    def tree_dp_from_leaf(self,merge,unit,f,g,Mode=False):\n\
    \        \"\"\" \u8449\u304B\u3089\u6728 DP \u884C\u3046.\n\n        [input]\n\
    \        merge: \u53EF\u63DB\u30E2\u30CE\u30A4\u30C9\u3092\u6210\u30592\u9805\u6F14\
    \u7B97 M x M -> M\n        unit: M \u306E\u5358\u4F4D\u5143\n        f: X x V\
    \ x V \u2192 M: f(x,v,w): v \u304C\u89AA, w \u304C\u5B50\n        g: M x V \u2192\
    \ X: g(x,v)\n        Mode: False \u2192 \u6839\u306E\u5024\u306E\u307F, True \u2192\
    \ \u5168\u3066\u306E\u5024\n\n        [\u88DC\u8DB3]\n        \u9802\u70B9 v \u306E\
    \u5B50\u304C x,y,z,..., w \u306E\u3068\u304D, \u66F4\u65B0\u5F0F\u306F * \u3092\
    \ merge \u3068\u3057\u3066\n            dp[v]=g(f(dp[x],v,x)*f(dp[y],v,y)*f(dp[z],v,z)*...*f(dp[w],v,w),\
    \ v)\n        \u306B\u306A\u308B.\n        \"\"\"\n        assert self.__after_seal_check()\n\
    \n        data=[unit]*(self.index+self.N)\n        ch=self.children\n\n      \
    \  for x in self.bottom_up():\n            for y in ch[x]:\n                data[x]=merge(data[x],\
    \ f(data[y], x, y))\n            data[x]=g(data[x], x)\n\n        if Mode:\n \
    \           return data\n        else:\n            return data[self.root]\n\n\
    \    def tree_dp_from_root(self, f, alpha):\n        \"\"\" \u6839\u304B\u3089\
    \u6728 DP \u3092\u884C\u3046.\n\n        [input]\n        alpha: \u521D\u671F\u5024\
    \n        f: X x V x V \u2192 X: f(x,v,w): v \u304C\u89AA, w \u304C\u5B50\n\n\
    \        [\u88DC\u8DB3]\n        \u9802\u70B9 v \u306E\u89AA\u304C x \u306E\u3068\
    \u304D, \u66F4\u65B0\u5F0F\u306F\n            dp[v]=f(dp[x],x,v) (x!=root), alpha\
    \ (x==root)\n        \u306B\u306A\u308B.\n        \"\"\"\n        assert self.__after_seal_check()\n\
    \n        data=[0]*(self.index+self.N)\n        ch=self.children\n\n        data[self.root]=alpha\n\
    \        for x in self.top_down():\n            for y in ch[x]:\n            \
    \    data[y]=f(data[x],x,y)\n\n        return data\n\n    def rerooting(self,\
    \ merge, unit, f, g):\n        \"\"\" \u5168\u65B9\u4F4D\u6728 DP \u3092\u884C\
    \u3046.\n\n        [input]\n        merge: \u53EF\u63DB\u30E2\u30CE\u30A4\u30C9\
    \u3092\u6210\u30592\u9805\u6F14\u7B97 M x M -> M\n        unit: M \u306E\u5358\
    \u4F4D\u5143\n        f: X x V x V \u2192 M: f(x,v,w): v \u304C\u89AA, w \u304C\
    \u5B50\n        g: M x V \u2192 X: g(x,v)\n\n        \u203B tree_dp_from_leaf\
    \ \u3068\u540C\u3058\u5F62\u5F0F\n\n        [\u88DC\u8DB3]\n        \u9802\u70B9\
    \ v \u306E\u5B50\u304C x,y,z,..., w \u306E\u3068\u304D, \u66F4\u65B0\u5F0F\u306F\
    \ * \u3092 merge \u3068\u3057\u3066\n            dp[v]=g(f(dp[x],v,x)*f(dp[y],v,y)*f(dp[z],v,z)*...*f(dp[w],v,w),\
    \ v)\n        \u306B\u306A\u308B.\n        \"\"\"\n        assert self.__after_seal_check()\n\
    \n        upper=[unit]*(self.index+self.N)\n        lower=[unit]*(self.index+self.N)\n\
    \n        ch=self.children\n        pa=self.parent\n\n        #DFS\u30D1\u30FC\
    \u30C8\n        lower=self.tree_dp_from_leaf(merge, unit, f, g, True)\n\n    \
    \    #BFS\u30D1\u30FC\u30C8\n        for v in self.top_down():\n            cc=ch[v]\n\
    \n            #\u7D2F\u7A4D\u30DE\u30FC\u30B8\n            deg=len(cc)\n\n   \
    \         Left=[unit]; x=unit\n            for c in cc:\n                x=merge(x,\
    \ f(lower[c], v, c))\n                Left.append(x)\n\n            Right=[unit];\
    \ y=unit\n            for c in cc[::-1]:\n                y=merge(y, f(lower[c],\
    \ v, c))\n                Right.append(y)\n            Right=Right[::-1]\n\n \
    \           for i in range(deg):\n                c=cc[i]\n\n                a=merge(Left[i],\
    \ Right[i+1])\n\n                if v!=self.root:\n                    b=merge(a,\
    \ f(upper[v], v, pa[v]))\n                else:\n                    b=a\n\n \
    \               upper[c]=g(b, v)\n\n        A=[unit]*(self.index+self.N)\n   \
    \     for v in range(self.index,self.index+self.N):\n            if v!=self.root:\n\
    \                a=f(upper[v], v, pa[v])\n            else:\n                a=unit\n\
    \n            for c in ch[v]:\n                a=merge(a, f(lower[c], v, c))\n\
    \            A[v]=g(a, v)\n        return A\n\n    def euler_tour_vertex(self,\
    \ order=None):\n        \"\"\" \u30AA\u30A4\u30E9\u30FC\u30C4\u30A2\u30FC (vertex)\
    \ \u306B\u95A2\u3059\u308B\u8A08\u7B97\u3092\u884C\u3046.\n\n        order: \u9802\
    \u70B9\u306E\u9806\u756A\u3092\u6307\u5B9A\u3059\u308B (\u7834\u58CA\u7684)\n\
    \        \"\"\"\n\n        assert self.__after_seal_check()\n        if hasattr(self,\"\
    euler_vertex\"):\n            return\n\n        #\u6700\u521D\n        X=[-1]*(2*self.N-1)\
    \ #X: Euler Tour (vertex) \u306E\u30EA\u30B9\u30C8\n\n        v=self.root\n\n\
    \        ch=self.children\n        if order!=None:\n            for i in range(self.index,self.index+self.N):\n\
    \                ch[i].sort(key=order)\n\n        pa=self.parent\n\n        R=[-1]*self.index+[len(ch[x])\
    \ for x in range(self.index,self.index+self.N)]\n        S=[0]*(self.index+self.N)\n\
    \n        for t in  range(2*self.N-1):\n            X[t]=v\n            if R[v]==S[v]:\n\
    \                v=pa[v]\n            else:   #\u9032\u3081\u308B\n          \
    \      w=v\n                v=ch[v][S[v]]\n                S[w]+=1\n\n       \
    \ self.euler_vertex=X\n        self.in_time=[-1]*(self.index+self.N)\n       \
    \ self.out_time=[-1]*(self.index+self.N)\n        for t in range(2*self.N-1):\n\
    \            v=X[t]\n            if self.in_time[v]==-1:\n                self.in_time[v]=self.out_time[v]=t\n\
    \            else:\n                self.out_time[v]=t\n\n    def euler_tour_edge(self):\n\
    \        \"\"\" \u30AA\u30A4\u30E9\u30FC\u30C4\u30A2\u30FC (edge) \u306B\u95A2\
    \u3059\u308B\u8A08\u7B97\u3092\u884C\u3046.\n\n        (u, v, k): u \u304B\u3089\
    \ v \u3078\u5411\u304B\u3046 (k=+1 \u306E\u3068\u304D\u306F\u8449\u3078\u9032\u3080\
    \u5411\u304D, k=-1 \u306E\u3068\u304D\u306F\u6839\u3078\u9032\u3080\u5411\u304D\
    )\n        \"\"\"\n\n        assert self.__after_seal_check()\n        if hasattr(self,\"\
    euler_edge\"):\n            return\n\n        if not hasattr(self, \"euler_vertex\"\
    ):\n            self.euler_tour_vertex()\n\n        self.euler_edge=[0]*(2*(self.N-1))\n\
    \        euler=self.euler_vertex\n        pa=self.parent\n        for t in range(2*(self.N-1)):\n\
    \            u=euler[t]; v=euler[t+1]\n            k=1 if u==pa[v] else -1\n \
    \           self.euler_edge[t]=(u,v,k)\n\n    def centroid(self, all=False):\n\
    \        \"\"\" \u6728\u306E\u91CD\u5FC3\u3092\u6C42\u3081\u308B\n\n        all:\
    \ False \u2192 \u91CD\u5FC3\u306E\u3046\u3061\u306E1\u9802\u70B9. True \u2192\
    \ \u5168\u3066\u306E\u91CD\u5FC3.\n        \"\"\"\n\n        assert self.__after_seal_check()\n\
    \n        M=self.N//2\n\n        if not hasattr(self,\"des_count\"):\n       \
    \     self.__descendant_count()\n\n        G=[]; ch=self.children; des=self.des_count\n\
    \n        for v in range(self.index, self.index+self.N):\n            if self.N-des[v]>M:\n\
    \                break\n\n            flag=1\n            for x in ch[v]:\n  \
    \              if des[x]>M:\n                    flag=0\n                    break\n\
    \            if flag:\n                if all:\n                    G.append(v)\n\
    \                else:\n                    return v\n        return G\n\n   \
    \ def generated_subtree(self,S):\n        \"\"\" S \u3092\u542B\u3080\u6700\u5C0F\
    \u306E\u90E8\u5206\u6728\u306E\u9802\u70B9\u3092\u6C42\u3081\u308B. \"\"\"\n \
    \       assert self.__after_seal_check(*S)\n\n        if not hasattr(self, \"\
    in_time\"):\n            self.euler_tour_vertex()\n\n        S=sorted(set(S),key=lambda\
    \ i:self.in_time[i])\n        K=len(S)\n\n        T=set()\n        for i in range(K-1):\n\
    \            for a in self.path(S[i],S[i+1]):\n                T.add(a)\n    \
    \    return sorted(T)\n\n    def generated_subtree_size(self,S):\n        \"\"\
    \" S \u3092\u542B\u3080\u6700\u5C0F\u306E\u90E8\u5206\u6728\u306E\u30B5\u30A4\u30BA\
    \u3092\u6C42\u3081\u308B. \"\"\"\n        assert self.__after_seal_check(*S)\n\
    \n        if not hasattr(self, \"in_time\"):\n            self.euler_tour_vertex()\n\
    \n        S=sorted(set(S),key=lambda i:self.in_time[i])\n        K=len(S)\n\n\
    \        X=0\n        for i in range(K-1):\n            X+=self.distance(S[i],S[i+1])\n\
    \        return (X+self.distance(S[-1],S[0]))//2\n\n#=================================================\n\
    def Making_Tree_from_Adjacent_List(N, A, root, index=0):\n    \"\"\" \u96A3\u63A5\
    \u30EA\u30B9\u30C8\u304B\u3089\u6728\u3092\u4F5C\u308B.\"\"\"\n\n    from collections\
    \ import deque\n\n    T=Tree(N, index)\n    T.root_set(root)\n\n    S=[False]*(N+index);\
    \ S[root]=True\n    Q=deque([root])\n    while Q:\n        v=Q.popleft()\n   \
    \     for w in A[v]:\n            if not S[w]:\n                S[w]=True\n  \
    \              T.parent_set(w,v)\n                Q.append(w)\n\n    T.seal()\n\
    \    return T\n\ndef Making_Tree_from_Edges(N, E, root, index=0):\n    \"\"\"\
    \ \u8FBA\u306E\u30EA\u30B9\u30C8\u304B\u3089\u6728\u3092\u4F5C\u308B.\n\n    N:\
    \ \u9802\u70B9\u6570\n    E: \u8FBA\u306E\u30EA\u30B9\u30C8 E=[(u[0],v[0]), ...,\
    \ (u[N-2], v[N-2]) ]\n    root: \u6839\n    \"\"\"\n\n    from collections import\
    \ deque\n\n    A=[[] for _ in range(N+index)]\n    for u,v in E:\n        A[u].append(v)\n\
    \        A[v].append(u)\n\n    T=Tree(N, index)\n    T.root_set(root)\n\n    S=[False]*(N+index);\
    \ S[root]=True\n    Q=deque([root])\n    while Q:\n        v=Q.popleft()\n   \
    \     for w in A[v]:\n            if not S[w]:\n                S[w]=True\n  \
    \              T.parent_set(w,v)\n                Q.append(w)\n\n    T.seal()\n\
    \    return T\n\ndef Spanning_Tree(N,E,root,index=0,exclude=False):\n    \"\"\"\
    \ \u9023\u7D50\u306A\u30B0\u30E9\u30D5\u304B\u3089\u5168\u57DF\u6728\u3092\u3064\
    \u304F\u308B.\n\n    N: \u9802\u70B9\u6570\n    E:  \u8FBA\u306E\u30EA\u30B9\u30C8\
    \n    root: \u6839\n    exclude: \u5168\u57DF\u6728\u304B\u3089\u5916\u308C\u305F\
    \u8FBA\u306E\u30EA\u30B9\u30C8\u3092\u51FA\u529B\u3059\u308B\u304B.\n    \"\"\"\
    \n\n    from collections import deque\n    F=[set() for _ in range(index+N)]\n\
    \    EE=[]\n    L=[]\n    for u,v in E:\n        assert index<=u<index+N\n   \
    \     assert index<=v<index+N\n\n        if (u==v) or (u in F[v]):\n         \
    \   L.append((u,v))\n            continue\n\n        EE.append((u,v))\n      \
    \  F[u].add(v)\n        F[v].add(u)\n\n    X=[-1]*(index+N)\n    X[root]=root\n\
    \n    C=[[] for _ in range(index+N)]\n\n    Q=deque([root])\n    while Q:\n  \
    \      x=Q.popleft()\n        for y in F[x]:\n            if X[y]==-1:\n     \
    \           X[y]=x\n                Q.append(y)\n                C[x].append(y)\n\
    \n    T=Tree(N,index)\n    T.root_set(root)\n    T.parent=X\n    T.children=C\n\
    \    T.seal()\n\n    if exclude==False:\n        return T\n\n    pa=T.parent\n\
    \    for u,v in EE:\n        if not(pa[v]==u or pa[u]==v):\n            L.append((u,v))\n\
    \n    return T,L\n"
  dependsOn: []
  isVerificationFile: false
  path: Tree/Tree.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Tree/Tree.py
layout: document
title: Tree
---

## Outline

木 $T=(V,E)$ における様々な計算をまとめたデータ構造

## Contents

---

### Constructer

```Python
T=Tree(N, index=0)
```

- $N$ 頂点の木グラフの準備をする.
- 頂点の番号は ${\rm index}, {\rm index}+1, \cdots, {\rm index}+(N-1)$ である.
- **計算量** : $O(N)$ Time.

---

### is_mutable

```Pyhon
T.is_mutable()
```

- 木が変更可能な状態かどうかを返す.

---

### root

```Python
T.root_set(root)
```

- 根を ${\rm root}$ に設定する.
- **制約**
  - ${\rm index} \leq {\rm root} \lt {\rm index}+N$

---

### parent_set

```Python
T.parent_set(x, y)
```

- 頂点 $x$ の親を頂点 $y$ に設定する.
- **制約**
  - ${\rm index} \leq x \lt {\rm index}+N$
  - ${\rm index} \leq y \lt {\rm index}+N$

---

### child_set

```Python
T.child_set(x, y)
```

- 頂点 $x$ の子の一つに頂点 $y$ に設定する.
- **制約**
  - ${\rm index} \leq x \lt {\rm index}+N$
  - ${\rm index} \leq y \lt {\rm index}+N$

---

### seal

```Python
T.seal()
```

- 木の情報を確定させる. これ以降木の変更は不可能.

---

### depth_search

```Python
T.depth_search(mode=True)
```

- 各頂点の深さを求める. `mode=True` ならば, 各頂点の深さのリストを返す.
- **制約**
  - ${\rm mode}$ は `True` または `False`
- **計算量** : $O(N)$ Time.

---

### vertex_depth

```Python
T.vertex_depth(x)
```

- 頂点 $x$ の深さを求める.
- **制約**
  - ${\rm index} \leq x \lt {\rm index}+N$

---

### upper

```Python
T.upper(x, k, over)
```

- 頂点 $x$ から親に移動することを $k$ 回行った後の頂点を求める. ただし, $\operatorname{depth}(x) <k$ のとき, `over=True` ならば根を返り値とし, `over=False` ならば, `ValueError` を吐く.
- **制約**
  - ${\rm index} \leq x \lt {\rm index}+N$
  - $k \geq 0$
- **計算量** : $O(\log N)$ Time.

---

### lowest_common_ancestor_greedy

```Python
T.lowest_common_ancestor_greedy(x, y)
```

- 2頂点 $x,y$ の最小共通先祖を愚直な方法で求める.
- **制約**
  - ${\rm index} \leq x \lt {\rm index}+N$
  - ${\rm index} \leq y \lt {\rm index}+N$
- **計算量** : $O(N)$ Time.

---

### lowest_common_ancestor

```Python
T.lowest_common_ancestor(x, y)
```

- 2頂点 $x,y$ の最小共通先祖を高速な方法で求める.
- **制約**
  - ${\rm index} \leq x \lt {\rm index}+N$
  - ${\rm index} \leq y \lt {\rm index}+N$
- **計算量** : 前計算: $O(N \log N)$ Time, 1 クエリ当たり $O(1)$ Time/Query.

---

### degree

```Python
T.degree(v)
```

- 頂点 $v$ の (グラフ理論における) 次数 を求める.
- **制約**
  - ${\rm index} \leq v \lt {\rm index}+N$

---

### diameter

```Python
T.diameter()
```

- 木の直径を求める.
- **計算量** : $O(N)$ Time.

---

### Path

```Python
T.path(u, v, falser=False)
```

- 木 $u,v$ -Path を求める.
- **制約**
  - ${\rm index} \leq u \lt {\rm index}+N$
  - ${\rm index} \leq v \lt {\rm index}+N$
- **計算量** :
  - ${\rm faster}=$ `False` のとき, $O(N)$ Time.
  - ${\rm faster}=$ `True` のとき, 1回でも `lowest_common_ansector` を使っていれば前計算がかからずに $O(N)$ Time. 使っていなければ初回のみ $O(N \log N)$ Time で, 2回目以降は $O(N)$ Time.

---
(作成途中)
