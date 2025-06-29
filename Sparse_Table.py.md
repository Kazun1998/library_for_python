---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test_verify/yosupo_library_checker/Data_Structure/Sparse_Table.test.py
    title: test_verify/yosupo_library_checker/Data_Structure/Sparse_Table.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links:
    - https://qiita.com/recuraki/items/0fcbc9e2abbc4fae5f62"""
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.13.5/x64/lib/python3.13/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.13.5/x64/lib/python3.13/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from typing import TypeVar, Generic, Callable\n\nSemiGroup = TypeVar('SemiGroup')\n\
    class Sparse_Table(Generic[SemiGroup]):\n    \"\"\" \u53C2\u8003: https://qiita.com/recuraki/items/0fcbc9e2abbc4fae5f62\"\
    \"\"\n\n    def __init__(self, A: list[SemiGroup], op: Callable[[SemiGroup, SemiGroup],\
    \ SemiGroup]):\n        \"\"\" \u534A\u7FA4 (SemiGroup, op) \u4E0A\u306E\u5217\
    \ A \u306B\u95A2\u3059\u308B Sparse Table \u3092\u69CB\u7BC9\u3059\u308B.\n\n\
    \        Args:\n            A (list[SemiGroup]): \u534A\u7FA4 (SemiGroup, op)\
    \ \u4E0A\u306E\u5217\n            op (Callable[[SemiGroup, SemiGroup], SemiGroup]):\
    \ \u534A\u7FA4\u4E0A\u306E\u6F14\u7B97 (x, y) -> xy\n\n        Remark:\n     \
    \       \u534A\u7FA4 (SemiGroup, op) \u306F\u7D50\u5408\u5247, \u53EF\u63DB\u5247\
    , \u51AA\u7B49\u5247\u3092\u6E80\u305F\u3057\u3066\u3044\u308B\u3053\u3068\u3092\
    \u8981\u6C42\u3059\u308B.\n        \"\"\"\n        self.op = op\n        n = len(A)\n\
    \        depth = max(1, (n - 1).bit_length())\n\n        self.table = [[a for\
    \ a in A]]\n        for k in range(1, depth):\n            prev_row = self.table[-1]\n\
    \            m = 1 << (k - 1)\n            row = [op(prev_row[i], prev_row[i +\
    \ m]) for i in range(n - 2 * m + 1)]\n            self.table.append(row)\n\n \
    \   def __len__(self) -> int:\n        return len(self.table[0])\n\n    def product(self,\
    \ l: int, r: int, default: SemiGroup = None, left_close: bool = True, right_close:\
    \ bool = True) -> SemiGroup:\n        \"\"\" \u7DCF\u7A4D A_l A_{l+1} ... A_r\
    \ \u3092\u6C42\u3081\u308B. \u305F\u3060\u3057, \u7A7A\u7A4D\u306F default \u3068\
    \u3059\u308B.\n\n        Args:\n            l (int): \u5DE6\u7AEF\n          \
    \  r (int): \u53F3\u7AEF\n            default (SemiGroup, optional): \u7A7A\u7A4D\
    \u306E\u3068\u304D\u306E\u8FD4\u308A\u5024. Defaults to None.\n            left_close\
    \ (bool, optional): False \u306B\u3059\u308B\u3068, \u5DE6\u7AEF\u304C\u958B\u306B\
    \u306A\u308B. Defaults to True.\n            right_close (bool, optional): False\
    \ \u306B\u3059\u308B\u3068, \u53F3\u7AEF\u304C\u958B\u306B\u306A\u308B. Defaults\
    \ to True.\n\n        Returns:\n            SemiGroup: \u7DCF\u7A4D\n        \"\
    \"\"\n\n        # \u533A\u9593\u3092\u5DE6\u534A\u958B\u533A\u9593\u306B\u5909\
    \u63DB\u3059\u308B.\n        if not left_close:\n            l += 1\n\n      \
    \  if right_close:\n            r += 1\n\n        length = r - l\n        if length\
    \ == 1:\n            # \u5358\u9805\n            return self.table[0][l]\n   \
    \     elif length <= 0:\n            # \u7A7A\u7A4D\n            return default\n\
    \n        lv = (length - 1).bit_length() - 1\n        row = self.table[lv]\n \
    \       return self.op(row[l], row[r - pow(2, lv)])\n"
  dependsOn: []
  isVerificationFile: false
  path: Sparse_Table.py
  requiredBy: []
  timestamp: '2025-06-22 19:54:08+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test_verify/yosupo_library_checker/Data_Structure/Sparse_Table.test.py
documentation_of: Sparse_Table.py
layout: document
title: Sparse Table
---

## Outline

可換で冪等律を満たす半群 $S=(S, \*)$ の列 $A=(A_0, A_1, \dots, A_{\lvert A \rvert-1})$ に対して, 区間積 $A_L \* \dots \* A_R$ の計算を $O(1)$ Time で行うことができるデータ構造.

ただし, 区間積を $O(1)$ Time で計算できる代償として, 更新ができない.

### Constructer

```Python
T=Sparse_Table(A, calc)
```

- $A$ : $S$ の列

以下, $N:=\lvert A \rvert$ とする.

- $\operatorname{calc} : S \times S \to S; (x,y) \mapsto x \* y$ : 二項演算
- **計算量** : $O(N \log N)$ Time.

---

### product

```Python
T.product(l, r, default=None, left_close=True, right_close=True)
```

- 区間積 $A_L \* A_{L+1} \* \dots \* A_R$  を求める. なお, $L>R$ の場合は `default` を返す.
- なお, `left_close` , `right_close` を `False` とすると, それぞれに対応する方が開区間 (端点が含まれない) になる.
- **制約**
  - $0 \leq L \lt N$
  - $0 \leq R \lt N$
- **計算量** : $O(1)$ Time.
