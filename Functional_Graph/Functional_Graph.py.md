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
  code: "class Functional_Graph:\n    def __init__(self, N, F=[]):\n        assert\
    \ (not F) or (len(F)==N)\n        self.__N=N\n\n        if F:\n            self.__F=F\n\
    \        else:\n            self.__F=list(range(N))\n\n        self.__build()\n\
    \n    def __len__(self):\n        return self.__N\n\n    def __getitem__(self,\
    \ index):\n        assert 0<=index<self.__N\n        return self.__F[index]\n\n\
    \    def __setitem(self, index, value):\n        assert 0<=index<self.__N\n  \
    \      self.__F[index]=value\n\n    def __build(self):\n        from collections\
    \ import deque\n\n        N=self.__N\n        F=self.__F\n        F_inv=[[] for\
    \ _ in range(len(self))]\n\n        for i in range(self.__N):\n            F_inv[F[i]].append(i)\n\
    \n        self.__F_inv=F_inv\n\n        # \u30B5\u30A4\u30AF\u30EB\u691C\u51FA\
    \u30D1\u30FC\u30C8\n        in_deg=[len(f_inv) for f_inv in F_inv]\n\n       \
    \ C=[1]*N\n        Q=deque([x for x in range(N) if in_deg[x]==0])\n        while\
    \ Q:\n            x=Q.pop()\n            C[x]=0\n            in_deg[F[x]]-=1\n\
    \            if in_deg[F[x]]==0:\n                Q.append(F[x])\n\n        cycle_vertex=[]\n\
    \        cycle_id=[-1]*N\n        cycle_vertex_id=[-1]*N\n        for x in range(N):\n\
    \            if C[x]:\n                c=[x]\n                C[x]=0\n       \
    \         y=F[x]\n                while y!=x:\n                    c.append(y)\n\
    \                    C[y]=0\n                    y=F[y]\n                cycle_vertex.append(c)\n\
    \n                i=len(cycle_vertex)-1\n                for j in range(len(c)):\n\
    \                    y=c[j]\n                    cycle_id[y]=i\n             \
    \       cycle_vertex_id[y]=j\n\n        self.__cycle_vertex=cycle_vertex\n   \
    \     self.__cycle_id=cycle_id\n        self.__cycle_vertex_id=cycle_vertex_id\n\
    \n        # \u30D6\u30E9\u30F3\u30C1\u30D1\u30FC\u30C8\n        tree_id=[-1]*N\
    \ # \u9802\u70B9 i \u304C\u5C5E\u3057\u3066\u3044\u308B\u6728\u306E id\n     \
    \   tree_vertex_id=[-1]*N # \u9802\u70B9 i \u304C\u5C5E\u3057\u3066\u3044\u308B\
    \u6728\u306B\u304A\u3051\u308B\u9802\u70B9\u306E\u756A\u53F7\n        tree_vertex=[]\
    \ # tree_vertex[tree_id[v]][tree_vertex_id[v]]=v\n        tree_depth=[0]*N # \u9802\
    \u70B9 v \u306E\u6DF1\u3055\n        tree_doubling=[]\n\n        i=j=0\n     \
    \   for x in range(N):\n            if cycle_id[x]!=-1:\n                tree_vertex.append([])\n\
    \n                j=0\n                tree_id[x]=i; tree_vertex_id[x]=j\n\n \
    \               Q=deque([x])\n                tree_vertex[-1].append(x)\n    \
    \            depth_max=0\n                while Q:\n                    x=Q.popleft()\n\
    \                    for y in F_inv[x]:\n                        if cycle_id[y]==-1:\n\
    \                            j+=1\n                            tree_id[y]=i; tree_vertex_id[y]=j\n\
    \                            tree_depth[y]=tree_depth[x]+1\n                 \
    \           depth_max=max(depth_max, tree_depth[y])\n                        \
    \    Q.append(y)\n                            tree_vertex[-1].append(y)\n    \
    \            i+=1\n\n                m=j+1\n                D=[[-1]*m for _ in\
    \ range(max(1,depth_max.bit_length()))]\n                for j in range(m):\n\
    \                    if j==0:\n                        D[0][j]=0\n           \
    \         else:\n                        D[0][j]=tree_vertex_id[F[tree_vertex[-1][j]]]\n\
    \n                for b in range(1, max(1,depth_max.bit_length())):\n        \
    \            for j in range(m):\n                        D[b][j]=D[b-1][D[b-1][j]]\n\
    \                tree_doubling.append(D)\n\n        self.__tree_id=tree_id\n \
    \       self.__tree_vertex_id=tree_vertex_id\n        self.__tree_vertex=tree_vertex\n\
    \        self.__tree_depth=tree_depth\n        self.__tree_doubling=tree_doubling\n\
    \n    def __upper(self, x, k):\n        i=self.__tree_id[x]\n        j=self.__tree_vertex_id[x]\n\
    \n        doubling=self.__tree_doubling[i]\n        b=0\n        while k:\n  \
    \          if k&1:\n                j=doubling[b][j]\n            k>>=1\n    \
    \        b+=1\n        return self.__tree_vertex[i][j]\n\n    def on_cycle(self,\
    \ x):\n        return self.__cycle_id[x]>=0\n\n    def calculate(self, x, k):\n\
    \        \"\"\" f^k(x) \u3092\u6C42\u3081\u308B.\n\n        \"\"\"\n\n       \
    \ if k<self.__tree_depth[x]:\n            return self.__upper(x, k)\n        else:\n\
    \            k-=self.__tree_depth[x]\n            x=self.__tree_vertex[self.__tree_id[x]][0]\n\
    \n            i=self.__cycle_id[x]\n            j=self.__cycle_vertex_id[x]\n\
    \            m=len(self.__cycle_vertex[i])\n            return self.__cycle_vertex[i][(j+k)%m]\n\
    \n    def calculate_list(self, k):\n        \"\"\" f^k(x) (x=0,1, ..., N-1) \u3092\
    \u6C42\u3081\u308B.\n        \"\"\"\n        return [self.calculate(x,k) for x\
    \ in range(self.__N)]\n\n    def get_cycle(self):\n        return self.__cycle_vertex\n\
    \n    def get_inverse(self):\n        return self.__F_inv\n"
  dependsOn: []
  isVerificationFile: false
  path: Functional_Graph/Functional_Graph.py
  requiredBy: []
  timestamp: '2022-10-27 18:36:50+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Functional_Graph/Functional_Graph.py
layout: document
title: Functional Graph
---

## Outline

Functional Graph における様々な計算を行う.

## Theory

### 定義

各頂点における出次数が $1$ であるような有向グラフを Functional Graph という.

このとき, 次の2つは1対1対応する.

* Functional Graph
* Map $F: V \to V$

対応の方法としては, Function Graph $D=(V,A)$ において, 各 $v \in V$ に対して唯一の出近傍を $F(v)$ で割り当てればよく. 逆に, 写像 $F: V \to V$ に対して, 有向グラフ $D=(V,A)$ を

$$A=\{\overrightarrow{v F(v)} \mid v \in V \}$$

とすると, $D$ は Functional Graph になる.

### サイクルへの分解

Functional Graph $D=(V,A)$ において, 各弱連結成分は次のものから構成されている.

* 有向サイクル $C: v_1 v_2 \dots v_m$
* $j=1,2, \dots, m$ に対して, $v_j$ を根とする根付き木 (ただし, 根付き木における各辺の向きは根へ向かう向きである).

このことから, 非負整数 $k$ と $v \in V$ が与えられたとき, $v$ から有向辺で $k$ 回辿った頂点 $w$ を次の方法で前計算のもと, 各クエリに対して $O(\log N)$ 時間/クエリ で求めることができる.

* $v$ がサイクル上の頂点であるとき, 周期性を利用することによって $w$ を $O(1)$ 時間で求められる.
* $v$ がサイクル上の頂点ではないとき, $v$ が属する部分木における頂点 $v$ の深さを $d$ とする.
  * $k \leq d$ ならば, $w$ は頂点 $v$ の $(d-k)$ 代親になる. これは $O(N \log N)$ 時間で求められる.
  * $k \gt d$ ならば, $v$ を $v$ が属している根付き木の根に, $k \gets k-d$ に置き換えることにより, $v$ がサイクル上の頂点の場合に帰着できる.

## Contents

---

### Constructer

```Python
F=Functional_Graph(N, F=[])
```

* $V=\\{0,1,2 \dots, N-1\\}$ とし, $v \mapsto F[v]$ に対応する Functional Graph を生成する.
* **計算量** : $O(N \log N)$ Times.

---

### on_cycle

```Python
F.on_cycle(x)
```

* 頂点 $x$ がサイクル上の頂点かどうかを判定する.
* 制約
  * $0 \leq x \lt N$.
* **計算量** : $O(1)$ Times.

---

### calculate

```Python
F.calculate(x, k)
```

* $F^k(x)=(\underbrace{F \circ \dots \circ F}_{k~{\rm times}})(x)$ を求める.
* 制約
  * $0 \leq x \lt N$.
  * $0 \leq k$
* **計算量** : $O(\log N)$ Times.

### calculate_list

```Python
F.calculate_list(x, k)
```

* リスト $[F^k(0), F^k(1), \dots, F^k(N-1)]$ を求める.
* 制約
  * $0 \leq k$
* **計算量** : $O(\log N)$ Times.

### get_cycle

```Python
F.get_cycle()
```

* Functional Graph にあるサイクルを返す.
* リストは $[[u_{0,0}, \dots, u_{0,m_0-1}], \dots, [u_{k-1,0}, \dots, u_{k-1, m_{k-1}-1}]]$ の形であり, $i=0,2, \dots, k-1$ に対して, $u_{i,0}, \dots, u_{i,m_i-1}$ がこの順に有向サイクルを成す.

### get_inverse

```Python
F.get_inverse()
```

* 次の条件を満たすような各要素がリストである長さ $N$ のリスト $[G_0, \dots, G_{N-1}]$ を返す.

$$\forall v \in V;~v \in G_x \iff f(x)=v$$

要は, $G_x$ は $f(v)=x$ となるような $v$ 全体のリスト.
