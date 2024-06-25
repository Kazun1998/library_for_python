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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.4/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.4/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def Quadratic_Function_Minimize(a,b,c,l,r):\n    \"\"\" l<=x<=r \u306B\u304A\
    \u3051\u308B ax^2+bx+c \u306E\u6700\u5C0F\u5024\u3092\u6C42\u3081\u308B.\n   \
    \ \"\"\"\n\n    f=lambda x:x*(a*x+b)+c\n\n    if a==0:\n        return min(f(l),f(r))\n\
    \    elif a>0:\n        xi=-b/(2*a)\n        if l<=xi<=r:\n            x=xi\n\
    \        elif r<=xi:\n            x=r\n        else:\n            x=l\n      \
    \  return f(x)\n    else:\n        return min(f(l), f(r))\n\ndef Quadratic_Function_Maximize(a,b,c,l,r):\n\
    \    \"\"\" l<=x<=r \u306B\u304A\u3051\u308B ax^2+bx+c \u306E\u6700\u5927\u5024\
    \u3092\u6C42\u3081\u308B.\n    \"\"\"\n\n    return -Quadratic_Function_Minimize(-a,-b,-c,l,r)\n\
    \ndef Quadratic_Function_Minimize_Integer(a,b,c,l,r):\n    \"\"\" l<=x<=r , x:\u6574\
    \u6570 \u306B\u304A\u3051\u308B ax^2+bx+c \u306E\u6700\u5C0F\u5024\u3092\u6C42\
    \u3081\u308B.\n    \"\"\"\n\n    f=lambda x:x*(a*x+b)+c\n\n    if a==0:\n    \
    \    return min(f(l),f(r))\n    elif a>0:\n        if 2*a*l<=-b<=2*a*r:\n    \
    \        x=(a-b)//(2*a)\n        elif 2*a*r<=-b:\n            x=r\n        else:\n\
    \            x=l\n        return f(x)\n    else:\n        return min(f(l), f(r))\n\
    \ndef Quadratic_Function_Maximize_Integer(a,b,c,l,r):\n    \"\"\" l<=x<=r \u306B\
    \u304A\u3051\u308B ax^2+bx+c \u306E\u6700\u5927\u5024\u3092\u6C42\u3081\u308B\
    .\n    \"\"\"\n\n    return -Quadratic_Function_Minimize_Integer(-a,-b,-c,l,r)\n\
    \n#=================================================\ndef Linear_Inverse_Sum_Function_Minimize(a,b,c,l,r):\n\
    \    \"\"\" l<=x<=r \u306B\u304A\u3051\u308B ax+b/x+c \u306E\u6700\u5C0F\u5024\
    \u3092\u6C42\u3081\u308B.\n    \"\"\"\n\n    f=lambda x:a*x+b/x+c\n\n    if a==0:\n\
    \        return f(r)\n    elif b==0:\n        return f(l)\n\n    from math import\
    \ sqrt\n    x=sqrt(b/a)\n\n    if l<=x<=r:\n        return f(x)\n    elif r<=x:\n\
    \        return f(r)\n    else:\n        return f(l)\n\ndef Linear_Inverse_Sum_Function_Minimize_Integer(a,b,c,l,r):\n\
    \    \"\"\" l<=x<=r, x: \u6574\u6570 \u306B\u304A\u3051\u308B ax+b/x+c \u306E\u6700\
    \u5C0F\u5024\u3092\u6C42\u3081\u308B.\n    \"\"\"\n\n    f=lambda x:a*x+b/x+c\n\
    \n    if a==0:\n        return b//r+c\n    elif b==0:\n        return a*l+c\n\n\
    \    if r*r<=b//a:\n        return f(r)\n    elif (b+a-1)//a<=l*l:\n        return\
    \ f(l)\n    else:\n        p=b//a\n        x=int(pow(p,1/2))\n\n        while\
    \ (x+1)*(x+1)<=p:\n            x+=1\n\n        while x*x>p:\n            x-=1\n\
    \n        if x==0:\n            return f(1)\n        else:\n            return\
    \ min(f(x), f(x+1))\n"
  dependsOn: []
  isVerificationFile: false
  path: Function_Minimizer.py
  requiredBy: []
  timestamp: '2023-08-08 23:43:12+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Function_Minimizer.py
layout: document
redirect_from:
- /library/Function_Minimizer.py
- /library/Function_Minimizer.py.html
title: Function_Minimizer.py
---
