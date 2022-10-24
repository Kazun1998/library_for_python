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
  code: "##\u3068.\u3067\u8868\u3055\u308C\u305F\u30B0\u30EA\u30C3\u30C9\u309201\u306B\
    \u5909\u63DB\u3059\u308B.\ndef Black_White_Grid(H:int, W:int, wall=False):\n \
    \   \"\"\"H: \u7E26\u306E\u30DE\u30B9\u6570, W: \u6A2A\u306E\u30DE\u30B9\u6570\
    \n\n    \u203B\u901A\u308C\u308B\u3068\u3053\u308D\u304C1\n    \"\"\"\n\n    f=lambda\
    \ s:1 if s==\".\" else 0\n\n    if wall:\n        S=[[0]*(W+2)]\n    else:\n \
    \       S=[]\n\n    for _ in range(H):\n        if wall:\n            S.append([0]+list(map(f,input()))+[0])\n\
    \        else:\n            S.append(list(map(f,input())))\n\n    if wall:\n \
    \       S.append([0]*(W+2))\n\n    return S\n\n#\u5C0F\u6570\u70B9\u4EE5\u4E0B\
    \u7B2Ck\u4F4D\u307E\u3067\u4E0E\u3048\u3089\u308C\u308B\u5C0F\u6570\u309210^k\u500D\
    \u3059\u308B.\ndef Decimal_to_Int(s:str,k:int,base=10) -> int:\n    \"\"\"\n\n\
    \    s:\u5C0F\u6570\u70B9\u3092\u542B\u3080\u304B\u3082\u3057\u308C\u306A\u3044\
    \u6570\n    k:\u5C0F\u6570\u70B9\u4EE5\u4E0B\u9AD8\u3005\u4F55\u4F4D\u307E\u3067\
    \u304B?\n    base:\u57FA\u6570\n    \"\"\"\n\n    if \".\" not in s:\n       \
    \ return int(s,base)*pow(base,k)\n\n    m=s.index(\".\")\n    return int(s.replace(\"\
    .\",\"\"))*pow(base,k-(len(s)-m-1))\n"
  dependsOn: []
  isVerificationFile: false
  path: Special_Input.py
  requiredBy: []
  timestamp: '2021-11-28 16:18:52+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Special_Input.py
layout: document
redirect_from:
- /library/Special_Input.py
- /library/Special_Input.py.html
title: Special_Input.py
---
