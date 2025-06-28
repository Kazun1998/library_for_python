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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.13.5/x64/lib/python3.13/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.13.5/x64/lib/python3.13/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class Topological_Sort:\n    __slots__=(\"__arc\", \"__rev\", \"__reflexive\"\
    , \"__is_DAG\", \"__order\")\n\n    def __init__(self, N: int, reflexive: bool\
    \ = False):\n        \"\"\" N \u9802\u70B9\u304B\u3089\u306A\u308B\u6709\u5411\
    \u7A7A\u30B0\u30E9\u30D5\u3092\u751F\u6210\u3059\u308B.\n\n        Args:\n   \
    \         N (int): \u9802\u70B9\u6570\n            reflexive (bool, optional):\
    \ True \u306B\u3059\u308B\u3068, \u81EA\u5DF1\u30EB\u30FC\u30D7\u306E\u8FFD\u52A0\
    \u3092\u8A8D\u3081\u308B. Defaults to False.\n        \"\"\"\n\n        self.__arc=[[]\
    \ for _ in  range(N)]\n        self.__rev=[[] for _ in range(N)]\n        self.__reflexive=reflexive\n\
    \n    @property\n    def N(self):\n        return len(self.__arc)\n\n    @property\n\
    \    def reflexive(self):\n        return self.__reflexive\n\n    def add_arc(self,\
    \ source: int, target: int):\n        \"\"\" source \u304B\u3089 target \u3078\
    \u306E\u5F27\u3092\u8FFD\u52A0\u3059\u308B.\n\n        Args:\n            source\
    \ (int): \u59CB\u70B9\n            target (int): \u7D42\u70B9\n        \"\"\"\n\
    \n        # \u81EA\u5DF1\u30EB\u30FC\u30D7\u3092\u8A8D\u3081\u306A\u3044\u5834\
    \u5408\u306E source == target \u306E\u3068\u304D\u306F\u68C4\u5374\u3059\u308B\
    .\n        if source == target and (not self.reflexive):\n            return\n\
    \n        self.__arc[source].append(target)\n        self.__rev[target].append(source)\n\
    \n    def add_vertex(self) -> int:\n        \"\"\" 1 \u9802\u70B9\u8FFD\u52A0\n\
    \n        Returns:\n            int: \u8FFD\u52A0\u3055\u308C\u305F\u9802\u70B9\
    \u306E\u9802\u70B9\u756A\u53F7\n        \"\"\"\n\n        self.__arc.append([])\n\
    \        self.__rev.append([])\n        return self.N - 1\n\n    def add_arc_multiple(self,\
    \ sources: list[int], targets: list[int]) -> int:\n        \"\"\" \u4EFB\u610F\
    \u306E s in sources, t in targets \u306B\u5BFE\u3057\u3066, s \u304B\u3089 t \u3078\
    \u306E\u5F27\u3092\u4F5C\u6210\u3059\u308B (\u4EEE\u60F3\u7684\u306B 1 \u9802\u70B9\
    \u3092\u8FFD\u52A0\u3059\u308B).\n\n        Args:\n            sources (list[int]):\
    \ \u59CB\u70B9\u306E\u30EA\u30B9\u30C8\n            targets (list[int]): \u7D42\
    \u70B9\u306E\u30EA\u30B9\u30C8\n\n        Returns:\n            int: \u8D85\u9802\
    \u70B9\u3068\u3057\u3066\u8FFD\u52A0\u3055\u308C\u305F\u9802\u70B9\u306E\u756A\
    \u53F7\n        \"\"\"\n\n        # \u65B9\u91DD\n        # (1) \u8D85\u9802\u70B9\
    \ x \u3092\u8FFD\u52A0\u3059\u308B.\n        # (2) \u4EFB\u610F\u306E s in sources\
    \ \u306B\u5BFE\u3057\u3066, \u5F27 sx \u3092\u8FFD\u52A0\u3059\u308B.\n      \
    \  # (3) \u4EFB\u610F\u306E t in targets \u306B\u5BFE\u3057\u3066, \u5F27 xt \u3092\
    \u8FFD\u52A0\u3059\u308B.\n        # \u3053\u306E\u3088\u3046\u306B\u3059\u308B\
    \u3053\u3068\u3067, \u8FFD\u52A0\u3059\u308B\u5F27\u306E\u6570\u3092 |sources|\
    \ x |targets| \u304B\u3089 |sources| + |targets| \u306B\u843D\u3068\u305B\u308B\
    .\n\n        x = self.add_vertex()\n        for s in sources:\n            self.add_arc(s,\
    \ x)\n\n        for t in targets:\n            self.add_arc(x, t)\n\n    def calculate(self):\n\
    \        \"\"\" DAG \u306B\u95A2\u3059\u308B\u8A08\u7B97\u3092\u884C\u3046.\n\
    \        \"\"\"\n\n        in_deg = [len(self.__rev[x]) for x in range(self.N)]\n\
    \        order = []\n        stack = [x for x in range(self.N) if in_deg[x] ==\
    \ 0]\n\n        while stack:\n            x = stack.pop()\n            order.append(x)\n\
    \n            for y in self.__arc[x]:\n                in_deg[y] -= 1\n      \
    \          if in_deg[y] == 0:\n                    stack.append(y)\n\n       \
    \ if len(order) == self.N:\n            self.__is_DAG = True\n            self.__order\
    \ = order\n        else:\n            self.__is_DAG = False\n            self.__order\
    \ = None\n\n    @property\n    def is_DAG(self):\n        return self.__is_DAG\n\
    \n    @property\n    def order(self):\n        return self.__order\n"
  dependsOn: []
  isVerificationFile: false
  path: Topological_Sort.py
  requiredBy: []
  timestamp: '2025-03-14 00:26:13+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Topological_Sort.py
layout: document
title: Topological Sort
---

## Outline

有向グラフ $D = (V, A)$ に対して, $V$ 上の全順序関係 $\leq$ が $D$ のトポロジカルソートであるとは, 以下を満たすことである.

* 任意の $u, v \in V~(u \neq v)$ に対して, $\overrightarrow{uv} \in A$ ならば, $u \leq v$ である.

位数 $N$, サイズ $M$ の有向グラフ $D$ に対して, $D$ のトポロジカルソートの存在判定及び構築を $O(N + M)$ 時間で行う.

## Theory

有向グラフ $D = (V, A)$ に対して, 以下が同値になる.

* (a) $D$ のトポロジカルソートが存在する.
* (b) $D$ において, サイクルが存在しない.

これを証明する.

### Proof

#### (a) ならば (b)

対偶を証明する. $D$ 上の有向サイクルを $v_1 v_2 \dots v_k$ ($k$ 個の頂点は全て相異なる) とする.

$\leq$ を $D$ 上の Topological Sort とする. ここで, サイクルの対称性により,

$$ v_1 = \min_{\leq}(v_1, v_2, \dots, v_k) $$

であるとしても一般性を失わない.

すると, $\overrightarrow{v_k v_1} \in A$ となるが, $\leq$ が Topological Sort より $v_k \leq v_1$ である.

一方で, $v_1$ の定め方より, $v_1 \leq v_k$ である.

$\leq$ が全順序であるので, $v_1 = v_k$ となる.

しかし, $v_1, \dots, v_k$ が相異なる $k$ 個の頂点であることに矛盾する.

よって, $D$ に Topological Sort は存在しない.

#### (b) ならば (a)

DAG $D$ の位数 $n$ に関する数学的帰納法で示す.

$1$ 頂点のときは任意の順序がトポロジカルソートになる.

$(n-1)$ 頂点の任意の DAG が Topological Sort を持つと仮定する. $D$ が $n$ 頂点の DAG とする.

$D$ は DAG なので, 入近傍が存在しない頂点 $x \in V$ が存在する. $D$ から頂点 $x$ を除いた $D$ の部分グラフ $D' := D - x$ は $D$ が DAG であるから, $D'$ も DAG である.

$D'$ の位数が $(n-1)$ であるので, 数学的帰納法の仮定により, $D'$ の Topological Sort $\leq'$ が存在する.

この $\leq'$ を用いて, $V$ 上の関係 $\leq$ を次のようにして定義する. ただし, $u,v \in V$ とする.

$$ u \leq v :\iff (u = x) \lor (u,v \neq x \land u \leq' v) $$

すると, この $\leq$ は $D$ 上の Topological Sort になる. 実際, $\overrightarrow{uv} \in A~(u \neq v)$ に対して,

* $u = x$ のときは, $\leq$ の定義により $u \leq v$ である.
* $v = x$ とはなり得ない. これは $x$ が $D$ 上で入近傍が存在しない頂点として取ってきており, $u \neq v$ であることから従う.
* $u,v \neq x$ のときは, $u \leq' v$ より $u \leq v$ となる.

この同値性における 「(b) ならば (a)」の証明を利用することによって, Topological Sort の判定と構築を行うことができる.
