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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.3/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.3/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def Convolution(A,B):\n    def FFT(A, inverse=False):\n        from math\
    \ import sin,cos,pi\n        N=len(A)\n        max_level=N.bit_length()-1\n\n\
    \        w=complex(cos(2*pi/N), sin(2*pi/N))\n\n        if inverse: #\u9006\u5909\
    \u63DB\u306A\u3089\u3070...\n            w=w.conjugate() #\u9006\u5143\n\n   \
    \     W=[0]*(max_level+1)\n        W[-1]=w\n\n        for k in range(max_level-1,-1,-1):\n\
    \            W[k]=W[k+1]*W[k+1]\n\n        def fft(X, level):\n            t=len(X)\n\
    \            if t==1:\n                return X\n\n            Y=[0]*(t>>1)\n\
    \            Z=[0]*(t>>1)\n\n            w=W[level]\n            u=1\n       \
    \     for j in range(t//2):\n                Y[j]=X[j]+X[j+t//2]\n           \
    \     Z[j]=(X[j]-X[j+t//2])*u\n                u*=w\n\n            Y=fft(Y, level-1)\n\
    \            Z=fft(Z, level-1)\n\n            V=[0]*t\n            for k in range(t>>1):\n\
    \                V[2*k]=Y[k]\n                V[2*k+1]=Z[k]\n            return\
    \ V\n\n        return fft(A, max_level)\n\n    def Inverse_NTT(A):\n        B=FFT(A,\
    \ True)\n        N=len(A)\n        return [b/N for b in B]\n    from math import\
    \ floor\n\n    #========================================\n\n    if len(A)==0 or\
    \ len(B)==0:\n        return 0\n\n    L=len(A)+len(B)-1\n    N=1<<((len(A)+len(B)-1)-1).bit_length()\n\
    \    A=A+[0]*(N-len(A))\n    B=B+[0]*(N-len(B))\n\n    A=FFT(A); B=FFT(B)\n  \
    \  A=[A[i]*B[i] for i in range(N)]\n    A=Inverse_NTT(A)\n\n    del A[L:]\n  \
    \  return [floor(a.real+0.5) for a in A]\n"
  dependsOn: []
  isVerificationFile: false
  path: Convolution/ADD_Convolution.py
  requiredBy: []
  timestamp: '2022-11-22 22:30:12+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Convolution/ADD_Convolution.py
layout: document
redirect_from:
- /library/Convolution/ADD_Convolution.py
- /library/Convolution/ADD_Convolution.py.html
title: Convolution/ADD_Convolution.py
---
