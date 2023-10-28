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
  code: "\"\"\"\nNote\n\n\u4E09\u5206\u63A2\u7D22\u3092\u7528\u3044\u308B\u969B, f\
    \ \u306F\u4EE5\u4E0B\u306E\u3046\u3061\u306E\u3069\u308C\u304B\u3092\u898B\u305F\
    \u3057\u3066\u3044\u306A\u3051\u308C\u3070\u306A\u3089\u306A\u3044.\n\n* f \u306F\
    \u4E0B (\u4E0A) \u306B \"\u72ED\u7FA9\" \u51F8\u3067\u3042\u308B\n* a<b \u304C\
    \u5B58\u5728\u3057\u3066, f \u306F [L,a] \u4E0A\u72ED\u7FA9\u5358\u8ABF\u6E1B\u5C11\
    \ (\u5897\u52A0), [a,b] \u4E0A\u5B9A\u6570, [b,R] \u4E0A\u72ED\u7FA9\u5358\u8ABF\
    \u5897\u52A0 (\u6E1B\u5C11)\n* f\u306F\u5358\u8ABF\u6E1B\u5C11 (\u5358\u8ABF\u5897\
    \u52A0)\n\"\"\"\n\ndef Ternary_Search_Minimize_Integer(L, R, f, arg=False):\n\
    \    \"\"\" \u4E09\u5206\u63A2\u7D22\u306B\u3088\u3063\u3066, \u6574\u6570\u3092\
    \u5B9A\u7FA9\u57DF\u3068\u3059\u308B\u95A2\u6570 f \u306E [L,R] \u306B\u304A\u3051\
    \u308B\u6700\u5C0F\u5024\u3092\u6C42\u3081\u308B.\n\n    f: [L,R] \u5185\u3067\
    \u4E0B\u306B\u51F8\u307E\u305F\u306F\u5358\u8ABF\u6E1B\u5C11\n    \"\"\"\n   \
    \ while (R-L)>3:\n        a=(2*L+R)//3\n        b=(L+2*R)//3\n\n        p=f(a);\
    \ q=f(b)\n        if p<=q:\n            R=b\n        else:\n            L=a\n\n\
    \    a=(2*L+R)//3\n    b=(L+2*R)//3\n\n    if arg:\n        y,argx=f(L),L\n  \
    \      for x in [a,b,R]:\n            p=f(x)\n            if y>p:\n          \
    \      y,argx=p,x\n        return y,argx\n    else:\n        return min(f(L),f(a),f(b),f(R))\n\
    \ndef Ternary_Search_Minimize_Real(L, R, f, arg=False, ep=1/(1<<20), Times=50):\n\
    \    \"\"\" \u4E09\u5206\u63A2\u7D22\u306B\u3088\u3063\u3066, \u5B9F\u6570\u3092\
    \u5B9A\u7FA9\u57DF\u3068\u3059\u308B\u95A2\u6570 f \u306E [L,R] \u306B\u304A\u3051\
    \u308B\u6700\u5C0F\u5024\u3092\u6C42\u3081\u308B.\n\n    f: [L,R] \u5185\u3067\
    \u4E0B\u306B\u51F8\u307E\u305F\u306F\u5358\u8ABF\u6E1B\u5C11\n    \"\"\"\n   \
    \ while (R-L)>=ep and Times:\n        Times-=1\n        a=(2*L+R)/3\n        b=(L+2*R)/3\n\
    \n        p=f(a); q=f(b)\n        if p<=q:\n            R=b\n        else:\n \
    \           L=a\n\n    a=(2*L+R)/3\n    b=(L+2*R)/3\n\n    if arg:\n        y,argx=f(L),L\n\
    \        for x in [a,b,R]:\n            p=f(x)\n            if y>p:\n        \
    \        y,argx=p,x\n        return y,argx\n    else:\n        return min(f(L),f(a),f(b),f(R))\n\
    \ndef Ternary_Search_Maximize_Integer(L, R, f, arg=False):\n    \"\"\" \u4E09\u5206\
    \u63A2\u7D22\u306B\u3088\u3063\u3066, \u6574\u6570\u3092\u5B9A\u7FA9\u57DF\u3068\
    \u3059\u308B\u95A2\u6570 f \u306E [L,R] \u306B\u304A\u3051\u308B\u6700\u5927\u5024\
    \u3092\u6C42\u3081\u308B.\n\n    f: [L,R] \u5185\u3067\u4E0A\u306B\u51F8\u307E\
    \u305F\u306F\u5358\u8ABF\u5897\u52A0\n    \"\"\"\n    while (R-L)>3:\n       \
    \ a=(2*L+R)//3\n        b=(L+2*R)//3\n\n        p=f(a); q=f(b)\n        if p>=q:\n\
    \            R=b\n        else:\n            L=a\n\n    a=(2*L+R)//3\n    b=(L+2*R)//3\n\
    \n    if arg:\n        y,argx=f(L),L\n        for x in [a,b,R]:\n            p=f(x)\n\
    \            if y<p:\n                y,argx=p,x\n        return y,argx\n    else:\n\
    \        return max(f(L),f(a),f(b),f(R))\n\ndef Ternary_Search_Maximize_Real(L,\
    \ R, f, arg=False, ep=1/(1<<20), Times=50):\n    \"\"\" \u4E09\u5206\u63A2\u7D22\
    \u306B\u3088\u3063\u3066, \u5B9F\u6570\u3092\u5B9A\u7FA9\u57DF\u3068\u3059\u308B\
    \u95A2\u6570 f \u306E [L,R] \u306B\u304A\u3051\u308B\u6700\u5927\u5024\u3092\u6C42\
    \u3081\u308B.\n\n    f: [L,R] \u5185\u3067\u4E0A\u306B\u51F8\u307E\u305F\u306F\
    \u5358\u8ABF\u5897\u52A0\n    \"\"\"\n\n    while (R-L)>=ep and Times:\n     \
    \   Times-=1\n        a=(2*L+R)/3\n        b=(L+2*R)/3\n\n        p=f(a); q=f(b)\n\
    \        if p>=q:\n            R=b\n        else:\n            L=a\n\n    a=(2*L+R)/3\n\
    \    b=(L+2*R)/3\n\n    if arg:\n        y,argx=f(L),L\n        for x in [a,b,R]:\n\
    \            p=f(x)\n            if y<p:\n                y,argx=p,x\n       \
    \ return y,argx\n    else:\n        return max(f(L),f(a),f(b),f(R))\n"
  dependsOn: []
  isVerificationFile: false
  path: Binary_Search/Ternary.py
  requiredBy: []
  timestamp: '2022-09-10 17:07:59+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Binary_Search/Ternary.py
layout: document
redirect_from:
- /library/Binary_Search/Ternary.py
- /library/Binary_Search/Ternary.py.html
title: Binary_Search/Ternary.py
---
