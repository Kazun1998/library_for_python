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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.0/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.0/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "#==================================================\n#Sum\u7CFB\ndef Linear_Sum(a,\
    \ b, L, R):\n    \"\"\" Sum_{i=L}^R (ai+b) \u3092\u6C42\u3081\u308B.\n    \"\"\
    \"\n\n    if L<=R:\n        return (a*(L+R)+2*b)*(R-L+1)//2\n    else:\n     \
    \   return 0\n\ndef Box_Sum_Count(P, Q, R, S, K):\n    \"\"\"P<=X<=Q, R<=Y<=S,\
    \ X+Y=K \u3092\u6E80\u305F\u3059\u6574\u6570\u306E\u7D44 (X,Y) \u306E\u500B\u6570\
    \u3092\u51FA\u529B\u3059\u308B.\n\n    P,Q,R,S:int (P<=Q, R<=S)\n    \"\"\"\n\
    \    A=max(0,K-(P  +R  )+1)\n    B=max(0,K-(Q+1+R  )+1)\n    C=max(0,K-(P  +S+1)+1)\n\
    \    D=max(0,K-(Q+1+S+1)+1)\n    return A-B-C+D\n\ndef Interval_Sum_Count(L, R,\
    \ X):\n    \"\"\"L<=x,y<=R \u3092\u6E80\u305F\u30592\u3064\u306E\u6574\u6570x,y\u306E\
    \u3046\u3061, x+y=X \u3092\u6E80\u305F\u3059\u7D44(x,y) \u306E\u500B\u6570\u3092\
    \u51FA\u529B\u3059\u308B.\n\n    L,R:Int (L<=R)\n    X:Int\n    \"\"\"\n\n   \
    \ if L>R:\n        return 0\n\n    if 2*L<=X<=L+R:\n        return X-2*L+1\n \
    \   elif L+R<=X<=2*R:\n        return 2*R+1-X\n    else:\n        return 0\n\n\
    def Interval_Sum_Count_Sum(L, R, A, B):\n    \"\"\"L<=x,y<=R \u3092\u6E80\u305F\
    \u30592\u3064\u306E\u6574\u6570x,y\u306E\u3046\u3061, A<=x+y<=B \u3092\u6E80\u305F\
    \u3059\u7D44(x,y) \u306E\u500B\u6570\u3092\u51FA\u529B\u3059\u308B.\n\n    L,R:Int\
    \ (L<=R)\n    A,B:Int (A<=B)\n    \"\"\"\n\n    if L>R or A>B:\n        return\
    \ 0\n\n    A=max(A,2*L)\n    B=min(B,2*R)\n    if B<2*L or 2*R<A:\n        return\
    \ 0\n\n    if A<=L+R<B:\n        return Linear_Sum(1,-2*L+1,A,L+R)+Linear_Sum(-1,2*R+1,L+R+1,B)\n\
    \    else:\n        if B<=L+R:\n            return Linear_Sum(1,-2*L+1,A,B)\n\
    \        else:\n            return Linear_Sum(-1,2*R+1,A,B)\n\ndef Bound_Sum(a,\
    \ b, D, U, L, R):\n    \"\"\" p[k]:=max(D,min(ak+b,U)) \u3068\u3057\u305F\u3068\
    \u304D, Sum_{k=L}^R p[k] \u3092\u6C42\u3081\u308B.\n\n    a,b :int\n    D,U (D<=U)\
    \ : int :\u6291\u3048\u8FBC\u3080\u7BC4\u56F2\n    L,R (L<=R) : int :\u548C\u3092\
    \u53D6\u308B\u7BC4\u56F2\n    \"\"\"\n\n    assert D<=U and L<=R\n\n    if a==0:\n\
    \        return max(D,min(b,U))*(R-L+1)\n\n    if a>0:\n        alpha=(D-b+a-1)//a\n\
    \        beta =(U-b)//a\n\n        if R<alpha:\n            return D*(R-L+1)\n\
    \        elif beta<L:\n            return U*(R-L+1)\n\n        X=0\n        if\
    \ L<alpha:\n            X+=D*(alpha-L)\n            L=alpha\n        if beta<R:\n\
    \            X+=U*(R-beta)\n            R=beta\n    else:\n        a_abs=-a\n\
    \        alpha=(b-U+a_abs-1)//a_abs\n        beta =(b-D)//a_abs\n\n        if\
    \ R<alpha:\n            return U*(R-L+1)\n        elif beta<L:\n            return\
    \ D*(R-L+1)\n\n        X=0\n        if L<alpha:\n            X+=U*(alpha-L)\n\
    \            L=alpha\n        if beta<R:\n            X+=D*(R-beta)\n        \
    \    R=beta\n    X+=Linear_Sum(a,b,L,R)\n    return X\n\ndef Linear_Max_Sum(a,\
    \ b, c, d, L, R):\n    \"\"\" sum_{k=L}^R max(ak+b,ck+d) \u3092\u6C42\u3081\u308B\
    .\n\n    a,b,c,d:int\n    L,R:int (L<=R)\n    \"\"\"\n\n    if L>R:\n        return\
    \ 0\n\n    if a==c:\n        return Linear_Sum(a,max(b,d),L,R)\n    if c>a:\n\
    \        a,b,c,d=c,d,a,b\n\n    if a*L+b>c*L+d:\n        return Linear_Sum(a,b,L,R)\n\
    \n    if a*R+b<c*R+d:\n        return Linear_Sum(c,d,L,R)\n\n    m=(d-b)//(a-c)\n\
    \    return Linear_Sum(c,d,L,m)+Linear_Sum(a,b,m+1,R)\n\ndef Linear_Min_Sum(a,\
    \ b, c, d, L, R):\n    \"\"\" sum_{k=L}^R min(ak+b,ck+d) \u3092\u6C42\u3081\u308B\
    .\n\n    a,b,c,d:int\n    L,R:int (L<=R)\n    \"\"\"\n    return -Linear_Max_Sum(-a,-b,-c,-d,L,R)\n\
    \n#==================================================\n#Sum_Count\u7CFB\ndef Range_Sum_DP(Range,\
    \ S, Mod=None, Mode=0):\n    \"\"\"Range=[(A_0,B_0),...,(A_{N-1}, B_{N-1})] \u3068\
    \u3057\u3068\u305F\u304D,\n    A_i<=X_i<=B_i, X_0+...+X_{n-1}=S \u3092\u6E80\u305F\
    \u3059\u7D44\u306E\u500B\u6570\u3092\u52D5\u7684\u8A08\u753B\u6CD5\u3067\u6C42\
    \u3081\u308B.\n\n    0<=A_i<=B_i\n    0<=S\n    \u8A08\u7B97\u91CF: O(NS)\n  \
    \  \"\"\"\n\n    D=[0]*(S+1); D[0]=1\n    E=[1]*(S+1)\n\n    for a,b in Range:\n\
    \        assert 0<=a<=b\n\n        for i in range(S+1):\n            if i<a:\n\
    \                D[i]=0\n            elif i<=b:\n                D[i]=E[i-a]\n\
    \            else:\n                D[i]=E[i-a]-E[i-b-1]\n\n        E[0]=D[0]\n\
    \        for i in range(1,S+1):\n            E[i]=D[i]+E[i-1]\n\n        if Mod!=None:\n\
    \            E[i]%=Mod\n\n    if Mode:\n        return D\n    else:\n        return\
    \ D[S]\n\ndef Range_Sum_Inclusion(Range, S, Mod=None):\n    \"\"\"Range=[(A_0,B_0),...,(A_{N-1},\
    \ B_{N-1})] \u3068\u3057\u3068\u305F\u304D,\n    A_i<=X_i<=B_i, X_0+...+X_{n-1}=S\
    \ \u3092\u6E80\u305F\u3059\u7D44\u306E\u500B\u6570\u3092\u5305\u9664\u539F\u7406\
    \u3067\u6C42\u3081\u308B.\n\n    0<=A_i<=B_i\n    0<=S\n    \u8A08\u7B97\u91CF\
    : O(N2^N)\n    \"\"\"\n    from itertools import product\n\n    def nCr(n,r):\n\
    \        if n<0: return 0\n        if r<0 or n<r: return 0\n\n        a=b=1\n\
    \        r=min(r,n-r)\n\n        while r:\n            a*=n; b*=r\n\n        \
    \    if Mod!=None:\n                a%=Mod; b%=Mod\n\n            n-=1; r-=1\n\
    \n        if Mod!=None:\n            return (a * pow(b, -1, Mod)) % Mod\n    \
    \    else:\n            return a//b\n\n    def nHr(n,r):\n        if n==r==0:\n\
    \            return 1\n        else:\n            return nCr(n+r-1,n-1)\n\n  \
    \  N=len(Range)\n    X=0\n    for p in product((0,1),repeat=N):\n        T=S\n\
    \        for i in range(N):\n            a,b=Range[i]\n            if p[i]:\n\
    \                T-=b+1\n            else:\n                T-=a\n\n        X+=pow(-1,sum(p))*nHr(N,T)\n\
    \n    if Mod==None:\n        return X\n    else:\n        return X%Mod\n\n#==================================================\n\
    #Find_Sum\u7CFB\ndef Find_Range_Sum(Range, S):\n    \"\"\"Range=[(A_0,B_0),...,(A_{N-1},\
    \ B_{N-1})] \u3068\u3057\u3068\u305F\u304D,\n    A_i<=X_i<=B_i, X_0+...+X_{n-1}=S\
    \ \u3092\u6E80\u305F\u3059\u7D44\u306E\u4F8B\u30921\u3064\u6C42\u3081\u308B.\n\
    \n    A_i<=B_i\n    \"\"\"\n\n    alpha=beta=0\n    for a,b in Range:\n      \
    \  alpha+=a\n        beta +=b\n\n    if not (alpha<=S<=beta): return None\n\n\
    \    N=len(Range)\n    X=[a for a,_ in Range]\n    remain=S-sum(X)\n    for i\
    \ in range(N):\n        y=min(Range[i][1],X[i]+remain)\n        remain-=y-X[i]\n\
    \        X[i]=y\n    return X\n#==================================================\n\
    #\u5E7E\u4F55\u7D1A\u6570\u7CFB\n\ndef Geometric_Sequence_Sum(r, n, Mod=None):\n\
    \    \"\"\" sum_{i=0}^{n-1} r^i [(mod Mod)] \"\"\"\n\n    if Mod==None:\n    \
    \    if r==1: return n\n        else: return (pow(r,n)-1)/(r-1)\n    else:\n \
    \       if r==1: return n%Mod\n        else: return (pow(r,n,(r-1)*Mod)//(r-1))%Mod\n"
  dependsOn: []
  isVerificationFile: false
  path: Summation/Math.py
  requiredBy: []
  timestamp: '2023-08-06 21:11:53+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Summation/Math.py
layout: document
redirect_from:
- /library/Summation/Math.py
- /library/Summation/Math.py.html
title: Summation/Math.py
---
