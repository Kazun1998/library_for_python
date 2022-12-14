---
title: Wavelet Matrix
documentation_of: //Wavelet_Matrix.py
---

## Outline

静的な数列 $A=(A\_0, \dots, A\_{N-1})$ に対する様々な検索, 計算を得意とするデータ構造

## Contents

---

### Constructer

```Python
W=Wavelet_Matrix(X)
```

- 整数列 $X$ に対する Wavelet Matrix を生成する.

以降の説明では, $N:=\lvert X \rvert$ とする.

- **計算量** : $O(N \log N)$ Times.

---

### rank

```Python
W.rank(i,value)
```

- $X_0, X_1, \dots, X_{i-1}$ にある `value` の個数を求める.
- **計算量** : $O(\log N)$ Times.

---
