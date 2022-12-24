---
title: Sparse Table
documentation_of: //Sparse_Table.py
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
