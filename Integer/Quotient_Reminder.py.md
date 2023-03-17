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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.2/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.2/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "#\u5546\u5217\u6319\ndef Quotient_Range(N):\n    \"\"\"N\u3067\u5272\u3063\
    \u305F\u5546\u306E\u53EF\u80FD\u6027\u3092\u5168\u3066\u5217\u6319\u3059\u308B\
    .\n\n    [Input]\n    N:\u6B63\u6574\u6570\n\n    [Output]\n    X:\u30EA\u30B9\
    \u30C8\n    X\u306E\u5404\u8981\u7D20(k,x,y) \u306F x<=i<=y \u3067\u3042\u308B\
    \u3053\u3068\u3068, floor(N/i)=k \u304C\u540C\u5024\u3067\u3042\u308B\u3053\u3068\
    \u3092\u8868\u3059.\n    \"\"\"\n    X=[]\n\n    M=1\n    while M*M<=N:\n    \
    \    X.append((N//M,M,M))\n        M+=1\n\n    for i in range(M,0,-1):\n     \
    \   L=N//(i+1)+1\n        R=N//i\n\n        if L<=R and X[-1][-1]<L:\n       \
    \     X.append((N//L,L,R))\n    return X\n\ndef Reminder_Enumeration(N,r):\n \
    \   \"\"\" N \u3092 q \u5272\u3063\u305F\u4F59\u308A\u304C r \u306B\u306A\u308B\
    \ q \u3092\u5168\u3066\u5217\u6319\u3059\u308B.\n\n    N: \u6B63\u6574\u6570\n\
    \    r: \u975E\u8CA0\u6574\u6570, N!=r\n    \"\"\"\n\n    assert N!=r,\"\u7121\
    \u9650\u500B\u3042\u308A\u307E\u3059.\"\n\n    k=1\n    X=[];Y=[]\n    N-=r\n\
    \    while k*k<=N:\n        if N%k==0:\n            if k>r:\n                X.append(k)\n\
    \            if k*k!=N and N//k>r:\n                Y.append(N//k)\n        k+=1\n\
    \    return X+Y[::-1]\n\ndef Next_Remainder(x, p, r):\n    \"\"\" x \u4EE5\u4E0A\
    \u3067 p \u3067\u5272\u3063\u3066 r \u4F59\u308B\u6574\u6570\u306E\u3046\u3061\
    , \u6700\u5C0F\u306E\u6574\u6570\u3092\u6C42\u3081\u308B.\n\n    \"\"\"\n\n  \
    \  if x%p<=r:\n        return (x//p)*p+r\n    else:\n        return (x//p+1)*p+r\n\
    \ndef Previous_Remainder(x, p, r):\n    \"\"\" x \u4EE5\u4E0B\u3067 p \u3067\u5272\
    \u3063\u3066 r \u4F59\u308B\u6574\u6570\u306E\u3046\u3061, \u6700\u5927\u306E\u6574\
    \u6570\u3092\u6C42\u3081\u308B.\n\n    \"\"\"\n\n    if r<=x%p:\n        return\
    \ (x//p)*p+r\n    else:\n        return (x//p-1)*p+r\n"
  dependsOn: []
  isVerificationFile: false
  path: Integer/Quotient_Reminder.py
  requiredBy: []
  timestamp: '2023-03-18 02:55:12+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Integer/Quotient_Reminder.py
layout: document
redirect_from:
- /library/Integer/Quotient_Reminder.py
- /library/Integer/Quotient_Reminder.py.html
title: Integer/Quotient_Reminder.py
---
