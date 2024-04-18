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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.3/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.3/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def Largest_Rectangle(H, mode=0):\n    \"\"\" \u30D2\u30B9\u30C8\u30B0\u30E9\
    \u30E0 H \u306B\u304A\u3051\u308B\u6700\u5927\u9577\u65B9\u5F62\u306E\u30B5\u30A4\
    \u30BA\u3092\u6C42\u3081\u308B.\n\n    H: \u30EA\u30B9\u30C8\n    mode: 1 \u306E\
    \u3068\u304D\u306F\u305D\u306E\u7BC4\u56F2\u3082\u6C42\u3081\u308B.\n    \"\"\"\
    \n    from collections import deque\n    H=H+[0]\n    S=deque([])\n    X=H[0]\n\
    \    l=r=-1\n    for i in range(len(H)):\n        if (not S) or H[S[-1]]<H[i]:\n\
    \            S.append(i)\n        else:\n            while S and H[S[-1]]>=H[i]:\n\
    \                j=S.pop()\n                if X<H[j]*(i-j):\n               \
    \     X=H[j]*(i-j)\n                    l=j; r=i-1\n            H[j]=H[i]\n  \
    \          S.append(j)\n\n    if mode==0:\n        return X\n    else:\n     \
    \   return X,(l,r)\n"
  dependsOn: []
  isVerificationFile: false
  path: Largest_Rectangle.py
  requiredBy: []
  timestamp: '2022-12-24 17:41:50+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Largest_Rectangle.py
layout: document
redirect_from:
- /library/Largest_Rectangle.py
- /library/Largest_Rectangle.py.html
title: Largest_Rectangle.py
---
