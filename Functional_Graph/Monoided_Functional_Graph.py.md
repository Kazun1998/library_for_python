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
  code: "class Monoided_Functional_Graph:\n    def __init__(self, N, K, op, unit):\n\
    \        \"\"\" \u6709\u5411\u8FBA\u306B\u30E2\u30CE\u30A4\u30C9\u306E\u91CD\u307F\
    \u3092\u4E57\u305B\u305F Functional Graph \u3092\u751F\u6210\u3059\u308B.\n\n\
    \        Args:\n            N : \u9802\u70B9\u6570 (0,1,2,...,N-1 \u3092\u751F\
    \u6210\u3059\u308B)\n            K : \u8A08\u7B97\u306B\u5FC5\u8981\u306A\u6700\
    \u5927\u306E\u6307\u6570\n            op : \u30E2\u30CE\u30A4\u30C9\u306E\u6F14\
    \u7B97 op(new, old)\n            unit : \u5358\u4F4D\u5143\n        \"\"\"\n\n\
    \        self.N=N\n        self.K=K\n        self.op=op\n        self.unit=unit\n\
    \n        self.out=[list(range(N))]\n        self.value=[[unit]*N]\n\n    def\
    \ set_arc(self, source, target, x):\n        self.out[0][source]=target\n    \
    \    self.value[0][source]=x\n\n    def build(self):\n        K=self.K>>1\n  \
    \      N=self.N\n        op=self.op\n        while K:\n            A=self.out[-1];\
    \ X=[0]*N\n            B=self.value[-1]; Y=[0]*N\n\n            for i in range(N):\n\
    \                p=A[i]; x=B[i]\n                q=A[p]; y=B[p]\n            \
    \    X[i]=q; Y[i]=op(y,x)\n\n            self.out.append(X)\n            self.value.append(Y)\n\
    \            K>>=1\n\n    def operate(self, v, k):\n        x=self.unit\n    \
    \    op=self.op\n        out=self.out\n        value=self.value\n        d=0\n\
    \        while k:\n            if k&1:\n                x=op(value[d][v], x)\n\
    \                v=out[d][v]\n            k>>=1; d+=1\n        return x\n\n"
  dependsOn: []
  isVerificationFile: false
  path: Functional_Graph/Monoided_Functional_Graph.py
  requiredBy: []
  timestamp: '2023-06-18 17:02:56+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Functional_Graph/Monoided_Functional_Graph.py
layout: document
redirect_from:
- /library/Functional_Graph/Monoided_Functional_Graph.py
- /library/Functional_Graph/Monoided_Functional_Graph.py.html
title: Functional_Graph/Monoided_Functional_Graph.py
---
