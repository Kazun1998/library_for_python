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
  code: "#\u30CF\u30DF\u30F3\u30B0\u8DDD\u96E2\ndef Hamming_Distance(S, T):\n    \"\
    \"\" \u5217\u306E\u9577\u3055\u304C\u7B49\u3057\u3044 S, T \u306B\u304A\u3051\u308B\
    \u30CF\u30DF\u30F3\u30B0\u8DDD\u96E2\u3092\u6C42\u3081\u308B.\n\n    S,T: (|S|=|T|\
    \ \u3092\u6E80\u305F\u3057\u3066\u3044\u306A\u3051\u308C\u3070\u306A\u3089\u306A\
    \u3044)\n    \"\"\"\n\n    assert len(S)==len(T)\n    return sum(int(S[i]!=T[i])\
    \ for i in range(len(S)))\n"
  dependsOn: []
  isVerificationFile: false
  path: Sequence/Hamming_Distance.py
  requiredBy: []
  timestamp: '2022-11-26 03:55:08+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Sequence/Hamming_Distance.py
layout: document
title: Hamming Distance
---

## Outline

$\lvert S \rvert = \lvert T \rvert$ である列 $S,T$ に対して, $N:=\lvert S \rvert$ とする.
このとき, $S_i \neq T_i$ を満たす $1$ 以上 $N$ 以下の整数 $i$ の個数を $S,T$ の Hamming 距離という.
