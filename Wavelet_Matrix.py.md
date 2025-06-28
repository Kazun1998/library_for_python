---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test_verify/yosupo_library_checker/Data_Structure/Range_Kth_Smallest.test.py
    title: test_verify/yosupo_library_checker/Data_Structure/Range_Kth_Smallest.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links:
    - https://judge.yosupo.jp/submission/33990
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.13.5/x64/lib/python3.13/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.13.5/x64/lib/python3.13/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class Fully_Indexable_Dictionary:\n    \"\"\"\n    references:\n    https://judge.yosupo.jp/submission/33990\n\
    \    \"\"\"\n\n    bucket_size = 32\n\n    def __init__(self, n: int):\n     \
    \   \"\"\" \u9577\u3055 n \u306E\u5B8C\u5099\u8F9E\u66F8\u3092\u751F\u6210\u3059\
    \u308B.\n\n        Args:\n            n (int): \u9577\u3055\n        \"\"\"\n\n\
    \        self.__n = n\n        self.__bucket_number = (n - 1) // self.bucket_size\
    \ + 1\n        self.bit = [0] * self.bucket_number\n        self.mask=[(1<<i)-1\
    \ for i in range(1<<5)]\n\n    def __popcount(self, x: int):\n        x = x -\
    \ ((x >> 1) & 0x55555555)\n        x = (x & 0x33333333) + ((x >> 2) & 0x33333333)\n\
    \        x = x + (x >> 4) & 0x0f0f0f0f\n        x = x + (x >> 8)\n        x =\
    \ x + (x >> 16)\n        return x & 0x0000007f\n\n    def __len__(self) -> int:\n\
    \        return self.__n\n\n    @property\n    def bucket_number(self) -> int:\n\
    \        return self.__bucket_number\n\n    def set(self, index: int, bit: int):\n\
    \        \"\"\" \u7B2C index \u8981\u7D20\u3092 bit \u306B\u5909\u66F4\u3059\u308B\
    .\n\n        Args:\n            index (int): \u8981\u7D20\u756A\u53F7\n      \
    \      bit (int): 0 or 1\n        \"\"\"\n\n        if index < 0:\n          \
    \  index += len(self)\n\n        if bit:\n            self.bit[index >> 5] |=\
    \ 1 << (index & 31)\n        else:\n            self.bit[index >> 5] &= ~(1 <<\
    \ (index & 31))\n\n    def build(self):\n        \"\"\" \u30C7\u30FC\u30BF\u69CB\
    \u9020\u3092\u78BA\u5B9A\u3055\u305B\u308B. \u203B \u4EE5\u964D, set \u306E\u4F7F\
    \u7528\u7981\u6B62\n\n        \"\"\"\n\n        # self.total[k] := 0, 1, ...,\
    \ k - 1 \u756A\u76EE\u306E k \u500B\u306E\u30D0\u30B1\u30C3\u30C8\u306B\u304A\u3051\
    \u308B bit \u306E\u7DCF\u548C\n\n        self.total = [0] * self.bucket_number\n\
    \        for k in range(1, self.bucket_number):\n            self.total[k] = self.total[k\
    \ - 1] + self.__popcount(self.bit[k - 1])\n\n    def access(self, index: int)\
    \ -> int:\n        \"\"\" \u7B2C index \u8981\u7D20\u3092\u51FA\u529B\u3059\u308B\
    .\n\n        Args:\n            index (int): \u8981\u7D20\u756A\u53F7\n\n    \
    \    Returns:\n            int: 0 or 1\n        \"\"\"\n\n        if index < 0:\n\
    \            index += len(self)\n\n        return (self.bit[index >> 5] >> (index\
    \ & 31)) & 1\n\n    __getitem__ = access\n\n    def rank(self, index: int, bit:\
    \ int) -> int:\n        \"\"\" [0, index) \u306B\u3042\u308B bit \u306E\u6570\u3092\
    \u6C42\u3081\u308B.\n\n        Args:\n            index (int): \u5DE6\u7AEF\n\
    \            bit (int): \u6C42\u3081\u308B bit\n\n        Returns:\n         \
    \   int: [0, index) \u306B\u3042\u308B bit \u306E\u6570\n        \"\"\"\n    \
    \    if index <= 0:\n            return 0\n\n        index = min(index, len(self))\n\
    \n        if index < len(self):\n            alpha = self.total[index >> 5] +\
    \ self.__popcount(self.bit[index >> 5] & self.mask[index & 31])\n        else:\n\
    \            alpha = self.total[-1] + self.__popcount(self.bit[-1])\n\n      \
    \  return alpha if bit else index-alpha\n\n    def select(self, k: int, bit: int,\
    \ default: int = -1) -> int:\n        \"\"\" \u5148\u982D\u304B\u3089 k (1-indexed)\
    \ \u756A\u76EE\u306E bit \u306E\u4F4D\u7F6E\u3092\u6C42\u3081\u308B (\u5B58\u5728\
    \u3057\u306A\u3044\u5834\u5408\u306F default).\n\n        Args:\n            k\
    \ (int): 1-indexed \u306B\u304A\u3051\u308B\u51FA\u73FE\u56DE\u6570\n        \
    \    bit (int): 0 or 1\n            default (int, optional): k \u756A\u76EE\u306E\
    \ bit \u304C\u5B58\u5728\u3057\u306A\u3044\u5834\u5408\u306E\u8FD4\u308A\u5024\
    . Defaults to -1.\n\n        Returns:\n            int: k \u756A\u76EE\u306E bit\
    \ \u306E\u4F4D\u7F6E\n        \"\"\"\n\n        if (k < 1 or self.rank(len(self),\
    \ bit) < k):\n            return default\n\n        l, r = 0, len(self)\n    \
    \    while r - l > 1:\n            m = (l + r) // 2\n            if self.rank(m,\
    \ bit) >= k:\n                r = m\n            else:\n                l = m\n\
    \        return l\n\nclass Wavelet_Matrix:\n    def __init__(self, X: list[int]):\n\
    \        \"\"\" X \u306B\u95A2\u3059\u308B Wavelet Matrix \u3092\u751F\u6210\u3059\
    \u308B.\n\n        Args:\n            X (list[int]): \u6574\u6570\u304B\u3089\u306A\
    \u308B\u30EA\u30B9\u30C8\n        \"\"\"\n\n        self.__n = N = len(X)\n\n\
    \        self.value_list = sorted(set(X))\n        self.value_dict = { x: i for\
    \ i, x in enumerate(self.value_list) }\n\n        self.__bit_size = len(self.value_dict).bit_length()\n\
    \n        self.zero_count = [0] * self.bit_size\n        self.dictionaries = [Fully_Indexable_Dictionary(N)\
    \ for _ in range(self.bit_size)]\n\n        Y = [self.value_dict[x] for x in X]\n\
    \        for lv in range(self.bit_size - 1, -1, -1):\n            dictionary =\
    \ self.dictionaries[~lv]\n            left = []\n            right = []\n    \
    \        for i in range(N):\n                if (Y[i] >> lv) & 1:\n          \
    \          dictionary.set(i, 1)\n                    right.append(Y[i])\n    \
    \            else:\n                    left.append(Y[i])\n\n            dictionary.build()\n\
    \            self.zero_count[~lv] = len(left)\n\n            Y = left + right\n\
    \n        self.begin = [0] * len(self.value_dict)\n        for i in range(N -\
    \ 1, -1, -1):\n            self.begin[Y[i]] = i\n\n    def access(self, index:\
    \ int) -> int:\n        \"\"\" \u7B2C index \u8981\u7D20\u306E\u5024\u3092\u6C42\
    \u3081\u308B.\n\n        Args:\n            index (int): \u8981\u7D20\u756A\u53F7\
    \n\n        Returns:\n            int: \u7B2C index \u8981\u7D20\n        \"\"\
    \"\n\n        if index < 0:\n            index += len(self)\n\n        p = 0\n\
    \        for lv in range(self.bit_size):\n            dictionary = self.dictionaries[lv]\n\
    \            bit = dictionary.access(index)\n            p = (p << 1) | bit\n\n\
    \            if bit:\n                index = self.zero_count[lv] + dictionary.rank(index,\
    \ 1)\n            else:\n                index = dictionary.rank(index ,0)\n\n\
    \        return self.value_list[p]\n\n    __getitem__ = access\n\n    def __len__(self)\
    \ -> int:\n        return self.__n\n\n    @property\n    def bit_size(self) ->\
    \ int:\n        return self.__bit_size\n\n    def rank(self, i: int, v: int) ->\
    \ int:\n        \"\"\" [0,i) \u306B\u3042\u308B value \u306E\u500B\u6570\u3092\
    \u6C42\u3081\u308B.\n\n        Args:\n            i (int): \u53F3\u7AEF (\u7B2C\
    \ i \u8981\u7D20\u306F\u542B\u307E\u306A\u3044)\n            v (int): \u5024\n\
    \n        Returns:\n            int: [0, i) \u306B\u3042\u308B v \u306E\u500B\u6570\
    \n        \"\"\"\n        return self.range_rank(0, i, v)\n\n    def range_rank(self,\
    \ l: int, r: int, v: int) -> int:\n        \"\"\" [l, r) \u306B\u3042\u308B v\
    \ \u306E\u500B\u6570\u3092\u6C42\u3081\u308B.\n\n        Args:\n            l\
    \ (int): \u5DE6\u7AEF\n            r (int): \u53F3\u7AEF (\u7B2C r \u9805\u81EA\
    \u8EAB\u306F\u542B\u3081\u306A\u3044)\n            value (int): \u5024\n\n   \
    \     Returns:\n            int: [l, r) \u306B\u3042\u308B v \u306E\u500B\u6570\
    \n        \"\"\"\n\n        if (value := self.value_dict.get(v, None)) is None:\n\
    \            return 0\n\n        for lv in range(self.bit_size):\n           \
    \ dictionary = self.dictionaries[lv]\n\n            if (value >> (self.bit_size\
    \ - lv - 1)) & 1:\n                l = dictionary.rank(l, 1) + self.zero_count[lv]\n\
    \                r = dictionary.rank(r, 1) + self.zero_count[lv]\n           \
    \ else:\n                l = dictionary.rank(l, 0)\n                r = dictionary.rank(r,\
    \ 0)\n\n        return r-l\n\n    def select(self, v: int, k: int, default: int\
    \ = -1) -> int:\n        \"\"\" k (1-indexed) \u756A\u76EE\u306B\u767B\u5834\u3059\
    \u308B v \u306E\u4F4D\u7F6E\u3092\u6C42\u3081\u308B.\n\n        Args:\n      \
    \      v (int): \u5024\n            k (int): 1-indexed \u3067\u306E\u51FA\u73FE\
    \u56DE\u6570\n            default (int, optional): v \u304C k \u500B\u4EE5\u4E0A\
    \u5B58\u5728\u3057\u306A\u3044\u5834\u5408\u306E\u8FD4\u308A\u5024. Defaults to\
    \ -1.\n\n        Returns:\n            int: k (1-indexed) \u756A\u76EE\u306B\u767B\
    \u5834\u3059\u308B v \u306E\u4F4D\u7F6E\n        \"\"\"\n\n        if (value :=\
    \ self.value_dict.get(v, None)) is None:\n            return default\n\n     \
    \   p = self.begin[value]\n        index = p + k - 1\n\n        for lv in range(self.bit_size):\n\
    \            dictionary = self.dictionaries[~lv]\n            if (value >> lv)\
    \ & 1:\n                index = dictionary.select(index - self.zero_count[~lv]\
    \ + 1, 1, None)\n            else:\n                index = dictionary.select(index+1,\
    \ 0, None)\n\n            if index is None:\n                return default\n\
    \        return index\n\n    def quantile(self, l: int, r: int, k: int) -> int:\n\
    \        \"\"\" [l,r) \u306B\u304A\u3051\u308B k (1-indexed) \u756A\u76EE\u306B\
    \u5C0F\u3055\u3044\u5024\u3092\u6C42\u3081\u308B.\n\n        Args:\n         \
    \   l (int): \u5DE6\u7AEF\n            r (int): \u53F3\u7AEF (\u7B2C r \u9805\u81EA\
    \u8EAB\u306F\u542B\u307E\u306A\u3044)\n            k (int): \u5C0F\u3055\u3044\
    \u65B9\u304B\u3089 k \u756A\u76EE\n\n        Returns:\n            int: [l,r)\
    \ \u306B\u304A\u3051\u308B k (1-indexed) \u756A\u76EE\u306B\u5C0F\u3055\u3044\u5024\
    \n        \"\"\"\n\n        p = 0\n        for lv in range(self.bit_size):\n \
    \           dictionary = self.dictionaries[lv]\n            alpha = dictionary.rank(r,\
    \ 0) - dictionary.rank(l, 0)\n            p <<= 1\n            if alpha < k:\n\
    \                p |= 1\n                k -= alpha\n                l = dictionary.rank(l,\
    \ 1) + self.zero_count[lv]\n                r = dictionary.rank(r, 1) + self.zero_count[lv]\n\
    \            else:\n                l = dictionary.rank(l, 0)\n              \
    \  r = dictionary.rank(r, 0)\n        return self.value_list[p]\n\n    kth_min\
    \ = quantile\n\n    def kth_max(self, l: int, r: int, k: int) -> int:\n      \
    \  \"\"\" [l,r) \u306B\u304A\u3051\u308B k (1-indexed) \u756A\u76EE\u306B\u5927\
    \u304D\u3044\u5024\u3092\u6C42\u3081\u308B.\n\n        Args:\n            l (int):\
    \ \u5DE6\u7AEF\n            r (int): \u53F3\u7AEF (\u7B2C r \u9805\u81EA\u8EAB\
    \u306F\u542B\u307E\u306A\u3044)\n            k (int): \u5927\u304D\u3044\u65B9\
    \u304B\u3089 k \u756A\u76EE\n\n        Returns:\n            int: [l,r) \u306B\
    \u304A\u3051\u308B k (1-indexed) \u756A\u76EE\u306B\u5927\u304D\u3044\u5024\n\
    \        \"\"\"\n        return self.quantile(l, r, r - l - k + 1)\n\n    def\
    \ top(self, l: int, r: int, k: int) -> list[tuple[int, int]]:\n        \"\"\"\
    \ [l,r) \u306B\u3042\u308B\u51FA\u73FE\u56DE\u6570\u304C\u591A\u3044\u9806\u304B\
    \u3089 k \u500B (\u5024, \u500B\u6570) \u306E\u30BF\u30D7\u30EB\u3092\u51FA\u529B\
    \u3059\u308B (\u500B\u6570\u540C\u7387\u306F\u5024\u304C\u5C0F\u3055\u3044\u65B9\
    \u304C\u512A\u5148).\n\n        l: \u5DE6\u7AEF\n        r: \u53F3\u7AEF (\u7B2C\
    \ r \u9805\u3092\u542B\u307E\u306A\u3044)\n        k: \u63A1\u7528\u3059\u308B\
    \u8981\u7D20\u6570\n        \"\"\"\n\n        assert k >= 1\n\n        from heapq\
    \ import heappush, heappop\n        X = []\n        Q = [(-(r - l), 0, 0, l, r)]\n\
    \        while k and Q:\n            _, p, lv, l, r = heappop(Q)\n\n         \
    \   if lv==self.bit_size:\n                X.append((self.value_list[p], r - l))\n\
    \                k -= 1\n                continue\n\n            dictionary =\
    \ self.dictionaries[lv]\n            beta = dictionary.rank(l, 0)\n          \
    \  alpha = dictionary.rank(r, 0) - beta\n\n            # 0\n            if alpha\
    \ > 0:\n                heappush(Q, (-alpha, p << 1, lv + 1, beta, beta + alpha))\n\
    \n            # 1\n            if (r - l) - alpha > 0:\n                x = self.zero_count[lv]\
    \ + (l - beta)\n                y = x + (r - l - alpha)\n                heappush(Q,\
    \ (-((r - l) - alpha), (p << 1) | 1, lv + 1, x, y))\n        return X\n\n    def\
    \ sum(self, l: int, r: int) -> int:\n        \"\"\" [l, r) \u306B\u304A\u3051\u308B\
    \u7DCF\u548C\u3092\u6C42\u3081\u308B.\n\n        Args:\n            l (int): \u5DE6\
    \u7AEF\n            r (int): \u53F3\u7AEF (\u7B2C r \u9805\u81EA\u8EAB\u306F\u542B\
    \u307E\u306A\u3044)\n\n        Returns:\n            int: \u7DCF\u548C\n     \
    \   \"\"\"\n\n        return sum(value * frequency for value, frequency in self.top(l,\
    \ r, r - l))\n\n    def range_all(self, l, r, value):\n        \"\"\" [l,r) \u306B\
    \u3042\u308B (value \u672A\u6E80\u306E\u500B\u6570, value \u3061\u3087\u3046\u3069\
    \u306E\u500B\u6570, value \u3088\u308A\u5927\u304D\u3044\u500B\u6570) \u3092\u6C42\
    \u3081\u308B.\n\n        l: \u5DE6\u7AEF\n        r: \u53F3\u7AEF (\u7B2C r \u9805\
    \u3092\u542B\u307E\u306A\u3044)\n        value: \u5024\n        \"\"\"\n\n   \
    \     pass\n\n    def range_freq(self, l, r, x, y):\n        \"\"\" [l,r) \u306B\
    \u3042\u308B x \u4EE5\u4E0A y \u672A\u6E80\u306E\u500B\u6570\u3092\u6C42\u3081\
    \u308B.\n\n        l: \u5DE6\u7AEF\n        r: \u53F3\u7AEF (\u7B2C r \u9805\u3092\
    \u542B\u307E\u306A\u3044)\n        value: \u5024\n        \"\"\"\n\n        pass\n\
    \n    def range_less(self, l, r, value):\n        \"\"\" [l,r) \u306B\u3042\u308B\
    \ value \u672A\u6E80\u306E\u500B\u6570\u3092\u6C42\u3081\u308B.\n\n        l:\
    \ \u5DE6\u7AEF\n        r: \u53F3\u7AEF (\u7B2C r \u9805\u3092\u542B\u307E\u306A\
    \u3044)\n        value: \u5024\n        \"\"\"\n\n        pass\n\n    def range_more(self,\
    \ l, r, value):\n        \"\"\" [l,r) \u306B\u3042\u308B value \u3088\u308A\u5927\
    \u304D\u3044\u500B\u6570\u3092\u6C42\u3081\u308B.\n\n        l: \u5DE6\u7AEF\n\
    \        r: \u53F3\u7AEF (\u7B2C r \u9805\u3092\u542B\u307E\u306A\u3044)\n   \
    \     value: \u5024\n        \"\"\"\n\n        pass\n\n    def range_list(self,\
    \ l, r, a, b):\n        \"\"\" [l,r) \u306B\u3042\u308B (value \u672A\u6E80\u306E\
    \u500B\u6570, value \u3061\u3087\u3046\u3069\u306E\u500B\u6570, value \u3088\u308A\
    \u5927\u304D\u3044\u500B\u6570) \u3092\u6C42\u3081\u308B.\n\n        l: \u5DE6\
    \u7AEF\n        r: \u53F3\u7AEF (\u7B2C r \u9805\u3092\u542B\u307E\u306A\u3044\
    )\n        value: \u5024\n        \"\"\"\n        pass\n\n    def range_max(self,\
    \ l, r, k):\n        pass\n\n    def range_min(self, l, r, k):\n        pass\n\
    \n    def prev_value(self, l, r, a, b):\n        pass\n\n    def next_value(self,\
    \ l, r, a, b):\n        pass\n\n    def intersect(self, l1: int, r1: int, l2:\
    \ int, r2: int) -> list[tuple[int, int, int]]:\n        \"\"\" [l1, r1), [l2,\
    \ r2) \u306B\u5171\u306B\u5B58\u5728\u3059\u308B\u8981\u7D20 v \u306B\u304A\u3051\
    \u308B (v, 1\u756A\u76EE\u306E\u533A\u9593\u306B\u3042\u308B v \u306E\u500B\u6570\
    , 2\u756A\u76EE\u306E\u533A\u9593\u306B\u3042\u308B v \u306E\u500B\u6570) \u306E\
    \u30EA\u30B9\u30C8\u3092\u51FA\u529B\u3059\u308B.\n\n        Args:\n         \
    \   l1 (int): \u533A\u9593 1 \u306E\u5DE6\u7AEF\n            r1 (int): \u533A\u9593\
    \ 1 \u306E\u53F3\u7AEF (\u7B2C r1 \u9805\u81EA\u8EAB\u306F\u542B\u307E\u306A\u3044\
    )\n            l2 (int): \u533A\u9593 2 \u306E\u5DE6\u7AEF\n            r2 (int):\
    \ \u533A\u9593 2 \u306E\u53F3\u7AEF (\u7B2C r2 \u9805\u81EA\u8EAB\u306F\u542B\u307E\
    \u306A\u3044)\n\n        Returns:\n            list[tuple[int, int, int]]: (v,\
    \ a, b) \u306E\u5F62\u306E\u30EA\u30B9\u30C8. \u5404\u9805\u306F\u4EE5\u4E0B\u3092\
    \u8868\u3059.\n                v: \u5171\u901A\u3057\u3066\u73FE\u308C\u308B\u8981\
    \u7D20\n                a: \u533A\u9593 1 \u306B\u304A\u3051\u308B v \u306E\u500B\
    \u6570\n                b: \u533A\u9593 2 \u306B\u304A\u3051\u308B v \u306E\u500B\
    \u6570\n        \"\"\"\n\n        X = [(l1, r1, l2, r2, 0)]\n        for lv in\
    \ range(self.bit_size):\n            Y = X\n            X = []\n            dictionary\
    \ = self.dictionaries[lv]\n            for l1, r1, l2, r2, p in Y:\n         \
    \       beta1 = dictionary.rank(l1, 0)\n                alpha1 = dictionary.rank(r1,\
    \ 0) - beta1\n                a1 = beta1\n                b1 = beta1 + alpha1\n\
    \                c1 = self.zero_count[lv] + (l1 - beta1)\n                d1 =\
    \ c1 + (r1 - l1- alpha1)\n\n                beta2 = dictionary.rank(l2, 0)\n \
    \               alpha2 = dictionary.rank(r2, 0) - beta2\n                a2 =\
    \ beta2\n                b2 = beta2 + alpha2\n                c2 = self.zero_count[lv]\
    \ + (l2 - beta2)\n                d2 = c2 + (r2 - l2 - alpha2)\n\n           \
    \     if a1 < b1 and a2 < b2:\n                    X.append((a1, b1, a2, b2, p\
    \ << 1))\n\n                if c1<d1 and c2<d2:\n                    X.append((c1,\
    \ d1, c2, d2, (p << 1) | 1))\n\n        return [(self.value_list[p], y1 - x1,\
    \ y2 - x2) for x1, y1, x2, y2, p in X]\n"
  dependsOn: []
  isVerificationFile: false
  path: Wavelet_Matrix.py
  requiredBy: []
  timestamp: '2025-05-24 11:39:51+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test_verify/yosupo_library_checker/Data_Structure/Range_Kth_Smallest.test.py
documentation_of: Wavelet_Matrix.py
layout: document
title: Wavelet Matrix
---

## Outline

静的な数列 $X=(X_0, \dots, X_{N-1})$ に対する様々な検索, 計算を得意とするデータ構造

## Contents

---

### Constructer

```Python
W=Wavelet_Matrix(X)
```

- 整数列 $X$ に対する Wavelet Matrix を生成する.

以降の説明では, $N:=\lvert X \rvert$ とする.

- **計算量** : $O(N \log N)$ Times.

--

### access

```Python
W.access(index)
```

- $X_{{\rm index}}$ を求める.
- **計算量** : $O(N \log N)$ Times.

---

### rank

```Python
W.rank(i, value)
```

- $X_0, X_1, \dots, X_{i-1}$ にある `value` の個数を求める.
- **計算量** : $O(\log N)$ Times.

---

### range_rank

```Python
W.rank(l, r, value)
```

- 部分列 $(X_l, X_{l+1}, \dots, X_{r-1})$ にある `value` の個数を求める.
- `rank` は `range_rank` の特別な場合
- **計算量** : $O(\log N)$ Times.

---

### select

```Python
W.select(value, k ,default=-1)
```

- $X_0, X_1, \dots, X_{N-1}$ において, $k$ 番目 (1-indexed) に `value` が現れる整数列の添字を求める (存在しない場合は `default` が返り値).
- **計算量** : $O(\log N)$ Times.

---

### quantile

```Python
W.quantile(l, r, k)
```

- 部分列 $(X_l, X_{l+1}, \dots, X_{r-1})$ のうち, $k$ (1-indexed) に小さい値を求める.
- **計算量** : $O(\log N)$ Times.

---

### kth_max

```Python
W.kth_max(l, r, k)
```

- 部分列 $(X_l, X_{l+1}, \dots, X_{r-1})$ のうち, $k$ (1-indexed) に大きい値を求める.
- `quantile` の双対に当たる.
- **計算量** : $O(\log N)$ Times.

---

### top

```Python
W.top(l, r, k)
```

- 部分列 $(X_l, X_{l+1}, \dots, X_{r-1})$ のうち, 出現回数が多い順に $k$ 個, (値, 回数) のタプルを生成する.
- 回数が同率の場合は値が小さい方が優先される.
- **計算量** : $O((r-l) \log N)$ Times.

---

### intersect

```Python
W.intersect(l1, r1, l2, r2)
```

- 2つの部分列 $(X_{l_1}, X_{l_1+1}, \dots, X_{r_1-1}), (X_{l_2}, X_{l_2+1}, \dots, X_{r_2-1})$ のうち, に共通して出てくる要素 $v$ を ($m$, 1番目の区間にある $v$ の個数, 2番目の区間にある $v$ の個数) という形式のタプルを生成する.
- **計算量** : $O((r_1-l_1)+(r_2-l_2))$ Times.

---
