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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.13.5/x64/lib/python3.13/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.13.5/x64/lib/python3.13/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from typing import TypeVar, Generic, Callable\n\nM = TypeVar('M')\nclass\
    \ Monoided_Functional_Graph(Generic[M]):\n    def __init__(self, N: int, K: int,\
    \ op: Callable[[M, M], M], unit: M):\n        \"\"\" \u6709\u5411\u8FBA\u306B\u30E2\
    \u30CE\u30A4\u30C9\u306E\u91CD\u307F\u3092\u4E57\u305B\u305F Functional Graph\
    \ \u3092\u751F\u6210\u3059\u308B.\n\n        Args:\n            N (int): \u9802\
    \u70B9\u6570 (0,1,2,...,N-1 \u3092\u751F\u6210\u3059\u308B)\n            K (int):\
    \ \u8A08\u7B97\u306B\u5FC5\u8981\u306A\u6700\u5927\u306E\u6307\u6570\n       \
    \     op (Callable[[M, M], M]): \u30E2\u30CE\u30A4\u30C9\u306E\u6F14\u7B97 op(new,\
    \ old)\n            unit (M): \u5358\u4F4D\u5143\n        \"\"\"\n\n        self.N=N\n\
    \        self.K=K\n        self.op=op\n        self.unit=unit\n\n        self.out=[list(range(N))]\n\
    \        self.value=[[unit]*N]\n\n    def set_arc(self, source: int, target: int,\
    \ x: M) -> None:\n        \"\"\" \u91CD\u307F x \u3067\u6709\u5411\u8FBA source\
    \ -> target \u3092\u8A2D\u5B9A\u3059\u308B\n\n        Args:\n            source\
    \ (int): \u59CB\u70B9\n            target (int): \u7D42\u70B9\n            x (M):\
    \ \u91CD\u307F\n        \"\"\"\n\n        self.out[0][source]=target\n       \
    \ self.value[0][source]=x\n\n    def build(self) -> None:\n        \"\"\" Functional\
    \ Graph \u3092\u78BA\u5B9A\u3055\u305B\u308B.\n        \"\"\"\n\n        # 1 \u6BB5\
    \u968E\u76EE\u306F\u5143\u306E\u60C5\u5831\u3067\u3042\u308B\u304B\u3089\u7701\
    \u7565\n        K = self.K >> 1\n        N = self.N\n        op = self.op\n\n\
    \        while K:\n            prev_out = self.out[-1]\n            current_out\
    \ = [0] * N\n            prev_value = self.value[-1]\n            current_value\
    \ = [None] * N\n\n            for i in range(N):\n                p = prev_out[i];\
    \ x = prev_value[i]\n                q = prev_out[p]; y = prev_value[p]\n\n  \
    \              current_out[i] = q\n                current_value[i] = op(y, x)\n\
    \n            self.out.append(current_out)\n            self.value.append(current_value)\n\
    \            K >>= 1\n\n    def calculate(self, v: int, k: int) -> M:\n      \
    \  \"\"\" \u9802\u70B9 v \u304B\u3089 k \u56DE\u79FB\u52D5\u3057\u305F\u3068\u304D\
    \u306E\u7D2F\u7A4D\u91CD\u307F\u3092\u6C42\u3081\u308B.\n\n        Args:\n   \
    \         v (int): \u59CB\u70B9\n            k (int): \u79FB\u52D5\u56DE\u6570\
    \n\n        Returns:\n            M: \u7D2F\u7A4D\u91CD\u307F\n        \"\"\"\n\
    \        x = self.unit\n        op = self.op\n        out = self.out\n       \
    \ value = self.value\n        for out, value in zip(out, value):\n           \
    \ if k & 1:\n                x = op(value[v], x)\n                v = out[v]\n\
    \            k >>= 1\n\n        return x\n"
  dependsOn: []
  isVerificationFile: false
  path: Functional_Graph/Monoided_Functional_Graph.py
  requiredBy: []
  timestamp: '2025-02-22 15:15:59+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Functional_Graph/Monoided_Functional_Graph.py
layout: document
redirect_from:
- /library/Functional_Graph/Monoided_Functional_Graph.py
- /library/Functional_Graph/Monoided_Functional_Graph.py.html
title: Functional_Graph/Monoided_Functional_Graph.py
---
