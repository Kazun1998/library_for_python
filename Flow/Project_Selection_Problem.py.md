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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.13.3/x64/lib/python3.13/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.13.3/x64/lib/python3.13/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "\"\"\" Note: Project Selection Problem \u3067\u5BFE\u5FDC\u3067\u304D\u308B\
    \u6761\u4EF6\u306E\u4E00\u89A7\n\nh(x)=0 \u306A\u3089\u3070 a \u70B9\u5F97\u308B\
    \ \u2192 set_zero(x,a)\nh(x)=1 \u306A\u3089\u3070 a \u70B9\u5F97\u308B \u2192\
    \ set_one(x,a)\nh(x)=0 \u304B\u3064 h(y)=1 \u306A\u3089\u3070 a (<=0) \u70B9\u3092\
    \u5F97\u308B \u2192 set_not_equal(x,y,a)\nh(x_0)=...=h(x_{k-1})=0 \u306A\u3089\
    \u3070 a (>=0) \u70B9\u3092\u5F97\u308B \u2192 set_all_zero(X,a)\nh(x_0)=...=h(x_{k-1})=1\
    \ \u306A\u3089\u3070 a (>=0) \u70B9\u3092\u5F97\u308B \u2192 set_all_one(X,a)\n\
    \n\u4E00\u822C\u7684\u306A\u30B0\u30E9\u30D5\u3067\u306F\u5BFE\u5FDC\u3067\u304D\
    \u306A\u3044\u6761\u4EF6\u306E\u4F8B\n[1]\nh(x)=h(y)=0 \u306A\u3089\u3070 a (<=0)\
    \ \u70B9\u3092\u5F97\u308B\nh(x)=h(y)=1 \u306A\u3089\u3070 a (<=0) \u70B9\u3092\
    \u5F97\u308B\n\u2192 \u30B0\u30E9\u30D5\u304C\u4E8C\u90E8\u30B0\u30E9\u30D5 (\u90E8\
    \u96C6\u5408\u3092 X,Y \u3068\u3059\u308B) \u3067\u3042\u308A, x in X,y in Y \u306A\
    \u3089\u3070, \u4EE5\u4E0B\u306E\u3088\u3046\u306B\u3057\u3066\u5909\u63DB\u3059\
    \u308B.\nh'(z)=h(x) (x in X), 1-h(y) (y in Y) \u3068\u3057\u3066, h' \u3067\u306E\
    \u6761\u4EF6 \u300Ch'(x),h'(y) \u304C\u30FB\u30FB\u30FB \u306A\u3089\u3070, a\
    \ (<=0) \u70B9\u3092\u5F97\u308B\u300D\u306B\u7F6E\u304D\u63DB\u3048\u308B.\n\n\
    [2]\nh(x) != h(y) \u306A\u3089\u3070, a (>=0) \u70B9\u3092\u5F97\u308B\n\u2192\
    \u30B0\u30E9\u30D5\u304C\u4E8C\u90E8\u30B0\u30E9\u30D5 (\u90E8\u96C6\u5408\u3092\
    \ X,Y \u3068\u3059\u308B) \u3067\u3042\u308A, x in X,y in Y \u306A\u3089\u3070\
    , \u4EE5\u4E0B\u306E\u3088\u3046\u306B\u3057\u3066\u5909\u63DB\u3059\u308B.\n\u7121\
    \u6761\u4EF6\u306B a \u70B9\u5F97\u3066, \u300Ch(x)=h(y) \u306A\u3089\u3070 -a\
    \ (<=0) \u70B9\u3092\u5F97\u308B\u300D\u306B\u7F6E\u304D\u63DB\u3048\u308B.\n\u203B\
    \u4E0B\u99C4\u3092\u5C65\u304B\u305B\u308B\u3053\u3068\u3068, \u4E0B\u99C4\u3092\
    A, \u5E30\u7740\u554F\u984C\u306E\u7B54\u3048\u3092 X \u3068\u3057\u305F\u3068\
    \u304D, \u5143\u554F\u984C\u306E\u7B54\u3048\u306F A+X \u306B\u306A\u308B\u3053\
    \u3068\u306B\u6CE8\u610F!!\n\"\"\"\n\nfrom Flow import *\n\ninf=float(\"inf\"\
    )\nclass Project_Selection_Problem:\n    def __init__(self,N=0):\n        \"\"\
    \" N \u8981\u7D20\u306E Project Selection Problem \u3092\u751F\u6210\u3059\u308B\
    .\n\n        N: int\n        \"\"\"\n\n        self.N=N\n        self.ver_num=N+2\n\
    \        self.base=0\n        self.source=N\n        self.target=N+1\n       \
    \ self.indivi=[[0,0] for _ in range(N+2)]\n        self.mutual=[]\n\n    def add_vertex(self):\n\
    \        n=self.ver_num\n        self.indivi.append([0,0])\n        self.ver_num+=1\n\
    \        return n\n\n    def __add_vertex_inner(self):\n        n=self.ver_num\n\
    \        self.indivi.append([None,None])\n        self.ver_num+=1\n        return\
    \ n\n\n    def add_vertices(self, k):\n        n=self.ver_num\n        self.indivi.extend([[0,0]\
    \ for _ in range(k)])\n        self.ver_num+=k\n        return list(range(n,n+k))\n\
    \n    def set_zero_one(self,x,y,a):\n        \"\"\" h(x)=0,  h(y)=1 \u306E\u3068\
    \u304D, a (<=0) \u70B9\u3092\u5F97\u308B\u3068\u3044\u3046\u6761\u4EF6\u3092\u8FFD\
    \u52A0\u3059\u308B.\n\n        0<=x,y<N\n        a<=0\n        \"\"\"\n\n    \
    \    assert 0<=x<self.N\n        assert 0<=y<self.N\n        assert a<=0\n\n \
    \       self.mutual.append((x,y,-a))\n\n    def set_zero(self,x,a):\n        \"\
    \"\" h(x)=0 \u306E\u3068\u304D, a \u70B9\u3092\u5F97\u308B\u3068\u3044\u3046\u6761\
    \u4EF6\u3092\u8FFD\u52A0\u3059\u308B.\n\n        0<=x<N\n        \"\"\"\n\n  \
    \      assert 0<=x<self.N\n        self.indivi[x][0]+=a\n\n    def set_one(self,x,a):\n\
    \        \"\"\" h(x)=1 \u306E\u3068\u304D, a \u70B9\u3092\u5F97\u308B\u3068\u3044\
    \u3046\u6761\u4EF6\u3092\u8FFD\u52A0\u3059\u308B.\n\n        0<=x<N\n        \"\
    \"\"\n\n        assert 0<=x<self.N\n        self.indivi[x][1]+=a\n\n    def set_all_zero(self,X,a):\n\
    \        \"\"\" h(x)=0 (forall x in X) \u306E\u3068\u304D, a (>=0) \u70B9\u3092\
    \u5F97\u308B\u3068\u3044\u3046\u6761\u4EF6\u3092\u8FFD\u52A0\u3059\u308B.\n\n\
    \        0<=x<N\n        a>=0\n        \"\"\"\n\n        assert a>=0\n\n     \
    \   k=self.__add_vertex_inner()\n        self.base+=a\n\n        self.indivi[k][0]=-a\n\
    \        for x in X:\n            assert 0<=x<self.N\n            self.mutual.append((k,x,inf))\n\
    \n    def set_all_one(self,X,a):\n        \"\"\" h(x)=1 (forall x in X) \u306E\
    \u3068\u304D, a (>=0) \u70B9\u3092\u5F97\u308B\u3068\u3044\u3046\u6761\u4EF6\u3092\
    \u8FFD\u52A0\u3059\u308B.\n\n        0<=x<N\n        a>=0\n        \"\"\"\n\n\
    \        assert a>=0\n\n        k=self.__add_vertex_inner()\n        self.base+=a\n\
    \n        self.indivi[k][1]=-a\n        for x in X:\n            assert 0<=x<self.N\n\
    \            self.mutual.append((x,k,inf))\n\n    def set_not_equal(self,x,y,a):\n\
    \        \"\"\" h(x)!=h(y) \u306A\u3089\u3070, a (<=0) \u70B9\u3092\u5F97\u308B\
    \u3068\u3044\u3046\u6761\u4EF6\u3092\u8FFD\u52A0\u3059\u308B.\n\n        0<=x,y<N\n\
    \        a<=0\n        \"\"\"\n\n        assert 0<=x<self.N and 0<=y<self.N\n\
    \        assert a<=0\n\n        self.set_zero_one(x,y,a)\n        self.set_zero_one(y,x,a)\n\
    \n    def set_equal(self,x,y,a):\n        \"\"\" h(x)=h(y) \u306A\u3089\u3070\
    , a (>=0) \u70B9\u3092\u5F97\u308B\u3068\u3044\u3046\u6761\u4EF6\u3092\u8FFD\u52A0\
    \u3059\u308B.\n\n        0<=x,y<N\n        a>=0\n        \"\"\"\n\n        assert\
    \ 0<=x<self.N and 0<=y<self.N\n        assert a>=0\n\n        self.set_all_zero([x,y],a)\n\
    \        self.set_all_one([x,y],a)\n\n    def ban_zero(self,x):\n        \"\"\"\
    \ h(x)=0 \u3068\u306A\u308B\u3053\u3068\u3092\u7981\u6B62\u3059\u308B. (\u5B9F\
    \u884C\u3057\u305F\u3089 -inf \u70B9\u306B\u306A\u308B)\n\n        0<=x<N\n  \
    \      \"\"\"\n\n        assert 0<=x<self.N\n        self.set_zero(x,-inf)\n\n\
    \    def ban_one(self,x):\n        \"\"\" h(x)=1 \u3068\u306A\u308B\u3053\u3068\
    \u3092\u7981\u6B62\u3059\u308B. (\u5B9F\u884C\u3057\u305F\u3089 -inf \u70B9\u306B\
    \u306A\u308B)\n\n        0<=x<N\n        \"\"\"\n\n        assert 0<=x<self.N\n\
    \        self.set_one(x,-inf)\n\n    def force_zero(self, x):\n        \"\"\"\
    \ h(x) = 0 \u3068\u3044\u3046\u6761\u4EF6\u3092\u8FFD\u52A0\u3059\u308B (\u3064\
    \u307E\u308A, ban_zero(x)).\n\n        0 <= x < N\n        \"\"\"\n\n        assert\
    \ 0 <= x < self.N\n        self.ban_one(x)\n\n    def force_one(self, x):\n  \
    \      \"\"\" h(x) = 1 \u3068\u3044\u3046\u6761\u4EF6\u3092\u8FFD\u52A0\u3059\u308B\
    \ (\u3064\u307E\u308A, ban_one(x)).\n\n        0 <= x < N\n        \"\"\"\n\n\
    \        assert 0 <= x < self.N\n        self.ban_zero(x)\n\n    def increase(self,\
    \ X):\n        \"\"\" h(x[0]) <= h(x[1]) <= ... <= h(x[k-1]) (h(x[i]) = 1, h(x[i+1])\
    \ = 0 \u3092\u7981\u6B62) \u3068\u3044\u3046\u6761\u4EF6\u3092\u8FFD\u52A0\u3059\
    \u308B.\n\n        \"\"\"\n\n        for i in range(len(X) - 1):\n           \
    \ self.set_zero_one(X[i + 1], X[i], -inf)\n\n    def decrease(self, X):\n    \
    \    \"\"\" h(x[0]) >= h(x[1]) >= ... >= h(x[k-1]) (h(x[i]) = 0, h(x[i+1]) = 1\
    \ \u3092\u7981\u6B62) \u3068\u3044\u3046\u6761\u4EF6\u3092\u8FFD\u52A0\u3059\u308B\
    .\n\n        \"\"\"\n\n        self.increase(X[::-1])\n\n    def solve(self,Mode=0):\n\
    \        \"\"\" Project Selection Problem \u3092\u89E3\u304F.\n\n        Mode\n\
    \        0: \u6700\u5927\u5024\u306E\u307F\n        1: \u6700\u5927\u5024\u3068\
    \u305D\u308C\u3092\u9054\u6210\u3059\u308B\u4F8B\n        \"\"\"\n\n        F=MaxFlow(self.ver_num)\n\
    \        base=self.base\n        for i in range(self.N):\n            F.add_arc(self.source,i,0)\n\
    \            F.add_arc(i,self.target,0)\n\n            if self.indivi[i][0]>=0:\n\
    \                base+=self.indivi[i][0]\n                F.add_arc(self.source,i,self.indivi[i][0])\n\
    \            else:\n                F.add_arc(i,self.target,-self.indivi[i][0])\n\
    \n            if self.indivi[i][1]>=0:\n                base+=self.indivi[i][1]\n\
    \                F.add_arc(i,self.target,self.indivi[i][1])\n            else:\n\
    \                F.add_arc(self.source,i,-self.indivi[i][1])\n\n        for i\
    \ in range(self.target+1,self.ver_num):\n            if self.indivi[i][0]!=None:\n\
    \                F.add_arc(self.source,i,-self.indivi[i][0])\n            if self.indivi[i][1]!=None:\n\
    \                F.add_arc(i,self.target,-self.indivi[i][1])\n\n        for x,y,c\
    \ in self.mutual:\n            F.add_arc(x,y,c)\n\n        alpha=F.max_flow(self.source,self.target)\n\
    \        if Mode==0:\n            return base-alpha\n        else:\n         \
    \   return base-alpha, F.min_cut(self.source), self.source, self.target\n"
  dependsOn: []
  isVerificationFile: false
  path: Flow/Project_Selection_Problem.py
  requiredBy: []
  timestamp: '2023-10-29 01:38:54+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Flow/Project_Selection_Problem.py
layout: document
title: Project Selection Problem
---

## Outline

$X,I$ を有限集合とする. 各 $i \in I$ に対して, 観点 $\tau_i: \mathrm{Map}(X, \{0,1\}) \to \mathbb{Z}$ が定まっている.

そして, この観点によって, 評価 $\operatorname{eval}: \mathrm{Map}(X, \{0,1\}) \to \mathbb{Z}$ を
$$\operatorname{eval}(h) := \sum_{i \in I} \tau_i(h)$$
として定める.

このとき, $h \in \mathrm{Map}(X, \{0,1\})$ における $\operatorname{eval}(h)$ の最大値と, 最大値を達成する $h$ を求める.

## Theory

$\tau_i$ が全て特殊な形であるとき, この問題は最小カット問題に帰着できる. そして, 最小カット問題は最大フロー問題の双対問題である. 従って, 最大フロー問題で解くことができる.

最大フロー問題で解くことができるような $\tau_i$ は以下のような形式である.

ただし,

* $x_i, y_i, z_{i,j} \in X$.
* $a_i, b_i$ は整数, $a_{+,i}$ は非負の整数, $a_{-,i}$ は非正の整数.

とする.

* $\tau_i(h) =\begin{cases} a_i & (h(x_i) = 0) \\ b_i & (h(x_i) = 1) \end{cases}$
* $\tau_i(h) = \begin{cases} a_{-,i} & (h(x_i) = 0, h(y_i) = 1) \\ 0 & (\text{otherwise}) \end{cases}$
* $\tau_i(h) = \begin{cases} a_{+,i} & (h(z_{i,1}) = \dots = h(z_{i, k_i}) = 0) \\ 0 & (\text{otherwise}) \end{cases}$
* $\tau_i(h) = \begin{cases} a_{+,i} & (h(z_{i,1}) = \dots = h(z_{i, k_i}) = 1) \\ 0 & (\text{otherwise}) \end{cases}$

---
なお, 以下の場合については, 一般的には対応できないが, 特殊な状況下では適当な変形によって最小カットに帰着できる.

(Pattern 1)

* 任意の $i \in I$ に対して, $\tau_i$ は以下の形式のいずれかである.
  * $\tau_i(h) =\begin{cases} a_i & (h(x_i) = 0) \\ b_i & (h(x_i) = 1) \end{cases}$
  * $\tau_i(h) = \begin{cases} a_{-,i} & (h(x_i) = h(y_i) = 0) \\ 0 & (\text{otherwise}) \end{cases}$
  * $\tau_i(h) = \begin{cases} a_{-,i} & (h(x_i) = h(y_i) = 1) \\ 0 & (\text{otherwise}) \end{cases}$
* $2$ 番目または $3$ 番目の形である $i \in I$ 全体の集合を $J$ として, $$E:=\{x_j y_j \mid j \in J\}$$ としたとき, 無向グラフ $(X,E)$ は二部グラフになる.

このとき, 二部グラフ $(X,E)$ の部集合を $A,B$ とする. $\bullet': \mathrm{Map}(X, \{0,1\}) \to \mathrm{Map}(X, \{0,1\})$ を
$$h'(x) = \begin{cases} h(x) & (x \in A) \\ 1-h(x) & (x \in B) \end{cases}$$
と定めると, $\bullet'$ は全単射になり, $h'$ に関して最小カットへ帰着できる.

(Pattern 2)

* 任意の $i \in I$ に対して, $\tau_i$ は以下の形式のいずれかである.
  * $\tau_i(h) =\begin{cases} a_i & (h(x_i) = 0) \\ b_i & (h(x_i) = 1) \end{cases}$
  * $\tau_i(h) = \begin{cases} a_{+,i} & (h(x_i) \neq h(y_i)) \\ 0 & (\text{otherwise}) \end{cases}$
* $2$ 番目の形である $i \in I$ 全体の集合を $J$ として, $$E:=\{x_j y_j \mid j \in J\}$$ としたとき, 無向グラフ $(X,E)$ は二部グラフになる.

このとき, $\bullet'$ を考えることにより, 次のようにして帰着できる.

* $\displaystyle \sum_{j \in J} a_{+,j}$ 点の下駄を履かせて, 「$h(x_j)=h(y_j)$ ならば $-a_{+,j}$ 点を得る」に置き換えることにより, (Pattern 1) に帰着させる.

このとき, 帰着先での最大値を $X$ としたとき, 本問題での最大値は $\displaystyle \left(\sum_{j \in J} a_{+,j} + X \right)$ であることに注意.
