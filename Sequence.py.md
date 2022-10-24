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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.8/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.8/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def Fibonacci(N,M=None):\n    \"\"\"\u30D5\u30A3\u30DC\u30CA\u30C3\u30C1\u6570\
    \u5217\u306E\u7B2CN\u9805\u3092\u6C42\u3081\u308B.\n\n    N:\u4F55\u9805\u76EE\
    ?\n    M:\u5270\u4F59\n    \"\"\"\n\n    if N==0:\n        return 0\n\n    a,b=0,1\n\
    \    I=1\n    if M==None:\n        while I<N:\n            a,b=b,a+b\n       \
    \     I+=1\n    else:\n        while I<N:\n            a,b=b,(a+b)%M\n       \
    \     I+=1\n    return b\n\ndef Lucas(N,M=None):\n    \"\"\"\u30D5\u30A3\u30DC\
    \u30CA\u30C3\u30C1\u6570\u5217\u306E\u7B2CN\u9805\u3092\u6C42\u3081\u308B.\n\n\
    \    N:\u4F55\u9805\u76EE?\n    M:\u5270\u4F59\n    \"\"\"\n\n    if N==0:\n \
    \       return 0\n\n    a,b=2,1\n    I=1\n    if M==None:\n        while I<N:\n\
    \            a,b=b,a+b\n            I+=1\n    else:\n        while I<N:\n    \
    \        a,b=b,(a+b)%M\n            I+=1\n    return b\n\ndef Cumulative(N,T):\n\
    \    \"\"\"\u6F38\u5316\u5F0FT_n=T_{n-1}+...+T_{n-k}\u3067\u5B9A\u3081\u3089\u308C\
    \u305F\u6570\u5217(T_n)\u306E\u7B2CN\u9805\u3092\u6C42\u3081\u308B.\n\n    N(Int):\u7B2C\
    N\u9805\n    T(List):[T_0,...,T_{k-1}]\u6700\u521D\u306Ek\u9805\n    \"\"\"\n\
    \    K=len(T)\n    if N<K:\n        return T[N]\n\n    T=list(T)\n    I=K-1\n\
    \    while I<N:\n        U=sum(T)\n        T=T[1:]+[U]\n        I+=1\n    return\
    \ T[-1]\n\ndef Derangement_List(N,Mod=None):\n    \"\"\"k=0,1,...,N\u306B\u95A2\
    \u3057\u3066,k\u8981\u7D20\u64B9\u4E71\u9806\u5217\u306E\u500B\u6570\u3092\u6C42\
    \u3081\u308B.\n    \"\"\"\n    if N<0:\n        return []\n    elif N==0:\n  \
    \      return [0]\n    elif N==1:\n        return [0,0]\n    elif Mod==1:\n  \
    \      return [0]*(N+1)\n\n    R=[0]*(N+1)\n    R[2]=1\n    a,b,c=0,0,1\n\n  \
    \  for k in range(3,N+1):\n        a,b,c=b,c,(k-1)*(b+c)\n\n        if Mod!=None:\n\
    \            c%=Mod\n        R[k]=c\n\n    return R\n\ndef Longest_Increase_Subsequence(A,Mode=False,equal=False):\n\
    \    \"\"\" \u5217 L \u306B\u304A\u3051\u308B LIS \u306E\u9577\u3055\u3092\u6C42\
    \u3081\u308B.\n\n    Mode=False \u306E\u3068\u304D ... LIS \u306E\u9577\u3055\
    , True \u306E\u3068\u304D ... (\u9577\u3055, \u4E00\u4F8B, \u4E00\u4F8B\u306E\u5404\
    \u8981\u7D20\u306E\u5834\u6240)\n    equal: False \u306E\u3068\u304D ... \u72ED\
    \u7FA9\u5358\u8ABF\u5897\u52A0, True \u306E\u3068\u304D... \u5E83\u7FA9\u5358\u8ABF\
    \u5897\u52A0\n    \"\"\"\n\n    if equal:\n        from bisect import bisect_right\
    \ as bis\n    else:\n        from bisect import bisect_left as bis\n\n    if Mode:\n\
    \        L=[]\n        Ind=[0]*len(A)\n        for i in range(len(A)):\n     \
    \       a=A[i]\n            k=bis(L,a)\n            if k==len(L):\n          \
    \      L.append(a)\n            else:\n                L[k]=a\n            Ind[i]=k\n\
    \n        X=[]\n        I=[]\n        j=len(L)-1\n        for i in range(len(A)-1,-1,-1):\n\
    \            if Ind[i]==j:\n                j-=1\n                X.append(A[i])\n\
    \                I.append(i)\n\n        return len(L), X[::-1], I[::-1]\n    else:\n\
    \        L=[]\n        for a in A:\n            k=bis(L,a)\n            if k==len(L):\n\
    \                L.append(a)\n            else:\n                L[k]=a\n    \
    \    return len(L)\n"
  dependsOn: []
  isVerificationFile: false
  path: Sequence.py
  requiredBy: []
  timestamp: '2021-12-19 16:19:58+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Sequence.py
layout: document
redirect_from:
- /library/Sequence.py
- /library/Sequence.py.html
title: Sequence.py
---
