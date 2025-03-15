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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.13.2/x64/lib/python3.13/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.13.2/x64/lib/python3.13/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# [Note]\n# \u81EA\u7136\u6570\u5168\u4F53\u306E\u96C6\u5408 N \u306B\u304A\
    \u3044\u3066, \u52A0\u6CD5\u3068 F_2 \u3068\u306E\u30B9\u30AB\u30E9\u30FC\u500D\
    \u3092\n#   (\u548C) x + y := x xor y\n#   (\u30B9\u30AB\u30E9\u30FC\u500D) [0]\
    \ x:=0, [1] x:=x\n# \u3068\u5B9A\u3081\u308B\u3068, N \u306F F_2 \u4E0A\u306E\u30D9\
    \u30AF\u30C8\u30EB\u7A7A\u9593\u306B\u306A\u308B.\n#\n# \u305F\u3060\u3057, \u5B9F\
    \u7528\u4E0A\u306F, \u3042\u308B\u975E\u8CA0\u6574\u6570 k \u3092\u7528\u3044\u3066\
    \ 2^k \u672A\u6E80\u306E\u81EA\u7136\u6570\u5168\u4F53\u306E\u96C6\u5408\u3092\
    \ V_k \u3068\u3057\u3066\u7A7A\u9593\u3092\u6271\u3046.\n# \u3053\u306E V_k \u306F\
    \ N \u306E\u90E8\u5206\u7A7A\u9593\u3067\u3042\u308B.\n\nclass XOR_Vector_Space:\n\
    \    def __init__(self, *vectors: int):\n        \"\"\" vectors \u304B\u3089\u306A\
    \u308B XOR \u30D9\u30AF\u30C8\u30EB\u7A7A\u9593\u3092\u751F\u6210\u3059\u308B\
    .\n        \"\"\"\n\n        self.basis: list[int] = []\n        self.add_vector(*vectors)\n\
    \        self.reduction()\n\n    def __contains__(self, x: int) -> bool:\n   \
    \     for v in self.basis:\n            x = min(x, x ^ v)\n        return x ==\
    \ 0\n\n    def __add__(self, other: \"XOR_Vector_Space\") -> \"XOR_Vector_Space\"\
    :\n        \"\"\" \u30D9\u30AF\u30C8\u30EB\u7A7A\u9593\u306E\u548C\u3092\u6C42\
    \u3081\u308B.\n\n        Args:\n            other (XOR_Vector_Space): \u30D9\u30AF\
    \u30C8\u30EB\u7A7A\u9593\n\n        Returns:\n            XOR_Vector_Space: \u548C\
    \u7A7A\u9593\n        \"\"\"\n\n        return XOR_Vector_Space(*(self.basis +\
    \ other.basis))\n\n    def add_vector(self, *T: int):\n        for x in T:\n \
    \           if (y := self.projection(x)):\n                self.basis.append(y)\n\
    \n    def dimension(self) -> int:\n        \"\"\" \u6B21\u5143\u3092\u6C42\u3081\
    \u308B.\n\n        Returns:\n            int: \u6B21\u5143\n        \"\"\"\n\n\
    \        return len(self.basis)\n\n    def reduction(self):\n        S = self.basis\n\
    \        for i in range(len(S)):\n            vb = S[i] & (-S[i])\n          \
    \  for j in  range(len(S)):\n                if (j != i) and (S[j] & vb):\n  \
    \                  S[j] ^= S[i]\n        self.basis = [s for s in S if s]\n\n\
    \    def projection(self, x: int) -> int:\n        \"\"\" \u30D9\u30AF\u30C8\u30EB\
    \u7A7A\u9593\u3078\u306E x \u306E\u5C04\u5F71\u3092\u6C42\u3081\u308B.\n\n   \
    \     Args:\n            x (int):\n\n        Returns:\n            int: \u5C04\
    \u5F71\u306E\u7D50\u679C\n        \"\"\"\n        for v in self.basis:\n     \
    \       x = min(x, x ^ v)\n        return x\n\n    def __repr__(self):\n     \
    \   return f\"{self.__class__.__name__}({', '.join(map(str, self.basis))})\"\n\
    \n    def is_subspace(self, V: \"XOR_Vector_Space\") -> bool:\n        \"\"\"\
    \ V \u306E\u90E8\u5206\u7A7A\u9593\u304B?\n\n        Args:\n            V (XOR_Vector_Space):\
    \ XOR \u30D9\u30AF\u30C8\u30EB\u7A7A\u9593\n\n        Returns:\n            bool:\
    \ \u90E8\u5206\u7A7A\u9593 ?\n        \"\"\"\n\n        return all(u in V for\
    \ u in self.basis)\n\n    def __le__(self, other: \"XOR_Vector_Space\") -> bool:\n\
    \        return self.is_subspace(other)\n\n    def __ge__(self,other):\n     \
    \   return other<=self\n\n    def __eq__(self,other):\n        return (self <=\
    \ other) and self.dimension() == other.dimension()\n"
  dependsOn: []
  isVerificationFile: false
  path: XOR_Vector_Space.py
  requiredBy: []
  timestamp: '2025-03-15 12:12:18+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: XOR_Vector_Space.py
layout: document
title: XOR Vector Space
---

## Outline

演算 XOR によって作られるベクトル空間に関する計算を行う.

## Theory

非負整数全体の集合を $\mathbb{N}$ とする. このとき, $\mathbb{N}$ は次のようにして体 $\mathbb{F}_2:=\mathbb{Z}/2\mathbb{Z}$ 上のベクトル空間とみなすことができる.

* $x,y \in \mathbb{N}$ に対して, 和 $x \oplus y$ を $x,y$ の XOR とする.
* $x \in \mathbb{N}$ に対して, スカラー倍をそれぞれ $[0]_2 x:=0, [1]_2x:=x$ と定義する.

なお, 実用的には整数 $K$ に対して, $V_K$ を $0$ 以上 $2^K$ 未満の非負整数全体の集合とすると, $V_K$ は $\mathbb{N}$ の部分空間になり, $V_K$ を全体として扱うことになる.

ここで, 体が $\mathbb{F}_2$ という位数 $2$ の体であることから, $\\# V_K=2^{\dim V_K}$ が成り立つ.

## Contents

### Constructer

```Python
V=XOR_Vector_Space()
```

* XOR ベクトル空間を生成する.

---
