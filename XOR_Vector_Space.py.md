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
  code: "\"\"\"Tips\n\u81EA\u7136\u6570\u5168\u4F53\u306E\u96C6\u5408 N \u306B\u304A\
    \u3044\u3066, \u52A0\u6CD5\u3068 F_2 \u3068\u306E\u30B9\u30AB\u30E9\u30FC\u500D\
    \u3092\n    x+y:=x xor y, [0] x:=0, [1] x:=x\n\u3068\u5B9A\u3081\u308B\u3068,\
    \ N \u306F F_2 \u4E0A\u306E\u30D9\u30AF\u30C8\u30EB\u7A7A\u9593\u306B\u306A\u308B\
    .\n\"\"\"\n\nclass XOR_Vector_Space:\n    def __init__(self):\n        self.S=[]\n\
    \n    def __contains__(self,x):\n        for v in self.S:\n            if x&v&(-v):\n\
    \                x^=v\n            if x==0:\n                return True\n   \
    \     return False\n\n    def __add__(self,other):\n        W=XOR_Vector_Space()\n\
    \n        W.S=self.S[:]\n        W.add_vector(*other.S)\n        return W\n\n\
    \    def add_vector(self,*T):\n        for x in T:\n            for v in self.S:\n\
    \                if x&v&(-v):\n                    x^=v\n                    if\
    \ x==0:\n                        break\n            if x:\n                self.S.append(x)\n\
    \n    def dim(self):\n        return len(self.S)\n\n    def reduction(self):\n\
    \        S=self.S\n        for i in range(len(S)):\n            vb=S[i]&(-S[i])\n\
    \            for j in  range(len(S)):\n                if i==j: continue\n\n \
    \               if S[j]&vb:\n                    S[j]^=S[i]\n        self.S=[s\
    \ for s in S if s]\n\n    def __le__(self,other):\n        for u in self.S:\n\
    \            if not u in other:\n                return False\n        return\
    \ True\n\n    def __ge__(self,other):\n        return other<=self\n\n    def __eq__(self,other):\n\
    \        return (self<=other) and (other<=self)\n\ndef Generate_Space(*S):\n \
    \   V=XOR_Vector_Space()\n    V.add_vector(*S)\n    V.reduction()\n    return\
    \ V\n\ndef Get_Basis(*S):\n    B=[]\n    V=XOR_Vector_Space()\n    k=0\n    for\
    \ v in S:\n        V.add_vector(v)\n        if k+1==V.dim():\n            B.append(v)\n\
    \            k+=1\n    return B\n"
  dependsOn: []
  isVerificationFile: false
  path: XOR_Vector_Space.py
  requiredBy: []
  timestamp: '2021-05-19 11:47:56+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: XOR_Vector_Space.py
layout: document
redirect_from:
- /library/XOR_Vector_Space.py
- /library/XOR_Vector_Space.py.html
title: XOR_Vector_Space.py
---
