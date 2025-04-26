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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.13.3/x64/lib/python3.13/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.13.3/x64/lib/python3.13/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "#Thansk for aaaaaaaaaa2230\n#URL: https://atcoder.jp/contests/practice2/submissions/17017372\n\
    \nfrom collections import deque\n\nclass Arc:\n    def __init__(self, source:\
    \ int, target: int, cap: int, base: int, direction: int, id: int):\n        self.source\
    \ = source\n        self.target = target\n        self.cap = cap\n        self.base\
    \ = base\n        self.rev: Arc = None\n        self.direction = direction # 1\
    \ \u304C\u9806, -1 \u304C\u9006\u9806\n        self.id = id\n\n    def __repr__(self):\n\
    \        return f\"{self.__class__.__name__}(source={self.source}, target={self.target},\
    \ cap={self.cap}, base={self.base}, direction={self.direction}, id={self.id})\"\
    \n\nclass Max_Flow:\n    inf = float(\"inf\")\n\n    def __init__(self, N: int\
    \ = 0):\n        \"\"\" N \u9802\u70B9\u306E\u6700\u5927\u30D5\u30ED\u30FC\u3092\
    \u7528\u610F\u3059\u308B.\n\n        Args:\n            N (int, optional): \u4F4D\
    \u6570. Defaults to 0.\n        \"\"\"\n\n        self.arc: list[list[Arc]] =\
    \ [[] for _ in range(N)]\n        self.__arc_list: list[Arc] =[]\n\n    @property\n\
    \    def order(self) -> int:\n        \"\"\" \u4F4D\u6570\n\n        Returns:\n\
    \            int: \u4F4D\u6570\n        \"\"\"\n        return len(self.arc)\n\
    \n    @property\n    def vertex_count(self) -> int:\n        \"\"\" \u9802\u70B9\
    \u6570\n\n        Returns:\n            int: \u9802\u70B9\u6570\n        \"\"\"\
    \n        return len(self.arc)\n\n    @property\n    def size(self) -> int:\n\
    \        \"\"\" \u30B5\u30A4\u30BA\n\n        Returns:\n            int: \u30B5\
    \u30A4\u30BA\n        \"\"\"\n        return len(self.__arc_list)\n\n    @property\n\
    \    def arc_count(self):\n        \"\"\" \u5F27\u306E\u6570\n\n        Returns:\n\
    \            int: \u5F27\u306E\u6570\n        \"\"\"\n        return len(self.__arc_list)\n\
    \n    def add_vertex(self) -> int:\n        \"\"\" \u9802\u70B9\u3092 1 \u500B\
    \u8FFD\u52A0\u3059\u308B.\n\n        Returns:\n            int: \u8FFD\u52A0\u3057\
    \u305F\u9802\u70B9\u306E\u756A\u53F7\n        \"\"\"\n\n        self.arc.append([])\n\
    \        return self.vertex_count - 1\n\n    def add_vertices(self, k: int) ->\
    \ int:\n        \"\"\" \u9802\u70B9\u3092 k \u500B\u8FFD\u52A0\u3059\u308B.\n\n\
    \        Args:\n            k (int): \u8FFD\u52A0\u3059\u308B\u9802\u70B9\u306E\
    \u6570\n\n        Returns:\n            int: \u8FFD\u52A0\u3059\u308B k \u500B\
    \u306E\u9802\u70B9\u306E\u756A\u53F7\u304B\u3089\u306A\u308B\u30EA\u30B9\u30C8\
    \n        \"\"\"\n\n        n = self.vertex_count\n        self.arc.extend([[]\
    \ for _ in range(k)])\n        return list(range(n, n + k))\n\n    def add_arc(self,\
    \ v: int, w: int, cap: int) -> int:\n        \"\"\" \u5BB9\u91CF cap \u306E\u5F27\
    \ v \u2192 w \u3092\u8FFD\u52A0\u3059\u308B.\n\n        Args:\n            v (int):\
    \ \u59CB\u70B9\n            w (int): \u7D42\u70B9\n            cap (int): \u5BB9\
    \u91CF\n\n        Returns:\n            int: \u8FFD\u52A0\u3057\u305F\u5F27\u306E\
    \u756A\u53F7\n        \"\"\"\n\n\n        m = self.size\n        arc = Arc(v,\
    \ w, cap, cap, 1, m)\n        arc_rev = Arc(w, v, 0, cap, -1, m)\n        arc.rev\
    \ = arc_rev\n        arc_rev.rev = arc\n        self.arc[v].append(arc)\n    \
    \    self.arc[w].append(arc_rev)\n        self.__arc_list.append(arc)\n\n    \
    \    return m\n\n    def get_arc(self, i: int) -> Arc:\n        \"\"\" i \u756A\
    \u76EE\u306E\u5F27\u3092\u5F97\u308B.\n\n        Args:\n            i (int): \u5F27\
    \u306E\u756A\u53F7\n\n        Returns:\n            Arc: \u5F27\n        \"\"\"\
    \n\n        assert 0 <= i < self.size\n        return self.__arc_list[i]\n\n \
    \   def get_all_arcs(self) -> list[Arc]:\n        return [self.get_arc(i) for\
    \ i in range(self.size)]\n\n    def change_arc(self, i, new_cap, new_flow):\n\
    \        \"\"\" i \u756A\u76EE\u306E\u8FBA\u306E\u60C5\u5831\u3092\u5909\u66F4\
    \u3059\u308B.\n\n        \"\"\"\n\n        assert 0 <= i < self.size\n       \
    \ assert 0 <= new_flow<=new_cap\n\n        a=self.__arc_list[i]\n        a.base=new_cap;\
    \ a.cap=new_cap-new_flow\n        a.rev.base=new_cap; a.rev.cap=new_flow\n\n \
    \   def add_edge(self, v, w, cap):\n        \"\"\" \u5BB9\u91CF cap \u306E\u7121\
    \u5411\u8FBA v \u2192 w \u3092\u52A0\u3048\u308B.\"\"\"\n        self.add_arc(v,w,cap)\n\
    \        self.add_arc(w,v,cap)\n\n    def __bfs(self, s: int, t: int) -> bool:\n\
    \        level = self.level = [-1] * self.vertex_count\n        Q = deque([s])\n\
    \        level[s] = 0\n        while Q:\n            v = Q.popleft()\n       \
    \     next_level = level[v] + 1\n            for arc in self.arc[v]:\n       \
    \         if not(arc.cap and level[arc.target] == -1):\n                    continue\n\
    \n                level[arc.target] = next_level\n                if arc.target\
    \ == t:\n                    return True\n\n                Q.append(arc.target)\n\
    \n        return False\n\n    def __dfs(self, s: int, t: int, up: int) -> int:\n\
    \        arc_to = self.arc\n        it = self.it\n        level = self.level\n\
    \n        st = deque([t])\n        while st:\n            v = st[-1]\n       \
    \     if v == s:\n                break\n\n            lv = level[v]-1\n     \
    \       while it[v] < len(arc_to[v]):\n                arc_rev = arc_to[v][it[v]]\n\
    \                arc = arc_rev.rev\n                if arc.cap == 0 or lv != level[arc.source]:\n\
    \                    it[v] += 1\n                    continue\n              \
    \  st.append(arc.source)\n                break\n\n            if it[v] == len(arc_to[v]):\n\
    \                st.pop()\n                level[v] = -1\n        else:\n    \
    \        return 0\n\n        st.pop()\n        flow = up\n        for w in st:\n\
    \            arc = arc_to[w][it[w]].rev\n            flow = min(flow, arc.cap)\n\
    \n        for w in st:\n            arc_rev = arc_to[w][it[w]]\n            arc_rev.cap\
    \ += flow\n            arc_rev.rev.cap -= flow\n\n        return flow\n\n    def\
    \ max_flow(self, source: int, target: int, flow_limit: int = inf) -> int:\n  \
    \      \"\"\" source \u304B\u3089 target \u3078 flow_limit \u3092\u4E0A\u9650\u3068\
    \u3057\u3066\u6D41\u305B\u308B\u3060\u3051\u6D41\u3057\u305F\u3068\u304D\u306E\
    \ \"\u8FFD\u52A0\u3067\u767A\u751F\u3059\u308B\" \u6D41\u91CF\u3092\u6C42\u3081\
    \u308B.\n\n        Args:\n            source (int): \u59CB\u70B9\n           \
    \ target (int): \u7D42\u70B9\n            flow_limit (int, optional): \u6D41\u91CF\
    \u306E\u4E0A\u9650. Defaults to inf.\n\n        Returns:\n            int: \"\u8FFD\
    \u52A0\u3067\u767A\u751F\u3059\u308B\" \u6D41\u91CF\n        \"\"\"\n\n      \
    \  flow = 0\n        while flow < flow_limit and self.__bfs(source, target):\n\
    \            self.it = [0] * self.vertex_count\n            while flow < flow_limit:\n\
    \                f = self.__dfs(source, target, flow_limit - flow)\n         \
    \       if f == 0:\n                    break\n                flow += f\n   \
    \     return flow\n\n    def get_flow(self) -> list[list[tuple[int, int, int]]]:\n\
    \        F = [[] for _ in range(self.vertex_count)]\n        for arc in self.__arc_list:\n\
    \            F[arc.source].append((arc.id, arc.target, arc.base - arc.cap))\n\
    \        return F\n\n    def min_cut(self, s: int) -> list[int]:\n        \"\"\
    \" s \u3092 0 \u5074\u306B\u542B\u3081\u308B\u6700\u5C0F\u30AB\u30C3\u30C8\u3092\
    \u6C42\u3081\u308B.\n\n        Args:\n            s (int): \u9802\u70B9\u756A\u53F7\
    \n\n        Returns:\n            list[int]: 0, 1 \u304B\u3089\u306A\u308B\u9577\
    \u3055\u304C\u4F4D\u6570\u306E\u30EA\u30B9\u30C8. \u6700\u5C0F\u30AB\u30C3\u30C8\
    \u306F 0 \u5074\u3068 1 \u5074\u306B\u5206\u304B\u308C\u308B. \u9802\u70B9 s \u306F\
    \u5FC5\u305A 0 \u5074\u306B\u306A\u308B.\n        \"\"\"\n\n        group = [1]\
    \ * self.vertex_count\n        Q = deque([s])\n        while Q:\n            v\
    \ = Q.pop()\n            group[v] = 0\n            for arc in self.arc[v]:\n \
    \               if arc.cap and group[arc.target]:\n                    Q.append(arc.target)\n\
    \        return group\n\n    def refresh(self):\n        for a in self.__arc_list:\n\
    \            a.cap = a.base\n            a.rev.cap = 0\n"
  dependsOn: []
  isVerificationFile: false
  path: Flow/Flow.py
  requiredBy: []
  timestamp: '2025-04-26 14:03:35+09:00'
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
