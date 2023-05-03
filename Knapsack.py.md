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
    - https://tjkendev.github.io/procon-library/python/dp/knapsack-meet-in-the-middle.html
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.3/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.3/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def Knapsack_01_Weight(List,Weight,Mode=False):\n    \"\"\"\u91CD\u3055\u304C\
    \u975E\u5E38\u306B\u8EFD\u304401-Knapsack Problem\u3092\u89E3\u304F.\n\n    List:\u5404\
    \u8981\u7D20\u306F\u30BF\u30D7\u30EB(v,w) \u306E\u5F62\u3067, v\u306F\u4FA1\u5024\
    , w\u306F\u91CD\u3055\n    Mode:Mode=True\u306E\u3068\u304D, \u6700\u5927\u5024\
    \u3068\u305D\u308C\u3092\u9054\u6210\u3059\u308B\u4F8B\u3092\u8FD4\u3059.\n  \
    \  [\u8A08\u7B97\u91CF]\n    O(NW)\n    \"\"\"\n\n    if Mode:\n        X=[[0]*(Weight+1)\
    \ for _ in range(len(List)+1)]\n        for i,(v,w) in enumerate(List,0):\n  \
    \          E=X[i]\n            F=X[i+1]\n\n            for s in range(Weight,w-1,-1):\n\
    \                F[s]=max(E[s],E[s-w]+v)\n        alpha=max(X[-1])\n        W=X[-1].index(alpha)\n\
    \n        L=[]\n        for i in range(len(List)-1,-1,-1):\n            if X[i+1][W]>X[i][W]:\n\
    \                v,w=List[i]\n                L.append((i,List[i]))\n        \
    \        W-=w\n        return alpha,L[::-1]\n    else:\n        X=[0]*(Weight+1)\n\
    \        for v,w in List:\n            for s in range(Weight,w-1,-1):\n      \
    \          X[s]=max(X[s],X[s-w]+v)\n        return max(X)\n\ndef Knapsack_01_Value(List,Weight,Mode=False):\n\
    \    \"\"\"\u4FA1\u5024\u304C\u975E\u5E38\u306B\u5C0F\u3055\u304401-Knapsack Problem\u3092\
    \u89E3\u304F.\n\n    List:\u5404\u8981\u7D20\u306F\u30BF\u30D7\u30EB(v,w) \u306E\
    \u5F62\u3067, v\u306F\u4FA1\u5024, w\u306F\u91CD\u3055\n    Mode:Mode=True\u306E\
    \u3068\u304D, \u6700\u5927\u5024\u3068\u305D\u308C\u3092\u9054\u6210\u3059\u308B\
    \u4F8B\u3092\u8FD4\u3059.\n    [\u8A08\u7B97\u91CF]\n    O(N sum(v))\n    \"\"\
    \"\n\n    inf=float(\"inf\")\n    v_sum=0\n    for v,_ in List:\n        v_sum+=v\n\
    \n    if Mode:\n        X=[[inf]*(v_sum+1) for _ in range(len(List)+1)]\n    \
    \    X[0][0]=0\n\n        for i,(v,w) in enumerate(List,0):\n            E=X[i]\n\
    \            F=X[i+1]\n\n            for s in range(v_sum,v-1,-1):\n         \
    \       F[s]=min(E[s],E[s-v]+w)\n            for s in range(v-1,-1,-1):\n    \
    \            F[s]=E[s]\n\n        E=X[-1]\n        Y=[v for v in range(v_sum+1)\
    \ if E[v]<=Weight]\n        V=alpha=max(Y)\n\n        L=[]\n        for i in range(len(List)-1,-1,-1):\n\
    \            if X[i+1][V]<X[i][V]:\n                v,w=List[i]\n            \
    \    L.append((i,List[i]))\n                V-=v\n        return alpha,L[::-1]\n\
    \    else:\n        X=[inf]*(v_sum+1)\n        X[0]=0\n\n        for v,w in List:\n\
    \            for s in range(v_sum,v-1,-1):\n                X[s]=min(X[s],X[s-v]+w)\n\
    \        Y=[v for v in range(v_sum+1) if X[v]<=Weight]\n        return max(Y)\n\
    \ndef Knapsack_01_Middle(List,Weight,Mode=False):\n    \"\"\"\u500B\u6570\u304C\
    \u975E\u5E38\u306B\u5C11\u306A\u304401-Knapsack Problem\u3092 (\u534A\u5206\u5168\
    \u5217\u6319\u3067) \u89E3\u304F.\n\n    List:\u5404\u8981\u7D20\u306F\u30BF\u30D7\
    \u30EB(v,w) \u306E\u5F62\u3067, v\u306F\u4FA1\u5024, w\u306F\u91CD\u3055\n   \
    \ [\u8A08\u7B97\u91CF]\n    O(N 2^(N/2))\n\n    [\u53C2\u8003\u5143]\n    https://tjkendev.github.io/procon-library/python/dp/knapsack-meet-in-the-middle.html\n\
    \    \"\"\"\n\n    def subset_sum(S):\n        T={0:0}\n        for v,w in S:\n\
    \            T1=dict(T)\n            for key,val in T.items():\n             \
    \   a=key+w\n                if a>Weight:\n                    continue\n    \
    \            if a in T1:\n                    T1[a]=max(T1[a],val + v)\n     \
    \           else:\n                    T1[a]=val+v\n            T=T1\n\n     \
    \   v=-1\n        R=[]\n        for w in sorted(T):\n            if T[w]>v:\n\
    \                v=T[w]\n                R.append((v,w))\n        return R\n\n\
    \    def merge(S,T):\n        T=T[::-1]\n        it=iter(T)\n        v1,w1=next(it)\n\
    \n        t=0\n\n        for v,w in S:\n            while w+w1>Weight:\n     \
    \           v1,w1=next(it)\n\n            if t<v+v1:\n                t=v+v1\n\
    \        return t\n\n    N=len(List)\n    A=subset_sum(List[:N//2])\n    B=subset_sum(List[N//2:])\n\
    \    return merge(A,B)\n"
  dependsOn: []
  isVerificationFile: false
  path: Knapsack.py
  requiredBy: []
  timestamp: '2021-05-23 18:03:35+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Knapsack.py
layout: document
redirect_from:
- /library/Knapsack.py
- /library/Knapsack.py.html
title: Knapsack.py
---
