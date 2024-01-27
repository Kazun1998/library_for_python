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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.1/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.1/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from heapq import heappush, heappop\nclass Min_Cost_Flow:\n    #\u6700\u5C0F\
    \u8CBB\u7528\u6D41\u554F\u984C\n\n    inf=float(\"inf\")\n\n    class Arc:\n \
    \       __slots__=(\"source\", \"target\", \"cap\", \"base\", \"rev\", \"cost\"\
    , \"direction\", \"id\")\n\n        def __init__(self, source, target, cap, base,\
    \ cost, direction, id):\n            self.source=source\n            self.target=target\n\
    \            self.cap=cap\n            self.base=base\n            self.cost=cost\n\
    \            self.rev=None\n            self.direction=direction\n           \
    \ self.id=id\n\n        def __repr__(self):\n            if self.direction==1:\n\
    \                return \"id: {}, {} -> {}, {} / {}, cost: {}\".format(self.id,\
    \ self.source, self.target, self.cap, self.base, self.cost)\n            else:\n\
    \                return \"id: {}, {} <- {}, {} / {}, cost: {}\".format(self.id,\
    \ self.target, self.source, self.cap, self.base, self.cost)\n\n    def __init__(self,\
    \ N=0, objective=1):\n        \"\"\" \u9802\u70B9\u6570 N \u306E Min Cost Flow\
    \ \u5834\u3092\u751F\u6210\u3059\u308B.\n\n        N: int\n        objective:\
    \ -1 \u306E\u3068\u304D, \u6700\u5927\u5024\u306B\u306A\u308B.\n        \"\"\"\
    \n        self.arc=[[] for _ in range(N)]\n        self.__arc_list=[]\n      \
    \  self.__objective=objective\n        self.__is_DAG=None\n        self.__has_negative=False\n\
    \n    def add_vertex(self):\n        self.arc.append([])\n        return self.vertex_count()-1\n\
    \n    def add_vertices(self, k):\n        n=self.vertex_count()\n        self.arc.extend([[]\
    \ for _ in range(k)])\n        return list(range(n,n+k))\n\n    def add_arc(self,\
    \ v, w, cap, cost):\n        \"\"\" \u9802\u70B9  v \u304B\u3089\u9802\u70B9 w\
    \ \u3078\u5BB9\u91CF cap, \u8CBB\u7528 cost \u306E\u6709\u5411\u8FBA\u3092\u52A0\
    \u3048\u308B (\u8FD4\u308A\u5024: \u52A0\u3048\u305F\u8FBA\u306E\u756A\u53F7).\n\
    \n        v: \u59CB\u70B9\n        w: \u7D42\u70B9\n        cap: \u5BB9\u91CF\n\
    \        cost: \u8CBB\u7528\n        \"\"\"\n\n        m=len(self.__arc_list)\n\
    \        a=self.Arc(v, w, cap, cap, self.__objective*cost, 1, m)\n        b=self.Arc(w,\
    \ v, 0, cap, -self.__objective*cost, -1, m)\n        a.rev=b\n        b.rev=a\n\
    \        self.arc[v].append(a)\n        self.arc[w].append(b)\n        self.__arc_list.append(a)\n\
    \n        return m\n\n    def get_arc(self, i, mode=0):\n        \"\"\" i \u756A\
    \u76EE\u306E\u8FBA\u306E\u60C5\u5831\u3092\u5F97\u308B.\n\n        \"\"\"\n  \
    \      assert 0<=i<len(self.__arc_list)\n        a=self.__arc_list[i]\n      \
    \  if mode:\n            return a,a.rev\n        else:\n            return a\n\
    \n    def get_all_arcs(self):\n        return [self.get_arc(i) for i in range(len(self.__arc_list))]\n\
    \n    def vertex_count(self):\n        return len(self.arc)\n\n    def arc_count(self):\n\
    \        return len(self.__arc_list)\n\n    def change_arc(self, i, new_cap, new_flow,\
    \ new_cost):\n        \"\"\" i \u756A\u76EE\u306E\u8FBA\u306E\u60C5\u5831\u3092\
    \u5909\u66F4\u3059\u308B.\n\n        \"\"\"\n\n        assert 0<=i<len(self.__arc_list)\n\
    \        assert 0<=new_flow<=new_cap\n\n        a=self.__arc_list[i]\n       \
    \ a.base=new_cap; a.cap=new_cap-new_flow\n        a.rev.base=new_cap; a.rev.cap=new_flow\n\
    \n    def __potential_by_Dijkstra(self, s):\n        \"\"\" s \u3092\u57FA\u6E96\
    \u3068\u3059\u308B\u30DD\u30C6\u30F3\u30B7\u30E3\u30EB\u3092 Dijkstra \u6CD5\u306B\
    \u3088\u3063\u3066\u6C42\u3081\u308B.\n\n        s: int\n        \"\"\"\n\n  \
    \      inf=Min_Cost_Flow.inf\n        N=self.vertex_count()\n        self.__pre_v=[-1]*N\n\
    \        self.__pre_e=[None]*N\n        self.__dist=[inf]*N; self.__dist[s]=0\n\
    \n        Q=[(0,s)]\n        while Q:\n            d,v=heappop(Q)\n\n        \
    \    if d>self.__dist[v]:\n                continue\n\n            for a in self.arc[v]:\n\
    \                w=a.target\n                if a.cap>0 and self.__dist[w]>d+self.__pot[v]-self.__pot[w]+a.cost:\n\
    \                    self.__dist[w]=d+self.__pot[v]-self.__pot[w]+a.cost\n   \
    \                 self.__pre_v[w]=v\n                    self.__pre_e[w]=a\n \
    \                   heappush(Q, (self.__dist[w],w))\n        return\n\n    def\
    \ __potential_for_DAG(self, s):\n        \"\"\" DAG \u4E0A\u306B\u304A\u3051\u308B\
    \ s \u3092\u57FA\u6E96\u3068\u3059\u308B\u30DD\u30C6\u30F3\u30B7\u30E3\u30EB\u3092\
    \u6C42\u3081\u308B.\n\n        s: int\n        \"\"\"\n\n        inf=Min_Cost_Flow.inf\n\
    \        N=self.vertex_count()\n\n        self.__pre_v=[-1]*N\n        self.__pre_e=[None]*N\n\
    \        self.__dist=[inf]*N; self.__dist[s]=0\n\n        for v in self.__top_sort:\n\
    \            for a in self.arc[v]:\n                w=a.target\n             \
    \   if a.direction==1 and self.__dist[w]>self.__dist[v]+a.cost:\n            \
    \        self.__dist[w]=self.__dist[v]+a.cost\n                    self.__pre_v[w]=v\n\
    \                    self.__pre_e[w]=a\n\n    def __topological_sort(self):\n\
    \        N=self.vertex_count()\n        in_deg=[0]*N\n        for i in range(self.arc_count()):\n\
    \            in_deg[self.__arc_list[i].target]+=1\n\n        Q=[v for v in range(N)\
    \ if in_deg[v]==0]\n        T=[]\n        while Q:\n            v=Q.pop()\n  \
    \          T.append(v)\n\n            for a in self.arc[v]:\n                w=a.target\n\
    \                if a.direction==1:\n                    in_deg[w]-=1\n      \
    \              if in_deg[w]==0:\n                        Q.append(w)\n\n     \
    \   if len(T)==N:\n            self.__is_DAG=True\n            self.__top_sort=T\n\
    \        else:\n            self.__is_DAG=False\n            self.__top_sort=None\n\
    \n    def __potential(self, s):\n        \"\"\" s \u3092\u57FA\u6E96\u3068\u3059\
    \u308B\u30DD\u30C6\u30F3\u30B7\u30E3\u30EB\u3092\u6C42\u3081\u308B.\n\n      \
    \  s: int\n        \"\"\"\n\n        if self.__is_DAG==None:\n            self.__topological_sort()\n\
    \n        if self.__is_DAG:\n            self.__potential_for_DAG(s)\n       \
    \     self.__is_DAG=False\n        else:\n            self.__potential_by_Dijkstra(s)\n\
    \        return\n\n    def flow(self, source, target, flow):\n        \"\"\" \u9802\
    \u70B9 s \u304B\u3089\u9802\u70B9 t \u3078\u65B0\u305F\u306B\u6D41\u91CF f \u3092\
    \u6D41\u3059\u969B\u306E\u6700\u5C0F\u8CBB\u7528\u3092\u6C42\u3081\u308B.\n\n\
    \        source: \u59CB\u70B9\n        target: \u7D42\u70B9\n        flow: \u6D41\
    \u91CF\n        \"\"\"\n        assert 0<=flow\n        return self.slope(source,\
    \ target, flow)[-1]\n\n    def slope(self, source, target, flow=-1):\n       \
    \ \"\"\" \u6D41\u91CF\u3068\u6700\u5C0F\u30B3\u30B9\u30C8\u306E\u95A2\u4FC2\u56F3\
    \u6298\u308C\u7DDA\u3092\u51FA\u529B\u3059\u308B.\n\n        source: \u59CB\u70B9\
    \n        target: \u7D42\u70B9\n        flow: \u6D41\u91CF\n        \"\"\"\n\n\
    \        assert 0<=source<self.vertex_count()\n        assert 0<=target<self.vertex_count()\n\
    \        assert source!=target\n\n\n        N=self.vertex_count(); inf=Min_Cost_Flow.inf\n\
    \        self.__pot=[0]*N\n\n        g=[0]\n\n        if flow<0:\n           \
    \ flow=Min_Cost_Flow.inf\n\n        while flow:\n            self.__potential(source)\n\
    \n            if self.__dist[target]==inf:\n                break\n\n        \
    \    for v in range(N):\n                self.__pot[v]+=self.__dist[v]\n\n   \
    \         push=flow; u=target\n            while u!=source:\n                push=min(push,\
    \ self.__pre_e[u].cap)\n                u=self.__pre_v[u]\n\n            flow-=push\n\
    \n            for _ in range(push):\n                g.append(g[-1]+self.__objective*self.__pot[target])\n\
    \n            u=target\n            while u!=source:\n                a=self.__pre_e[u]\n\
    \                a.cap-=push; a.rev.cap+=push\n                u=self.__pre_v[u]\n\
    \        return g\n\n    def get_flow(self, mode=0):\n        if mode==0:\n  \
    \          return [a.base-a.cap for a in self.__arc_list]\n        else:\n   \
    \         F=[[] for _ in range(self.vertex_count())]\n            for i,a in enumerate(self.__arc_list):\n\
    \                F[a.source].append((i,a.target,a.base-a.cap))\n            return\
    \ F\n\n    def refresh(self):\n        for a in self.__arc_list:\n           \
    \ a.cap=a.base\n            a.rev.cap=0\n\nclass Max_Gain_Flow(Min_Cost_Flow):\n\
    \    def __init__(self, N=0):\n        Min_Cost_Flow.__init__(self, N, -1)\n"
  dependsOn: []
  isVerificationFile: false
  path: Min_Cost_Flow/Min_Cost_Flow.py
  requiredBy: []
  timestamp: '2022-04-20 15:00:17+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Min_Cost_Flow/Min_Cost_Flow.py
layout: document
title: Min Cost Flow
---

## Outline

有向グラフ $D=(V,A)$ において, 各孤 $a \in A$ には容量 $u(a)$ [単位] と1単位あたりの費用 $c(a)$ [/単位] が設定されている.

$s,t \in V$ に対して, $s$ から $t$ に水を $F$ [単位] 流す場合に必要な最小費用を求める.

## Contents

---

### Constructer

```Python
F=Flow(N=0)
```

- $N$ 頂点からなる空グラフを用意する.

---

### add_vertex

```Pyhon
F.add_vertex()
```

- $1$ 頂点を追加する. 返り値としてその追加した頂点の番号を返す.

---

### add_vertices

```Pyhon
F.add_vertices(k)
```

- $k$ 頂点を追加する. 返り値としてその追加した $k$ 個の頂点の番号のリストを返す.

---

### add_arc

```Pyhon
F.add_arc(v, w, cap)
```

- 容量 ${\rm cap}$ の孤 $\overrightarrow{vw}$ を追加する. 返り値として, 追加した辺の番号を返す.

---

### get_arc

```Pyhon
F.get_arc(i, mode=0)
```

- $i$ 番目の辺に関する情報を得る. ${\rm mode}=1$ とすると, $i$ 番目の辺だけでなく, $i$ 番目の辺の逆辺に関する情報も得る.

---

### get_all_arcs

```Pyhon
F.get_all_arcs()
```

- 全ての辺に関する情報を得る (逆辺は得られない).

---

### vertex_count

```Pyhon
F.vertetx_count()
```

- 有向グラフの位数 (頂点数) を得る.

---

### arc_count

```Pyhon
F.arc_count()
```

- 有向グラフのサイズ (辺の数) を得る.

---

### change_arc

```Pyhon
F.change_arc(i, new_cap, new_flow)
```

- $i$ 番目の辺を容量 `new_cap` で現在 `new_flow` である状態に変更する.

---

### add_edge

```Pyhon
F.add_edge(v, w, cap)
```

- 容量が `cap` である **無向辺** $vw$ を追加する.

---

### max_flow

```Pyhon
F.max_flow(source, target, flow_limit)
```

- $s=$ `source` , $t=$ `target` である場合の最大流問題を解く. なお,答えの最大値は `flow_limit` とする.

### get_flow

```Pyhon
F.get_flow(mode=0)
```

- `mode` $=0$ のとき : 長さがサイズのリストが与えられる. 第 $i$ 要素には $i$ 番目の (有向) 辺にながれている水量が格納されている.
- `mode` $=1$ のとき : 位数を $N$ とする. 長さ $N$ のリストが返され, 第 $v$ 要素には $v$ を始点とする各有向辺について $($`辺の番号` $,$  `終点` $,$ `辺に流れる水量`$)$ の情報を持つタプルのリストである.
