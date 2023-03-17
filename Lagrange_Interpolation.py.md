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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.2/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.2/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def Lagrange_Interpolation_Point(L,X,P):\n    \"\"\" \u6CD5\u304C P \u306E\
    \u4E0B\u3067\u306ELagrange \u88DC\u9593\u3092\u884C\u3044, x=X \u3067\u306E\u5024\
    \u3092\u8FD4\u3059.\n\n    [Input]\n    L: [(x_0,y_0), ..., (x_N, y_N)]: F(x_i)=y_i\
    \ (mod P)\n    X: F(X) \u3092\u8FD4\u3059.\n    P: \u6CD5\n\n    [Output]\n  \
    \  F(X)\n\n    [Complexity]\n    O(N^2+log P)\n    \"\"\"\n\n    N=len(L)-1\n\n\
    \    x=[p[0] for p in L]\n    y=[p[1] for p in L]\n\n    X%=P\n    Y=0\n    for\
    \ i in range(N+1):\n        a=b=1\n        for j in range(N+1):\n            if\
    \ i==j: continue\n            a*=X-x[j]; a%=P\n            b*=x[i]-x[j]; b%=P\n\
    \        c=(a*pow(b,P-2,P))%P\n        Y+=y[i]*c; Y%=P\n    return Y\n\ndef Lagrange_Interpolation_Polynomial(T,P):\n\
    \    \"\"\" \u6CD5\u304C P \u306E\u4E0B\u3067\u306ELagrange \u88DC\u9593\u3092\
    \u884C\u3044, \u591A\u9805\u5F0F\u306E\u4FC2\u6570\u30EA\u30B9\u30C8\u3092\u8FD4\
    \u3059.\n\n    [Input]\n    T: [(x_0,y_0), ..., (x_N, y_N)]: F(x_n)=y_n  (i !=j\
    \ => x_i != x_j (mod P))\n    P: \u6CD5\n\n    [Output]\n    [[X^0]F, [X^1]F,\
    \ ..., [X^{N-1}]F ]\n\n    [Complexity]\n    O(N^2)\n\n    [Thanks]\n    hamayanhamayan\n\
    \    \"\"\"\n\n    N=len(T)\n    X=[0]*N; Y=[0]*N\n    for i in range(N):\n  \
    \      X[i]=T[i][0]\n        Y[i]=T[i][1]\n\n    Poly=[0]*(N+1); Poly[0]=1\n \
    \   for x,y in zip(X,Y):\n        tmp=[0]*(N+1)\n        for i in range(N):\n\
    \            tmp[i+1]=Poly[i]\n        for i in range(N):\n            tmp[i]=(tmp[i]-x*Poly[i])%P\n\
    \        Poly=tmp\n\n    res=[0]*N\n    for i,(x,y) in enumerate(zip(X,Y)):\n\
    \        if y==0:\n            continue\n\n        Q=1\n        for j in range(N):\n\
    \            if j!=i:\n                Q=Q*(x-X[j])%P\n        Q=pow(Q,P-2,P)\n\
    \n        tmp=Poly.copy()\n\n        for j in  range(N,0,-1):\n            res[j-1]=(res[j-1]+(tmp[j]*Q)%P*y)%P\n\
    \            tmp[j-1]=(tmp[j-1]+tmp[j]*x)%P\n    return res\n\ndef Lagrange_Interpolation_Point_Arithmetic(L,a,b,X,P):\n\
    \    \"\"\" \u6CD5\u304C P \u306E\u4E0B\u3067\u306ELagrange \u88DC\u9593\u3092\
    \u884C\u3044, x=X \u3067\u306E\u5024\u3092\u8FD4\u3059. \u305F\u3060\u3057, x_i=ai+b\n\
    \n    [Input]\n    L: [y_0, ..., y_n]: F(x_i)=y_i (mod P)\n    X: F(X) \u3092\u8FD4\
    \u3059.\n    P: \u6CD5\n\n    [Output]\n    F(X)\n\n    [Complexity]\n    O(N+log\
    \ P)\n    \"\"\"\n\n    d=len(L)-1\n\n    X%=P\n    Left=[1]*(d+1)\n    for i\
    \ in range(d+1):\n        if i:\n            Left[i]=(Left[i-1]*(X-(a*i+b)))%P\n\
    \        else:\n            Left[i]=(X-(a*i+b))%P\n\n    Right=[1]*(d+1)\n   \
    \ for i in range(d,-1,-1):\n        if i<d:\n            Right[i]=(Right[i+1]*(X-(a*i+b)))%P\n\
    \        else:\n            Right[i]=(X-(a*i+b))%P\n\n    fact=1\n    for i in\
    \ range(1,d+1): fact=(fact*i)%P\n\n    Fact_inv=[1]*(d+1); Fact_inv[-1]=pow(fact,P-2,P)\n\
    \    for i in range(d-1,-1,-1):\n        Fact_inv[i]=(Fact_inv[i+1]*(i+1))%P\n\
    \n    Y=0\n    coef=pow(-a,d*(P-2),P)\n\n    for i in range(d+1):\n        V_inv=(Fact_inv[i]*Fact_inv[d-i])%P\n\
    \        if i==0:\n            S=(Right[i+1]*V_inv)%P\n        elif i==d:\n  \
    \          S=(Left[i-1]*V_inv)%P\n        else:\n            u=(Left[i-1]*Right[i+1])%P\n\
    \            S=(u*V_inv)%P\n\n        M=L[i]*S%P\n        Y=(Y+coef*M)%P\n   \
    \     coef=-coef\n    return Y\n"
  dependsOn: []
  isVerificationFile: false
  path: Lagrange_Interpolation.py
  requiredBy: []
  timestamp: '2021-09-12 03:07:22+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Lagrange_Interpolation.py
layout: document
title: Lagrange Interpolation
---

## Outline

$(N+1)$ 個の条件 $y_i=f(x_i)$ $(0 \leq i \leq N)$ を満たす高々 $N$ 次多項式 $f(x)$ や, $f$ のある点での値 $f(X)$ を求める.

## Theory

$x_0, \dots, x_N$ は全て異なるとする. このとき, $(N+1)$ 個の条件式

$$y_i=f(x_i) \quad (0 \leq i\leq N)$$

を満たす高々 $N$ 次の多項式を求める. $x_0, \dots, x_N$ が全て異なるという条件下では $f$ は必ず一意に存在する.

$i=0,1,2, \dots, N$ に対して, Lagrange 基底多項式 $\ell_i(x)$ を

$$\ell_i(x):=\prod_{\substack{0 \leq k \leq N \\ k \neq i}} \dfrac{x-x_k}{x_i-x_k}$$

とする. このとき, $j=0,1, \dots, N$ に対して,

$$\ell_i(x_j)=[i=j]$$

が成り立つ.

よって,

$$f:=\sum_{i=0}^N y_i \ell_i$$

がその求めるべき多項式になる.

ここで, $x_0, \dots, x_N$ が等差数列であったとする. つまり, $x_i=ai+b$ であるとする. このとき,

$$x_i-x_k=(ai+b)-(ak+b)=a(i-k)$$

が成り立つから, Lagrange 基底多項式は

$$\begin{align*}
\ell_i(x)
&=\prod_{\substack{0 \leq k \leq N \\ k \neq i}} \dfrac{x-x_k}{x_i-x_k} \\
&=\prod_{\substack{0 \leq k \leq N \\ k \neq i}} \dfrac{x-(ai+b)}{a(i-k)} \\
&=\dfrac{1}{(-a)^N} \cdot \dfrac{ \mathrm{Left}_{i-1}(x) \cdot \mathrm{Right}_{i+1}(x)}{(-1)^{i} i! (N-i)!} \\
\end{align*}$$

である. ただし,

$$\mathrm{Left}_i(x):=\prod_{k=0}^i (x-(ak+b)), \quad \mathrm{Right}_i(x):=\prod_{k=i}^N (x-(ak+b))$$

である.

よって, 評価点の $x$ 座標が等差数列であるとき, ある点 $X$ での値 $f(X) \pmod{P} $ を $O(N+\log P)$ 時間で求めることができる.
