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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.2/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.2/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "#\u6700\u5C0F\u516C\u500D\u6570\ndef lcm(m,n):\n    from math import gcd\n\
    \    return (m//gcd(m,n))*n\n\ndef LCM(*X):\n    from functools import reduce\n\
    \    return reduce(lcm,X)\n\n#floor(a^(1/k)) \u3092\u6C42\u3081\u308B.\ndef Floor_Root(a,k):\n\
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
  path: Integer/Value.py
  requiredBy: []
  timestamp: '2023-08-20 11:29:25+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Integer/Value.py
layout: document
redirect_from:
- /library/Integer/Value.py
- /library/Integer/Value.py.html
title: Integer/Value.py
---
