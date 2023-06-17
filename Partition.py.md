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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def Integer_Partition(N,M):\n    \"\"\" \u5404\u9805\u304C M \u4EE5\u4E0B\
    \u306E N \u306E\u5206\u5272\u3092\u6C42\u3081\u308B. \"\"\"\n\n    M=min(M,N)\n\
    \    Q=[[k] for k in range(1,M+1)]\n    X=[]\n\n    while Q:\n        x=Q.pop()\n\
    \        alpha=sum(x)\n\n        if alpha==N:\n            X.append(x)\n     \
    \       continue\n\n        for k in range(1, min(M, N-alpha, x[-1])+1):\n   \
    \         Q.append(x+[k])\n\n    return X\n\ndef Integer_Partition_yielder(N,M):\n\
    \    \"\"\" \u5404\u9805\u304C M \u4EE5\u4E0B\u306E N \u306E\u5206\u5272\u3092\
    \u6C42\u3081\u308B. (yielder)\"\"\"\n\n    M=min(M,N)\n    Q=[[k] for k in range(1,M+1)]\n\
    \n    while Q:\n        x=Q.pop()\n        alpha=sum(x)\n\n        if alpha==N:\n\
    \            yield x\n            continue\n\n        for k in range(1, min(M,\
    \ N-alpha, x[-1])+1):\n            Q.append(x+[k])\n\n"
  dependsOn: []
  isVerificationFile: false
  path: Partition.py
  requiredBy: []
  timestamp: '2023-05-20 13:42:15+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Partition.py
layout: document
redirect_from:
- /library/Partition.py
- /library/Partition.py.html
title: Partition.py
---
