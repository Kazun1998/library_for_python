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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.7/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.7/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def FFT(A,inverse=False):\n    from math import sin,cos,exp,pi\n\n    n=len(A)\n\
    \    max_level=(n-1).bit_length()\n    m=1<<max_level\n\n    w=complex(cos(2*pi/m),sin(2*pi/m))\n\
    \n    if inverse: #\u9006\u5909\u63DB\u306A\u3089\u3070...\n        w=1/w #\u9006\
    \u5143\n\n    W=[0]*(max_level+1)\n    W[-1]=w\n\n    for k in range(max_level-1,-1,-1):\n\
    \        W[k]=W[k+1]*W[k+1]\n\n    U=[[0]*(1<<x) for x in range(max_level+1)]\n\
    \n    for y in range(1,max_level+1):\n        for x in range(1<<y):\n        \
    \    if x==0:\n                U[y][x]=1\n            else:\n                U[y][x]=U[y][x-1]*W[y]\n\
    \n    def fft(x,level):\n        t=len(x)\n        if t==1:\n            return\
    \ x\n\n        y=[0]*(t>>1)\n        z=[0]*(t>>1)\n\n        for k in range(t//2):\n\
    \            y[k]=x[k]+x[k+t//2]\n            z[k]=(x[k]-x[k+t//2])*U[level][k]\n\
    \n        y=fft(y,level-1)\n        z=fft(z,level-1)\n\n        x=[0]*t\n    \
    \    for k in range(t>>1):\n            x[2*k]=y[k]\n            x[2*k+1]=z[k]\n\
    \n        return x\n\n    B=A+[0]*(m-n)\n    return fft(B,max_level)\n\ndef Inverse_FFT(A):\n\
    \    G=FFT(A,True)\n    return [a/len(G) for a in G]\n\ndef Convolution(A,B):\n\
    \    from math import floor\n\n    N=len(A);M=len(B)\n    if N==0 or M==0:\n \
    \       return []\n\n    z=1<<((N+M-2).bit_length())\n\n    A=A+[0]*(z-N)\n  \
    \  B=B+[0]*(z-M)\n\n    P=FFT(A)\n    Q=FFT(B)\n\n    R=[0]*z\n    for i in range(z):\n\
    \        R[i]=P[i]*Q[i]\n    R=Inverse_FFT(R)\n    return  [floor(a.real+1/2)\
    \ for a in R]\n\n#=================================================\ndef Primitive_Root(p):\n\
    \    if p==2:\n        return 1\n\n    fac=[]\n    q=2\n    v=p-1\n\n    while\
    \ v>=q*q:\n        e=0\n        while v%q==0:\n            e+=1\n            v//=q\n\
    \n        if e>0:\n            fac.append(q)\n        q+=1\n\n    if v>1:\n  \
    \      fac.append(v)\n\n    g=2\n    while g<p:\n        if pow(g,p-1,p)!=1:\n\
    \            return None\n\n        flag=True\n        for q in fac:\n       \
    \     if pow(g,(p-1)//q,p)==1:\n                flag=False\n                break\n\
    \n        if flag:\n            return g\n\n        g+=1\n\ndef NTT(A,Mod,primitive=None,inverse=False):\n\
    \    n=len(A)\n    max_level=(n-1).bit_length()\n    m=1<<max_level\n\n    if\
    \ primitive==None:\n        primitive=Primitive_Root(Mod)\n\n    u=Mod-1\n   \
    \ e=0\n    while u%2==0:\n        e+=1\n        u>>=1\n\n    w=pow(primitive,u,Mod)\n\
    \n    if inverse: #\u9006\u5909\u63DB\u306A\u3089\u3070...\n        w=pow(w,Mod-2,Mod)\
    \ #\u9006\u5143\n\n    W=[0]*(e+1)\n    W[-1]=w\n\n    for k in range(e-1,-1,-1):\n\
    \        W[k]=(W[k+1]*W[k+1])%Mod\n\n    U=[[0]*(1<<x) for x in range(max_level+1)]\n\
    \n    for y in range(1,max_level+1):\n        for x in range(1<<y):\n        \
    \    if x==0:\n                U[y][x]=1\n            else:\n                U[y][x]=(U[y][x-1]*W[y])%Mod\n\
    \n    def ntt(x,level):\n        t=len(x)\n        if t==1:\n            return\
    \ x\n\n        y=[0]*(t>>1)\n        z=[0]*(t>>1)\n\n        for k in range(t//2):\n\
    \            y[k]=(x[k]+x[k+t//2])%Mod\n            z[k]=((x[k]-x[k+t//2])*U[level][k])%Mod\n\
    \n        y=ntt(y,level-1)\n        z=ntt(z,level-1)\n\n        x=[0]*t\n    \
    \    for k in range(t>>1):\n            x[2*k]=y[k]\n            x[2*k+1]=z[k]\n\
    \n        return x\n\n    B=A+[0]*(m-n)\n    return ntt(B,max_level)\n\ndef Inverse_NTT(A,Mod,primitive=None):\n\
    \    B=NTT(A,Mod,primitive,inverse=True)\n    N_inv=pow(len(A),Mod-2,Mod)\n  \
    \  return [(N_inv*b)%Mod for b in B]\n\ndef Convolution_Mod(A,B,Mod,primitive=None):\n\
    \    N=len(A);M=len(B)\n    if N==0 or M==0:\n        return []\n\n    z=1<<((N+M-2).bit_length())\n\
    \n    A=A+[0]*(z-N)\n    B=B+[0]*(z-M)\n\n    if primitive==None:\n        primitive=Primitive_Root(Mod)\n\
    \n    P=NTT(A,Mod,primitive)\n    Q=NTT(B,Mod,primitive)\n\n    R=[(P[i]*Q[i])%Mod\
    \ for i in range(z)]\n\n    return Inverse_NTT(R,Mod,primitive)\n#=================================================\n"
  dependsOn: []
  isVerificationFile: false
  path: Convolution.py
  requiredBy: []
  timestamp: '2021-04-27 14:48:27+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Convolution.py
layout: document
redirect_from:
- /library/Convolution.py
- /library/Convolution.py.html
title: Convolution.py
---
