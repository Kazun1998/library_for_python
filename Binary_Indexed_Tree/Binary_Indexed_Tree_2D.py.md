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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.5/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.5/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class Binary_Indexed_Tree_2D():\n    def __init__(self, M, op, zero, neg):\n\
    \        \"\"\" op \u3092\u6F14\u7B97\u3068\u3059\u308B N \u9805\u306E Binary\
    \ Indexed Tree (0-indexed) \u3092\u4F5C\u6210\n        op: \u6F14\u7B97 (2\u5909\
    \u6570\u95A2\u6570, \u53EF\u63DB\u7FA4)\n        zero: \u7FA4 op \u306E\u5358\u4F4D\
    \u5143 (x+e=e+x=x\u3092\u6E80\u305F\u3059e)\n        neg : \u7FA4 op \u306E\u9006\
    \u5143 (1\u5909\u6570\u95A2\u6570, x+neg(x)=neg(x)+x=e \u3092\u307F\u305F\u3059\
    \ neg(x))\n        \"\"\"\n\n        self.op=op\n        self.zero=zero\n    \
    \    self.neg=neg\n\n        self.H=H=len(M)\n        self.W=W=len(M[0]) if self.H\
    \ else 0\n\n        X=[[zero]*(W+1) for _ in range(H+1)]\n\n        for i in range(H):\n\
    \            Mi=M[i]\n            for j in range(W):\n                alpha=Mi[j]\n\
    \n                a=i+1\n                while a<=H:\n                    Xa=X[a]\n\
    \                    b=j+1\n                    while b<=W:\n                \
    \        Xa[b]=op(Xa[b], alpha)\n                        b+=b&(-b)\n         \
    \           a+=a&(-a)\n        self.data=X\n\n    def get(self, i, j):\n     \
    \   \"\"\" \u7B2C (i,j) \u8981\u7D20\u306E\u5024\u3092\u51FA\u529B\u3059\u308B\
    .\n        (i,j)   : \u6570\u5217\u306E\u8981\u7D20\n        \"\"\"\n        return\
    \ self.sum(i,j,i,j)\n\n    def add(self, i, j, x):\n        \"\"\" \u7B2C (i,j)\
    \ \u8981\u7D20\u306B x \u3092\u52A0\u3048, \u66F4\u65B0\u3092\u884C\u3046.\n \
    \       (i,j): \u6570\u5217\u306E\u8981\u7D20\n        x    : \u52A0\u3048\u308B\
    \u5024\n        \"\"\"\n        H=self.H; W=self.W\n        if (i<0) or (i>=H)\
    \ or (j<0) or (j>=W):\n            return\n\n        X=self.data; op=self.op\n\
    \        a=i+1\n        while a<=H:\n            Xa=X[a]\n            b=j+1\n\
    \            while b<=W:\n                Xa[b]=op(Xa[b], x)\n               \
    \ b+=b&(-b)\n            a+=a&(-a)\n\n    def update(self, i, j, x):\n       \
    \ \"\"\" \u7B2C (i,j) \u8981\u7D20\u3092 x \u306B\u5909\u3048, \u66F4\u65B0\u3092\
    \u884C\u3046.\n        (i,j): \u6570\u5217\u306E\u8981\u7D20\n        x: \u66F4\
    \u65B0\u5F8C\u306E\u5024\n        \"\"\"\n\n        a=self.get(i,j)\n        y=self.op(self.neg(a),x)\n\
    \        self.add(i,j,y)\n\n    def sum(self, i0, j0, i1, j1):\n        \"\"\"\
    \ sum_{i0<=x<=i1, j0<=y<=j1} B[x][y] \u3092\u6C42\u3081\u308B.\n        \"\"\"\
    \n\n        if (i0>i1) or (j0>j1):\n            return self.zero\n\n        op=self.op;\
    \ neg=self.neg; box=self.__box\n\n        a=op(box(i1,j1), box(i0-1, j0-1))\n\
    \        b=op(box(i1,j0-1), box(i0-1, j1))\n        return op(a,neg(b))\n\n  \
    \  def __box(self, i, j):\n        \"\"\" sum_{0<=x<=i, 0<=y<=j} B[x][y] \u3092\
    \u6C42\u3081\u308B.\"\"\"\n\n        if (i<0) or (j<0):\n            return self.zero\n\
    \n        H=self.H; W=self.W\n        X=self.data; op=self.op\n\n        i=min(i,H-1);\
    \ j=min(j, W-1)\n\n        total=self.zero\n\n        a=i+1\n        while a>0:\n\
    \            Xa=X[a]\n            b=j+1\n            while b>0:\n            \
    \    total=op(total, Xa[b])\n                b-=b&(-b)\n            a-=a&(-a)\n\
    \        return total\n\n    def all_sum(self):\n        return self.sum(0, 0,\
    \ self.H-1, self.W-1)\n\n    def __getitem__(self,index):\n        if isinstance(index,int):\n\
    \            return [self.get(index, j) for j in range(self.W)]\n        elif\
    \ isinstance(index, tuple) and len(index)==2:\n            i,j=index\n       \
    \     return self.get(i,j)\n\n    def __setitem__(self, index, value):\n     \
    \   self.update(*index,value)\n"
  dependsOn: []
  isVerificationFile: false
  path: Binary_Indexed_Tree/Binary_Indexed_Tree_2D.py
  requiredBy: []
  timestamp: '2023-03-20 03:47:37+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Binary_Indexed_Tree/Binary_Indexed_Tree_2D.py
layout: document
redirect_from:
- /library/Binary_Indexed_Tree/Binary_Indexed_Tree_2D.py
- /library/Binary_Indexed_Tree/Binary_Indexed_Tree_2D.py.html
title: Binary_Indexed_Tree/Binary_Indexed_Tree_2D.py
---
