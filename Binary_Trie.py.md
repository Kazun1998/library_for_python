---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test_verify/yosupo_library_checker/Data_Structure/Set_Xor_Min.test.py
    title: test_verify/yosupo_library_checker/Data_Structure/Set_Xor_Min.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links:
    - https://judge.yosupo.jp/submission/35057
    - https://judge.yosupo.jp/submission/53782
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.13.3/x64/lib/python3.13/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.13.3/x64/lib/python3.13/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class Binary_Trie:\n    \"\"\" Reference\n    https://judge.yosupo.jp/submission/35057\n\
    \    https://judge.yosupo.jp/submission/53782\n    \"\"\"\n\n    def __init__(self,\
    \ max_value: int, allow_multiple: bool = False, query_number: int = None):\n \
    \       self.bit = max_value.bit_length()\n        self.upper = 1 << self.bit\n\
    \        self.multi = allow_multiple\n\n        if query_number is not None:\n\
    \            self.arc = [-1] * 2 * (self.bit * query_number + 1)\n           \
    \ self.size = [0] * (self.bit*query_number + 1)\n            self.terminal = [0]\
    \ * (self.bit*query_number + 1)\n            self.id=0\n        else:\n      \
    \      self.arc = [-1, -1]\n            self.size = [0]\n            self.terminal\
    \ = [0]\n\n        self.query_number = query_number\n        self.v_list = [0]\
    \ * (self.bit + 1)\n        self._lazy_xor = 0\n\n    @property\n    def lazy_xor(self)\
    \ -> int:\n        return self._lazy_xor\n\n    def xor_all(self, x: int):\n \
    \       assert 0 <= x < self.upper\n        self._lazy_xor ^= x\n\n    def __ixor__(self,\
    \ x: int):\n        self.xor_all(x)\n        return self\n\n    def insert(self,\
    \ x: int) -> bool:\n        \"\"\" x \u3092\u8FFD\u52A0\u3059\u308B\n\n      \
    \  Args:\n            x (int): \u8FFD\u52A0\u3059\u308B\u8981\u7D20\n\n      \
    \  Returns:\n            bool: \u5DEE\u5206\u304C\u767A\u751F\u3057\u305F\u3089\
    \ True\n        \"\"\"\n\n        assert 0 <= x < self.upper\n\n        x ^= self.lazy_xor\n\
    \        v = 0\n        for i in reversed(range(self.bit)):\n            d = (x\
    \ >> i) & 1\n            if self.arc[2 * v + d] == -1:\n                if self.query_number\
    \ is not None:\n                    self.id += 1\n                    self.arc[2\
    \ * v + d] = self.id\n                else:\n                    self.arc[2 *\
    \ v + d] = len(self.size)\n                    self.arc.extend([-1, -1])\n   \
    \                 self.terminal.append(0)\n                    self.size.append(0)\n\
    \n            v = self.arc[2 * v + d]\n            self.v_list[i] = v\n\n    \
    \    if self.terminal[v] > 0 and (not self.multi):\n            return False\n\
    \n        self.terminal[v] += 1\n        for w in self.v_list:\n            self.size[w]\
    \ += 1\n\n        return True\n\n    def discard(self, x: int) -> bool:\n    \
    \    \"\"\" x \u304C\u5B58\u5728\u3059\u308B\u5834\u5408, x \u3092 (1 \u500B)\
    \ \u524A\u9664\u3059\u308B\n\n        Args:\n            x (int): \u524A\u9664\
    \u3059\u308B\u8981\u7D20\n\n        Returns:\n            bool: \u5DEE\u5206\u304C\
    \u767A\u3057\u5F97\u3057\u305F\u3089 True\n        \"\"\"\n        if not (0 <=\
    \ x < self.upper):\n            return\n\n        x ^= self.lazy_xor\n       \
    \ v = 0\n        for i in reversed(range(self.bit)):\n            d = (x >> i)\
    \ & 1\n            if self.arc[2*v+d] == -1:\n                return False\n\n\
    \            v = self.arc[2 * v + d]\n            self.v_list[i] = v\n\n     \
    \   if self.terminal[v] == 0:\n            return False\n\n        self.terminal[v]\
    \ -= 1\n        for w in self.v_list:\n            self.size[w] -= 1\n\n     \
    \   return True\n\n    def erase(self, x: int, k: int) -> int:\n        \"\"\"\
    \ x \u3092\u9AD8\u3005 k \u56DE\u524A\u9664\u3059\u308B (\u305F\u3060\u3057, k=-1\
    \ \u306E\u3068\u304D\u306F\u7121\u9650\u56DE)\n\n        Args:\n            x\
    \ (int): \u524A\u9664\u3059\u308B\u8981\u7D20\n            k (int): \u524A\u9664\
    \u3059\u308B\u56DE\u6570 (k = -1 \u306E\u3068\u304D\u306F\u7121\u9650\u56DE)\n\
    \n        Returns:\n            int: \u5B9F\u969B\u306B\u524A\u9664\u3057\u305F\
    \u56DE\u6570\n        \"\"\"\n\n        assert -1 <= k\n        if not (0 <= x\
    \ < self.upper):\n            return 0\n\n        x ^= self.lazy_xor\n       \
    \ v = 0\n        for i in reversed(range(self.bit)):\n            d = (x>>i) &\
    \ 1\n            if self.arc[2 * v + d] == -1:\n                return 0\n\n \
    \           v = self.arc[2 * v + d]\n            self.v_list[i] = v\n\n      \
    \  if (k == -1) or (self.terminal[v] < k):\n            k = self.terminal[v]\n\
    \n        self.terminal[v] -= k\n        for w in self.v_list:\n            self.size[w]\
    \ -= k\n\n        return k\n\n    def count(self, x: int) -> int:\n        \"\"\
    \" x \u306E\u500B\u6570\u3092\u6C42\u3081\u308B\n\n        Args:\n           \
    \ x (int): \u8981\u7D20\n\n        Returns:\n            int: \u500B\u6570\n \
    \       \"\"\"\n\n        if not (0 <= x < self.upper):\n            return 0\n\
    \n        x ^= self.lazy_xor\n        v = 0\n        for i in reversed(range(self.bit)):\n\
    \            d = (x >> i) & 1\n            if self.arc[2 * v + d] == -1:\n   \
    \             return 0\n\n            v = self.arc[2 * v + d]\n        return\
    \ self.terminal[v]\n\n    def __contains__(self, x: int) -> bool:\n        return\
    \ bool(self.count(x))\n\n    def __len__(self) -> int:\n        return self.size[0]\n\
    \n    def __bool__(self) -> bool:\n        return bool(len(self))\n\n    def less_count(self,\
    \ x: int, equal: bool = False) -> int:\n        \"\"\" x \u672A\u6E80\u306E\u8981\
    \u7D20\u6570\u3092\u6C42\u3081\u308B.\n\n        Args:\n            x (int): \u95BE\
    \u5024\n            equal (bool, optional): True \u306B\u3059\u308B\u3068, \"\u672A\
    \u6E80\" \u304C \"\u4EE5\u4E0B\" \u306B\u306A\u308B. Defaults to False.\n\n  \
    \      Returns:\n            int: x \u3088\u308A\u5927\u304D\u3044\u8981\u7D20\
    \u306E\u6570.\n        \"\"\"\n\n        x ^= self.lazy_xor\n        if equal:\n\
    \            x += 1\n\n        if x < 0:\n            return 0\n\n        if self.upper\
    \ <= x:\n            return len(self)\n\n        v = 0\n        res = 0\n    \
    \    for i in reversed(range(self.bit)):\n            d = (x>>i) & 1\n       \
    \     lc = self.arc[2 * v]\n            rc = self.arc[2 * v + 1]\n\n         \
    \   if (self.lazy_xor >> i) & 1:\n                lc, rc = rc ,lc\n\n        \
    \    if d:\n                if lc != -1:\n                    res += self.size[lc]\n\
    \                if rc == -1:\n                    return res\n              \
    \  v = rc\n            else:\n                if lc == -1:\n                 \
    \   return res\n                v = lc\n        return res\n\n    def more_count(self,\
    \ x: int, equal: bool = False) -> int:\n        \"\"\" x \u3088\u308A\u5927\u304D\
    \u3044\u8981\u7D20\u6570\u3092\u6C42\u3081\u308B.\n\n        Args:\n         \
    \   x (int): \u95BE\u5024\n            equal (bool, optional): True \u306B\u3059\
    \u308B\u3068, \"\u3088\u308A\u5927\u304D\u3044\" \u304C \"\u4EE5\u4E0A\" \u306B\
    \u306A\u308B. Defaults to False.\n\n        Returns:\n            int: x \u3088\
    \u308A\u5927\u304D\u3044\u8981\u7D20\u306E\u6570.\n        \"\"\"\n\n        return\
    \ len(self) - self.less_count(x, not equal)\n\n    def low_value(self, x: int,\
    \ equal = False, default = None):\n        \"\"\" x \u672A\u6E80\u306E\u6574\u6570\
    \u306E\u3046\u3061, \u6700\u5927\u306E\u6574\u6570\u3092\u6C42\u3081\u308B (\u5B58\
    \u5728\u3057\u306A\u3044\u5834\u5408\u306F default).\n\n        equal: True \u306E\
    \u3068\u304D, \"\u672A\u6E80\" \u304C \"\u4EE5\u4E0B\" \u306B\u306A\u308B.\n \
    \       \"\"\"\n\n        x ^= self.lazy_xor\n        if equal:\n            x\
    \ += 1\n\n        alpha = self.less_count(x, False)\n\n        return self.kth_element(alpha\
    \ - 1) if alpha > 0 else default\n\n    def high_value(self, x: int, equal: bool\
    \ = False, default: int = None) -> int:\n        \"\"\" x \u3088\u308A\u5927\u304D\
    \u3044\u6574\u6570\u306E\u3046\u3061, \u6700\u5C0F\u306E\u6574\u6570\u3092\u6C42\
    \u3081\u308B.\n\n        Args:\n            x (int): \u95BE\u5024\n          \
    \  equal (bool, optional): True \u306B\u3059\u308B\u3068, \"\u3088\u308A\u5927\
    \u304D\u3044\" \u304C \"\u4EE5\u4E0A\" \u306B\u306A\u308B. Defaults to False.\n\
    \            default (int, optional): x \u3088\u308A\u5927\u304D\u3044\u6574\u6570\
    \u304C\u5B58\u5728\u3057\u306A\u3044\u5834\u5408\u306E\u8FD4\u308A\u5024. Defaults\
    \ to None.\n\n        Returns:\n            int: _description_\n        \"\"\"\
    \n        x ^= self.lazy_xor\n        if equal:\n            x -= 1\n\n      \
    \  beta = self.more_count(x, False)\n        if beta == 0:\n            return\
    \ default\n        else:\n            return self.kth_element(-beta, 0)\n\n  \
    \  def kth_element(self, k: int, default: int = None) -> int:\n        \"\"\"\
    \ \u6607\u9806 k \u756A\u76EE\u3092\u6C42\u3081\u308B.\n\n        Args:\n    \
    \        k (int): \u756A\u53F7\n            default (int, optional): k \u756A\u76EE\
    \u304C\u5B58\u5728\u3057\u306A\u3044\u5834\u5408\u306E\u8FD4\u308A\u5024. Defaults\
    \ to None.\n\n        Returns:\n            int: \u6607\u9806 k \u756A\u76EE\u306E\
    \u8981\u7D20\n        \"\"\"\n        if k < 0:\n            k += len(self)\n\n\
    \        if not (0 <= k < len(self)):\n            return default\n\n        v\
    \ = 0\n        res = 0\n        for i in reversed(range(self.bit)):\n        \
    \    lc = self.arc[2 * v]\n            rc = self.arc[2 * v + 1]\n\n          \
    \  if (self.lazy_xor >> i) & 1:\n                lc, rc = rc, lc\n\n         \
    \   if lc == -1:\n                v = rc\n                res |= 1 << i\n    \
    \        elif self.size[lc] <= k:\n                k -= self.size[lc]\n      \
    \          v = rc\n                res |= 1 << i\n            else:\n        \
    \        v = lc\n        return res\n\n    @property\n    def min(self) -> int:\n\
    \        return self.kth_element(0)\n\n    @property\n    def max(self) -> int:\n\
    \        return self.kth_element(-1)\n\n    def __getitem__(self, index: int)\
    \ -> int:\n        return self.kth_element(index)\n"
  dependsOn: []
  isVerificationFile: false
  path: Binary_Trie.py
  requiredBy: []
  timestamp: '2025-05-18 20:41:24+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test_verify/yosupo_library_checker/Data_Structure/Set_Xor_Min.test.py
documentation_of: Binary_Trie.py
layout: document
redirect_from:
- /library/Binary_Trie.py
- /library/Binary_Trie.py.html
title: Binary_Trie.py
---
