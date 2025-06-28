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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.13.5/x64/lib/python3.13/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.13.5/x64/lib/python3.13/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def General_Binary_Increase_Search_Integer(L: int, R: int, cond, default\
    \ = None) -> int:\n    \"\"\" \u6761\u4EF6\u5F0F\u304C\u5358\u8ABF\u5897\u52A0\
    \u3067\u3042\u308B\u3068\u304D, \u6574\u6570\u4E0A\u3067\u4E8C\u90E8\u63A2\u7D22\
    \u3092\u884C\u3044, cond(x) \u304C\u771F\u306B\u306A\u308B\u6700\u5C0F\u306E\u6574\
    \u6570 x \u3092\u6C42\u3081\u308B.\n\n    Args:\n        L (int): \u89E3\u306E\
    \u4E0B\u9650\n        R (int): \u89E3\u306E\u4E0A\u9650\n        cond (Callable[[int],\
    \ bool]): \u6761\u4EF6(1\u5909\u6570\u95A2\u6570, \u5E83\u7FA9\u5358\u8ABF\u5897\
    \u52A0\u3092\u6E80\u305F\u3059)\n        default (Any, optional): R \u3067\u6761\
    \u4EF6\u3092\u6E80\u305F\u3055\u306A\u3044 (\u3064\u307E\u308A, [L, R] \u4E0A\u3067\
    \u306F\u5E38\u306B\u507D) \u3068\u304D\u306E\u8FD4\u308A\u5024. Defaults to None.\n\
    \n    Returns:\n        int: cond(x) \u304C\u771F\u306B\u306A\u308B\u6700\u5C0F\
    \u306E\u6574\u6570 x\n    \"\"\"\n    if not cond(R):\n        return default\n\
    \n    if cond(L):\n        return L\n\n    R += 1\n    while R - L>1:\n      \
    \  C = L + (R - L) // 2\n        if cond(C):\n            R = C\n        else:\n\
    \            L = C\n    return R\n\ndef General_Binary_Decrease_Search_Integer(L:\
    \ int, R: int, cond, default = None) -> int:\n    \"\"\" \u6761\u4EF6\u5F0F\u304C\
    \u5358\u8ABF\u6E1B\u5C11\u3067\u3042\u308B\u3068\u304D, \u6574\u6570\u4E0A\u3067\
    \u4E8C\u90E8\u63A2\u7D22\u3092\u884C\u3044, cond(x) \u304C\u771F\u306B\u306A\u308B\
    \u6700\u5927\u306E\u6574\u6570 x \u3092\u6C42\u3081\u308B.\n\n    Args:\n    \
    \    L (int): \u89E3\u306E\u4E0B\u9650\n        R (int): \u89E3\u306E\u4E0A\u9650\
    \n        cond (Callable[[int], bool]): \u6761\u4EF6(1\u5909\u6570\u95A2\u6570\
    , \u5E83\u7FA9\u5358\u8ABF\u6E1B\u5C11\u3092\u6E80\u305F\u3059)\n        default\
    \ (Any, optional): L \u3067\u6761\u4EF6\u3092\u6E80\u305F\u3055\u306A\u3044 (\u3064\
    \u307E\u308A, [L, R] \u4E0A\u3067\u306F\u5E38\u306B\u507D) \u3068\u304D\u306E\u8FD4\
    \u308A\u5024. Defaults to None.\n\n    Returns:\n        int: cond(x) \u304C\u771F\
    \u306B\u306A\u308B\u6700\u5C0F\u306E\u6574\u6570 x\n    \"\"\"\n\n    if not cond(L):\n\
    \        return default\n\n    if cond(R):\n        return R\n\n    L -= 1\n \
    \   while R - L > 1:\n        C = L + (R - L) // 2\n        if cond(C):\n    \
    \        L = C\n        else:\n            R = C\n    return L\n\ndef General_Binary_Increase_Search_Real(L:\
    \ float, R: float, cond, trial: int, default: float = None) -> float:\n    \"\"\
    \" \u6761\u4EF6\u5F0F cond \u304C\u5358\u8ABF\u5897\u52A0\u3067\u3042\u308B\u3068\
    \u304D, \u5B9F\u6570\u4E0A\u3067\u306E cond \u306B\u95A2\u3059\u308B\u4E8C\u5206\
    \u63A2\u7D22\u3092\u884C\u3044, cond(x) \u304C\u771F\u306B\u306A\u308B\u6700\u5C0F\
    \u306E\u5B9F\u6570 x \u306E\u8FD1\u4F3C\u5024\u3092\u6C42\u3081\u308B.\n\n   \
    \ Args:\n        L (float): \u4E0B\u9650\n        R (float): \u4E0A\u9650\n  \
    \      cond (Callable[[float], bool]): \u6761\u4EF6\u5F0F (\u5358\u8ABF\u5897\u52A0\
    )\n        trial (int): \u5224\u5B9A\u56DE\u6570\u306E\u6700\u5927\u5024\n   \
    \     default (float, optional): cond(R) \u304C\u507D\u306B\u306A\u308B\u3068\u304D\
    \u306E\u8FD4\u308A\u5024. Defaults to None.\n\n    Returns:\n        float: cond(x)\
    \ \u304C\u6700\u5C0F\u306B\u306A\u308B\u5B9F\u6570 x \u306E\u8FD1\u4F3C\u5024\n\
    \    \"\"\"\n\n    # [L, R] \u3067\u631F\u3081\u306A\u3044\u5834\u5408\u3092\u5148\
    \u306B\u51E6\u7406\u3059\u308B.\n    if not cond(R):\n        return default\n\
    \n    if cond(L):\n        return L\n\n    for _ in range(trial):\n        C =\
    \ L + (R - L) / 2\n        if cond(C):\n            R = C\n        else:\n   \
    \         L = C\n\n    return (L + R) / 2\n\ndef General_Binary_Decrease_Search_Real(L:\
    \ float, R: float, cond, trial: int, default: float = None) -> float:\n    \"\"\
    \" \u6761\u4EF6\u5F0F cond \u304C\u5358\u8ABF\u6E1B\u5C11\u3067\u3042\u308B\u3068\
    \u304D, \u5B9F\u6570\u4E0A\u3067\u306E cond \u306B\u95A2\u3059\u308B\u4E8C\u5206\
    \u63A2\u7D22\u3092\u884C\u3044, cond(x) \u304C\u771F\u306B\u306A\u308B\u6700\u5927\
    \u306E\u5B9F\u6570 x \u306E\u8FD1\u4F3C\u5024\u3092\u6C42\u3081\u308B.\n\n   \
    \ Args:\n        L (float): \u4E0B\u9650\n        R (float): \u4E0A\u9650\n  \
    \      cond (Callable[[float], bool]): \u6761\u4EF6\u5F0F (\u5358\u8ABF\u5897\u52A0\
    )\n        trial (int): \u5224\u5B9A\u56DE\u6570\u306E\u6700\u5927\u5024\n   \
    \     default (float, optional): cond(L) \u304C\u507D\u306B\u306A\u308B\u3068\u304D\
    \u306E\u8FD4\u308A\u5024. Defaults to None.\n\n    Returns:\n        float: cond(x)\
    \ \u304C\u6700\u5927\u306B\u306A\u308B\u5B9F\u6570 x \u306E\u8FD1\u4F3C\u5024\n\
    \    \"\"\"\n\n    # [L, R] \u3067\u631F\u3081\u306A\u3044\u5834\u5408\u3092\u5148\
    \u306B\u51E6\u7406\u3059\u308B.\n\n    if not cond(L):\n        return default\n\
    \n    if cond(R):\n        return R\n\n    for _ in range(trial):\n        C =\
    \ L + (R - L) / 2\n        if cond(C):\n            L = C\n        else:\n   \
    \         R = C\n\n    return (L + R) / 2\n"
  dependsOn: []
  isVerificationFile: false
  path: Binary_Search/General.py
  requiredBy: []
  timestamp: '2025-04-13 21:10:57+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Binary_Search/General.py
layout: document
title: General Binary Search
---

## Outline

整数 (実数) $x$ に関する条件 $\operatorname{cond}(x)$ について, 以下を求める.

* $\operatorname{cond}$ が単調増加の場合 : $\operatorname{cond}(x)=\mathbb{T}$ になるような最小の整数 (実数) $x$.
* $\operatorname{cond}$ が単調減少の場合 : $\operatorname{cond}(x)=\mathbb{T}$ になるような最大の整数 (実数) $x$.

## Theory

$X$ は $\mathbb{Z}$ か $\mathbb{R}$ であるとする. $X$ 上の条件 $\operatorname{cond}: X \to \\{\mathbb{T}, \mathbb{F}\\}$ について, 以下を定義する.

* 以下を満たすとき, $\operatorname{cond}$ は単調増加であるという: $\forall x \in X;\,\operatorname{cond}(x)=\mathbb{T} \Rightarrow \left(\forall y \geq x;\, \operatorname{cond}(x)=\mathbb{T} \right)$
* 以下を満たすとき, $\operatorname{cond}$ は単調減少であるという: $\forall x \in X;\,\operatorname{cond}(x)=\mathbb{F} \Rightarrow \left(\forall y \geq x;\,\operatorname{cond}(x)=\mathbb{F} \right)$
* 単調増加または単調減少であるとき, 単調という.

$X=\mathbb{Z}$ とする. このとき, 単調増加である $\operatorname{cond}$ に対して, $\operatorname{cond}(x)=\mathbb{T}$ となる最小の $x \in \mathbb{Z}$ を $X$ として, $X$ を求める.

1. $L,R \in \mathbb{Z}$ を $\operatorname{cond}(L)=\mathbb{F}, \operatorname{cond}(R)=\mathbb{T}$ であるとする. このとき, $L \lt X \leq R$ が保証されている.
2. $R-L>1$ である限り, 以下を繰り返し行う.
    * $C:=\left \lfloor \dfrac{L+R}{2} \right \rfloor$ とする.
    * $\operatorname{cond}(C)=\mathbb{T}$ ならば, $L \lt X \leq C$ であることが分かる. よって, $R \gets C$ とする.
    * $\operatorname{cond}(C)=\mathbb{F}$ ならば, $C \lt X \leq L$ であることが分かる. よって, $L \gets C$ とする.
3. $R-L>1$ のとき, 初期値の定め方から, $R-L=1$ である. よって, $L \lt X \leq R$ となる整数 $X$ は $X=R$ に限られる. 従って, $R$ を出力すれば良い.

$\operatorname{cond}$ が単調減少の場合も同様であり, $X=\mathbb{R}$ の場合も $C:=\dfrac{L+R}{2}$ と変更すればよい. ただし, $X=\mathbb{R}$ の場合は厳密に求めることは不可能であり, ある程度の誤差の範囲で求めることになる.

また, $L, R$ は自分で見つける必要があり, $L,R$ が最初に満たすべき条件 (単調増加か単調減少かでかわる) を満たしていない場合は例外処理となる (特に $\operatorname{cond}(L)=\operatorname{cond}(R)=\mathbb{F}$) のとき.
