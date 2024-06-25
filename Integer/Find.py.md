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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.4/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.4/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def Find_Previous_Arithmetic_Progression(l: int, d: int, k: int, x: int,\
    \ default = None):\n    \"\"\" \u521D\u9805 l, \u516C\u5DEE d, \u9805\u6570 k\
    \ \u306E\u6574\u6570\u5217\u306B\u3042\u308B x \u4EE5\u4E0B\u306E\u6700\u5927\u306E\
    \u9805\u3092\u6C42\u3081\u308B.\n\n    Args:\n        l (int): \u521D\u9805\n\
    \        d (int): \u516C\u5DEE\n        k (int): \u9805\u6570\n        x (int):\
    \ \u4E0B\u7AEF\n        default : \u5B58\u5728\u3057\u306A\u3044\u5834\u5408\u306E\
    \u8FD4\u308A\u5024. Defaults to None.\n    \"\"\"\n\n    if d < 0:\n        l,\
    \ d = l + (k - 1) * d, -d\n\n    if d == 0:\n        return x if x == l else default\n\
    \n    r = l + (k - 1) * d\n    if x < l:\n        return default\n\n    x = min(x,\
    \ r)\n    p = (x - l) // d\n    return l + p * d\n\ndef Find_Next_Arithmetic_Progression(l:\
    \ int, d: int, k: int, x: int, default = None):\n    \"\"\" \u521D\u9805 l, \u516C\
    \u5DEE d, \u9805\u6570 k \u306E\u6574\u6570\u5217\u306B\u3042\u308B x \u4EE5\u4E0A\
    \u306E\u6700\u5C0F\u306E\u9805\u3092\u6C42\u3081\u308B.\n\n    Args:\n       \
    \ l (int): \u521D\u9805\n        d (int): \u516C\u5DEE\n        k (int): \u9805\
    \u6570\n        x (int): \u4E0B\u7AEF\n        default : \u5B58\u5728\u3057\u306A\
    \u3044\u5834\u5408\u306E\u8FD4\u308A\u5024. Defaults to None.\n    \"\"\"\n\n\
    \    if d < 0:\n        l, d = l + (k - 1) * d, -d\n\n    if d == 0:\n       \
    \ return x if x == l else default\n\n    r = l + (k - 1) * d\n    if r < x:\n\
    \        return default\n\n    x = max(x, l)\n    p = (x - l + d - 1) // d\n \
    \   return l + p * d\n"
  dependsOn: []
  isVerificationFile: false
  path: Integer/Find.py
  requiredBy: []
  timestamp: '2024-02-25 14:43:02+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Integer/Find.py
layout: document
redirect_from:
- /library/Integer/Find.py
- /library/Integer/Find.py.html
title: Integer/Find.py
---
