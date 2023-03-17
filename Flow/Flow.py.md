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
    - https://atcoder.jp/contests/practice2/submissions/17017372
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.2/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.2/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "#Thansk for aaaaaaaaaa2230\n#URL: https://atcoder.jp/contests/practice2/submissions/17017372\n\
    \nfrom collections import deque\nclass MaxFlow:\n    inf = float(\"inf\")\n\n\
    \    class Arc:\n        def __init__(self, source, target, cap, base, direction,\
    \ id):\n            self.source=source\n            self.target=target\n     \
    \       self.cap = cap\n            self.base = base\n            self.rev = None\n\
    \            self.direction=direction\n            self.id=id\n\n        def __repr__(self):\n\
    \            if self.direction==1:\n                return \"id: {}, {} -> {},\
    \ {} / {}\".format(self.id, self.source, self.target, self.cap, self.base)\n \
    \           else:\n                return \"id: {}, {} <- {}, {} / {}\".format(self.id,\
    \ self.target, self.source, self.cap, self.base)\n\n    def __init__(self, N=0):\n\
    \        \"\"\" N \u9802\u70B9\u306E\u30D5\u30ED\u30FC\u5834\u3092\u751F\u6210\
    \u3059\u308B.\n        \"\"\"\n\n        self.arc = [[] for _ in range(N)]\n \
    \       self.__arc_list=[]\n\n    def add_vertex(self):\n        self.arc.append([])\n\
    \        return self.vertex_count()-1\n\n    def add_vertices(self, k):\n    \
    \    n=self.vertex_count()\n        self.arc.extend([[] for _ in range(k)])\n\
    \        return list(range(n,n+k))\n\n    def add_arc(self, v, w, cap):\n    \
    \    \"\"\" \u5BB9\u91CF cap \u306E\u6709\u5411\u8FBA v \u2192 w \u3092\u52A0\u3048\
    \u308B.\n        \"\"\"\n\n        m=len(self.__arc_list)\n        a=self.Arc(v,w,cap,cap,1,m)\n\
    \        b=self.Arc(w,v,0,cap,-1,m)\n        a.rev=b; b.rev=a\n        self.arc[v].append(a)\n\
    \        self.arc[w].append(b)\n        self.__arc_list.append(a)\n        return\
    \ m\n\n    def get_arc(self, i, mode=0):\n        \"\"\" i \u756A\u76EE\u306E\u8FBA\
    \u306E\u60C5\u5831\u3092\u5F97\u308B.\n\n        \"\"\"\n\n        assert 0<=i<len(self.__arc_list)\n\
    \        a=self.__arc_list[i]\n        if mode:\n            return a,a.rev\n\
    \        else:\n            return a\n\n    def get_all_arcs(self):\n        return\
    \ [self.get_arc(i) for i in range(len(self.__arc_list))]\n\n    def vertex_count(self):\n\
    \        return len(self.arc)\n\n    def arc_count(self):\n        return len(self.__arc_list)\n\
    \n    def change_arc(self, i, new_cap, new_flow):\n        \"\"\" i \u756A\u76EE\
    \u306E\u8FBA\u306E\u60C5\u5831\u3092\u5909\u66F4\u3059\u308B.\n\n        \"\"\"\
    \n\n        assert 0<=i<len(self.__arc_list)\n        assert 0<=new_flow<=new_cap\n\
    \n        a=self.__arc_list[i]\n        a.base=new_cap; a.cap=new_cap-new_flow\n\
    \        a.rev.base=new_cap; a.rev.cap=new_flow\n\n    def add_edge(self, v, w,\
    \ cap):\n        \"\"\" \u5BB9\u91CF cap \u306E\u7121\u5411\u8FBA v \u2192 w \u3092\
    \u52A0\u3048\u308B.\"\"\"\n        self.add_arc(v,w,cap)\n        self.add_arc(w,v,cap)\n\
    \n    def __bfs(self, s, t):\n        level=self.level=[-1]*self.vertex_count()\n\
    \        Q=deque([s])\n        level[s]=0\n        while Q:\n            v=Q.popleft()\n\
    \            next_level=level[v]+1\n            for a in self.arc[v]:\n      \
    \          if a.cap and level[a.target]==-1:\n                    level[a.target]=next_level\n\
    \                    if a.target==t:\n                        return True\n  \
    \                  Q.append(a.target)\n        return False\n\n    def __dfs(self,\
    \ s, t, up):\n        arc = self.arc\n        it = self.it\n        level = self.level\n\
    \n        st = deque([t])\n        while st:\n            v = st[-1]\n       \
    \     if v == s:\n                st.pop()\n                flow = up\n      \
    \          for w in st:\n                    a = arc[w][it[w]].rev\n         \
    \           flow = min(flow, a.cap)\n                for w in st:\n          \
    \          a = arc[w][it[w]]\n                    a.cap += flow\n            \
    \        a.rev.cap -= flow\n                return flow\n            lv = level[v]-1\n\
    \            while it[v] < len(arc[v]):\n                a = arc[v][it[v]]\n \
    \               ra = a.rev\n                if ra.cap == 0 or lv != level[a.target]:\n\
    \                    it[v] += 1\n                    continue\n              \
    \  st.append(a.target)\n                break\n            if it[v] == len(arc[v]):\n\
    \                st.pop()\n                level[v]=-1\n        return 0\n\n \
    \   def max_flow(self, source, target, flow_limit=inf):\n        \"\"\" source\
    \ \u304B\u3089 target \u306B\u9AD8\u3005 flow_limit \u306E\u6C34\u6D41\u3092\u6D41\
    \u3059\u3068\u304D, \"\u65B0\u305F\u306B\u6D41\u308C\u308B\" \u6C34\u6D41\u306E\
    \u5927\u304D\u3055\"\"\"\n\n        flow = 0\n        while flow < flow_limit\
    \ and self.__bfs(source, target):\n            self.it = [0]*self.vertex_count()\n\
    \            while flow < flow_limit:\n                f = self.__dfs(source,\
    \ target, flow_limit-flow)\n                if f == 0:\n                    break\n\
    \                flow += f\n        return flow\n\n    def get_flow(self, mode=0):\n\
    \        if mode==0:\n            return [a.base-a.cap for a in self.__arc_list]\n\
    \        else:\n            F=[[] for _ in range(self.vertex_count())]\n     \
    \       for i,a in enumerate(self.__arc_list):\n                F[a.source].append((i,\
    \ a.target, a.base-a.cap))\n            return F\n\n    def min_cut(self,s):\n\
    \        \"\"\" s \u3092 0 \u306B\u542B\u3081\u308B\u6700\u5C0F\u30AB\u30C3\u30C8\
    \u3092\u6C42\u3081\u308B.\n        \"\"\"\n\n        group = [1]*self.vertex_count()\n\
    \        Q = deque([s])\n        while Q:\n            v = Q.pop()\n         \
    \   group[v] = 0\n            for a in self.arc[v]:\n                if a.cap\
    \ and group[a.target]:\n                    Q.append(a.target)\n        return\
    \ group\n\n    def refresh(self):\n        for a in self.__arc_list:\n       \
    \     a.cap=a.base\n            a.rev.cap=0\n"
  dependsOn: []
  isVerificationFile: false
  path: Flow/Flow.py
  requiredBy: []
  timestamp: '2022-04-20 14:59:57+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Flow/Flow.py
layout: document
title: Flow
---

## Outline

有向グラフ $D=(V,A)$ において, 各孤 $a \in A$ には容量 $u(a)$ が定められている.

2頂点 $s, t \in V$ に対して, $s$ から $t$ へ流せる水の最大量を求める.

厳密には, 以下の問題を解く.

- Maximize : $F$
- Subject to :
  - $\displaystyle \sum_{\substack{a \in A \\\\ s=\operatorname{sink}(a)}} f_{a}-\sum_{\substack{a \in A \\\\ s=\operatorname{target}(a)}} f_{a}=F$
  - $\displaystyle \sum_{\substack{a \in A \\\\ t=\operatorname{sink}(a)}} f_{a}-\sum_{\substack{a \in A \\\\ t=\operatorname{target}(a)}} f_{a}=-F$
  - $\displaystyle \sum_{\substack{a \in A \\\\ v=\operatorname{sink}(a)}} f_{a}-\sum_{\substack{a \in A \\\\ v=\operatorname{target}(a)}} f_{a}=0 \quad (\forall v \in V \setminus \\{s,t\\})$
  - $0 \leq f_{a} \leq u(a) \quad (\forall a \in A)$

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
