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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.8/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.8/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from Modulo_Polynominal import *\n\n#===\u6F38\u5316\u5F0F\ndef Nth_Term_of_Linearly_Recurrent_Sequence(A,C,N,offset=0):\n\
    \    \"\"\" A[i]=C[0]*A[i-1]+C[1]*A[i-2]+...+C[d-1]*A[i-d] \u3067\u8868\u3055\u308C\
    \u308B\u6570\u5217 (A[i]) \u306E\u7B2C N \u9805\u3092\u6C42\u3081\u308B.\n\n \
    \   A=(A[0], ..., A[d-1]): \u6700\u521D\u306E d \u9805\n    C=(C[0], ..., C[d-1]):\
    \ \u7DDA\u5F62\u6F38\u5316\u5F0F\n    N: \u6C42\u3081\u308B\u9805\u6570\n    offset:\
    \ \u305A\u3089\u3059\u9805\u6570 (\u521D\u9805\u304C\u7B2C offset \u9805\u306B\
    \u306A\u308B)\n    \"\"\"\n\n    assert len(A)==len(C)\n    d=len(A)\n\n    if\
    \ N<d:\n        return A[N]%Mod\n\n    A=Modulo_Polynominal(A,d+1)\n    Q=Modulo_Polynominal([-C[i-1]\
    \ if i else 1  for i in range(d+1)], d+1)\n\n    P=A*Q; P[d]=0\n    return Polynominal_Coefficient(P,Q,N-offset)\n\
    \ndef Find_Linear_Recurrence(A):\n    \"\"\" A \u304B\u3089\u63A8\u5B9A\u3055\u308C\
    \u308B\u6700\u5C0F\u306E\u9577\u3055\u306E\u95A2\u4FC2\u5F0F\u3092\u6C42\u3081\
    \u308B.\n\n    Reference: https://judge.yosupo.jp/submission/28692\n    \"\"\"\
    \n\n    N=len(A)\n    B=[1]; C=[1]\n    l=0; m=0; p=1\n    for i in range(N):\n\
    \        m+=1\n        d=A[i]\n        for j in range(1,l+1):\n            d+=C[j]*A[i-j]\n\
    \            d%=Mod\n        if d==0:\n            continue\n\n        T=C.copy()\n\
    \        q=pow(p,Mod-2,Mod)*d%Mod\n        C=C+[0]*(len(B)+m-len(C))\n\n     \
    \   for j in range(len(B)):\n            C[j+m]-=q*B[j]\n            C[j+m]%=Mod\n\
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
    \    H=Multipoint_Evaluation(Modulo_Polynominal(A,M+1),\n                    \
    \        [i*M for i in range(M)])\n\n    X=1\n    for h in H:\n        X*=h; X%=Mod\n\
    \n    for i in range(M*M+1, N+1):\n        X*=i; X%=Mod\n    return X\n\n#===\
    \ \u7279\u5225\u306A\u6570\u5217\ndef Bernoulli(N, mode=0):\n    \"\"\"\u30D9\u30EB\
    \u30CC\u30FC\u30A4\u6570 B_0,B_1,...,B_N \u306E (mod Mod) \u3067\u306E\u5024\u3092\
    \u6C42\u3081\u308B.\n    \"\"\"\n\n    P=Exp(Modulo_Polynominal([0,1],N+2))[1:]\n\
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
    \    c*=-1\n            j+=i\n            k+=1\n    P=Modulo_Polynominal(F,N+1)\n\
    \n    if mode==0:\n        return Exp(P)[N]\n    else:\n        return Exp(P)\n\
    \ndef Stirling_1st(N):\n    \"\"\" k=0,1, ..., N \u306B\u5BFE\u3059\u308B\u7B2C\
    \ I \u7A2E Stirling \u6570\u3092\u6C42\u3081\u308B.\n\n    \"\"\"\n\n    def g(n):\n\
    \        if n==0:\n            return Modulo_Polynominal([1],N+1)\n        elif\
    \ n==1:\n            return Modulo_Polynominal([0,1], N+1)\n        elif n&1:\n\
    \            return Modulo_Polynominal([-n+1, 1],N+1)*g(n-1)\n        else:\n\
    \            P=g(n//2)\n            return P*Taylor_Shift(P, -n//2)\n\n    return\
    \ g(N).Poly\n\ndef Stirling_2nd(N):\n    \"\"\" k=0,1, ..., N \u306B\u5BFE\u3059\
    \u308B\u7B2C II \u7A2E Stirling \u6570\u3092\u6C42\u3081\u308B.\n\n    \"\"\"\n\
    \n    fact=[0]*(N+1); fact[0]=1\n    for i in range(1,N+1):\n        fact[i]=i*fact[i-1]%Mod\n\
    \n    fact_inv=[0]*(N+1); fact_inv[-1]=pow(fact[-1],Mod-2,Mod)\n    for i in range(N-1,-1,-1):\n\
    \        fact_inv[i]=(i+1)*fact_inv[i+1]%Mod\n\n    A=[pow(i,N,Mod)*fact_inv[i]%Mod\
    \ for i in range(N+1)]\n    B=[fact_inv[i] if i&1==0 else -fact_inv[i] for i in\
    \ range(N+1)]\n    return Calc.Convolution(A,B)[:N+1]\n\ndef Bell(N, mode=0):\n\
    \    \"\"\" Bell \u6570 B[N] \u3092\u6C42\u3081\u308B.\n\n    \"\"\"\n    F=Exp(Exp(Modulo_Polynominal([0,1],N+1))-1).Poly\n\
    \    fact=1\n    for i in range(1,N+1):\n        fact=(i*fact)%Mod\n        F[i]=(fact*F[i])%Mod\n\
    \n    if mode:\n        return F\n    else:\n        return F[N]\n\n#===\ndef\
    \ Subset_Sum(X,K):\n    \"\"\" X \u306E\u8981\u7D20\u306E\u3046\u3061, \u4EFB\u610F\
    \u500B\u3092\u7528\u3044\u3066, \u548C\u304C k=0,1,...,K \u306B\u306A\u308B\u7D44\
    \u307F\u5408\u308F\u305B\u306E\u7DCF\u6570\u3092 Mod \u3067\u5272\u3063\u305F\u4F59\
    \u308A\u3092\u6C42\u3081\u308B.\n\n    X: \u30EA\u30B9\u30C8\n    K: \u975E\u8CA0\
    \u6574\u6570\n    \"\"\"\n    A=[0]*(K+1)\n    for x in X:\n        if x<=K:\n\
    \            A[x]+=1\n\n    Inv=[0]*(K+1)\n    Inv[1]=1\n    for i in range(2,K+1):\n\
    \        Inv[i]=(-(Mod//i)*Inv[Mod%i])%Mod\n\n    F=[0]*(K+1)\n    for i in range(1,K+1):\n\
    \        j=i\n        k=1\n        c=1\n        while j<=K:\n            F[j]=(F[j]+c*Inv[k]*A[i])%Mod\n\
    \            c*=-1\n            j+=i\n            k+=1\n    P=Modulo_Polynominal(F,K+1)\n\
    \    return Exp(P).Poly\n\n#===\n#\u591A\u9805\u5F0F\u548C\ndef Polynominal_Sigma(P):\n\
    \    \"\"\" Q(n)=P(1)+P(2)+...+P(n) \u3092\u6E80\u305F\u3059\u591A\u9805\u5F0F\
    \ Q \u3092\u6C42\u3081\u308B.\n\n    \"\"\"\n\n    from itertools import accumulate\n\
    \n    N=len(P.Poly)\n    A=Multipoint_Evaluation(P, list(range(1,N+2)))\n    A=list(accumulate(A,lambda\
    \ x,y:(x+y)%Mod))\n    return Polynominal_Interpolation(list(range(1,N+2)), A)\n\
    \ndef Differences(P, k=1):\n    \"\"\" P \u306E k- \u5DEE\u5206 D[k](P(n))=D[k-1](P(n+1)-P(n)),\
    \ D[0](P)=P \u3092\u6C42\u3081\u308B. \"\"\"\n\n    N=len(P.Poly)\n\n    fact=[1]*(k+1)\n\
    \    for i in range(1,k+1):\n        fact[i]=i*fact[i-1]%Mod\n\n    fact_inv=[1]*(k+1);\
    \ fact_inv[-1]=pow(fact[i],Mod-2,Mod)\n    for i in range(k-1,-1,-1):\n      \
    \  fact_inv[i]=(i+1)*fact_inv[i+1]%Mod\n\n    Q=[0]*(N-k)\n    sgn=1 if k%2==0\
    \ else -1\n\n    for r in range(k+1):\n        alpha=sgn*fact[k]*(fact_inv[r]*fact_inv[k-r]%Mod)%Mod\n\
    \        for j in range(N-k):\n            Q[j]+=alpha*P[j]%Mod\n\n        if\
    \ r!=k:\n            sgn*=-1\n            P=Taylor_Shift(P,1)\n\n    return Modulo_Polynominal(Q,P.max_degree)\n"
  dependsOn: []
  isVerificationFile: false
  path: Modulo_Sequence/Modulo_Sequence.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Modulo_Sequence/Modulo_Sequence.py
layout: document
redirect_from:
- /library/Modulo_Sequence/Modulo_Sequence.py
- /library/Modulo_Sequence/Modulo_Sequence.py.html
title: Modulo_Sequence/Modulo_Sequence.py
---
