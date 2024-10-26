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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.7/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.7/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class Sparse_Table:\n    \"\"\" \u53C2\u8003: https://qiita.com/recuraki/items/0fcbc9e2abbc4fae5f62\"\
    \"\"\n\n    def __init__(self, A, op):\n        \"\"\" A \u306E\u6F14\u7B97 op\
    \ \u306B\u5BFE\u3059\u308B Sparse Table \u3092\u751F\u6210\u3059\u308B.\n\n  \
    \      A: list\n        op: \u4E8C\u9805\u6F14\u7B97\n        (op \u306F\u7D50\
    \u5408\u5247, \u53EF\u63DB\u5247, \u51AA\u7B49\u901F\u3092\u6E80\u305F\u3057\u3066\
    \u3044\u308B\u3053\u3068\u3092\u8981\u6C42\u3059\u308B)\n        \"\"\"\n\n  \
    \      self.op=op\n        self.N=N=len(A)\n        self.depth=max(1,(N-1).bit_length())\n\
    \n        self.table=[[a for a in A]]\n        for k in range(1, self.depth):\n\
    \            tab=self.table[-1]\n            m=1<<(k-1)\n            B=[op(tab[i],\
    \ tab[i+m]) for i in range(N-2*m+1)]\n            self.table.append(B)\n\n   \
    \ def product(self, l, r, default=None, left_close=True, right_close=True):\n\
    \        \"\"\" l<=i<=r \u306B\u5BFE\u3059\u308B\u7A4D\u3092\u751F\u6210\u3059\
    \u308B.\n\n        \"\"\"\n\n        if not left_close:\n            l+=1\n\n\
    \        if right_close:\n            r+=1\n\n        length=r-l\n        if length==1:\n\
    \            return self.table[0][l]\n        elif length<=0:\n            return\
    \ default\n\n        lv=(length-1).bit_length()-1\n        tab=self.table[lv]\n\
    \        return self.op(tab[l], tab[r-(2**lv)])\n"
  dependsOn: []
  isVerificationFile: false
  path: Sparse_Table.py
  requiredBy: []
  timestamp: '2022-12-18 03:53:02+09:00'
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
