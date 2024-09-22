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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.6/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.6/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class Nimber():\n    def __init__(self,x):\n        assert x>=0\n       \
    \ self.x=x\n\n    def __str__(self):\n        return \"Nimber({})\".format(self.x)\n\
    \n    def __repr__(self):\n        return \"Nimber({})\".format(self.x)\n\n  \
    \  #\u6B63, \u8CA0\n    def __pos__(self):\n        return self\n\n    def __neg__(self):\n\
    \        return self\n\n    #\u52A0\u6CD5\n    def __add__(self,other):\n    \
    \    return Nimber(self.x^other.x)\n\n    #\u6E1B\u6CD5\n    def __sub__(self,other):\n\
    \        return self+other\n\n    #\u4E57\u6CD5\n"
  dependsOn: []
  isVerificationFile: false
  path: Nimber.py
  requiredBy: []
  timestamp: '2021-04-27 14:48:27+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Nimber.py
layout: document
redirect_from:
- /library/Nimber.py
- /library/Nimber.py.html
title: Nimber.py
---
