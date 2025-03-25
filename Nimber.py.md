---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test_verify/yosupo_library_checker/Math/Nimber.test.py
    title: test_verify/yosupo_library_checker/Math/Nimber.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.13.2/x64/lib/python3.13/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.13.2/x64/lib/python3.13/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class Nimber:\n    def __init__(self, x: int = 0):\n        if type(x) is\
    \ str:\n            x = int(x)\n\n        self.__x = x\n\n    def __eq__(self,\
    \ other: \"Nimber\") -> bool:\n        return self.__x == other.__x\n\n    def\
    \ __str__(self) -> str:\n        return str(self.__x)\n\n    def __repr__(self)\
    \ -> str:\n        return f\"{self.__class__.__name__}({self.__x})\"\n\n    def\
    \ __pos__(self) -> \"Nimber\":\n        return Nimber(self.__x)\n\n    def __neg__(self)\
    \ -> \"Nimber\":\n        return Nimber(self.__x)\n\n    def __add__(self, other:\
    \ \"Nimber\") -> \"Nimber\":\n        return Nimber(self.__x ^ other.__x)\n\n\
    \    def __sub__(self, other: \"Nimber\") -> \"Nimber\":\n        return Nimber(self.__x\
    \ ^ other.__x)\n\n    def __mul__(self, other: \"Nimber\") -> \"Nimber\":\n  \
    \      lv = max(self.level(self.__x), self.level(other.__x))\n        return Nimber(self.__mul_calc(self.__x,\
    \ other.__x, lv))\n\n    __SMALL_NIM_PRODUCT_MEMO = [[-1] * 256 for _ in range(256)]\n\
    \    __SMALL_NIM_PRODUCT_MEMO[0][0] = __SMALL_NIM_PRODUCT_MEMO[0][1] = __SMALL_NIM_PRODUCT_MEMO[1][0]\
    \ = 0\n    __SMALL_NIM_PRODUCT_MEMO[1][1] = 1\n\n    @classmethod\n    def __mul_calc(cls,\
    \ x: int, y: int, lv: int) -> int:\n        if lv <= 3 and cls.__SMALL_NIM_PRODUCT_MEMO[x][y]\
    \ != -1:\n            return cls.__SMALL_NIM_PRODUCT_MEMO[x][y]\n\n        x1,\
    \ x0 = cls.separate(x, lv)\n        y1, y0 = cls.separate(y, lv)\n\n        p\
    \ = cls.__mul_calc(x0, y0, lv - 1)\n        e = 1 << (1 << (lv - 1))\n\n     \
    \   a = p ^ cls.__mul_calc(x0 ^ x1, y0 ^ y1, lv - 1) * e\n        b = cls.__mul_calc(cls.__mul_calc(x1,\
    \ y1, lv - 1), e >> 1, lv - 1)\n\n        res = (p * e) ^ a ^ b\n        if lv\
    \ <= 3:\n            cls.__SMALL_NIM_PRODUCT_MEMO[x][y] = res\n\n        return\
    \ res\n\n    def __truediv__(self, other: \"Nimber\") -> \"Nimber\":\n       \
    \ return self * other.inverse()\n\n    @staticmethod\n    def __floor_log(x: int)\
    \ -> int:\n        return x.bit_length() - 1\n\n    @staticmethod\n    def separate(x:\
    \ int, lv: int):\n        if lv == 0:\n            raise ValueError\n\n      \
    \  upper = x >> (1 << (lv - 1))\n        lower = x ^ (upper << (1 << (lv - 1)))\n\
    \        return upper, lower\n\n    @classmethod\n    def level(cls, x: int) ->\
    \ int:\n        if x == 0:\n            return 0\n        else:\n            return\
    \ cls.__floor_log(cls.__floor_log(x)) + 1\n\n    def __hash__(self) -> int:\n\
    \        return hash(self.__x)\n\n    @classmethod\n    def __square_calc(cls,\
    \ x: int, lv: int) -> int:\n        if lv <= 3 and cls.__SMALL_NIM_PRODUCT_MEMO[x][x]\
    \ != -1:\n            return cls.__SMALL_NIM_PRODUCT_MEMO[x][x]\n\n        x1,\
    \ x0 = cls.separate(x, lv)\n\n        x1_square = cls.__square_calc(x1, lv - 1)\n\
    \        x0_square = cls.__square_calc(x0, lv - 1)\n        e = 1 << (1 << (lv\
    \ - 1))\n\n        res = (x1_square * e) ^ cls.__mul_calc(cls.__mul_calc(x1, x1,\
    \ lv - 1), e >> 1, lv - 1) ^ x0_square\n        if lv <= 3:\n            cls.__SMALL_NIM_PRODUCT_MEMO[x][x]\
    \ = res\n\n        return res\n\n    def square(self) -> \"Nimber\":\n       \
    \ \"\"\" \u81EA\u5206\u81EA\u8EAB\u306E\u81EA\u4E57\u3092\u6C42\u3081\u308B.\n\
    \n        Returns:\n            Nimber: self * self\n        \"\"\"\n        return\
    \ Nimber(self.__square_calc(self.__x, self.level(self.__x)))\n\n    def __pow__(self,\
    \ n: int) -> \"Nimber\":\n        x = self\n        y = Nimber(1)\n        while\
    \ n:\n            if n & 1:\n                y *= x\n            x = x.square()\n\
    \            n >>= 1\n\n        return y\n\n    def inverse(self):\n        return\
    \ pow(self, (1 << (1 << self.level(self.__x))) - 2)\n"
  dependsOn: []
  isVerificationFile: false
  path: Nimber.py
  requiredBy: []
  timestamp: '2025-03-22 22:31:05+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test_verify/yosupo_library_checker/Math/Nimber.test.py
documentation_of: Nimber.py
layout: document
title: Nimber
---

## Outline

組み合わせゲーム理論において用いられる Nim から導入された Nimber の計算を行う.

## Theory

非負整数 $n$ に対して,
    $$ F_n := \{0, 1, \dots, 2^n - 1 \} $$
とする.

### 加法

$F_n$ 上の演算 $\oplus: F_n \times F_n \to F_n$ を
    $$ x \oplus y := \mathrm{mex} \left(\{ a \oplus y \mid 0 \leq a < x \} \cup \{ x \oplus b \mid 0 \leq b < y \} \right)$$
によって帰納的に定める. ただし, $S \subsetneq \mathbb{N}$ に対して, $S$ の最小除外数 $\mathrm{mex}~S$ を
    $$ \mathrm{mex}~S := \min (\mathbb{N} \setminus S) $$
で定義する.

すると, $\oplus$ は Bitwise-XOR と一致する.

このことから, 以下が従う.

* $\oplus$ は $F_n$ において可換群になる. 特に, 以下が成り立つ.
  * $x < 2^m < 2^n$ に対して, $x \oplus 2^m = x + 2^m$.
  * 単位元は $0$ である.
  * $x \in F_n$ の逆元は $x$ 自身である.

### 乗法

$F_{2^n}$ 上の演算 $\otimes: F_{2^n} \times F_{2^n} \to F_{2^n}$ を
    $$ x \otimes y := \mathrm{mex} \left(\{(a \otimes y) \oplus (x \otimes b) \oplus (a \otimes b) \mid 0 \leq a < x, 0 \leq b < y\} \right)$$
によって帰納的に定める.

このとき, $(F_{2^n}, \oplus, \otimes)$ は $1$ を乗法単位元とする可換体になる.

### 計算

可換体 $(F_{2^n}, \oplus, \otimes)$ に対して, 以下が成り立つ. ただし, 非負整数 $k~(< n) $ に対して,
    $$e_k := 2^{2^k}, \quad e'_k := 2^{2^k - 1} \left(= e_k / 2 \right)$$
とする.

* $x \in F$ に対して, $x < e_k$ ならば, $x \otimes e_k = x \times e_k$ である.
* $e_k \otimes e_k = \frac{3}{2} e_k = e_k + e'_k = e_k \oplus e'_k $.

これらの性質により, $x, y \in F_{2^n}$ に対して, $x \oplus y$ の計算を次のようにして, $F_{2^{n-1}}$ 上の計算に帰着させることができる.

まず, $x,y \in F_{2^n}$ より, $x, y$ はそれぞれ $x_0, x_1, y_0, y_1 \in F_{2^{n-1}}$ を用いて,
    $$ x = x_1 e_{k-1} + x_0, \quad y = y_1 e_{k-1} + y_0 $$
と表せる.

すると,
$$
\begin{align*}
    x \otimes y
    &= (x_1 e_{k-1} + x_0) \otimes (y_1 e_{k-1} + y_0) \\
    &= (x_1 e_{k-1} \oplus x_0) \otimes (y_1 e_{k-1} \oplus y_0) \\
    &= (x_1 \otimes e_{k-1} \oplus x_0) \otimes (y_1 \otimes e_{k-1} \oplus y_0) \\
    &= \left((x_1 \otimes y_1) \otimes (e_{k-1} \otimes e_{k-1}) \right) \oplus \left((x_0 \otimes y_1 \oplus x_1 \otimes y_0) \otimes e_{k-1} \right) \oplus (x_0 \otimes y_0) \\
    &= \left((x_1 \otimes y_1) \otimes (e_{k-1} \otimes e'_{k-1}) \right) \oplus \left((x_0 \otimes y_1 \oplus x_1 \otimes y_0) \otimes e_{k-1} \right) \oplus (x_0 \otimes y_0) \\
    &= \left((x_1 \otimes y_1 \oplus x_0 \otimes y_1 \oplus x_1 \otimes y_0) \otimes e_{k-1} \right) \oplus (x_1 \otimes y_1 \otimes e'_{k-1}) \oplus (x_0 \otimes y_0) \\
    &= \left(((x_1 \otimes y_1 \oplus x_0 \otimes y_1 \oplus x_1 \otimes y_0 \oplus x_0 \otimes y_0) \oplus x_0 \otimes y_0) \otimes e_{k-1} \right) \oplus (x_1 \otimes y_1 \otimes e'_{k-1}) \oplus (x_0 \otimes y_0) \\
    &= \left(((x_1 \oplus x_0) \otimes (y_1 \oplus y_0) \oplus (x_0 \otimes y_0)) \otimes e_{k-1} \right) \oplus (x_1 \otimes y_1 \otimes e'_{k-1}) \oplus (x_0 \otimes y_0)\\
    &= \left(((x_1 \oplus x_0) \otimes (y_1 \oplus y_0) \oplus (x_0 \otimes y_0)) \times e_{k-1} \right) \oplus (x_1 \otimes y_1 \otimes e'_{k-1}) \oplus (x_0 \otimes y_0) \\
\end{align*}
$$

となり,
    $$(x_1 \oplus x_0) \otimes (y_1 \oplus y_0), \quad x_0 \otimes y_0, \quad x_1 \otimes y_1 \otimes e'_{k-1}$$
の $4$ つの "1 レベル下" の積に帰着される.

## Reference

* https://drive.google.com/file/d/16g1tfSHUU4NXNTDgaD8FSA1WB4FtJCyV/edit
* https://natsugiri.hatenablog.com/entry/2020/03/29/073605
