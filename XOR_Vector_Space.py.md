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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "\"\"\"\n[Tips]\n\u81EA\u7136\u6570\u5168\u4F53\u306E\u96C6\u5408 N \u306B\
    \u304A\u3044\u3066, \u52A0\u6CD5\u3068 F_2 \u3068\u306E\u30B9\u30AB\u30E9\u30FC\
    \u500D\u3092\n    x+y:=x xor y, [0] x:=0, [1] x:=x\n\u3068\u5B9A\u3081\u308B\u3068\
    , N \u306F F_2 \u4E0A\u306E\u30D9\u30AF\u30C8\u30EB\u7A7A\u9593\u306B\u306A\u308B\
    .\n\"\"\"\n\nclass XOR_Vector_Space:\n    def __init__(self):\n        self.basis=[]\n\
    \n    def __contains__(self, x):\n        for v in self.basis:\n            x=min(x,\
    \ x^v)\n        return x==0\n\n    def __add__(self, other):\n        W=XOR_Vector_Space()\n\
    \n        W.basis=self.basis[:]\n        W.add_vector(*other.bais)\n        return\
    \ W\n\n    def add_vector(self, *T):\n        for x in T:\n            for v in\
    \ self.basis:\n                x=min(x, x^v)\n\n            if x:\n          \
    \      self.basis.append(x)\n\n    def dimension(self):\n        return len(self.basis)\n\
    \n    def reduction(self):\n        S=self.basis\n        for i in range(len(S)):\n\
    \            vb=S[i]&(-S[i])\n            for j in  range(len(S)):\n         \
    \       if i==j:\n                    continue\n\n                if S[j]&vb:\n\
    \                    S[j]^=S[i]\n        self.basis=[s for s in S if s]\n\n  \
    \  def projection(self, x):\n        for v in self.basis:\n            x=min(x,\
    \ x^v)\n        return x\n\n    def __repr__(self):\n        return \"[XOR Vector\
    \ Space]: dim: {}, basis: {}\".format(self.dimension(), self.basis)\n\n    def\
    \ __le__(self,other):\n        for u in self.basis:\n            if not u in other:\n\
    \                return False\n        return True\n\n    def __ge__(self,other):\n\
    \        return other<=self\n\n    def __eq__(self,other):\n        return (self<=other)\
    \ and (other<=self)\n\ndef Generate_Space(*S):\n    \"\"\" S \u306B\u3088\u3063\
    \u3066\u751F\u6210\u3055\u308C\u308B XOR \u30D9\u30AF\u30C8\u30EB\u7A7A\u9593\u3092\
    \u6C42\u3081\u308B.\n\n    \"\"\"\n\n    V=XOR_Vector_Space()\n    V.add_vector(*S)\n\
    \    V.reduction()\n    return V\n\ndef Get_Basis(*S):\n    \"\"\" S \u306B\u3088\
    \u3063\u3066\u751F\u6210\u3055\u308C\u308B XOR \u30D9\u30AF\u30C8\u30EB\u7A7A\u9593\
    \ V \u306B\u304A\u3044\u3066, S \u306E\u90E8\u5206\u96C6\u5408\u3067\u3082\u3042\
    \u308BV \u306E\u57FA\u5E95\u3092\u6C42\u3081\u308B\n\n    \"\"\"\n\n    B=[]\n\
    \    V=XOR_Vector_Space()\n    for v in S:\n        w=V.projection(v)\n      \
    \  if w:\n            B.append(v)\n            V.basis.append(w)\n    return B\n"
  dependsOn: []
  isVerificationFile: false
  path: XOR_Vector_Space.py
  requiredBy: []
  timestamp: '2022-12-25 03:43:05+09:00'
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
