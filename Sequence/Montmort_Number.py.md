---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test_verify/yosupo_library_checker/Math/Montmort_Number.test.py
    title: test_verify/yosupo_library_checker/Math/Montmort_Number.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.3/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.3/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def Montmort_Number(N, Mod=None):\n    \"\"\" k=0,1,...,N \u306B\u95A2\u3057\
    \u3066, k \u8981\u7D20\u64B9\u4E71\u9806\u5217\u306E\u500B\u6570\u3092\u6C42\u3081\
    \u308B.\n    \"\"\"\n    if N<0:\n        return []\n    elif N==0:\n        return\
    \ [0]\n\n    X=[0]*(N+1)\n    if Mod==None:\n        for k in range(2, N+1):\n\
    \            X[k]=k*X[k-1]+(-1 if k%2 else 1)\n    else:\n        for k in range(2,\
    \ N+1):\n            X[k]=(k*X[k-1]+(-1 if k%2 else 1))%Mod\n\n    return X\n\n"
  dependsOn: []
  isVerificationFile: false
  path: Sequence/Montmort_Number.py
  requiredBy: []
  timestamp: '2022-11-25 11:47:07+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test_verify/yosupo_library_checker/Math/Montmort_Number.test.py
documentation_of: Sequence/Montmort_Number.py
layout: document
title: Montmort Number
---

## Theory

$N$ を正の整数とする. $\sigma \in \mathfrak{S}\_N$ が以下を満たす時, $\sigma$ を撹乱順列 (完全順列) という.

* $\forall i \in \\{1,2, \dots, N\\}; \sigma(i) \neq i$

$\mathfrak{S}\_N$ にある撹乱順列の個数を $M_N$ と書く. このとき, $M_N$ は次の式で表される.

$$M_N=\begin{cases} 0 & (N=1) \\ 1 & (N=2) \\ (N-1)(M_{N-1}+M_{N-2}) & (N \geq 3) \end{cases}$$

実際, $N=1,2$ の時は簡単に確かめる事ができる. $N \geq 3$ のとき, 撹乱順列 $\sigma \in \mathfrak{S}\_N$ において, $k:=\sigma(1)$ として, $\sigma(k)$ の値で場合分けをする.

* $\sigma(k)=1$ のとき, $(\sigma(2), \sigma(3), \dots, \sigma(k-1), \sigma(k+1), \dots, \sigma(N))$ は $(2,3, \dots, k-1, k+1, N)$ の $(N-2)$ 要素の撹乱順列になっている. また, 逆も成り立つ. よって, この場合は $M\_{N-2}$ 通りである.
* $\sigma(k) \neq 1$ のとき, $(\sigma(2), \dots, \sigma(N))$ は $(1,2, \dots, k-1, k+1, \dots, N)$ の並び替えであるが, 各 $i=2,3, \dots, N$ に対して, $\sigma(i)$ として禁止される値が $(1,2, \dots, k-1, k+1, \dots, N)$ の中に指定されている. 実際, $i=2,3, \dots, N$ に対して, $i \neq k$ ならば, $\sigma(i) \neq i$, $i=k$ ならば, $\sigma(k) \neq 1$ (場合分けの条件から) である. 各 $k$ に対して, このような順列の数は $M\_{N-1}$ 個である.

よって, $\sigma(1)=k$ となるような攪乱順列の個数は $(M\_{N-1}+M\_{N-2})$ 個であり, $k=2,3, \dots, N$ の場合を考えることによって,

$$M_N=(N-1)(M_{N-1}+M_{N-2})$$

となる.

また, この漸化式を変形すると,

$$M_N-N M_{N-1}=-(M_{N-1}-(N-1) M_{N-2})$$

である. よって,

$$\begin{align*}
M_{N}-N M_{N-1}
&=-(M_{N-1}-(N-1) M_{N-2}) \\
&=(-1)^2 (M_{N-2}-(N-2) M_{N-3}) \\
&=\vdots \\
&=(-1)^{N-2} (M_{2}-2M_{1})\\
&=(-1)^N (1-2 \times 0) \\
&=(-1)^N
\end{align*}$$

であるから, $(M\_N)$ は二項間漸化式

$$M_N=\begin{cases} 0 & (N=1) \\ NM_{N-1}+(-1)^N & (N \geq 2) \end{cases}$$

ともなる.
