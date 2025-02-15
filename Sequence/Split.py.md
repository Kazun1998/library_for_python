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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.13.2/x64/lib/python3.13/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.13.2/x64/lib/python3.13/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def split(A: list, separator: list) -> list[list]:\n    if not A:\n     \
    \   return []\n\n    sep = set(separator)\n    res = [[]]\n\n    for a in A:\n\
    \        if a not in sep:\n            res[-1].append(a)\n        else:\n    \
    \        res.append([])\n\n    return res\n"
  dependsOn: []
  isVerificationFile: false
  path: Sequence/Split.py
  requiredBy: []
  timestamp: '2025-01-03 00:56:06+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Sequence/Split.py
layout: document
redirect_from:
- /library/Sequence/Split.py
- /library/Sequence/Split.py.html
title: Sequence/Split.py
---
