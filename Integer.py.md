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
    - https://judge.yosupo.jp/submission/31819
    - https://judge.yosupo.jp/submission/6131
    - https://qiita.com/convexineq/items/e3d599cb9f91a73f936d
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "#\u7D20\u56E0\u6570\u5206\u89E3\ndef Prime_Factorization(N):\n    if N==0:\n\
    \        return [[0,1]]\n\n    if N<0:\n        R=[[-1,1]]\n    else:\n      \
    \  R=[]\n\n    N=abs(N)\n\n    if N&1==0:\n        R.append([2,0])\n        while\
    \ N&1==0:\n            N>>=1\n            R[-1][1]+=1\n\n    if N%3==0:\n    \
    \    R.append([3,0])\n        while N%3==0:\n            N//=3\n            R[-1][1]+=1\n\
    \n    p=5\n    flag=0\n    while p*p<=N:\n        if N%p==0:\n            R.append([p,0])\n\
    \            while N%p==0:\n                N//=p\n                R[-1][1]+=1\n\
    \n        p+=2+2*flag\n        flag^=1\n\n    if N!=1:\n        R.append([N,1])\n\
    \n    return R\n\n#\u6839\u57FA\ndef Radical(N):\n    \"\"\" N \u304C\u7D20\u56E0\
    \u6570\u5206\u89E3 N=p^a*q^b*r^c ... \u3068\u306A\u308B\u3068\u304D, pqr... \u3092\
    \u8FD4\u3059.\n\n    N: \u975E\u8CA0\u6574\u6570\n    \"\"\"\n\n    assert N>=0,\"\
    N\u306F\u975E\u8CA0\u6574\u6570\u3067\u306F\u306A\u3044.\"\n    a=1\n\n    if\
    \ N&1==0:\n        a*=2\n        while N&1==0:\n            N>>=1\n\n    if N%3==0:\n\
    \        a*=3\n        while N%3==0:\n            N//=3\n\n    k=5\n    Flag=0\n\
    \    while k*k<=N:\n        if N%k==0:\n            a*=k\n            while N%k==0:\n\
    \                N//=k\n        k+=2+2*Flag\n        Flag^=1\n\n    if N>1:\n\
    \        a*=N\n    return a\n\n#\u7D20\u56E0\u6570\u306E\u7A2E\u985E\ndef Prime_Factor_List(N):\n\
    \    \"\"\"N\u304C\u7D20\u56E0\u6570\u5206\u89E3 N=p^a*q^b*r^c ...\u3068\u306A\
    \u308B\u3068\u304D,\u30EA\u30B9\u30C8[p,q,r,...]\u3092\u8FD4\u3059.\n    \"\"\"\
    \n    N=abs(N)\n    X=[]\n    if N%2==0:\n        X.append(2)\n        while N&1==0:\n\
    \            N>>=1\n\n    if N%3==0:\n        X.append(3)\n        while N%3==0:\n\
    \            N//=3\n\n    p=5\n    Flag=1\n    while p*p<=N:\n        if N%p==0:\n\
    \            X.append(p)\n            while N%p==0:\n                N//=p\n \
    \       p+=2 if Flag else 4\n        Flag^=1\n\n    if N!=1:\n        X.append(N)\n\
    \    return X\n\n#\u7D04\u6570\u5168\u90E8\ndef Divisors(N):\n    N=abs(N)\n \
    \   L,U=[],[]\n    k=1\n    while k*k <=N:\n        if N%k== 0:\n            L.append(k)\n\
    \            if k*k!=N:\n                U.append(N//k)\n        k+=1\n    return\
    \ L+U[::-1]\n\n#\u7D20\u56E0\u6570\u5206\u89E3\u306E\u7D50\u679C\u304B\u3089,\
    \ \u7D04\u6570\u3092\u5168\u3066\u6C42\u3081\u308B.\ndef Divisors_from_Prime_Factor(P,\
    \ sorting=False):\n    X=[1]\n    for p,e in P:\n        q=1\n        n=len(X)\n\
    \        for _ in range(e):\n            q*=p\n            for j in range(n):\n\
    \                X.append(X[j]*q)\n\n    if sorting:\n        X.sort()\n\n   \
    \ return X\n\n#\u9AD8\u5EA6\u5408\u6210\u6570\n#\u53C2\u8003\u5143:https://qiita.com/convexineq/items/e3d599cb9f91a73f936d\n\
    def Highly_Composite_Number(N):\n    \"\"\" N \u4EE5\u4E0B\u306E\u9AD8\u5EA6\u5408\
    \u6210\u6570\u3092\u6C42\u3081\u308B.\n    \"\"\"\n\n    from heapq import heappop,heappush\n\
    \    from math import log\n    prime = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263]\n\
    \    lim = [[2*int(log(p,q)) for q in prime] for p in prime] #\u679D\u5208\u308A\
    \u7528\u914D\u5217\n    # \u521D\u671F\u72B6\u614B\n    q = [(2,2,[1])] # (n,n\u306E\
    \u7D04\u6570\u306E\u500B\u6570\u3001n\u306E\u6307\u6570\u8868\u8A18)\u3092\u4FDD\
    \u5B58\u3059\u308B heapq\n    res = [(1,1,[])]\n\n    while q and q[0][0] <= N:\n\
    \        n,val,lst = heappop(q)\n        if val > res[-1][1]: #\u6761\u4EF6\u3092\
    \u307F\u305F\u3059\u306A\u3089\u7B54\u306B\u8FFD\u52A0\n            res.append((n,val,lst[:]))\n\
    \        L = len(lst)\n        e0 = lst[0]\n        #\u5168\u90E81\u306A\u3089\
    \u65B0\u3057\u3044\u7D20\u6570\u3067\u6A2A\u306B\u4F38\u3070\u305B\u308B\n   \
    \     if e0 == 1:\n            heappush(q,(n*prime[L],val*2,[1]*(L+1)))\n    \
    \    #\u6700\u4E0A\u6BB5\u306E\u4E0A\u3092\u6A2A\u65B9\u5411\u306B\u7A4D\u3080\
    \n        for i in range(L):\n            if e0 > lst[i]: break #\u6BB5\u5DEE\u304C\
    \u3042\u308B\u3068\u3001\u3082\u3046\u4F38\u3070\u305B\u306A\u3044\n         \
    \   if e0 >= lim[L][i]: break #\u679D\u5208\u308A\uFF08\u91CD\u8981\uFF09\n  \
    \          n *= prime[i]\n            if n <= N:\n                lst[i] += 1\n\
    \                val = val//(e0+1)*(e0+2)\n                heappush(q,(n,val,lst[:]))\n\
    \    return res\n\n#\u7D20\u6570\u5224\u5B9A\ndef Is_Prime(N):\n    N=abs(N)\n\
    \    if N<=1:\n        return False\n\n    if (N==2) or (N==3) or (N==5):\n  \
    \      return True\n\n    r=N%6\n    if not(r==1 or r==5):\n        return False\n\
    \n    p=5\n    flag=0\n    while p*p<=N:\n        if N%p==0:\n            return\
    \ False\n\n        p+=2+2*flag\n        flag^=1\n    return True\n\n#\u7D20\u6570\
    \u5224\u5B9A for long long\ndef Is_Prime_for_long_long(N):\n    if N<=1: return\
    \ False\n    if N==2 or N==7 or N==61: return True\n    if N%2==0: return False\n\
    \n    d=N-1\n    while d%2==0: d//=2\n\n    for a in (2,7,61):\n        t=d\n\
    \        y=pow(a,t,N)\n        while t!=N-1 and y!=1 and y!=N-1:\n           \
    \ y=(y*y)%N\n            t<<=1\n        if y!=N-1 and t%2==0:\n            return\
    \ False\n    return True\n\n#Miller-Rabin\u306E\u7D20\u6570\u5224\u5B9A\u6CD5\n\
    def Miller_Rabin_Primality_Test(N, Times=20):\n    \"\"\" Miller-Rabin \u306B\u3088\
    \u308B\u6574\u6570 N \u306E\u7D20\u6570\u5224\u5B9A\u3092\u884C\u3046.\n\n   \
    \ N: \u6574\u6570\n    \u203B True \u306F\u6B63\u78BA\u306B\u306F Probably True\
    \ \u3067\u3042\u308B ( False \u306F \u78BA\u5B9A False ).\n    \"\"\"\n    from\
    \ random import randint as ri\n\n    if N==2: return True\n\n    if N==1 or N%2==0:\
    \ return False\n\n    q=N-1\n    k=0\n    while q&1==0:\n        k+=1\n      \
    \  q>>=1\n\n    for _ in range(Times):\n        m=ri(2,N-1)\n        y=pow(m,q,N)\n\
    \        if y==1:\n            continue\n\n        flag=True\n        for i in\
    \ range(k):\n            if (y+1)%N==0:\n                flag=False\n        \
    \        break\n\n            y*=y\n            y%=N\n\n        if flag:\n   \
    \         return False\n    return True\n\n#\u30DD\u30E9\u30FC\u30C9\u30FB\u30ED\
    \u30FC\u30A2\u30EB\u30B4\u30EA\u30BA\u30E0\u306B\u3088\u3063\u3066\u7D20\u56E0\
    \u6570\u3092\u767A\u898B\u3059\u308B\n#\u53C2\u8003\u5143:https://judge.yosupo.jp/submission/6131\n\
    def Find_Factor_Rho(N):\n    if N==1:\n        return 1\n    from math import\
    \ gcd\n    m=1<<(N.bit_length()//8+1)\n\n    for c in range(1,99):\n        f=lambda\
    \ x:(x*x+c)%N\n        y,r,q,g=2,1,1,1\n        while g==1:\n            x=y\n\
    \            for i in range(r):\n                y=f(y)\n            k=0\n   \
    \         while k<r and g==1:\n                for i in range(min(m, r - k)):\n\
    \                    y=f(y)\n                    q=q*abs(x - y)%N\n          \
    \      g=gcd(q,N)\n                k+=m\n            r <<=1\n\n        if g<N:\n\
    \            if Miller_Rabin_Primality_Test(g):\n                return g\n  \
    \          elif Miller_Rabin_Primality_Test(N//g):\n                return N//g\n\
    \    return N\n\n#\u30DD\u30E9\u30FC\u30C9\u30FB\u30ED\u30FC\u30A2\u30EB\u30B4\
    \u30EA\u30BA\u30E0\u306B\u3088\u308B\u7D20\u56E0\u6570\u5206\u89E3\n#\u53C2\u8003\
    \u5143:https://judge.yosupo.jp/submission/6131\ndef Pollard_Rho_Prime_Factorization(N):\n\
    \    I=2\n    res=[]\n    while I*I<=N:\n        if N%I==0:\n            k=0\n\
    \            while N%I==0:\n                k+=1\n                N//=I\n    \
    \        res.append([I,k])\n\n        I+=1+(I%2)\n\n        if I!=101 or N<2**20:\n\
    \            continue\n\n        while N>1:\n            if Miller_Rabin_Primality_Test(N):\n\
    \                res.append([N,1])\n                N=1\n            else:\n \
    \               j=Find_Factor_Rho(N)\n                k=0\n                while\
    \ N%j==0:\n                    N//=j\n                    k+=1\n             \
    \   res.append([j,k])\n    if N>1:\n        res.append([N,1])\n    res.sort(key=lambda\
    \ x:x[0])\n    return res\n\n#\u6B21\u306E\u7D20\u6570\ndef Next_Prime(N,K=1):\n\
    \    \"\"\"\n    N \u3092\u4E0A\u56DE\u308B\u81EA\u7136\u6570\u306E\u3046\u3061\
    , K \u756A\u76EE\u306B\u5C0F\u3055\u3044\u7D20\u6570\n\n    N: \u81EA\u7136\u6570\
    \n    \"\"\"\n    if K>0:\n        while K>0:\n            N+=1\n            if\
    \ Is_Prime(N):\n                K-=1\n    else:\n        while K<0:\n        \
    \    N-=1\n            if Is_Prime(N):\n                K+=1\n    return N\n\n\
    #\u30A8\u30E9\u30C8\u30B9\u30C6\u30CD\u30B9\u306E\u7BE9\ndef Sieve_of_Eratosthenes(N):\n\
    \    \"\"\" N \u307E\u3067\u306E\u30A8\u30E9\u30C8\u30B9\u30C6\u30CD\u30B9\u306E\
    \u7BE9\u3092\u5B9F\u884C\n\n    [Input]\n    N:\u81EA\u7136\u6570\n\n    [Output]\n\
    \    \u7D20\u6570\u304B\u3069\u3046\u304B\u306E\u30EA\u30B9\u30C8 ([0,0,1,1,0,1,...])\n\
    \    \"\"\"\n\n    if N==0:\n        return [0]\n\n    T=[1]*(N+1)\n    T[0]=T[1]=0\n\
    \n    for x in range(4,N+1,2):\n        T[x]=0\n\n    for x in range(9,N+1,3):\n\
    \        T[x]=0\n\n    a=5\n    Flag=0\n    while a*a<=N:\n        if T[a]:\n\
    \            b=a*a\n            c=2*a\n            while b<=N:\n             \
    \   T[b]=0\n                b+=c\n        a+=2+2*Flag\n        Flag^=1\n    return\
    \ T\n\ndef Prime_List(N):\n    \"\"\" N \u4EE5\u4E0B\u306E\u7D20\u6570\u3092\u5217\
    \u6319\n\n    [Input]\n    N: \u81EA\u7136\u6570\n\n    [Output]\n    N \u4EE5\
    \u4E0B\u306E\u7D20\u6570\u3092\u6607\u9806\u306B\u4E26\u3079\u305F\u30EA\u30B9\
    \u30C8 [2,3,5,...]\n    \"\"\"\n\n    if N==0 or N==1:\n        return []\n  \
    \  elif N==2:\n        return [2]\n\n    if N%2==0:\n        N-=1\n\n    M=(N+1)//2\n\
    \n    prime=[1]*M # prime[k]:=2k+1 \u306F\u7D20\u6570?\n\n    for x in range(4,M,3):\n\
    \        prime[x]=0\n\n    a=5\n    Flag=0\n    while a*a<=N:\n        if prime[(a-1)>>1]:\n\
    \            ii=(a*a-1)>>1\n            for j in range(ii,M,a):\n            \
    \    prime[j]=0\n        a+=2+2*Flag\n        Flag^=1\n\n    X=[(k<<1)|1 for k\
    \ in range(M) if prime[k]]\n    X[0]=2\n\n    return X\n\ndef Interval_Sieve_of_Eratosthenes(L,R):\n\
    \    \"\"\" L \u4EE5\u4E0A R \u4EE5\u4E0B\u306E\u30A8\u30E9\u30C8\u30B9\u30C6\u30CD\
    \u30B9\u306E\u7BE9\u3092\u5B9F\u884C\n\n    [Input]\n    N:\u81EA\u7136\u6570\n\
    \n    [Output]\n    \u7D20\u6570\u304B\u3069\u3046\u304B\u306E\u30EA\u30B9\u30C8\
    \ X: X[k]:=k+L \u304C\u7D20\u6570\u306A\u3089 1, \u7D20\u6570\u3067\u306A\u3044\
    \u306A\u3089\u3070 0\n    \"\"\"\n\n    M=1\n    while True:\n        if (M+1)*(M+1)>R:\n\
    \            break\n        M+=1\n\n    X=[1]*(R-L+1)\n\n    if L<=0<=R:\n   \
    \     X[0-L]=0\n    if L<=1<=R:\n        X[1-L]=0\n\n    for p in Prime_List(M):\n\
    \        for x in range(max((L+p-1)//p*p,p*p),R+1,p):\n            X[x-L]=0\n\
    \    return X\n\ndef Smallest_Prime_Factor(N):\n    \"\"\" 0,1,2,...,N \u306E\u6700\
    \u5C0F\u306E\u7D20\u56E0\u6570\u306E\u30EA\u30B9\u30C8 (0,1 \u306B\u3064\u3044\
    \u3066\u306F 1 \u306B\u3057\u3066\u3044\u308B)\n    \"\"\"\n\n    if N<=1:\n \
    \       return [1]*(N+1)\n\n    T=[0]*(N+1); T[0]=T[1]=1\n\n    for i in range(2,\
    \ N+1, 2):\n        T[i]=2\n\n    for i in range(3, N+1, 6):\n        T[i]=3\n\
    \n    prime=[2,3]\n    i=5; d=2\n    while i<=N:\n        if T[i]==0:\n      \
    \      T[i]=i\n            prime.append(i)\n\n        for p in prime:\n      \
    \      if i*p<=N:\n                T[i*p]=p\n            else:\n             \
    \   break\n            if p==T[i]:\n                break\n        i+=d; d=6-d\n\
    \    return T\n\ndef Faster_Prime_Factorization(N,L):\n    \"\"\" Smallest_Prime_Factors(N)\u3067\
    \u6C42\u3081\u305F\u30EA\u30B9\u30C8\u3092\u5229\u7528\u3057\u3066, N \u3092\u9AD8\
    \u901F\u7D20\u56E0\u6570\u5206\u89E3\u3059\u308B.\n\n    L: Smallest_Prime_Factors(N)\u3067\
    \u6C42\u3081\u305F\u30EA\u30B9\u30C8\n    \"\"\"\n    if N==0:\n        return\
    \ [[0,1]]\n    elif N>0:\n        D=[]\n    else:\n        D=[[-1,1]]\n      \
    \  N=abs(N)\n\n    while N>1:\n        a=L[N]\n        k=0\n        while L[N]==a:\n\
    \            k+=1\n            N//=a\n        D.append([a,k])\n    return D\n\n\
    def Interval_Prime_Factorization(L,R):\n    \"\"\" x=L,L+1,...,R \u306B\u5BFE\u3057\
    \u3066\u7D20\u56E0\u6570\u5206\u89E3\u3092\u884C\u3046.\n\n    \"\"\"\n\n    assert\
    \ 0<=L<=R\n\n    M=1\n    while True:\n        if (M+1)*(M+1)>R:\n           \
    \ break\n        M+=1\n\n    if L==0:\n        flag=1\n        L=1\n    else:\n\
    \        flag=0\n\n    A=list(range(L,R+1))\n    X=[[] for _ in range(R-L+1)]\n\
    \n    for p in Prime_List(M):\n        for x in range((L+p-1)//p*p,R+1,p):\n \
    \           k=0\n            while A[x-L]%p==0:\n                A[x-L]//=p\n\
    \                k+=1\n            X[x-L].append((p,k))\n\n    for x in range(L,R+1):\n\
    \        if A[x-L]!=1:\n            X[x-L].append((A[x-L],1))\n\n    if flag:\n\
    \        return [(0,1)]+X\n    else:\n        return  X\n\n#\u7D20\u6570\u306E\
    \u500B\u6570\n#Thanks for pyranine\n#URL: https://judge.yosupo.jp/submission/31819\n\
    def Prime_Pi(N):\n    \"\"\" N \u4EE5\u4E0B\u306E\u7D20\u6570\u306E\u500B\u6570\
    \n\n    N: int\n    \"\"\"\n\n    if N<2: return 0\n    v = int(N ** 0.5) + 1\n\
    \    smalls = [i // 2 for i in range(1, v + 1)]\n    smalls[1] = 0\n    s = v\
    \ // 2\n    roughs = [2 * i + 1 for i in range(s)]\n    larges = [(N // roughs[i]\
    \ + 1) // 2 for i in range(s)]\n    skip = [False] * v\n\n    pc = 0\n    for\
    \ p in range(3, v):\n        if smalls[p] <= smalls[p - 1]:\n            continue\n\
    \n        q = p * p\n        pc += 1\n        if q * q > N:\n            break\n\
    \        skip[p] = True\n        for i in range(q, v, 2 * p):\n            skip[i]\
    \ = True\n\n        ns = 0\n        for k in range(s):\n            i = roughs[k]\n\
    \            if skip[i]:\n                continue\n            d = i * p\n  \
    \          larges[ns] = larges[k] - (larges[smalls[d] - pc] if d < v else smalls[N\
    \ // d]) + pc\n            roughs[ns] = i\n            ns += 1\n        s = ns\n\
    \        for j in range((v - 1) // p, p - 1, -1):\n            c = smalls[j] -\
    \ pc\n            e = min((j + 1) * p, v)\n            for i in range(j * p, e):\n\
    \                smalls[i] -= c\n\n    for k in range(1, s):\n        m = N //\
    \ roughs[k]\n        s = larges[k] - (pc + k - 1)\n        for l in range(1, k):\n\
    \            p = roughs[l]\n            if p * p > m:\n                break\n\
    \            s -= smalls[m // p] - (pc + l - 1)\n        larges[0] -= s\n\n  \
    \  return larges[0]\n\n#K\u4E57\u30EA\u30B9\u30C8\ndef Power_List(N,K,Mod):\n\
    \    \"\"\" i=0,1,...,N \u306B\u304A\u3051\u308B i^K (mod Mod) \u306E\u30EA\u30B9\
    \u30C8\u3092\u6C42\u3081\u308B.\n    [\u8A08\u7B97\u91CF] O(N log log N+pi(N)\
    \ log K)\n    N,K,Mod: int\n    \"\"\"\n\n    if N==0:\n        return [0]\n\n\
    \    S=Smallest_Prime_Factor(N)\n    A=[0]*(N+1); A[1]=pow(1,K,Mod)\n\n    for\
    \ i in range(2,N+1):\n        if S[i]<i:\n            A[i]=A[S[i]]*A[i//S[i]]%Mod\n\
    \        else:\n            A[i]=pow(i,K,Mod)\n    return A\n\n#\u5E73\u65B9\u6570\
    ?\ndef Is_Square_Number(N):\n    if N<0:\n        return False\n    elif N==0:\n\
    \        return True\n\n    for p in [2,3]:\n        F=0\n        while N%p==0:\n\
    \            F^=1\n            N//=p\n        if F:\n            return False\n\
    \n    k=5\n    Flag=1\n    while k*k<=N:\n        F=0\n        while N%k==0:\n\
    \            F^=1\n            N//=k\n        if F:\n            return False\n\
    \        k+=2 if Flag else 4\n    return N==1\n\n#\u7ACB\u65B9\u6570?\ndef Is_Cubic_Number(N):\n\
    \    if N<0:\n        return False\n    elif N==0:\n        return True\n\n  \
    \  for p in [2,3]:\n        F=0\n        while N%p==0:\n            F+=1\n   \
    \         N//=p\n        if F%3:\n            return False\n\n    k=5\n    Flag=1\n\
    \    while k*k<=N:\n        F=0\n        while N%k==0:\n            F+=1\n   \
    \         N//=k\n        if F%3:\n            return False\n        k+=2 if Flag\
    \ else 4\n    return N==1\n\n#Euler's Totient\u95A2\u6570\ndef Euler_Totient(N):\n\
    \    \"\"\" 1 \u4EE5\u4E0A N \u4EE5\u4E0B\u306E\u6574\u6570\u306E\u3046\u3061\
    , N \u3068\u4E92\u3044\u306B\u7D20\u306A\u6574\u6570\u306E\u500B\u6570 phi (N)\
    \ \u3092\u6C42\u3081\u308B.\n\n    Args:\n        N (int): \u6B63\u306E\u6574\u6570\
    \n\n    Returns:\n        int: varphi (N)\n    \"\"\"\n\n    assert N>=0,\"N\u304C\
    \u975E\u8CA0\u6574\u6570\u3067\u306F\u306A\u3044.\"\n\n    e=(N&(-N)).bit_length()-1\n\
    \    if e>0:\n        phi=1<<(e-1)\n        N>>=e\n    else:\n        phi=1\n\n\
    \    e=0\n    while N%3==0:\n        e+=1\n        N//=3\n\n    if e>0:\n    \
    \    phi*=pow(3,e-1)*2\n\n    flag=0\n    p=5\n    while p*p<=N:\n        if N%p==0:\n\
    \            e=0\n            while N%p==0:\n                e+=1\n          \
    \      N//=p\n\n            phi*=pow(p,e-1)*(p-1)\n\n        p+=2\n        flag^=1\n\
    \n    if N>1:\n        phi*=N-1\n\n    return phi\n\n#Euler's Totient\u95A2\u6570\
    \ndef Euler_Totient_List(N):\n    \"\"\"k=0,1,...,N \u306B\u5BFE\u3057\u3066,\
    \ 1\u4EE5\u4E0Ak\u4EE5\u4E0B\u306E\u6574\u6570\u306E\u3046\u3061, k\u3068\u4E92\
    \u3044\u306B\u7D20\u306A\u6574\u6570\u306E\u500B\u6570 \u03C6(k) \u3092\u6C42\u3081\
    \u308B.\n\n    N:\u6B63\u306E\u6574\u6570\n    \"\"\"\n\n    assert N>=0,\"N\u304C\
    \u975E\u8CA0\u6574\u6570\u3067\u306F\u306A\u3044.\"\n\n    phi=list(range(N+1))\n\
    \    for p in range(2,N+1):\n        if phi[p]==p:\n            for j in range(p,N+1,p):\n\
    \                phi[j]=phi[j]//p*(p-1)\n    return phi\n\n#\u7D04\u6570\u306E\
    K\u4E57\u548C\ndef Divisor_Sigma(N,K=1):\n    if N==1:\n        return 1\n\n \
    \   H=Prime_Factorization(N)\n\n    R=1\n    p=2\n    while p*p<=N:\n        if\
    \ N%p==0:\n            e=0\n            while N%p==0:\n                N//=p\n\
    \                e+=1\n\n            if K:\n                s=pow(p,K)\n     \
    \           R*=(pow(s,e+1)-1)//(s-1)\n            else:\n                R*=e+1\n\
    \        p+=1\n\n    if N>1:\n        R*=pow(N,K)+1\n\n    return R\n\n#\u5B8C\
    \u5168\u6570?\ndef Is_Perfect(N):\n    return 2*N==Divisor_Sigma(N,1)\n\n#\u5546\
    \u5217\u6319\ndef Quotient_Range(N):\n    \"\"\"N\u3067\u5272\u3063\u305F\u5546\
    \u306E\u53EF\u80FD\u6027\u3092\u5168\u3066\u5217\u6319\u3059\u308B.\n\n    [Input]\n\
    \    N:\u6B63\u6574\u6570\n\n    [Output]\n    X:\u30EA\u30B9\u30C8\n    X\u306E\
    \u5404\u8981\u7D20(k,x,y) \u306F x<=i<=y \u3067\u3042\u308B\u3053\u3068\u3068\
    , floor(N/i)=k \u304C\u540C\u5024\u3067\u3042\u308B\u3053\u3068\u3092\u8868\u3059\
    .\n    \"\"\"\n    X=[]\n\n    M=1\n    while M*M<=N:\n        X.append((N//M,M,M))\n\
    \        M+=1\n\n    for i in range(M,0,-1):\n        L=N//(i+1)+1\n        R=N//i\n\
    \n        if L<=R and X[-1][-1]<L:\n            X.append((N//L,L,R))\n    return\
    \ X\n\ndef Reminder_Enumeration(N,r):\n    \"\"\" N \u3092 q \u5272\u3063\u305F\
    \u4F59\u308A\u304C r \u306B\u306A\u308B q \u3092\u5168\u3066\u5217\u6319\u3059\
    \u308B.\n\n    N: \u6B63\u6574\u6570\n    r: \u975E\u8CA0\u6574\u6570, N!=r\n\
    \    \"\"\"\n\n    assert N!=r,\"\u7121\u9650\u500B\u3042\u308A\u307E\u3059.\"\
    \n\n    k=1\n    X=[];Y=[]\n    N-=r\n    while k*k<=N:\n        if N%k==0:\n\
    \            if k>r:\n                X.append(k)\n            if k*k!=N and N//k>r:\n\
    \                Y.append(N//k)\n        k+=1\n    return X+Y[::-1]\n\ndef Next_Remainder(x,\
    \ p, r):\n    \"\"\" x \u4EE5\u4E0A\u3067 p \u3067\u5272\u3063\u3066 r \u4F59\u308B\
    \u6574\u6570\u306E\u3046\u3061, \u6700\u5C0F\u306E\u6574\u6570\u3092\u6C42\u3081\
    \u308B.\n\n    \"\"\"\n\n    if x%p<=r:\n        return (x//p)*p+r\n    else:\n\
    \        return (x//p+1)*p+r\n\ndef Previous_Remainder(x, p, r):\n    \"\"\" x\
    \ \u4EE5\u4E0B\u3067 p \u3067\u5272\u3063\u3066 r \u4F59\u308B\u6574\u6570\u306E\
    \u3046\u3061, \u6700\u5927\u306E\u6574\u6570\u3092\u6C42\u3081\u308B.\n\n    \"\
    \"\"\n\n    if r<=x%p:\n        return (x//p)*p+r\n    else:\n        return (x//p-1)*p+r\n\
    \n#\u6CD5 p \u306E\u539F\u59CB\u6839\ndef Primitive_Root(p):\n    \"\"\"Z/pZ\u4E0A\
    \u306E\u539F\u59CB\u6839\u3092\u898B\u3064\u3051\u308B\n\n    p:\u7D20\u6570\n\
    \    \"\"\"\n    if p==2:\n        return 1\n    if p==998244353:\n        return\
    \ 3\n    if p==10**9+7:\n        return 5\n\n    fac=[]\n    q=2\n    v=p-1\n\n\
    \    while v>=q*q:\n        e=0\n        while v%q==0:\n            e+=1\n   \
    \         v//=q\n\n        if e>0:\n            fac.append(q)\n        q+=1\n\n\
    \    if v>1:\n        fac.append(v)\n\n    g=2\n    while g<p:\n        if pow(g,p-1,p)!=1:\n\
    \            return None\n\n        flag=True\n        for q in fac:\n       \
    \     if pow(g,(p-1)//q,p)==1:\n                flag=False\n                break\n\
    \n        if flag:\n            return g\n\n        g+=1\n\n#\u6700\u5927\u516C\
    \u7D04\u6570\ndef gcd(m,n):\n    m=abs(m)\n    n=abs(n)\n\n    while n:\n    \
    \    m,n=n,m%n\n    return m\n\ndef GCD(*X):\n    from functools import reduce\n\
    \    return reduce(gcd,X)\n\n#\u62E1\u5F35\u30E6\u30FC\u30AF\u30EA\u30C3\u30C9\
    \u306E\u4E92\u9664\u6CD5\ndef Extend_Euclid(a: int, b: int):\n    \"\"\" gcd(a,b)\
    \ \u3068 ax+by=gcd(a,b) \u3092\u6E80\u305F\u3059\u6574\u6570 x,y \u306E\u4F8B\u3092\
    \u6319\u3052\u308B.\n\n    [Input]\n    a,b: \u6574\u6570\n\n    [Output]\n  \
    \  (x,y,gcd(a,b))\n    \"\"\"\n    s,t,u,v=1,0,0,1\n    while b:\n        q,a,b=a//b,b,a%b\n\
    \        s,t=t,s-q*t\n        u,v=v,u-q*v\n    return s,u,a\n\ndef Modulo_Inverse(a,\
    \ m):\n    \"\"\" (mod m) \u306B\u304A\u3051\u308B\u9006\u5143\u3092\u6C42\u3081\
    \u308B.\n\n    Args:\n        a (int): mod m \u306E\u5143\n        m (int): \u6CD5\
    \n\n    Returns:\n        int: \u53EF\u9006\u5143\u304C\u5B58\u5728\u3059\u308B\
    \u306A\u3089\u3070\u305D\u306E\u5024, \u5B58\u5728\u3057\u306A\u3044\u306E\u3067\
    \u3042\u308C\u3070 -1\n    \"\"\"\n\n    h=Extend_Euclid(a,m)\n    return h[0]%m\
    \ if h[2]==1 else -1\n\n#\u6700\u5C0F\u516C\u500D\u6570\ndef lcm(m,n):\n    return\
    \ (m//gcd(m,n))*n\n\ndef LCM(*X):\n    from functools import reduce\n    return\
    \ reduce(lcm,X)\n\n#floor(a^(1/k)) \u3092\u6C42\u3081\u308B.\ndef Floor_Root(a,k):\n\
    \    \"\"\"floor(a^(1/k)) \u3092\u6C42\u3081\u308B.\n\n    a:\u975E\u8CA0\u6574\
    \u6570\n    k:\u6B63\u306E\u6574\u6570\n    \"\"\"\n    assert 0<=a and 0<k\n\
    \    if a==0: return 0\n    if k==1: return a\n\n    #\u5927\u4F53\u306E\u5024\
    \u3092\u6C42\u3081\u308B.\n    x=int(pow(a,1/k))\n\n    #\u5897\u3084\u3059\n\
    \    while pow(x+1,k)<=a:\n        x+=1\n\n    #\u6E1B\u3089\u3059\n    while\
    \ pow(x,k)>a:\n        x-=1\n    return x\n\n#ceil(a^(1/k)) \u3092\u6C42\u3081\
    \u308B.\ndef Ceil_Root(a,k):\n    \"\"\"ceil(a^(1/k)) \u3092\u6C42\u3081\u308B\
    .\n\n    a:\u975E\u8CA0\u6574\u6570\n    k:\u6B63\u306E\u6574\u6570\n    \"\"\"\
    \n    assert 0<=a and 0<k\n    if a==0:\n        return 0\n    if k==1:\n    \
    \    return a\n\n    #\u5927\u4F53\u306E\u5024\u3092\u6C42\u3081\u308B.\n    x=int(pow(a,1/k))+1\n\
    \n    #\u5897\u3084\u3059\n    while pow(x,k)<a:\n        x+=1\n\n    #\u6E1B\u3089\
    \u3059\n    while a<=pow(x-1,k):\n        x-=1\n    return x\n\ndef kth_Power(a,k):\n\
    \    \"\"\" \u6574\u6570 a \u304C k \u4E57\u6570\u304B\u3069\u3046\u304B\u3092\
    \u6C42\u3081, \u305D\u3046\u306A\u3089\u3070, b^k=a \u3092\u6E80\u305F\u3059 k\
    \ \u3092\u8FD4\u3059.\n\n    [Input]\n    a: int\n    k: int (k>0)\n\n    [Output]\n\
    \    \u5B58\u5728\u3057\u306A\u3044  : None\n    \u5B58\u5728\u3059\u308B    :\
    \ b^k=a \u3092\u6E80\u305F\u3059 b\n    \"\"\"\n\n    if k%2==0:\n        if a<0:\n\
    \            return None\n        b=Floor_Root(a,k)\n        return b if pow(b,k)==a\
    \ else None\n    else:\n        sgn=1 if a>=0 else -1\n        b=Floor_Root(abs(a),k)\n\
    \        return sgn*b if pow(sgn*b,k)==a else None\n"
  dependsOn: []
  isVerificationFile: false
  path: Integer.py
  requiredBy: []
  timestamp: '2022-12-06 20:55:37+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Integer.py
layout: document
redirect_from:
- /library/Integer.py
- /library/Integer.py.html
title: Integer.py
---
