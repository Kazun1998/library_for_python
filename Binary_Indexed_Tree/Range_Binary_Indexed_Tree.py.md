---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Binary_Indexed_Tree/Binary_Indexed_Tree.py
    title: Binary Indexed Tree (Fenwick Tree)
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from Binary_Indexed_Tree import Binary_Indexed_Tree\n\nclass Range_Binary_Indexed_Tree():\n\
    \    def __init__(self, L, calc, unit, inv, mul, index=1):\n        \"\"\" calc\
    \ \u3092\u6F14\u7B97\u3068\u3059\u308B N \u9805\u306E Binary Indexed Tree (\u533A\
    \u9593\u4F5C\u7528\u4ED8\u304D) \u3092\u4F5C\u6210\n        calc: \u6F14\u7B97\
    \ (2\u5909\u6570\u95A2\u6570, \u53EF\u63DB\u7FA4)\n        unit: \u7FA4 calc \u306E\
    \u5358\u4F4D\u5143 (x+e=e+x=x\u3092\u6E80\u305F\u3059e)\n        inv : \u7FA4\
    \ calc \u306E\u9006\u5143 (1\u5909\u6570\u95A2\u6570, x+inv(x)=inv(x)+x=e \u3092\
    \u307F\u305F\u3059 inv(x))\n        mul: r \u3092\u6574\u6570, x \u3092\u53EF\u63DB\
    \u7FA4\u306E\u5143\u3068\u3057\u305F\u3068\u304D\u306E mul(r,x):=r*x\n       \
    \ \"\"\"\n\n        self.bit0=Binary_Indexed_Tree(L, calc, unit, inv, index)\n\
    \n        self.calc=calc\n        self.unit=unit\n        self.inv=inv\n     \
    \   self.mul=mul\n        self.index=index\n\n        self.num=self.bit0.num\n\
    \        self.depth=self.bit0.depth\n\n        self.bit1=Binary_Indexed_Tree([unit]*self.num,\
    \ calc, unit, inv, index)\n\n    def index_number(self, k, index=1):\n       \
    \ \"\"\" \u7B2C k \u8981\u7D20\u306E\u5024\u3092\u51FA\u529B\u3059\u308B.\n  \
    \      k    : \u6570\u5217\u306E\u8981\u7D20\n        index: \u5148\u982D\u306E\
    \u8981\u7D20\u306E\u756A\u53F7\n        \"\"\"\n        return self.sum(k,k,index)\n\
    \n    def add(self, k, x, index=1):\n        \"\"\" \u7B2C k \u8981\u7D20\u306B\
    \ x \u3092\u52A0\u3048, \u66F4\u65B0\u3092\u884C\u3046.\n        k    : \u6570\
    \u5217\u306E\u8981\u7D20\n        x    : \u52A0\u3048\u308B\u5024\n        index:\
    \ \u5148\u982D\u306E\u8981\u7D20\u306E\u756A\u53F7\n        \"\"\"\n\n       \
    \ self.bit0.add(k,x,index)\n\n    def add_range(self, l, r, x, index=1):\n   \
    \     \"\"\" \u7B2C l \u8981\u7D20\u304B\u3089\u7B2C r \u8981\u7D20\u5168\u3066\
    \u306B x \u3092\u52A0\u3048, \u66F4\u65B0\u3092\u884C\u3046.\n        l,r: \u66F4\
    \u65B0\u306E\u7BC4\u56F2\n        x: \u52A0\u7B97\u3059\u308B\u5024\n        index:\
    \ \u5148\u982D\u306E\u8981\u7D20\u306E\u756A\u53F7\n        \"\"\"\n        l=max(1,l+(1-index))\n\
    \        r=min(self.num,r+(1-index))\n\n        inv=self.inv; mul=self.mul\n\n\
    \        self.bit0.add(l, inv(mul(l-1,x)),index)\n        self.bit1.add(l, x,\
    \ index)\n\n        if r<self.index+self.num-1:\n            self.bit0.add(r+1,\
    \ mul(r,x), index)\n            self.bit1.add(r+1, inv(x), index)\n\n    def update(self,\
    \ k, x, index=1):\n        \"\"\" \u7B2C k \u8981\u7D20\u3092 x \u306B\u5909\u3048\
    , \u66F4\u65B0\u3092\u884C\u3046.\n        k: \u6570\u5217\u306E\u8981\u7D20\n\
    \        x: \u66F4\u65B0\u5F8C\u306E\u5024\n        \"\"\"\n\n        self.bit0.update(k,x,index)\n\
    \n    def sum(self, l, r, index=1):\n        \"\"\" \u7B2C l \u8981\u7D20\u304B\
    \u3089\u7B2C r \u8981\u7D20\u307E\u3067\u306E\u7DCF\u548C\u3092\u6C42\u3081\u308B\
    .\n        \u203B l != index \u306A\u3089\u3070, \u7FA4\u3067\u306A\u304F\u3066\
    \u306F\u306A\u3089\u306A\u3044.\n        l : \u59CB\u307E\u308A\n        r   :\
    \ \u7D42\u308F\u308A\n        index: \u5148\u982D\u306E\u8981\u7D20\u306E\u756A\
    \u53F7\n        \"\"\"\n        alpha=max(1, l+(1-index))\n        beta=min(self.num,\
    \ r+(1-index))\n\n        Y=self.bit0.sum(1,beta,1)+self.bit1.sum(1,beta,1)*beta\n\
    \n        if alpha==1:\n            return Y\n        else:\n            X=self.bit0.sum(1,\
    \ alpha-1,1)+self.bit1.sum(1, alpha-1,1)*(alpha-1)\n            return self.calc(self.inv(X),Y)\n\
    \n    def all_sum(self):\n        return self.bit0.data[-1]+self.bit1.data[-1]*self.num\n\
    \n    def binary_search(self, cond, index=1):\n        \"\"\" cond(B[1]+...+B[k])\
    \ \u3092\u6E80\u305F\u3059\u6700\u5C0F\u306E k \u3092\u8FD4\u3059.\n\n       \
    \ cond: \u5358\u8ABF\u5897\u52A0\n\n        \u203B cond(uint)=True \u306E\u5834\
    \u5408\u306E\u8FD4\u308A\u5024\u306F index-1\n        \u203B cond(B[1]+...+B[k])\
    \ \u306A\u308B k \u304C\u5B58\u5728\u3057\u306A\u3044\u5834\u5408\u306E\u8FD4\u308A\
    \u5024\u306F self.num+index\n        \"\"\"\n\n        pass\n\n    def __getitem__(self,index):\n\
    \        if isinstance(index,int):\n            return self.index_number(index,self.index)\n\
    \        else:\n            return [self.index_number(t,self.index) for t in index]\n\
    \n    def __setitem__(self,index,val):\n        self.update(index,val,self.index)\n\
    \nfrom operator import add,neg,mul\nB=Range_Binary_Indexed_Tree([0]*10, add, 0,\
    \ neg, mul ,1)\n\n"
  dependsOn:
  - Binary_Indexed_Tree/Binary_Indexed_Tree.py
  isVerificationFile: false
  path: Binary_Indexed_Tree/Range_Binary_Indexed_Tree.py
  requiredBy: []
  timestamp: '2023-03-20 03:47:37+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Binary_Indexed_Tree/Range_Binary_Indexed_Tree.py
layout: document
redirect_from:
- /library/Binary_Indexed_Tree/Range_Binary_Indexed_Tree.py
- /library/Binary_Indexed_Tree/Range_Binary_Indexed_Tree.py.html
title: Binary_Indexed_Tree/Range_Binary_Indexed_Tree.py
---
