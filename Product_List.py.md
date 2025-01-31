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
  code: "class Product_List_2D:\n    def __init__(self, default, H, W):\n        \"\
    \"\" H x W \u306E\u76F4\u7A4D\u30EA\u30B9\u30C8\u3092\u751F\u6210\u3059\u308B\
    . \"\"\"\n\n        self.H=H\n        self.W=W\n        self.list=[default]*(H*W)\n\
    \n    def __len__(self):\n        return self.H*self.W\n\n    def get(self, i,\
    \ j):\n        if i<0:\n            i+=self.H\n\n        if j<0:\n           \
    \ j+=self.W\n\n        return self.list[i*self.W+j]\n\n    def get_all(self):\n\
    \        return [self.list[i*self.W: (i+1)*self.W] for i in range(self.H)]\n\n\
    \    def projection_H(self, i):\n        if i<0:\n            i+=self.H\n\n  \
    \      return self.list[i*self.W: (i+1)*self.W]\n\n    def set(self, i, j, value):\n\
    \        if i<0:\n            i+=self.H\n\n        if j<0:\n            j+=self.W\n\
    \n        self.list[i*self.W+j]=value\n\n    def set_once(self, i, A):\n     \
    \   if i<0:\n            i+=self.H\n\n        index=i*self.W\n        for j in\
    \ range(self.W):\n            self.list[index]=A[j]\n            index+=1\n\n\
    \    def __getitem__(self, index):\n        return self.get(index[0], index[1])\n\
    \n    def __setitem__(self, index, value):\n        self.set(index[0], index[1],\
    \ value)\n\n    def __repr__(self):\n        return \"[Product List 2D] : Height:\
    \ {}, Width: {}\".format(self.H, self.W)\n\nclass Product_List_3D:\n    def __init__(self,\
    \ default, H, W, D):\n        \"\"\" H x W x D \u306E\u76F4\u7A4D\u30EA\u30B9\u30C8\
    \u3092\u751F\u6210\u3059\u308B. \"\"\"\n\n        self.H=H\n        self.W=W\n\
    \        self.D=D\n        self.list=[default]*(H*W*D)\n\n    def __len__(self):\n\
    \        return self.H*self.W*self.D\n\n    def get(self, i, j, k):\n        if\
    \ i<0:\n            i+=self.H\n\n        if j<0:\n            j+=self.W\n\n  \
    \      if k<0:\n            k+=self.D\n\n        return self.list[(i*self.W+j)*self.D+k]\n\
    \n    def get_all(self):\n        return [[[self.get(i,j,k) for k in range(self.D)]\
    \ for j in range(self.W)] for i in range(self.H)]\n\n    def projection_H(self,\
    \ i):\n        if i<0:\n            i+=self.H\n\n        return [self.projection_HW(i,j)\
    \ for j in range(self.W)]\n\n    def projection_HW(self, i, j):\n        if i<0:\n\
    \            i+=self.H\n\n        if j<0:\n            j+=self.W\n\n        start=(i*self.W+j)*self.D\n\
    \        return self.list[start: start+self.D]\n\n    def set(self, i, j, k, value):\n\
    \        if i<0:\n            i+=self.H\n\n        if j<0:\n            j+=self.W\n\
    \n        if k<0:\n            k+=self.D\n\n        self.list[(i*self.W+j)*self.D+k]=value\n\
    \n    def set_once(self, i, j, A):\n        if i<0:\n            i+=self.H\n\n\
    \        if j<0:\n            j+=self.W\n\n        index=(i*self.W+j)*self.D\n\
    \        for j in range(self.D):\n            self.list[index]=A[j]\n        \
    \    index+=1\n\n    def __getitem__(self, index):\n        return self.get(index[0],\
    \ index[1], index[2])\n\n    def __setitem__(self, index, value):\n        self.set(index[0],\
    \ index[1], index[2], value)\n\n    def __repr__(self):\n        return \"[Product\
    \ List 3D] : Height: {}, Width: {}, Depth: {}\".format(self.H, self.W, self.D)\n\
    \nclass Product_List_4D:\n    def __init__(self, default, H, W, D, T):\n     \
    \   \"\"\" H x W x D x T \u306E\u76F4\u7A4D\u30EA\u30B9\u30C8\u3092\u751F\u6210\
    \u3059\u308B. \"\"\"\n\n        self.H=H\n        self.W=W\n        self.D=D\n\
    \        self.T=T\n        self.list=[default]*(H*W*D*T)\n\n    def __len__(self):\n\
    \        return self.H*self.W*self.D*self.T\n\n    def get(self, i, j, k, l):\n\
    \        if i<0:\n            i+=self.H\n\n        if j<0:\n            j+=self.W\n\
    \n        if k<0:\n            k+=self.D\n\n        if l<0:\n            l+=self.T\n\
    \n        return self.list[((i*self.W+j)*self.D+k)*self.T+l]\n\n    def get_all(self):\n\
    \        return [[[[self.get(i,j,k,l) for l in range(self.T)] for k in range(self.D)]\
    \ for j in range(self.W)] for i in range(self.H)]\n\n    def set(self, i, j, k,\
    \ l, value):\n        if i<0:\n            i+=self.H\n\n        if j<0:\n    \
    \        j+=self.W\n\n        if k<0:\n            k+=self.D\n\n        if l<0:\n\
    \            l+=self.T\n\n        self.list[((i*self.W+j)*self.D+k)*self.T+l]=value\n\
    \n    def set_once(self, i, j, k, A):\n        if i<0:\n            i+=self.H\n\
    \n        if j<0:\n            j+=self.W\n\n        if k<0:\n            k+=self.D\n\
    \n        index=((i*self.W+j)*self.D+k)*self.T\n        for j in range(self.T):\n\
    \            self.list[index]=A[j]\n            index+=1\n\n    def __getitem__(self,\
    \ index):\n        return self.get(index[0], index[1], index[2], index[3])\n\n\
    \    def __setitem__(self, index, value):\n        self.set(index[0], index[1],\
    \ index[2], index[3], value)\n\n    def __repr__(self):\n        return \"[Product\
    \ List 4D] : Height: {}, Width: {}, Depth: {}, Time: {}\".format(self.H, self.W,\
    \ self.D, self.T)\n"
  dependsOn: []
  isVerificationFile: false
  path: Product_List.py
  requiredBy: []
  timestamp: '2022-12-14 18:54:57+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Product_List.py
layout: document
redirect_from:
- /library/Product_List.py
- /library/Product_List.py.html
title: Product_List.py
---
