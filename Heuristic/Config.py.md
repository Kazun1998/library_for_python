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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.13.1/x64/lib/python3.13/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.13.1/x64/lib/python3.13/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from os import getenv\nfrom sys import stderr\n\nclass Config:\n    @staticmethod\n\
    \    def is_product(key = 'environment', development = 'development'):\n     \
    \   return getenv(key) == development\n\n    @staticmethod\n    def debug(*messages):\n\
    \        stderr.write(f\"[debug] {' '.join(map(str, messages))}\\n\")\n"
  dependsOn: []
  isVerificationFile: false
  path: Heuristic/Config.py
  requiredBy: []
  timestamp: '2025-02-01 00:09:19+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Heuristic/Config.py
layout: document
redirect_from:
- /library/Heuristic/Config.py
- /library/Heuristic/Config.py.html
title: Heuristic/Config.py
---
