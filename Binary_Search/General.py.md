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
  code: "def General_Binary_Increase_Search_Integer(L, R, cond, default=None):\n \
    \   \"\"\" \u6761\u4EF6\u5F0F\u304C\u5358\u8ABF\u5897\u52A0\u3067\u3042\u308B\u3068\
    \u304D, \u6574\u6570\u4E0A\u3067\u4E8C\u90E8\u63A2\u7D22\u3092\u884C\u3046.\n\n\
    \    L: \u89E3\u306E\u4E0B\u9650\n    R: \u89E3\u306E\u4E0A\u9650\n    cond: \u6761\
    \u4EF6(1\u5909\u6570\u95A2\u6570, \u5E83\u7FA9\u5358\u8ABF\u5897\u52A0\u3092\u6E80\
    \u305F\u3059)\n    default: L\u3067\u6761\u4EF6\u3092\u6E80\u305F\u3055\u306A\u3044\
    \u3068\u304D\u306E\u8FD4\u308A\u5024\n    \"\"\"\n\n    if not(cond(R)):\n   \
    \     return default\n\n    if cond(L):\n        return L\n\n    R+=1\n    while\
    \ R-L>1:\n        C=L+(R-L)//2\n        if cond(C):\n            R=C\n       \
    \ else:\n            L=C\n    return R\n\ndef General_Binary_Decrease_Search_Integer(L,\
    \ R, cond, default=None):\n    \"\"\" \u6761\u4EF6\u5F0F\u304C\u5358\u8ABF\u6E1B\
    \u5C11\u3067\u3042\u308B\u3068\u304D, \u6574\u6570\u4E0A\u3067\u4E8C\u90E8\u63A2\
    \u7D22\u3092\u884C\u3046.\n\n    L: \u89E3\u306E\u4E0B\u9650\n    R: \u89E3\u306E\
    \u4E0A\u9650\n    cond: \u6761\u4EF6 (1\u5909\u6570\u95A2\u6570, \u5E83\u7FA9\u5358\
    \u8ABF\u6E1B\u5C11 \u3092\u6E80\u305F\u3059)\n    default: R \u3067\u6761\u4EF6\
    \u3092\u6E80\u305F\u3055\u306A\u3044\u3068\u304D\u306E\u8FD4\u308A\u5024\n   \
    \ \"\"\"\n\n    if not(cond(L)):\n        return default\n\n    if cond(R):\n\
    \        return R\n\n    L-=1\n    while R-L>1:\n        C=L+(R-L)//2\n      \
    \  if cond(C):\n            L=C\n        else:\n            R=C\n    return L\n\
    \ndef General_Binary_Increase_Search_Real(L, R, cond,ep=1/(1<<20), Times=30, default=None):\n\
    \    \"\"\" \u6761\u4EF6\u5F0F\u304C\u5358\u8ABF\u5897\u52A0\u3067\u3042\u308B\
    \u3068\u304D, \u5B9F\u6570\u4E0A\u3067\u4E00\u822C\u7684\u306A\u4E8C\u90E8\u63A2\
    \u7D22\u3092\u884C\u3046.\n\n    L: \u89E3\u306E\u4E0B\u9650\n    R: \u89E3\u306E\
    \u4E0A\u9650\n    cond: \u6761\u4EF6(1\u5909\u6570\u95A2\u6570, \u5E83\u7FA9\u5358\
    \u8ABF\u5897\u52A0\u3092\u6E80\u305F\u3059)\n    ep: \u89E3\u306E\u8A31\u5BB9\u3059\
    \u308B\u8AA4\u5DEE\n    Times: \u5224\u5B9A\u56DE\u6570\u306E\u4E0A\u9650\n  \
    \  default: L\u3067\u6761\u4EF6\u3092\u6E80\u305F\u3055\u306A\u3044\u3068\u304D\
    \u306E\u8FD4\u308A\u5024\n    \"\"\"\n    if not(cond(R)):\n        return default\n\
    \n    if cond(L):\n        return L\n\n    while (R-L)>=ep and Times:\n      \
    \  Times-=1\n        C=L+(R-L)/2\n        if cond(C):\n            R=C\n     \
    \   else:\n            L=C\n    return (L+R)/2\n\ndef General_Binary_Decrease_Search_Real(L,\
    \ R, cond, ep=1/(1<<20), Times=30, default=None):\n    \"\"\" \u6761\u4EF6\u5F0F\
    \u304C\u5358\u8ABF\u6E1B\u5C11\u3067\u3042\u308B\u3068\u304D, \u5B9F\u6570\u4E0A\
    \u3067\u4E00\u822C\u7684\u306A\u4E8C\u90E8\u63A2\u7D22\u3092\u884C\u3046.\n\n\
    \    L:\u89E3\u306E\u4E0B\u9650\n    R:\u89E3\u306E\u4E0A\u9650\n    cond:\u6761\
    \u4EF6(1\u5909\u6570\u95A2\u6570, \u5E83\u7FA9\u5358\u8ABF\u6E1B\u5C11\u3092\u6E80\
    \u305F\u3059)\n    ep: \u89E3\u306E\u8A31\u5BB9\u3059\u308B\u8AA4\u5DEE\n    Times:\
    \ \u5224\u5B9A\u56DE\u6570\u306E\u4E0A\u9650\n    default: R\u3067\u6761\u4EF6\
    \u3092\u6E80\u305F\u3055\u306A\u3044\u3068\u304D\u306E\u8FD4\u308A\u5024\n   \
    \ \"\"\"\n\n    if not(cond(L)):\n        return default\n\n    if cond(R):\n\
    \        return R\n\n    while (R-L)>=ep and Times:\n        Times-=1\n      \
    \  C=L+(R-L)/2\n        if cond(C):\n            L=C\n        else:\n        \
    \    R=C\n    return (L+R)/2\n"
  dependsOn: []
  isVerificationFile: false
  path: Binary_Search/General.py
  requiredBy: []
  timestamp: '2022-10-01 17:24:05+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Binary_Search/General.py
layout: document
redirect_from:
- /library/Binary_Search/General.py
- /library/Binary_Search/General.py.html
title: Binary_Search/General.py
---
