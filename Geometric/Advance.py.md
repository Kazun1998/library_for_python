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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.7/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.7/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from Point import *\nfrom Circle import *\nfrom Triangle import *\n\ndef\
    \ Minimum_Enclosing_Circle(S,Times=100):\n    \"\"\"\u70B9\u306E\u96C6\u5408 S\
    \ \u306B\u304A\u3051\u308B\u6700\u5C0F\u5185\u5305\u5186\u3092\u6C42\u3081\u308B\
    .\n    \"\"\"\n\n    ep=max_ep(*S)\n    if len(S)==1:\n        return Circle(S[0],0)\n\
    \    elif len(S)==2:\n        M=(S[0]+S[1])/2\n        return Circle(M,abs(M-S[0]))\n\
    \    elif len(S)==3:\n        A,B,C=S\n        a=abs(B-C); b=abs(C-A); c=abs(A-B)\n\
    \        a2=a*a; b2=b*b; c2=c*c\n        if compare(a2,b2+c2,ep)==1:\n       \
    \     return Minimum_Enclosing_Circle([B,C])\n        elif compare(b2,c2+a2,ep)==1:\n\
    \            return Minimum_Enclosing_Circle([C,A])\n        elif compare(c2,a2+b2,ep)==1:\n\
    \            return Minimum_Enclosing_Circle([A,B])\n        else:\n         \
    \   ta=a2*(-a2+b2+c2)\n            tb=b2*(a2-b2+c2)\n            tc=c2*(a2+b2-c2)\n\
    \            s=ta+tb+tc\n\n            K=(ta/s)*A+(tb/s)*B+(tc/s)*C\n        \
    \    return Circle(K,abs(K-A))\n\n    def f(x,y):\n        res=0\n        for\
    \ p in S:\n            dx=x-p.x; dy=y-p.y\n            res=max(res,dx*dx+dy*dy)\n\
    \        return sqrt(res)\n\n    def g(x):\n        L=y_min; R=y_max\n       \
    \ for _ in range(Times):\n            a=(2*L+R)/3\n            b=(L+2*R)/3\n\n\
    \            if f(x,a)>f(x,b):\n                L=a\n            else:\n     \
    \           R=b\n        c=(L+R)/2\n        return f(x,c),c\n\n    inf=float(\"\
    inf\")\n    x_min,x_max=inf,-inf\n    y_min,y_max=inf,-inf\n\n    for p in S:\n\
    \        x_min=min(x_min,p.x)\n        x_max=max(x_max,p.x)\n        y_min=min(y_min,p.y)\n\
    \        y_max=max(y_max,p.y)\n\n    L=x_min; R=x_max\n    for _ in range(Times):\n\
    \        a=(2*L+R)/3\n        b=(L+2*R)/3\n\n        if g(a)[0]>g(b)[0]:\n   \
    \         L=a\n        else:\n            R=b\n\n    X=(L+R)/2\n    r,Y=g(X)\n\
    \n    C=Point(X,Y)\n\n    Q=sorted([(0,abs(C-S[0])),(1,abs(C-S[1])),(2,abs(C-S[2]))],key=lambda\
    \ t:t[1],reverse=True)\n    for i in range(3,len(S)):\n        m=(i,abs(C-S[i]))\n\
    \        for k in range(3):\n            if m[1]>Q[k][1]:\n                Q[k],m=m,Q[k]\n\
    \    return Minimum_Enclosing_Circle([S[j] for j,_ in Q])\n"
  dependsOn: []
  isVerificationFile: false
  path: Geometric/Advance.py
  requiredBy: []
  timestamp: '2021-08-13 04:28:12+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Geometric/Advance.py
layout: document
redirect_from:
- /library/Geometric/Advance.py
- /library/Geometric/Advance.py.html
title: Geometric/Advance.py
---
