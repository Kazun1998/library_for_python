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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def Run_Length_Encoding(S):\n    \"\"\" Run Length \u5727\u7E2E\n\n    S:\
    \ \u5217\n    \"\"\"\n    if not S:\n        return []\n\n    R=[[S[0],1]]\n\n\
    \    for i in range(1,len(S)):\n        if R[-1][0]==S[i]:\n            R[-1][1]+=1\n\
    \        else:\n            R.append([S[i],1])\n\n    return R\n"
  dependsOn: []
  isVerificationFile: false
  path: Sequence/Run_Length_Encoding.py
  requiredBy: []
  timestamp: '2022-11-26 03:55:08+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Sequence/Run_Length_Encoding.py
layout: document
redirect_from:
- /library/Sequence/Run_Length_Encoding.py
- /library/Sequence/Run_Length_Encoding.py.html
title: Sequence/Run_Length_Encoding.py
---
