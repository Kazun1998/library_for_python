---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test_verify/yosupo_library_checker/Data_Structure/Number_of_Subsequences.test.py
    title: test_verify/yosupo_library_checker/Data_Structure/Number_of_Subsequences.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.13.5/x64/lib/python3.13/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.13.5/x64/lib/python3.13/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def Subsequence_Count(S, Mod=None, empty=True):\n    \"\"\" \u5217 S \u306E\
    \u7570\u306A\u308B (\u9023\u7D9A\u3068\u306F\u9650\u3089\u306A\u3044) \u90E8\u5206\
    \u5217\u306E\u500B\u6570\u3092\u6C42\u3081\u308B.\n\n    Mod: \u4F59\u308A\n \
    \   empty: \u7A7A\u90E8\u5206\u5217\u3092\u8A8D\u3081\u308B\u306A\u3089\u3070\
    \ True, \u8A8D\u3081\u306A\u3044\u306A\u3089\u3070 False.\n    \"\"\"\n\n    X=0\n\
    \    dp={}\n    for a in S:\n        Y=2*X+1-dp.get(a, 0)\n        dp[a]=X+1\n\
    \n        if Mod is None:\n            X=Y\n        else:\n            X=Y%Mod\n\
    \n    if Mod is not None:\n        return (X+empty)%Mod\n    else:\n        return\
    \ X+empty\n"
  dependsOn: []
  isVerificationFile: false
  path: Sequence/Subsequence_Count.py
  requiredBy: []
  timestamp: '2022-11-26 05:05:47+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test_verify/yosupo_library_checker/Data_Structure/Number_of_Subsequences.test.py
documentation_of: Sequence/Subsequence_Count.py
layout: document
redirect_from:
- /library/Sequence/Subsequence_Count.py
- /library/Sequence/Subsequence_Count.py.html
title: Sequence/Subsequence_Count.py
---
