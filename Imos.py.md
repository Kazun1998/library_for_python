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
  code: "class Imos_1:\n    def __init__(self, N: int):\n        \"\"\" \u533A\u9593\
    \ 0 <= t < N \u306B\u5BFE\u3059\u308B Imos \u6CD5\u306E\u30C7\u30FC\u30BF\u69CB\
    \u9020\u3092\u4F5C\u6210\u3059\u308B.\n\n        Args:\n            N (int): \u5E45\
    \n        \"\"\"\n\n        self.__lazy = [0] * (N + 1)\n\n    def __len__(self)\
    \ -> int:\n        return len(self.__lazy) - 1\n\n    def add(self, l: int, r:\
    \ int, x: int = 1):\n        \"\"\" \u9589\u533A\u9593 [l, r] \u306B x \u3092\u52A0\
    \u7B97\u3059\u308B.\n\n        Args:\n            l (int): \u5DE6\u7AEF\n    \
    \        r (int): \u53F3\u7AEF\n            x (int, optional): \u52A0\u7B97\u3059\
    \u308B\u5024. Defaults to 1.\n        \"\"\"\n\n        if l > r:\n          \
    \  return\n\n        if 0 <= l < len(self):\n            self.__lazy[l] += x\n\
    \n        if 0 <= r < len(self):\n            self.__lazy[r + 1] -= x\n\n    def\
    \ cumulate(self) -> list[int]:\n        \"\"\" \u7D2F\u7A4D\u548C\u3092\u6C42\u3081\
    \u308B.\n\n        Returns:\n            list[int]: \u7D2F\u7A4D\u548C\n     \
    \   \"\"\"\n\n        y = self.__lazy.copy()[:-1]\n        for i in range(1, len(self)):\n\
    \            y[i] += y[i - 1]\n\n        return y\n\n#=================================================\n\
    from collections import defaultdict\nclass Sparse_Imos_1:\n    def __init__(self):\n\
    \        self.dict = defaultdict(int)\n\n    def add(self, l: int, r: int, x:\
    \ int = 1):\n        \"\"\" \u9589\u533A\u9593 [l,r] \u306B x \u3092\u52A0\u7B97\
    \u3059\u308B.\n\n        Args:\n            l (int): \u5DE6\u7AEF\n          \
    \  r (int): \u53F3\u7AEF\n            x (int, optional): \u52A0\u7B97\u3059\u308B\
    \u5024. Defaults to 1.\n        \"\"\"\n\n        if l > r:\n            return\n\
    \n        self.dict[l] += x\n        self.dict[r + 1] -= x\n\n    def cumulative(self,\
    \ since: int, until: int) -> list[tuple[int, int, int]]:\n        \"\"\" since\
    \ \u304B\u3089 until \u307E\u3067\u306E\u7D2F\u7A4D\u548C\u3092\u6C42\u3081\u308B\
    .\n\n        Args:\n            since (int): \u59CB\u70B9\n            until (int):\
    \ \u7D42\u70B9\n\n        Returns:\n            list[tuple[int, int, int]]: (y,\
    \ l, r) \u3068\u3044\u3046\u5F62\u306E\u30EA\u30B9\u30C8.\n                (y,\
    \ l, r) \u306F l <= x <= r \u306E\u7BC4\u56F2\u306B\u304A\u3044\u3066\u306F\u7D2F\
    \u7A4D\u548C\u304C y \u3067\u3042\u308B\u3068\u3044\u3046\u3053\u3068\u3092\u610F\
    \u5473\u3059\u308B.\n        \"\"\"\n\n        res: list[tuple[int, int, int]]\
    \ = []\n        cum = 0\n        t_old = since\n        dic = self.dict\n    \
    \    for t in sorted(dic):\n            if t > until:\n                break\n\
    \n            if dic[t] == 0:\n                continue\n\n            if t_old\
    \ <= t - 1:\n                res.append((cum, t_old, t - 1))\n\n            cum\
    \ += dic[t]\n            t_old = t\n\n        if t_old <= until:\n           \
    \ res.append((cum, t_old, until))\n\n        return res\n\n#=================================================\n\
    class Linear_Imos_1:\n    def __init__(self, N: int):\n        \"\"\" \u9577\u3055\
    \u304C N \u306E 1 \u6B21\u5F0F\u5BFE\u5FDC Imos \u6CD5\u30AF\u30E9\u30B9\u306E\
    \u30A4\u30F3\u30B9\u30BF\u30F3\u30B9\u3092\u4F5C\u6210\u3059\u308B.\n\n      \
    \  Args:\n            N (int): \u5E45\n        \"\"\"\n\n        # 1 \u6B21\u5F0F\
    \u3092\u52A0\u7B97\u3059\u308B \u2192 \u7D2F\u7A4D\u548C\u306F 2 \u56DE\u3068\u308B\
    \ \u2192 \u9045\u5EF6\u914D\u5217\u306E\u9577\u3055\u306F (N + 2)\n        self.__lazy\
    \ = [0] * (N + 2)\n\n    def __len__(self) -> int:\n        return len(self.__lazy)\
    \ - 2\n\n    def add(self, l: int, r: int, x: int = 1):\n        \"\"\" \u9589\
    \u533A\u9593 [l, r] \u306B\u4E00\u69D8\u306B x \u3092\u52A0\u7B97\u3059\u308B\
    .\n\n        Args:\n            l (int): \u5DE6\u7AEF\n            r (int): \u53F3\
    \u7AEF\n            x (int, optional): \u52A0\u7B97\u3059\u308B\u5024. Defaults\
    \ to 1.\n        \"\"\"\n\n        self.add_linear(l, r, x, 0)\n\n    def add_linear(self,\
    \ l: int, r: int, a: int, b: int):\n        \"\"\" \u9589\u533A\u9593 [l, r] \u306B\
    \u6B21\u306E\u3088\u3046\u306B\u3057\u3066\u52A0\u7B97\u3059\u308B.\n        I[l]\
    \ += a, I[l + 1] += a + b, I[l + 2] += a +2b, ..., I[t] += a + (t - r) b, ...,\
    \  I[r] += a + (r - l) b\n\n        Args:\n            l (int): \u5DE6\u7AEF\n\
    \            r (int): \u53F3\u7AEF\n            a (int): 1 \u6B21\u5F0F\u306E\u5B9A\
    \u6570\u9805\n            b (int): 1 \u6B21\u5F0F\u306E\u50BE\u304D\n        \"\
    \"\"\n\n        if l < 0:\n            a += b * (-l)\n            l = 0\n\n  \
    \      r = min(r, len(self) - 1)\n\n        if l > r:\n            return\n\n\
    \        lazy = self.__lazy\n        difference = [(l, a), (l + 1, -a + b), (r\
    \ + 1, -a - (r - l + 1) * b), (r + 2, a + (r - l) * b)]\n        for k, x in difference:\n\
    \            lazy[k] += x\n\n    def add_mountain(self, l: int, m: int, a: int,\
    \ b: int):\n        \"\"\" \u9589\u533A\u9593 [l, l + 2m] \u306B\u6B21\u306E\u3088\
    \u3046\u306B\u5C71\u578B\u306B\u52A0\u7B97\u3059\u308B.\n        I[l] += a, I[l\
    \ + 1] = a + b, I[l + 2] = a + 2b, ..., I[l + m] = a + mb\n        I[l + m + 1]\
    \ += a + (m - 1)b, I[l + m + 2] += a + (m - 2)b, ..., I[l + 2m - 1] += a + b,\
    \ I[l + 2m] += a\n\n        Args:\n            l (int): \u5DE6\u7AEF\n       \
    \     m (int): \u5C71\u306E\u9577\u3055\n            a (int): \u5B9A\u6570\u9805\
    \n            b (int): 1 \u6B21\u5F0F\u306E\u50BE\u304D\n        \"\"\"\n    \
    \    self.add_linear(l, l + m, a, b)\n        self.add_linear(l + m + 1, l + 2\
    \ * m, a + (m - 1) * b, -b)\n\n    def add_slide_multiple(self, l: int, k: int,\
    \ m: int, a: int):\n        \"\"\" \u4EE5\u4E0B\u3092 k \u500B\u306E\u6574\u6570\
    \ t = l, l + 1, ..., l + (k - 1) \u306B\u5BFE\u3057\u3066\u884C\u3046.\n     \
    \   (\u64CD\u4F5C): \u9577\u3055 m \u306E\u9023\u7D9A\u533A\u9593 x = t, t + 1,\
    \ ..., t + (m - 1) \u306B\u5BFE\u3057\u3066, \u4E00\u69D8\u306B a \u3092\u52A0\
    \u7B97\u3059\u308B.\n\n        Args:\n            l (int): \u64CD\u4F5C\u306E\u59CB\
    \u70B9\n            k (int): \u64CD\u4F5C\u306E\u56DE\u6570\n            m (int):\
    \ 1 \u56DE\u306E\u64CD\u4F5C\u3067\u52A0\u7B97\u3059\u308B\u9805\u306E\u6570\n\
    \            a (int): \u52A0\u7B97\u3059\u308B\u5024\n        \"\"\"\n       \
    \ if m <= 0:\n            return\n\n        if k >= m:\n            self.add_linear(l,\
    \ l + (m - 2), a, a)\n            self.add(l + (m - 1), l + k - 1, a * m)\n  \
    \          self.add_linear(l + k, l + k + m - 1, a * (m - 1), -a)\n        else:\n\
    \            self.add_linear(l, l + (k - 1), a, a)\n            self.add(l + k,\
    \ l + m - 2, a * k)\n            self.add_linear(l + m - 1, l + (m - 1) + (k -\
    \ 1), a * k, -a)\n\n    def cumulate(self) -> list[int]:\n        \"\"\" \u7D2F\
    \u7A4D\u548C\u3092\u6C42\u3081\u308B.\n\n        Returns:\n            list[int]:\
    \ \u7D2F\u7A4D\u548C\n        \"\"\"\n\n        y = self.__lazy.copy()[:-2]\n\
    \        for _ in range(2):\n            for i in range(1, len(self)):\n     \
    \           y[i] += y[i - 1]\n        return y\n\n#=================================================\n\
    class Imos_2:\n    def __init__(self, W: int, H: int):\n        self.__width =\
    \ W\n        self.__height = H\n        self.list=[[0]*(W+1) for _ in range(H+1)]\n\
    \n    @property\n    def width(self) -> int:\n        return self.__width\n\n\
    \    @property\n    def height(self) -> int:\n        return self.__height\n\n\
    \    def add(self, i0: int, j0: int, i1: int, j1: int, x: int = 1):\n        \"\
    \"\" \u9589\u533A\u9593 [i0, j0] x [i1, j1] \u306B x \u3092\u52A0\u7B97\u3059\u308B\
    .\n\n        Args:\n            i0 (int): \u5DE6\u7AEF\n            j0 (int):\
    \ \u4E0A\u7AEF\n            i1 (int): \u53F3\u7AEF\n            j1 (int): \u4E0B\
    \u7AEF\n            x (int, optional): \u52A0\u7B97\u3059\u308B\u5024. Defaults\
    \ to 1.\n        \"\"\"\n\n        self.list[i0][j0] += x\n        self.list[i0][j1\
    \ + 1] -= x\n        self.list[i1 + 1][j0] -= x\n        self.list[i1 + 1][j1\
    \ + 1] += x\n\n    def add_row(self, i: int, x: int):\n        \"\"\" \u7B2C i\
    \ \u884C (i, *) \u306B x \u3092\u52A0\u3048\u308B.\n\n        Args:\n        \
    \    i (int): \u884C\u756A\u53F7\n            x (int): \u52A0\u7B97\u3059\u308B\
    \u5024\n        \"\"\"\n        self.add(i, 0, i, self.width - 1, x)\n\n    def\
    \ add_column(self, j: int, x: int):\n        \"\"\" \u7B2C j \u5217 (*, j) \u306B\
    \ x \u3092\u52A0\u3048\u308B.\n\n        Args:\n            j (int): \u5217\u756A\
    \u53F7\n            x (int): \u52A0\u7B97\u3059\u308B\u5024\n        \"\"\"\n\
    \        self.add(0, j, self.height - 1, j, x)\n\n    def cumulate(self):\n  \
    \      Y=[self.list[i].copy()[:-1] for i in range(self.height)]\n\n        for\
    \ _ in range(2):\n            for i in range(len(Y)):\n                y=Y[i]\n\
    \                for j in range(1,len(y)):\n                    y[j]+=y[j-1]\n\
    \            Y=[list(y) for y in zip(*Y)]\n        return Y\n"
  dependsOn: []
  isVerificationFile: false
  path: Imos.py
  requiredBy: []
  timestamp: '2025-06-01 13:49:00+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Imos.py
layout: document
title: "Imos \u6CD5"
---

## Outline

最初に $M$ 個の区間加算クエリが与えられた後の $Q$ 個の一点取得クエリの処理をまとめて $O(M + Q)$ 時間で行うことができる.

## Theory

$R$ を環として, $\mathcal{A}$ を $R$ を要素に持つ列全体の集合とする. このとき, $\mathcal{A}$ は区間ごとの和とスカラー倍によって, $R$ 係数の加群と見ることができる.

写像 $D: \mathcal{A} \to \mathcal{A}$ を

$$ D\boldsymbol{e}_n := \boldsymbol{e}_n - \boldsymbol{e}_{n+1} $$

となるような線形写像で定める. ただし, $\boldsymbol{e}_n$ とは, 第 $n$ 項のみ $1$ でそれ以外が全て $0$ である列とする.

すると,

$$ D \left(\sum_{n=l}^r \boldsymbol{e}_n \right) = \sum_{n=l}^r D \boldsymbol{e}_n = \sum_{n=l}^r (\boldsymbol{e}_n - \boldsymbol{e}_{n+1}) = \boldsymbol{e}_l - \boldsymbol{e}_{r+1} $$

になる.

従って, $Q$ 個の区間加算クエリの合計を $D$ で送った像は次のように, $2Q$ 個の項の和で表すことができる.

$$ \begin{align*}
  D \left(\sum_{q=1}^Q \left( \alpha_q \sum_{n={l_q}}^{r_q} \boldsymbol{e}_n \right) \right)
  &= \sum_{q=1}^Q \alpha_q \left(D \sum_{n={l_q}}^{r_q} \boldsymbol{e}_n \right) \\
  &= \sum_{q=1}^Q \alpha_q (\boldsymbol{e}_{l_q} - \boldsymbol{e}_{r_q + 1}) \\
  &= \sum_{q=1}^Q (\alpha_q \boldsymbol{e}_{l_q} - \alpha \boldsymbol{e}_{r_q + 1})
\end{align*} $$

そして, $D$ は同型写像になる. 実際, $D^{-1}: \mathcal{A} \to \mathcal{A}$ は以下を満たす線形写像となる.

$$ D^{-1} \boldsymbol{e}_n = \sum_{k=0}^n \boldsymbol{e}_k $$

よって,

$$ \boldsymbol{x} := \sum_{n=0}^\infty \alpha_n \boldsymbol{e}_n $$

とすると,

$$ T_n D^{-1} \boldsymbol{x} = \sum_{k=0}^n \alpha_k $$

となる. 特に, $n \geq 1$ のときは

$$ T_n D^{-1} \boldsymbol{x} = T_{n-1} D^{-1} \boldsymbol{x} + \alpha_n $$

となる. これはまさに $(T_n D^{-1} \boldsymbol{x})$ の累積和を表している式になる.

以上から,

$$ \boldsymbol{y} := \sum_{q=1}^Q \left( \alpha_q \sum_{n={l_q}}^{r_q} \boldsymbol{e}_n \right) $$

は

$$ \boldsymbol{x} := D \boldsymbol{y} = \sum_{q=1}^Q (\alpha_q \boldsymbol{e}_{l_q} - \boldsymbol{e}_{r_q + 1}) $$

として, $\beta_n$ を $\beta_n := T_n \boldsymbol{x}$ で定めることによって,

$$ T_n \boldsymbol{y} = \begin{cases} \beta_0 & (n = 0) \\ T_{n-1} \boldsymbol{y} + \beta_n & (n \geq 1) \end{cases} $$

で求められる.
