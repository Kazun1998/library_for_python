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
  code: "class Sparse_Binary_Indexed_Tree():\n    def __init__(self, N, calc, unit,\
    \ inv, index=1):\n        \"\"\" calc \u3092\u6F14\u7B97\u3068\u3059\u308B\u6700\
    \u9AD8\u306E\u6DFB\u5B57\u304C N \u306B\u306A\u308B\u3088\u3046\u306A Sparse Binary\
    \ Indexed Tree \u3092\u4F5C\u6210\n        calc: \u6F14\u7B97 (2\u5909\u6570\u95A2\
    \u6570, \u53EF\u63DB\u7FA4)\n        unit: \u7FA4 calc \u306E\u5358\u4F4D\u5143\
    \ (x+e=e+x=x\u3092\u6E80\u305F\u3059e)\n        inv : \u7FA4 calc \u306E\u9006\
    \u5143 (1\u5909\u6570\u95A2\u6570, x+inv(x)=inv(x)+x=e \u3092\u307F\u305F\u3059\
    \ inv(x))\n        \"\"\"\n        self.calc=calc\n        self.unit=unit\n  \
    \      self.inv=inv\n        self.index=index\n\n        d=max(1,(N+(1-index)-1).bit_length())\n\
    \        k=2**d\n\n        self.num=k\n        self.depth=d\n        self.data={}\n\
    \n    def index_number(self, k, index=1):\n        \"\"\" \u7B2C k \u8981\u7D20\
    \u306E\u5024\u3092\u51FA\u529B\u3059\u308B.\n        k    : \u6570\u5217\u306E\
    \u8981\u7D20\n        index: \u5148\u982D\u306E\u8981\u7D20\u306E\u756A\u53F7\n\
    \        \"\"\"\n        return self.sum(k,k,index)\n\n    def add(self, k, x,\
    \ index=1):\n        \"\"\" \u7B2C k \u8981\u7D20\u306B x \u3092\u52A0\u3048,\
    \ \u66F4\u65B0\u3092\u884C\u3046.\n        k    : \u6570\u5217\u306E\u8981\u7D20\
    \n        x    : \u52A0\u3048\u308B\u5024\n        index: \u5148\u982D\u306E\u8981\
    \u7D20\u306E\u756A\u53F7\n        right:\u300C\u5DE6\u304B\u3089\u300D\u304C\u300C\
    \u53F3\u304B\u3089\u300D\u306B\u306A\u308B\n        \"\"\"\n        p=k+(1-index)\n\
    \        while p<=self.num:\n            self.data[p]=self.calc(self.data.get(p,self.unit),x)\n\
    \            p+=p&(-p)\n\n    def update(self, k, x, index=1):\n        \"\"\"\
    \ \u7B2C k \u8981\u7D20\u3092 x \u306B\u5909\u3048, \u66F4\u65B0\u3092\u884C\u3046\
    .\n        k: \u6570\u5217\u306E\u8981\u7D20\n        x: \u66F4\u65B0\u5F8C\u306E\
    \u5024\n        \"\"\"\n\n        a=self.index_number(k,index)\n        y=self.calc(self.inv(a),x)\n\
    \n        self.add(k,y,index)\n\n    def sum(self, From, To, index=1):\n     \
    \   \"\"\" \u7B2C From \u8981\u7D20\u304B\u3089\u7B2C To \u8981\u7D20\u307E\u3067\
    \u306E\u7DCF\u548C\u3092\u6C42\u3081\u308B.\n        \u203BFrom!=1\u3092\u4F7F\
    \u3046\u306A\u3089\u3070, \u7FA4\u3067\u306A\u304F\u3066\u306F\u306A\u3089\u306A\
    \u3044.\n        From : \u59CB\u307E\u308A\n        To   : \u7D42\u308F\u308A\n\
    \        index: \u5148\u982D\u306E\u8981\u7D20\u306E\u756A\u53F7\n        \"\"\
    \"\n        alpha=max(1,From+(1-index))\n        beta=min(self.num,To+(1-index))\n\
    \n        if alpha>beta:\n            return self.unit\n        elif alpha==1:\n\
    \            return self.__section(beta)\n        else:\n            return self.calc(self.inv(self.__section(alpha-1)),self.__section(beta))\n\
    \n    def __section(self,x):\n        \"\"\" B[1]+...+B[x] \u3092\u6C42\u3081\u308B\
    . \"\"\"\n        S=self.unit\n        while x:\n            S=self.calc(self.data.get(x,self.unit),S)\n\
    \            x-=x&(-x)\n        return S\n\n    def all_sum(self):\n        return\
    \ self.data.get(self.num,self.unit)\n\n    def binary_search(self, cond, index=1):\n\
    \        \"\"\" cond(B[1]+...+B[k]) \u3092\u6E80\u305F\u3059\u6700\u5C0F\u306E\
    \ k \u3092\u8FD4\u3059.\n\n        cond: \u5358\u8ABF\u5897\u52A0\n\n        \u203B\
    \ cond(uint)=True \u306E\u5834\u5408\u306E\u8FD4\u308A\u5024\u306F index-1\n \
    \       \u203B cond(B[1]+...+B[k]) \u306A\u308B k \u304C\u5B58\u5728\u3057\u306A\
    \u3044\u5834\u5408\u306E\u8FD4\u308A\u5024\u306F self.num+index\n        \"\"\"\
    \n\n        if cond(self.unit):\n            return index-1\n\n        j=0\n \
    \       r=self.num\n        t=r\n        data=self.data\n        alpha=self.unit\n\
    \n        for _ in range(self.depth+1):\n            if j+t<=self.num:\n     \
    \           beta=self.calc(alpha,data.get(j+t,self.unit))\n                if\
    \ not cond(beta):\n                    alpha=beta\n                    j+=t\n\
    \            t>>=1\n\n        return j+index\n\n    def __getitem__(self,index):\n\
    \        if isinstance(index,int):\n            return self.index_number(index,self.index)\n\
    \        else:\n            return [self.index_number(t,self.index) for t in index]\n\
    \n    def __setitem__(self,index,val):\n        self.update(index,val,self.index)\n"
  dependsOn: []
  isVerificationFile: false
  path: Binary_Indexed_Tree/Sparse_Binary_Indexed_Tree.py
  requiredBy: []
  timestamp: '2022-09-10 17:06:43+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Binary_Indexed_Tree/Sparse_Binary_Indexed_Tree.py
layout: document
redirect_from:
- /library/Binary_Indexed_Tree/Sparse_Binary_Indexed_Tree.py
- /library/Binary_Indexed_Tree/Sparse_Binary_Indexed_Tree.py.html
title: Binary_Indexed_Tree/Sparse_Binary_Indexed_Tree.py
---
