---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links:
    - https://judge.yosupo.jp/submission/28692
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.4/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.4/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from Modulo_Polynomial import *\n\n#===\u6F38\u5316\u5F0F\ndef Nth_Term_of_Linearly_Recurrent_Sequence(A,\
    \ C, N, offset=0):\n    \"\"\" A[i]=C[0]*A[i-1]+C[1]*A[i-2]+...+C[d-1]*A[i-d]\
    \ \u3067\u8868\u3055\u308C\u308B\u6570\u5217 (A[i]) \u306E\u7B2C N \u9805\u3092\
    \u6C42\u3081\u308B.\n\n    A=(A[0], ..., A[d-1]): \u6700\u521D\u306E d \u9805\n\
    \    C=(C[0], ..., C[d-1]): \u7DDA\u5F62\u6F38\u5316\u5F0F\n    N: \u6C42\u3081\
    \u308B\u9805\u6570\n    offset: \u305A\u3089\u3059\u9805\u6570 (\u521D\u9805\u304C\
    \u7B2C offset \u9805\u306B\u306A\u308B)\n    \"\"\"\n\n    assert len(A)==len(C)\n\
    \    d=len(A)\n\n    N-=offset\n\n    if N<0:\n        return 0\n    elif N<d:\n\
    \        return A[N]%Mod\n\n    A=Modulo_Polynomial(A,d+1)\n    Q=Modulo_Polynomial([-C[i-1]\
    \ if i else 1  for i in range(d+1)], d+1)\n\n    P=A*Q; P[d]=0\n    return Polynominal_Coefficient(P,Q,N)\n\
    \ndef Find_Linear_Recurrence(A):\n    \"\"\" A \u304B\u3089\u63A8\u5B9A\u3055\u308C\
    \u308B\u6700\u5C0F\u306E\u9577\u3055\u306E\u95A2\u4FC2\u5F0F\u3092\u6C42\u3081\
    \u308B.\n\n    Reference: https://judge.yosupo.jp/submission/28692\n    \"\"\"\
    \n\n    N=len(A)\n    B=[1]; C=[1]\n    l=0; m=0; p=1\n    for i in range(N):\n\
    \        m+=1\n        d=A[i]\n        for j in range(1,l+1):\n            d+=C[j]*A[i-j]\n\
    \            d%=Mod\n        if d==0:\n            continue\n\n        T=C.copy()\n\
    \        q=pow(p, -1, Mod)*d%Mod\n        C=C+[0]*(len(B)+m-len(C))\n\n      \
    \  for j in range(len(B)):\n            C[j+m]-=q*B[j]\n            C[j+m]%=Mod\n\
    \        if 2*l<=i:\n            B=T\n            l,m,p=i+1-l,0,d\n\n    return\
    \ [Mod-c if c else 0 for c in C[1:]]\n\ndef Fibonacci(N):\n    \"\"\" Fibonacci\
    \ \u5217\u306E\u7B2C N \u9805\u3092\u6C42\u3081\u308B.\n\n    \"\"\"\n    return\
    \ Nth_Term_of_Linearly_Recurrent_Sequence([0,1],[1,1],N)\n\ndef Lucas(N):\n  \
    \  \"\"\" Lucas \u5217\u306E\u7B2C N \u9805\u3092\u6C42\u3081\u308B.\n\n    \"\
    \"\"\n\n    return Nth_Term_of_Linearly_Recurrent_Sequence([2,1],[1,1],N)\n\n\
    def Cumulative(A,N):\n    \"\"\" d:=|A| \u3068\u3057\u3066, \u6F38\u5316\u5F0F\
    \ A[i]=A[i-1]+...+A[i-d] \u3067\u8868\u3055\u308C\u308B\u5217 A \u306E\u7B2C N\
    \ \u9805\u3092\u6C42\u3081\u308B.\n\n    \"\"\"\n\n    return Nth_Term_of_Linearly_Recurrent_Sequence(A,\
    \ [1]*len(A), N)\n\ndef Factorial_Modulo(N):\n    \"\"\" N! mod Mod \u3092\u6C42\
    \u3081\u308B.\n\n    \"\"\"\n    from collections import deque\n\n    if N==0:\n\
    \        return 1\n\n    if N>=Mod:\n        return 0\n\n    M=0\n    while (M+1)*(M+1)<=N:\n\
    \        M+=1\n\n    A=Calc.Multiple_Convolution(*[[i,1] for i in range(1,M+1)])\n\
    \    H=Multipoint_Evaluation(Modulo_Polynomial(A,M+1),\n                     \
    \       [i*M for i in range(M)])\n\n    X=1\n    for h in H:\n        X*=h; X%=Mod\n\
    \n    for i in range(M*M+1, N+1):\n        X*=i; X%=Mod\n    return X\n\n#===\
    \ \u7279\u5225\u306A\u6570\u5217\ndef Bernoulli(N, mode=0):\n    \"\"\"\u30D9\u30EB\
    \u30CC\u30FC\u30A4\u6570 B_0,B_1,...,B_N \u306E (mod Mod) \u3067\u306E\u5024\u3092\
    \u6C42\u3081\u308B.\n    \"\"\"\n\n    P=Exp(Modulo_Polynomial([0,1],N+2))[1:]\n\
    \    F=P.inverse().Poly[:-1]\n\n    if mode==0:\n        fact=1\n        for i\
    \ in range(2,N+1):\n            fact=(fact*i)%Mod\n        return F[-1]*fact%Mod\n\
    \    else:\n        fact=1\n        for i in range(N+1):\n            F[i]=(F[i]*fact)%Mod\n\
    \            fact=(fact*(i+1))%Mod\n        return F\n\ndef PartitionsP(N, mode=0):\n\
    \    \"\"\"\u5206\u5272\u6570 p(0),...,p(N) (mod Mod) \u3092\u6C42\u3081\u308B\
    .\n\n    p(k):=k\u3092\u9806\u5E8F\u3092\u533A\u5225\u305B\u305A\u306B\u81EA\u7136\
    \u6570\u306E\u548C\u306B\u5206\u3051\u308B\u5834\u5408\u306E\u6570\n    \"\"\"\
    \n\n    F=[0]*(N+1)\n    F[0]=1\n    k=1\n    while k*(3*k-1)<=2*N:\n        m=-1\
    \ if k&1 else 1\n        F[k*(3*k-1)//2]+=m\n\n        if k*(3*k+1)<=2*N:\n  \
    \          F[k*(3*k+1)//2]+=m\n        k+=1\n\n    if mode==0:\n        return\
    \ Calc.Inverse(F)[-1]\n    else:\n        return Calc.Inverse(F)\n\ndef PartitionsQ(N,\
    \ mode=0):\n    \"\"\" \u5404\u9805\u304C\u76F8\u7570\u306A\u308B N \u306E\u5206\
    \u5272\u306E\u6570\u3092\u6C42\u3081\u308B.\n\n    \"\"\"\n\n    Inv=[0]*(N+1)\n\
    \    Inv[1]=1\n    for i in range(2,N+1):\n        Inv[i]=(-(Mod//i)*Inv[Mod%i])%Mod\n\
    \n    F=[0]*(N+1)\n    for i in range(1,N+1):\n        j=i\n        k=1\n    \
    \    c=1\n        while j<=N:\n            F[j]=(F[j]+c*Inv[k])%Mod\n        \
    \    c*=-1\n            j+=i\n            k+=1\n    P=Modulo_Polynomial(F,N+1)\n\
    \n    if mode==0:\n        return Exp(P)[N]\n    else:\n        return Exp(P).Poly\n\
    \ndef Stirling_1st(N):\n    \"\"\" k=0,1, ..., N \u306B\u5BFE\u3059\u308B\u7B2C\
    \ I \u7A2E Stirling \u6570\u3092\u6C42\u3081\u308B.\n\n    \"\"\"\n\n    def g(n):\n\
    \        if n==0:\n            return Modulo_Polynomial([1],N+1)\n        elif\
    \ n==1:\n            return Modulo_Polynomial([0,1], N+1)\n        elif n&1:\n\
    \            return Modulo_Polynomial([-n+1, 1],N+1)*g(n-1)\n        else:\n \
    \           P=g(n//2)\n            return P*Taylor_Shift(P, -n//2)\n\n    return\
    \ g(N).Poly\n\ndef Stirling_2nd(N):\n    \"\"\" k=0,1, ..., N \u306B\u5BFE\u3059\
    \u308B\u7B2C II \u7A2E Stirling \u6570 (\u533A\u5225\u306E\u3067\u304D\u308B N\
    \ \u500B\u306E\u3082\u306E\u3092\u533A\u5225\u3067\u304D\u306A\u3044 K \u500B\u306E\
    \u30B0\u30EB\u30FC\u30D7 (\u7A7A\u30B0\u30EB\u30FC\u30D7\u7981\u6B62) \u306B\u5206\
    \u5272\u3059\u308B\u65B9\u6CD5) \u3092\u6C42\u3081\u308B.\n\n    \"\"\"\n\n  \
    \  fact=[0]*(N+1); fact[0]=1\n    for i in range(1,N+1):\n        fact[i]=i*fact[i-1]%Mod\n\
    \n    fact_inv=[0]*(N+1); fact_inv[-1]=pow(fact[-1], -1, Mod)\n    for i in range(N-1,-1,-1):\n\
    \        fact_inv[i]=(i+1)*fact_inv[i+1]%Mod\n\n    A=[pow(i,N,Mod)*fact_inv[i]%Mod\
    \ for i in range(N+1)]\n    B=[fact_inv[i] if i&1==0 else -fact_inv[i] for i in\
    \ range(N+1)]\n    return Calc.Convolution(A,B)[:N+1]\n\ndef Bell(N, mode=0):\n\
    \    \"\"\" Bell \u6570 (\u96C6\u5408 {1,2,...,N} \u306E\u5206\u5272\u306E\u65B9\
    \u6CD5) B[N] \u3092\u6C42\u3081\u308B.\n\n    \"\"\"\n    F=Exp(Exp(Modulo_Polynomial([0,1],N+1))-1).Poly\n\
    \    fact=1\n    for i in range(1,N+1):\n        fact=(i*fact)%Mod\n        F[i]=(fact*F[i])%Mod\n\
    \n    if mode:\n        return F\n    else:\n        return F[N]\n\ndef Motzkin(N,\
    \ mode=0):\n    \"\"\" Motzkin \u6570 (\u5186\u5468\u4E0A\u306E\u533A\u5225\u304C\
    \u3064\u304F\u76F8\u7570\u306A\u308B N \u70B9\u3092\u7DDA\u5206\u3092\u3069\u306E\
    2\u3064\u3082\u5171\u901A\u90E8\u5206\u304C\u306A\u3044 (N \u70B9\u3067\u5171\u6709\
    \u3082\u7981\u6B62) \u3067\u7D50\u3076\u65B9\u6CD5 (\u7D50\u3070\u308C\u306A\u3044\
    \u70B9\u304C\u3042\u3063\u3066\u3082\u3088\u3044) \u306E\u6570.\n\n    \"\"\"\n\
    \n    two_inv=pow(2, -1, Mod)\n    F=((Modulo_Polynomial([1,-1], N+3)-Sqrt(Modulo_Polynomial([1,-2,-3],\
    \ N+3)))*two_inv)>>2\n\n    if mode:\n        return F.Poly[:N+1]\n    else:\n\
    \        return F[N]\n\n#===\ndef Subset_Sum(X, K):\n    \"\"\" X \u306E\u8981\
    \u7D20\u306E\u3046\u3061, \u4EFB\u610F\u500B\u3092\u7528\u3044\u3066, \u548C\u304C\
    \ k=0,1,...,K \u306B\u306A\u308B\u7D44\u307F\u5408\u308F\u305B\u306E\u7DCF\u6570\
    \u3092 Mod \u3067\u5272\u3063\u305F\u4F59\u308A\u3092\u6C42\u3081\u308B.\n\n \
    \   X: \u30EA\u30B9\u30C8\n    K: \u975E\u8CA0\u6574\u6570\n    \"\"\"\n    A=[0]*(K+1)\n\
    \    for x in X:\n        if x<=K:\n            A[x]+=1\n\n    Inv=[0]*(K+1)\n\
    \    Inv[1]=1\n    for i in range(2,K+1):\n        Inv[i]=(-(Mod//i)*Inv[Mod%i])%Mod\n\
    \n    F=[0]*(K+1)\n    for i in range(1,K+1):\n        if A[i]:\n            j=i\n\
    \            k=1\n            c=1\n            while j<=K:\n                F[j]=(F[j]+c*Inv[k]*A[i])%Mod\n\
    \                c*=-1\n                j+=i\n                k+=1\n    P=Modulo_Polynomial(F,K+1)\n\
    \    return Exp(P).Poly\n\n#===\n#\u591A\u9805\u5F0F\u548C\ndef Polynominal_Sigma(P):\n\
    \    \"\"\" Q(n)=P(1)+P(2)+...+P(n) \u3092\u6E80\u305F\u3059\u591A\u9805\u5F0F\
    \ Q \u3092\u6C42\u3081\u308B.\n\n    \"\"\"\n\n    from itertools import accumulate\n\
    \n    N=len(P.Poly)\n    A=Multipoint_Evaluation(P, list(range(1,N+2)))\n    A=list(accumulate(A,lambda\
    \ x,y:(x+y)%Mod))\n    return Polynominal_Interpolation(list(range(1,N+2)), A)\n\
    \ndef Differences(P, k=1):\n    \"\"\" P \u306E k- \u5DEE\u5206 D[k](P(n))=D[k-1](P(n+1)-P(n)),\
    \ D[0](P)=P \u3092\u6C42\u3081\u308B. \"\"\"\n\n    N=len(P.Poly)\n\n    fact=[1]*(k+1)\n\
    \    for i in range(1,k+1):\n        fact[i]=i*fact[i-1]%Mod\n\n    fact_inv=[1]*(k+1);\
    \ fact_inv[-1]=pow(fact[i], -1, Mod)\n    for i in range(k-1,-1,-1):\n       \
    \ fact_inv[i]=(i+1)*fact_inv[i+1]%Mod\n\n    Q=[0]*(N-k)\n    sgn=1 if k%2==0\
    \ else -1\n\n    for r in range(k+1):\n        alpha=sgn*fact[k]*(fact_inv[r]*fact_inv[k-r]%Mod)%Mod\n\
    \        for j in range(N-k):\n            Q[j]+=alpha*P[j]%Mod\n\n        if\
    \ r!=k:\n            sgn*=-1\n            P=Taylor_Shift(P,1)\n\n    return Modulo_Polynomial(Q,P.max_degree)\n"
  dependsOn: []
  isVerificationFile: false
  path: Modulo_Sequence/Modulo_Sequence.py
  requiredBy: []
  timestamp: '2023-08-06 21:39:33+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Modulo_Sequence/Modulo_Sequence.py
layout: document
title: Modulo Sequence
---

## Outline

線形漸化式で表された数列に関する計算を行う.

## Theory

### 線形漸化式の第 $N$ 項

数列 $A=(A_n)$ は漸化式

$$A_n=\sum_{k=0}^{d-1} C_k A_{n-k-1} \quad (n \geq d)$$

を満たしているとする.

このとき, 形式的ベキ級数 $Q$, 多項式 $P$ をそれぞれ

- $Q(X)=1-C_0 X-C_1 X^2-\dots-C_{d-1} X^d$
- $P(X)=(A_0+A_1 X+\dots+A_{d-1} X^{d-1}) Q(X) \pmod{X^d}$

とすると, 任意の非負整数 $n$ において,

$$A_n=\left[X^n \right] \dfrac{P(X)}{Q(X)}$$

となる.

### 分割数

非負整数 $N$ に対して, $N$ を $0$ 個以上の正の整数の和で表す方法 (ただし, 順番の違いは同一視する) を分割数といい, $P_N$ と書く.

このとき, $P_N$ は

$$P_N=\left[X^N \right] \prod_{n=1}^\infty \dfrac{1}{1-X^n}$$

である.

なお, 五角数定理 により,

$$\prod_{n=1}^\infty (1-X^n)=\sum_{n=-\infty}^{\infty} (-1)^n X^{n(3n-1)/2}$$

となるから, 高速化できる.

### 相異なる整数への分割

非負整数 $N$ に対して, $N$ を $0$ 個以上相異なる正の整数の和で表す方法 (ただし, 順番の違いは同一視する) を $Q_N$ と書く.

このとき, $Q_N$ は

$$Q_N=\left[X^N \right] \prod_{n=1}^\infty (1+X^n)$$

である.

なお, ベキ級数展開することによって,

$$1+X^n=\exp \left(\log (1+X^n) \right)=\exp \left( \sum_{k=1}^\infty (-1)^{k-1} X^{kn} \right)$$

であるから,

$$Q_N=\left[X^N \right] \exp \left(\sum_{n=1}^\infty \sum_{k=1}^\infty (-1)^{k-1} X^{kn} \right)$$

となる. なお, $Q_N$ を求める際には, $N$ 次まであれば十分でるが, $kn \leq N$ となる非負整数の組の個数は $O(N \log N)$ 個程度になる.

## Contents

---

### Nth_Term_of_Linearly_Recurrent_Sequence

```Pyhon
Nth_Term_of_Linearly_Recurrent_Sequence(A, C, N, offset=0)
```

- $A,C$ の長さを $d$ とする.
- 線形漸化式 $\displaystyle A_n=\sum_{k=0}^{d-1} C_k A_{n-k-1} \quad (n \geq d)$ で表される整数列 $A=(A_i)$ の第 $N$ 項 $A_N$ を求める.
- **制約**
  - $A$ と $C$ の長さは等しい.
- **計算量** : $O(d \log d \log N)$ Time.

---

### Find_Linear_Recurrence

```Python
Find_Linear_Recurrence(A)
```

- 整数列 $A=(A_0, \dots, A_{N-1})$ が見たす最小の次数の漸化式を求める.

---

### Fibonacci

```Python
Fibonacci(N)
```

- 以下で定義される Fibonacci 数列 $F=(F_n)$ の第 $N$ 項を求める.
  - $F_0=0, F_1=1$
  - $F_n=F_{n-1}+F_{n-2} \quad (n \geq 2)$
- **計算量** : $O(\log N)$ Time.

---

### Lucas

```Python
Lucas(N)
```

- 以下で定義される Lucas 数列 $L=(L_n)$ の第 $N$ 項を求める.
  - $L_0=2, L_1=1$
  - $L_n=L_{n-1}+L_{n-2} \quad (n \geq 2)$
- **計算量** : $O(\log N)$ Time.

---

### Cumulative

```Python
Cumulative(A,N)
```

- $A$ の長さを $d$ とする. 以下で定義される数列 $B=(B_n)$ の第 $N$ 項を求める.
  - $B_n=A_n \quad (0 \leq n \leq d-1)$
  - $B_n=B_{n-1}+B_{n-2}+\dots+B_{n-d} \quad (n \geq d)$
- **計算量** : $A$ の長さを $d$ として, $O(d \log d \log N)$ Time.

---

### Factorial_Modulo

```Python
Factorial_Modulo(N)
```

- $N! \pmod{\mathrm{mod}}$ を求める.

- **計算量** : $O(\sqrt{N} (\log N)^2)$ Time.

---

### Bernoulli

```Python
Bernoulli(N, mode=0)
```

- Bernoulli 数を求める.
- ${\rm mode}=0$ ならば, $B_N$ のみ, ${\rm mode}=1$ ならば, $B_0, \dots, B_N$ からなるリスト.
- **計算量** : $O(N \log N)$ TIme.

---

### PartitionsP

```Python
PartitionsP(N, mode=0)
```

- 以下で定義される $P_k$ を求める.
  - 整数 $k$ を順番を考慮せずに自然数の和にわける場合の数
- ${\rm mode}=0$ ならば, $P_N$ のみ, ${\rm mode}=1$ ならば, $P_0, \dots, P_N$ からなるリスト.
- **計算量** : $O(N \log N)$ TIme.

---

### PartitionsQ

```Python
PartitionsQ(N, mode=0)
```

- 以下で定義される $Q_k$ を求める.
  - 整数 $k$ を相異なる自然数の和にわける場合の数
- ${\rm mode}=0$ ならば, $Q_N$ のみ, ${\rm mode}=1$ ならば, $Q_0, \dots, Q_N$ からなるリスト.
- **計算量** : $O(N \log N)$ TIme.

---

### Stirling_1st

``` Python
Stirling_1st(N)
```

- $k=0,1,\dots,N$ に対する第 I 種スターリング数 $\begin{bmatrix} n \\ k \end{bmatrix}$ を求める.
- **計算量** : $O(N (\log N)^2)$ Time ?

### Stirling_2nd

``` Python
Stirling_2nd(N)
```

- $k=0,1,\dots,N$ に対する第 II 種スターリング数 $\begin{Bmatrix} n \\ k \end{Bmatrix}$ を求める.
- **計算量** : $O(N \log N)$ Time.

### Bell

```Pythoon
Bell(N, mode=0)
```

- 次の式で定義される Bell 数 $B_n$ を求める. $\displaystyle \sum_{n=0}^\infty B_n x^n=\exp(\exp(x)-1)$

- ${\rm mode}=0$ ならば, $B_N$ のみ, ${\rm mode}=1$ ならば, $B_0, \dots, B_N$ からなるリスト.
- **計算量** : $O(N \log N)$ TIme.

### Motzkin

```Pythoon
Motzkin(N, mode=0)
```

- 次の式で定義される Motzkin 数 $M_n$ を求める. $\displaystyle \sum_{n=0}^\infty M_n x^n=\dfrac{1-x-\sqrt{1-2x-3x^2}}{2x^2}$

- ${\rm mode}=0$ ならば, $M_N$ のみ, ${\rm mode}=1$ ならば, $M_0, \dots, M_N$ からなるリスト.
- **計算量** : $O(N \log N)$ TIme.
