---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test_verify/yosupo_library_checker/Data_Structure/Disjoint_Sparse_Table.test.py
    title: test_verify/yosupo_library_checker/Data_Structure/Disjoint_Sparse_Table.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links:
    - https://ei1333.github.io/library/structure/others/disjoint-sparse-table.cpp.html
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.1/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.1/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class Disjoint_Sparse_Table:\n    \"\"\" \u53C2\u8003: https://ei1333.github.io/library/structure/others/disjoint-sparse-table.cpp.html\
    \ \"\"\"\n\n    def __init__(self, L, calc):\n        \"\"\" L \u306E\u6F14\u7B97\
    \ calc \u306B\u5BFE\u3059\u308B Disjoint Sparse Table \u3092\u751F\u6210\u3059\
    \u308B.\n\n        L: list\n        calc: \u4E8C\u9805\u6F14\u7B97\n        \"\
    \"\"\n\n        self.calc=calc\n        self.size=N=len(L)\n        self.b=max(1,(N-1).bit_length())\n\
    \n        self.table=[[0]*self.size for _ in range(self.b)]\n\n        tab=self.table[0]\n\
    \        for i in range(self.size):\n            tab[i]=L[i]\n\n        shift=1\n\
    \        for i in range(1,self.b):\n            shift<<=1\n            tab=self.table[i]\n\
    \n            for j in range(0,N,2*shift):\n                t=min(j+shift,N)\n\
    \                tab[t-1]=L[t-1]\n\n                for k in range(t-2,j-1,-1):\n\
    \                    tab[k]=calc(L[k],tab[k+1])\n\n                if N<=t:\n\
    \                    break\n\n                tab[t]=L[t]\n                r=min(t+shift,N)\n\
    \n                for k in range(t+1,r):\n                    tab[k]=calc(tab[k-1],L[k])\n\
    \n    def product(self, l, r, default=None, left_close=True, right_close=True):\n\
    \        \"\"\" l<=i<=r \u306B\u5BFE\u3059\u308B\u7A4D\u3092\u751F\u6210\u3059\
    \u308B.\n\n        \"\"\"\n\n        if not left_close:\n            l+=1\n\n\
    \        if not right_close:\n            r-=1\n\n        if l==r:\n         \
    \   return self.table[0][l]\n        elif l>r:\n            return default\n\n\
    \        p=(l^r).bit_length()-1\n        tab=self.table[p]\n        return self.calc(tab[l],\
    \ tab[r])\n"
  dependsOn: []
  isVerificationFile: false
  path: Disjoint_Sparse_Table.py
  requiredBy: []
  timestamp: '2022-11-22 04:38:45+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test_verify/yosupo_library_checker/Data_Structure/Disjoint_Sparse_Table.test.py
documentation_of: Disjoint_Sparse_Table.py
layout: document
title: Disjoint Sparse Table
---

## Outline

半群 $S=(S, \*)$ の列 $A=(A_0, A_1, \dots, A_{\lvert A \rvert-1})$ に対して, 区間積 $A_L \* \dots \* A_R$ の計算を $O(1)$ Time で行うことができるデータ構造.

ただし, 区間積を $O(1)$ Time で計算できる代償として, 更新ができない.

### Constructer

```Python
T=Disjoint_Sparse_Table(A, calc)
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
